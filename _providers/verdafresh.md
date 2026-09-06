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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://verdafresh.com/
- group: company
  title: ''
  type: Blog
  url: https://verdafresh.com/news
- group: operate
  title: ''
  type: Support
  url: mailto:info@verdafresh.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verdafresh-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verdafresh-llms.txt
coverage:
  checked: '2026-09-02'
  detail: VerdaFresh sells oxygen barrier coatings and coated plastic film to packaging converters — its entire web presence is a five-page brochure whose only downloads are PDF product datasheets, and api., developer., developers., docs. and app.verdafresh.com all return NXDOMAIN.
  evidence:
  - status: 200
    url: https://verdafresh.com/
  - status: 404
    url: https://verdafresh.com/openapi.json
  - status: 404
    url: https://verdafresh.com/.well-known/agent-card.json
  - status: 404
    url: https://verdafresh.com/llms.txt
  - status: 0
    url: https://api.verdafresh.com/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: VerdaFresh is a Wayne, Pennsylvania materials-science company that develops water-based, saran-free oxygen barrier coatings for recyclable flexible food packaging. Its High Oxygen Barrier and Ultra High Barrier coatings are applied to BOPP, HD-BOPE, MDO-PE and PET film substrates to extend shelf life while keeping the finished package mono-material and recyclable, replacing PVdC and metallized structures. The company sells coatings and coated films to converters and CPG brands, is APR-recognized and a member of the U.S. Plastics Pact, and publishes technical datasheets rather than software. It is a physical-products manufacturer with no developer program, API, SDK or machine-readable interface of any kind.
image: https://verdafresh.com/assets/images/favicons/apple-touch-icon.png
layout: provider
modified: '2026-09-02'
name: VerdaFresh
nav: Providers
network: true
overview: 'VerdaFresh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Packaging, Flexible Packaging, Food Packaging, and Materials Science.


  VerdaFresh''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Verdafresh Domain Security
  slug: verdafresh-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: verdafresh
tags:
- Company
- Packaging
- Flexible Packaging
- Food Packaging
- Materials Science
- Barrier Coatings
- Recycling
- Sustainability
- Circular Economy
- Manufacturing
website: https://verdafresh.com/
---
