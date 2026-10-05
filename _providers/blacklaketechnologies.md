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
  href: https://raw.githubusercontent.com/api-evangelist/blacklaketechnologies/refs/heads/main/llms/blacklaketechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blacklaketechnologies-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blacklaketechnologies/refs/heads/main/hosts/blacklaketechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacklaketechnologies-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacklaketechnologies/refs/heads/main/security/blacklaketechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacklaketechnologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.blacklake.tech
coverage:
  checked: '2026-09-29'
  detail: The company website provides no developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://www.blacklake.tech
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Black Lake Technologies provides an Industrial AI platform delivering AI agents that automate and optimize manufacturing operations. Their solutions cover order processing, scheduling, and fulfillment, leveraging data-driven decision-making across factories. Serving over 40,000 factories and 2 million users, the platform claims 95% decision accuracy and supports 30+ industries, aiming to transform traditional production into agile, AI‑enabled processes.
layout: provider
modified: '2026-09-29'
name: Blacklaketechnologies
nav: Providers
network: true
overview: Blacklaketechnologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Manufacturing, Industrial, and Platform.
random_paper: 6
score:
  band: minimal
  composite: 3.7
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blacklaketechnologies Domain Security
  slug: blacklaketechnologies-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: blacklaketechnologies
tags:
- Company
- Artificial Intelligence
- Manufacturing
- Industrial
- Platform
website: https://www.blacklake.tech
---
