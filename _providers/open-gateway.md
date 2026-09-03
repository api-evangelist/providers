---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Open Gateway Agentic Access
  operation_count: 70
  slug: open-gateway-agentic-access
  summary_line: 70 operations · 52 acting
api_count: 22
apis:
- baseURL_template: '{apiRoot}/kyc-age-verification/v0.2'
  baseurl_source: spec_template
  description: Operations to verify the age of a user.
  name: GSMA Open Gateway Age Verification API
  slug: open-gateway-age-verification-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Operations for ApiProduct Resource
  name: GSMA Open Gateway API Product API
  slug: open-gateway-apiproduct-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Operations for ApiProductOrder Resource
  name: GSMA Open Gateway API Product Order API
  slug: open-gateway-apiproductorder-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Operations for Application Resource
  name: GSMA Open Gateway Application API
  slug: open-gateway-application-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Operations for ApplicationOwner Resource
  name: GSMA Open Gateway Application Owner API
  slug: open-gateway-applicationowner-api
- baseURL_template: '{apiRoot}/call-forwarding-signal/v0.4'
  baseurl_source: spec_template
  description: Provides information on Call Forwarding settings for the provided phone number (PhoneNumber).
  name: GSMA Open Gateway Call Forwarding information retrieval API
  slug: open-gateway-call-forwarding-information-retrieval-api
- baseURL_template: '{apiRoot}/device-swap/v1'
  baseurl_source: spec_template
  description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: GSMA Open Gateway Check Device Swap API
  slug: open-gateway-check-device-swap-api
- baseURL_template: '{apiRoot}/sim-swap/v2'
  baseurl_source: spec_template
  description: The Check SIM swap API from GSMA Open Gateway — 1 operation(s) for check sim swap.
  name: GSMA Open Gateway Check SIM swap API
  slug: open-gateway-check-sim-swap-api
- baseURL_template: '{apiRoot}/kyc-tenure/v0.2'
  baseurl_source: spec_template
  description: Check details about the length of tenure of the subscriber
  name: GSMA Open Gateway Check Subscriber Tenure API
  slug: open-gateway-check-subscriber-tenure-api
- baseURL_template: '{apiRoot}/connected-network-type/v0.1'
  baseurl_source: spec_template
  description: Operations to get the network type device is connected to
  name: GSMA Open Gateway Connected Network Type API
  slug: open-gateway-connected-network-type-api
- baseURL_template: '{apiRoot}/device-reachability-status/v1'
  baseurl_source: spec_template
  description: Operations to get the current reachability status of a device
  name: GSMA Open Gateway Device reachability status API
  slug: open-gateway-device-reachability-status-api
- baseURL_template: '{apiRoot}/device-reachability-status-subscriptions/v0.8'
  baseurl_source: spec_template
  description: Operation to manage event subscription on device reachability status event.
  name: GSMA Open Gateway Device reachability status subscription API
  slug: open-gateway-device-reachability-status-subscription-api
- baseURL_template: '{apiRoot}/simple-edge-discovery/v2'
  baseurl_source: spec_template
  description: Find the closest Edge Cloud Zone to the user device.
  name: GSMA Open Gateway Discovery API
  slug: open-gateway-discovery-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Endpoints to register and terminate an Event Listener
  name: GSMA Open Gateway events subscription API
  slug: open-gateway-events-subscription-api
- baseURL_template: '{apiRoot}/device-identifier/v0.3'
  baseurl_source: spec_template
  description: Retrieve details about the device being used by a mobile subscriber
  name: GSMA Open Gateway Get Device Identifiers API
  slug: open-gateway-get-device-identifiers-api
- baseURL_template: '{apiRoot}/home-devices-qod/v0.4'
  baseurl_source: spec_template
  description: QoD control operations for home devices
  name: GSMA Open Gateway Home Devices QoD API
  slug: open-gateway-home-devices-qod-api
