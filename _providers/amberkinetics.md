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
  href: https://raw.githubusercontent.com/api-evangelist/amberkinetics/refs/heads/main/llms/amberkinetics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amberkinetics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amberkinetics/refs/heads/main/hosts/amberkinetics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amberkinetics-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://amberkinetics.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://amberkinetics.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amberkinetics/refs/heads/main/security/amberkinetics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amberkinetics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amberkinetics.com
coverage:
  checked: '2026-10-05'
  detail: No API contract or documentation was found at api.amberkinetics.com or amberkinetics.com.
  evidence:
  - status: 0
    url: https://api.amberkinetics.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Amberkinetics is a biotechnology startup focused on synthetic biology and life‑science research. It develops engineered microbial platforms for sustainable production of high‑value compounds, aiming to accelerate innovation in biotech and provide scalable solutions for industry and academia. The company emerged from the API Evangelist harvest backlog and is being profiled for its API ecosystem.
image: https://amberkinetics.com/wp-content/uploads/2020/05/amber-kinetics-social.png
layout: provider
modified: '2026-09-24'
name: Amberkinetics
nav: Providers
network: true
overview: Amberkinetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Synthetic Biology, Research, and Innovation.
random_paper: 13
score:
  band: minimal
  composite: 4.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.5
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amberkinetics Domain Security
  slug: amberkinetics-domain-security
  summary_line: TLSv1.2
slug: amberkinetics
tags:
- Company
- Biotechnology
- Synthetic Biology
- Research
- Innovation
- Life Sciences
website: https://amberkinetics.com
---
