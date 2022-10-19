import functools
import typing
import itertools
import egcd

def orderFactors(g: int, p: int, phiFactorization: typing.List[typing.Tuple[int,int]])->typing.Iterable[typing.Tuple[int,int]]:
    phi = functools.reduce(lambda x, y: x * y[0]**y[1],itertools.chain([1],phiFactorization))
    for prime, exp in phiFactorization:
        for i in range(1,exp+1):
            if pow(g,phi//(prime**i),p) != 1:
                #If pow(g,phi//(prime**i),p) != 1, we know prime**i | ord(<g>)
                yield (prime,exp-i+1)
                break

def order(g: int, p: int, phiFactorization: typing.List[typing.Tuple[int,int]])->int:
    return functools.reduce(lambda x, y: x*y[0]**y[1],itertools.chain([1],orderFactors(g,p,phiFactorization)))

def CRT(*args: typing.List[typing.Tuple[int,int]])->int:
    def _CRT_Pair(a1,n1,a2,n2):
        m1, m2 = egcd.egcd(n1,n2)[1:]
        return (a1*m2*n2 + a2*m1*n1) % (n1*n2), n1*n2
    return functools.reduce(lambda t1, t2: _CRT_Pair(*t1,*t2),args)[0]

def inverse(x: int,modulus: int)->int:
    a, n1 = egcd.egcd(x,modulus)[:2]
    if a != 1:
        raise ValueError(f"{x} is not coprime to {modulus}!")
    return n1