- baseURL_template: '{apiRoot}/location-retrieval/v0.5'
  baseurl_source: spec_template
  description: Retrieve the location of a device
  name: GSMA Open Gateway Location retrieval API
  slug: open-gateway-location-retrieval-api
- baseURL_template: '{apiRoot}/location-verification/v3'
  baseurl_source: spec_template
  description: Verification of the location of a device
  name: GSMA Open Gateway Location verification API
  slug: open-gateway-location-verification-api
- baseURL_template: '{apiRoot}/kyc-match/v0.4'
  baseurl_source: spec_template
  description: Operations to match a customer identity against the account data bound to their phone number.
  name: GSMA Open Gateway Match API
  slug: open-gateway-match-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Operations for Monitor Resource
  name: GSMA Open Gateway Monitor API
  slug: open-gateway-monitor-api
- baseURL_template: '{apiRoot}/openGatewayOperateAPIOnboardingAndOrdering/v5/'
  baseurl_source: spec_template
  description: Notifications for Resource Lifecycle and event notifications
  name: GSMA Open Gateway notification listener API
  slug: open-gateway-notification-listener-api
- baseURL_template: '{apiRoot}/carrier-billing/v0.5'
  baseurl_source: spec_template
  description: Operations to manage One Step Payment procedure
  name: GSMA Open Gateway One Step Payment API
  slug: open-gateway-one-step-payment-api
- baseURL_template: '{apiRoot}/one-time-password-sms/v1'
  baseurl_source: spec_template
  description: API operations to manage OTP codes
  name: GSMA Open Gateway OTP Management API
  slug: open-gateway-otp-management-api
- baseURL_template: '{apiRoot}/carrier-billing/v0.5'
  baseurl_source: spec_template
  description: Operations to obtain information about payments
  name: GSMA Open Gateway Payment API
  slug: open-gateway-payment-api
- baseURL_template: '{apiRoot}/number-verification/v2'
  baseurl_source: spec_template
  description: API operation to return the phone number associated to the access token.
  name: GSMA Open Gateway Phone number share API
  slug: open-gateway-phone-number-share-api
- baseURL_template: '{apiRoot}/number-verification/v2'
  baseurl_source: spec_template
  description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: GSMA Open Gateway Phone number verify API
  slug: open-gateway-phone-number-verify-api
- baseURL_template: '{apiRoot}/population-density-data/v0.3'
  baseurl_source: spec_template
  description: Operations to retrieve population density information.
  name: GSMA Open Gateway Population Density Data API
  slug: open-gateway-population-density-data-api
- baseURL_template: '{apiRoot}/qos-profiles/v1'
  baseurl_source: spec_template
  description: Manage QoS Profiles
  name: GSMA Open Gateway QoS Profiles API
  slug: open-gateway-qos-profiles-api
- baseURL_template: '{apiRoot}/quality-on-demand/v1'
  baseurl_source: spec_template
  description: Manage QoS sessions
  name: GSMA Open Gateway QoS Sessions API
  slug: open-gateway-qos-sessions-api
- baseURL_template: '{apiRoot}/device-swap/v1'
  baseurl_source: spec_template
  description: Receive the last date in which the device of the end-user was swapped
  name: GSMA Open Gateway Retrieve Device Swap Date API
  slug: open-gateway-retrieve-device-swap-date-api
- baseURL_template: '{apiRoot}/sim-swap/v2'
  baseurl_source: spec_template
  description: The Retrieve SIM swap date API from GSMA Open Gateway — 1 operation(s) for retrieve sim swap date.
  name: GSMA Open Gateway Retrieve SIM swap date API
  slug: open-gateway-retrieve-sim-swap-date-api
- baseURL_template: '{apiRoot}/device-roaming-status/v1'
  baseurl_source: spec_template
  description: Operation to get device roaming status and country information (if roaming) synchronously
  name: GSMA Open Gateway Roaming status retrieval API
  slug: open-gateway-roaming-status-retrieval-api
