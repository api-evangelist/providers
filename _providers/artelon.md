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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/artelon/refs/heads/main/llms/artelon-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artelon-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artelon/refs/heads/main/hosts/artelon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artelon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artelon/refs/heads/main/vendors/artelon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/artelon-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artelon/refs/heads/main/security/artelon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artelon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artelon.com/
coverage:
  checked: 2026-09-26
  detail: No machine‑readable API specification found on the company site or API subdomains.
  evidence:
  - status: 200
    url: https://www.artelon.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Artelon, now part of Stryker, develops dynamic synthetic implants for tendon and ligament injuries. Founded by orthopedic surgeon Lars Peterson, the company combines expertise in chemistry and textile engineering to create the Artelon FlexBand product, enhancing tissue strength and recovery. Their website offers detailed information on science, surgical indications, patient experiences, and product education, reflecting a commitment to innovative orthopedic solutions.
image: https://static.wixstatic.com/media/09eb1b_de9df8ab919b4109bdd15a974fc5a604%7Emv2.png/v1/fit/w_2500,h_1330,al_c/09eb1b_de9df8ab919b4109bdd15a974fc5a604%7Emv2.png
layout: provider
modified: '2026-09-26'
name: Artelon
nav: Providers
network: true
overview: Artelon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Orthopedic, Medical Devices, Synthetic Implants, and FlexBand.
random_paper: 9
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artelon Domain Security
  slug: artelon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artelon
tags:
- Company
- Orthopedic
- Medical Devices
- Synthetic Implants
- FlexBand
website: https://www.artelon.com/
---
