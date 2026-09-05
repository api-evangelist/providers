---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Magic Link Agentic Access
  operation_count: 3
  slug: magic-link-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: 'REST API for backend integrations: validate Magic-issued DID tokens, fetch user metadata, log out users, and manage white-label policies.'
  name: Magic Admin API
  slug: admin-api
- description: REST API to provision server-managed wallets and sign transactions in backend services.
  name: Magic Server Wallets API
  slug: server-wallets
- baseURL: https://api.magic.link
  baseurl_source: declared
  description: SDK client configuration
  name: Magic Client API
  slug: magic-link-client-api
- baseURL: https://api.magic.link
  baseurl_source: declared
  description: Magic user metadata and session management
  name: Magic Users API
  slug: magic-link-users-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Magic Admin Client API
  slug: open-magic-link-client-api
- collection_type: open
  name: Magic Admin Client Users API
  slug: open-magic-link-users-api
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
random_paper: 1
rate_limits:
- limit_count: 1
  name: Magic Link Rate Limits
  slug: magic-link-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 45.0
    catalog_earned_first_party: 0.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
