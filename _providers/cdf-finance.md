---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/cdf-finance/llms/cdf-finance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdf-finance-llms.txt
- group: other
  href: https://artifacts.apis.io/cdf-finance/hosts/cdf-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cdf-finance-hosts.yml
- group: other
  href: https://artifacts.apis.io/cdf-finance/vendors/cdf-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cdf-finance-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cdf-finance/security/cdf-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdf-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cdf.finance/
- group: operate
  title: ''
  type: Support
  url: https://cdf.finance/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://cdf.finance/planos
coverage:
  checked: '2026-11-04'
  detail: No public developer documentation or machine‑readable API contracts were found on any of the provider's hosts.
  evidence:
  - status: 200
    url: https://app.cdf.finance/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-04'
description: CDF Finance is a personal finance management application powered by artificial intelligence, allowing users to record expenses via voice or photo, track accounts, cards, goals, investments, and interact with Fran, an AI assistant that understands their financial life. The service offers free basic features with optional PRO subscription plans, targeting Brazilian users and supporting iOS, Android, and web platforms.
image: https://cdf.finance/og-image.png
layout: provider
modified: '2026-11-04'
name: CDF Finance
nav: Providers
network: true
overview: 'CDF Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Personal Finance, Mobile, and Web.


  CDF Finance''s developer surface includes support, pricing, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cdf Finance Domain Security
  slug: cdf-finance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cdf-finance
tags:
- Finance
- Artificial Intelligence
- Personal Finance
- Mobile
- Web
website: https://cdf.finance/
---
