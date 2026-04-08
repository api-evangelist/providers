---
aid: mastercard-developer-hub-for-fdx-apis
url: https://raw.githubusercontent.com/api-evangelist/mastercard-developer-hub-for-fdx-apis/refs/heads/main/apis.yml
apis:
- aid: mastercard-fdx:authorization-api
  name: Mastercard FDX Authorization API
  description: Dynamic Client Registration, Token, Introspection, Authorize API.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: http://example.com
  baseURL: http://api.example.com
  tags:
  - Authorization
  - FDX
  properties:
  - type: Documentation
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#authorization-server
  - type: OpenAPI
    url: fdx-authorization-api-openapi.yaml
  - type: MockServer
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-authorization-server
  - type: GitHubRepository
    url: https://github.com/Mastercard/Fdx-Mock-Auth-Server
- aid: mastercard-fdx:resource-api
  name: Mastercard FDX Resource API
  description: FDX Mock Resource Server API reference for developers.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: http://example.com
  baseURL: http://api.example.com
  tags:
  - FDX
  - Payments
  properties:
  - type: Documentation
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/api-reference/#resource-server
  - type: OpenAPI
    url: fdx-resource-api-openapi.yaml
  - type: MockServer
    url: https://developer.mastercard.com/fdx-dev-hub/documentation/how-to-run/#fdx-mock-resource-server
  - type: GitHubRepository
    url: https://github.com/Mastercard/Fdx-Mock-Resource-Server
name: Mastercard Developer Hub for FDX APIs
tags:
- Banking
- FDX
- Open Banking
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Financial Data Exchange (FDX) is a nonprofit industry standards body that created the FDX API, a technical standard for user-permissioned financial data sharing. The FDX API standard, like other data sharing methods used in open banking, gives consumers more control over who can access their financial data. The open banking industry is founded on the principles of interoperability, which are being advanced by forthcoming rulemaking from the The Consumer Financial Protection Bureau (CFPB).
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

