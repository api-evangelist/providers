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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Avenda Health provides healthcare data services.
  name: Avenda Health API
  slug: avenda-health-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avenda-health/refs/heads/main/hosts/avenda-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avenda-health-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avenda-health/refs/heads/main/security/avenda-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avenda-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.avendahealth.com/
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract discovered despite probing known API hosts.
  evidence:
  - status: 403
    url: https://api.avendahealth.com/openapi.json
  - status: 403
    url: https://api.avendahealth.com/openapi.yaml
  - status: 403
    url: https://api.avendahealth.com/swagger.json
  - status: 403
    url: https://api.avendahealth.com/v1/openapi.json
  - status: 403
    url: https://api.avendahealth.com/api-docs
  - status: 403
    url: https://api.avendahealth.com/docs
  - status: 403
    url: https://api.avendahealth.com/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Avenda Health is a privately held healthcare technology company founded in 2017 and based in Culver City, California. It focuses on AI‑driven cancer detection solutions, notably its FDA‑cleared Unfold AI platform that helps oncologists identify invisible cancers, improving treatment outcomes and patient quality of life. The company employs 11‑50 staff and aims to build a world where no patient dies of cancer.
layout: provider
modified: '2026-09-26'
name: Avenda Health
nav: Providers
network: true
overview: Avenda Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Oncology, and Technology.
random_paper: 0
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avenda Health Domain Security
  slug: avenda-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: avenda-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Oncology
- Technology
website: https://www.avendahealth.com/
---
