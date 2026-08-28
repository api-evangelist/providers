---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Verizon Agentic Access
  operation_count: 8
  slug: verizon-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 18
apis:
- description: Software Management Services API lets customers manage, schedule and distribute software updates to eligible 4G and 5G Internet of Things devices.
  name: Verizon 5G Edge
  slug: verizon-5g-edge
- description: Available exclusively for IP Contact Center (IPCC) customers, our Communications Platform as a Service (CPaaS) offering provides a set of APIs that you can leverage to build customized solutions for i
  name: Verizon Communications Platform as a Service (CPaaS)
  slug: communications-platform-as-a-service
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Inventory Management
  slug: verizon-inventory-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Incident Management
  slug: verizon-incident-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Change Management
  slug: verizon-change-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Event Management
  slug: verizon-event-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Problem Management
  slug: verizon-problem-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Order Management
  slug: verizon-order-management
- description: Verizon provides customers a suite of TM Forum certified service management APIs and associated documentation that expose Verizons ITIL (Information Technology Infrastructure Library) functions. These
  name: Verizon Billing Management
  slug: verizon-billing-management
- description: These innovative network provisioning API solutions can be deployed in the enterprises network eco-system to drive real-time network adjustments according to their changing business needs. Taking an a
  name: Verizon Dynamic Bandwidth APIs
  slug: verizon-dynamic-bandwidth-apis
- description: MEF-standardized Dynamic Network Manager APIs. Verizon documents the same API surface under four product families — Private IP, Internet Dedicated, E-Line and E-LAN — which is why this appeared four t
  name: Dynamic Network Manager (DNM) Standardized APIs
  slug: dynamic-network-manager-dnm-standardized-apis
- description: SCI supports APIs to fetch data consumption and bandwidth utilization measurements for the SCI connection to the cloud.
  name: Secure Cloud Interconnect APIs Utilization
  slug: secure-cloud-interconnect-apis-utilization
- description: SCI supports APIs to fetch data consumption and bandwidth utilization measurements for the SCI connection to the cloud.
  name: Secure Cloud Interconnect APIs Billing Usage
  slug: secure-cloud-interconnect-apis-billing-usage
- description: Account information and management
  name: Verizon Accounts API
  slug: verizon-accounts-api
- description: Callback subscription management
  name: Verizon Callbacks API
  slug: verizon-callbacks-api
- description: Device activation, deactivation, and management
  name: Verizon Devices API
  slug: verizon-devices-api
- description: Session management and authentication
  name: Verizon Session API
  slug: verizon-session-api
- description: SMS messaging to devices
  name: Verizon SMS API
  slug: verizon-sms-api
artifact_total: 98
asyncapis:
- description: ''
  name: Verizon Thingspace Callbacks Webhooks
  slug: verizon-thingspace-callbacks-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Verizon ThingSpace Connectivity Management Accounts API
  slug: open-verizon-accounts-api
- collection_type: open
  name: Verizon ThingSpace Connectivity Management Accounts Callbacks API
  slug: open-verizon-callbacks-api
- collection_type: open
  name: Verizon ThingSpace Connectivity Management Accounts Devices API
  slug: open-verizon-devices-api
- collection_type: open
  name: Verizon ThingSpace Connectivity Management Accounts Session API
  slug: open-verizon-session-api
- collection_type: open
  name: Verizon ThingSpace Connectivity Management Accounts SMS API
  slug: open-verizon-sms-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verizon-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/verizon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verizon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verizon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/verizon-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verizon
- group: company
  title: ''
  type: Website
  url: https://www.verizon.com
- group: agent
  title: ''
  type: LlmsText
  url: https://www.verizon.com/llms.txt
- group: start
  title: ''
  type: Portal
  url: https://developers.verizon.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.verizon.com/#/apis/ns/documentation/help
- group: operate
  title: ''
  type: FAQ
  url: https://developers.verizon.com/#/apis/ns/documentation/frequently-asked-questions
- group: start
  title: ''
  type: Login
  url: https://secure.verizon.com/signin?goto=https://developers.verizon.com/apis/sec/v1/login
