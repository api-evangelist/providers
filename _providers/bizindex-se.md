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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BizIndex services (MCP endpoint discovered)
  name: BizIndex API
  slug: bizindex-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bizindex-se/hosts/bizindex-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bizindex-se-hosts.yml
- group: other
  href: https://artifacts.apis.io/bizindex-se/vendors/bizindex-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bizindex-se-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bizindex-se/security/bizindex-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bizindex-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bizindex.se/
- group: other
  title: ''
  type: x-coverage
  url: https://bizindex.se/
created: '2026-11-02'
description: Bizindex är ett öppet index över svenska aktiebolag som samlar registeruppgifter från Bolagsverket och SCB, visar vilken webbplats som är kopplad till varje företag samt ger en synlighetskontroll med gratis åtgärdsråd. Plattformen möjliggör sökning bland över 38 000 företag i 13 branscher och erbjuder detaljerad information om deras registrering, webbplats och historik innan någon bekräftar uppgifterna. Detta stödjer både konsumenter och företag i att fatta informerade beslut baserade på transparent data.
image: https://bizindex.se/opengraph-image?43d5de9779ae9fd0
layout: provider
modified: '2026-11-02'
name: Bizindex
nav: Providers
network: true
overview: Bizindex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business, Index, Swedish, Companies, and Open Data.
random_paper: 18
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bizindex Se Domain Security
  slug: bizindex-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: bizindex-se
tags:
- Business
- Index
- Swedish
- Companies
- Open Data
website: https://bizindex.se/
---
