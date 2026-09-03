---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: 'The Cardless partner API surface used by brands to embed a co-branded credit card program: partner authentication (Basic-auth exchange of a partner-signed JWT for a bearer access token), application s'
  name: Cardless Partner API
  slug: partner-api
- description: A remote Model Context Protocol server published by Cardless at docs.cardless.com/mcp (Mintlify-hosted). It answers tools/list anonymously and exposes three read-oriented tools over the Cardless docum
  name: Cardless Docs MCP Server
  slug: docs-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.cardless.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cardless.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cardless.com/
- group: company
  title: ''
  type: Blog
  url: https://www.cardless.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.cardless.com/help
- group: start
  title: ''
  type: SignUp
  url: https://app.cardless.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.cardless.com/terms_of_service/default/terms_of_service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.cardless.com/privacy_policy/default/privacy_policy.pdf
- group: other
  title: ''
  type: Customers
  url: https://www.cardless.com/customers
- group: company
  title: ''
  type: Careers
  url: https://www.cardless.com/careers
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cardless-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cardless-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cardless-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cardless-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cardless-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cardless-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cardless-lifecycle.yml
- group: design
  title: ''
  type: Components
  url: components/cardless-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cardless-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cardless-llms.txt
created: '2026-08-01'
description: Cardless, Inc. is a San Francisco fintech that operates an embedded co-branded credit card platform, letting consumer brands launch and run their own credit card programs natively inside their own apps and websites. The platform pairs a partner API surface with pre-built components covering the full credit journey — application and identity verification, real-time decisioning, checkout with instant virtual cards, card management and transaction disputes — while Cardless handles issuing-bank relationships, card production, underwriting, fraud, KYC/AML compliance, servicing and support behind the scenes. It is network-agnostic across Visa, Mastercard and American Express. Named partners include Coinbase (Coinbase One Card), Bilt, Qatar Airways Privilege Club, Alibaba.com, LATAM Airlines, Avianca LifeMiles, TAP Air Portugal and Avelo Airlines. Developer documentation at docs.cardless.com is gated behind a partner login, so no public OpenAPI, SDKs or sandbox credentials are published.
image: https://framerusercontent.com/images/hm4RTByVdin3oyQTHY2rMm9doQ.jpg
layout: provider
mcp_servers:
- description: ''
  name: Cardless Docs
  slug: cardless-docs
modified: '2026-08-01'
name: Cardless
nav: Providers
network: true
overview: 'Cardless publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Fintech, Credit Cards, and Card Issuing.


  Cardless'' developer surface includes documentation, engineering blog, support, signup flow, authentication, and 15 more developer resources.'
random_paper: 9
scopes:
- name: Cardless Scopes
  scope_count: 1
  slug: cardless-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials/refreshToken
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cardless/refs/heads/main/screenshots/cardless-2026-08-07T162953.png
security:
- kind: authentication
  name: Cardless Authentication
  slug: cardless-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Cardless Domain Security
  slug: cardless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardless
tags:
- Company
- Financial-Services
- Fintech
- Credit Cards
- Card Issuing
- Embedded Finance
- Payments
- Banking as a Service
- Lending
- Co-Branded Cards
- Loyalty
website: https://www.cardless.com/
---
