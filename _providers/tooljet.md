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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Tooljet Agentic Access
  operation_count: 23
  slug: tooljet-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 1
apis:
- baseURL: https://your-tooljet-instance.com/api/ext
  baseurl_source: declared
  description: Application export, import, and Git sync endpoints
  name: ToolJet Applications API
  slug: tooljet-applications-api
- baseURL: https://your-tooljet-instance.com/api/ext
  baseurl_source: declared
  description: Group and permission management endpoints
  name: ToolJet Groups API
  slug: tooljet-groups-api
- baseURL: https://your-tooljet-instance.com/api/ext
  baseurl_source: declared
  description: User management endpoints
  name: ToolJet Users API
  slug: tooljet-users-api
- baseURL: https://your-tooljet-instance.com/api/ext
  baseurl_source: declared
  description: Workspace management endpoints
  name: ToolJet Workspaces API
  slug: tooljet-workspaces-api
artifact_total: 23
collections:
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tooljet/overview
- group: other
  href: https://artifacts.apis.io/tooljet/capabilities/tooljet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tooljet-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tooljet/agentic-access/tooljet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tooljet-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tooljet/security/tooljet-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tooljet-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tooljet/security/tooljet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tooljet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tooljet/authentication/tooljet-authentication.yml
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
  href: https://artifacts.apis.io/tooljet/plans/tooljet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tooljet-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tooljet/rate-limits/tooljet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tooljet-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tooljet/finops/tooljet-finops.yml
  title: ''
  type: FinOps
  url: finops/tooljet-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.tooljet.com/rss/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/ToolJet/tooljet-mcp
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://blog.tooljet.com/tooljet-mcp-model-context-protocol/
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
- has_sources: false
  method: generated
  name: Tooljet Finops
  primary_unit: builder-seat
  service_category: ''
  slug: tooljet-finops
  template: true
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
mcp_servers:
- description: ''
  name: MCP Server Source
  slug: mcp-server-source
modified: '2026-09-06'
name: ToolJet
nav: Providers
network: true
overview: 'ToolJet publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Applications API, Groups API, Users API, and 1 more. Tagged areas include Low-Code, Internal Tools, Open Source, Application Builder, and Workflow Automation.


  The ToolJet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ToolJet''s developer surface includes authentication, documentation, engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Tooljet Plans Pricing
  plan_count: 4
  slug: tooljet-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Tooljet Rate Limits
  slug: tooljet-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: ToolJet — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tooljet-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 23.5
    contract_quality: 56.4
    developer_ergonomics: 25.0
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tooljet/tooljet-2026-06-20T195448.png
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
- Low-Code
- Internal Tools
- Open Source
- Application Builder
- Workflow Automation
- No-Code
- Dashboards
- AI Agents
website: https://tooljet.com/
---
