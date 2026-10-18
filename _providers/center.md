---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 6.5
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/center/refs/heads/main/well-known/center-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/center-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/center/refs/heads/main/hosts/center-hosts.yml
  title: ''
  type: Hosts
  url: hosts/center-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/center/refs/heads/main/vendors/center-vendors.yml
  title: ''
  type: Vendors
  url: vendors/center-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://center.com/terms?lang=en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://center.com/privacy?lang=en
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/center/refs/heads/main/security/center-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/center-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://center.com/
coverage:
  checked: '2026-10-07'
  detail: The provider’s documentation is only available via a JavaScript‑rendered site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://center.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-07'
description: Center is a personal assistant platform that operates via SMS and messaging. Users can text Center to ask questions, make bookings, manage errands, and access integrated services like Gmail, Google Calendar, Drive, and Contacts. The service emphasizes privacy, offering opt‑out options and clear terms. It targets consumers seeking convenient, text‑based interactions for daily tasks and information retrieval.
layout: provider
modified: '2026-10-07'
name: Center
nav: Providers
network: true
overview: Center is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PersonalAssistant, SMS, Messaging, and Artificial Intelligence.
random_paper: 3
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Center Domain Security
  slug: center-domain-security
  summary_line: TLSv1.3 · DMARC
slug: center
tags:
- Company
- PersonalAssistant
- SMS
- Messaging
- Artificial Intelligence
- Privacy
website: https://center.com/
---
