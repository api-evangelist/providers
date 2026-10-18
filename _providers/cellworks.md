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
api_count: 1
apis:
- description: Actionable AI platform for precision medicine, providing case analysis and therapeutic decision support.
  name: Cellworks API
  slug: cellworks-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellworks/refs/heads/main/hosts/cellworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cellworks-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cellworks/refs/heads/main/vendors/cellworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cellworks-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cellworks/refs/heads/main/security/cellworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cellworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cellworks.life
coverage:
  checked: '2026-10-07'
  detail: Portal pages return HTML shells with no OpenAPI or other machine‑readable contract discovered.
  evidence:
  - status: 404
    url: https://portal.cellworks.life/openapi.json
  - status: 200 (HTML shell)
    url: https://portaladmin.cellworks.life/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cellworks provides actionable AI for individualized precision medicine, integrating mechanistic biology, clinical guidelines, and over 300 million patient records to predict individual drug responses. Their platform serves bio‑pharma companies, physicians, and health systems with tools for case analysis, evidence generation, and therapeutic decision support.
image: https://cellworks.life/logo.png
layout: provider
modified: '2026-10-07'
name: Cellworks
nav: Providers
network: true
overview: Cellworks is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Precision Medicine, Healthcare, and BioPharma.
random_paper: 14
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cellworks Domain Security
  slug: cellworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cellworks
tags:
- Company
- Artificial Intelligence
- Precision Medicine
- Healthcare
- BioPharma
website: https://cellworks.life
---
