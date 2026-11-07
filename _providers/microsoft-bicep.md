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
    agent_skills: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Microsoft Bicep Agentic Access
  operation_count: 23
  slug: microsoft-bicep-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 2
apis:
- description: Command-line interface for compiling and deploying Bicep files.
  name: Bicep CLI
  slug: bicep-cli
- description: Language server implementation for Bicep providing IntelliSense and validation.
  name: Bicep Language Server
  slug: bicep-language-server
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Create, validate, and manage ARM/Bicep template deployments
  name: Microsoft Bicep Deployments API
  slug: microsoft-bicep-deployments-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Manage versions of Template Spec resources
  name: Microsoft Bicep Template Spec Versions API
  slug: microsoft-bicep-template-spec-versions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: Manage Template Spec resources for reusable Bicep templates
  name: Microsoft Bicep Template Specs API
  slug: microsoft-bicep-template-specs-api
artifact_total: 34
collections:
- collection_type: open
  name: Microsoft Bicep Deployments API
  slug: open-microsoft-bicep-deployments-api
- collection_type: open
  name: Microsoft Bicep Deployments API
  slug: open-microsoft-bicep-deployments
- collection_type: open
  name: Microsoft Bicep Deployments Template Spec Versions API
  slug: open-microsoft-bicep-template-spec-versions-api
- collection_type: open
  name: Microsoft Bicep Deployments Template Specs API
  slug: open-microsoft-bicep-template-specs-api
- collection_type: open
  name: Microsoft Bicep Template Specs API
  slug: open-microsoft-bicep-template-specs
common:
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/rules/microsoft-bicep-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-bicep-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/rules/microsoft-bicep-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-bicep-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/vocabulary/microsoft-bicep-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-bicep-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/data-model/microsoft-bicep-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-bicep-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bicep/cli/microsoft-bicep-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-bicep-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/errors/microsoft-bicep-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-bicep-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/conformance/microsoft-bicep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-bicep-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-bicep/llms/microsoft-bicep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-bicep-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-bicep/mcp/microsoft-bicep-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-bicep-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-bicep/mcp/microsoft-bicep-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-bicep-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/well-known/microsoft-bicep-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-bicep-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-bicep/well-known/microsoft-bicep-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-bicep-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bicep/hosts/microsoft-bicep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-bicep-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bicep/vendors/microsoft-bicep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-bicep-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bicep/packages/microsoft-bicep-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-bicep-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bicep/packages/microsoft-bicep-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-bicep-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/security/microsoft-bicep-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-bicep-trust-center.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bicep/plans/microsoft-bicep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-bicep-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-bicep/rate-limits/microsoft-bicep-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-bicep-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bicep/finops/microsoft-bicep-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-bicep-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/bicep/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/bicep/blob/main/CODE_OF_CONDUCT.md
- group: agent
  href: https://artifacts.apis.io/microsoft-bicep/agentic-access/microsoft-bicep-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bicep-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/security/microsoft-bicep-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-bicep-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/security/microsoft-bicep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-bicep-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/authentication/microsoft-bicep-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-bicep-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bicep/scopes/microsoft-bicep-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-bicep-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/azure-sdk/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/resources/deployments
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: learn
  title: ''
  type: Learning Resources
  url: https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview
- group: build
  title: ''
  type: Bicep Examples
  url: https://github.com/Azure/bicep/tree/main/docs/examples
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/Azure/bicep/releases
- group: docs
  title: ''
  type: Contributing Guide
  url: https://github.com/Azure/bicep/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/bicep/blob/main/LICENSE
- group: design
  href: https://artifacts.apis.io/microsoft-bicep/json-ld/microsoft-bicep-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-bicep-context.jsonld
- group: docs
  href: https://artifacts.apis.io/microsoft-bicep/json-schema/microsoft-bicep-deployment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-bicep-deployment-schema.json
- group: docs
  href: https://artifacts.apis.io/microsoft-bicep/json-schema/microsoft-bicep-template-spec-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-bicep-template-spec-schema.json
created: '2024-01-15'
description: Microsoft Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources. It provides a transparent abstraction over ARM templates and offers a more concise syntax, improved type safety, and better support for modularity and code reuse.
finops:
- has_sources: true
  method: generated
  name: Microsoft Bicep Finops
  primary_unit: N/A
  service_category: Developer Tools / Infrastructure as Code
  slug: microsoft-bicep-finops
  template: false
image: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/media/bicep-logo.png
json_schemas:
- name: DeploymentExtended
  property_count: 6
  slug: microsoft-bicep-deployment-extended
- name: Microsoft Bicep Deployment
  property_count: 7
  slug: microsoft-bicep-deployment
- name: DeploymentValidateResult
  property_count: 5
  slug: microsoft-bicep-deployment-validate-result
- name: DeploymentWhatIf
  property_count: 2
  slug: microsoft-bicep-deployment-what-if
- name: ScopedDeployment
  property_count: 4
  slug: microsoft-bicep-scoped-deployment
- name: TemplateSpecListResult
  property_count: 2
  slug: microsoft-bicep-template-spec-list-result
- name: Microsoft Bicep Template Spec
  property_count: 7
  slug: microsoft-bicep-template-spec
- name: TemplateSpecUpdateModel
  property_count: 1
  slug: microsoft-bicep-template-spec-update-model
- name: TemplateSpecVersionListResult
  property_count: 2
  slug: microsoft-bicep-template-spec-version-list-result
- name: TemplateSpecVersionModel
  property_count: 7
  slug: microsoft-bicep-template-spec-version-model
- name: WhatIfOperationResult
  property_count: 3
  slug: microsoft-bicep-what-if-operation-result
jsonld:
- class_count: 0
  name: Microsoft Bicep Context
  property_count: 9
  slug: microsoft-bicep-context
layout: provider
mcp_servers:
- description: MCP server; 10 tools listed.
  name: Bicep MCP server
  slug: bicep-mcp-server
modified: '2026-05-19'
name: Microsoft Bicep
nav: Providers
network: true
overview: 'Microsoft Bicep publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deployments API, Template Spec Versions API, Template Specs API, and 2 more. Tagged areas include ArmTemplates, Microsoft Azure, Cloud, Deployment, and DevOps.


  The Microsoft Bicep catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Microsoft Bicep''s developer surface includes CLI, support, getting-started guide, authentication, engineering blog, documentation, API reference, and 40 more developer resources.'
plans:
- name: Microsoft Bicep Plans Pricing
  plan_count: 3
  slug: microsoft-bicep-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Microsoft Bicep Rate Limits
  slug: microsoft-bicep-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Microsoft Bicep — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-bicep-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Microsoft Bicep API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 3
    warn: 2
  slug: microsoft-bicep-rules
scopes:
- name: Microsoft Bicep Scopes
  scope_count: 1
  slug: microsoft-bicep-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.9
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 57.9
    developer_ergonomics: 71.4
    discoverability: 66.7
    operational_transparency: 36.8
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
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
screenshot: https://apis.io/screenshots/microsoft-bicep/microsoft-bicep-2026-06-20T185444.png
security:
- kind: authentication
  name: Microsoft Bicep Authentication
  slug: microsoft-bicep-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Bicep Domain Security
  slug: microsoft-bicep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Bicep Vulnerability Disclosure
  slug: microsoft-bicep-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Bicep Trust Center
  slug: microsoft-bicep-trust-center
  summary_line: GDPR
slug: microsoft-bicep
tags:
- ArmTemplates
- Microsoft Azure
- Cloud
- Deployment
- DevOps
- Infrastructure as Code
website: https://www.microsoft.com/
---
