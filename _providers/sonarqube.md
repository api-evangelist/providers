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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sonarqube Agentic Access
  operation_count: 11
  slug: sonarqube-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: Code issue search and management
  name: SonarQube Issues API
  slug: sonarqube-issues-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: Component metrics and measurement data
  name: SonarQube Measures API
  slug: sonarqube-measures-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: Project creation, search, and management
  name: SonarQube Projects API
  slug: sonarqube-projects-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: Quality gate configuration and status
  name: SonarQube Quality Gates API
  slug: sonarqube-quality-gates-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: Analysis rule search and configuration
  name: SonarQube Rules API
  slug: sonarqube-rules-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: SonarQube server status and health monitoring
  name: SonarQube System API
  slug: sonarqube-system-api
- baseURL_template: https://{sonarqubeHost}/api
  baseurl_source: spec_template
  description: User account management
  name: SonarQube Users API
  slug: sonarqube-users-api
artifact_total: 37
asyncapis:
- description: ''
  name: Sonarqube Webhooks
  slug: sonarqube-webhooks
collections:
- collection_type: open
  name: SonarQube Web Issues API
  slug: open-sonarqube-issues-api
- collection_type: open
  name: SonarQube Web Measures API
  slug: open-sonarqube-measures-api
- collection_type: open
  name: SonarQube Web Projects API
  slug: open-sonarqube-projects-api
- collection_type: open
  name: SonarQube Web Quality Gates API
  slug: open-sonarqube-quality-gates-api
- collection_type: open
  name: SonarQube Web Rules API
  slug: open-sonarqube-rules-api
- collection_type: open
  name: SonarQube Web System API
  slug: open-sonarqube-system-api
- collection_type: open
  name: SonarQube Web Users API
  slug: open-sonarqube-users-api
common:
- group: agent
  href: https://artifacts.apis.io/sonarqube/agentic-access/sonarqube-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sonarqube-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/rules/sonarqube-rules.yml
  title: ''
  type: Spectral
  url: rules/sonarqube-rules.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/rules/sonarqube-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/sonarqube-jsonschema-spectral-rules.yml
- group: agent
  href: https://artifacts.apis.io/sonarqube/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/asyncapi/sonarqube-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sonarqube-webhooks.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/data-model/sonarqube-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sonarqube-data-model.yml
- group: build
  href: https://artifacts.apis.io/sonarqube/cli/sonarqube-cli.yml
  title: ''
  type: CLI
  url: cli/sonarqube-cli.yml
- group: operate
  href: https://artifacts.apis.io/sonarqube/changelog/sonarqube-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sonarqube-changelog.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/conventions/sonarqube-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sonarqube-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sonarsource.com/
- group: auth
  href: https://artifacts.apis.io/sonarqube/security/sonarqube-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sonarqube-trust-center.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.sonarsource.com/sonarqube-server/server-update-and-maintenance/maintenance/deprecations/deprecation-policy/
- group: design
  href: https://artifacts.apis.io/sonarqube/lifecycle/sonarqube-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sonarqube-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/errors/sonarqube-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sonarqube-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sonarqube/conformance/sonarqube-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sonarqube-conformance.yml
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-webhooks.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-webhooks.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-user_tokens.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-user_tokens.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-user_groups.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-user_groups.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-tests.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-tests.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-settings.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-settings.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-security.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-security.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-root.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-root.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-qualityprofiles.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-qualityprofiles.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-projectpullrequests.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-projectpullrequests.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-projectlink.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-projectlink.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-projectbranches.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-projectbranches.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-projectanalyses.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-projectanalyses.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-project_tags.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-project_tags.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-plugins.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-plugins.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-permissions.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-permissions.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-notifications.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-notifications.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-newcodeperiods.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-newcodeperiods.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-navigation.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-navigation.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-hotspots.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-hotspots.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-favorites.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-favorites.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-duplications.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-duplications.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-developers.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-developers.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-components.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-components.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-commons.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-commons.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-ce.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-ce.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-batch.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-batch.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-alm_settings.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-alm_settings.proto
- group: other
  href: https://artifacts.apis.io/sonarqube/grpc/sonarqube-ws-alm_integrations.proto
  title: ''
  type: Protobuf
  url: grpc/sonarqube-ws-alm_integrations.proto
