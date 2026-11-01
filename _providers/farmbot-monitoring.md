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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Farmbot Monitoring Solutions providing water level monitoring data via MCP endpoints.
  name: Farmbot Monitoring API
  slug: farmbot-monitoring-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/farmbot-monitoring/conventions/farmbot-monitoring-conventions.yml
  title: ''
  type: Conventions
  url: conventions/farmbot-monitoring-conventions.yml
- group: auth
  href: https://artifacts.apis.io/farmbot-monitoring/authentication/farmbot-monitoring-authentication.yml
  title: ''
  type: Authentication
  url: authentication/farmbot-monitoring-authentication.yml
- group: agent
  href: https://artifacts.apis.io/farmbot-monitoring/well-known/farmbot-monitoring-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/farmbot-monitoring-well-known.yml
- group: other
  href: https://artifacts.apis.io/farmbot-monitoring/hosts/farmbot-monitoring-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmbot-monitoring-hosts.yml
- group: other
  href: https://artifacts.apis.io/farmbot-monitoring/vendors/farmbot-monitoring-vendors.yml
  title: ''
  type: Vendors
  url: vendors/farmbot-monitoring-vendors.yml
- group: auth
  href: https://artifacts.apis.io/farmbot-monitoring/security/farmbot-monitoring-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmbot-monitoring-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://farmbot.com.au/
- group: company
  title: ''
  type: Blog
  url: https://farmbot.com.au/news/
- group: operate
  title: ''
  type: Support
  url: https://farmbot.com.au/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://farmbot.com.au/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://farmbot.com.au/terms-of-service/
- group: start
  title: ''
  type: GettingStarted
  url: https://farmbot.com.au/how-to/
coverage:
  checked: '2026-10-28'
  detail: The provider's API surfaces only a well-known OAuth resource JSON and no OpenAPI/AsyncAPI/GraphQL spec is publicly available.
  evidence:
  - status: 200
    url: https://farmbot.com.au/.well-known/oauth-protected-resource
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Farmbot Monitoring Solutions, founded in Sydney in 2014, is a leading Australian AgTech company providing water level monitoring and sensor solutions for farms. Their experienced team understands farmers' daily challenges and delivers user‑friendly products that reduce costs, boost productivity, and streamline farm management.
image: https://farmbot.com.au/wp-content/uploads/2025/09/farmbot-logo.webp
layout: provider
modified: '2026-10-28'
name: Farmbot Monitoring Solutions
nav: Providers
network: true
overview: 'Farmbot Monitoring Solutions is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AgTech, Water Monitoring, Sensors, Australia, and Farm Management.


  Farmbot Monitoring Solutions'' developer surface includes authentication, engineering blog, support, getting-started guide, and 8 more developer resources.'
random_paper: 14
scopes:
- name: Farmbot Monitoring Scopes
  scope_count: 0
  slug: farmbot-monitoring-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Farmbot Monitoring Authentication
  slug: farmbot-monitoring-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Farmbot Monitoring Domain Security
  slug: farmbot-monitoring-domain-security
  summary_line: TLSv1.3 · DMARC
slug: farmbot-monitoring
tags:
- AgTech
- Water Monitoring
- Sensors
- Australia
- Farm Management
website: https://farmbot.com.au/
---
