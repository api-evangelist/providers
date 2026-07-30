---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Magic Link Agentic Access
  operation_count: 3
  slug: magic-link-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 4
apis:
- description: 'REST API for backend integrations: validate Magic-issued DID tokens, fetch user metadata, log out users, and manage white-label policies.'
  name: Magic Admin API
  slug: admin-api
- description: REST API to provision server-managed wallets and sign transactions in backend services.
  name: Magic Server Wallets API
  slug: server-wallets
- description: SDK client configuration
  name: Magic Client API
  slug: magic-link-client-api
- description: Magic user metadata and session management
  name: Magic Users API
  slug: magic-link-users-api
artifact_total: 11
collections:
- collection_type: open
  name: Magic Admin API
  slug: open-magic-link
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/magic-link-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magic-link-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/magic-link-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magiclabs-inc
- group: company
  title: ''
  type: Website
  url: https://magic.link/
- group: commercial
  title: ''
  type: Plans
  url: plans/magic-link-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/magic-link-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/magic-link-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/magiclabs
created: '2026-05-08'
description: Magic is an embedded-wallet and authentication platform offering passwordless login (magic links, OAuth, WebAuthn, SMS) plus white-label Embedded Wallets and Server Wallets. Primary surface is the Magic SDK; an Admin REST API exists for user lookup, token validation, and metadata.
finops:
- name: Magic Link Finops
  service_category: Web3
  slug: magic-link-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magic-link.png
layout: provider
modified: '2026-05-08'
name: Magic
nav: Providers
network: true
overview: 'Magic publishes 2 APIs on the [APIs.io](https://apis.io/) network: Client API and Users API. Tagged areas include Web3, Wallets, Authentication, Embedded Wallets, and MPC.


  Magic''s developer surface includes authentication, engineering blog, and 7 more developer resources.'
plans:
- name: Magic Link Plans Pricing
  plan_count: 4
  slug: magic-link-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Magic Link Rate Limits
  slug: magic-link-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Magic Link Authentication
  slug: magic-link-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Magic Link Domain Security
  slug: magic-link-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: magic-link
tags:
- Web3
- Wallets
- Authentication
- Embedded Wallets
- MPC
website: https://magic.link/
---
