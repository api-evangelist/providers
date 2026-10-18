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
  href: https://raw.githubusercontent.com/api-evangelist/algorized/refs/heads/main/llms/algorized-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algorized-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algorized/refs/heads/main/hosts/algorized-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algorized-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algorized/refs/heads/main/vendors/algorized-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algorized-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.algorized.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algorized/refs/heads/main/security/algorized-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algorized-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.algorized.com
coverage:
  checked: '2026-10-05'
  detail: The company website provides no developer documentation or API reference.
  evidence:
  - status: 200
    url: https://www.algorized.com
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Algorized develops edge-native nervous system technologies for physical AI, creating sensing and perception solutions that protect life by detecting human presence, tracking, positioning, and vital signs even through obstacles. Their sustainable, unobtrusive edge‑AI models integrate seamlessly with people, places, and sensors across robotics, industrial, and safety applications, aiming to reduce risk and enhance wellbeing.
image: https://static.wixstatic.com/media/4c9199_9c103d27490e43e2b0170511a37e8526%7Emv2.png/v1/fit/w_2500,h_1330,al_c/4c9199_9c103d27490e43e2b0170511a37e8526%7Emv2.png
layout: provider
modified: '2026-09-24'
name: Algorized
nav: Providers
network: true
overview: Algorized is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Edge Computing, Robotics, and Safety.
random_paper: 15
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Algorized Domain Security
  slug: algorized-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: algorized
tags:
- Company
- Artificial Intelligence
- Edge Computing
- Robotics
- Safety
website: https://www.algorized.com
---