- group: agent
  href: https://artifacts.apis.io/sonarqube/llms/sonarqube-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sonarqube-llms.txt
- group: build
  href: https://artifacts.apis.io/sonarqube/mcp/sonarqube-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sonarqube-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/sonarqube/well-known/sonarqube-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sonarqube-status-security.txt
- group: agent
  href: https://artifacts.apis.io/sonarqube/well-known/sonarqube-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sonarqube-well-known.yml
- group: other
  href: https://artifacts.apis.io/sonarqube/hosts/sonarqube-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sonarqube-hosts.yml
- group: build
  href: https://artifacts.apis.io/sonarqube/integrations/sonarqube-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/sonarqube-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/sonarqube/vendors/sonarqube-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sonarqube-vendors.yml
- group: build
  href: https://artifacts.apis.io/sonarqube/packages/sonarqube-packages.yml
  title: ''
  type: SDKs
  url: packages/sonarqube-packages.yml
- group: build
  href: https://artifacts.apis.io/sonarqube/packages/sonarqube-packages.yml
  title: ''
  type: Packages
  url: packages/sonarqube-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sonarsource.com/
- group: auth
  title: ''
  type: Security
  url: https://www.sonarsource.com/solutions/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.sonarsource.com/products/sonarqube/ide/roadmap/
- group: auth
  href: https://artifacts.apis.io/sonarqube/authentication/sonarqube-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sonarqube-authentication.yml
- group: commercial
  href: https://artifacts.apis.io/sonarqube/plans/sonarqube-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sonarqube-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/sonarqube/finops/sonarqube-finops.yml
  title: ''
  type: FinOps
  url: finops/sonarqube-finops.yml
- group: other
  href: https://artifacts.apis.io/sonarqube/capabilities/sonarqube-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sonarqube-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sonarqube/overview
- group: auth
  href: https://artifacts.apis.io/sonarqube/security/sonarqube-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonarqube-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonarsource
- group: start
  title: ''
  type: Portal
  url: https://www.sonarsource.com/products/sonarqube/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonarsource.com/sonarqube-server/
- group: docs
  title: ''
  type: Reference
  url: https://api-docs.sonarsource.com/
- group: company
  title: ''
  type: Website
  url: https://www.sonarsource.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SonarSource
- group: company
  title: ''
  type: Blog
  url: https://www.sonarsource.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://community.sonarsource.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sonarsource.com/plans-and-pricing/
- group: design
  href: https://artifacts.apis.io/sonarqube/vocabulary/sonarqube-vocabulary.yml
  title: SonarQube Vocabulary
  type: Vocabulary
  url: vocabulary/sonarqube-vocabulary.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/SonarSource/sonarqube-mcp-server
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonarqube.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonarsource.com/legal/sonarqube/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonarsource.com/company/privacy/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sonarsource.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sonarsource.com/get-started/cloud/
- group: start
  title: ''
  type: SignUp
  url: https://www.sonarsource.com/products/sonarqube/cloud/signup/
- group: operate
  title: ''
  type: ChangeLog
  url: https://community.sonarsource.com/c/sq/releases/24
- group: commercial
  title: ''
  type: Legal
  url: https://www.sonarsource.com/legal/
- group: other
  title: ''
  type: Accessibility
  url: https://www.sonarsource.com/accessibility/
- group: other
  title: ''
  type: Subprocessors
  url: https://www.sonarsource.com/legal/sub-processors/
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.sonarsource.com/legal/data-processing-addendum/
- group: operate
  title: ''
  type: SLA
  url: https://www.sonarsource.com/legal/sonarcloud/service-level-agreement/
- group: other
  title: ''
  type: Downloads
  url: https://www.sonarsource.com/products/sonarqube/downloads/
