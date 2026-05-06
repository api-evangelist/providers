---
aid: duo-security
name: Duo Security
description: Duo Security is a multi-factor authentication and zero trust security platform from Cisco for securing access to applications and APIs.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authentication
  - MFA
  - Zero Trust
  - Identity
url: https://raw.githubusercontent.com/api-evangelist/duo-security/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: duo-security:duo-admin-api
    name: Duo Admin API
    description: The Duo Admin API provides programmatic access to manage users, groups, phones, hardware tokens, WebAuthn credentials, bypass codes, and bulk operations across a Duo Security tenant. Requests are authenticated using HMAC-SHA1 signed HTTP Basic credentials derived from your integration key and secret key.
    humanURL: https://duo.com/docs/adminapi
    baseURL: https://api-XXXXXXXX.duosecurity.com
    tags:
      - Authentication
      - MFA
      - Admin
      - Identity
    properties:
      - type: Documentation
        url: https://duo.com/docs/adminapi
      - type: OpenAPI
        url: openapi/duo-admin-api-openapi.yml
common:
  - type: Website
    url: https://duo.com
  - type: Documentation
    url: https://duo.com/docs
  - type: GitHub Organization
    url: https://github.com/duosecurity
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
