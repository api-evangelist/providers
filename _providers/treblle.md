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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Treblle Agentic Access
  operation_count: 12
  slug: treblle-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 15
apis:
- description: Treblle analyzes 40 API-specific data points for every API request. All data is consolidated and easily accessible in one centralized location. The only platform you need to build, ship and understand
  name: Treblle
  slug: treblle
- description: Treblle API Intelligence is a federated platform that provides 50+ API-specific data points for every request across an entire API landscape, helping teams debug and deploy fixes 15x faster through en
  name: Treblle API Intelligence
  slug: api-intelligence
- description: 'Treblle API Documentation automatically generates real-time API documentation from live API traffic and SDK instrumentation, including authentication methods, endpoints, OpenAPI specs, Swagger editor '
  name: Treblle API Documentation
  slug: api-documentation
- description: Treblle API Governance runs 30+ automated tests on APIs to assess design, performance, and security with API scoring systems. It enables shift-left and runtime security governance through automated ru
  name: Treblle API Governance
  slug: api-governance
- description: Treblle API Analytics provides customizable dashboards for monitoring API performance and usage, enabling teams to track request metrics, location data, device information, and response times with rea
  name: Treblle API Analytics
  slug: api-analytics
- description: Treblle API Security provides real-time threat detection with 15+ automated security checks on every API request, analyzing payloads for SQL injection patterns, performing IP reputation checks, detect
  name: Treblle API Security
  slug: api-security
- description: Treblle API Insights is a free governance tool that evaluates OpenAPI specifications, providing scores from 1-100 and letter grades from A-F across design, security, and performance categories with 30
  name: Treblle API Insights
  slug: api-insights
- description: Alfred is Treblle's AI-powered integration assistant for developer portals, enabling automated code generation across multiple programming languages, endpoint discovery, and intelligent API documentat
  name: Treblle Alfred AI
  slug: alfred
- description: Aspen is Treblle's intelligent API testing application for macOS featuring AI-powered capabilities through Alfred AI, the ability to organize API requests through Collections, automatic code generatio
  name: Treblle Aspen API Testing
  slug: aspen
- description: Retrieve performance metrics, usage statistics, error rates, and geographic distribution data for monitored APIs.
  name: Treblle Analytics API
  slug: treblle-analytics-api
- description: View auto-discovered endpoints detected by Treblle from live traffic, including documentation and schema data.
  name: Treblle Endpoints API
  slug: treblle-endpoints-api
- description: Run automated API governance checks against OpenAPI specifications, scoring APIs on design, security, and performance dimensions.
  name: Treblle Governance API
  slug: treblle-governance-api
- description: Manage project team members and access permissions.
  name: Treblle Members API
  slug: treblle-members-api
- description: Create and manage Treblle API projects. Each project corresponds to a monitored API and generates an API ID and SDK token.
  name: Treblle Projects API
  slug: treblle-projects-api
- description: Access real-time API request and response logs captured by Treblle SDK instrumentation across all monitored APIs.
  name: Treblle Requests API
  slug: treblle-requests-api
arazzos:
- description: List workspace projects, select the first one, and retrieve its analytics over a date range.
  name: Treblle Find a Project and Pull Its Analytics
  slug: treblle-find-project-and-analytics-workflow
- description: Resolve a project then run Treblle's governance check against an OpenAPI spec and capture the scorecard.
  name: Treblle Governance Scorecard
  slug: treblle-governance-scorecard-workflow
- description: Create a project, invite a teammate to it, and list the resulting member roster.
  name: Treblle Onboard a Project and Its Team
  slug: treblle-onboard-project-and-team-workflow
- description: Resolve a project then pull its analytics and auto-discovered endpoints for a single health view.
  name: Treblle Project Health Snapshot
  slug: treblle-project-health-snapshot-workflow
- description: Resolve a project, list its captured API requests, and pull the full detail of the most recent one.
  name: Treblle Inspect a Project's Recent Requests
  slug: treblle-project-recent-requests-workflow
- description: Create a Treblle project and confirm its API ID and SDK token are ready for instrumentation.
  name: Treblle Provision a Monitoring Project
  slug: treblle-provision-project-workflow
- description: Find requests returning a given error status code for a project and open the most recent failure's detail.
  name: Treblle Triage Failing API Requests
  slug: treblle-triage-error-requests-workflow
- description: Read a project, update its environment and metadata, and confirm the change took effect.
  name: Treblle Promote a Project's Environment
  slug: treblle-update-project-environment-workflow
artifact_total: 60
collections:
- collection_type: postman
  name: Treblle API
  slug: postman-treblle-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Treblle Analytics API
  slug: open-treblle-analytics-api
- collection_type: open
  name: Treblle API
  slug: open-treblle-api
