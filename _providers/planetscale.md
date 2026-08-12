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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Planetscale Agentic Access
  operation_count: 60
  slug: planetscale-agentic-access
  summary_line: 60 operations · 30 acting
api_count: 20
apis:
- description: PlanetScale OAuth allows developers to create OAuth applications that can access users' PlanetScale accounts on their behalf. The implementation supports the Authorization Code grant type, enabling th
  name: PlanetScale OAuth
  slug: oauth
- description: The PlanetScale Serverless Driver for JavaScript is a Fetch API-compatible database driver designed for serverless and edge compute platforms such as Cloudflare Workers, Vercel Edge Functions, and Net
  name: PlanetScale Serverless Driver for JavaScript
  slug: serverless-driver
- description: The PlanetScale CLI (pscale) is a command-line tool that brings PlanetScale database management to the terminal. It allows developers to create, delete, and list databases and branches, open interacti
  name: PlanetScale CLI
  slug: cli
- description: Manage database branch backups, including listing, creating, and retrieving backup details.
  name: planetscale Backups API
  slug: planetscale-backups-api
- description: Access organization billing data and invoices programmatically.
  name: planetscale Billing API
  slug: planetscale-billing-api
- description: Manage PgBouncer connection pooling instances for database branches, including creating, listing, resizing, and deleting bouncers.
  name: planetscale Bouncers API
  slug: planetscale-bouncers-api
- description: Manage database branches for schema development and safe migrations, including creating, listing, updating, and deleting branches.
  name: planetscale Branches API
  slug: planetscale-branches-api
- description: Retrieve available cluster size SKUs for Vitess and Postgres database branches.
  name: planetscale Cluster Sizes API
  slug: planetscale-cluster-sizes-api
- description: Manage PlanetScale databases, including creating, listing, updating settings, and deleting databases.
  name: planetscale Databases API
  slug: planetscale-databases-api
- description: Manage deploy requests for applying schema changes from development branches to production, including creating, reviewing, queueing, and completing deployments.
  name: planetscale Deploy Requests API
  slug: planetscale-deploy-requests-api
- description: Manage IP restriction entries for controlling database access by IP address.
  name: planetscale IP Restrictions API
  slug: planetscale-ip-restrictions-api
- description: Manage members within an organization, including listing, retrieving, updating roles, and removing members.
  name: planetscale Organization Members API
  slug: planetscale-organization-members-api
- description: Manage PlanetScale organizations, including listing organizations and retrieving organization details.
  name: planetscale Organizations API
  slug: planetscale-organizations-api
- description: Manage branch passwords and connection credentials for connecting applications to database branches.
  name: planetscale Passwords API
  slug: planetscale-passwords-api
- description: Analyze and report on query patterns for database branches.
  name: planetscale Query Patterns API
  slug: planetscale-query-patterns-api
- description: Manage role-based credentials for database access.
  name: planetscale Roles API
  slug: planetscale-roles-api
- description: View and manage schema recommendations for optimizing database performance and structure.
  name: planetscale Schema Recommendations API
  slug: planetscale-schema-recommendations-api
- description: Manage service tokens for API authentication, including creating, listing, and deleting tokens and their access grants.
  name: planetscale Service Tokens API
  slug: planetscale-service-tokens-api
- description: Manage teams within an organization, including creating teams, adding members, and controlling database access.
  name: planetscale Teams API
  slug: planetscale-teams-api
- description: Manage webhook configurations for database event notifications.
  name: planetscale Webhooks API
  slug: planetscale-webhooks-api
artifact_total: 71
asyncapis:
- description: PlanetScale webhooks deliver HTTP POST callbacks to a configured URL when specific events occur within a PlanetScale organization. Webhooks enable real-time notifications for database branch lifecycle
  name: PlanetScale Webhook Events
  slug: planetscale-webhooks-asyncapi
collections:
- collection_type: open
  name: PlanetScale Platform API
  slug: open-planetscale-platform-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planetscale-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planetscale-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planetscale-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://planetscale.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planetscale
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planetscale
- group: design
  title: ''
  type: JSONLD
  url: json-ld/planetscale-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/planetscale-database-schema.json
