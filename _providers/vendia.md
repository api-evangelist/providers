---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Every Vendia project (Uni) is provisioned with an auto-generated GraphQL API derived from its JSON Schema data model — get_X / list_XItems / list_XVersions queries and add_X / create_X / put_X / updat
  name: Vendia Share GraphQL API
  slug: vendia-share-graphql-api
artifact_total: 8
asyncapis:
- description: ''
  name: Vendia Notifications Webhooks
  slug: vendia-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vendia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vendia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vendia.com/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vendia.com/platform/operational/scalar-data/graphql/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vendia.com/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://www.vendia.com/company/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.vendia.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vendia.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendia
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendia.com/platform/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://share.vendia.net/signup
- group: start
  title: ''
  type: Login
  url: https://share.vendia.net
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vendia.com/legal/share-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vendia.com/legal/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.vendia.com/legal/security-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.vendia.com/security/soc2
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vendia.com/
- group: operate
  title: ''
  type: SLA
  url: https://www.vendia.com/legal/share-service-level-agreement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vendiahq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/vendiahq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@vendiahq
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vendia-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendia-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vendia-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/vendia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vendia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vendia-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vendia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vendia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vendia-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.vendia.com/releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vendia-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendia-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vendia-notifications-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vendia-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vendia-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendia-rate-limits.yml
created: '2026-08-05'
description: Vendia is an enterprise data platform company founded by Tim Wagner (creator of AWS Lambda) and Shruthi Rao (founder of the AWS blockchain practice). Its flagship product is the Vendia MCP Gateway — a managed, multi-tenant Model Context Protocol server that gives AI agents governed, audited access to Amazon S3 buckets, third-party REST APIs described by OpenAPI/Swagger ("API Catalogs"), and remote MCP servers behind a single OAuth-protected endpoint. Underneath sits Vendia Share, a real-time distributed data platform that exposes each project as an auto-generated GraphQL API over a consensus-backed ledger, with fine-grained permissions, RBAC, schema evolution, file and folder APIs, block/dead-letter notifications, and analytical data products ingested from S3, Snowflake, Databricks, BigQuery, Cloudera, MySQL and PostgreSQL.
image: https://www.vendia.com/wp-content/uploads/2025/09/Power_genai_with_enterprise_data.webp
layout: provider
mcp_servers:
- description: ''
  name: Vendia MCP Gateway
  slug: vendia-mcp-gateway
modified: '2026-08-05'
name: Vendia
nav: Providers
network: true
overview: 'Vendia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Artificial Intelligence, Data Sharing, and Data Platform.


  The Vendia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vendia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Vendia Plans
  plan_count: 3
  slug: vendia-plans
random_paper: 1
rate_limits:
- limit_count: 3
  name: Vendia Rate Limits
  slug: vendia-rate-limits
scopes:
- name: Vendia Scopes
  scope_count: 3
  slug: vendia-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 62.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 84.2
  previous_composite: 62.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vendia/refs/heads/main/screenshots/vendia-2026-08-17T080436.png
security:
- kind: authentication
  name: Vendia Authentication
  slug: vendia-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 6 schemes
- kind: domain-security
  name: Vendia Domain Security
  slug: vendia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vendia
tags:
- Company
- MCP
- Artificial Intelligence
- Data Sharing
- Data Platform
- GraphQL
- Agents
- API Gateway
- Data Governance
website: https://www.vendia.com/
---
