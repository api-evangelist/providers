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
  href: https://raw.githubusercontent.com/api-evangelist/biosqueeze/refs/heads/main/llms/biosqueeze-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biosqueeze-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biosqueeze/refs/heads/main/hosts/biosqueeze-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biosqueeze-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biosqueeze/refs/heads/main/vendors/biosqueeze-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biosqueeze-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biosqueeze.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://biosqueeze.com/team
- group: company
  title: ''
  type: Blog
  url: https://biosqueeze.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biosqueeze/refs/heads/main/security/biosqueeze-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biosqueeze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biosqueeze.com
coverage:
  checked: '2026-09-28'
  detail: No API surface discovered; attempts to fetch OpenAPI spec at https://api.biosqueeze.com/openapi.json returned no content.
  evidence:
  - status: 0
    url: https://api.biosqueeze.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-28'
description: BioSqueeze is a biomineralization platform company that provides engineered solutions for challenging subsurface problems across energy, defense, mining, infrastructure, and environmental sectors. By strengthening soils, sealing fluid pathways, and healing fractures, BioSqueeze enables increased bearing capacity, leak control, and infrastructure repair, with over 400 field deployments worldwide.
image: https://biosqueeze.com/assets/platform-home-subsurface.jpg
layout: provider
modified: '2026-09-28'
name: Biosqueeze
nav: Providers
network: true
overview: 'Biosqueeze is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biomineralization, SubsurfaceEngineering, Energy, Defense, and Mining.


  Biosqueeze''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
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
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biosqueeze Domain Security
  slug: biosqueeze-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biosqueeze
tags:
- Biomineralization
- SubsurfaceEngineering
- Energy
- Defense
- Mining
- Infrastructure
- Environmental
website: https://biosqueeze.com
---
