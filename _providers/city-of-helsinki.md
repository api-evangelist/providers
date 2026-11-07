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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/city-of-helsinki/security/city-of-helsinki-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/city-of-helsinki-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/city-of-helsinki/well-known/city-of-helsinki-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/city-of-helsinki-security.txt
- group: auth
  href: https://artifacts.apis.io/city-of-helsinki/well-known/city-of-helsinki-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/city-of-helsinki-api-security.txt
- group: agent
  href: https://artifacts.apis.io/city-of-helsinki/well-known/city-of-helsinki-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/city-of-helsinki-well-known.yml
- group: other
  href: https://artifacts.apis.io/city-of-helsinki/hosts/city-of-helsinki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/city-of-helsinki-hosts.yml
- group: auth
  href: https://artifacts.apis.io/city-of-helsinki/security/city-of-helsinki-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/city-of-helsinki-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/city-of-helsinki/security/city-of-helsinki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/city-of-helsinki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hel.fi/fi
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 302
    url: http://www.hel.fi/www/helsinki/en
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: City of Helsinki is the municipal government of Finland's capital, providing a wide range of public services, data, and digital platforms to residents, businesses, and visitors. The city maintains open data portals, transportation APIs, event listings, and various civic services, fostering transparency and innovation. This profile captures its publicly available APIs and documentation for developers.
layout: provider
modified: '2026-10-26'
name: City of Helsinki
nav: Providers
network: true
overview: City of Helsinki is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Open Data, Finland, Helsinki, and Civic Tech.
random_paper: 15
score:
  band: minimal
  composite: 5.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/city-of-helsinki/city-of-helsinki-2026-11-03T124232.png
security:
- kind: domain-security
  name: City Of Helsinki Domain Security
  slug: city-of-helsinki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: City Of Helsinki Vulnerability Disclosure
  slug: city-of-helsinki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: city-of-helsinki
tags:
- Government
- Open Data
- Finland
- Helsinki
- Civic Tech
- Public Services
website: https://www.hel.fi/fi
---
