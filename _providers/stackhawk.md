---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Stackhawk Agentic Access
  operation_count: 54
  slug: stackhawk-agentic-access
  summary_line: 54 operations · 25 acting
api_count: 1
apis:
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Token management and login
  name: StackHawk Api Authentication API
  slug: stackhawk-api-authentication-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Manage applications and environments
  name: StackHawk Applications API
  slug: stackhawk-applications-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Organization-level configurations
  name: StackHawk Global Configuration API
  slug: stackhawk-global-configuration-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: OpenAPI spec uploads and mapping
  name: StackHawk Hosted OAS API
  slug: stackhawk-hosted-oas-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Team creation and member assignment
  name: StackHawk Organization Teams API
  slug: stackhawk-organization-teams-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Member management and audit logs
  name: StackHawk Organizations API
  slug: stackhawk-organizations-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Scan command control
  name: StackHawk Perch API
  slug: stackhawk-perch-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Profile scan analysis
  name: StackHawk Profile Scans API
  slug: stackhawk-profile-scans-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Scan report generation
  name: StackHawk Reports API
  slug: stackhawk-reports-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Repository management
  name: StackHawk Repositories API
  slug: stackhawk-repositories-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Scan configuration file management
  name: StackHawk Scan Configuration API
  slug: stackhawk-scan-configuration-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Security policy management
  name: StackHawk Scan Policies API
  slug: stackhawk-scan-policies-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Scan result reporting and findings
  name: StackHawk Scan Results API
  slug: stackhawk-scan-results-api
- baseURL: https://api.stackhawk.com
  baseurl_source: declared
  description: Authenticated user information
  name: StackHawk User API
  slug: stackhawk-user-api
artifact_total: 60
collections:
- collection_type: postman
  name: StackHawk Api Authentication API
  slug: postman-stackhawk-api-authentication-api
- collection_type: postman
  name: StackHawk Api Authentication Applications API
  slug: postman-stackhawk-applications-api
- collection_type: postman
  name: StackHawk Api Authentication Global Configuration API
  slug: postman-stackhawk-global-configuration-api
- collection_type: postman
  name: StackHawk Api Authentication Hosted OAS API
  slug: postman-stackhawk-hosted-oas-api
- collection_type: postman
  name: StackHawk Api Authentication Organization Teams API
  slug: postman-stackhawk-organization-teams-api
- collection_type: postman
  name: StackHawk Api Authentication Organizations API
  slug: postman-stackhawk-organizations-api
- collection_type: postman
  name: StackHawk Api Authentication Perch API
  slug: postman-stackhawk-perch-api
- collection_type: postman
  name: StackHawk Api Authentication Profile Scans API
  slug: postman-stackhawk-profile-scans-api
- collection_type: postman
  name: StackHawk Api Authentication Reports API
  slug: postman-stackhawk-reports-api
- collection_type: postman
  name: StackHawk Api Authentication Repositories API
  slug: postman-stackhawk-repositories-api
- collection_type: postman
  name: StackHawk Api Authentication Scan Configuration API
  slug: postman-stackhawk-scan-configuration-api
- collection_type: postman
  name: StackHawk Api Authentication Scan Policies API
  slug: postman-stackhawk-scan-policies-api
- collection_type: postman
  name: StackHawk Api Authentication Scan Results API
  slug: postman-stackhawk-scan-results-api
- collection_type: postman
  name: StackHawk Api Authentication User API
  slug: postman-stackhawk-user-api
- collection_type: open
  name: StackHawk Api Authentication API
  slug: open-stackhawk-api-authentication-api
- collection_type: open
  name: StackHawk Api Authentication Applications API
  slug: open-stackhawk-applications-api
- collection_type: open
  name: StackHawk Api Authentication Global Configuration API
  slug: open-stackhawk-global-configuration-api
- collection_type: open
  name: StackHawk Api Authentication Hosted OAS API
  slug: open-stackhawk-hosted-oas-api
- collection_type: open
  name: StackHawk Api Authentication Organization Teams API
  slug: open-stackhawk-organization-teams-api
- collection_type: open
  name: StackHawk Api Authentication Organizations API
  slug: open-stackhawk-organizations-api
- collection_type: open
  name: StackHawk Api Authentication Perch API
  slug: open-stackhawk-perch-api
- collection_type: open
  name: StackHawk Api Authentication Profile Scans API
  slug: open-stackhawk-profile-scans-api
- collection_type: open
  name: StackHawk Api Authentication Reports API
  slug: open-stackhawk-reports-api
