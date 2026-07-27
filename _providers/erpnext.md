---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Erpnext Agentic Access
  operation_count: 9
  slug: erpnext-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 3
apis:
- description: The Method API from ERPNext — 1 operation(s) for method.
  name: ERPNext Method API
  slug: erpnext-method-api
- description: If you are developing something serious, you may want to use oAuth2.
  name: ERPNext Naive Authentication API
  slug: erpnext-naive-authentication-api
- description: The Resource API from ERPNext — 2 operation(s) for resource.
  name: ERPNext Resource API
  slug: erpnext-resource-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/erpnext-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/erpnext-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erpnext-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/erpnext-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/erpnext-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://erpnext.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.frappe.io/erpnext/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/frappe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/erpnext-official
- group: company
  title: ''
  type: Blog
  url: https://frappe.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://frappe.io/erpnext/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://frappecloud.com/monitor
- group: other
  title: ''
  type: X
  url: https://x.com/erpnext
- group: commercial
  title: ''
  type: Plans
  url: plans/erpnext-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erpnext-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/erpnext-finops.yml
created: '2026-06-13'
description: ERPNext is a free and open-source enterprise resource planning (ERP) platform built on the Frappe Framework. It provides a comprehensive REST API for managing accounting, inventory, manufacturing, sales, purchase, HR, and CRM modules. The Frappe Framework auto-generates RESTful endpoints for all DocTypes, supporting standard HTTP methods with JSON responses, token-based authentication, OAuth2, and flexible filtering and pagination.
examples:
- key_count: 1
  name: Customer Doctype
  slug: customer-doctype
- key_count: 1
  name: Doclist Response
  slug: doclist-response
- key_count: 2
  name: Login Request
  slug: login-request
- key_count: 3
  name: Login Response
  slug: login-response
finops:
- name: Erpnext Finops
  service_category: ''
  slug: erpnext-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erpnext.png
json_schemas:
- name: DocList
  property_count: 1
  slug: doclist
- name: DocType
  property_count: 7
  slug: doctype
jsonld:
- class_count: 10
  name: context Context
  property_count: 4
  slug: context
layout: provider
modified: '2026-06-13'
name: ERPNext
nav: Providers
network: true
overview: 'ERPNext publishes 3 APIs on the [APIs.io](https://apis.io/) network: Method API, Naive Authentication API, and Resource API. Tagged areas include ERP, Enterprise Resource Planning, Accounting, Inventory, and Manufacturing.


  The ERPNext catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ERPNext''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Erpnext Plans Pricing
  plan_count: 3
  slug: erpnext-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 0
  name: Erpnext Rate Limits
  slug: erpnext-rate-limits
rules:
- name: ERPNext API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: erpnext-jsonschema-spectral-rules
scopes:
- name: Erpnext Scopes
  scope_count: 1
  slug: erpnext-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 50.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erpnext/refs/heads/main/screenshots/erpnext-2026-06-20T180820.png
security:
- kind: authentication
  name: Erpnext Authentication
  slug: erpnext-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Erpnext Domain Security
  slug: erpnext-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Erpnext Vulnerability Disclosure
  slug: erpnext-vulnerability-disclosure
  summary_line: disclosure policy published
slug: erpnext
tags:
- ERP
- Enterprise Resource Planning
- Accounting
- Inventory
- Manufacturing
- Sales
- CRM
- HR
- Open Source
website: https://erpnext.com
---
