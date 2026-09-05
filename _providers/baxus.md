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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'The BAXUS backend service (NestJS) that powers the marketplace and BoozApp: bottle and listing search, marketplace listings, and user "bar" collections. Undocumented public/read endpoints are evidence'
  name: BAXUS API (BoozApp / Marketplace)
  slug: baxus-api-boozapp-marketplace
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://baxus.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BAXUSNFT
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baxus.co/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baxus.co/termsconditions
- group: start
  title: ''
  type: Login
  url: https://www.baxus.co/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baxus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/baxus-llms.txt
created: '2026-07-17'
description: BAXUS is a peer-to-peer marketplace for buying, selling, trading, and storing fine and rare wine and spirits, built on the Solana blockchain. Founded in 2021 by Tzvi Wiesel and based in Woodland Park, New Jersey, BAXUS authenticates physical bottles and holds them in climate-controlled vaults, then tokenizes each as an NFT that serves as a digital certificate of ownership and provenance. Beyond the marketplace and Vault, BAXUS operates the BoozApp collection app, an open-source AI whiskey sommelier agent (BOB), and Whisky-Goggles AI bottle recognition. Its backend API at services.baxus.co powers bottle search, marketplace listings, and user bar collections. Backed by Multicoin Capital.
image: https://www.baxus.co/assets/icons/baxus_gold.svg
layout: provider
modified: '2026-07-18'
name: Baxus
nav: Providers
network: true
overview: Baxus publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Blockchain, Solana, and NFT.
random_paper: 1
rate_limits:
- limit_count: 1
  name: Baxus Rate Limits
  slug: baxus-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 16.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baxus/refs/heads/main/screenshots/baxus-2026-07-25T202441.png
security:
- kind: domain-security
  name: Baxus Domain Security
  slug: baxus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baxus
tags:
- Company
- Crypto Web3
- Blockchain
- Solana
- NFT
- Spirits
- Wine
- Whiskey
- Marketplace
- Collectibles
website: https://baxus.co
---
