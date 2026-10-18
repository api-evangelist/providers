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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/coremedic/refs/heads/main/llms/coremedic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coremedic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremedic/refs/heads/main/hosts/coremedic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coremedic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coremedic/refs/heads/main/vendors/coremedic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coremedic-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coremedic/refs/heads/main/security/coremedic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coremedic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coremedic.de
coverage:
  checked: '2026-10-11'
  detail: Coremedic provides no public developer program or API documentation.
  evidence:
  - status: 0
    url: https://api.coremedic.de
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Coremedic GmbH is a privately held medical device company headquartered in Radolfzell, Germany, with a subsidiary in Biel, Switzerland. Founded in 2012 as a spin‑out from the University of Bern, Coremedic develops minimally invasive treatments for mitral valve regurgitation, notably the ChordArt TMVr system. The company focuses on innovative cardiology solutions, holds EN ISO 13485 certification, and operates within the European medical technology market, offering detailed product information, clinical data, and contact resources through its website.
layout: provider
modified: '2026-10-10'
name: Coremedic
nav: Providers
network: true
overview: Coremedic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Cardiology, Mitral Valve, Germany, and Healthcare.
random_paper: 15
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coremedic Domain Security
  slug: coremedic-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coremedic
tags:
- Medical Devices
- Cardiology
- Mitral Valve
- Germany
- Healthcare
website: https://www.coremedic.de
---
