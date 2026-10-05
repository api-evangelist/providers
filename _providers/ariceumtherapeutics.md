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
  href: https://raw.githubusercontent.com/api-evangelist/ariceumtherapeutics/refs/heads/main/llms/ariceumtherapeutics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ariceumtherapeutics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ariceumtherapeutics/refs/heads/main/hosts/ariceumtherapeutics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ariceumtherapeutics-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ariceumtherapeutics/refs/heads/main/security/ariceumtherapeutics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ariceumtherapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://ariceumtherapeutics.com
coverage:
  checked: 2026-09-26
  detail: The company website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: http://ariceumtherapeutics.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Ariceumtherapeutics is a biotech company focused on developing innovative radiopharmaceutical therapies for rare cancers. The firm aims to leverage cutting‑edge molecular targeting and imaging technologies to create precision treatments that improve patient outcomes while minimizing side effects. As a relatively new entrant in the oncology space, Ariceumtherapeutics is building its pipeline through collaborations with academic institutions and seeks to expand its clinical trial portfolio in the coming years.
layout: provider
modified: '2026-09-26'
name: Ariceumtherapeutics
nav: Providers
network: true
overview: Ariceumtherapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Oncology, Radiopharmaceuticals, and Clinical Trials.
random_paper: 15
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ariceumtherapeutics Domain Security
  slug: ariceumtherapeutics-domain-security
  summary_line: TLSv1.3
slug: ariceumtherapeutics
tags:
- Company
- Biotechnology
- Oncology
- Radiopharmaceuticals
- Clinical Trials
website: http://ariceumtherapeutics.com
---
