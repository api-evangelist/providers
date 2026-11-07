---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Career Rift platform, documented on the features page.
  name: Career Rift API
  slug: career-rift-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/careerrift-com/plans/careerrift-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/careerrift-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/careerrift-com/conformance/careerrift-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/careerrift-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/careerrift-com/well-known/careerrift-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/careerrift-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/careerrift-com/hosts/careerrift-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/careerrift-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/careerrift-com/vendors/careerrift-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/careerrift-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://careerrift.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://careerrift.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://careerrift.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://careerrift.com/extension/changelog
- group: auth
  href: https://artifacts.apis.io/careerrift-com/security/careerrift-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/careerrift-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://careerrift.com/
coverage:
  checked: '2026-11-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC spec found on any discovered host.
  evidence:
  - status: 404
    url: https://api.careerrift.com/openapi.json
  - status: 404
    url: https://api.careerrift.com/openapi.yaml
  - status: 307
    url: https://app.careerrift.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Career Rift is a job application tracker and job search organizer that consolidates all your applications onto a single board. It integrates with email and calendar to auto‑update application status, supports major job boards, and offers AI‑assisted interview preparation. The platform is free to start and aims to replace cumbersome spreadsheets with a unified workspace.
image: https://careerrift.com/og.png
layout: provider
modified: '2026-11-03'
name: Career Rift
nav: Providers
network: true
overview: 'Career Rift is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Job Search, Productivity, Artificial Intelligence, and Software-as-a-Service.


  Career Rift''s developer surface includes pricing, changelog, and 9 more developer resources.'
plans:
- name: Careerrift Com Plans Pricing
  plan_count: 5
  slug: careerrift-com-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Careerrift Com Domain Security
  slug: careerrift-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: careerrift-com
tags:
- Company
- Job Search
- Productivity
- Artificial Intelligence
- Software-as-a-Service
- Careers
website: https://careerrift.com/
---
