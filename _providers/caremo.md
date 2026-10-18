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
  href: https://raw.githubusercontent.com/api-evangelist/caremo/refs/heads/main/llms/caremo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caremo-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/caremo/refs/heads/main/hosts/caremo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caremo-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caremo.net/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://caremo.net/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/caremo/refs/heads/main/security/caremo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caremo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caremo.net
coverage:
  checked: '2026-10-07'
  detail: Caremo provides home caregiving services and does not expose a software API.
  evidence:
  - status: 0
    url: https://api.caremo.net
  reason: not-a-software-company
  state: none
created: '2026-10-07'
description: Caremo is a private in‑home caregiving company owned by Four Vanguards LLC, providing personalized nursing, therapy, and companion services to seniors and post‑operative patients in the San Mateo County area. Founded in 2018, CareMo emphasizes compassionate, family‑like care, offering customized care plans, 24‑hour support, and a range of specialized services such as stroke recovery, Alzheimer’s care, and COVID‑19 rehabilitation. The company’s mission is to make clients feel loved, valued, and well‑cared for through high‑quality, affordable home health solutions.
layout: provider
modified: '2026-10-07'
name: Caremo
nav: Providers
network: true
overview: 'Caremo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HomeHealth, Caregiving, SeniorCare, and Therapy.


  Caremo''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Caremo Domain Security
  slug: caremo-domain-security
  summary_line: TLSv1.3
slug: caremo
tags:
- Company
- HomeHealth
- Caregiving
- SeniorCare
- Therapy
- California
website: https://caremo.net
---
