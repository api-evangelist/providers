---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bytebase Agentic Access
  operation_count: 24
  slug: bytebase-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 1
apis:
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: AccessGrantService manages temporary access grants within projects.
  name: Bytebase Access Grant Service API
  slug: bytebase-accessgrantservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ActuatorService manages system health and operational information.
  name: Bytebase Actuator Service API
  slug: bytebase-actuatorservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: AIService provides AI chat capabilities for the page agent.
  name: Bytebase AI Service API
  slug: bytebase-aiservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: AuditLogService manages audit logs for system activities and API calls.
  name: Bytebase Audit Log Service API
  slug: bytebase-auditlogservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: CelService manages CEL (Common Expression Language) parsing and formatting operations.
  name: Bytebase Cel Service API
  slug: bytebase-celservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ChangelogService manages database migration history.
  name: Bytebase Changelog Service API
  slug: bytebase-changelogservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: DatabaseCatalogService manages database schema metadata and classification.
  name: Bytebase Database Catalog Service API
  slug: bytebase-databasecatalogservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: DatabaseGroupService manages database groups for organizing databases by criteria.
  name: Bytebase Database Group Service API
  slug: bytebase-databasegroupservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: DatabaseService manages databases and their schemas.
  name: Bytebase Database Service API
  slug: bytebase-databaseservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: GroupService manages user groups for organizing users and permissions.
  name: Bytebase Group Service API
  slug: bytebase-groupservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: IdentityProviderService manages external identity providers for SSO authentication.
  name: Bytebase Identity Provider Service API
  slug: bytebase-identityproviderservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: InstanceRoleService manages database roles within instances.
  name: Bytebase Instance Role Service API
  slug: bytebase-instanceroleservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: InstanceService manages database instances and their connections.
  name: Bytebase Instance Service API
  slug: bytebase-instanceservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: IssueService manages issues for tracking database changes and tasks.
  name: Bytebase Issue Service API
  slug: bytebase-issueservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: OrgPolicyService manages organizational policies at various resource levels.
  name: Bytebase Org Policy Service API
  slug: bytebase-orgpolicyservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: PlanService manages deployment plans for database changes.
  name: Bytebase Plan Service API
  slug: bytebase-planservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ProjectService manages projects that group databases and changes.
  name: Bytebase Project Service API
  slug: bytebase-projectservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: QueryHistoryService manages query history records of SQL Editor queries and exports.
  name: Bytebase Query History Service API
  slug: bytebase-queryhistoryservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ReleaseService manages releases for coordinating deployments.
  name: Bytebase Release Service API
  slug: bytebase-releaseservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ReviewConfigService manages approval flow configurations.
  name: Bytebase Review Config Service API
  slug: bytebase-reviewconfigservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: RevisionService manages schema revision history.
  name: Bytebase Revision Service API
  slug: bytebase-revisionservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: RoleService manages workspace roles and permissions.
  name: Bytebase Role Service API
  slug: bytebase-roleservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: RolloutService manages the execution of deployment plans.
  name: Bytebase Rollout Service API
  slug: bytebase-rolloutservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: 'SavedQueryService manages saved queries in the SQL Editor. A saved query is private to its creator until shared. Permissions come from three places: - The creator owns the saved query and holds every '
  name: Bytebase Saved Query Service API
  slug: bytebase-savedqueryservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: ServiceAccountService manages service accounts for API integrations.
  name: Bytebase Service Account Service API
  slug: bytebase-serviceaccountservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: SettingService manages workspace-level settings and configurations.
  name: Bytebase Setting Service API
  slug: bytebase-settingservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: SheetService manages SQL scripts and saved queries.
  name: Bytebase Sheet Service API
  slug: bytebase-sheetservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: SQLService executes SQL queries and manages query operations.
  name: Bytebase SQL Service API
  slug: bytebase-sqlservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: SubscriptionService manages enterprise subscriptions and licensing.
  name: Bytebase Subscription Service API
  slug: bytebase-subscriptionservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: UserService manages user accounts and authentication.
  name: Bytebase User Service API
  slug: bytebase-userservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: WorkloadIdentityService manages workload identities for external CI/CD integrations.
  name: Bytebase Workload Identity Service API
  slug: bytebase-workloadidentityservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: WorkspaceService manages workspace-level operations and profile.
  name: Bytebase Workspace Service API
  slug: bytebase-workspaceservice-api
