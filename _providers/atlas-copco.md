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
  href: https://raw.githubusercontent.com/api-evangelist/atlas-copco/refs/heads/main/hosts/atlas-copco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-copco-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-copco/refs/heads/main/vendors/atlas-copco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-copco-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlascopco.com/en-uk/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlascopco.com/fr-dz/compressors/service/plans
- group: company
  title: ''
  type: Newsroom
  url: https://www.atlascopco.com/fr-dz/news
- group: company
  title: ''
  type: Blog
  url: https://www.atlascopco.com/fr-dz/rental/resources/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-copco/refs/heads/main/security/atlas-copco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-copco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlascopco.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI or other machine-readable spec found on api.atlascopco.com.
  evidence:
  - status: 0
    url: https://api.atlascopco.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Atlas Copco is a global industrial company that provides sustainable productivity solutions, including compressors, vacuum solutions, generators, pumps, power tools, and assembly systems. With a presence in over 180 markets, it focuses on innovation, energy efficiency, and digital services to help customers improve performance and reduce environmental impact. The company’s extensive portfolio serves industries such as manufacturing, construction, mining, and automotive, delivering equipment and services that enhance operational efficiency and reliability.
layout: provider
modified: '2026-10-14'
name: Atlas Copco
nav: Providers
network: true
overview: 'Atlas Copco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial, Manufacturing, Energy, and Tools.


  Atlas Copco''s developer surface includes pricing, engineering blog, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atlas Copco Domain Security
  slug: atlas-copco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atlas-copco
tags:
- Company
- Industrial
- Manufacturing
- Energy
- Tools
website: https://atlascopco.com/
---
