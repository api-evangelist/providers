---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/aplos/well-known/aplos-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aplos-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/aplos/plans/aplos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aplos-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.aplos.com/security
- group: agent
  href: https://artifacts.apis.io/aplos/llms/aplos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aplos-llms.txt
- group: agent
  href: https://artifacts.apis.io/aplos/well-known/aplos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aplos-well-known.yml
- group: other
  href: https://artifacts.apis.io/aplos/hosts/aplos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aplos-hosts.yml
- group: other
  href: https://artifacts.apis.io/aplos/vendors/aplos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aplos-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aplos.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aplos.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.aplos.com/signup
- group: auth
  title: ''
  type: Security
  url: https://www.aplos.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aplos.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.aplos.com/about/team
- group: auth
  href: https://artifacts.apis.io/aplos/security/aplos-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aplos-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/aplos/security/aplos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aplos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aplos.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aplos.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.aplos.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.aplos.com/mcp
  - status: 403
    url: https://status.aplos.com/mcp
  - status: 200
    url: https://www.aplos.com/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Aplos provides cloud‑based nonprofit accounting software designed to help charities, churches, and other mission‑driven organizations manage their finances, track donations, and stay compliant. The platform offers fund accounting, transaction management, advanced reporting, payroll, and AI‑powered bill entry, all tailored for the nonprofit sector. Aplos also delivers expert bookkeeping services and integrates with partners like Gusto to streamline payroll and benefits.
image: https://cdn.prod.website-files.com/644691be9cfddf7b3e816e96/66bfb23e78c00f4df165c02e_aplos%20open%20graph.png
layout: provider
modified: '2026-10-26'
name: Aplos
nav: Providers
network: true
overview: 'Aplos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Non-Profit, Software, and Cloud.


  Aplos'' developer surface includes signup flow, pricing, support, and 15 more developer resources.'
plans:
- name: Aplos Plans Pricing
  plan_count: 4
  slug: aplos-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.3
    operational_transparency: 13.2
  previous_composite: 29.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aplos/aplos-2026-11-03T121019.png
security:
- kind: domain-security
  name: Aplos Domain Security
  slug: aplos-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Aplos Trust Center
  slug: aplos-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: aplos
tags:
- Company
- Accounting
- Non-Profit
- Software
- Cloud
website: https://www.aplos.com/
---
