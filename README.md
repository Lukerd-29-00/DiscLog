# Overview
This is a simple project designed to calculate discrete logarithms in multiplicitive groups modulo some number via the <a href="https://en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm">Pohlig Hellman algorithm</a>. It works best when the modulus is a smooth integer; i.e. it has a lot of small prime factors. This is mostly so that you don't have to download all of sagemath to do this one pretty simple thing, and Alperton's calculator has been having some issues.

# Usage
Just import the package and call the pohligH function with the base, the power, the modulus, and the pre-computed factors of phi. The primitives package also comes with a CRT function if you need it.

## Factorization
I didn't implement a factorization for large integers in this library, because I don't hate myself quite that much. I recommend <a href="https://www.alpertron.com.ar/ECM.HTM">This factorization calculator</a>, which should handle any reasonable number you give it. The pohligh module comes with a get_factors function for parsing the output of this calculator. You just need to get the factorization in the right format by clicking the share button near the bottom.

# Licensing
This is an MIT license. Don't worry, I'm not going to sue you for using the project I did in a day. I promise. I have a License file in the src branch if you really need it, for some reason.