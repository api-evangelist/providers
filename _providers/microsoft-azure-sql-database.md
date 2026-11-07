---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Microsoft Azure Sql Database Agentic Access
  operation_count: 15
  slug: microsoft-azure-sql-database-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 6
apis:
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Databases API from Azure SQL Database — 14 operation(s) from the Microsoft.Sql 2025-01-01 Azure Resource Manager contract (databases.json).
  name: Azure SQL Database Databases API
  slug: microsoft-azure-sql-database-databases-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ElasticPools API from Azure SQL Database — 6 operation(s) from the Microsoft.Sql 2025-01-01 Azure Resource Manager contract (elasticPools.json).
  name: Azure SQL Database ElasticPools API
  slug: microsoft-azure-sql-database-elasticpools-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The FailoverGroups API from Azure SQL Database — 8 operation(s) from the Microsoft.Sql 2025-01-01 Azure Resource Manager contract (failoverGroups.json).
  name: Azure SQL Database FailoverGroups API
  slug: microsoft-azure-sql-database-failovergroups-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Servers API from Azure SQL Database — 9 operation(s) from the Microsoft.Sql 2025-01-01 Azure Resource Manager contract (servers.json).
  name: Azure SQL Database Servers API
  slug: microsoft-azure-sql-database-servers-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Firewall Rules API from Azure SQL Database — 5 operation(s) from the Microsoft.Sql 2025-01-01 Azure Resource Manager contract (firewallRules.json).
  name: Azure SQL Database Firewall Rules API
  slug: microsoft-azure-sql-database-firewall-rules-api
artifact_total: 46
collections:
- collection_type: open
  name: Azure SQL Database REST Databases API
  slug: open-microsoft-azure-sql-database-databases-api
- collection_type: open
  name: Azure SQL Database REST Databases ElasticPools API
  slug: open-microsoft-azure-sql-database-elasticpools-api
- collection_type: open
  name: Azure SQL Database REST Databases FailoverGroups API
  slug: open-microsoft-azure-sql-database-failovergroups-api
- collection_type: open
  name: Azure SQL Database REST Databases FirewallRules API
  slug: open-microsoft-azure-sql-database-firewallrules-api
- collection_type: open
  name: Azure SQL Database REST Databases Servers API
  slug: open-microsoft-azure-sql-database-servers-api
- collection_type: open
  name: Azure SQL Database REST API
  slug: open-microsoft-azure-sql-database
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/rules/microsoft-azure-sql-database-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-sql-database-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/json-ld/microsoft-azure-sql-database-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-sql-database-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/vocabulary/microsoft-azure-sql-database-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-sql-database-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-sql-database/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/data-model/microsoft-azure-sql-database-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-sql-database-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-sql-database/cli/microsoft-azure-sql-database-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-sql-database-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/conventions/microsoft-azure-sql-database-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-sql-database-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/conventions/microsoft-azure-sql-database-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-sql-database-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/lifecycle/microsoft-azure-sql-database-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-sql-database-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/errors/microsoft-azure-sql-database-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-sql-database-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-sql-database/conformance/microsoft-azure-sql-database-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-sql-database-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-sql-database/llms/microsoft-azure-sql-database-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-sql-database-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-sql-database/mcp/microsoft-azure-sql-database-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-sql-database-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-sql-database/mcp/microsoft-azure-sql-database-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-sql-database-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/well-known/microsoft-azure-sql-database-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-sql-database-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-sql-database/well-known/microsoft-azure-sql-database-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-sql-database-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-sql-database/hosts/microsoft-azure-sql-database-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-sql-database-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-sql-database/integrations/microsoft-azure-sql-database-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-azure-sql-database-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-sql-database/vendors/microsoft-azure-sql-database-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-sql-database-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-sql-database/packages/microsoft-azure-sql-database-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-sql-database-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-sql-database/packages/microsoft-azure-sql-database-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-sql-database-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/scopes/microsoft-azure-sql-database-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-sql-database-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/security/microsoft-azure-sql-database-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-sql-database-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/security/microsoft-azure-sql-database-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-sql-database-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-sql-database/plans/microsoft-azure-sql-database-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-sql-database-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-sql-database/rate-limits/microsoft-azure-sql-database-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-sql-database-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-sql-database/finops/microsoft-azure-sql-database-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-sql-database-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-sql-database/capabilities/microsoft-azure-sql-database-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-sql-database-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-sql-database/agentic-access/microsoft-azure-sql-database-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-sql-database-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/security/microsoft-azure-sql-database-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-sql-database-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-sql-database/authentication/microsoft-azure-sql-database-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-sql-database-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-sql/database/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-sql/database/single-database-create-quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/product/azure-sql-database/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-sql-database
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure SQL Database is a fully managed relational database service built on the SQL Server engine with built-in intelligence, high availability, and elastic scaling. It is managed through the Microsoft.Sql Azure Resource Manager REST API at management.azure.com (servers, databases, elastic pools, failover groups, firewall rules), with first-party SDKs for Python, JavaScript, .NET, Go and Java.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Sql Database Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-sql-database-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-sql-database.png
json_schemas:
- name: CheckNameAvailabilityRequest
  property_count: 2
  slug: microsoft-azure-sql-database-check-name-availability-request
