---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Swimlane Agentic Access
  operation_count: 28
  slug: swimlane-agentic-access
  summary_line: 28 operations · 7 acting
api_count: 11
apis:
- description: 'The Swimlane Turbine API provides access to the cloud-native Turbine platform, enabling integration with 500+ security tools and connectors. The Turbine API connector supports generic API requests to '
  name: Swimlane Turbine API
  slug: swimlane-turbine-api
- description: Swimlane provides a SCIM v2 API for user lifecycle management and provisioning on Business plans. The SCIM endpoint uses a separately generated bearer token for authentication and enables automated us
  name: Swimlane SCIM API
  slug: swimlane-scim-api
- description: Application (workspace) management endpoints
  name: Swimlane Applications API
  slug: swimlane-applications-api
- description: Endpoints for obtaining and managing authentication tokens
  name: Swimlane Authentication API
  slug: swimlane-authentication-api
- description: Group management endpoints
  name: Swimlane Groups API
  slug: swimlane-groups-api
- description: Job logging and status endpoints
  name: Swimlane Logging API
  slug: swimlane-logging-api
- description: Record CRUD and search endpoints
  name: Swimlane Records API
  slug: swimlane-records-api
- description: Report management and execution endpoints
  name: Swimlane Reports API
  slug: swimlane-reports-api
- description: Server settings and configuration
  name: Swimlane Settings API
  slug: swimlane-settings-api
- description: Task management and execution endpoints
  name: Swimlane Tasks API
  slug: swimlane-tasks-api
- description: User management endpoints
  name: Swimlane Users API
  slug: swimlane-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Swimlane REST Applications API
  slug: open-swimlane-applications-api
- collection_type: open
  name: Swimlane REST Applications Authentication API
  slug: open-swimlane-authentication-api
- collection_type: open
  name: Swimlane REST Applications Groups API
  slug: open-swimlane-groups-api
- collection_type: open
  name: Swimlane REST Applications Logging API
  slug: open-swimlane-logging-api
- collection_type: open
  name: Swimlane REST Applications Records API
  slug: open-swimlane-records-api
- collection_type: open
  name: Swimlane REST Applications Reports API
  slug: open-swimlane-reports-api
- collection_type: open
  name: Swimlane REST Applications Settings API
  slug: open-swimlane-settings-api
- collection_type: open
  name: Swimlane REST Applications Tasks API
  slug: open-swimlane-tasks-api
- collection_type: open
  name: Swimlane REST Applications Users API
  slug: open-swimlane-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swimlane-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swimlane-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swimlane-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swimlane-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://swimlane.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.swimlane.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/swimlane
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swimlane
- group: company
  title: ''
  type: Blog
  url: https://swimlane.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://swimlane.com/platform/
- group: other
  title: ''
  type: X
  url: https://twitter.com/swimlane
- group: commercial
  title: ''
  type: Plans
  url: plans/swimlane-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swimlane-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/swimlane-finops.yml
created: '2026-06-13'
description: Swimlane is a security orchestration, automation, and response (SOAR) platform that provides a REST API for managing playbooks, cases, alerts, workflows, and integrating with security tools. The Swimlane Turbine platform offers agentic AI automation for security operations, enabling enterprise security teams and MSSPs to automate threat detection, incident response, and compliance workflows at scale. The REST API supports bearer token and personal access token (PAT) authentication and exposes endpoints for users, roles, records, applications, playbooks, and more.
examples:
- key_count: 4
  name: Swimlane Authenticate Example
  slug: swimlane-authenticate-example
- key_count: 3
  name: Swimlane Create Record Example
  slug: swimlane-create-record-example
- key_count: 3
  name: Swimlane Search Records Example
  slug: swimlane-search-records-example
finops:
- name: Swimlane Finops
  service_category: ''
  slug: swimlane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swimlane.png
json_schemas:
- name: Swimlane Application
  property_count: 5
  slug: swimlane-app
- name: Swimlane Record
  property_count: 8
  slug: swimlane-record
- name: Swimlane User
  property_count: 9
  slug: swimlane-user
jsonld:
- class_count: 11
  name: Swimlane Context
  property_count: 30
  slug: swimlane-context
layout: provider
modified: '2026-06-13'
name: Swimlane
nav: Providers
network: true
overview: 'Swimlane publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Authentication API, Groups API, and 6 more. Tagged areas include SOAR, Security Orchestration, Automation, Incident Response, and Playbooks.


  The Swimlane catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Swimlane''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Swimlane Plans Pricing
  plan_count: 2
  slug: swimlane-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 1
  name: Swimlane Rate Limits
  slug: swimlane-rate-limits
rules:
- name: Swimlane API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: swimlane-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swimlane/refs/heads/main/screenshots/swimlane-2026-06-20T194822.png
security:
- kind: authentication
  name: Swimlane Authentication
  slug: swimlane-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Swimlane Domain Security
  slug: swimlane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Swimlane Vulnerability Disclosure
  slug: swimlane-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: swimlane
tags:
- SOAR
- Security Orchestration
- Automation
- Incident Response
- Playbooks
- Case Management
- Security Operations
- Agentic AI
website: https://swimlane.com
---
