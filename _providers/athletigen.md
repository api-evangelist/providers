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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/athletigen/refs/heads/main/hosts/athletigen-hosts.yml
  title: ''
  type: Hosts
  url: hosts/athletigen-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/athletigen/refs/heads/main/security/athletigen-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/athletigen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://athletigen.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on api.athletigen.com or athletigen.com.
  evidence:
  - status: 0
    url: https://api.athletigen.com/openapi.json
  - status: 0
    url: https://api.athletigen.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Athletigen is a health‑focused biotechnology company that provides personalized genetic and biomarker insights to help individuals optimize nutrition, fitness, and wellness. Their platform leverages DNA testing and advanced analytics to deliver actionable recommendations for diet, exercise, and lifestyle. The company aims to empower users with data‑driven guidance for better health outcomes.
image: https://img1.wsimg.com/isteam/videos/uA41GmyyG8IMaxXdb
layout: provider
modified: '2026-09-26'
name: Athletigen
nav: Providers
network: true
overview: Athletigen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Biotechnology, Genetics, and Wellness.
random_paper: 5
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 48.2
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
  name: Athletigen Domain Security
  slug: athletigen-domain-security
  summary_line: TLSv1.3 · HSTS
slug: athletigen
tags:
- Company
- Health
- Biotechnology
- Genetics
- Wellness
website: https://athletigen.com
---
