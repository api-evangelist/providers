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
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Policy Agentic Access
  operation_count: 7
  slug: microsoft-azure-policy-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 7
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure Policy Operations API
  slug: microsoft-azure-policy-operations-api
- description: 'Azure Resource Manager REST API for Azure Policy (Microsoft.Authorization) - policy definitions, policy set definitions (initiatives), assignments and their versions at subscription, management group '
  name: Azure Policy REST API
  slug: microsoft-azure-policy-policy-definitions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PolicyAssignments API from Azure Policy — 6 operation(s) for policyassignments.
  name: Azure Policy Policy Assignments API
  slug: microsoft-azure-policy-policyassignments-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PolicyDefinitions API from Azure Policy — 6 operation(s) for policydefinitions.
  name: Azure Policy Policy Definitions API
  slug: microsoft-azure-policy-policydefinitions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PolicyDefinitionVersions API from Azure Policy — 9 operation(s) for policydefinitionversions.
  name: Azure Policy Policy Definition Versions API
  slug: microsoft-azure-policy-policydefinitionversions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PolicySetDefinitions API from Azure Policy — 6 operation(s) for policysetdefinitions.
  name: Azure Policy Policy Set Definitions API
  slug: microsoft-azure-policy-policysetdefinitions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The PolicySetDefinitionVersions API from Azure Policy — 9 operation(s) for policysetdefinitionversions.
  name: Azure Policy Policy Set Definition Versions API
  slug: microsoft-azure-policy-policysetdefinitionversions-api
artifact_total: 29
collections:
- collection_type: open
  name: Azure Policy REST Operations API
  slug: open-microsoft-azure-policy-operations-api
- collection_type: open
  name: Azure Policy REST Operations Policy Definitions API
  slug: open-microsoft-azure-policy-policy-definitions-api
- collection_type: open
  name: Azure Policy REST API
  slug: open-microsoft-azure-policy
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/rules/microsoft-azure-policy-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-policy-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/json-ld/microsoft-azure-policy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-policy-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/vocabulary/microsoft-azure-policy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-policy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-policy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/data-model/microsoft-azure-policy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-policy-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-policy/cli/microsoft-azure-policy-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-policy-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/conventions/microsoft-azure-policy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-policy-conventions.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/lifecycle/microsoft-azure-policy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-policy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/errors/microsoft-azure-policy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-policy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-policy/conformance/microsoft-azure-policy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-policy-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-policy/llms/microsoft-azure-policy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-policy-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-policy/mcp/microsoft-azure-policy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-policy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-policy/mcp/microsoft-azure-policy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-policy-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-policy/well-known/microsoft-azure-policy-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-policy-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-policy/well-known/microsoft-azure-policy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-policy-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-policy/hosts/microsoft-azure-policy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-policy-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-policy/vendors/microsoft-azure-policy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-policy-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-policy/packages/microsoft-azure-policy-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-policy-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-policy/packages/microsoft-azure-policy-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-policy-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-policy/plans/microsoft-azure-policy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-policy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-policy/rate-limits/microsoft-azure-policy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-policy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-policy/finops/microsoft-azure-policy-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-policy-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-policy/agentic-access/microsoft-azure-policy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-policy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-policy/security/microsoft-azure-policy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-policy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-policy/authentication/microsoft-azure-policy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-policy-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-policy/scopes/microsoft-azure-policy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-policy-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/governance/policy/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/azure-policy
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Azure Policy is a service that enables you to create, assign, and manage policies that enforce rules and effects over your Azure resources. It helps with compliance, governance, and consistency by evaluating resources against business standards and reporting on their state.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Policy Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-policy-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-policy.png
json_schemas:
- name: OperationList
  property_count: 2
  slug: microsoft-azure-policy-operation-list
- name: PolicyAssignment
  property_count: 7
  slug: microsoft-azure-policy-policy-assignment
- name: PolicyDefinition
  property_count: 5
  slug: microsoft-azure-policy-policy-definition
- name: PolicyDefinitionVersion
  property_count: 5
  slug: microsoft-azure-policy-policy-definition-version
- name: PolicySetDefinition
  property_count: 5
  slug: microsoft-azure-policy-policy-set-definition
- name: PolicySetDefinitionVersionListResult
  property_count: 2
  slug: microsoft-azure-policy-policy-set-definition-version-list-result
- name: PolicySetDefinitionVersion
  property_count: 5
  slug: microsoft-azure-policy-policy-set-definition-version
jsonld:
- class_count: 34
  name: Microsoft Azure Policy Context
  property_count: 60
  slug: microsoft-azure-policy-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 1 tool listed.
  name: Azure MCP Server - Azure Policy tools
  slug: azure-mcp-server---azure-policy-tools
modified: '2026-09-16'
name: Azure Policy
nav: Providers
network: true
overview: 'Azure Policy publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Operations API, REST API, Policy Assignments API, and 4 more. Tagged areas include Compliance, Governance, Policy, and Resource Management.


  The Azure Policy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Policy''s developer surface includes CLI, changelog, engineering blog, getting-started guide, authentication, developer portal, pricing, and 35 more developer resources.'
plans:
- name: Microsoft Azure Policy Plans Pricing
  plan_count: 0
  slug: microsoft-azure-policy-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 6
  name: Microsoft Azure Policy Rate Limits
  slug: microsoft-azure-policy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Azure Policy API Rules
  rule_count: 53
  severity_counts:
    error: 45
    hint: 0
    info: 4
    warn: 4
  slug: microsoft-azure-policy-rules
scopes:
- name: Microsoft Azure Policy Scopes
  scope_count: 1
  slug: microsoft-azure-policy-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.2
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 58.0
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-policy/microsoft-azure-policy-2026-06-20T185431.png
security:
- kind: authentication
  name: Microsoft Azure Policy Authentication
  slug: microsoft-azure-policy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Policy Domain Security
  slug: microsoft-azure-policy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: assign-azure-policy
  slug: microsoft-azure-policy-assign-policy
- name: author-custom-policy-definition
  slug: microsoft-azure-policy-author-custom-definition
slug: microsoft-azure-policy
tags:
- Compliance
- Governance
- Policy
- Resource Management
website: https://azure.microsoft.com/en-us/products/azure-policy
---
