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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wiz-freight-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiz-freight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wizfreight.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/wizfreight
coverage:
  checked: '2026-09-04'
  detail: 'Wiz Freight''s operating surface is gone: wizfreight.com now serves a GoDaddy Website Builder "Launching Soon" placeholder, the former booking portal at https://wizfreight.com/bookings returns 404 into that placeholder, and the platform host sit.wizfreight.net no longer resolves, after trade press reported in September 2025 that the Chennai digital forwarder had suspended export bookings amid an executive exodus.'
  evidence:
  - status: 200
    url: https://wizfreight.com/
  - status: 404
    url: https://wizfreight.com/bookings
  - status: 404
    url: https://wizfreight.com/openapi.json
  - status: 404
    url: https://wizfreight.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/wizfreight
  reason: defunct
  state: none
created: '2026-09-04'
description: 'Wiz Freight (Wiz Logtec Solutions Private Limited) was a Chennai, India based digital freight forwarder founded in 2020 by Ramkumar Ramachandran and Ramkumar Govindarajan, offering ocean, air and surface freight booking, instant rate discovery, live shipment tracking, digital documentation and multi-currency freight payments through its own technology platform. The company raised roughly $58.6M from Tiger Global Management, Nippon Express Holdings, SBI Investment, Stride Ventures, Foundamental and Axilor Ventures. Trade press reported in September 2025 that the company had suspended export bookings amid an executive exodus, and as of September 2026 its public surface is gone: wizfreight.com serves a GoDaddy Website Builder placeholder, the former booking portal path 404s, and the sit.wizfreight.net platform host no longer resolves. No developer program, API reference or machine-readable contract was ever published on a reachable host, and none survives today.'
layout: provider
modified: '2026-09-04'
name: Wiz Freight
nav: Providers
network: true
overview: Wiz Freight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, Freight Forwarding, and Supply Chain.
random_paper: 2
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Wiz Freight Domain Security
  slug: wiz-freight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wiz-freight
tags:
- Company
- Logistics
- Freight
- Freight Forwarding
- Supply Chain
- Shipping
- Transportation
- India
website: https://wizfreight.com/
---
