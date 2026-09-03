---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://betastore.co'', ''status'': 301, ''note'': ''declared website redirects to https://slotsdemoplaywin.com/ — a different registrable domain (betastore.co -> slotsdemoplaywin.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://betastore.co
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simplemarket-inc
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betastore-beta-store-domain-security.yml
created: '2026-07-17'
description: BetaStore (legal entity SimpleMarket Inc., trading as BetaStore.co) is a B2B retail marketplace founded in 2020 by Steve Dakayi-Kamga and Leo-Armel Tchoudjang that serves informal neighborhood retailers in West and Central Africa, operating across Nigeria, Senegal and Ivory Coast from offices in Lagos and a Wilmington, Delaware registration. The platform lets small shopkeepers restock fast-moving consumer goods directly from manufacturers and distributors at wholesale prices, ordering through SMS, chat, WhatsApp and a mobile app, with logistics partners delivering to the store within 24 hours, and it layers embedded working-capital financing on top of observed retailer sales. BetaStore raised a 2.5 million dollar pre-Series A in May 2022 led by 500 Global with VestedWorld and Loyal VC. As of the July 2026 enrichment pass BetaStore publishes no public API, developer portal, documentation, SDK or machine-readable artifact of any kind, and its betastore.co domain serves no content
  -- both the apex and www hosts answer every path with a blanket Cloudflare 301 to unrelated third-party domains, and no api/app/docs subdomain resolves.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betastore-beta-store.png
layout: provider
modified: '2026-07-20'
name: BetaStore, Beta Store
nav: Providers
network: true
overview: BetaStore, Beta Store is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B Marketplace, Retail, FMCG, and Supply Chain.
random_paper: 12
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/betastore-beta-store/refs/heads/main/screenshots/betastore-beta-store-2026-07-25T202803.png
security:
- kind: domain-security
  name: Betastore Beta Store Domain Security
  slug: betastore-beta-store-domain-security
  summary_line: TLSv1.3
slug: betastore-beta-store
tags:
- Company
- B2B Marketplace
- Retail
- FMCG
- Supply Chain
- Logistics
- Embedded Finance
- E-Commerce
- Africa
website: https://betastore.co
---
