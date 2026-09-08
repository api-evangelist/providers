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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-09-07'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Power Platform Agentic Access
  operation_count: 8
  slug: microsoft-power-platform-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- description: The Microsoft Dataverse Web API provides OData v4 RESTful access to the Dataverse data platform that underpins Power Platform. Developers can perform CRUD operations on tables, execute actions and fun
  name: Microsoft Dataverse Web API
  slug: dataverse-api
- description: The Power Platform Admin API enables programmatic management of Power Platform environments, connectors, data loss prevention policies, and tenant settings. Administrators can create and manage enviro
  name: Power Platform Admin API
  slug: admin-api
- description: Power Platform Connectors provide pre-built integrations with hundreds of external services and enable developers to create custom connectors using OpenAPI definitions. Connectors abstract API authent
  name: Power Platform Connectors
  slug: connectors-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Metadata API from Microsoft Power Platform — 3 operation(s) for metadata.
  name: Microsoft Power Platform Metadata API
  slug: microsoft-power-platform-metadata-api
- baseURL: https://{org}.api.crm.dynamics.com/api/data/v9.2/
  baseurl_source: declared
  description: The Records API from Microsoft Power Platform — 2 operation(s) for records.
  name: Microsoft Power Platform Records API
  slug: microsoft-power-platform-records-api
- description: The unified REST API for Power Platform administration, at https://api.powerplatform.com/{namespace}/{resource}?api-version={version}. Namespaces include licensing, appmanagement, environmentmanagemen
  name: Power Platform API
  slug: power-platform-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Microsoft.PowerPlatform Azure Resource Manager provider - 19 operations over enterprisePolicies, accounts, privateEndpointConnections and privateLinkResources, covering customer-managed encryption
  name: Power Platform Enterprise Policies (Azure Resource Manager)
  slug: microsoft-power-platform-enterprise-policies
artifact_total: 22
asyncapis:
- description: ''
  name: Microsoft Power Platform Webhooks
  slug: microsoft-power-platform-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dataverse Web Metadata API
  slug: open-microsoft-power-platform-metadata-api
- collection_type: open
  name: Microsoft Dataverse Web Metadata Records API
  slug: open-microsoft-power-platform-records-api
- collection_type: open
  name: Microsoft Dataverse Web API
  slug: open-microsoft-power-platform
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/power-platform
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-power-platform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-power-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-power-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-power-platform-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-power-platform
- group: start
  title: ''
  type: Portal
  url: https://make.powerapps.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-platform/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerapps.microsoft.com/en-us/pricing/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-authentication-v2
- group: company
  title: ''
  type: Blog
  url: https://powerplatform.microsoft.com/en-us/blog/
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
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/power-platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-platform/developer/get-started
- group: start
  title: ''
  type: SignUp
  url: https://www.microsoft.com/en-us/power-platform/products/power-apps/free
- group: operate
  title: ''
  type: Roadmap
  url: https://learn.microsoft.com/en-us/power-platform/release-plan/
- group: operate
  title: ''
  type: Community
  url: https://community.powerplatform.com/
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-power-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/microsoft-power-platform-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-power-platform-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-power-platform-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-power-platform-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-power-platform-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-power-platform-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-power-platform-security.txt
- group: auth
  title: ''
  type: Security
  url: security/microsoft-power-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-power-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-power-platform-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/microsoft-power-platform-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-power-platform-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-power-platform-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/microsoft-power-platform-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-power-platform-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-power-platform-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-power-platform-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-power-platform-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-power-platform-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-power-platform-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-power-platform-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-power-platform-records-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/microsoft-power-platform-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-power-platform-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/microsoft-power-platform-finops.yml
created: '2024-01-01'
description: Microsoft Power Platform is a suite of low-code development tools including Power Apps, Power Automate, Power BI, and Power Virtual Agents. It provides APIs for accessing Dataverse, managing environments, and integrating with external services through connectors.
finops:
- name: Microsoft Power Platform Finops
  service_category: API
  slug: microsoft-power-platform-finops
image: /assets/icons/microsoft-power-platform.png
layout: provider
mcp_servers:
- description: 'Microsoft ships a first-party MCP server for Dataverse, the data platform underneath Power Platform. It is reachable two ways: a remote HTTP endpoint on the customer''s own Dataverse environment host, '
  name: Microsoft Dataverse MCP Server
  slug: microsoft-dataverse-mcp-server
modified: '2026-09-06'
name: Microsoft Power Platform
nav: Providers
network: true
overview: 'Microsoft Power Platform publishes 3 APIs on the [APIs.io](https://apis.io/) network: Metadata API, Records API, and Power Platform Enterprise Policies (Azure Resource Manager). Tagged areas include Dataverse, Low-Code, Microsoft, Power Apps, and Power Automate.


  The Microsoft Power Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Microsoft Power Platform''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, API reference, and 41 more developer resources.'
plans:
- name: Microsoft Power Platform Plans Pricing
  plan_count: 4
  slug: microsoft-power-platform-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 7
  name: Microsoft Power Platform Rate Limits
  slug: microsoft-power-platform-rate-limits
scopes:
- name: Microsoft Power Platform Scopes
  scope_count: 5
  slug: microsoft-power-platform-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials/implicit
score:
  band: exemplar
  composite: 76.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 89.5
    commercial_clarity: 89.5
    contract_governance: 18.2
    contract_quality: 54.6
    developer_ergonomics: 80.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 75.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 71.6
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-power-platform/refs/heads/main/screenshots/microsoft-power-platform-2026-06-20T185525.png
security:
- kind: authentication
  name: Microsoft Power Platform Authentication
  slug: microsoft-power-platform-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Power Platform Domain Security
  slug: microsoft-power-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Power Platform Vulnerability Disclosure
  slug: microsoft-power-platform-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Microsoft Power Platform Trust Center
  slug: microsoft-power-platform-trust-center
  summary_line: trust center published
slug: microsoft-power-platform
tags:
- Dataverse
- Low-Code
- Microsoft
- Power Apps
- Power Automate
- Power BI
website: https://www.microsoft.com/en-us/power-platform
---