- group: start
  title: ''
  type: Signup
  url: https://secure.verizon.com/account/register/start?goto=https%3A%2F%2Fdevelopers.verizon.com%2Fapis%2Fsec%2Fv1%2Flogin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.verizon.com/about/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.verizon.com/about/terms-conditions/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/rules/verizon-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/vocabulary/verizon-vocabulary.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verizon-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/verizon-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/verizon-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verizon-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/verizon-etx-protobuf.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verizon-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verizon-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verizon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verizon-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.verizon.com/support/service-outage-status/
- group: design
  title: ''
  type: Conventions
  url: conventions/verizon-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/verizon-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/verizon-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verizon-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/verizon-thingspace-callbacks-webhooks.yml
- group: auth
  title: ''
  type: Security
  url: https://www.verizon.com/solutions-and-services/report-security-vulnerability/
- group: other
  title: ''
  type: Overlay
  url: overlays/verizon-accounts-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/verizon-callbacks-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/verizon-devices-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/verizon-session-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/verizon-sms-api-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://thingspace.verizon.com/documentation/api-documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://thingspace.verizon.com/documentation/apis/connectivity-management/api-reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://thingspace.verizon.com/documentation/apis/connectivity-management/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Verizon
created: '2024-11-19'
description: Verizon is a leading telecommunications company providing wireless, wireline, broadband, and global enterprise services. Verizon offers developer APIs for IoT device management via ThingSpace, 5G edge computing, TM Forum service management, dynamic network bandwidth, and communications platform APIs for contact center and SMS solutions.
examples:
- key_count: 7
  name: Thingspace Connectivity Account Information Example
  slug: thingspace-connectivity-account-information-example
- key_count: 1
  name: Thingspace Connectivity Activate Devices Request Example
  slug: thingspace-connectivity-activate-devices-request-example
- key_count: 2
  name: Thingspace Connectivity Callback Summary Example
  slug: thingspace-connectivity-callback-summary-example
- key_count: 2
  name: Thingspace Connectivity Carrier Information Example
  slug: thingspace-connectivity-carrier-information-example
- key_count: 3
  name: Thingspace Connectivity Deactivate Devices Request Example
  slug: thingspace-connectivity-deactivate-devices-request-example
- key_count: 2
  name: Thingspace Connectivity Device Id Example
  slug: thingspace-connectivity-device-id-example
- key_count: 5
  name: Thingspace Connectivity Device Information Example
  slug: thingspace-connectivity-device-information-example
- key_count: 2
  name: Thingspace Connectivity Device List Request Example
  slug: thingspace-connectivity-device-list-request-example
- key_count: 3
  name: Thingspace Connectivity Device List Response Example
  slug: thingspace-connectivity-device-list-response-example
- key_count: 2
  name: Thingspace Connectivity Device Request Response Example
  slug: thingspace-connectivity-device-request-response-example
- key_count: 2
  name: Thingspace Connectivity Feature Example
  slug: thingspace-connectivity-feature-example
- key_count: 3
  name: Thingspace Connectivity Ip Pool Example
  slug: thingspace-connectivity-ip-pool-example
- key_count: 4
  name: Thingspace Connectivity Register Callback Request Example
  slug: thingspace-connectivity-register-callback-request-example
- key_count: 3
  name: Thingspace Connectivity Send Sms Request Example
  slug: thingspace-connectivity-send-sms-request-example
- key_count: 2
  name: Thingspace Connectivity Session Login Request Example
  slug: thingspace-connectivity-session-login-request-example
- key_count: 2
  name: Thingspace Connectivity Session Login Response Example
  slug: thingspace-connectivity-session-login-response-example
features:
- 'Verizon: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Verizon Network APIs (5G, location, identity) sold via the Verizon Open Innovation API portal with custom enterprise contracts.
finops:
- name: Verizon Finops
  service_category: Telecommunications
  slug: verizon-finops
graphqls:
- description: This conceptual GraphQL schema models Verizon's telecom, network, and connectivity services as exposed through the ThingSpace IoT platform, 5G Edge computing infrastructure, TM Forum service managemen
  name: Verizon GraphQL Schema
  slug: verizon-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verizon.png
