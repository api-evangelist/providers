---
aid: 1password
url: https://raw.githubusercontent.com/api-evangelist/1password/refs/heads/main/apis.yml
apis:
- aid: 1password:1password-connect-api
  name: 1Password Connect Server API
  tags:
  - Items
  - Passwords
  - Secrets
  - Vaults
  humanURL: https://developer.1password.com/docs/connect/api-reference/
  baseURL: http://localhost:8080
  properties:
  - url: https://developer.1password.com/docs/connect/api-reference/
    type: Documentation
  - url: openapi/1password-connect-openapi.yml
    type: OpenAPI
  description: The 1Password Connect Server API provides secure access to 1Password items and vaults in your company's apps and cloud infrastructure through a private REST API. Connect Servers bridge the gap between 1Password and your infrastructure by enabling programmatic access to secrets stored in shared vaults. You can create, read, update, and delete items, manage vaults, and retrieve files attached to items.
- aid: 1password:1password-events-api
  name: 1Password Events API
  tags:
  - Audit
  - Events
  - Monitoring
  - Security
  humanURL: https://developer.1password.com/docs/events-api/reference/
  baseURL: https://events.1password.com
  properties:
  - url: https://developer.1password.com/docs/events-api/reference/
    type: Documentation
  - url: openapi/1password-events-openapi.yml
    type: OpenAPI
  description: The 1Password Events API provides programmatic access to event data generated within a 1Password account. It enables security teams and administrators to retrieve sign-in attempts, item usage records, and audit events for monitoring, compliance, and security analysis. The API uses cursor-based pagination with POST requests to efficiently stream large volumes of event data.
- aid: 1password:1password-partnership-api
  name: 1Password Partnership API
  tags:
  - Billing
  - Partners
  - Passwords
  humanURL: https://developer.1password.com/docs/partnership-api/reference/
  baseURL: https://billing.b5test.eu/api/v1
  properties:
  - url: https://developer.1password.com/docs/partnership-api/reference/
    type: Documentation
  - url: openapi/1password-partnership-openapi.yml
    type: OpenAPI
  description: You can use the 1Password Partnership API to manage the provisioning and deprovisioning of third-party partner billing accounts for your customers. The API supports partner billing accounts for 1Password individual and family accounts. The Partnership API does not support 1Password team or business accounts.
name: 1Password
tags:
- Password Manager
- Passwords
- Security
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-07'
position: Consuming
description: 1Password is a password manager that helps individuals and businesses securely store and manage passwords, credentials, and sensitive information. The 1Password Partnership API enables partners to manage provisioning and deprovisioning of third-party partner billing accounts for customers, supporting individual and family account types.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

