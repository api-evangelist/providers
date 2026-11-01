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
- group: auth
  href: https://artifacts.apis.io/cameo3/well-known/cameo3-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cameo3-help-security.txt
- group: agent
  href: https://artifacts.apis.io/cameo3/well-known/cameo3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cameo3-well-known.yml
- group: other
  href: https://artifacts.apis.io/cameo3/hosts/cameo3-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cameo3-hosts.yml
- group: other
  href: https://artifacts.apis.io/cameo3/vendors/cameo3-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cameo3-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.cameo.com/
- group: auth
  href: https://artifacts.apis.io/cameo3/security/cameo3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cameo3-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cameo.com
coverage:
  checked: '2026-10-06'
  detail: Cameo3 provides no public developer program or API.
  evidence:
  - status: 200
    url: https://www.cameo.com
  reason: no-developer-program
  state: none
created: '2026-10-06'
description: Cameo3 is a marketplace that connects fans with their favorite celebrities, allowing personalized video shoutouts and other fan experiences. Founded in 2017 and headquartered in Chicago, Illinois, Cameo has grown into a platform hosting thousands of talent across entertainment, sports, and business, offering a range of services for both consumers and creators.
layout: provider
modified: '2026-10-06'
name: Cameo3
nav: Providers
network: true
overview: 'Cameo3 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Celebrities, Gifts, and Business.


  Cameo3''s developer surface includes documentation and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 35.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cameo3 Domain Security
  slug: cameo3-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cameo3
tags:
- Celebrities
- Gifts
- Business
website: https://www.cameo.com
---
