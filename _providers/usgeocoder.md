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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: USgeocoder provides address geocoding, standardization, political jurisdictions, census data, and real-time sales tax lookup via a RESTful JSON/XML API.
  name: USgeocoder API
  slug: usgeocoder-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/usgeocoder/hosts/usgeocoder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/usgeocoder-hosts.yml
- group: other
  href: https://artifacts.apis.io/usgeocoder/vendors/usgeocoder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/usgeocoder-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usgeocoder.com/
- group: start
  title: ''
  type: Login
  url: https://usgeocoder.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.usgeocoder.com/
- group: auth
  href: https://artifacts.apis.io/usgeocoder/security/usgeocoder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/usgeocoder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usgeocoder.com/
- group: docs
  title: ''
  type: Documentation
  url: https://usgeocoder.com/api_overview
- group: docs
  title: ''
  type: APIReference
  url: https://usgeocoder.com/api_overview
- group: start
  title: ''
  type: GettingStarted
  url: https://usgeocoder.com/api_trial_signup_step1
- group: company
  title: ''
  type: Blog
  url: http://blog.usgeocoder.com
- group: operate
  title: ''
  type: Support
  url: https://usgeocoder.com/contact_us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usgeocoder.com/termsof_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usgeocoder.com/privacy_statement
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation pages are HTML only and do not expose an OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://usgeocoder.com/api_overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: USgeocoder provides robust US sales tax rates and political district data for every address and geocode, including congressional, state legislative, county, municipality, school districts, elected officials, and census geographies. Their API enables developers to integrate accurate location-based tax and district information into applications, supporting compliance, analytics, and service personalization across the United States.
layout: provider
modified: '2026-10-27'
name: USgeocoder
nav: Providers
network: true
overview: 'USgeocoder is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Location, Tax, and District.


  USgeocoder''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, and 9 more developer resources.'
plans:
- name: Usgeocoder Plans Pricing
  plan_count: 0
  slug: usgeocoder-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Usgeocoder Domain Security
  slug: usgeocoder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: usgeocoder
tags:
- Company
- API
- Location
- Tax
- District
website: https://usgeocoder.com/
---
