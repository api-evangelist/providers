---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 52
  human_in_the_loop: 0
  name: Open Gateway Agentic Access
  operation_count: 70
  slug: open-gateway-agentic-access
  summary_line: 70 operations · 52 acting
api_count: 22
apis:
- description: CAMARA Number Verification 2.1.0 as certified under GSMA Open Gateway. Verifies that the phone number claimed by a user matches the number of the SIM on the network connection, or returns the network-
  name: CAMARA Number Verification API
  slug: camara-number-verification
- description: CAMARA SIM Swap 2.1.0 as certified under GSMA Open Gateway. Checks whether the SIM associated with a mobile phone number has been swapped within a given period, and retrieves the last SIM change date,
  name: CAMARA SIM Swap API
  slug: camara-sim-swap
- description: CAMARA Device Swap 1.0.0 as certified under GSMA Open Gateway. Reports whether the device attached to a mobile subscription has changed within a supplied period and retrieves the last device change da
  name: CAMARA Device Swap API
  slug: camara-device-swap
- description: CAMARA Call Forwarding Signal 0.4.0 as certified under GSMA Open Gateway. Exposes whether unconditional or conditional call forwarding is active on a subscriber line, a signal used to detect social-en
  name: CAMARA Call Forwarding Signal API
  slug: camara-call-forwarding-signal
- description: CAMARA Know Your Customer Match 0.4.0 as certified under GSMA Open Gateway. Compares customer-supplied identity attributes (name, address, birthdate, identity document, email) against the data the mob
  name: CAMARA Know Your Customer Match API
  slug: camara-kyc-match
- description: CAMARA Know Your Customer Age Verification 0.2.1 as certified under GSMA Open Gateway. Answers whether the subscriber behind a phone number is over a given age threshold using operator-held identity d
  name: CAMARA Know Your Customer Age Verification API
  slug: camara-kyc-age-verification
- description: CAMARA KYC Tenure 0.2.0 as certified under GSMA Open Gateway. Confirms whether a mobile subscription has been active with the operator for at least a requested duration, a low-friction trust signal fo
  name: CAMARA KYC Tenure API
  slug: camara-kyc-tenure
- description: 'CAMARA One Time Password SMS 1.1.1 as certified under GSMA Open Gateway. Sends a one-time password by SMS to a subscriber''s phone number and validates the code the user returns, delivered through the '
  name: CAMARA One Time Password SMS API
  slug: camara-one-time-password-sms
- description: CAMARA Quality-On-Demand 1.1.0 as certified under GSMA Open Gateway. Creates, reads, extends and deletes temporary sessions that raise the network quality of service for a specific device and applicat
  name: CAMARA Quality on Demand API
  slug: camara-quality-on-demand
- description: CAMARA QoS Profiles 1.1.0 as certified under GSMA Open Gateway. Lists the quality-of-service profiles an operator makes available and retrieves a single profile by name, so a developer can discover wh
  name: CAMARA QoS Profiles API
  slug: camara-qos-profiles
- description: CAMARA Device Reachability Status 1.1.0 as certified under GSMA Open Gateway. Returns whether a device is currently reachable on the network and by which means (SMS, data), the core device-state signa
  name: CAMARA Device Reachability Status API
  slug: camara-device-reachability-status
- description: CAMARA Device Reachability Status Subscriptions 0.8.0 as certified under GSMA Open Gateway. Creates and manages event subscriptions that push CloudEvents notifications to a consumer sink when a device
  name: CAMARA Device Reachability Status Subscriptions API
  slug: camara-device-reachability-status-subscriptions
- description: 'CAMARA Device Identifier 0.3.0 as certified under GSMA Open Gateway. Retrieves the identifier, type and pseudonymous identifier of the device a subscription is currently using, and matches a supplied '
  name: CAMARA Device Identifier API
  slug: camara-device-identifier
- description: CAMARA Device Roaming Status 1.0.0 as certified under GSMA Open Gateway. Reports whether a device is roaming and, where available, the country it is roaming in, used for travel-aware fraud rules and I
  name: CAMARA Device Roaming Status API
  slug: camara-device-roaming-status
- description: CAMARA Connected Network Type 0.1.0 as certified under GSMA Open Gateway. Returns the access technology a device is currently attached to (for example 4G or 5G standalone), letting an application adap
  name: CAMARA Connected Network Type API
  slug: camara-connected-network-type
- description: CAMARA Population Density Data 0.3.0 as certified under GSMA Open Gateway. Returns aggregated, anonymised estimates of how many devices are present in a requested geographic area over a time window, f
  name: CAMARA Population Density Data API
  slug: camara-population-density-data
- description: CAMARA Device Location Retrieval 0.5.0 as certified under GSMA Open Gateway. Returns the network-derived location of a device as a circle or polygon with an accuracy indication, without relying on han
  name: CAMARA Device Location Retrieval API
  slug: camara-location-retrieval
- description: CAMARA Device Location Verification 3.0.0 as certified under GSMA Open Gateway. Verifies whether a device is inside, outside or partly within a supplied area rather than returning coordinates, a priva
  name: CAMARA Device Location Verification API
  slug: camara-location-verification
- description: CAMARA Simple Edge Discovery 2.0.1 as certified under GSMA Open Gateway. Returns the closest MEC (multi-access edge computing) platform to a given device so that an application can route traffic to th
  name: CAMARA Simple Edge Discovery API
  slug: camara-simple-edge-discovery
- description: 'CAMARA Carrier Billing 0.5.0 as certified under GSMA Open Gateway. Creates and manages direct carrier-billing payments charged to a subscriber''s mobile account, including payment status, confirmation '
  name: CAMARA Carrier Billing API
  slug: camara-carrier-billing
- description: CAMARA Home Devices QoD 0.4.0 as certified under GSMA Open Gateway. Requests prioritised quality of service for a device on a fixed broadband home network, extending Quality on Demand beyond mobile to
  name: CAMARA Home Devices QoD API
  slug: camara-home-devices-qod
- description: 'TM Forum TMF931 Open Gateway Operate API - Onboarding and Ordering 5.2.1, the GSMA-defined ''Operate API'' that channel partners and aggregators use to onboard against an operator: browse the API produc'
  name: TM Forum TMF931 Open Gateway Onboarding and Ordering API
  slug: tmf931-onboarding-ordering
artifact_total: 29
asyncapis:
- description: ''
  name: Open Gateway Webhooks
  slug: open-gateway-webhooks
common:
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
  name: open-gateway-mcp.yml
  slug: open-gateway-mcpyml
modified: '2026-07-25'
name: GSMA Open Gateway
nav: Providers
network: true
overview: 'GSMA Open Gateway publishes 22 APIs on the [APIs.io](https://apis.io/) network, including CAMARA Number Verification API, CAMARA SIM Swap API, CAMARA Device Swap API, and 19 more. Tagged areas include Telecommunications, United Kingdom, Network APIs, CAMARA, and Open Gateway.


  The GSMA Open Gateway catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GSMA Open Gateway''s developer surface includes authentication, documentation, developer portal, privacy policy, sandbox, changelog, API reference, and 36 more developer resources.'
random_paper: 103
scopes:
- name: Open Gateway Scopes
  scope_count: 38
  slug: open-gateway-scopes
  summary_line: 38 scopes
score:
  band: developing
  composite: 53.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 68.1
    developer_ergonomics: 64.7
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