- baseURL_template: '{apiRoot}/carrier-billing/v0.5'
  baseurl_source: spec_template
  description: Operations to manage Two Step Payment procedure
  name: GSMA Open Gateway Two Step Payment API
  slug: open-gateway-two-step-payment-api
- baseURL_template: '{apiRoot}/call-forwarding-signal/v0.4'
  baseurl_source: spec_template
  description: Provides information on Unconditional Call Forwarding settings for the provided phone number (PhoneNumber)
  name: GSMA Open Gateway Unconditional Call Forwarding information retrieval API
  slug: open-gateway-unconditional-call-forwarding-information-retrieval-api
artifact_total: 62
asyncapis:
- description: ''
  name: Open Gateway Webhooks
  slug: open-gateway-webhooks
collections:
- collection_type: open
  name: Call Forwarding Signal
  slug: open-camara-call-forwarding-signal
- collection_type: open
  name: Carrier Billing
  slug: open-camara-carrier-billing
- collection_type: open
  name: Connected Network Type
  slug: open-camara-connected-network-type
- collection_type: open
  name: Device Identifier
  slug: open-camara-device-identifier
- collection_type: open
  name: Device Reachability Status
  slug: open-camara-device-reachability-status
- collection_type: open
  name: Device Roaming Status
  slug: open-camara-device-roaming-status
- collection_type: open
  name: Device Swap
  slug: open-camara-device-swap
- collection_type: open
  name: Home Devices QoD
  slug: open-camara-home-devices-qod
- collection_type: open
  name: Know Your Customer Age Verification
  slug: open-camara-kyc-age-verification
- collection_type: open
  name: Know Your Customer Match
  slug: open-camara-kyc-match
- collection_type: open
  name: KYC Tenure
  slug: open-camara-kyc-tenure
- collection_type: open
  name: Device Location Retrieval
  slug: open-camara-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-camara-location-verification
- collection_type: open
  name: Number Verification
  slug: open-camara-number-verification
- collection_type: open
  name: One Time Password SMS
  slug: open-camara-one-time-password-sms
- collection_type: open
  name: Population Density Data
  slug: open-camara-population-density-data
- collection_type: open
  name: QoS Profiles
  slug: open-camara-qos-profiles
- collection_type: open
  name: Quality-On-Demand
  slug: open-camara-quality-on-demand
- collection_type: open
  name: SIM Swap
  slug: open-camara-sim-swap
- collection_type: open
  name: Simple Edge Discovery
  slug: open-camara-simple-edge-discovery
- collection_type: open
  name: Open Gateway Operate API Onboarding and Ordering
  slug: open-tmforum-tmf931-open-gateway-onboarding-ordering
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/open-gateway-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-number-verification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-sim-swap-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-device-swap-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-call-forwarding-signal-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-kyc-match-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-kyc-age-verification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-kyc-tenure-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-one-time-password-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-quality-on-demand-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-qos-profiles-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-device-reachability-status-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-device-reachability-status-subscriptions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-device-identifier-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-device-roaming-status-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-connected-network-type-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-population-density-data-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-location-retrieval-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-location-verification-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-simple-edge-discovery-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-carrier-billing-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-camara-home-devices-qod-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/open-gateway-tmforum-tmf931-open-gateway-onboarding-ordering-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-gateway-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-gateway-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-gateway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-gateway-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gsma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: start
  title: ''
  type: Portal
  url: https://open-gateway.gsma.com/
- group: other
  title: ''
  type: APIDescriptions
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
- group: auth
  title: ''
  type: Certification
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/what-is-gsma-open-gateway-certification/
- group: docs
  title: ''
  type: Specification
  url: https://github.com/camaraproject
- group: docs
  title: ''
  type: Specification
  url: https://github.com/tmforum-apis/TMF931_OpenGatewayOnboardingAndOrderingComponentSuite
