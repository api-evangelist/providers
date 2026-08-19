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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Tooljet Agentic Access
  operation_count: 23
  slug: tooljet-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 4
apis:
- description: Application export, import, and Git sync endpoints
  name: ToolJet Applications API
  slug: tooljet-applications-api
- description: Group and permission management endpoints
  name: ToolJet Groups API
  slug: tooljet-groups-api
- description: User management endpoints
  name: ToolJet Users API
  slug: tooljet-users-api
- description: Workspace management endpoints
  name: ToolJet Workspaces API
  slug: tooljet-workspaces-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ToolJet External Applications API
  slug: open-tooljet-applications-api
- collection_type: open
  name: ToolJet External Applications Groups API
  slug: open-tooljet-groups-api
- collection_type: open
  name: ToolJet External Applications Users API
  slug: open-tooljet-users-api
- collection_type: open
  name: ToolJet External Applications Workspaces API
  slug: open-tooljet-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tooljet-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tooljet-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tooljet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tooljet-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tooljet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tooljet.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ToolJet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tooljet
- group: other
  title: ''
  type: X
  url: https://x.com/tooljet
- group: company
  title: ''
  type: Blog
  url: https://blog.tooljet.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tooljet.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tooljet.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tooljet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tooljet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tooljet-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.tooljet.com/rss/
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: 2026-06-12
description: ToolJet is an open-source low-code platform for building internal tools, dashboards, business applications, workflows, and AI agents. It provides a REST API (the ToolJet External API) that enables programmatic management of users, workspaces, applications, and user roles across self-hosted and cloud deployments. Authentication is handled via a static access token configured in environment variables and passed as a Basic Authorization header. ToolJet supports connecting to external data sources including REST APIs, GraphQL, databases, and cloud storage, and offers OpenAPI-spec-driven data source integration within the platform. Pricing spans a free tier up to enterprise plans with SSO, Git sync, audit logs, and SCIM provisioning.
examples:
- key_count: 3
  name: Tooljet Create Group Example
  slug: tooljet-create-group-example
- key_count: 6
  name: Tooljet Create User Example
  slug: tooljet-create-user-example
- key_count: 4
  name: Tooljet Import App Example
  slug: tooljet-import-app-example
finops:
- name: Tooljet Finops
  service_category: ''
  slug: tooljet-finops
graphqls:
- description: ToolJet does not expose a native GraphQL management API of its own. Instead, it provides a **GraphQL data source connector** that allows ToolJet applications to connect to any external GraphQL endpoin
  name: ToolJet GraphQL API
  slug: tooljet-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tooljet.png
json_schemas:
- name: ToolJet Group
  property_count: 4
  slug: tooljet-group
- name: ToolJet User
  property_count: 6
  slug: tooljet-user
jsonld:
- class_count: 21
  name: Tooljet Context
  property_count: 7
  slug: tooljet-context
layout: provider
modified: 2026-06-12
name: ToolJet
nav: Providers
network: true
overview: 'ToolJet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Groups API, Users API, and 1 more. Tagged areas include low-code, internal tools, open-source, application builder, and workflow automation.


  The ToolJet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ToolJet''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Tooljet Plans Pricing
  plan_count: 4
  slug: tooljet-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 4
  name: Tooljet Rate Limits
  slug: tooljet-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ToolJet API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tooljet-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: -8.4
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 9.8
    contract_quality: 65.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tooljet/refs/heads/main/screenshots/tooljet-2026-06-20T195448.png
security:
- kind: authentication
  name: Tooljet Authentication
  slug: tooljet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tooljet Domain Security
  slug: tooljet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tooljet Trust Center
  slug: tooljet-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: tooljet
tags:
- low-code
- internal tools
- open-source
- application builder
- workflow automation
- no-code
- dashboards
- AI agents
website: https://tooljet.com/
---