- collection_type: open
  name: StackHawk Api Authentication Repositories API
  slug: open-stackhawk-repositories-api
- collection_type: open
  name: StackHawk Api Authentication Scan Configuration API
  slug: open-stackhawk-scan-configuration-api
- collection_type: open
  name: StackHawk Api Authentication Scan Policies API
  slug: open-stackhawk-scan-policies-api
- collection_type: open
  name: StackHawk Api Authentication Scan Results API
  slug: open-stackhawk-scan-results-api
- collection_type: open
  name: StackHawk Api Authentication User API
  slug: open-stackhawk-user-api
- collection_type: open
  name: StackHawk API
  slug: open-stackhawk
common:
- group: commercial
  href: https://artifacts.apis.io/stackhawk/plans/stackhawk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stackhawk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/stackhawk/rate-limits/stackhawk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stackhawk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stackhawk/finops/stackhawk-finops.yml
  title: ''
  type: FinOps
  url: finops/stackhawk-finops.yml
- group: other
  href: https://artifacts.apis.io/stackhawk/capabilities/stackhawk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stackhawk-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stackhawk/overview
- group: agent
  href: https://artifacts.apis.io/stackhawk/agentic-access/stackhawk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stackhawk-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/stackhawk/security/stackhawk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stackhawk-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stackhawk/security/stackhawk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackhawk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stackhawk/security/stackhawk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stackhawk-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/stackhawk/authentication/stackhawk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stackhawk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackhawk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackhawk
- group: company
  title: ''
  type: Website
  url: https://www.stackhawk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackhawk.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.stackhawk.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackhawk.com/
- group: company
  title: ''
  type: Blog
  url: https://www.stackhawk.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.stackhawk.com/changelog.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackhawk.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.stackhawk.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stackhawk.com/llms.txt
created: '2025-01-08'
description: StackHawk is an application and API security testing platform that helps engineering teams find, triage, and fix security vulnerabilities in their APIs and web applications. It provides Dynamic Application Security Testing (DAST) with deep OpenAPI spec integration, CI/CD pipeline automation, AI-powered spec generation, and an AppSec Intelligence platform for program-level visibility across the software development lifecycle.
examples:
- key_count: 4
  name: Stackhawk List Findings Example
  slug: stackhawk-list-findings-example
finops:
- has_sources: true
  method: derived
  name: Stackhawk Finops
  primary_unit: user
  service_category: ''
  slug: stackhawk-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackhawk.png
json_schemas:
- name: StackHawk Security Finding
  property_count: 7
  slug: stackhawk-finding
- name: StackHawk Scan
  property_count: 7
  slug: stackhawk-scan
json_structures:
- name: Stackhawk Scan Structure
  property_count: 0
  slug: stackhawk-scan-structure
jsonld:
- class_count: 9
  name: Stackhawk Context
  property_count: 4
  slug: stackhawk-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.stackhawk.com over HTTP.
  name: StackHawk MCP Server
  slug: stackhawk
modified: '2026-05-19'
name: StackHawk
nav: Providers
network: true
overview: 'StackHawk publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api Authentication API, Applications API, Global Configuration API, and 11 more. Tagged areas include API Security, Application Security, DAST, Security Testing, and Vulnerability Management.


  The StackHawk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StackHawk''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, pricing, and 14 more developer resources.'
plans:
- name: Stackhawk Plans Pricing
  plan_count: 2
  slug: stackhawk-plans-pricing
- name: Stackhawk Price Estimates
  plan_count: 0
  slug: stackhawk-price-estimates
random_paper: 1
rate_limits:
- limit_count: 5
  name: Stackhawk Rate Limits
  slug: stackhawk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: StackHawk — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stackhawk-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 7
  extends: []
  name: StackHawk API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: stackhawk-rules
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.3
    catalog_earned_first_party: 8.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    contract_governance: 9.8
    contract_quality: 53.3
    developer_ergonomics: 40.5
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: platform-generated
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/stackhawk/stackhawk-2026-06-20T194446.png
security:
- kind: authentication
  name: Stackhawk Authentication
  slug: stackhawk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stackhawk Domain Security
  slug: stackhawk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stackhawk Vulnerability Disclosure
  slug: stackhawk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Stackhawk Trust Center
  slug: stackhawk-trust-center
  summary_line: SOC 2
slug: stackhawk
tags:
- API Security
- Application Security
- DAST
- Security Testing
- Vulnerability Management
website: https://www.stackhawk.com/
---
