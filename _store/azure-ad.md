---
aid: azure-ad
url: https://raw.githubusercontent.com/api-evangelist/azure-ad/refs/heads/main/apis.yml
apis:
- aid: azure-ad:microsoft-graph-api
  name: Microsoft Graph API
  description: The primary API for accessing Azure AD and other Microsoft 365 services.
  humanURL: https://docs.microsoft.com/en-us/graph/overview
  baseURL: https://graph.microsoft.com
  tags:
  - Directory
  - Identity
  - Microsoft 365
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Change Log
    url: https://docs.microsoft.com/en-us/graph/changelog
- aid: azure-ad:azure-ad-b2c-api
  name: Azure AD B2C API
  description: Business-to-consumer identity management solution.
  humanURL: https://docs.microsoft.com/en-us/azure/active-directory-b2c/
  baseURL: https://login.microsoftonline.com
  tags:
  - Authentication
  - B2C
  - Consumer Identity
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/azure/active-directory-b2c/overview
name: Azure Active Directory
tags:
- Authentication
- Authorization
- Identity
- OAuth
- OpenID Connect
- Single Sign-On
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft's cloud-based identity and access management service that helps employees sign in and access resources. Azure AD provides OAuth, OpenID Connect, SAML, and other identity protocols for securing applications and managing user identities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

