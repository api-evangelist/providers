---
access_model:
  confidence: high
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
  - sandbox
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 84
  human_in_the_loop: 1
  name: Smarthr Agentic Access
  operation_count: 141
  slug: smarthr-agentic-access
  summary_line: 141 operations · 84 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Business establishments (jigyosho) registered for the tenant.
  name: SmartHR Business Establishments API
  slug: smarthr-business-establishments-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Employee ("crew") records - the core personnel objects in SmartHR.
  name: SmartHR Crews API
  slug: smarthr-crews-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Templates defining custom fields attached to crew records.
  name: SmartHR Custom Field Templates API
  slug: smarthr-custom-field-templates-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Organizational departments that crews belong to.
  name: SmartHR Departments API
  slug: smarthr-departments-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Employment type master data (full-time, part-time, contract, etc.).
  name: SmartHR Employment Types API
  slug: smarthr-employment-types-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: Webhook subscriptions that notify external systems of changes.
  name: SmartHR Webhooks API
  slug: smarthr-webhooks-api
- baseURL: https://{tenant}.smarthr.jp/api
  baseurl_source: declared
  description: カスタム家族項目テンプレートを操作します
  name: SmartHR カスタム家族項目テンプレート API
  slug: smarthr-default-api
artifact_total: 23
asyncapis:
- description: ''
  name: Kufu Smarthr Webhooks
  slug: kufu-smarthr-webhooks
collections:
- collection_type: open
  name: SmartHR Business Establishments API
  slug: open-smarthr-business-establishments-api
- collection_type: open
  name: SmartHR Business Establishments Crews API
  slug: open-smarthr-crews-api
- collection_type: open
  name: SmartHR Business Establishments Custom Field Templates API
  slug: open-smarthr-custom-field-templates-api
- collection_type: open
  name: SmartHR Business Establishments Departments API
  slug: open-smarthr-departments-api
- collection_type: open
  name: SmartHR Business Establishments Employment Types API
  slug: open-smarthr-employment-types-api
- collection_type: open
  name: SmartHR Business Establishments Webhooks API
  slug: open-smarthr-webhooks-api
- collection_type: open
  name: SmartHR API
  slug: open-smarthr
common:
- group: other
  href: https://artifacts.apis.io/smarthr/capabilities/smarthr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smarthr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/smarthr/agentic-access/smarthr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smarthr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smarthr/security/smarthr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smarthr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smarthr/authentication/smarthr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smarthr-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kufu
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smarthr
- group: company
  title: ''
  type: Website
  url: https://smarthr.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.smarthr.jp/
- group: commercial
  href: https://artifacts.apis.io/smarthr/plans/smarthr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smarthr-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smarthr/rate-limits/smarthr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smarthr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smarthr/finops/smarthr-finops.yml
  title: ''
  type: FinOps
  url: finops/smarthr-finops.yml
created: '2026-07-12'
description: SmartHR is a leading Japanese cloud HR, labor, and personnel management SaaS (smarthr.jp). Its per-tenant REST API exposes an organization's employee ("crew") records and the master data around them - departments, employment types, business establishments, and custom field templates - plus webhook subscriptions for change notifications. The API is served from each customer's own tenant subdomain (https://{tenant}.smarthr.jp/api) under a /v1 path, and is authenticated with a per-tenant access token passed as a Bearer token.
finops:
- has_sources: true
  method: generated
  name: Smarthr Finops
  primary_unit: ''
  service_category: Human Resources and Personnel Management
  slug: smarthr-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smarthr.png
layout: provider
modified: '2026-07-12'
name: SmartHR
nav: Providers
network: true
overview: 'SmartHR publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Business Establishments API, Crews API, Custom Field Templates API, and 4 more. Tagged areas include Human Resources, HRIS, Labor Management, Payroll, and Japan.


  The SmartHR catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SmartHR''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Smarthr Plans Pricing
  plan_count: 4
  slug: smarthr-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Smarthr Rate Limits
  slug: smarthr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: SmartHR API Rules
  rule_count: 68
  severity_counts:
    error: 57
    hint: 0
    info: 6
    warn: 5
  slug: smarthr-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 62.9
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smarthr/smarthr-2026-09-02T155924.png
security:
- kind: authentication
  name: Kufu Authentication
  slug: kufu-authentication
  summary_line: 2 schemes
- kind: authentication
  name: Smarthr Authentication
  slug: smarthr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smarthr Domain Security
  slug: smarthr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smarthr
tags:
- Human Resources
- HRIS
- Labor Management
- Payroll
- Japan
- Employees
- Personnel
- Onboarding
- Software-as-a-Service
website: https://smarthr.jp/
---
