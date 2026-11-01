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
- group: other
  href: https://artifacts.apis.io/20tree-ai/hosts/20tree-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/20tree-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/20tree-ai/vendors/20tree-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/20tree-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.overstory.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.overstory.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.overstory.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.overstory.com/blog
- group: auth
  href: https://artifacts.apis.io/20tree-ai/security/20tree-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/20tree-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.overstory.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://20tree.ai/
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Overstory provides actionable vegetation intelligence to electric utilities, helping them optimize resources, mitigate vegetation risk, and future‑proof operations against climate and market challenges. Their platform directs pruning efforts to reduce wildfires and power outages, delivering safer, more reliable power.
image: http://static1.squarespace.com/static/6065a3e68fb0fa053417527f/t/6093bfa2df4b06579d0d7f11/1626340435165/unsplash-image-uMWPrcRsrto.jpg?format=1500w
layout: provider
modified: '2026-10-29'
name: Overstory
nav: Providers
network: true
overview: 'Overstory is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Utilities, Vegetation, and AI.


  Overstory''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 7.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 20Tree Ai Domain Security
  slug: 20tree-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 20tree-ai
tags:
- Company
- Energy
- Utilities
- Vegetation
- AI
website: https://www.overstory.com/
---
