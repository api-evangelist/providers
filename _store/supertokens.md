---
aid: supertokens
name: SuperTokens
description: SuperTokens is an open source authentication solution providing session management, social login, email/password auth, and passwordless flows for web and mobile apps. It is an open source alternative to Auth0, Firebase Auth, and AWS Cognito. SuperTokens exposes a Core Driver Interface (CDI) HTTP API for backend SDKs to communicate with the supertokens-core service, as well as a Frontend Driver Interface (FDI) for frontend SDK interaction. Available SDKs cover Node.js, Python, Go, Java, React, Flutter, iOS, and Android.
url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Authentication
  - Open Source
  - Session Management
  - Social Login
  - Passwordless
  - Identity
  - Authorization
  - Multi-Tenancy
  - Node.js
  - Self-Hosted
apis:
  - aid: supertokens:core-driver-interface
    name: SuperTokens Core Driver Interface
    description: The Core Driver Interface (CDI) is the REST API exposed by the supertokens-core HTTP service. Backend SDKs (Node.js, Python, Go) communicate with the core via this API to perform authentication operations including session creation, verification, refresh, user sign-up/sign-in, email verification, password reset, multi-tenancy, and user metadata management.
    humanURL: https://github.com/supertokens/core-driver-interface
    baseURL: https://{supertokens-core-host}:{port}
    tags:
      - Authentication
      - Session Management
      - Core API
      - Identity
      - Open Source
    properties:
      - type: Documentation
        url: https://supertokens.com/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/openapi/supertokens-core-driver-interface-openapi.yml
      - type: GitHub Repository
        url: https://github.com/supertokens/supertokens-core
      - type: API Specification
        url: https://github.com/supertokens/core-driver-interface
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/json-schema/supertokens-session-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/json-structure/supertokens-session-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/json-ld/supertokens-context.jsonld
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/rules/supertokens-cdi-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/capabilities/authentication.yaml
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/supertokens/refs/heads/main/vocabulary/supertokens-vocabulary.yml
common:
  - type: Website
    url: https://supertokens.com
  - type: Documentation
    url: https://supertokens.com/docs
  - type: GitHub Organization
    url: https://github.com/supertokens
  - type: GitHub Repository
    url: https://github.com/supertokens/supertokens-core
  - type: SDK Node.js
    url: https://github.com/supertokens/supertokens-node
  - type: SDK Python
    url: https://github.com/supertokens/supertokens-python
  - type: SDK Go
    url: https://github.com/supertokens/supertokens-golang
  - type: SDK React
    url: https://github.com/supertokens/supertokens-web-js
  - type: SDK Flutter
    url: https://github.com/supertokens/supertokens-flutter
  - type: Changelog
    url: https://github.com/supertokens/supertokens-core/blob/master/CHANGELOG.md
  - type: Issues
    url: https://github.com/supertokens/supertokens-core/issues
  - type: Features
    data:
      - 'Free self-hosted: open-source core at any scale'
      - 'Cloud: $0.02/MAU (free under 5K MAUs)'
      - 'Self-hosted paid add-ons: same rates as Cloud, $100/mo minimum'
      - Email/password, social login, SSO, magic links, SMS/Email OTP
      - User Management Dashboard (3 users free, $20/user/mo above)
      - Session Management with rotating refresh tokens
      - 'MFA add-on: $0.01/MAU'
      - 'Account Linking add-on: $0.005/MAU'
      - 'Frontend SDKs: React, Next.js, Vue, Angular, vanilla JS'
      - 'Backend SDKs: Node.js, Python, Go (community for others)'
      - RBAC built-in
      - Pre-built UI components
      - Self-hostable Postgres or MySQL backend
      - Open source (Apache 2.0)
      - SOC 2 compliant managed cloud
      - Recipe-based architecture (one for each auth method)
    sources:
      - https://supertokens.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
