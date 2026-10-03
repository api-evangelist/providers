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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/llms/belfry-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/belfry-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/well-known/belfry-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/belfry-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/well-known/belfry-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/belfry-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/hosts/belfry-hosts.yml
  title: ''
  type: Hosts
  url: hosts/belfry-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/vendors/belfry-vendors.yml
  title: ''
  type: Vendors
  url: vendors/belfry-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.belfrysoftware.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.belfrysoftware.com/tag/news
- group: start
  title: ''
  type: Login
  url: https://www.belfrysoftware.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/belfry/refs/heads/main/security/belfry-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/belfry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.belfrysoftware.com
- group: company
  title: ''
  type: About
  url: https://www.belfrysoftware.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.belfrysoftware.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.belfrysoftware.com/plans
- group: start
  title: ''
  type: Demo
  url: https://www.belfrysoftware.com/demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.belfrysoftware.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.belfrysoftware.com/terms-of-service
coverage:
  checked: '2026-09-27'
  detail: Provider's website hosts documentation pages but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://www.belfrysoftware.com/plans
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Belfry Software provides security guard management software, offering scheduling, timekeeping, operations, payroll, and billing solutions for security companies. Their platform includes AI-driven teammate features, recruiting tools, and on-demand pay for officers, aiming to streamline security operations and improve workforce efficiency.
image: https://cdn.prod.website-files.com/64dd01bc406bf2448a2f2b56/65037007465310f0f8179b6c_Belfry%20Gradient%20Logo%20XXS.png
layout: provider
modified: '2026-09-27'
name: Belfry
nav: Providers
network: true
overview: 'Belfry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Software, Scheduling, Payroll, and GuardManagement.


  Belfry''s developer surface includes engineering blog, pricing, and 14 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Belfry Domain Security
  slug: belfry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: belfry
tags:
- Security
- Software
- Scheduling
- Payroll
- GuardManagement
website: https://www.belfrysoftware.com
---