- name: CheckNameAvailabilityResponse
  property_count: 4
  slug: microsoft-azure-sql-database-check-name-availability-response
- name: DatabaseListResult
  property_count: 2
  slug: microsoft-azure-sql-database-database-list-result
- name: Database
  property_count: 11
  slug: microsoft-azure-sql-database-database
- name: DatabaseUpdate
  property_count: 4
  slug: microsoft-azure-sql-database-database-update
- name: ElasticPoolListResult
  property_count: 2
  slug: microsoft-azure-sql-database-elastic-pool-list-result
- name: ElasticPool
  property_count: 9
  slug: microsoft-azure-sql-database-elastic-pool
- name: ElasticPoolUpdate
  property_count: 3
  slug: microsoft-azure-sql-database-elastic-pool-update
- name: ExportDatabaseDefinition
  property_count: 7
  slug: microsoft-azure-sql-database-export-database-definition
- name: FailoverGroupListResult
  property_count: 2
  slug: microsoft-azure-sql-database-failover-group-list-result
- name: FailoverGroup
  property_count: 7
  slug: microsoft-azure-sql-database-failover-group
- name: FailoverGroupUpdate
  property_count: 2
  slug: microsoft-azure-sql-database-failover-group-update
- name: FirewallRuleListResult
  property_count: 2
  slug: microsoft-azure-sql-database-firewall-rule-list-result
- name: FirewallRuleList
  property_count: 1
  slug: microsoft-azure-sql-database-firewall-rule-list
- name: FirewallRule
  property_count: 4
  slug: microsoft-azure-sql-database-firewall-rule
- name: ImportExistingDatabaseDefinition
  property_count: 7
  slug: microsoft-azure-sql-database-import-existing-database-definition
- name: ImportExportOperationResult
  property_count: 5
  slug: microsoft-azure-sql-database-import-export-operation-result
- name: ImportNewDatabaseDefinition
  property_count: 11
  slug: microsoft-azure-sql-database-import-new-database-definition
- name: RefreshExternalGovernanceStatusOperationResult
  property_count: 5
  slug: microsoft-azure-sql-database-refresh-external-governance-status-operation-result
- name: Server
  property_count: 9
  slug: microsoft-azure-sql-database-server
- name: ServerUpdate
  property_count: 3
  slug: microsoft-azure-sql-database-server-update
jsonld:
- class_count: 42
  name: Microsoft Azure Sql Database Context
  property_count: 120
  slug: microsoft-azure-sql-database-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 13 tools listed.
  name: Azure MCP Server - Azure SQL Database tools
  slug: azure-mcp-server---azure-sql-database-tools
modified: '2026-11-05'
name: Azure SQL Database
nav: Providers
network: true
overview: 'Azure SQL Database publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Databases API, ElasticPools API, FailoverGroups API, and 2 more. Tagged areas include Database, SQL, Relational Database, Microsoft Azure, and Microsoft.


  The Azure SQL Database catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure SQL Database''s developer surface includes CLI, changelog, authentication, developer portal, pricing, documentation, getting-started guide, and 41 more developer resources.'
plans:
- name: Microsoft Azure Sql Database Plans Pricing
  plan_count: 0
  slug: microsoft-azure-sql-database-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Microsoft Azure Sql Database Rate Limits
  slug: microsoft-azure-sql-database-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Azure SQL Database API Rules
  rule_count: 56
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 6
  slug: microsoft-azure-sql-database-rules
scopes:
- name: Microsoft Azure Sql Database Scopes
  scope_count: 1
  slug: microsoft-azure-sql-database-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 22.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.4
    developer_ergonomics: 66.1
    discoverability: 85.0
    operational_transparency: 76.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 83.3
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-sql-database/microsoft-azure-sql-database-2026-06-20T185438.png
security:
- kind: authentication
  name: Microsoft Azure Sql Database Authentication
  slug: microsoft-azure-sql-database-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Sql Database Domain Security
  slug: microsoft-azure-sql-database-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Sql Database Vulnerability Disclosure
  slug: microsoft-azure-sql-database-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Sql Database Trust Center
  slug: microsoft-azure-sql-database-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: geo-failover
  slug: microsoft-azure-sql-database-geo-failover
- name: provision-database
  slug: microsoft-azure-sql-database-provision-database
slug: microsoft-azure-sql-database
tags:
- Database
- SQL
- Relational Database
- Microsoft Azure
- Microsoft
- Cloud Database
- Managed Database
- SQL Server
website: https://microsoft.com
---
