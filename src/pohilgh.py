import math
import typing
import re
import primitives

def pohligH(base: int, power: int, modulus,phiFactors: typing.Iterable[typing.Tuple[int, int]])->int:
    #Make sure that the base actually generates a cyclic group to begin with.
    assert math.gcd(base,modulus) == 1
    #Make sure the order of the group generated by base is correct.
    assert pow(base,primitives.order(base,modulus,phiFactors),modulus) == 1
    #Get the prime factorization of the order of the group generated by base.
    oFactors = primitives.orderFactors(base,modulus,phiFactors)
    base_order = primitives.order(base,modulus,phiFactors)
    def solve_for_prime(generator: int,prime: int,exponent: int,h: int)->int:
        x = 0
        gamma = pow(generator,prime ** (exponent - 1),modulus)
        gInv = primitives.inverse(generator,modulus)
        for k in range(exponent):
            h0 = pow(pow(gInv,x,modulus)*h,pow(prime,exponent-1-k),modulus)
            d = None
            for y in range(prime):
                if pow(gamma,y,modulus) == h0:
                    d = y
                    break
            assert d != None
            x += prime**k*d
            x %= modulus
        return x
    #Calculates the values of base and power for each group of order prime**exp in the factorization of the group order.
    pohlig_component = lambda target, prime, exponent: pow(target,base_order//(prime**exponent),modulus)
    congruences = [(solve_for_prime(pohlig_component(base,prime,exp),prime,exp,pohlig_component(power,prime,exp)),prime**exp) for prime, exp in oFactors]
    return primitives.CRT(*congruences)

factorsRe = r"([0-9]+)(?:\^([0-9]+))?"

def get_factors(factorsStr: str)->typing.Iterable[typing.Tuple[int,int]]:
    try:
        return [(int(p), int(e or "1")) for p, e in re.findall(factorsRe,factorsStr)]
    except TypeError:
        raise ValueError("Couldn't find factors in that string.")

if __name__ == "__main__":
    phi = 447547859673081522838818585882585728821124568961264884315519211488721582296631456321194919220282793237136779462667899249348754076655821005337793668370131460403938453342829518965538341303424783568254583317982352291547212957599525343932219674311676158425505333457715200000000000000000000000000000000000000
    phiFactorsStr = "2^250 × 3^91 × 5^38 × 7^23 × 11^14 × 13^11 × 17^8 × 19^6 × 23^6 × 29^4 × 31^3 × 37^3 × 41 × 43^2 × 47^2 × 53 × 59 × 61^2 × 67 × 71 × 73^2 × 79 × 83^2 × 89 × 97 × 101 × 103 × 107 × 113 × 127 × 131 × 139 × 163 × 173 × 179 × 191 × 233 × 239 × 251 × 281 × 293 × 359"
    p = 0xf6c6d4d9e03b8d02e7a525366e6a811d8558fbde1368904742a82e376b2511b48108be0dddb3fbb8fefb22cd66e158ac684a98e09d122ce37cda9574f2fc62f6fb1b99d6663a8db8380391b35653b87991279b3a296a774d18ec18d42169ee67d4f21ba9b3f39cdced3a0584177aa6639a70f48622b719a4952ddb4decf3
    power = pow(2,65537,p)
    base = 2
    phiFactors = get_factors(phiFactorsStr)
    assert pohligH(base,power,p,phiFactors) == 65537