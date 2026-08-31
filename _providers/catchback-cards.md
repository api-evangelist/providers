---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catchback-cards-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchbackcards.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CatchBack-Cards
created: '2026-07-17'
description: 'Catchback Cards (CatchBack) is a Y Combinator (Winter 2026) company building a mobile and web platform for trading card collectors, focused on Pokemon and sports cards. Collectors open digital mystery packs to receive physical cards, receive instant buyback offers paid out via Venmo or PayPal, and trade cards through a $1 marketplace. The platform differentiates on transparency: it lets creators build custom mystery packs with personalized chases and customized odds using cryptographically trusted tooling, and publishes open-source verification so collectors can independently validate pack randomness and odds. The company launched its iOS app on January 25, 2026 and is a seven-person team based in San Francisco. Catchback Cards is a consumer application and does not currently publish a public API, developer portal, or OpenAPI definition; this profile is maintained in the API Evangelist network as a portfolio lead and is enriched only with independently verifiable facts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catchback-cards.png
layout: provider
modified: '2026-07-18'
name: Catchback Cards
nav: Providers
network: true
overview: Catchback Cards is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading Cards, Collectibles, Marketplace, and Consumer.
random_paper: 16
score:
  band: minimal
  composite: 1.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 1.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/catchback-cards/refs/heads/main/screenshots/catchback-cards-2026-07-25T204805.png
security:
- kind: domain-security
  name: Catchback Cards Domain Security
  slug: catchback-cards-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: catchback-cards
tags:
- Company
- Trading Cards
- Collectibles
- Marketplace
- Consumer
- Mobile
- Payments
- Y Combinator
website: https://catchbackcards.com
---