- group: auth
  title: ''
  type: Authentication
  url: https://github.com/camaraproject/IdentityAndConsentManagement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSMA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gsma
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.gsma.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.gsma.com/security/cvd-submit-a-vulnerability/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.gsma.com/aboutus/legal/privacy
- group: build
  title: ''
  type: Packages
  url: packages/open-gateway-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/open-gateway-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/open-gateway-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/open-gateway-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/open-gateway-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/open-gateway-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/open-gateway-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/open-gateway-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/open-gateway-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/camaraproject/ReleaseManagement/blob/main/documentation/API_Release_Guidelines.md
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/open-gateway-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/open-gateway-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/open-gateway-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://open-gateway.gsma.com/sandbox
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/open-gateway-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/camaraproject/ReleaseManagement/releases
- group: design
  title: ''
  type: DataModel
  url: data-model/open-gateway-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/open-gateway-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gsma.com/security/
- group: docs
  title: ''
  type: APIReference
  url: https://camaraproject.github.io/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/wp-content/uploads/2024/02/Channel-Partner-Onboarding-Guide-WA.101-v1.0.pdf
- group: company
  title: ''
  type: Blog
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/resources/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gsma.com/about-us/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsma.com/aboutus/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camaraproject
created: '2026-07-25'
description: 'GSMA Open Gateway is the mobile industry''s operator-commitment and certification layer for network APIs, run by the GSM Association from its London headquarters in the United Kingdom. Launched at MWC Barcelona on 27 February 2023 with 21 operator groups and eight universal network APIs, it is the go-to-market wrapper around CAMARA, the Linux Foundation-hosted Telco Global API Alliance that actually authors the OpenAPI definitions. GSMA sits above the value chain rather than in it: it signs operators and channel partners to a memorandum of understanding, certifies implementations against CAMARA service APIs and TM Forum Operate APIs, and publishes which certified APIs are live in which markets. Its API posture is honestly non-existent as a first-party surface. GSMA operates no callable API, publishes no OpenAPI under its own name, and runs no self-serve developer portal with keys or a sandbox. open-gateway.gsma.com is a filterable directory of certified deployments, and every
  automated probe of it and of gsma.com returned an HTTP 403 Cloudflare bot challenge. The specifications are open on GitHub under camaraproject and tmforum-apis; the endpoints belong to operators; and developers reach them through aggregators and channel partners such as Aduna, Vonage, Infobip, Sinch, Twilio, Nokia, AWS and Bridge Alliance rather than through the GSMA. Per the GSMA''s own Q1 2026 Open Gateway update, 81 operator groups and 61 channel partners covering 292 networks and about 80 percent of global mobile connections have signed, with 237 certified API assets drawn from 33 CAMARA tagged released APIs and 280 API instances commercially launched across 85 networks in 50 markets.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: GSMA Open Gateway MCP Server
  slug: gsma-open-gateway-mcp-server
modified: '2026-07-25'
name: GSMA Open Gateway
nav: Providers
network: true
overview: 'GSMA Open Gateway publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Age Verification API, API Product API, API Product Order API, and 31 more. Tagged areas include Telecommunications, United Kingdom, Network APIs, CAMARA, and Open Gateway.


  The GSMA Open Gateway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GSMA Open Gateway''s developer surface includes authentication, documentation, developer portal, privacy policy, sandbox, changelog, API reference, and 59 more developer resources.'
random_paper: 15
scopes:
- name: Open Gateway Scopes
  scope_count: 38
  slug: open-gateway-scopes
  summary_line: 38 scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 59.4
    developer_ergonomics: 61.3
    discoverability: 77.8
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 69.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-gateway/refs/heads/main/screenshots/open-gateway-2026-08-07T190457.png
security:
- kind: authentication
  name: Open Gateway Authentication
  slug: open-gateway-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Open Gateway Domain Security
  slug: open-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Open Gateway Vulnerability Disclosure
  slug: open-gateway-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: open-gateway
tags:
- Telecommunications
- United Kingdom
- Network APIs
- CAMARA
- Open Gateway
- Standards
- Mobile Network Operator
- Identity Verification
- SIM Swap
- Quality on Demand
- 5G
- Certification
- Trade Association
- TM Forum
website: https://www.gsma.com/
---
