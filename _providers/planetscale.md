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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Planetscale Agentic Access
  operation_count: 60
  slug: planetscale-agentic-access
  summary_line: 60 operations · 30 acting
api_count: 1
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
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage database branch backups, including listing, creating, and retrieving backup details.
  name: planetscale Backups API
  slug: planetscale-backups-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Access organization billing data and invoices programmatically.
  name: planetscale Billing API
  slug: planetscale-billing-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage PgBouncer connection pooling instances for database branches, including creating, listing, resizing, and deleting bouncers.
  name: planetscale Bouncers API
  slug: planetscale-bouncers-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage database branches for schema development and safe migrations, including creating, listing, updating, and deleting branches.
  name: planetscale Branches API
  slug: planetscale-branches-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Retrieve available cluster size SKUs for Vitess and Postgres database branches.
  name: planetscale Cluster Sizes API
  slug: planetscale-cluster-sizes-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage PlanetScale databases, including creating, listing, updating settings, and deleting databases.
  name: planetscale Databases API
  slug: planetscale-databases-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage deploy requests for applying schema changes from development branches to production, including creating, reviewing, queueing, and completing deployments.
  name: planetscale Deploy Requests API
  slug: planetscale-deploy-requests-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage IP restriction entries for controlling database access by IP address.
  name: planetscale IP Restrictions API
  slug: planetscale-ip-restrictions-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage members within an organization, including listing, retrieving, updating roles, and removing members.
  name: planetscale Organization Members API
  slug: planetscale-organization-members-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage PlanetScale organizations, including listing organizations and retrieving organization details.
  name: planetscale Organizations API
  slug: planetscale-organizations-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage branch passwords and connection credentials for connecting applications to database branches.
  name: planetscale Passwords API
  slug: planetscale-passwords-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Analyze and report on query patterns for database branches.
  name: planetscale Query Patterns API
  slug: planetscale-query-patterns-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage role-based credentials for database access.
  name: planetscale Roles API
  slug: planetscale-roles-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: View and manage schema recommendations for optimizing database performance and structure.
  name: planetscale Schema Recommendations API
  slug: planetscale-schema-recommendations-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage service tokens for API authentication, including creating, listing, and deleting tokens and their access grants.
  name: planetscale Service Tokens API
  slug: planetscale-service-tokens-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage teams within an organization, including creating teams, adding members, and controlling database access.
  name: planetscale Teams API
  slug: planetscale-teams-api
- baseURL: https://api.planetscale.com/v1
  baseurl_source: declared
  description: Manage webhook configurations for database event notifications.
  name: planetscale Webhooks API
  slug: planetscale-webhooks-api
artifact_total: 89
asyncapis:
- description: PlanetScale webhooks deliver HTTP POST callbacks to a configured URL when specific events occur within a PlanetScale organization. Webhooks enable real-time notifications for database branch lifecycle
  name: PlanetScale Webhook Events
  slug: planetscale-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PlanetScale Platform Backups API
  slug: open-planetscale-backups-api
- collection_type: open
  name: PlanetScale Platform Backups Billing API
  slug: open-planetscale-billing-api
- collection_type: open
  name: PlanetScale Platform Backups Bouncers API
  slug: open-planetscale-bouncers-api
- collection_type: open
  name: PlanetScale Platform Backups Branches API
  slug: open-planetscale-branches-api
- collection_type: open
  name: PlanetScale Platform Backups Cluster Sizes API
  slug: open-planetscale-cluster-sizes-api
- collection_type: open
  name: PlanetScale Platform Backups Databases API
  slug: open-planetscale-databases-api
- collection_type: open
  name: PlanetScale Platform Backups Deploy Requests API
  slug: open-planetscale-deploy-requests-api
- collection_type: open
  name: PlanetScale Platform Backups IP Restrictions API
  slug: open-planetscale-ip-restrictions-api
- collection_type: open
  name: PlanetScale Platform Backups Organization Members API
  slug: open-planetscale-organization-members-api
- collection_type: open
  name: PlanetScale Platform Backups Organizations API
  slug: open-planetscale-organizations-api
- collection_type: open
  name: PlanetScale Platform Backups Passwords API
  slug: open-planetscale-passwords-api
- collection_type: open
  name: PlanetScale Platform API
  slug: open-planetscale-platform-api
- collection_type: open
  name: PlanetScale Platform Backups Query Patterns API
  slug: open-planetscale-query-patterns-api
- collection_type: open
  name: PlanetScale Platform Backups Roles API
  slug: open-planetscale-roles-api
- collection_type: open
  name: PlanetScale Platform Backups Schema Recommendations API
  slug: open-planetscale-schema-recommendations-api
- collection_type: open
  name: PlanetScale Platform Backups Service Tokens API
  slug: open-planetscale-service-tokens-api
- collection_type: open
  name: PlanetScale Platform Backups Teams API
  slug: open-planetscale-teams-api
- collection_type: open
  name: PlanetScale Platform Backups Webhooks API
  slug: open-planetscale-webhooks-api
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
name: Planetscale
nav: Providers
network: true
overview: 'Planetscale publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Backups API, Billing API, Bouncers API, and 14 more.


  The Planetscale catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Planetscale''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Planetscale Plans Pricing
  plan_count: 5
  slug: planetscale-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Planetscale Rate Limits
  slug: planetscale-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Planetscale API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: planetscale-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Planetscale API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: planetscale-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 69.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 69.9
    developer_ergonomics: 19.0
    discoverability: 44.4
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 31.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
