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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 65
  human_in_the_loop: 3
  name: Thenile Agentic Access
  operation_count: 137
  slug: thenile-agentic-access
  summary_line: 137 operations · 65 acting · 3 human-in-the-loop
api_count: 4
apis:
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The auth API from Nile — 10 operation(s) for auth.
  name: Nile Auth API
  slug: thenile-auth-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The authentication API from Nile — 18 operation(s) for authentication.
  name: Nile Authentication API
  slug: thenile-authentication-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The compute API from Nile — 2 operation(s) for compute.
  name: Nile Compute API
  slug: thenile-compute-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The credentials API from Nile — 3 operation(s) for credentials.
  name: Nile Credentials API
  slug: thenile-credentials-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The Databases API from Nile — 18 operation(s) for databases.
  name: Nile Databases API
  slug: thenile-databases-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The developers API from Nile — 6 operation(s) for developers.
  name: Nile Developers API
  slug: thenile-developers-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The Internal API from Nile — 2 operation(s) for internal.
  name: Nile Internal API
  slug: thenile-internal-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The tenants API from Nile — 7 operation(s) for tenants.
  name: Nile Tenants API
  slug: thenile-tenants-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The users API from Nile — 27 operation(s) for users.
  name: Nile Users API
  slug: thenile-users-api
- baseURL: https://global.thenile.dev
  baseurl_source: declared
  description: The Workspaces API from Nile — 17 operation(s) for workspaces.
  name: Nile Workspaces API
  slug: thenile-workspaces-api
artifact_total: 39
common:
- group: other
  href: https://artifacts.apis.io/thenile/capabilities/thenile-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thenile-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/thenile/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/thenile/llms/thenile-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thenile-docs-llms.txt
- group: agent
  href: https://artifacts.apis.io/thenile/agentic-access/thenile-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thenile-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/thenile/plans/thenile-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thenile-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thenile/rules/thenile-rules.yml
  title: ''
  type: Spectral
  url: rules/thenile-rules.yml
- group: design
  href: https://artifacts.apis.io/thenile/json-ld/thenile-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thenile-context.jsonld
- group: design
  href: https://artifacts.apis.io/thenile/vocabulary/thenile-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thenile-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/thenile/data-model/thenile-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thenile-data-model.yml
- group: build
  href: https://artifacts.apis.io/thenile/cli/thenile-cli.yml
  title: ''
  type: CLI
  url: cli/thenile-cli.yml
- group: design
  href: https://artifacts.apis.io/thenile/errors/thenile-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thenile-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thenile/conformance/thenile-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thenile-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thenile/llms/thenile-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thenile-llms.txt
- group: build
  href: https://artifacts.apis.io/thenile/mcp/thenile-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thenile-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/thenile/mcp/thenile-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thenile-mcp.yml
- group: agent
  href: https://artifacts.apis.io/thenile/well-known/thenile-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thenile-well-known.yml
- group: other
  href: https://artifacts.apis.io/thenile/hosts/thenile-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thenile-hosts.yml
- group: other
  href: https://artifacts.apis.io/thenile/vendors/thenile-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thenile-vendors.yml
- group: build
  href: https://artifacts.apis.io/thenile/packages/thenile-packages.yml
  title: ''
  type: SDKs
  url: packages/thenile-packages.yml
- group: build
  href: https://artifacts.apis.io/thenile/packages/thenile-packages.yml
  title: ''
  type: Packages
  url: packages/thenile-packages.yml
- group: auth
  href: https://artifacts.apis.io/thenile/authentication/thenile-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thenile-authentication.yml
- group: auth
  href: https://artifacts.apis.io/thenile/security/thenile-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thenile-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thenile.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.thenile.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.thenile.dev/docs/api-reference/post-oauth2token
- group: start
  title: ''
  type: GettingStarted
  url: https://www.thenile.dev/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.thenile.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/niledatabase
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thenile.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.thenile.dev/
- group: start
  title: ''
  type: SignUp
  url: https://console.thenile.dev
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thenile.dev/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thenile.dev/terms-of-service
created: '2026-10-13'
description: Nile is a serverless PostgreSQL platform re-engineered for multi-tenant B2B applications, offering virtual tenant databases, tenant isolation, vector embeddings, and built-in user and tenant authentication (Nile Auth). Its control-plane REST API manages workspaces, databases, credentials, regions and billing, a database API manages tenants, users and OIDC providers, and a regional auth API powers sign-in, sessions and tenant membership.
finops:
- has_sources: true
  method: derived
  name: Thenile Finops
  primary_unit: subscription
  service_category: ''
  slug: thenile-finops
  template: false
image: https://www.thenile.dev/favicon.ico
json_schemas:
- name: APIError
  property_count: 3
  slug: thenile-apierror
- name: CreateBasicUserRequest
  property_count: 7
  slug: thenile-create-basic-user-request
- name: CreateDatabaseRequest
  property_count: 2
  slug: thenile-create-database-request
- name: DedicatedComputeInstance
  property_count: 11
  slug: thenile-dedicated-compute-instance
- name: GetDatabaseResponse
  property_count: 11
  slug: thenile-get-database-response
- name: LogicalDatabase
  property_count: 5
  slug: thenile-logical-database
- name: MfaDisableRequest
  property_count: 5
  slug: thenile-mfa-disable-request
- name: MfaSetupResponse
  property_count: 8
  slug: thenile-mfa-setup-response
- name: MfaVerifyRequest
  property_count: 2
  slug: thenile-mfa-verify-request
- name: MfaVerifyResponse
  property_count: 2
  slug: thenile-mfa-verify-response
- name: OIDCProvider
  property_count: 7
  slug: thenile-oidcprovider
- name: OIDCRelyingParty
  property_count: 7
  slug: thenile-oidcrelying-party
- name: TenantSSORegistration
  property_count: 7
  slug: thenile-tenant-ssoregistration
- name: TenantUser
  property_count: 9
  slug: thenile-tenant-user
- name: UnauthenticatedProvisionDatabaseResponse
  property_count: 10
  slug: thenile-unauthenticated-provision-database-response
- name: User
  property_count: 9
  slug: thenile-user
- name: WorkspaceUsageResponse
  property_count: 9
  slug: thenile-workspace-usage-response
jsonld:
- class_count: 86
  name: Thenile Context
  property_count: 167
  slug: thenile-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 13 tools listed.
  name: Nile MCP Server
  slug: nile-mcp-server
modified: '2026-10-13'
name: Nile
nav: Providers
network: true
overview: 'Nile publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Authentication API, Compute API, and 7 more. Tagged areas include Company, Database, PostgreSQL, Serverless, and Multi-Tenant.


  The Nile catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nile''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Thenile Plans Pricing
  plan_count: 4
  slug: thenile-plans-pricing
- name: Thenile Price Estimates
  plan_count: 0
  slug: thenile-price-estimates
random_paper: 1
rate_limits:
- limit_count: 0
  name: Thenile Rate Limits
  slug: thenile-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Nile API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 7
  slug: thenile-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 65.2
    developer_ergonomics: 43.5
    discoverability: 76.7
    operational_transparency: 2.6
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 40.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thenile/thenile-2026-11-03T144624.png
security:
- kind: authentication
  name: Thenile Authentication
  slug: thenile-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Thenile Domain Security
  slug: thenile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: thenile-manage-tenant-users
  slug: thenile-manage-tenant-users
- name: thenile-provision-database
  slug: thenile-provision-database
slug: thenile
tags:
- Company
- Database
- PostgreSQL
- Serverless
- Multi-Tenant
- Authentication
- B2B SaaS
website: https://www.thenile.dev
---
