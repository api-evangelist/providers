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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 142
  human_in_the_loop: 1
  name: Losant Agentic Access
  operation_count: 237
  slug: losant-agentic-access
  summary_line: 237 operations · 142 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Authentication and Account resources on the Losant Platform.
  name: Losant Authentication and Account API
  slug: losant-authentication-and-account-api
- description: Data and Data Tables resources on the Losant Platform.
  name: Losant Data and Data Tables API
  slug: losant-data-and-data-tables-api
- description: Edge and Embedded Compute resources on the Losant Platform.
  name: Losant Edge and Embedded Compute API
  slug: losant-edge-and-embedded-compute-api
- description: Enterprise Instance resources on the Losant Platform.
  name: Losant Enterprise Instance API
  slug: losant-enterprise-instance-api
- description: Notebooks resources on the Losant Platform.
  name: Losant Notebooks API
  slug: losant-notebooks-api
- description: Workflow Engine resources on the Losant Platform.
  name: Losant Workflow Engine API
  slug: losant-workflow-engine-api
artifact_total: 69
asyncapis:
- description: ''
  name: Losant Event Surface
  slug: losant-event-surface
collections:
- collection_type: postman
  name: Losant Application API
  slug: postman-losant-application-api
- collection_type: postman
  name: Losant Application Authentication and Account API
  slug: postman-losant-authentication-and-account-api
- collection_type: postman
  name: Losant Application Data and Data Tables API
  slug: postman-losant-data-and-data-tables-api
- collection_type: postman
  name: Losant Application Device API
  slug: postman-losant-device-api
- collection_type: postman
  name: Losant Application Edge and Embedded Compute API
  slug: postman-losant-edge-and-embedded-compute-api
- collection_type: postman
  name: Losant Application Enterprise Instance API
  slug: postman-losant-enterprise-instance-api
- collection_type: postman
  name: Losant Application Experience API
  slug: postman-losant-experience-api
- collection_type: postman
  name: Losant Application Notebooks API
  slug: postman-losant-notebooks-api
- collection_type: postman
  name: Losant Application Workflow Engine API
  slug: postman-losant-workflow-engine-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Losant Application API
  slug: open-losant-application-api
- collection_type: open
  name: Losant Authentication and Account API
  slug: open-losant-auth-api
- collection_type: open
  name: Losant Application Authentication and Account API
  slug: open-losant-authentication-and-account-api
- collection_type: open
  name: Losant Application Data and Data Tables API
  slug: open-losant-data-and-data-tables-api
- collection_type: open
  name: Losant Data and Data Tables API
  slug: open-losant-data-api
- collection_type: open
  name: Losant Application Device API
  slug: open-losant-device-api
- collection_type: open
  name: Losant Application Edge and Embedded Compute API
  slug: open-losant-edge-and-embedded-compute-api
- collection_type: open
  name: Losant Edge and Embedded Compute API
  slug: open-losant-edge-api
- collection_type: open
  name: Losant Application Enterprise Instance API
  slug: open-losant-enterprise-instance-api
- collection_type: open
  name: Losant Application Experience API
  slug: open-losant-experience-api
- collection_type: open
  name: Losant Enterprise Instance API
  slug: open-losant-instance-api
- collection_type: open
  name: Losant Notebooks API
  slug: open-losant-notebook-api
- collection_type: open
  name: Losant Application Notebooks API
  slug: open-losant-notebooks-api
- collection_type: open
  name: Losant Workflow Engine API
  slug: open-losant-workflow-api
- collection_type: open
  name: Losant Application Workflow Engine API
  slug: open-losant-workflow-engine-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/losant/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/losant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/losant-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/losant-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.losant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.losant.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.losant.com/getting-started/walkthrough/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.losant.com/rest-api/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.losant.com/mqtt/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.losant.com/cli/overview/
- group: other
  title: ''
  type: Education
  url: https://docs.losant.com/university/overview/
- group: other
  title: ''
  type: Templates
  url: https://docs.losant.com/template-library/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.losant.com/workflow-lab/overview/
- group: docs
  title: ''
  type: Guides
  url: https://docs.losant.com/guides/overview/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Losant
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-rest-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-rest-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-rest-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-mqtt-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-mqtt-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-mqtt-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-mqtt-arduino
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Losant/losant-esp-idf-esp32
- group: build
  title: ''
  type: CLI
  url: https://github.com/Losant/losant-cli
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Losant/eea-examples
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Losant/notebook-examples
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Losant/application-templates
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Losant/workflow-node-catalog
- group: company
  title: ''
  type: Blog
  url: https://www.losant.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.losant.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.losant.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.losant.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/losant/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/losantiot
- group: commercial
  title: ''
  type: Plans
  url: plans/losant-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/losant-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/losant-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/losant-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/losant-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/losant-context.jsonld
- group: build
  title: ''
  type: Packages
  url: packages/losant-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/losant-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/losant-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.losant.com/mcp
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/losant-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/losant-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/losant-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.losant.com/references/security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/losant-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/losant-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.losant.com/edge-compute/gateway-edge-agent/changelog/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/losant-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/losant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Losant/losant-mcp-server/blob/main/SECURITY.md
- group: start
  title: ''
  type: Sandbox
  url: sandbox/losant-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/losant-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/losant-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/losant-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/losant-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/losant-event-surface.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-application-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-authentication-and-account-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-data-and-data-tables-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-device-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-edge-and-embedded-compute-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-enterprise-instance-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-experience-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-notebooks-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/losant-workflow-engine-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.losant.com/rest-api/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Losant
