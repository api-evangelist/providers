---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: VolunteerHub provides a cloud‑based platform that helps nonprofit organizations recruit, schedule, and manage volunteers.
  name: VolunteerHub API
  slug: volunteerhub-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/volunteerhub/plans/volunteerhub-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/volunteerhub-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/volunteerhub/hosts/volunteerhub-hosts.yml
  title: ''
  type: Hosts
  url: hosts/volunteerhub-hosts.yml
- group: other
  href: https://artifacts.apis.io/volunteerhub/vendors/volunteerhub-vendors.yml
  title: ''
  type: Vendors
  url: vendors/volunteerhub-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://volunteerhub.com/solutions/libraries
- group: company
  title: ''
  type: Newsroom
  url: https://volunteerhub.com/news
- group: other
  title: ''
  type: Leadership
  url: https://volunteerhub.com/about/team
- group: start
  title: ''
  type: GettingStarted
  url: https://academy.volunteerhub.com/courses/volunteerhub-quickstart-course/lectures/51597735
- group: auth
  href: https://artifacts.apis.io/volunteerhub/security/volunteerhub-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/volunteerhub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://volunteerhub.com/
- group: company
  title: ''
  type: Blog
  url: https://volunteerhub.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.volunteerhub.com/support/home
- group: commercial
  title: ''
  type: Pricing
  url: https://volunteerhub.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://volunteerhub.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://volunteerhub.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volunteerhub
coverage:
  checked: '2026-10-28'
  detail: API documentation and endpoints are behind a customer login, returning 403/401 on MCP probes.
  evidence:
  - status: 403
    url: https://volunteerhub.com/mcp
  - status: 401
    url: https://support.volunteerhub.com/mcp
  reason: customer-only-docs
  state: gated
created: '2026-10-28'
description: VolunteerHub provides a cloud‑based platform that helps nonprofit organizations recruit, schedule, and manage volunteers. It offers tools for volunteer recruitment, event scheduling, hour tracking, database management, fundraising, liability waivers, rewards, and comprehensive reporting, enabling organizations to streamline operations and increase community impact.
image: https://volunteerhub.com/hubfs/assets-volunteer-hub/logos/logo-full-color.svg
layout: provider
modified: '2026-10-28'
name: VolunteerHub
nav: Providers
network: true
overview: 'VolunteerHub is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Volunteer Management, Non-Profit, Scheduling, Recruiting, and Platform.


  VolunteerHub''s developer surface includes getting-started guide, engineering blog, support, pricing, and 11 more developer resources.'
plans:
- name: Volunteerhub Plans Pricing
  plan_count: 3
  slug: volunteerhub-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Volunteerhub Rate Limits
  slug: volunteerhub-rate-limits
scopes:
- name: Volunteerhub Scopes
  scope_count: 0
  slug: volunteerhub-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 2.6
  previous_composite: 25.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/volunteerhub/volunteerhub-2026-11-03T145920.png
security:
- kind: authentication
  name: Volunteerhub Authentication
  slug: volunteerhub-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Volunteerhub Domain Security
  slug: volunteerhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: volunteerhub
tags:
- Volunteer Management
- Non-Profit
- Scheduling
- Recruiting
- Platform
website: https://volunteerhub.com/
---
