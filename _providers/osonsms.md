---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cloud-based SMS messaging API as described in the PDF documentation.
  name: Oson SMS API
  slug: oson-sms-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/osonsms/hosts/osonsms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/osonsms-hosts.yml
- group: auth
  href: https://artifacts.apis.io/osonsms/security/osonsms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/osonsms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://osonsms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://osonsms.com/docs/sms-api-documentation.pdf
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cab.osonsms.com/
- group: start
  title: ''
  type: SignUp
  url: https://cab.osonsms.com/signup
- group: start
  title: ''
  type: Login
  url: https://cab.osonsms.com/login
coverage:
  checked: '2026-10-26'
  detail: API documentation is provided only as a PDF file with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://osonsms.com/docs/sms-api-documentation.pdf
  reason: pdf-only-docs
  state: unreadable
created: '2026-10-26'
description: Oson SMS provides a cloud‑based SMS messaging platform for businesses in Tajikistan and the surrounding region, enabling bulk SMS sending, personalized campaigns, delivery analytics, and integration options. The service supports multiple payment methods, detailed reporting, partner programs, and offers branded sender IDs with real‑time statistics for engaging customers via text messages.
layout: provider
modified: '2026-10-26'
name: Oson SMS
nav: Providers
network: true
overview: 'Oson SMS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SMS, Messaging, Cloud, and Communications.


  Oson SMS''s developer surface includes documentation, signup flow, and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 5.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/osonsms/osonsms-2026-11-03T140751.png
security:
- kind: domain-security
  name: Osonsms Domain Security
  slug: osonsms-domain-security
  summary_line: TLSv1.2
slug: osonsms
tags:
- Company
- SMS
- Messaging
- Cloud
- Communications
website: https://osonsms.com/
---