integrations:
- description: Deploy 5G Edge applications on Verizon MEC nodes through AWS Wavelength partnership.
  name: AWS Wavelength
- description: Build edge-native applications through Verizon and Google Cloud edge computing integration.
  name: Google Cloud MEC
- description: Connect TM Forum service management APIs to ServiceNow and other ITSM platforms.
  name: ITSM Platforms
- description: Integrate ThingSpace device management with enterprise IoT platforms and data lakes.
  name: IoT Platforms
json_schemas:
- name: AccountInformation
  property_count: 7
  slug: thingspace-connectivity-account-information
- name: ActivateDevicesRequest
  property_count: 1
  slug: thingspace-connectivity-activate-devices-request
- name: CallbackSummary
  property_count: 2
  slug: thingspace-connectivity-callback-summary
- name: CarrierInformation
  property_count: 2
  slug: thingspace-connectivity-carrier-information
- name: DeactivateDevicesRequest
  property_count: 3
  slug: thingspace-connectivity-deactivate-devices-request
- name: DeviceId
  property_count: 2
  slug: thingspace-connectivity-device-id
- name: DeviceInformation
  property_count: 5
  slug: thingspace-connectivity-device-information
- name: DeviceListRequest
  property_count: 2
  slug: thingspace-connectivity-device-list-request
- name: DeviceListResponse
  property_count: 3
  slug: thingspace-connectivity-device-list-response
- name: DeviceRequestResponse
  property_count: 2
  slug: thingspace-connectivity-device-request-response
- name: Feature
  property_count: 2
  slug: thingspace-connectivity-feature
- name: IpPool
  property_count: 3
  slug: thingspace-connectivity-ip-pool
- name: RegisterCallbackRequest
  property_count: 4
  slug: thingspace-connectivity-register-callback-request
- name: SendSmsRequest
  property_count: 3
  slug: thingspace-connectivity-send-sms-request
- name: SessionLoginRequest
  property_count: 2
  slug: thingspace-connectivity-session-login-request
- name: SessionLoginResponse
  property_count: 2
  slug: thingspace-connectivity-session-login-response
json_structures:
- name: Thingspace Connectivity Account Information Structure
  property_count: 7
  slug: thingspace-connectivity-account-information-structure
- name: Thingspace Connectivity Activate Devices Request Structure
  property_count: 1
  slug: thingspace-connectivity-activate-devices-request-structure
- name: Thingspace Connectivity Callback Summary Structure
  property_count: 2
  slug: thingspace-connectivity-callback-summary-structure
- name: Thingspace Connectivity Carrier Information Structure
  property_count: 2
  slug: thingspace-connectivity-carrier-information-structure
- name: Thingspace Connectivity Deactivate Devices Request Structure
  property_count: 3
  slug: thingspace-connectivity-deactivate-devices-request-structure
- name: Thingspace Connectivity Device Id Structure
  property_count: 2
  slug: thingspace-connectivity-device-id-structure
- name: Thingspace Connectivity Device Information Structure
  property_count: 5
  slug: thingspace-connectivity-device-information-structure
- name: Thingspace Connectivity Device List Request Structure
  property_count: 2
  slug: thingspace-connectivity-device-list-request-structure
- name: Thingspace Connectivity Device List Response Structure
  property_count: 3
  slug: thingspace-connectivity-device-list-response-structure
- name: Thingspace Connectivity Device Request Response Structure
  property_count: 2
  slug: thingspace-connectivity-device-request-response-structure
- name: Thingspace Connectivity Feature Structure
  property_count: 2
  slug: thingspace-connectivity-feature-structure
- name: Thingspace Connectivity Ip Pool Structure
  property_count: 3
  slug: thingspace-connectivity-ip-pool-structure
- name: Thingspace Connectivity Register Callback Request Structure
  property_count: 4
  slug: thingspace-connectivity-register-callback-request-structure
- name: Thingspace Connectivity Send Sms Request Structure
  property_count: 3
  slug: thingspace-connectivity-send-sms-request-structure
