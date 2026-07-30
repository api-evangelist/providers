---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 58
  human_in_the_loop: 0
  name: Gsma Agentic Access
  operation_count: 107
  slug: gsma-agentic-access
  summary_line: 107 operations · 58 acting
api_count: 18
apis:
- description: 'The GSMA Mobile Money API is a harmonised REST/JSON specification for mobile money platforms, developed by the GSMA with the mobile money industry and published openly at developer.mobilemoneyapi.io. '
  name: GSMA Mobile Money API
  slug: gsma-mobile-money-api
- description: CAMARA Call Forwarding Signal API as published on the GSMA Open Gateway developer portal. Lets an application check whether unconditional or conditional call forwarding is active on a subscriber's lin
  name: GSMA Open Gateway Call Forwarding Signal API
  slug: gsma-open-gateway-call-forwarding-signal
- description: CAMARA Carrier Billing API as published on the GSMA Open Gateway developer portal. Allows a service provider to charge a purchase to the end user's mobile account through the operator, with payment cr
  name: GSMA Open Gateway Carrier Billing API
  slug: gsma-open-gateway-carrier-billing
- description: CAMARA Carrier Billing Refund API as published on the GSMA Open Gateway developer portal. Companion to Carrier Billing, allowing full or partial refunds of a carrier-billed payment to be requested and
  name: GSMA Open Gateway Carrier Billing Refund API
  slug: gsma-open-gateway-carrier-billing-refund
- description: CAMARA Mobile Device Identifier API as published on the GSMA Open Gateway developer portal. Returns identifying details for the device a subscriber is currently using, such as manufacturer, model, and
  name: GSMA Open Gateway Mobile Device Identifier API
  slug: gsma-open-gateway-device-identifier
- description: 'CAMARA Device Location Retrieval API as published on the GSMA Open Gateway developer portal. Retrieves the network-derived location of a device as a circle or polygon with an accuracy radius, without '
  name: GSMA Open Gateway Device Location Retrieval API
  slug: gsma-open-gateway-device-location-retrieval
- description: CAMARA Device Location Verification API as published on the GSMA Open Gateway developer portal. Answers whether a device is within a requested area rather than returning coordinates, a privacy-preserv
  name: GSMA Open Gateway Device Location Verification API
  slug: gsma-open-gateway-device-location-verification
- description: CAMARA Device Reachability Status API as published on the GSMA Open Gateway developer portal. Reports whether a device is currently reachable on the network and by which connectivity type, used for Io
  name: GSMA Open Gateway Device Reachability Status API
  slug: gsma-open-gateway-device-reachability-status
- description: 'CAMARA Device Roaming Status API as published on the GSMA Open Gateway developer portal. Reports whether a subscriber''s device is currently roaming and, where available, the visited country, used for '
  name: GSMA Open Gateway Device Roaming Status API
  slug: gsma-open-gateway-device-roaming-status
- description: CAMARA Device Swap API as published on the GSMA Open Gateway developer portal. Checks whether the device associated with a mobile number has changed within a recent window, a signal used alongside SIM
  name: GSMA Open Gateway Device Swap API
  slug: gsma-open-gateway-device-swap
- description: CAMARA Home Devices Quality on Demand API as published on the GSMA Open Gateway developer portal. Requests a prioritised quality-of-service profile for a device on a fixed or home broadband connection
  name: GSMA Open Gateway Home Devices QoD API
  slug: gsma-open-gateway-home-devices-quality-on-demand
- description: CAMARA Know Your Customer Match API as published on the GSMA Open Gateway developer portal. Submits customer-supplied identity attributes such as name, address, and date of birth and returns per-attri
  name: GSMA Open Gateway Know Your Customer Match API
  slug: gsma-open-gateway-know-your-customer
- description: 'CAMARA Number Verification API as published on the GSMA Open Gateway developer portal. Silently verifies or retrieves the mobile number of the device making a request using network-based or SIM-based '
  name: GSMA Open Gateway Number Verification API
  slug: gsma-open-gateway-number-verification
- description: CAMARA One Time Password SMS API as published on the GSMA Open Gateway developer portal. Sends a one-time password by SMS through the operator and validates the code the user returns, offered as a fal
  name: GSMA Open Gateway One Time Password SMS API
  slug: gsma-open-gateway-otp-validation
- description: CAMARA Population Density Data API as published on the GSMA Open Gateway developer portal. Returns aggregated, anonymised estimates of device density across a requested geographic area and time window
  name: GSMA Open Gateway Population Density Data API
  slug: gsma-open-gateway-population-density-data
- description: CAMARA Quality on Demand API as published on the GSMA Open Gateway developer portal. Requests, extends, and releases a prioritised network quality profile for a device session, with event notification
  name: GSMA Open Gateway Quality On Demand API
  slug: gsma-open-gateway-quality-on-demand
- description: CAMARA SIM Swap API as published on the GSMA Open Gateway developer portal. Checks whether the SIM associated with a mobile number has been swapped within a recent window and returns the last swap dat
  name: GSMA Open Gateway SIM Swap API
  slug: gsma-open-gateway-sim-swap
- description: CAMARA Simple Edge Discovery API as published on the GSMA Open Gateway developer portal. Returns the closest edge cloud zone to a given device so an application can route traffic to the lowest-latency
  name: GSMA Open Gateway Simple Edge Discovery API
  slug: gsma-open-gateway-simple-edge-discovery
