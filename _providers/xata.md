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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Xata Agentic Access
  operation_count: 64
  slug: xata-agentic-access
  summary_line: 64 operations · 35 acting
api_count: 12
apis:
- description: Operations for managing API keys, including creation, listing, and deletion
  name: Xata API Keys API
  slug: xata-api-keys-api
- description: Internal organization billing operations
  name: Xata Billing API
  slug: xata-billing-api
- description: Operations for managing database branches within projects, including creation, configuration, and deletion
  name: Xata Branches API
  slug: xata-branches-api
- description: PostgreSQL connectivity via HTTP SQL, WebSocket wire protocol proxy, and native wire protocol.
  name: Xata Gateway API
  slug: xata-gateway-api
- description: Operations for managing GitHub App installation mappings
  name: Xata GitHub App API
  slug: xata-github-app-api
- description: Operations for retrieving log entries for a branch
  name: Xata Logs API
  slug: xata-logs-api
- description: Operations for linking user accounts to cloud marketplace subscriptions
  name: Xata Marketplace API
  slug: xata-marketplace-api
- description: Operations for retrieving observability metrics for a branch
  name: Xata Metrics API
  slug: xata-metrics-api
- description: Operations for creating, retrieving, updating, and deleting organizations
  name: Xata Organizations API
  slug: xata-organizations-api
- description: Operations for creating, retrieving, updating, and deleting projects within an organization
  name: Xata Projects API
  slug: xata-projects-api
- description: The Projects Webhooks API from Xata — 1 operation(s) for projects webhooks.
  name: Xata Projects Webhooks API
  slug: xata-projects-webhooks-api
- description: The Webhooks API from Xata — 2 operation(s) for webhooks.
  name: Xata Webhooks API
  slug: xata-webhooks-api
artifact_total: 39
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xata-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/xata-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/xata-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xata-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xata-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/xata-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://xata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://xata.io/docs/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xataio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xataio
- group: other
  title: ''
  type: X
  url: https://twitter.com/xata
- group: company
  title: ''
  type: Blog
  url: https://xata.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://xata.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://www.xatastatus.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.xata.tech/openapi.json
- group: commercial
  title: ''
  type: Plans
  url: plans/xata-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xata-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/xata-finops.yml
created: '2026-06-12'
description: Xata is a serverless Postgres platform designed for modern development and agentic workloads, offering instant database branching with copy-on-write storage so teams can clone any Postgres database in under one second. The platform provides a managed REST API, CLI, TypeScript and Python SDKs, and a WebSocket wire-protocol proxy for direct Postgres connections. Xata supports schema migrations, built-in PII anonymization, and scale-to-zero compute, with deployment options spanning Xata Cloud (SaaS), BYOC, and open-source self-hosted. An open-source AI agent (Xata Agent) monitors and optimizes PostgreSQL performance with MCP server extensibility.
examples:
- key_count: 7
  name: Xata Branch Credentials Example
  slug: xata-branch-credentials-example
- key_count: 4
  name: Xata Create Branch Example
  slug: xata-create-branch-example
- key_count: 2
  name: Xata Create Organization Example
  slug: xata-create-organization-example
- key_count: 6
  name: Xata Organization Response Example
  slug: xata-organization-response-example
- key_count: 1
  name: Xata Sql Query Example
  slug: xata-sql-query-example
- key_count: 1
  name: Xata Sql Response Example
  slug: xata-sql-response-example
finops:
- name: Xata Finops
  service_category: Database
  slug: xata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xata.png
json_schemas:
- name: APIKeyPreview
  property_count: 11
  slug: xata-apikeypreview
- name: BillingInvoice
  property_count: 7
  slug: xata-billinginvoice
- name: BranchCredentials
  property_count: 2
  slug: xata-branchcredentials
- name: BranchMetadata
  property_count: 14
  slug: xata-branchmetadata
- name: ErrorResponse
  property_count: 17
  slug: xata-errorresponse
- name: Organization
  property_count: 4
  slug: xata-organization
- name: Project
  property_count: 5
  slug: xata-project
- name: QueryResult
  property_count: 5
  slug: xata-queryresult
- name: SQLRequest
  property_count: 4
  slug: xata-sqlrequest
- name: User
  property_count: 2
  slug: xata-user
jsonld:
- class_count: 65
  name: Xata Context
  property_count: 0
  slug: xata-context
layout: provider
modified: '2026-06-12'
name: Xata
nav: Providers
network: true
overview: 'Xata publishes 12 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Billing API, Branches API, and 9 more. Tagged areas include Database, Postgres, Serverless, Developer Tools, and Branching.


  The Xata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Xata''s developer surface includes authentication, documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Xata Plans Pricing
  plan_count: 4
  slug: xata-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 3
  name: Xata Rate Limits
  slug: xata-rate-limits
rules:
- name: Xata API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: xata-jsonschema-spectral-rules
scopes:
- name: Xata Scopes
  scope_count: 15
  slug: xata-scopes
  summary_line: 15 scopes · implicit
score:
  band: developing
  composite: 52.6
  delta: -4.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xata/refs/heads/main/screenshots/xata-2026-06-20T201708.png
security:
- kind: authentication
  name: Xata Authentication
  slug: xata-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Xata Domain Security
  slug: xata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Xata Vulnerability Disclosure
  slug: xata-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Xata Trust Center
  slug: xata-trust-center
  summary_line: HIPAA, GDPR
slug: xata
tags:
- Database
- Postgres
- Serverless
- Developer Tools
- Branching
- AI Agent
website: https://xata.io/
---
