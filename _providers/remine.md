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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/remine/refs/heads/main/hosts/remine-hosts.yml
  title: ''
  type: Hosts
  url: hosts/remine-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/remine/refs/heads/main/vendors/remine-vendors.yml
  title: ''
  type: Vendors
  url: vendors/remine-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.remine.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/remine/refs/heads/main/security/remine-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/remine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://remine.com/
- group: operate
  title: ''
  type: Support
  url: https://support.remine.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://mortgage.remine.com/signup
- group: company
  title: ''
  type: Partner
  url: https://remine.com/mlss-associations
- group: commercial
  title: ''
  type: TermsOfService
  url: https://remine.com/tos-privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remine
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://blog.remine.com/mcp
  - status: 403
    url: https://help.remine.com/mcp
  - status: 403
    url: https://info.remine.com/mcp
  - status: 200
    url: https://remine.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Remine is a Bellingham, Washington-based real estate data and prospecting platform delivered to agents, lenders, MLSs and REALTOR associations, often as an MLS member benefit. It combines property, owner, tax and mortgage data (including distressed deals, rate and loan duration) with predictive likely-to-sell analytics, nationwide map search and lead contact information, alongside Remine Pro and Remine Docs (document storage, sharing and e-signature). Remine publishes no public API, developer documentation or machine-readable contract; product help is in its Zendesk support center.
image: https://remine.com/wp-content/uploads/2025/12/remine-og.jpg
layout: provider
modified: '2026-10-13'
name: Remine
nav: Providers
network: true
overview: 'Remine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Property Data, Mortgage Data, and Lead Generation.


  Remine''s developer surface includes documentation, support, signup flow, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Remine Domain Security
  slug: remine-domain-security
  summary_line: TLSv1.3 · DMARC
slug: remine
tags:
- Company
- Real Estate
- Property Data
- Mortgage Data
- Lead Generation
- Predictive Analytics
- MLS
website: https://remine.com/
---
