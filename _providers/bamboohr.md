---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bamboohr Agentic Access
  operation_count: 14
  slug: bamboohr-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 8
apis:
- description: RESTful HTTPS API for accessing and manipulating employee data, directories, time-off, reports, and other BambooHR HRIS resources. Supports OAuth 2.0 for multi-customer apps and API key (HTTP Basic) f
  name: BambooHR REST API
  slug: rest-api
- description: Event-driven webhook surface for BambooHR. Webhooks fire when monitored fields change on Employee records (and when employee records are created or deleted). Subscribers register an HTTPS URL per moni
  name: BambooHR Webhooks
  slug: webhooks
- description: Employee directory
  name: BambooHR Directory API
  slug: bamboohr-directory-api
- description: Employee records
  name: BambooHR Employees API
  slug: bamboohr-employees-api
- description: Employee files
  name: BambooHR Files API
  slug: bamboohr-files-api
- description: Field metadata
  name: BambooHR Meta API
  slug: bamboohr-meta-api
- description: Custom and standard reports
  name: BambooHR Reports API
  slug: bamboohr-reports-api
- description: Time-off requests and balances
  name: BambooHR Time Off API
  slug: bamboohr-time-off-api
artifact_total: 17
collections:
- collection_type: open
  name: BambooHR Webhooks
  slug: open-bamboohr-asyncapi
- collection_type: open
  name: BambooHR REST API
  slug: open-bamboohr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bamboohr-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bamboohr-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bamboohr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bamboohr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bamboohr-authentication.yml
- group: auth
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
graphqls:
- description: 'BambooHR is a cloud-based human resources software platform for small and medium-sized businesses. This conceptual GraphQL schema models the BambooHR REST API surface, covering employee records, time '
  name: BambooHR GraphQL Schema
  slug: bamboohr-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bamboohr.png
layout: provider
modified: '2026-05-30'
name: BambooHR
nav: Providers
network: true
overview: 'BambooHR publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Directory API, Employees API, and 4 more. Tagged areas include HR, HRIS, Human Resources, Payroll, and Time Tracking.


  BambooHR''s developer surface includes authentication, documentation, API reference, signup flow, pricing, support, and 10 more developer resources.'
random_paper: 32
scopes:
- name: Bamboohr Scopes
  scope_count: 1
  slug: bamboohr-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 35.0
  delta: -1.4
  facets:
    commercial_clarity: 18.4
    contract_quality: 65.2
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bamboohr/refs/heads/main/screenshots/bamboohr-2026-06-20T172934.png
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Bamboohr Trust Center
  slug: bamboohr-trust-center
  summary_line: SOC 2, PCI DSS
slug: bamboohr
tags:
- HR
- HRIS
- Human Resources
- Payroll
- Time Tracking
- Applicant Tracking
- Performance Management
website: https://www.bamboohr.com/
---
