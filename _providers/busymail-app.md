---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/busymail-app/well-known/busymail-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/busymail-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/busymail-app/hosts/busymail-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/busymail-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/busymail-app/vendors/busymail-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/busymail-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://busymail.app/terms
- group: operate
  title: ''
  type: Support
  url: https://busymail.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://busymail.app/privacy
- group: company
  title: ''
  type: Blog
  url: https://busymail.app/blog
- group: auth
  href: https://artifacts.apis.io/busymail-app/security/busymail-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/busymail-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://busymail.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://busymail.app/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://busymail.app/signup
- group: other
  title: ''
  type: Download
  url: https://busymail.app/download
coverage:
  checked: '2026-11-03'
  detail: No public API documentation or machine‑readable contract was found on the provider’s hosts.
  evidence:
  - status: 0
    url: https://api.busymail.app/openapi.json
  - status: 404
    url: https://dl.busymail.app/openapi.json
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Busymail is an AI‑enhanced email client that connects to Gmail, Yahoo and any IMAP server, reads your inbox and surfaces actionable items such as replies, bills and travel details. It offers a 14‑day free trial, then $15 /month with a refund guarantee.
image: https://busymail.app/og-image.png
layout: provider
modified: '2026-11-03'
name: Busymail
nav: Providers
network: true
overview: 'Busymail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Email, Artificial Intelligence, Productivity, Software-as-a-Service, and IMAP.


  Busymail''s developer surface includes support, engineering blog, pricing, signup flow, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Busymail App Domain Security
  slug: busymail-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: busymail-app
tags:
- Email
- Artificial Intelligence
- Productivity
- Software-as-a-Service
- IMAP
- Company
website: https://busymail.app/
---
