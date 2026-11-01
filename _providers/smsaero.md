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
  href: https://artifacts.apis.io/smsaero/hosts/smsaero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smsaero-hosts.yml
- group: build
  href: https://artifacts.apis.io/smsaero/packages/smsaero-packages.yml
  title: ''
  type: SDKs
  url: packages/smsaero-packages.yml
- group: build
  href: https://artifacts.apis.io/smsaero/packages/smsaero-packages.yml
  title: ''
  type: Packages
  url: packages/smsaero-packages.yml
- group: auth
  href: https://artifacts.apis.io/smsaero/security/smsaero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smsaero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smsaero.ru/
coverage:
  checked: '2026-10-27'
  detail: Documentation at https://smsaero.ru/docs/ is a JavaScript‑rendered HTML site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://smsaero.ru/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: SMS Aero provides a mass SMS messaging service with guaranteed delivery, offering API access for sending bulk SMS, managing contacts, and tracking delivery reports. The platform supports multiple languages, integrates with popular frameworks, and includes features such as scheduling, personalization, and analytics to help businesses communicate effectively with their customers worldwide.
layout: provider
modified: '2026-10-27'
name: SMS Aero
nav: Providers
network: true
overview: SMS Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Messaging, Bulk, and API.
random_paper: 18
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 51.8
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
  name: Smsaero Domain Security
  slug: smsaero-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: smsaero
tags:
- Company
- SMS
- Messaging
- Bulk
- API
website: https://smsaero.ru/
---
