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
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Integration Services Agentic Access
  operation_count: 7
  slug: microsoft-azure-integration-services-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Azure Logic Apps is a cloud-based platform for creating and running automated workflows that integrate apps, data, services, and systems. It provides a visual designer and hundreds of pre-built connec
  name: Azure Logic Apps
  slug: azure-logic-apps
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Azure Service Bus is a fully managed enterprise message broker with message queues and publish-subscribe topics. It decouples applications and services from each other, providing reliable asynchronous
  name: Azure Service Bus
  slug: azure-service-bus
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Azure Event Grid is a highly scalable, fully managed publish-subscribe event distribution service. It enables event-driven architectures by routing events from Azure services and custom sources to eve
  name: Azure Event Grid
  slug: azure-event-grid
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Azure Event Hubs is a big data streaming platform and event ingestion service capable of receiving and processing millions of events per second. It is used for telemetry ingestion, application logging
  name: Azure Event Hubs
  slug: azure-event-hubs
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Microsoft Azure Integration Services Operations API
  slug: microsoft-azure-integration-services-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Services operations
  name: Azure API Management
  slug: microsoft-azure-integration-services-services-api
artifact_total: 23
collections:
- collection_type: open
  name: Azure API Management REST Operations API
  slug: open-microsoft-azure-integration-services-operations-api
- collection_type: open
  name: Azure API Management REST Operations Services API
  slug: open-microsoft-azure-integration-services-services-api
- collection_type: open
  name: Azure API Management REST API
  slug: open-microsoft-azure-integration-services
common:
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-integration-services/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/rules/microsoft-azure-integration-services-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-integration-services-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/json-ld/microsoft-azure-integration-services-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-integration-services-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/vocabulary/microsoft-azure-integration-services-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-integration-services-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/data-model/microsoft-azure-integration-services-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-integration-services-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-integration-services/cli/microsoft-azure-integration-services-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-integration-services-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/conventions/microsoft-azure-integration-services-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-integration-services-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/conventions/microsoft-azure-integration-services-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-integration-services-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/lifecycle/policies/modern
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/lifecycle/microsoft-azure-integration-services-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-integration-services-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/errors/microsoft-azure-integration-services-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-integration-services-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-integration-services/conformance/microsoft-azure-integration-services-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-integration-services-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-integration-services/llms/microsoft-azure-integration-services-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-integration-services-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-integration-services/mcp/microsoft-azure-integration-services-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-integration-services-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-integration-services/mcp/microsoft-azure-integration-services-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-integration-services-mcp.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-integration-services/hosts/microsoft-azure-integration-services-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-integration-services-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-integration-services/vendors/microsoft-azure-integration-services-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-integration-services-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-integration-services/packages/microsoft-azure-integration-services-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-integration-services-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-integration-services/packages/microsoft-azure-integration-services-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-integration-services-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/azure/
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-integration-services/rate-limits/microsoft-azure-integration-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-integration-services-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-integration-services/finops/microsoft-azure-integration-services-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-integration-services-finops.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-integration-services/plans/microsoft-azure-integration-services-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-integration-services-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-integration-services/capabilities/microsoft-azure-integration-services-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-integration-services-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-integration-services/agentic-access/microsoft-azure-integration-services-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-integration-services-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-integration-services/security/microsoft-azure-integration-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-integration-services-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-integration-services/authentication/microsoft-azure-integration-services-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-integration-services-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-integration-services/scopes/microsoft-azure-integration-services-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-integration-services-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/category/integration
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/?product=integration
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/integrationsonazureblog
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@MicrosoftAzure
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/category/azure
- group: start
  title: ''
  type: Console
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
created: '2026-03-16'
description: Microsoft Azure Integration Services is a collection of cloud-based integration capabilities that connect applications, data, and processes across cloud and on-premises environments. It includes API Management, Logic Apps, Service Bus, Event Grid, and Event Hubs to enable enterprise integration, messaging, and event-driven architectures.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Integration Services Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-integration-services-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-integration-services.png
json_schemas:
- name: OperationList
  property_count: 2
  slug: microsoft-azure-integration-services-operation-list
jsonld:
- class_count: 5
  name: Microsoft Azure Integration Services Context
  property_count: 11
  slug: microsoft-azure-integration-services-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 14 tools listed.
  name: Azure MCP Server
  slug: azure-mcp-server
modified: '2026-09-16'
name: Microsoft Azure Integration Services
nav: Providers
network: true
overview: 'Microsoft Azure Integration Services publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Azure Logic Apps, Azure Service Bus, Azure Event Grid, and 3 more. Tagged areas include API Management, Enterprise, Event-Driven, Integration, and Messaging.


  The Microsoft Azure Integration Services catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Integration Services'' developer surface includes changelog, getting-started guide, CLI, API reference, authentication, developer portal, documentation, and 39 more developer resources.'
plans:
- name: Microsoft Azure Integration Services Plans Pricing
  plan_count: 0
  slug: microsoft-azure-integration-services-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 7
  name: Microsoft Azure Integration Services Rate Limits
  slug: microsoft-azure-integration-services-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Microsoft Azure Integration Services API Rules
  rule_count: 53
  severity_counts:
    error: 42
    hint: 0
    info: 3
    warn: 8
  slug: microsoft-azure-integration-services-rules
scopes:
- name: Microsoft Azure Integration Services Scopes
  scope_count: 1
  slug: microsoft-azure-integration-services-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 63.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.2
    catalog_earned_first_party: 12.0
    catalog_gap: 40.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.9
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 89.9
    discoverability: 76.7
    operational_transparency: 68.4
  previous_composite: 49.4
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
screenshot: https://apis.io/screenshots/microsoft-azure-integration-services/microsoft-azure-integration-services-2026-06-20T185419.png
security:
- kind: authentication
  name: Microsoft Azure Integration Services Authentication
  slug: microsoft-azure-integration-services-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Integration Services Domain Security
  slug: microsoft-azure-integration-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: provision-service-bus-queue
  slug: microsoft-azure-integration-services-provision-service-bus-queue
- name: run-logic-app-trigger
  slug: microsoft-azure-integration-services-run-logic-app-trigger
- name: subscribe-event-grid-topic
  slug: microsoft-azure-integration-services-subscribe-event-grid-topic
slug: microsoft-azure-integration-services
tags:
- API Management
- Enterprise
- Event-Driven
- Integration
- Messaging
website: https://azure.microsoft.com/en-us/products/category/integration
---