artifact_total: 25
asyncapis:
- description: ''
  name: Gsma Webhooks
  slug: gsma-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gsma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gsma-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gsma-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gsma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gsma.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open-gateway.gsma.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-gateway.gsma.com/docs
- group: start
  title: ''
  type: Sandbox
  url: https://open-gateway.gsma.com/sandbox
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mobilemoneyapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-frequently-asked-questions/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/supporters/
- group: other
  title: ''
  type: Dataset
  url: https://d3bj8knxlstxyw.cloudfront.net/assets-map-launches.json
- group: docs
  title: ''
  type: Documentation
  url: https://open-gateway.gsma.com/map
- group: docs
  title: ''
  type: Specification
  url: https://camaraproject.org/api-overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GSMA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camaraproject
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gsma/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/gsma
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/gsma
- group: company
  title: ''
  type: Newsroom
  url: https://www.gsma.com/newsroom/
- group: other
  title: ''
  type: Services
  url: https://www.gsmaservices.com/
- group: other
  title: ''
  type: Membership
  url: https://www.gsma.com/get-involved/gsma-membership/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gsma-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gsma-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.gsma.com/security/
- group: build
  title: ''
  type: Packages
  url: packages/gsma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gsma-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gsma-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/gsma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gsma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gsma-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/change-list.html
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gsma-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gsma-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gsma-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gsma-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/change-list.html
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gsma-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gsma-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gsma-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gsma-webhooks.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mobilemoneyapi.io/api-versions-1.2/resources/api-service-definition.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mobilemoneyapi.io/sdks/getting-started/introduction.html
- group: operate
  title: ''
  type: Support
  url: https://developer.mobilemoneyapi.io/support/
- group: company
  title: ''
  type: Blog
  url: https://www.gsma.com/newsroom/
- group: start
  title: ''
  type: SignUp
  url: https://developer.mobilemoneyapi.io/signup/
- group: start
  title: ''
  type: Login
  url: https://developer.mobilemoneyapi.io/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gsma.com/aboutus/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsma.com/aboutus/legal/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://developer.mobilemoneyapi.io/faq/
- group: other
  title: ''
  type: Glossary
  url: https://developer.mobilemoneyapi.io/glossary/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mobilemoneyapi.io/
created: '2026-07-25'
description: 'The GSMA (GSM Association) is the London-headquartered global trade body for the mobile industry, representing roughly 750 mobile network operators and around 400 companies in the wider mobile ecosystem, and the organiser of MWC Barcelona. In telecom''s API value chain the GSMA is not a network operator and not an aggregator; it is the standards and commitment layer. Its GSMA Open Gateway initiative is the memorandum of understanding under which 69 operator groups, representing 78% of global mobile connections, commit to exposing a common set of network APIs, while the API specifications themselves are authored in the Linux Foundation''s CAMARA project. The GSMA''s API posture is unusually open for a standards body: its Open Gateway developer portal at open-gateway.gsma.com publishes 17 CAMARA OpenAPI 3.0.3 documents in full, without login, alongside a live public deployment map covering 607 launched API instances across 80 operators and 65 countries, and it runs a separate,
  fully open Mobile Money API developer portal with a downloadable OpenAPI 3.0.0 specification, SDKs, and use-case guides. The gates are real but narrow: the API sandbox requires a GitHub sign-in, the anti-fraud Scam Signal API is held in a private GSMA repository rather than in public CAMARA, and the commercial GSMA Services products (Device Check, IMEI Database, PathFinder, Disposable Number Check) are membership and contract gated with no public documentation. The GSMA runs no production network API endpoints of its own — every Open Gateway API is served by an operator or a channel partner such as Infobip, IPification, TMT iD, XConnect, or Singtel.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: gsma-mcp.yml
  slug: gsma-mcpyml
modified: '2026-07-25'
name: GSMA
nav: Providers
network: true
overview: 'GSMA publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Mobile Money API, Open Gateway Call Forwarding Signal API, Open Gateway Carrier Billing API, and 15 more. Tagged areas include Telecommunications, United Kingdom, Standards, Trade Association, and Network APIs.


  The GSMA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GSMA''s developer surface includes authentication, documentation, sandbox, YouTube channel, changelog, API reference, getting-started guide, and 47 more developer resources.'
random_paper: 14
scopes:
- name: Gsma Scopes
  scope_count: 30
  slug: gsma-scopes
  summary_line: 30 scopes
score:
  band: strong
  composite: 58.7
  delta: 3.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.6
    developer_ergonomics: 69.0
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 5.6
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 93.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Gsma Authentication
  slug: gsma-authentication
  summary_line: http/openIdConnect/unknown · 3 schemes
- kind: domain-security
  name: Gsma Domain Security
  slug: gsma-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gsma Vulnerability Disclosure
  slug: gsma-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gsma
tags:
- Telecommunications
- United Kingdom
- Standards
- Trade Association
- Network APIs
- CAMARA
- Open Gateway
- Mobile Network Operators
- Identity Verification
- SIM Swap
- Mobile Money
- eSIM
- 5G
- Anti-Fraud
- Specification
website: https://www.gsma.com/
---
