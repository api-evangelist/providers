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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Finch Agentic Access
  operation_count: 9
  slug: finch-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Connect API from Finch — 1 operation(s) for connect.
  name: Finch Connect API
  slug: finch-connect-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Benefits API from Finch — 4 operation(s) for benefits.
  name: Finch Benefits API
  slug: finch-benefits-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Deductions API from Finch — 6 operation(s) for deductions.
  name: Finch Deductions API
  slug: finch-deductions-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Documents API from Finch — 2 operation(s) for documents.
  name: Finch Documents API
  slug: finch-documents-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Management API from Finch — 9 operation(s) for management.
  name: Finch Management API
  slug: finch-management-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Organization API from Finch — 4 operation(s) for organization.
  name: Finch Organization API
  slug: finch-organization-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Payroll API from Finch — 8 operation(s) for payroll.
  name: Finch Payroll API
  slug: finch-payroll-api
- baseURL: https://api.tryfinch.com
  baseurl_source: declared
  description: The Sandbox API from Finch — 9 operation(s) for sandbox.
  name: Finch Sandbox API
  slug: finch-sandbox-api
artifact_total: 21
collections:
- collection_type: open
  name: Finch Auth API
  slug: open-finch-auth-api
- collection_type: open
  name: Finch Auth Connect API
  slug: open-finch-connect-api
- collection_type: open
  name: Finch Auth Employer API
  slug: open-finch-employer-api
- collection_type: open
  name: Finch API
  slug: open-finch
common:
- group: commercial
  href: https://artifacts.apis.io/finch/plans/finch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/finch/rate-limits/finch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/finch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/finch/finops/finch-finops.yml
  title: ''
  type: FinOps
  url: finops/finch-finops.yml
- group: other
  href: https://artifacts.apis.io/finch/capabilities/finch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/finch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/finch/agentic-access/finch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/finch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/finch/security/finch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/finch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/finch/security/finch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/finch/authentication/finch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finch-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Finch-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finchapi
- group: company
  title: ''
  type: Website
  url: https://www.tryfinch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tryfinch.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.tryfinch.com/api-reference/
- group: start
  title: ''
  type: Signup
  url: https://dashboard.tryfinch.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryfinch.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.tryfinch.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.tryfinch.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tryfinch.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.tryfinch.com/llms.txt
created: '2026-03-16'
description: Finch is a unified employment API providing standardized read and write access to HRIS, payroll, and benefits systems. Through a single integration, developers can pull company directory data, individual PII, employment records, payments, pay statements, and benefits across hundreds of providers (ADP, Gusto, Paylocity, Workday, BambooHR, Rippling, Justworks, TriNet, and more). Finch Connect handles end-user authorization via OAuth.
finops:
- has_sources: false
  method: generated
  name: Finch Finops
  primary_unit: request
  service_category: API
  slug: finch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finch.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.tryfinch.com over HTTP; 3 tools listed.
  name: Finch MCP Server
  slug: finch
modified: '2026-05-19'
name: Finch
nav: Providers
network: true
overview: 'Finch publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connect API, Benefits API, Deductions API, and 5 more. Tagged areas include Employment, HRIS, Payroll, Benefits, and Human Resources.


  The Finch catalog on APIs.io includes 1 Spectral governance ruleset.


  Finch''s developer surface includes authentication, documentation, API reference, signup flow, pricing, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Finch Plans Pricing
  plan_count: 3
  slug: finch-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Finch Rate Limits
  slug: finch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Finch API Rules
  rule_count: 58
  severity_counts:
    error: 41
    hint: 0
    info: 4
    warn: 13
  slug: finch-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 56.2
    developer_ergonomics: 31.0
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/finch/finch-2026-06-20T181218.png
security:
- kind: authentication
  name: Finch Authentication
  slug: finch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Finch Domain Security
  slug: finch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Finch Trust Center
  slug: finch-trust-center
  summary_line: SOC 2
slug: finch
tags:
- Employment
- HRIS
- Payroll
- Benefits
- Human Resources
- Unified API
- Workforce
- Integration
- Employee Benefits
website: https://www.tryfinch.com/
---
