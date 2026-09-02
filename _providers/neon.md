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
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.2
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 26
  human_in_the_loop: 2
  name: Neon Agentic Access
  operation_count: 46
  slug: neon-agentic-access
  summary_line: 46 operations · 26 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Neon Data API provides a secure, stateless HTTP interface to Neon Postgres databases, allowing developers to access and manage data directly from web browsers, serverless functions, and edge runti
  name: Neon Data API
  slug: data-api
- description: The Neon Serverless Driver is a low-latency JavaScript and TypeScript driver that enables querying Neon Postgres databases from serverless and edge environments over HTTP or WebSockets in place of TCP
  name: Neon Serverless Driver
  slug: serverless-driver
- description: Neon Auth is a managed authentication service built on Better Auth that connects directly to a Neon Postgres database. It stores authentication data including users, sessions, and OAuth configurations
  name: Neon Auth
  slug: auth
- description: Manage API keys for authentication. API keys are used to authenticate requests to the Neon API via Bearer token.
  name: Neon API Keys API
  slug: neon-api-keys-api
- description: Manage Neon Auth configuration for branches, including OAuth providers, webhooks, and authentication settings.
  name: Neon Auth API
  slug: neon-auth-api
- description: Manage branches within a project. Branches are copies of your data created using copy-on-write technology for development, testing, and preview environments.
  name: Neon Branches API
  slug: neon-branches-api
- description: Query consumption metrics for projects and accounts. Available for Scale, Business, and Enterprise plan accounts.
  name: Neon Consumption API
  slug: neon-consumption-api
- description: Manage Data API configuration for branches, including enabling and disabling the PostgREST-compatible HTTP interface.
  name: Neon Data API API
  slug: neon-data-api-api
- description: Manage databases within a branch. A branch can contain multiple databases.
  name: Neon Databases API
  slug: neon-databases-api
- description: Manage compute endpoints for branches. Compute endpoints provide the processing resources for database queries. A branch can have one read-write and multiple read-only endpoints.
  name: Neon Endpoints API
  slug: neon-endpoints-api
- description: View and manage operations for a project. Operations track the progress and status of actions performed on project resources.
  name: Neon Operations API
  slug: neon-operations-api
- description: Manage Neon projects. A project is the top-level object in the Neon hierarchy containing branches, databases, roles, and compute endpoints.
  name: Neon Projects API
  slug: neon-projects-api
- description: Manage Postgres roles within a branch. Roles control database access and permissions.
  name: Neon Roles API
  slug: neon-roles-api
artifact_total: 103
asyncapis:
- description: 'Neon Auth webhooks deliver HTTP POST requests when authentication events occur, including OTP delivery, magic link delivery, and user creation. Webhooks can be used to replace built-in email delivery '
  name: Neon Auth Webhook Events
  slug: neon-auth-webhooks-asyncapi
collections:
- collection_type: postman
  name: Neon Management API Keys API
  slug: postman-neon-api-keys-api
- collection_type: postman
  name: Neon Management API Keys Auth API
  slug: postman-neon-auth-api
- collection_type: postman
  name: Neon Management API Keys Branches API
  slug: postman-neon-branches-api
- collection_type: postman
  name: Neon Management API Keys Consumption API
  slug: postman-neon-consumption-api
- collection_type: postman
  name: Neon Management API Keys Data API API
  slug: postman-neon-data-api-api
- collection_type: postman
  name: Neon Management API Keys Databases API
  slug: postman-neon-databases-api
- collection_type: postman
  name: Neon Management API Keys Endpoints API
  slug: postman-neon-endpoints-api
- collection_type: postman
  name: Neon Management API Keys Operations API
  slug: postman-neon-operations-api
- collection_type: postman
  name: Neon Management API Keys Projects API
  slug: postman-neon-projects-api
- collection_type: postman
  name: Neon Management API Keys Roles API
  slug: postman-neon-roles-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Neon Management API Keys API
  slug: open-neon-api-keys-api
- collection_type: open
  name: Neon Management API Keys Auth API
  slug: open-neon-auth-api
- collection_type: open
  name: Neon Management API Keys Branches API
  slug: open-neon-branches-api
- collection_type: open
  name: Neon Management API Keys Consumption API
  slug: open-neon-consumption-api
- collection_type: open
  name: Neon Management API Keys Data API API
  slug: open-neon-data-api-api
- collection_type: open
  name: Neon Management API Keys Databases API
  slug: open-neon-databases-api
- collection_type: open
  name: Neon Management API Keys Endpoints API
  slug: open-neon-endpoints-api
- collection_type: open
  name: Neon Management API
  slug: open-neon-management-api
- collection_type: open
  name: Neon Management API Keys Operations API
  slug: open-neon-operations-api
- collection_type: open
  name: Neon Management API Keys Projects API
  slug: open-neon-projects-api
- collection_type: open
  name: Neon Management API Keys Roles API
  slug: open-neon-roles-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/neon/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/neon-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/neon-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/neon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/neon-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/neondatabase/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neondatabase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neondatabase
- group: start
  title: ''
  type: Portal
  url: https://neon.com/docs
- group: company
  title: ''
  type: Blog
  url: https://neon.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://neon.com/pricing
- group: start
  title: ''
  type: Login
  url: https://console.neon.tech
- group: start
  title: ''
  type: Signup
  url: https://console.neon.tech/signup
- group: operate
  title: ''
  type: Support
  url: https://neon.com/docs/introduction/support
- group: operate
  title: ''
  type: StatusPage
  url: https://neonstatus.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://neon.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://neon.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://neon.com
- group: agent
  title: ''
  type: LlmsText
  url: https://api-docs.neon.tech/llms.txt
