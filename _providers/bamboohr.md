---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bamboohr Agentic Access
  operation_count: 14
  slug: bamboohr-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 1
apis:
- description: RESTful HTTPS API for accessing and manipulating employee data, directories, time-off, reports, and other BambooHR HRIS resources. Supports OAuth 2.0 for multi-customer apps and API key (HTTP Basic) f
  name: BambooHR REST API
  slug: rest-api
- description: Event-driven webhook surface for BambooHR. Webhooks fire when monitored fields change on Employee records (and when employee records are created or deleted). Subscribers register an HTTPS URL per moni
  name: BambooHR Webhooks
  slug: webhooks
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Employee directory
  name: BambooHR Directory API
  slug: bamboohr-directory-api
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Employee records
  name: BambooHR Employees API
  slug: bamboohr-employees-api
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Employee files
  name: BambooHR Files API
  slug: bamboohr-files-api
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Field metadata
  name: BambooHR Meta API
  slug: bamboohr-meta-api
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Custom and standard reports
  name: BambooHR Reports API
  slug: bamboohr-reports-api
- baseURL: https://api.bamboohr.com/api/gateway.php
  baseurl_source: declared
  description: Time-off requests and balances
  name: BambooHR Time Off API
  slug: bamboohr-time-off-api
artifact_total: 23
collections:
- collection_type: open
  name: BambooHR Webhooks
  slug: open-bamboohr-asyncapi
- collection_type: open
  name: BambooHR REST Directory API
  slug: open-bamboohr-directory-api
- collection_type: open
  name: BambooHR REST Directory Employees API
  slug: open-bamboohr-employees-api
- collection_type: open
  name: BambooHR REST Directory Files API
  slug: open-bamboohr-files-api
- collection_type: open
  name: BambooHR REST Directory Meta API
  slug: open-bamboohr-meta-api
- collection_type: open
  name: BambooHR REST Directory Reports API
  slug: open-bamboohr-reports-api
- collection_type: open
  name: BambooHR REST Directory Time Off API
  slug: open-bamboohr-time-off-api
- collection_type: open
  name: BambooHR REST API
  slug: open-bamboohr
common:
- group: company
  title: ''
  type: Blog
  url: https://www.bamboohr.com/blog/
- group: other
  href: https://artifacts.apis.io/bamboohr/capabilities/bamboohr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bamboohr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bamboohr/agentic-access/bamboohr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bamboohr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bamboohr/security/bamboohr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bamboohr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bamboohr/security/bamboohr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bamboohr-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bamboohr/security/bamboohr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bamboohr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bamboohr/authentication/bamboohr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bamboohr-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bamboohr/scopes/bamboohr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bamboohr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BambooHR
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bamboohr
- group: company
  title: ''
  type: Website
  url: https://www.bamboohr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.bamboohr.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bamboohr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.bamboohr.com/reference
- group: start
  title: ''
  type: Signup
  url: https://www.bamboohr.com/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bamboohr.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://help.bamboohr.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.bamboohr.com/llms.txt
created: '2026-05-11'
description: BambooHR is a cloud-based human resources software platform for small and medium-sized businesses, providing core HR, applicant tracking, onboarding, time tracking, payroll, performance management, and employee self-service. The BambooHR REST API allows developers to read and update employee data, generate reports, manage time-off, and integrate with the HRIS using either OAuth 2.0 or per-customer API keys over HTTPS Basic Auth.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bamboohr.png
layout: provider
modified: '2026-10-06'
name: BambooHR
nav: Providers
network: true
overview: 'BambooHR publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Directory API, Employees API, and 5 more. Tagged areas include Human Resources, HRIS, Payroll, Time Tracking, and Applicant Tracking.


  The BambooHR catalog on APIs.io includes 1 Spectral governance ruleset.


  BambooHR''s developer surface includes engineering blog, authentication, documentation, API reference, signup flow, pricing, support, and 11 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: BambooHR API Rules
  rule_count: 63
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 1
  slug: bamboohr-rules
scopes:
- name: Bamboohr Scopes
  scope_count: 1
  slug: bamboohr-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 50.2
    developer_ergonomics: 54.8
    discoverability: 64.3
    operational_transparency: 13.2
  previous_composite: 36.9
  provenance:
    agentic_access: derived
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
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bamboohr/bamboohr-2026-06-20T172934.png
security:
- kind: authentication
  name: Bamboohr Authentication
  slug: bamboohr-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bamboohr Domain Security
  slug: bamboohr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bamboohr Vulnerability Disclosure
  slug: bamboohr-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Bamboohr Trust Center
  slug: bamboohr-trust-center
  summary_line: SOC 2, PCI DSS
slug: bamboohr
tags:
- Human Resources
- HRIS
- Payroll
- Time Tracking
- Applicant Tracking
- Performance Management
website: https://www.bamboohr.com/
---
