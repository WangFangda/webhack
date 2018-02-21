# Ciphers and algorithms

## Symmetric Encryption
* For authenticated encryption:  
  [XSalsa20Poly1305](https://download.libsodium.org/doc/secret-key_cryptography/authenticated_encryption.html) 
  (a.k.a. crypto_secretbox) for Authenticated Encryption. Note the X in the
  beginning of the name. The version without the X is faster, but unsafe for
  use with random nonce - the nonce number must be an incrementing counter,
  and there must be security precautions taken against nonce reuse.

* For AEAD (Authenticated Encryption with Additional Data):  
  [XChaCha20-Poly1305](https://download.libsodium.org/doc/secret-key_cryptography/xchacha20-poly1305_construction.html) 
  in IETF-compatible construction. Note the X in the beginning of the name.

## Hashing and Authentication
* For general hashing and integrity checks (not authentication):  
  SHA-256, SHA-512, SHA-512/256 or [Blake2b](https://download.libsodium.org/doc/hashing/generic_hashing.html)

* For message authentication and symmetric digital signatures:  
  HMAC-SHA256, HMAC-SHA512(/256) or Blake2b

* For password hashing:
  Currently [scrypt](https://download.libsodium.org/doc/password_hashing/scrypt.html),
  but be ready to switch to [Argon2](https://download.libsodium.org/doc/password_hashing/the_argon2i_function.html)
  once it stabilizes. If you need to use Argon2 now, make sure you're using
  Argon2id with the latest algorithm version (v1.3 as of the time of this
  writing).

## Asymmetric Encryption and Signature
* For Asymmetric Key Exchange (Diffie-Hellman):  
  Curve25519 (X25519), [crypto_kx](https://download.libsodium.org/doc/key_exchange/) in libsodium

* For Public-key Signature:  
  Ed25519
  [crypto_sign](https://download.libsodium.org/doc/public-key_cryptography/public-key_signatures.html) in libsodium

* For Asymmetric Encryption:  
  Curve225519 + XSalsa20-Poly1305
  [crypto_box](https://download.libsodium.org/doc/public-key_cryptography/authenticated_encryption.html) in libsodium

## Random Number Generator
* On Linux and Mac [use from /dev/urandom](https://www.2uo.de/myths-about-urandom/).
  You don't need to use any library, just open it as a file and read to your
  heart's content.
* In browser-side JS, your best bet is [`window.crypto.getRandomValues()`](https://developer.mozilla.org/en-US/docs/Web/API/RandomSource/getRandomValues).
* Java is a mess, like always, because Oracle is embarrassingly clueless about
  cryptography:
  http://www.thezonemanager.com/2015/07/whats-so-special-about-devurandom.html
  https://security.stackexchange.com/questions/14386/what-do-i-need-to-configure-to-make-sure-my-software-uses-dev-urandom

# Libraries
* libsodium and its [bindings](https://download.libsodium.org/doc/bindings_for_other_languages/). This should always be your top choice.
* TweetNacl ports are a mixed bag - make sure they are maintained and audited.
  Unfortunately, sometimes you don't have any other choice, since you can't
  use a native library like libsodium.
* OpenSSL, BoringSSL or LibreSSL. The later two have less bugs, but are harder
  to integrate.
* The Go standard library and `golang.org/x/crypto` is generally very solid
  and contains good implementations of the NaCl ciphers and Blake2b.

# Learning materials

* [the cryptopals crypto challenges](https://cryptopals.com)
* [Standford's Cryptograhy I and II by Dan Boneh on Coursera](https://www.coursera.org/instructor/~774)
* Cryptography Engineering by Ferguson, Schneier, and Kohno
* https://www.crypto101.io/ - 100% up to date, but incomplete

# Advice
* [Cryptogpraic Best Practices](https://gist.github.com/atoponce/07d8d4c833873be2f68c34f9afc5a78a)
  Nicely formatted fork of tptacek's cryptographic right answers. I disagree
  on the risk of implementing AES-CTR+HMAC vs. AES-GCM incorrectly (I've seen
  implementations of both by inexperienced engineers and I believe it's easier
  to mess up GCM). In any case, AES-GCM is only 3rd place - you should really
  use libsodium and avoid all NIST standards except SHA-2.
* Ask on [Cryptoraphy Stack Exchange](https://crypto.stackexchange.com/)




![img](img.png)

