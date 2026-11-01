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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/eurosms/hosts/eurosms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eurosms-hosts.yml
- group: auth
  href: https://artifacts.apis.io/eurosms/security/eurosms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eurosms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eurosms.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://eurosms.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: EuroSms provides bulk SMS sending services via web and API integrations, offering XML, HTTP and WebService interfaces for businesses in Slovakia, Czechia, Hungary and Austria. Their platform supports sending SMS from Excel, Outlook, and custom applications, with features like two‑way messaging, delivery reports, and GDPR‑compliant data handling. Documentation includes API reference, pricing, and integration guides.
layout: provider
modified: '2026-10-28'
name: EuroSms
nav: Providers
network: true
overview: EuroSms is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, BulkMessaging, API, and Slovakia.
random_paper: 14
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eurosms Domain Security
  slug: eurosms-domain-security
  summary_line: DMARC
slug: eurosms
tags:
- Company
- SMS
- BulkMessaging
- API
- Slovakia
website: https://eurosms.com/
---
