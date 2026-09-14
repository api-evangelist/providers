---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granular Agentic Access
  operation_count: 7
  slug: granular-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Granular Insights provides analytics and reporting APIs for farm operations, enabling agronomic analysis, yield benchmarking, and field performance reporting for precision agriculture workflows.
  name: Granular Insights API
  slug: granular-insights-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Field activities — planting, application, harvest
  name: Granular (Corteva Agriscience) Activities API
  slug: granular-activities-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Crop plans and variety information
  name: Granular (Corteva Agriscience) Crops API
  slug: granular-crops-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Farm entity management
  name: Granular (Corteva Agriscience) Farms API
  slug: granular-farms-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Field boundary and attribute management
  name: Granular (Corteva Agriscience) Fields API
  slug: granular-fields-api
- baseURL: https://api.granular.ag
  baseurl_source: declared
  description: Farm financial records and cost tracking
  name: Granular (Corteva Agriscience) Financials API
  slug: granular-financials-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Granular Farm Management Activities API
  slug: open-granular-activities-api
- collection_type: open
  name: Granular Farm Management Activities Crops API
  slug: open-granular-crops-api
- collection_type: open
  name: Granular Farm Management API
  slug: open-granular-farm-management
- collection_type: open
  name: Granular Farm Management Activities Farms API
  slug: open-granular-farms-api
- collection_type: open
  name: Granular Farm Management Activities Fields API
  slug: open-granular-fields-api
- collection_type: open
  name: Granular Farm Management Activities Financials API
  slug: open-granular-financials-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/granular-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/granular-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/granular-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/granular-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/granular-scopes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/granular-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/granular-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/granular-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/granular-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/granular-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://support.insights.granular.ag/hc/en-us
- group: company
  title: ''
  type: Website
  url: https://granular.ag/
- group: start
  title: ''
  type: Portal
  url: https://us.app.granular.ag/
coverage:
  checked: '2026-09-12'
  detail: Granular Insights runs a real Kong API gateway at us.insights.granular.ag whose /api routes answer '{"message":"no Route matched with those values"}' to an unauthenticated caller, but there is no developer portal, no API reference and no spec anywhere public — every Granular surface redirects into a tenant sign-in, and the api.granular.ag host this record has always carried has no DNS record at all.
  evidence:
  - status: 404
    url: https://us.insights.granular.ag/api
  - status: 301
    url: https://granular.ag/
  - status: 0
    url: https://api.granular.ag/
  - status: 403
    url: https://us.app.granular.ag/.well-known/agent-card.json
  reason: customer-only-docs
  state: gated
created: '2026-04-28'
description: Granular is a farm management platform now part of Corteva Agriscience, providing APIs for crop planning, field records management, financial analysis, and farm operational tracking. The platform serves commercial agriculture operations with data-driven decision support tools.
finops:
- name: Granular Finops
  service_category: API
  slug: granular-finops
json_schemas:
- name: Granular Farm Field
  property_count: 15
  slug: granular-field
jsonld:
- class_count: 9
  name: Granular Context
  property_count: 16
  slug: granular-context
layout: provider
modified: '2026-09-12'
name: Granular (Corteva Agriscience)
nav: Providers
network: true
overview: 'Granular (Corteva Agriscience) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Crops API, Farms API, and 2 more. Tagged areas include Agriculture, Farm Management, Financial, Crop Planning, and Agronomy.


  The Granular (Corteva Agriscience) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Granular (Corteva Agriscience)''s developer surface includes authentication, support, developer portal, and 10 more developer resources.'
plans:
- name: Granular Plans Pricing
  plan_count: 0
  slug: granular-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Granular Rate Limits
  slug: granular-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Granular (Corteva Agriscience) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: granular-jsonschema-spectral-rules
scopes:
- name: Granular Scopes
  scope_count: 2
  slug: granular-scopes
  summary_line: 2 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/screenshots/granular-2026-06-20T182321.png
security:
- kind: authentication
  name: Granular Authentication
  slug: granular-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Granular Domain Security
  slug: granular-domain-security
  summary_line: TLSv1.3 · DMARC
slug: granular
tags:
- Agriculture
- Farm Management
- Financial
- Crop Planning
- Agronomy
website: https://granular.ag/
---
