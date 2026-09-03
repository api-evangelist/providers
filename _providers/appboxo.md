---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://appboxo.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.boxo.io/ — a different registrable domain (appboxo.com -> boxo.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Appboxo Webhooks
  slug: appboxo-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appboxo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appboxo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.boxo.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boxo.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.boxo.io/MiniApp%20API%20Reference/APIReference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.boxo.io/host-apps/GettingStarted
- group: company
  title: ''
  type: Blog
  url: https://www.boxo.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appboxo
- group: operate
  title: ''
  type: Support
  url: https://www.boxo.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.boxo.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boxo.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boxo.io/privacy
- group: build
  title: ''
  type: Packages
  url: packages/appboxo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appboxo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appboxo-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appboxo-error-codes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appboxo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appboxo-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appboxo-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/appboxo-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/appboxo-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appboxo-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appboxo-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appboxo-lifecycle.yml
created: '2026-07-17'
description: Appboxo (Boxo) is a superapp / miniapp platform that lets any mobile app embed third-party services as native-feeling miniapps through a single integration. It ships host-app SDKs for iOS, Android, Flutter, React Native, Expo and Capacitor plus a web JavaScript SDK bridge that exposes native UI (tab bar, navigation bar, action sheets, QR reader, maps) and device capabilities to web miniapps. The Boxo Platform provides server-to-server integrations — Boxo Connect (SSO / user authorization), Boxo Payments (in-app order payments with host-app callbacks), custom events, and configurable request signaturing (RSA2 / HMAC / ECDSA) — so a host app can launch new services (eSIM, marketplace, remittance, insurance, travel, loyalty) far faster than building them in-house. Appboxo is a portfolio company of 500 Global.
image: https://framerusercontent.com/assets/LHGWxAyjSr0ojCUUO5aqzWZOASs.png
layout: provider
modified: '2026-07-17'
name: Appboxo
nav: Providers
network: true
overview: 'Appboxo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Super App, Mini Apps, Mobile SDK, and Embedded Finance.


  The Appboxo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Appboxo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 61.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appboxo/refs/heads/main/screenshots/appboxo-2026-07-25T200739.png
security:
- kind: authentication
  name: Appboxo Authentication
  slug: appboxo-authentication
  summary_line: http-basic/bearer-token/oauth2-sso/request-signing · 6 schemes
- kind: domain-security
  name: Appboxo Domain Security
  slug: appboxo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appboxo
tags:
- Company
- Super App
- Mini Apps
- Mobile SDK
- Embedded Finance
- Payments
- Single Sign-On
- App Platform
- eSIM
- Developer Tools
website: https://appboxo.com
---
