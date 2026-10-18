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
  href: https://raw.githubusercontent.com/api-evangelist/blendr/refs/heads/main/hosts/blendr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blendr-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blendr/refs/heads/main/security/blendr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blendr-domain-security.yml
coverage:
  checked: '2026-10-16'
  detail: Blendr.io no longer offers an API after its acquisition by Qlik, and all attempted spec URLs return 404.
  evidence:
  - status: 404
    url: https://api.blendr.io/openapi.json
  - status: 404
    url: https://api.blendr.io/swagger.json
  reason: defunct
  state: none
created: '2026-10-16'
description: Blendr.io was a data integration and workflow automation platform that enabled developers to connect SaaS applications and automate business processes via APIs. The company was acquired by Qlik, and its former domain now redirects to Qlik Automate, indicating the technology has been integrated into Qlik’s suite of AI‑driven analytics and automation tools. Blendr.io’s original offering focused on low‑code integration, event‑driven workflows, and a RESTful API for managing connectors and tasks.
layout: provider
modified: '2026-10-16'
name: Blendr.io
nav: Providers
network: true
overview: Blendr.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Integration, Automation, Workflows, Software-as-a-Service, and Data.
random_paper: 15
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 4
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
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blendr Domain Security
  slug: blendr-domain-security
  summary_line: DMARC
slug: blendr
tags:
- Integration
- Automation
- Workflows
- Software-as-a-Service
- Data
---
