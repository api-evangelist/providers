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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Albi provides a REST API documented at the Help Center.
  name: Albi API
  slug: albi-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/albi/refs/heads/main/conformance/albi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/albi-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/albi/refs/heads/main/well-known/albi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/albi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/albi/refs/heads/main/hosts/albi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/albi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/albi/refs/heads/main/vendors/albi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/albi-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.albiware.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/albi/refs/heads/main/security/albi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/albi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://albiware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://albiware.com/resource-center/
- group: docs
  title: ''
  type: APIReference
  url: https://help.albiware.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://albiware.com/book-demo
- group: operate
  title: ''
  type: Support
  url: https://help.albiware.com/
- group: company
  title: ''
  type: Blog
  url: https://albiware.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://albiware.com/albi-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://albiware.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://albiware.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://albiware.com/login
coverage:
  checked: '2026-10-05'
  detail: Probing common OpenAPI endpoints on api.albiware.com returned 404, and no other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://api.albiware.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Albi provides a cloud‑based restoration management platform for contractors and service providers. The software unifies job management, field documentation, AI‑driven analytics, mobile scheduling, e‑signatures, and integrations with thousands of third‑party tools. Albi offers tiered subscription plans (Base, Pro, Enterprise) and emphasizes rapid onboarding, 24‑hour support, and a marketplace of add‑ons. The platform is marketed to restoration businesses seeking to consolidate operations into a single web and mobile application.
image: https://albiware.com/wp-content/uploads/albi_1200x630.png
layout: provider
modified: '2026-09-24'
name: Albi
nav: Providers
network: true
overview: 'Albi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restoration, Software, Software-as-a-Service, Cloud, and Management.


  Albi''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.6
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 2.1
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Albi Domain Security
  slug: albi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: albi
tags:
- Restoration
- Software
- Software-as-a-Service
- Cloud
- Management
website: https://albiware.com/
---
