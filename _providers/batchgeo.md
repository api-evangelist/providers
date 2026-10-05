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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/batchgeo/refs/heads/main/llms/batchgeo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/batchgeo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/batchgeo/refs/heads/main/hosts/batchgeo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/batchgeo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/batchgeo/refs/heads/main/vendors/batchgeo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/batchgeo-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/batchgeo/refs/heads/main/security/batchgeo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/batchgeo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://batchgeo.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.batchgeo.com
- group: docs
  title: ''
  type: APIReference
  url: https://api.batchgeo.com
- group: commercial
  title: ''
  type: Pricing
  url: https://api.batchgeo.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blog.batchgeo.com
- group: operate
  title: ''
  type: Support
  url: https://support.batchgeo.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://api.batchgeo.com/signup/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://blog.batchgeo.com/mcp
  - status: 401
    url: https://support.batchgeo.com/mcp
  - status: 403
    url: https://equityzen.com/company/batchgeo
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: BatchGeo is a SaaS platform founded in 2006 that lets users create interactive Google Maps from spreadsheet data. It supports bulk address mapping, custom marker groups, and embedded maps for websites. Over 1.5 million live maps have been generated for users worldwide, serving sectors like real‑estate, sales, and nonprofit. The service offers free and Pro plans, a REST API for automated mapping, and extensive support resources.
layout: provider
modified: '2026-09-27'
name: Batchgeo
nav: Providers
network: true
overview: 'Batchgeo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mapping, Software-as-a-Service, Data Visualization, Real Estate, and Sales.


  Batchgeo''s developer surface includes documentation, API reference, pricing, engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Batchgeo Domain Security
  slug: batchgeo-domain-security
  summary_line: TLSv1.2 · DMARC
slug: batchgeo
tags:
- Mapping
- Software-as-a-Service
- Data Visualization
- Real Estate
- Sales
website: https://batchgeo.com
---
