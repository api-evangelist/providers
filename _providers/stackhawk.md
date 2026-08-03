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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Stackhawk Agentic Access
  operation_count: 54
  slug: stackhawk-agentic-access
  summary_line: 54 operations · 25 acting
api_count: 14
apis:
- description: Token management and login
  name: StackHawk Api Authentication API
  slug: stackhawk-api-authentication-api
- description: Manage applications and environments
  name: StackHawk Applications API
  slug: stackhawk-applications-api
- description: Organization-level configurations
  name: StackHawk Global Configuration API
  slug: stackhawk-global-configuration-api
- description: OpenAPI spec uploads and mapping
  name: StackHawk Hosted OAS API
  slug: stackhawk-hosted-oas-api
- description: Team creation and member assignment
  name: StackHawk Organization Teams API
  slug: stackhawk-organization-teams-api
- description: Member management and audit logs
  name: StackHawk Organizations API
  slug: stackhawk-organizations-api
- description: Scan command control
  name: StackHawk Perch API
  slug: stackhawk-perch-api
- description: Profile scan analysis
  name: StackHawk Profile Scans API
  slug: stackhawk-profile-scans-api
- description: Scan report generation
  name: StackHawk Reports API
  slug: stackhawk-reports-api
- description: Repository management
  name: StackHawk Repositories API
  slug: stackhawk-repositories-api
- description: Scan configuration file management
  name: StackHawk Scan Configuration API
  slug: stackhawk-scan-configuration-api
- description: Security policy management
  name: StackHawk Scan Policies API
  slug: stackhawk-scan-policies-api
- description: Scan result reporting and findings
  name: StackHawk Scan Results API
  slug: stackhawk-scan-results-api
- description: Authenticated user information
  name: StackHawk User API
  slug: stackhawk-user-api
artifact_total: 44
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
  name: StackHawk API
  slug: open-stackhawk
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stackhawk/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stackhawk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stackhawk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackhawk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackhawk-domain-security.yml
- group: auth
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
- name: Stackhawk Finops
  service_category: API
  slug: stackhawk-finops
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
modified: '2026-05-19'
name: StackHawk
nav: Providers
network: true
overview: 'StackHawk publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Api Authentication API, Applications API, Global Configuration API, and 11 more. Tagged areas include API Security, Application Security, DAST, Security Testing, and Vulnerability Management.


  The StackHawk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  StackHawk''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, changelog, pricing, and 10 more developer resources.'
plans:
- name: Stackhawk Plans Pricing
  plan_count: 3
  slug: stackhawk-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Stackhawk Rate Limits
  slug: stackhawk-rate-limits
rules:
- name: StackHawk API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stackhawk-jsonschema-spectral-rules
- name: StackHawk API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: stackhawk-rules
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.7
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stackhawk/refs/heads/main/screenshots/stackhawk-2026-06-20T194446.png
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
