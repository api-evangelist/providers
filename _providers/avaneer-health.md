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
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://avaneerhealth.com/security/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaneer-health/refs/heads/main/hosts/avaneer-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avaneer-health-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avaneer-health/refs/heads/main/vendors/avaneer-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avaneer-health-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.avaneerhealth.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaneer-health/refs/heads/main/security/avaneer-health-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/avaneer-health-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avaneer-health/refs/heads/main/security/avaneer-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avaneer-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avaneerhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://avaneerhealth.com/category/press/
coverage:
  checked: 2026-09-26
  detail: Developer portal returns HTML shells for OpenAPI endpoints, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://developer.avaneerhealth.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Avaneer Health provides a real‑time healthcare revenue cycle management platform that connects payers and providers to deliver accurate insurance coverage information instantly. By simplifying data exchange, Avaneer improves outcomes, reduces claim errors, and accelerates care delivery across the healthcare ecosystem.
layout: provider
modified: '2026-09-26'
name: Avaneer Health
nav: Providers
network: true
overview: 'Avaneer Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Revenue Cycle, Interoperability, Real-Time Data, and API Platform.


  Avaneer Health''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avaneer Health Domain Security
  slug: avaneer-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Avaneer Health Trust Center
  slug: avaneer-health-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: avaneer-health
tags:
- Healthcare
- Revenue Cycle
- Interoperability
- Real-Time Data
- API Platform
website: https://avaneerhealth.com/
---