- group: start
  title: ''
  type: SignUp
  url: https://accounts.losant.com/create-account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.losant.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.losant.com/legal/privacy-policy
- group: operate
  title: ''
  type: Community
  url: https://forums.losant.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.losant.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.suse.com/news/suse-acquires-losant
created: '2026-05-25'
description: Losant is an Enterprise IoT Platform that lets product teams build connected experiences, manage fleets of devices, orchestrate edge and embedded compute, and visualize and act on IoT data. The platform exposes a comprehensive REST API (the Platform API) covering applications, devices, data tables, time-series data, events, workflows (visual workflow engine), edge and embedded deployments, end-user experiences, notebooks, files, integrations, webhooks, dashboards, organizations, audit logs, and self-hosted enterprise instance administration. Devices may also connect via MQTT. Customers include industrial, smart-building, agriculture, and connected-product companies; Losant emphasizes white-labeled end-user experiences ("Experiences") and edge compute on Linux gateways plus microcontrollers via the Embedded Edge Agent (EEA). Losant also ships a hosted, OAuth 2.0-protected Model Context Protocol (MCP) server at https://mcp.losant.com/mcp so AI assistants can query and write application
  configuration and telemetry. Losant was acquired by SUSE, which is folding the platform into an open process automation offering for Industrial IoT.
examples:
- key_count: 4
  name: Losant Application Api Create Application Example
  slug: losant-application-api-create-application-example
- key_count: 4
  name: Losant Application Api Get Application Example
  slug: losant-application-api-get-application-example
- key_count: 4
  name: Losant Auth Api Authenticate Device Example
  slug: losant-auth-api-authenticate-device-example
- key_count: 4
  name: Losant Auth Api Authenticate User Example
  slug: losant-auth-api-authenticate-user-example
- key_count: 4
  name: Losant Data Api Last Value Query Example
  slug: losant-data-api-last-value-query-example
- key_count: 4
  name: Losant Data Api Time Series Query Example
  slug: losant-data-api-time-series-query-example
- key_count: 4
  name: Losant Device Api Send Command Example
  slug: losant-device-api-send-command-example
- key_count: 4
  name: Losant Device Api Send State Example
  slug: losant-device-api-send-state-example
- key_count: 4
  name: Losant Edge Api Release Edge Deployment Example
  slug: losant-edge-api-release-edge-deployment-example
- key_count: 4
  name: Losant Experience Api Create Experience User Example
  slug: losant-experience-api-create-experience-user-example
- key_count: 4
  name: Losant Notebook Api Execute Notebook Example
  slug: losant-notebook-api-execute-notebook-example
- key_count: 4
  name: Losant Workflow Api Create Flow Example
  slug: losant-workflow-api-create-flow-example
finops:
- name: Losant Finops
  service_category: ''
  slug: losant-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/losant.png
json_schemas:
- name: Losant Application
  property_count: 19
  slug: losant-application
- name: Losant DataTable
  property_count: 8
  slug: losant-data-table
- name: Losant Device
  property_count: 18
  slug: losant-device
- name: Losant EdgeDeployment
  property_count: 17
  slug: losant-edge-deployment
- name: Losant Event
  property_count: 18
  slug: losant-event
- name: Losant ExperienceUser
  property_count: 14
  slug: losant-experience-user
- name: Losant Flow
  property_count: 27
  slug: losant-flow
- name: Losant Notebook
  property_count: 13
  slug: losant-notebook
json_structures:
- name: Losant Application Structure
  property_count: 19
  slug: losant-application-structure
- name: Losant Data Structure
  property_count: 0
  slug: losant-data-structure
- name: Losant Device Structure
  property_count: 18
  slug: losant-device-structure
- name: Losant Flow Structure
  property_count: 27
  slug: losant-flow-structure
jsonld:
- class_count: 20
  name: Losant Context
  property_count: 7
  slug: losant-context
layout: provider
mcp_servers:
- description: ''
  name: Losant MCP Server
  slug: losant-mcp-server
- description: ''
  name: Losant hosted MCP endpoint
  slug: losant-hosted-mcp-endpoint
modified: '2026-08-26'
name: Losant
nav: Providers
network: true
overview: 'Losant publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication and Account API, Data and Data Tables API, Edge and Embedded Compute API, and 3 more. Tagged areas include IoT, Internet Of Things, Devices, Edge Compute, and Embedded.


  The Losant catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Losant''s developer surface includes authentication, developer portal, documentation, getting-started guide, CLI, engineering blog, pricing, and 71 more developer resources.'
plans:
- name: Losant Plans Pricing
  plan_count: 4
  slug: losant-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 17
  name: Losant Rate Limits
  slug: losant-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Losant API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: losant-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Losant API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: losant-rules
scopes:
- name: Losant Scopes
  scope_count: 7
  slug: losant-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 81.2
  coverage:
    artifact_dirs: 33
    catalog_gap: 24.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 47.0
    contract_quality: 74.0
    developer_ergonomics: 94.6
    discoverability: 74.1
    governance: 47.0
    operational_transparency: 94.7
  previous_composite: 81.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/losant/refs/heads/main/screenshots/losant-2026-06-20T184729.png
security:
- kind: authentication
  name: Losant Authentication
  slug: losant-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Losant Domain Security
  slug: losant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Losant Vulnerability Disclosure
  slug: losant-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: losant
tags:
- IoT
- Internet Of Things
- Devices
- Edge Compute
- Embedded
- MQTT
- Industrial IoT
- Telemetry
- Workflow-Automation
- Visual Workflow Engine
- Dashboards
- Time Series
- Connected Products
- Enterprise
website: https://www.losant.com/
---
