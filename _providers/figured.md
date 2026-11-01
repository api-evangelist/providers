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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Figured RESTful API for accessing farm data and building integrations.
  name: Figured API
  slug: figured-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/figured/plans/figured-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/figured-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/figured/authentication/figured-authentication.yml
  title: ''
  type: Authentication
  url: authentication/figured-authentication.yml
- group: design
  href: https://artifacts.apis.io/figured/conformance/figured-conformance.yml
  title: ''
  type: Conformance
  url: conformance/figured-conformance.yml
- group: agent
  href: https://artifacts.apis.io/figured/llms/figured-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/figured-llms.txt
- group: auth
  href: https://artifacts.apis.io/figured/well-known/figured-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/figured-status-security.txt
- group: auth
  href: https://artifacts.apis.io/figured/well-known/figured-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/figured-help-security.txt
- group: agent
  href: https://artifacts.apis.io/figured/well-known/figured-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/figured-well-known.yml
- group: other
  href: https://artifacts.apis.io/figured/hosts/figured-hosts.yml
  title: ''
  type: Hosts
  url: hosts/figured-hosts.yml
- group: other
  href: https://artifacts.apis.io/figured/vendors/figured-vendors.yml
  title: ''
  type: Vendors
  url: vendors/figured-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.figured.com/en-us/security
- group: other
  title: ''
  type: Leadership
  url: https://www.figured.com/en-us/about-us/team
- group: auth
  href: https://artifacts.apis.io/figured/security/figured-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/figured-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://figured.com/
- group: company
  title: ''
  type: Blog
  url: https://www.figured.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.figured.com/en-us/resources/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.figured.com/en-us/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.figured.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.figured.com/en-us/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figured.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figured.com/en-us/privacy-notice
- group: start
  title: ''
  type: SignUp
  url: https://my.figured.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figured.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.figured.com/
coverage:
  checked: '2026-10-28'
  detail: API documentation redirects to a login page, preventing unauthenticated access.
  evidence:
  - status: 302
    url: https://my.figured.com/developer/api/documentation
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Figured provides a complete online livestock, crop and production tracking, farm budgeting and forecasting tool that gives you accurate data in real time. The platform helps farmers and agribusinesses manage finances, plan operations, and integrate with accounting software, delivering actionable insights for better decision making.
image: https://www.figured.com/hubfs/Figured_October2019/Images/figured-logo.png
layout: provider
modified: '2026-10-28'
name: Figured
nav: Providers
network: true
overview: 'Figured is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Agriculture, FarmManagement, SaaS, and Accounting.


  Figured''s developer surface includes authentication, engineering blog, documentation, getting-started guide, support, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Figured Plans Pricing
  plan_count: 4
  slug: figured-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Figured Rate Limits
  slug: figured-rate-limits
scopes:
- name: Figured Scopes
  scope_count: 0
  slug: figured-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Figured Authentication
  slug: figured-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Figured Domain Security
  slug: figured-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: figured
tags:
- Finance
- Agriculture
- FarmManagement
- SaaS
- Accounting
website: https://figured.com/
---
