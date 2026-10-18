---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The USITC DataWeb provides interactive access to U.S. international trade statistics and U.S. tariff data, including imports, exports, and production by commodity and country.
  name: USITC DataWeb
  slug: usitc-dataweb
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/plans/international-trade-commission-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/international-trade-commission-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/rate-limits/international-trade-commission-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/international-trade-commission-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/finops/international-trade-commission-finops.yml
  title: ''
  type: FinOps
  url: finops/international-trade-commission-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/security/international-trade-commission-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/international-trade-commission-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usitc.gov/
- group: other
  title: ''
  type: Data
  url: https://www.usitc.gov/data/index.htm
created: '2024-12-03'
description: The United States International Trade Commission (USITC) is an independent, nonpartisan, quasi-judicial federal agency that fulfills a range of trade-related mandates. The USITC provides high-quality analysis of international trade issues to the President and the Congress, and serves as the primary forum for the adjudication of intellectual property and trade disputes. The agency exposes U.S. trade and tariff statistics through the USITC DataWeb interactive data service.
finops:
- has_sources: false
  method: generated
  name: International Trade Commission Finops
  primary_unit: ''
  service_category: API
  slug: international-trade-commission-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/international-trade-commission.png
layout: provider
modified: '2026-04-28'
name: International Trade Commission
nav: Providers
network: true
overview: 'International Trade Commission is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Government Data, Intellectual Property, Trade, and Tariffs.


  The International Trade Commission catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: International Trade Commission Plans Pricing
  plan_count: 3
  slug: international-trade-commission-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: International Trade Commission Rate Limits
  slug: international-trade-commission-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 0
  extends: []
  name: International Trade Commission API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: international-trade-commission-rules
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/screenshots/international-trade-commission-2026-06-20T183500.png
security:
- kind: domain-security
  name: International Trade Commission Domain Security
  slug: international-trade-commission-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: international-trade-commission
tags:
- Federal Government
- Government Data
- Intellectual Property
- Trade
- Tariffs
website: https://www.usitc.gov/
---
