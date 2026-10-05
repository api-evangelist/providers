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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Auris provides payroll and HR APIs documented at the resources page.
  name: Auris API
  slug: auris-api
artifact_total: 4
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/llms/auris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auris-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/well-known/auris-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/auris-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/well-known/auris-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auris-well-known.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/plans/auris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auris-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/security/auris-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/auris-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/hosts/auris-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auris-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/vendors/auris-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auris-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.auris.io/press/
- group: start
  title: ''
  type: Login
  url: https://www.auris.io/login/
- group: other
  title: ''
  type: Leadership
  url: https://www.auris.io/about-us/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/security/auris-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/auris-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/auris/refs/heads/main/security/auris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auris-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.auris.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.auris.io/resources/
- group: company
  title: ''
  type: Blog
  url: https://www.auris.io/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.auris.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auris.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auris.io/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.auris.io/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.auris.io/get-started/
coverage:
  checked: 2026-09-26
  detail: API documentation is only available as HTML pages; no machine‑readable OpenAPI/AsyncAPI spec was found despite probing common endpoints.
  evidence:
  - status: 0
    url: https://api.auris.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Auris provides cloud‑based payroll and HR solutions for small and medium‑size businesses. Its platform offers secure, compliant payroll processing, benefits administration, time tracking, hiring tools, and integrated tax compliance, all backed by real‑human support. The service aims to simplify workforce management, reduce administrative overhead, and ensure regulatory adherence for growing companies.
image: https://dae142b6.delivery.rocketcdn.me/wp-content/uploads/auris-featured.jpg
layout: provider
modified: '2026-09-26'
name: Auris
nav: Providers
network: true
overview: 'Auris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payroll, Human Resources, Software-as-a-Service, and Small Business.


  Auris'' developer surface includes documentation, engineering blog, pricing, support, getting-started guide, and 15 more developer resources.'
plans:
- name: Auris Plans Pricing
  plan_count: 3
  slug: auris-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 67.9
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 25.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auris Domain Security
  slug: auris-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Auris Vulnerability Disclosure
  slug: auris-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: auris
tags:
- Company
- Payroll
- Human Resources
- Software-as-a-Service
- Small Business
website: https://www.auris.io
---
