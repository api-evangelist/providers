---
aid: moov
specificationVersion: '0.19'
name: Moov
description: Moov is a financial infrastructure platform that enables developers to embed money movement capabilities directly into their applications. Their developer platform provides a RESTful API, client-side JavaScript SDK, pre-built UI components, and official backend SDKs across multiple languages for building compliant, full-featured financial products.
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-04'
tags:
  - Banking
  - Embedded Finance
  - Financial Infrastructure
  - Money Movement
  - Payments
  - Transfers
apis:
  - aid: moov:moov-api
    name: Moov API
    description: The Moov API is a RESTful financial infrastructure platform that enables developers to integrate money movement capabilities into their applications. The API supports a full range of financial operations including account management, payment method onboarding, transfers, sweeps, refunds, dispute resolution, card issuing, and payment links. Authentication uses OAuth2 access tokens with permission scopes.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.moov.io/api/
    tags:
      - Banking
      - Financial Infrastructure
      - Money Movement
      - Payments
      - Transfers
    properties:
      - type: Documentation
        url: https://docs.moov.io/api/
      - type: OpenAPI
        url: openapi/moov-api-openapi.yml
      - type: AsyncAPI
        url: asyncapi/moov-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/moov-account-schema.json
      - type: JSONSchema
        url: json-schema/moov-transfer-schema.json
      - type: JSONLD
        url: json-ld/moov-context.jsonld
  - aid: moov:moov-js
    name: Moov.js
    description: Moov.js is a client-side JavaScript SDK designed to streamline interactions with the Moov API while keeping personally identifiable information out of developer infrastructure. All PII is transmitted directly to Moov, relieving developers of the responsibility for storing or handling sensitive user data. The SDK supports account creation, funding source integration, and transfer facilitation, along with pre-built UI components called Moov Drops.
    humanURL: https://docs.moov.io/moovjs/
    tags:
      - Client SDK
      - Data Collection
      - JavaScript
      - Payments
      - PCI Compliance
    properties:
      - type: Documentation
        url: https://docs.moov.io/moovjs/
  - aid: moov:moov-drops
    name: Moov Drops
    description: Moov Drops are pre-built, drop-in web UI components for complicated payment and account management flows. These components securely collect payment and account information from users without developers needing to build complex financial forms from scratch. Drops integrate with the Moov API and Moov.js to provide a cohesive front-end experience for onboarding, bank account linking, card collection, and other payment-related workflows.
    humanURL: https://docs.moov.io/guides/developer-tools/
    tags:
      - Embedded Finance
      - Frontend
      - Payments
      - UI Components
      - Web Components
    properties:
      - type: Documentation
        url: https://docs.moov.io/guides/developer-tools/
  - aid: moov:moov-backend-sdks
    name: Moov Backend SDKs
    description: Moov provides official server-side client libraries for interacting with the Moov API across multiple programming languages, including Go, TypeScript, Python, Java, PHP, Ruby, and C#/.NET. These SDKs abstract the HTTP layer and provide idiomatic interfaces for each language to access Moov's full range of financial operations. Each SDK is actively maintained and versioned to track the Moov API's versioning scheme.
    humanURL: https://docs.moov.io/sdks/
    tags:
      - .NET
      - Go
      - Java
      - PHP
      - Python
      - Ruby
      - SDK
      - TypeScript
    properties:
      - type: Documentation
        url: https://docs.moov.io/sdks/
common:
  - type: Portal
    url: https://docs.moov.io/
  - type: Documentation
    url: https://docs.moov.io/
  - type: Website
    url: https://moov.io/
  - type: Blog
    url: https://moov.io/blog/
  - type: Login
    url: https://dashboard.moov.io/
  - type: Features
    data:
      - 'Card Acceptance: IC+ + 0.60% + $0.15/transaction'
      - 'Tap to Pay: IC+ + 0.50% + $0.15'
      - 'Instant Payments (RTP): 0.95% (50¢ min, $5 cap)'
      - 'ACH transfers: $0.25-$0.40 each'
      - 'Moov Wallets: $0.50/active wallet/month'
      - 'Virtual Cards: $0.15 per card creation'
      - $500/month minimum across all products
      - Apple Pay and Google Pay support
      - 'International cards: +1.5% surcharge'
      - 'REST API: 600 req/min default'
      - Webhooks for facilitator/account/transfer events
      - OAuth 2.0 + API tokens
      - Embedded onboarding for sub-merchants
      - KYC/KYB built in
      - 1099-K reporting handled
      - Custom pricing for high-volume
    sources:
      - https://moov.io/pricing
    updated: '2026-05-04'
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
