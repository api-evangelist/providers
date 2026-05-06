---
aid: passbolt
name: Passbolt
description: Passbolt is an open source password manager for teams. The Passbolt API provides programmatic access to manage resources (passwords), folders, users, groups, sharing, comments, metadata, and authentication via GPGAuth or JWT.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Password Manager
  - Security
  - Secrets
  - Identity
created: '2025-02-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/passbolt/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: passbolt:passbolt
    name: Passbolt API
    description: Low-level reference for the Passbolt API covering authentication, resources, folders, users, groups, sharing, comments, metadata keys, and healthcheck. JWT is the preferred authentication method; legacy GPGAuth is also supported.
    humanURL: https://www.passbolt.com/docs/api/
    baseURL: https://passbolt.local
    tags:
      - Password Manager
      - Security
      - Secrets
    properties:
      - type: Documentation
        url: https://www.passbolt.com/docs/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/passbolt/refs/heads/main/openapi/passbolt-openapi.yaml
      - type: SignUp
        url: https://www.passbolt.com/pricing
      - type: TermsOfService
        url: https://www.passbolt.com/terms
      - type: License
        url: https://www.gnu.org/licenses/agpl-3.0.html
common:
  - type: Website
    url: https://www.passbolt.com
  - type: Documentation
    url: https://www.passbolt.com/docs/
  - type: SourceCode
    url: https://github.com/passbolt
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
