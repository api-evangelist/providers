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
- description: Access control and pass management API
  name: Entrino API
  slug: entrino-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entrino/refs/heads/main/hosts/entrino-hosts.yml
  title: ''
  type: Hosts
  url: hosts/entrino-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/entrino/refs/heads/main/vendors/entrino-vendors.yml
  title: ''
  type: Vendors
  url: vendors/entrino-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.entrino.net/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/entrino/refs/heads/main/security/entrino-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/entrino-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://entrino.net/
coverage:
  checked: '2026-10-16'
  detail: Entrino's homepage requires region selection and renders content via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.entrino.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Entrino.net provides access control and pass management solutions for venues and events. Their platform enables organizers to manage visitor entry, issue digital passes, and enforce security policies in real time. With multi‑regional support, Entrino offers customizable access rules, analytics, and integration options for ticketing systems, ensuring smooth and secure experiences for both staff and attendees.
layout: provider
modified: '2026-10-16'
name: Entrino.net
nav: Providers
network: true
overview: Entrino.net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Access Control, EventManagement, Security, Software-as-a-Service, and Entrino.
random_paper: 19
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Entrino Domain Security
  slug: entrino-domain-security
  summary_line: TLSv1.3
slug: entrino
tags:
- Access Control
- EventManagement
- Security
- Software-as-a-Service
- Entrino
website: https://entrino.net/
---
