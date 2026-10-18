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
- description: Credflow provides AI‑driven credentialing and payer enrollment APIs. Documentation page not found; attempts to locate OpenAPI spec returned 404/401.
  name: Credflow API
  slug: credflow-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credflow/refs/heads/main/hosts/credflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/credflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/credflow/refs/heads/main/vendors/credflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/credflow-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credflow.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credflow.ai/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/credflow/refs/heads/main/security/credflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/credflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credflow.ai
created: '2026-10-11'
description: CredFlow AI provides AI‑driven credentialing and payer enrollment solutions for healthcare providers. Their platform automates credentialing software, services, and modules, offering network lookup, payer directory auditing, and AI telecaller agents. The service supports CAQH, Medicare PECOS, and major insurers, handling applications across 22 payer portals with high completion rates.
image: https://www.credflow.ai/images/logoo.png
layout: provider
modified: '2026-10-11'
name: Credflow
nav: Providers
network: true
overview: Credflow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Healthcare, Artificial Intelligence, and Credentialing.
random_paper: 18
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
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
    score: 10.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Credflow Domain Security
  slug: credflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: credflow
tags:
- Company
- Fintech
- Healthcare
- Artificial Intelligence
- Credentialing
website: https://www.credflow.ai
---
