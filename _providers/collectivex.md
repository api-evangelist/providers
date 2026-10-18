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
  href: https://raw.githubusercontent.com/api-evangelist/collectivex/refs/heads/main/hosts/collectivex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/collectivex-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.collectivex.ai/signup.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/collectivex/refs/heads/main/security/collectivex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/collectivex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.collectivex.ai
coverage:
  checked: '2026-10-09'
  detail: No public developer program or API documentation is available.
  evidence:
  - status: 200
    url: https://www.collectivex.ai
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CollectiveX is an AI‑powered healthcare platform that combines global medical expertise with advanced artificial intelligence to enhance diagnostic accuracy, improve patient outcomes, and accelerate medical research and education. The platform offers diagnosis support, treatment planning, and collaborative research tools for clinicians and researchers worldwide.
layout: provider
modified: '2026-10-09'
name: Collectivex
nav: Providers
network: true
overview: 'Collectivex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Artificial Intelligence, Diagnostics, Research, and Platform.


  Collectivex''s developer surface includes signup flow and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Collectivex Domain Security
  slug: collectivex-domain-security
  summary_line: TLSv1.3
slug: collectivex
tags:
- Healthcare
- Artificial Intelligence
- Diagnostics
- Research
- Platform
- Company
website: https://www.collectivex.ai
---