- group: company
  title: ''
  type: Newsroom
  url: https://www.sonarsource.com/company/newsroom/
- group: company
  title: ''
  type: Partners
  url: https://www.sonarsource.com/company/partners/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonarsource.com/sonarqube-mcp-server/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sonarsource.com/sonarqube-cli/
created: '2026-03-16'
description: SonarQube is SonarSource's code quality and code security platform, shipped as the self-managed SonarQube Server (Community Build, Developer, Enterprise and Data Center editions), the hosted SonarQube Cloud, SonarQube for IDE and the SonarQube CLI. Every SonarQube Server instance exposes the Web API at <instance>/api (and the newer Web API v2 at /api/v2) for projects, issues, measures, quality gates, rules, users, webhooks and system administration, documented inside the instance and described by protobuf message contracts in the open-source sonar-ws module. SonarSource also publishes an official MCP server (self-hosted container, a Server-hosted extension at <instance>/mcp, and a Sonar-hosted OAuth endpoint for SonarQube Cloud).
examples:
- key_count: 1
  name: Sonarqube Component Measures Example
  slug: sonarqube-component-measures-example
- key_count: 1
  name: Sonarqube Quality Gate Status Example
  slug: sonarqube-quality-gate-status-example
- key_count: 3
  name: Sonarqube Search Issues Example
  slug: sonarqube-search-issues-example
finops:
- has_sources: false
  method: generated
  name: Sonarqube Finops
  primary_unit: request
  service_category: API
  slug: sonarqube-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonarqube.png
json_schemas:
- name: Issue
  property_count: 21
  slug: sonarqube-issue
- name: Project
  property_count: 8
  slug: sonarqube-project
- name: QualityGate
  property_count: 5
  slug: sonarqube-quality-gate
json_structures:
- name: Sonarqube Web Api Structure
  property_count: 0
  slug: sonarqube-web-api-structure
jsonld:
- class_count: 0
  name: Sonarqube Context
  property_count: 7
  slug: sonarqube-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: 'SonarSource ships one official MCP server, SonarSource/sonarqube-mcp-server (Java, LGPL), in three deployments: (1) a Sonar-hosted endpoint embedded in SonarQube Cloud at https://api.sonarcloud.io/mcp'
  name: SonarQube MCP Server
  slug: sonarqube
modified: '2026-11-05'
name: SonarQube
nav: Providers
network: true
overview: 'SonarQube publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Issues API, Measures API, Projects API, and 4 more. Tagged areas include Code Quality, Developer Tools, DevOps, Security, and Static Analysis.


  The SonarQube catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  SonarQube''s developer surface includes CLI, changelog, authentication, developer portal, documentation, engineering blog, support, and 82 more developer resources.'
plans:
- name: Sonarqube Plans Pricing
  plan_count: 3
  slug: sonarqube-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Sonarqube Rate Limits
  slug: sonarqube-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: SonarQube — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sonarqube-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 9
  extends: []
  name: SonarQube API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 4
  slug: sonarqube-rules
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 40
    catalog_earned: 62.5
    catalog_earned_first_party: 12.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.7
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 68.7
    developer_ergonomics: 74.4
    discoverability: 58.3
    operational_transparency: 57.9
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sonarqube/sonarqube-2026-06-20T194159.png
security:
- kind: authentication
  name: Sonarqube Authentication
  slug: sonarqube-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Sonarqube Domain Security
  slug: sonarqube-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sonarqube Trust Center
  slug: sonarqube-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001:2022, ISO/IEC 27018:2019, CSA STAR Level 1, PCI DSS SAQ-A
skill_count: 3
skills:
- name: sonarqube-check-quality-gate
  slug: sonarqube-check-quality-gate
- name: sonarqube-provision-project
  slug: sonarqube-provision-project
- name: sonarqube-triage-issues
  slug: sonarqube-triage-issues
slug: sonarqube
tags:
- Code Quality
- Developer Tools
- DevOps
- Security
- Static Analysis
- Code Security
- SAST
website: https://www.sonarsource.com/
---
