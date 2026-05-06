---
aid: google-cloud-kms
name: Google Cloud KMS
description: Google Cloud Key Management Service (KMS) allows you to create, import, and manage cryptographic keys and perform cryptographic operations in a central cloud service. It supports encryption, decryption, signing, and verification using symmetric and asymmetric keys for securing data and workloads.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-kms/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Cryptography
  - Encryption
  - Google Cloud
  - Key Management
  - KMS
  - Security
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
common:
  - type: Portal
    url: https://cloud.google.com/kms
  - type: Getting Started
    url: https://cloud.google.com/kms/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/kms/docs
  - type: Authentication
    url: https://cloud.google.com/kms/docs/iam
  - type: Pricing
    url: https://cloud.google.com/kms/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/kms/docs/support
  - type: JSONLDContext
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