created: '2025-03-07'
description: Neon is a serverless Postgres platform that provides fully managed, scalable PostgreSQL databases optimized for modern cloud and edge application development. Their developer platform offers management APIs, data APIs, authentication services, and serverless drivers for building and automating database-driven workflows.
features:
- 'Free: 100 CU-hours/project, 0.5 GB storage, 60K MAU'
- 'Launch: $0.106/CU-hour, $0.35/GB-month, up to 16 CU autoscale'
- 'Scale: $0.222/CU-hour, up to 56 CU fixed, HIPAA/SOC 2'
- Postgres-compatible (latest versions supported)
- Branching for safe schema changes
- Bottomless storage (S3-backed)
- Compute autoscale to zero
- Read replicas
- pgvector for embeddings
- Neon Auth (Stack Auth integration)
- 'Management API: 700 req/hour/org'
- Connection pooling built-in (PgBouncer)
- Time travel (restore to any point in window)
- Private networking (VPC peering) on Scale
- IP allow rules on Scale
- Acquired by Databricks (Q4 2025)
finops:
- name: Neon Finops
  service_category: Serverless Postgres
  slug: neon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neon.png
json_schemas:
- name: ApiKey
  property_count: 5
  slug: neon-apikey
- name: ApiKeyCreateRequest
  property_count: 1
  slug: neon-apikeycreaterequest
- name: ApiKeyCreateResponse
  property_count: 2
  slug: neon-apikeycreateresponse
- name: AuthConfig
  property_count: 4
  slug: neon-authconfig
- name: AuthConfigUpdate
  property_count: 1
  slug: neon-authconfigupdate
- name: Neon Branch
  property_count: 11
  slug: neon-branch
- name: BranchCreateRequest
  property_count: 2
  slug: neon-branchcreaterequest
- name: BranchUpdateRequest
  property_count: 1
  slug: neon-branchupdaterequest
- name: ConnectionUri
  property_count: 2
  slug: neon-connectionuri
- name: ConsumptionHistoryPerAccount
  property_count: 1
  slug: neon-consumptionhistoryperaccount
- name: ConsumptionHistoryPerProject
  property_count: 2
  slug: neon-consumptionhistoryperproject
- name: ConsumptionMetric
  property_count: 6
  slug: neon-consumptionmetric
- name: DataApiConfig
  property_count: 5
  slug: neon-dataapiconfig
- name: DataApiConfigUpdate
  property_count: 5
  slug: neon-dataapiconfigupdate
- name: Database
  property_count: 6
  slug: neon-database
- name: DatabaseCreateRequest
  property_count: 1
  slug: neon-databasecreaterequest
- name: DatabaseUpdateRequest
  property_count: 1
  slug: neon-databaseupdaterequest
- name: Neon Compute Endpoint
  property_count: 14
  slug: neon-endpoint
- name: EndpointCreateRequest
  property_count: 1
  slug: neon-endpointcreaterequest
- name: EndpointUpdateRequest
  property_count: 1
  slug: neon-endpointupdaterequest
- name: OAuthProvider
  property_count: 6
  slug: neon-oauthprovider
- name: OAuthProviderCreateRequest
  property_count: 4
  slug: neon-oauthprovidercreaterequest
- name: OAuthProviderUpdateRequest
  property_count: 3
  slug: neon-oauthproviderupdaterequest
- name: Neon Operation
  property_count: 10
  slug: neon-operation
- name: Pagination
  property_count: 4
  slug: neon-pagination
- name: Neon Project
  property_count: 15
  slug: neon-project
- name: ProjectCreateRequest
  property_count: 1
  slug: neon-projectcreaterequest
- name: ProjectUpdateRequest
  property_count: 1
  slug: neon-projectupdaterequest
- name: Role
  property_count: 6
  slug: neon-role
- name: RoleCreateRequest
  property_count: 1
  slug: neon-rolecreaterequest
json_structures:
- name: Neon Structure
  property_count: 0
  slug: neon-structure
jsonld:
- class_count: 0
  name: Neon Context
  property_count: 7
  slug: neon-context
layout: provider
modified: '2026-05-19'
name: Neon
nav: Providers
network: true
overview: 'Neon publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Auth, API Keys API, Auth API, and 8 more. Tagged areas include Databases, Serverless, Postgres, Infrastructure, and Authentication.


  The Neon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Neon''s developer surface includes authentication, developer portal, engineering blog, pricing, signup flow, support, and 14 more developer resources.'
plans:
- name: Neon Plans Pricing
  plan_count: 3
  slug: neon-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Neon Rate Limits
  slug: neon-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Neon API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: neon-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Neon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: neon-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 64.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 13.6
    contract_quality: 67.8
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neon/refs/heads/main/screenshots/neon-2026-06-20T190138.png
security:
- kind: authentication
  name: Neon Authentication
  slug: neon-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Neon Domain Security
  slug: neon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Neon Vulnerability Disclosure
  slug: neon-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Neon Trust Center
  slug: neon-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 9
skills:
- name: claimable-postgres
  slug: claimable-postgres
- name: neon-ai-gateway
  slug: neon-ai-gateway
- name: neon-functions
  slug: neon-functions
- name: neon-object-storage
  slug: neon-object-storage
- name: neon-postgres-branches
  slug: neon-postgres-branches
- name: neon-postgres-egress-optimizer
  slug: neon-postgres-egress-optimizer
- name: neon-postgres
  slug: neon-postgres
- name: neon
  slug: neon
- name: score-eval
  slug: score-eval
slug: neon
tags:
- Databases
- Serverless
- Postgres
- Infrastructure
- Authentication
- Edge
website: https://neon.com
---
