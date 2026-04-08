---
aid: google-cloud-kms
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-kms/refs/heads/main/apis.yml
apis:
- name: Google Cloud KMS API
  description: The Cloud KMS API enables creating and managing cryptographic keys, key rings, and crypto key versions, and performing encrypt, decrypt, sign, and verify operations.
  humanURL: https://cloud.google.com/kms
  baseURL: https://cloudkms.googleapis.com
  tags:
  - Cryptography
  - Encryption
  - Keys
  - KMS
  properties:
  - type: Documentation
    url: https://cloud.google.com/kms/docs/reference/rest
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/kms/docs/iam
  - type: Getting Started
    url: https://cloud.google.com/kms/docs/quickstart
  - type: JSONSchema
    url: json-schema/crypto-key.json
  - type: JSONLDContext
    url: json-ld/context.jsonld
name: Google Cloud KMS
tags:
- Cryptography
- Encryption
- Google Cloud
- Key Management
- KMS
- Security
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Key Management Service (KMS) allows you to create, import, and manage cryptographic keys and perform cryptographic operations in a central cloud service. It supports encryption, decryption, signing, and verification using symmetric and asymmetric keys for securing data and workloads.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

