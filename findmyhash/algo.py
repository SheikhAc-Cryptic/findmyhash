from enum import Enum

class Algo(Enum):
    MD2         =   "md2"
    MD4         =   "md4"
    MD5 	    =   "md5"
    SHA1 	    =   "sha1"
    SHA224	    =   "sha224"
    SHA256 	    =   "sha256"
    SHA384	    =   "sha384"
    SHA512 	    =   "sha512"
    RIPEMD128	=   "ripemd128"
    RIPEMD160	=   "ripemd160"
    RIPEMD256	=   "ripemd256"
    RIPEMD320	=   "ripemd320"
    LM          =   "lm"
    NTLM	    =   "ntlm"
    MYSQL	    =   "mysql"
    CISCO7	    =   "cisco7"
    JUNIPER     =   "juniper"
    GOST	    =   "gost"
    WHIRLPOOL   =   "whirlpool"
    SNEFRU      =   "snefru"
    SNEFRU256   =   "snefru256"
    LDAP_MD5    =   "ldap_md5"
    LDAP_SHA1   =   "ldap_sha1"