---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/crossborder-ai/hosts/crossborder-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossborder-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/crossborder-ai/vendors/crossborder-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossborder-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://exactera.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://exactera.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://exactera.com/news/
- group: auth
  href: https://artifacts.apis.io/crossborder-ai/security/crossborder-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossborder-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://exactera.com/
coverage:
  checked: '2026-10-25'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found at the provider’s API hosts.
  evidence:
  - status: 0
    url: https://api.crossborder.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Exactera offers expert tax and transfer pricing compliance services delivered by specialists and powered by AI. It helps multinational corporations navigate complex global tax regulations, ensuring accurate reporting, documentation, and strategic planning. The platform combines deep tax expertise with advanced AI-driven analytics to automate compliance, reduce risk, and optimize tax positions across jurisdictions.
image: https://exactera.com/wp-content/uploads/2023/05/OG_image.jpg
layout: provider
modified: '2026-10-25'
name: Exactera
nav: Providers
network: true
overview: Exactera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Tax, AI, Compliance, and Global.
random_paper: 23
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crossborder Ai Domain Security
  slug: crossborder-ai-domain-security
  summary_line: TLSv1.3
slug: crossborder-ai
tags:
- Company
- Tax
- AI
- Compliance
- Global
website: https://exactera.com/
---
