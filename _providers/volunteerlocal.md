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
- description: VolunteerLocal offers a cloud‑based platform for nonprofits to manage volunteers, schedule shifts, track hours, and communicate with participants.
  name: VolunteerLocal API
  slug: volunteerlocal-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/volunteerlocal/plans/volunteerlocal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/volunteerlocal-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/volunteerlocal/hosts/volunteerlocal-hosts.yml
  title: ''
  type: Hosts
  url: hosts/volunteerlocal-hosts.yml
- group: other
  href: https://artifacts.apis.io/volunteerlocal/vendors/volunteerlocal-vendors.yml
  title: ''
  type: Vendors
  url: vendors/volunteerlocal-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://volunteerlocal.com/legal/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://app.volunteerlocal.com/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.volunteerlocal.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.volunteerlocal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.volunteerlocal.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volunteerlocal
- group: auth
  href: https://artifacts.apis.io/volunteerlocal/security/volunteerlocal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volunteerlocal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.volunteerlocal.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.volunteerlocal.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.volunteerlocal.com/support
- group: operate
  title: ''
  type: Contact
  url: https://www.volunteerlocal.com/lets-connect
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is publicly available on the discovered hosts.
  evidence:
  - status: 404
    url: https://api.volunteerlocal.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: VolunteerLocal provides a cloud‑based platform that helps nonprofit organizations manage volunteers, schedule shifts, track hours, and communicate with participants. Its features include volunteer databases, communication tools, scheduling, reporting, and integrations, enabling efficient volunteer program administration.
layout: provider
modified: '2026-10-27'
name: VolunteerLocal
nav: Providers
network: true
overview: 'VolunteerLocal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Volunteer Management, Scheduling, Communications, Tracking, and Reporting.


  VolunteerLocal''s developer surface includes signup flow, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Volunteerlocal Plans Pricing
  plan_count: 6
  slug: volunteerlocal-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 53.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/volunteerlocal/volunteerlocal-2026-11-03T145919.png
security:
- kind: domain-security
  name: Volunteerlocal Domain Security
  slug: volunteerlocal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: volunteerlocal
tags:
- Volunteer Management
- Scheduling
- Communications
- Tracking
- Reporting
- Database
- Event Management
website: https://www.volunteerlocal.com/
---
