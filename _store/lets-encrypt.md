---
aid: lets-encrypt
name: Let's Encrypt
description: Let's Encrypt is a free, automated, and open certificate authority run by the Internet Security Research Group affiliated with the Linux Foundation. It provides TLS certificates to secure the web, having issued billions of certificates to enable HTTPS for websites worldwide via the ACME protocol.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Certificates
  - Linux Foundation
  - Security
  - TLS
  - ACME
  - PKI
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/lets-encrypt/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lets-encrypt:lets-encrypt-acme-api
    name: Let's Encrypt ACME API
    description: The ACME (Automatic Certificate Management Environment) protocol API, defined by RFC 8555, used by Let's Encrypt to automate the issuance, renewal, and revocation of free TLS/SSL certificates that secure websites with HTTPS.
    humanURL: https://letsencrypt.org/docs/
    baseURL: https://acme-v02.api.letsencrypt.org
    tags:
      - ACME
      - Certificates
      - TLS
      - PKI
    properties:
      - type: Documentation
        url: https://letsencrypt.org/docs/
      - type: OpenAPI
        url: openapi/lets-encrypt-acme-openapi.yml
common:
  - type: Documentation
    name: Let's Encrypt Documentation
    description: Official documentation for Let's Encrypt.
    url: https://letsencrypt.org/docs/
  - type: GitHubOrg
    name: Let's Encrypt GitHub
    description: Source code and repositories for Let's Encrypt.
    url: https://github.com/letsencrypt
  - type: Specification
    name: ACME RFC 8555
    description: IETF specification for the ACME protocol.
    url: https://datatracker.ietf.org/doc/html/rfc8555
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