- baseURL: https://demo.bytebase.com/v1
  baseurl_source: declared
  description: AuthService handles user authentication operations.
  name: Bytebase Auth Service API
  slug: bytebase-auth-service-api
artifact_total: 54
collections:
- collection_type: open
  name: Bytebase Auth API
  slug: open-bytebase-auth-api
- collection_type: open
  name: Bytebase Auth Databases API
  slug: open-bytebase-databases-api
- collection_type: open
  name: Bytebase Auth Groups API
  slug: open-bytebase-groups-api
- collection_type: open
  name: Bytebase Auth Instances API
  slug: open-bytebase-instances-api
- collection_type: open
  name: Bytebase Auth Issues API
  slug: open-bytebase-issues-api
- collection_type: open
  name: Bytebase Auth Plans API
  slug: open-bytebase-plans-api
- collection_type: open
  name: Bytebase Auth Projects API
  slug: open-bytebase-projects-api
- collection_type: open
  name: Bytebase Auth Roles API
  slug: open-bytebase-roles-api
- collection_type: open
  name: Bytebase Auth Rollouts API
  slug: open-bytebase-rollouts-api
- collection_type: open
  name: Bytebase Auth Sheets API
  slug: open-bytebase-sheets-api
- collection_type: open
  name: Bytebase Auth Users API
  slug: open-bytebase-users-api
- collection_type: open
  name: Bytebase Auth Webhooks API
  slug: open-bytebase-webhooks-api
- collection_type: open
  name: Bytebase API
  slug: open-bytebase
common:
- group: company
  title: ''
  type: Blog
  url: https://www.bytebase.com/blog/
- group: other
  href: https://artifacts.apis.io/bytebase/capabilities/bytebase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bytebase-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/bytebase/agentic-access/bytebase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bytebase-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bytebase/security/bytebase-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bytebase-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/bytebase/security/bytebase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bytebase-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/bytebase/authentication/bytebase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bytebase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytebase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bytebase
- group: company
  title: ''
  type: Website
  url: https://www.bytebase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bytebase.com/integrations/api/overview
- group: commercial
  href: https://artifacts.apis.io/bytebase/plans/bytebase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bytebase-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bytebase/rate-limits/bytebase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bytebase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bytebase/finops/bytebase-finops.yml
  title: ''
  type: FinOps
  url: finops/bytebase-finops.yml
created: '2026-06-21'
description: Bytebase is a database DevOps and CI/CD platform - the GitOps-style control plane for schema change, migration, and access management across MySQL, PostgreSQL, and many other engines. Every action in the web console is backed by a documented API exposed as both Connect/gRPC and RESTful HTTP (gRPC transcoding), authenticated with a service-account Bearer token. Bytebase ships as free, self-hostable open source (OSS) with paid Pro and Enterprise tiers.
finops:
- has_sources: true
  method: generated
  name: Bytebase Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: bytebase-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bytebase.png
layout: provider
modified: '2026-10-06'
name: Bytebase
nav: Providers
network: true
overview: 'Bytebase publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Grant Service API, Actuator Service API, AI Service API, and 30 more. Tagged areas include Database, DevOps, Schema Migration, CI/CD, and DevSecOps.


  The Bytebase catalog on APIs.io includes 1 Spectral governance ruleset.


  Bytebase''s developer surface includes engineering blog, authentication, documentation, and 10 more developer resources.'
plans:
- name: Bytebase Plans Pricing
  plan_count: 3
  slug: bytebase-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Bytebase Rate Limits
  slug: bytebase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Bytebase API Rules
  rule_count: 46
  severity_counts:
    error: 31
    hint: 0
    info: 2
    warn: 13
  slug: bytebase-rules
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 45.4
    developer_ergonomics: 22.6
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 28.3
      derived: 0
      marker_coverage: 71.7
      total: 46
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bytebase/bytebase-2026-07-25T204142.png
security:
- kind: authentication
  name: Bytebase Authentication
  slug: bytebase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bytebase Domain Security
  slug: bytebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bytebase Trust Center
  slug: bytebase-trust-center
  summary_line: SOC 2, HIPAA
slug: bytebase
tags:
- Database
- DevOps
- Schema Migration
- CI/CD
- DevSecOps
- Developer Tools
website: https://www.bytebase.com
---
