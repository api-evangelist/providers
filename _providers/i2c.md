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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/i2c/refs/heads/main/llms/i2c-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/i2c-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.i2cinc.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/i2c/refs/heads/main/security/i2c-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/i2c-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.i2cinc.com/
coverage:
  checked: 2026-09-21
  detail: API spec URLs on apis.i2cinc.com return HTML shells instead of machine‑readable OpenAPI documents.
  evidence:
  - status: 200
    url: https://apis.i2cinc.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Outpace legacy and unproven modern platforms with i2c’s next generation platform and composable solutions built for speed, reliability and scale. i2c Inc. provides a comprehensive suite of banking and payments APIs, enabling fintechs and enterprises to integrate core financial services quickly and securely.
image: https://static-cdn.i2cinc.com/wp-content/uploads/2025/10/i2c-inc-Logo.jpg
layout: provider
modified: '2026-09-21'
name: i2c Inc.
nav: Providers
network: true
overview: 'i2c Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Payments, and Fintech.


  i2c Inc.''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: I2C Domain Security
  slug: i2c-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: i2c
tags:
- Company
- Banking
- Payments
- Fintech
website: https://www.i2cinc.com/
---
