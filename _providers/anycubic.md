---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anycubic/refs/heads/main/llms/anycubic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anycubic-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anycubic/refs/heads/main/well-known/anycubic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anycubic-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anycubic/refs/heads/main/hosts/anycubic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anycubic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anycubic/refs/heads/main/vendors/anycubic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anycubic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://store.anycubic.com/policies/terms-of-service
- group: company
  title: ''
  type: Newsroom
  url: https://store.anycubic.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anycubic/refs/heads/main/security/anycubic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anycubic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anycubic.com
coverage:
  checked: 2026-09-25
  detail: No public developer program or API documentation found; attempts to fetch OpenAPI at api.anycubic.com returned no content.
  evidence:
  - status: 0
    url: https://api.anycubic.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: 'Anycubic is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
image: https://www.anycubic.com/k3c2.jpg
layout: provider
modified: '2026-09-25'
name: Anycubic
nav: Providers
network: true
overview: Anycubic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, FDM Printers, LCD Printers, Resin Materials, and Filament Materials.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anycubic Domain Security
  slug: anycubic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anycubic
tags:
- 3D Printing
- FDM Printers
- LCD Printers
- Resin Materials
- Filament Materials
- 3D Printing Accessories
- 3D Printing Software
website: https://www.anycubic.com
---
