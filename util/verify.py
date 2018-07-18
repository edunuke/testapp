# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 11:07:09 2018

@author: eduperez
"""
#%%
from pathlib import Path
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


with open(Path.cwd()
              .joinpath('Desktop')
              .joinpath('walletapi')
              .joinpath('btcvalidator')
              .joinpath('app')
              .joinpath('utils')
              .joinpath('pub').with_suffix('.pem'),'rb') as file:
    pub_key = RSA.importKey(file.read())
# Read shared key from file
with open(Path.cwd()
              .joinpath('Desktop')
              .joinpath('walletapi')
              .joinpath('btcvalidator')
              .joinpath('app')
              .joinpath('utils')
              .joinpath('priv').with_suffix('.pem'),'rb') as file:
    private_key = RSA.importKey(file.read())
    
#%%
message = "getcredentials"
digest = SHA256.new()
digest.update(message.encode('utf-8'))
#%%
# Load private key and sign message
signer = PKCS1_v1_5.new(private_key)
signed_message = signer.sign(digest)
#%%


# Load public key and verify message
verifier = PKCS1_v1_5.new(pub_key.publickey())
verified = verifier.verify(digest, signed_message)


#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\pubmessage.txt', 'w') as file:
    file.write(signed_message.hex())

#%%
with open('C:\\Users\\eduperez\\Desktop\\walletapi\\btcapi\\app\\pubmessage.txt', 'r') as file:
    a = file.readlines()[0]
#%%

from bottle import route






