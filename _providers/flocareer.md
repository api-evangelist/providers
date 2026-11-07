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
api_count: 1
apis:
- description: FloCareer provides a platform that connects job seekers with employers, offering tools for resume building, career advice, and AI‑driven job matching.
  name: FloCareer API
  slug: flocareer-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/flocareer/plans/flocareer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flocareer-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/flocareer/hosts/flocareer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flocareer-hosts.yml
- group: other
  href: https://artifacts.apis.io/flocareer/vendors/flocareer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flocareer-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flocareer.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flocareer.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://flocareer.com/pricing
- group: start
  title: ''
  type: Login
  url: https://flocareer.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://blog.flocareer.com
- group: auth
  href: https://artifacts.apis.io/flocareer/security/flocareer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flocareer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flocareer.com/
coverage:
  checked: '2026-10-27'
  detail: The website and docs provide only HTML pages with no discoverable OpenAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 404
    url: https://flocareer.com/openapi.json
  - status: 404
    url: https://flocareer.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: FloCareer provides a platform that connects job seekers with employers, offering tools for resume building, career advice, and AI‑driven job matching. The service includes a public API that enables developers to integrate job listings, applicant tracking, and career resources into their applications, supporting both web and mobile experiences.
layout: provider
modified: '2026-10-26'
name: FloCareer
nav: Providers
network: true
overview: 'FloCareer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Interview, Hiring, and Platform.


  FloCareer''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Flocareer Plans Pricing
  plan_count: 4
  slug: flocareer-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 20.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flocareer/flocareer-2026-11-03T132156.png
security:
- kind: domain-security
  name: Flocareer Domain Security
  slug: flocareer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flocareer
tags:
- Company
- Artificial Intelligence
- Interview
- Hiring
- Platform
website: https://flocareer.com/
---
