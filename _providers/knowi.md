---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Knowi Agentic Access
  operation_count: 26
  slug: knowi-agentic-access
  summary_line: 26 operations · 15 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://knowi.com/api/1.0
  baseurl_source: spec
  description: Obtain and revoke bearer tokens.
  name: Knowi Authentication API
  slug: knowi-authentication-api
- baseURL: https://knowi.com/api/1.0
  baseurl_source: spec
  description: Manage dashboards and shared URLs.
  name: Knowi Dashboards API
  slug: knowi-dashboards-api
- baseURL: https://knowi.com/api/1.0
  baseurl_source: spec
  description: Manage user groups.
  name: Knowi Groups API
  slug: knowi-groups-api
- baseURL: https://www.knowi.com
  baseurl_source: spec
  description: Retrieve dataset contents.
  name: Knowi Pull API
  slug: knowi-pull-api
- baseURL: https://www.knowi.com
  baseurl_source: spec
  description: Send data to Knowi datasets in real time.
  name: Knowi Push API
  slug: knowi-push-api
- baseURL: https://knowi.com/api/1.0
  baseurl_source: spec
  description: Manage workspace users.
  name: Knowi Users API
  slug: knowi-users-api
- description: Manage action API to be used in alert and report
  name: Knowi Action Management API
  slug: knowi-action-management-api-api
- description: The Alerts API from Knowi — 7 operation(s) for alerts.
  name: Knowi Alerts API
  slug: knowi-alerts-api
- description: Authentication API to be authenticate to management API
  name: Knowi Authentication Management API
  slug: knowi-authentication-management-api-api
- description: Manage categories
  name: Knowi Category Management API
  slug: knowi-category-management-api-api
- description: Manage datasources
  name: Knowi Datasource Management API
  slug: knowi-datasource-management-api-api
- description: Manage user group
  name: Knowi Group Management API
  slug: knowi-group-management-api-api
- description: Manage KPI
  name: Knowi KPI Management API
  slug: knowi-kpi-management-api-api
- description: Manage and access NLP functionalities
  name: Knowi Natural Language Processing Management API
  slug: knowi-natural-language-processing-management-api-api
- description: Manage reports
  name: Knowi Report Management API
  slug: knowi-report-management-api-api
- description: Manage roles
  name: Knowi Role Management API
  slug: knowi-role-management-api-api
- description: Manage users
  name: Knowi User Management API
  slug: knowi-user-management-api-api
- description: The Data Sources API from Knowi — 1 operation(s) for data sources.
  name: Knowi Data Sources API
  slug: knowi-data-sources-api
artifact_total: 34
collections:
- collection_type: open
  name: Knowi Management Authentication API
  slug: open-knowi-authentication-api
- collection_type: open
  name: Knowi Management Authentication Dashboards API
  slug: open-knowi-dashboards-api
- collection_type: open
  name: Knowi Management Authentication Groups API
  slug: open-knowi-groups-api
- collection_type: open
  name: Knowi Management API
  slug: open-knowi-management-api
- collection_type: open
  name: Knowi Management Authentication Pull API
  slug: open-knowi-pull-api
- collection_type: open
  name: Knowi Management Authentication Push API
  slug: open-knowi-push-api
- collection_type: open
  name: Knowi Push Data API
  slug: open-knowi-push-data-api
- collection_type: open
  name: Knowi Management Authentication Users API
  slug: open-knowi-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/knowi/plans/knowi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/knowi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/knowi/rate-limits/knowi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/knowi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/knowi/finops/knowi-finops.yml
  title: ''
  type: FinOps
  url: finops/knowi-finops.yml
- group: other
  href: https://artifacts.apis.io/knowi/capabilities/knowi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/knowi-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/knowi/agentic-access/knowi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/knowi-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/knowi/security/knowi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/knowi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/knowi/security/knowi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/knowi-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/knowi/authentication/knowi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/knowi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud9-charts
- group: company
  title: ''
  type: Website
  url: https://www.knowi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.knowi.com/docs
- group: company
  title: ''
  type: Blog
  url: https://www.knowi.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.knowi.com/blog/feed/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.knowi.com/pricing
- group: start
  title: ''
  type: Login
  url: https://www.knowi.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.knowi.com/signup
- group: operate
  title: ''
  type: Support
  url: https://www.knowi.com/support
- group: agent
  title: ''
  type: LlmsText
  url: https://knowi.com/llms.txt
created: '2026-03-26'
description: Knowi is an analytics and business intelligence platform with native integration to NoSQL, SQL, and REST API data sources, providing AI-powered analytics, embedded dashboards, and natural language querying.
finops:
- has_sources: false
  method: generated
  name: Knowi Finops
  primary_unit: request
  service_category: API
  slug: knowi-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/knowi.png
layout: provider
modified: '2026-05-19'
name: Knowi
nav: Providers
network: true
overview: 'Knowi publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Dashboards API, Groups API, and 15 more. Tagged areas include AI Analytics, API Analytics, Business Intelligence, Data Visualization, and Embedded Analytics.


  The Knowi catalog on APIs.io includes 1 Spectral governance ruleset.


  Knowi''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, support, and 12 more developer resources.'
plans:
- name: Knowi Plans Pricing
  plan_count: 3
  slug: knowi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Knowi Rate Limits
  slug: knowi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Knowi API Rules
  rule_count: 61
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 9
  slug: knowi-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.8
  facets:
    access_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 49.4
    developer_ergonomics: 31.0
    discoverability: 69.6
    operational_transparency: 7.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 66.7
      total: 18
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/knowi/knowi-2026-06-20T184113.png
security:
- kind: authentication
  name: Knowi Authentication
  slug: knowi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Knowi Domain Security
  slug: knowi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Knowi Trust Center
  slug: knowi-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: knowi
tags:
- AI Analytics
- API Analytics
- Business Intelligence
- Data Visualization
- Embedded Analytics
- NoSQL Analytics
website: https://www.knowi.com
---