description: PlanetScale is a serverless MySQL database platform powered by Vitess, providing horizontal scaling, branching workflows, non-blocking schema changes, and other developer-friendly database features.
features:
- Postgres EBS single-node from $5/mo
- Postgres EBS HA 3-node from $15/mo
- Postgres Metal 3-node from $50/mo
- Vitess Non-Metal 3-node from $39/mo
- Vitess Metal 3-node from $609/mo
- Cluster sizes from 1/16 vCPU to 96 vCPU
- arm64 and x86-64 architectures
- Multi-region deployment options
- Optional PgBouncer for Postgres
- Optional read replicas
- Branching for safe schema changes
- Deploy requests for review-and-merge schema flow
- Connection pooling built in
- Insights for query performance
- Boost for query result caching
- Management API at 240 req/min/org
finops:
- name: Planetscale Finops
  service_category: Distributed Database
  slug: planetscale-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/planetscale.png
json_schemas:
- name: Backup
  property_count: 8
  slug: planetscale-backup
- name: Bouncer
  property_count: 6
  slug: planetscale-bouncer
- name: Branch
  property_count: 13
  slug: planetscale-branch
- name: ClusterSize
  property_count: 6
  slug: planetscale-clustersize
- name: PlanetScale Database
  property_count: 16
  slug: planetscale-database
- name: DeployRequest
  property_count: 12
  slug: planetscale-deployrequest
- name: DeployRequestReview
  property_count: 5
  slug: planetscale-deployrequestreview
- name: Error
  property_count: 2
  slug: planetscale-error
- name: Invoice
  property_count: 7
  slug: planetscale-invoice
- name: IpRestriction
  property_count: 4
  slug: planetscale-iprestriction
- name: Organization
  property_count: 7
  slug: planetscale-organization
- name: OrganizationMember
  property_count: 5
  slug: planetscale-organizationmember
- name: Password
  property_count: 10
  slug: planetscale-password
- name: PasswordWithPlaintext
  property_count: 0
  slug: planetscale-passwordwithplaintext
- name: QueryPatternsReport
  property_count: 4
  slug: planetscale-querypatternsreport
- name: RoleCredentials
  property_count: 7
  slug: planetscale-rolecredentials
- name: SchemaLintError
  property_count: 6
  slug: planetscale-schemalinterror
- name: SchemaRecommendation
  property_count: 7
  slug: planetscale-schemarecommendation
- name: ServiceToken
  property_count: 3
  slug: planetscale-servicetoken
- name: ServiceTokenAccess
  property_count: 4
  slug: planetscale-servicetokenaccess
- name: ServiceTokenWithPlaintext
  property_count: 0
  slug: planetscale-servicetokenwithplaintext
- name: Team
  property_count: 7
  slug: planetscale-team
- name: Webhook
  property_count: 6
  slug: planetscale-webhook
json_structures:
- name: Planetscale Structure
  property_count: 0
  slug: planetscale-structure
jsonld:
- class_count: 0
  name: Planetscale Context
  property_count: 10
  slug: planetscale-context
layout: provider
modified: '2026-05-19'
name: planetscale
nav: Providers
network: true
overview: 'planetscale publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Backups API, Billing API, Bouncers API, and 14 more.


  The planetscale catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  planetscale''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Planetscale Plans Pricing
  plan_count: 5
  slug: planetscale-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Planetscale Rate Limits
  slug: planetscale-rate-limits
rules:
- name: planetscale API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: planetscale-asyncapi-spectral-rules
- name: planetscale API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: planetscale-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.9
  delta: -8.6
  facets:
    commercial_clarity: 15.8
    contract_quality: 77.7
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 13.2
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/planetscale/refs/heads/main/screenshots/planetscale-2026-06-20T191803.png
security:
- kind: authentication
  name: Planetscale Authentication
  slug: planetscale-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Planetscale Domain Security
  slug: planetscale-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: planetscale
---