- name: Thingspace Connectivity Session Login Request Structure
  property_count: 2
  slug: thingspace-connectivity-session-login-request-structure
- name: Thingspace Connectivity Session Login Response Structure
  property_count: 2
  slug: thingspace-connectivity-session-login-response-structure
jsonld:
- class_count: 16
  name: Verizon Thingspace Connectivity Context
  property_count: 43
  slug: verizon-thingspace-connectivity-context
layout: provider
mcp_servers:
- description: 'CANDIDATE, NOT A VERIZON PRODUCT. Verizon publishes no Model Context Protocol server. This is an API Evangelist-derived tool proposal: one tool per real ThingSpace Connectivity Management operationId,'
  name: ThingSpace MCP tool candidate (API Evangelist derived — Verizon operates no MCP server)
  slug: thingspace-mcp-tool-candidate-api-evangelist-derived-verizon-operates-no-mcp-server
modified: '2026-08-04'
name: Verizon
nav: Providers
network: true
overview: 'Verizon publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Callbacks API, Devices API, and 2 more. Tagged areas include Wireless, Telecommunications, IoT, 5G, and Enterprise.


  The Verizon catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Verizon''s developer surface includes authentication, developer portal, support, FAQ, signup flow, changelog, sandbox, and 36 more developer resources.'
plans:
- name: Verizon Plans Pricing
  plan_count: 1
  slug: verizon-plans-pricing
press:
- date: '2026-05-25'
  title: Verizon Business and AWS accelerate AI applications at ...
  url: https://www.verizon.com/about/news/verizon-business-and-aws-new-fiber-deal
- date: '2026-05-25'
  title: Verizon infuses AI in network, accelerates Open RAN ...
  url: https://www.samsung.com/global/business/networks/insights/press-release/0224-verizon-infuses-ai-in-network-accelerates-open-ran-innovation-with-multi-vendor-ran-intelligent-controller-deployment/
- date: '2026-05-25'
  title: Responsible Artificial Intelligence | About Verizon
  url: https://www.verizon.com/about/investors/responsible-ai-program
- date: '2026-05-25'
  title: 'Verizon AI Connect: AI Network Infrastructure and ...'
  url: https://www.verizon.com/business/solutions/ai-connect/
- date: '2026-05-25'
  title: Verizon unveils AI strategy to power next-gen AI demands
  url: https://www.verizon.com/about/news/verizon-unveils-ai-strategy-power-next-gen-ai-demands
random_paper: 4
rate_limits:
- limit_count: 1
  name: Verizon Rate Limits
  slug: verizon-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Verizon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: verizon-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: Verizon API Rules
  rule_count: 33
  severity_counts:
    error: 17
    hint: 0
    info: 3
    warn: 13
  slug: verizon-spectral-rules
scopes:
- name: Verizon Scopes
  scope_count: 3
  slug: verizon-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 64.7
  delta: 1.9
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 45.5
    contract_quality: 44.4
    developer_ergonomics: 80.4
    discoverability: 68.5
    governance: 45.5
    operational_transparency: 60.5
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 81.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verizon/refs/heads/main/screenshots/verizon-2026-06-20T200943.png
security:
- kind: authentication
  name: Verizon Authentication
  slug: verizon-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Verizon Domain Security
  slug: verizon-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Verizon Vulnerability Disclosure
  slug: verizon-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: verizon
tags:
- Wireless
- Telecommunications
- IoT
- 5G
- Enterprise
- Network APIs
- Fortune 100
use_cases:
- description: Manage large-scale IoT device fleets with activation, deactivation, and status monitoring.
  name: IoT Fleet Management
- description: Remotely diagnose, configure, and update IoT devices over Verizon's wireless network.
  name: Remote Device Management
- description: Automate network bandwidth provisioning and IT service management with TM Forum APIs.
  name: Enterprise Network Automation
- description: Build ultra-low-latency applications on Verizon's 5G edge computing infrastructure.
  name: 5G Edge Applications
- description: Build customized IVR and call routing solutions with Verizon's CPaaS Voice API.
  name: Contact Center Modernization
website: https://www.verizon.com
---
