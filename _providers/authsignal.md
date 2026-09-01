---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 2
  name: Authsignal Agentic Access
  operation_count: 26
  slug: authsignal-agentic-access
  summary_line: 26 operations · 18 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'Server-to-server REST API used to track user actions, evaluate the rules engine, mint short-lived URLs for the pre-built authentication UI, issue client tokens, validate challenge results, and manage '
  name: Authsignal Server API
  slug: server-api
- description: Browser / device-facing REST API for fully custom authentication UIs. Supports passkeys, authenticator apps, SMS / WhatsApp OTP, email OTP, magic links, and push challenges. Authenticated with short-l
  name: Authsignal Client API
  slug: client-api
- description: 'REST API for tenant-level configuration: actions and rules, theme and branding, and other tenant settings. Authenticated with a separate management API key.'
  name: Authsignal Management API
  slug: management-api
- description: Outbound webhooks delivering authentication and enrollment events, enabling downstream systems to react to user lifecycle changes and challenge outcomes.
  name: Authsignal Webhooks
  slug: webhooks
- description: Official server-side SDK for Node.js / TypeScript wrapping the Server API.
  name: Authsignal Node.js SDK
  slug: sdk-node
- description: Official server-side Python SDK for the Authsignal Server API.
  name: Authsignal Python SDK
  slug: sdk-python
- description: Official Java / Kotlin SDK for the Authsignal Server API.
  name: Authsignal Java SDK
  slug: sdk-java
- description: Official C# / .NET SDK for the Authsignal Server API.
  name: Authsignal .NET SDK
  slug: sdk-dotnet
- description: Official Ruby SDK for the Authsignal Server API.
  name: Authsignal Ruby SDK
  slug: sdk-ruby
- description: Official PHP SDK for the Authsignal Server API.
  name: Authsignal PHP SDK
  slug: sdk-php
- description: Official Go SDK for the Authsignal Server API.
  name: Authsignal Go SDK
  slug: sdk-go
- description: JavaScript / TypeScript browser SDK wrapping the Client API and WebAuthn / passkey ceremonies for web applications.
  name: Authsignal Browser SDK
  slug: sdk-browser
- description: Native iOS (Swift) SDK for passkeys, push, and OTP challenges in iOS applications.
  name: Authsignal iOS SDK
  slug: sdk-ios
- description: Native Android (Kotlin) SDK for passkeys, push, and OTP challenges in Android applications.
  name: Authsignal Android SDK
  slug: sdk-android
- description: React Native wrapper around the iOS and Android SDKs.
  name: Authsignal React Native SDK
  slug: sdk-react-native
- description: Flutter (Dart) SDK wrapping the iOS and Android native SDKs.
  name: Authsignal Flutter SDK
  slug: sdk-flutter
- description: The Actions API from Authsignal — 3 operation(s) for actions.
  name: Authsignal Actions API
  slug: authsignal-actions-api
- description: The Authenticators API from Authsignal — 4 operation(s) for authenticators.
  name: Authsignal Authenticators API
  slug: authsignal-authenticators-api
- description: The Challenges API from Authsignal — 5 operation(s) for challenges.
  name: Authsignal Challenges API
  slug: authsignal-challenges-api
- description: The Devices API from Authsignal — 3 operation(s) for devices.
  name: Authsignal Devices API
  slug: authsignal-devices-api
- description: The Sessions API from Authsignal — 5 operation(s) for sessions.
  name: Authsignal Sessions API
  slug: authsignal-sessions-api
- description: The Users API from Authsignal — 2 operation(s) for users.
  name: Authsignal Users API
  slug: authsignal-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Authsignal Server Actions API
  slug: open-authsignal-actions-api
- collection_type: open
  name: Authsignal Server Actions Authenticators API
  slug: open-authsignal-authenticators-api
- collection_type: open
  name: Authsignal Server Actions Challenges API
  slug: open-authsignal-challenges-api
- collection_type: open
  name: Authsignal Server Actions Devices API
  slug: open-authsignal-devices-api
- collection_type: open
  name: Authsignal Server Actions Sessions API
  slug: open-authsignal-sessions-api
- collection_type: open
  name: Authsignal Server Actions Users API
  slug: open-authsignal-users-api
- collection_type: open
  name: Authsignal Server API
  slug: open-authsignal
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/authsignal/authsignal-node/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/authsignal/authsignal-node/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/authsignal/authsignal-node/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/authsignal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authsignal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/authsignal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.authsignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.authsignal.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/authsignal
- group: operate
  title: ''
  type: Status
  url: https://status.authsignal.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.authsignal.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.authsignal.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authsignal
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.authsignal.com/llms.txt
created: '2026-05-23'
description: Authsignal is a passwordless, step-up, and risk-based authentication platform. The product wraps passkeys, authenticator apps (TOTP), SMS and WhatsApp OTP, email OTP and magic links, push notifications, biometrics (face / palm), and ID verification behind a unified Server API, Client API, and Management API. A no-code rules engine routes high-risk events through step-up challenges, and audit / observability surfaces every authentication attempt. Authsignal slots in front of existing identity providers (Cognito, Auth0, Azure AD B2C, Keycloak, IdentityServer, NextAuth.js) or works standalone.
finops:
- name: Authsignal Finops
  service_category: API
  slug: authsignal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authsignal.png
layout: provider
modified: '2026-05-23'
name: Authsignal
nav: Providers
network: true
overview: 'Authsignal publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Authenticators API, Challenges API, and 3 more. Tagged areas include Authentication, Passkeys, MFA, Step-Up, and Passwordless.


  Authsignal''s developer surface includes authentication, documentation, GitHub presence, status page, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Authsignal Plans Pricing
  plan_count: 1
  slug: authsignal-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Authsignal Rate Limits
  slug: authsignal-rate-limits
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.1
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authsignal/refs/heads/main/screenshots/authsignal-2026-06-20T172610.png
security:
- kind: authentication
  name: Authsignal Authentication
  slug: authsignal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Authsignal Domain Security
  slug: authsignal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authsignal
tags:
- Authentication
- Passkeys
- MFA
- Step-Up
- Passwordless
- Risk
- Biometrics
- Identity Verification
website: https://www.authsignal.com/
---