- collection_type: open
  name: Treblle Analytics Endpoints API
  slug: open-treblle-endpoints-api
- collection_type: open
  name: Treblle Analytics Governance API
  slug: open-treblle-governance-api
- collection_type: open
  name: Treblle Analytics Members API
  slug: open-treblle-members-api
- collection_type: open
  name: Treblle Analytics Projects API
  slug: open-treblle-projects-api
- collection_type: open
  name: Treblle Analytics Requests API
  slug: open-treblle-requests-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/treblle-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/treblle-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/treblle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/treblle-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/treblle/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-find-project-and-analytics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-governance-scorecard-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-onboard-project-and-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-project-health-snapshot-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-project-recent-requests-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-provision-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-triage-error-requests-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/treblle-update-project-environment-workflow.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://treblle.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.treblle.com/guides/getting-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.treblle.com/guides/getting-started/
- group: other
  title: ''
  type: Customers
  url: https://treblle.com/customers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.treblle.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.treblle.com/
- group: auth
  title: ''
  type: Security
  url: https://treblle.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://treblle.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://treblle.com/privacy-policy
- group: company
  title: ''
  type: About
  url: https://treblle.com/about-us
- group: other
  title: ''
  type: Enterprise
  url: https://treblle.com/enterprise
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/treblle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/treblle
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/treblleapi
- group: start
  title: ''
  type: Signup
  url: https://identity.treblle.com/register
- group: start
  title: ''
  type: Login
  url: https://identity.treblle.com/login
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/treblle-vocabulary.yml
created: '2025-01-08'
description: Treblle helps engineering and product teams build, ship and understand their REST APIs in one single place. Empowering API producers by showing actionable data in real-time where it matters. Gain a deeper understanding of your API consumers and elevate developer experience (DX). Treblle analyzes 40+ API-specific data points for every API request across the entire API landscape.
examples:
- key_count: 2
  name: Treblle List Projects Example
  slug: treblle-list-projects-example
- key_count: 2
  name: Treblle Run Governance Example
  slug: treblle-run-governance-example
finops:
- name: Treblle Finops
  service_category: Developer Tools / API Observability
  slug: treblle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/treblle.png
json_schemas:
- name: ApiRequest
  property_count: 8
  slug: treblle-apirequest
- name: ApiRequestDetail
  property_count: 12
  slug: treblle-apirequestdetail
- name: CreateProjectRequest
  property_count: 3
  slug: treblle-createprojectrequest
- name: Endpoint
  property_count: 7
  slug: treblle-endpoint
- name: Treblle Governance Result
  property_count: 9
  slug: treblle-governance
- name: GovernanceCheckRequest
  property_count: 1
  slug: treblle-governancecheckrequest
- name: GovernanceResult
  property_count: 9
  slug: treblle-governanceresult
- name: InviteMemberRequest
  property_count: 2
  slug: treblle-invitememberrequest
- name: Member
  property_count: 5
  slug: treblle-member
- name: PaginationMeta
  property_count: 4
  slug: treblle-paginationmeta
- name: Treblle Project
  property_count: 9
  slug: treblle-project
- name: ProjectAnalytics
  property_count: 6
  slug: treblle-projectanalytics
- name: Treblle API Request
  property_count: 13
  slug: treblle-request
- name: UpdateProjectRequest
  property_count: 3
  slug: treblle-updateprojectrequest
json_structures:
- name: Treblle Project Structure
  property_count: 0
  slug: treblle-project-structure
- name: Treblle Structure
  property_count: 0
  slug: treblle-structure
jsonld:
- class_count: 32
  name: Treblle Context
  property_count: 0
  slug: treblle-context
layout: provider
modified: '2026-05-19'
name: Treblle
nav: Providers
network: true
overview: 'Treblle publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Endpoints API, Governance API, and 3 more. Tagged areas include Analytics, Artificial Intelligence, Developer Experience, Documentation, and Governance.


  The Treblle catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Treblle''s developer surface includes authentication, pricing, documentation, getting-started guide, engineering blog, signup flow, and 24 more developer resources.'
plans:
- name: Treblle Plans Pricing
  plan_count: 3
  slug: treblle-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Treblle Rate Limits
  slug: treblle-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Treblle API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: treblle-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Treblle API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: treblle-rules
score:
  band: strong
  composite: 55.6
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 28.8
    contract_quality: 74.8
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/treblle/refs/heads/main/screenshots/treblle-2026-06-20T195643.png
security:
- kind: authentication
  name: Treblle Authentication
  slug: treblle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Treblle Domain Security
  slug: treblle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Treblle Trust Center
  slug: treblle-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: treblle
tags:
- Analytics
- Artificial Intelligence
- Developer Experience
- Documentation
- Governance
- Insights
- Observability
- Platform
- Security
- Testing
---
