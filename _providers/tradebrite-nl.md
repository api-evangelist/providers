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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/tradebrite-nl/llms/tradebrite-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradebrite-nl-llms.txt
- group: other
  href: https://artifacts.apis.io/tradebrite-nl/hosts/tradebrite-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradebrite-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/tradebrite-nl/vendors/tradebrite-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tradebrite-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tradebrite-nl/security/tradebrite-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradebrite-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradebrite.nl/
- group: docs
  title: ''
  type: APIReference
  url: https://tradebrite.nl/property-context/
- group: docs
  title: ''
  type: APIReference
  url: https://tradebrite.nl/vehicle-context/
- group: docs
  title: ''
  type: APIReference
  url: https://tradebrite.nl/allergiecheck/
created: '2026-10-30'
description: Tradebrite NL is a Dutch AI‑automation and development studio offering AI‑driven services, custom web and mobile applications, and specialized APIs for Dutch vehicle, address, and allergen contexts. Their platform provides AI‑enhanced automation for repetitive tasks, bespoke AI applications, and integrates with various data sources to deliver intelligent solutions for businesses in the Netherlands and beyond.
layout: provider
modified: '2026-10-30'
name: tradebrite-nl
nav: Providers
network: true
overview: 'tradebrite-nl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Development, Netherlands, and Services.


  tradebrite-nl''s developer surface includes API reference and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tradebrite-nl/tradebrite-nl-2026-11-03T144951.png
security:
- kind: domain-security
  name: Tradebrite Nl Domain Security
  slug: tradebrite-nl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tradebrite-nl
tags:
- Artificial Intelligence
- Automation
- Development
- Netherlands
- Services
website: https://tradebrite.nl/
---
