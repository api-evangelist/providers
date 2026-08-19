---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.7
  scored_at: '2026-08-19'
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
- description: GSMA Call Forwarding Signal from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA Call Forwarding Signal
  slug: gsma-open-gateway-call-forwarding-signal-openapi
- description: GSMA Carrier Billing from GSMA — 6 path(s) described in OpenAPI.
  name: GSMA Carrier Billing
  slug: gsma-open-gateway-carrier-billing-openapi
- description: GSMA Carrier Billing Refund from GSMA — 3 path(s) described in OpenAPI.
  name: GSMA Carrier Billing Refund
  slug: gsma-open-gateway-carrier-billing-refund-openapi
- description: GSMA CAMARA Mobile Device Identifier from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA CAMARA Mobile Device Identifier
  slug: gsma-open-gateway-device-identifier-openapi
- description: GSMA Device Location Retrieval from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Device Location Retrieval
  slug: gsma-open-gateway-device-location-retrieval-openapi
- description: GSMA Device Location Verification from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Device Location Verification
  slug: gsma-open-gateway-device-location-verification-openapi
- description: GSMA Device Reachability Status from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Device Reachability Status
  slug: gsma-open-gateway-device-reachability-status-openapi
- description: GSMA Device Roaming Status from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Device Roaming Status
  slug: gsma-open-gateway-device-roaming-status-openapi
- description: GSMA Device Swap from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA Device Swap
  slug: gsma-open-gateway-device-swap-openapi
- description: GSMA Home Devices QoD from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Home Devices QoD
  slug: gsma-open-gateway-home-devices-quality-on-demand-openapi
- description: GSMA Know Your Customer Match from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Know Your Customer Match
  slug: gsma-open-gateway-know-your-customer-openapi
- description: GSMA Number Verification from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA Number Verification
  slug: gsma-open-gateway-number-verification-openapi
- description: GSMA One Time Password SMS from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA One Time Password SMS
  slug: gsma-open-gateway-otp-validation-openapi
- description: GSMA Population Density Data from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Population Density Data
  slug: gsma-open-gateway-population-density-data-openapi
- description: GSMA Quality-On-Demand from GSMA — 4 path(s) described in OpenAPI.
  name: GSMA Quality-On-Demand
  slug: gsma-open-gateway-quality-on-demand-openapi
- description: GSMA SIM Swap from GSMA — 2 path(s) described in OpenAPI.
  name: GSMA SIM Swap
  slug: gsma-open-gateway-sim-swap-openapi
- description: GSMA Simple Edge Discovery from GSMA — 1 path(s) described in OpenAPI.
  name: GSMA Simple Edge Discovery
  slug: gsma-open-gateway-simple-edge-discovery-openapi
artifact_total: 43
asyncapis:
- description: ''
  name: Gsma Webhooks
  slug: gsma-webhooks
collections:
- collection_type: open
  name: Mobile Money API
  slug: open-gsma-mobile-money-api
- collection_type: open
  name: Call Forwarding Signal
  slug: open-gsma-open-gateway-call-forwarding-signal
- collection_type: open
  name: Carrier Billing Refund
  slug: open-gsma-open-gateway-carrier-billing-refund
- collection_type: open
  name: Carrier Billing
  slug: open-gsma-open-gateway-carrier-billing
- collection_type: open
  name: CAMARA Mobile Device Identifier
  slug: open-gsma-open-gateway-device-identifier
- collection_type: open
  name: Device Location Retrieval
  slug: open-gsma-open-gateway-device-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-gsma-open-gateway-device-location-verification
- collection_type: open
  name: Device Reachability Status
  slug: open-gsma-open-gateway-device-reachability-status
- collection_type: open
  name: Device Roaming Status
  slug: open-gsma-open-gateway-device-roaming-status
- collection_type: open
  name: Device Swap
  slug: open-gsma-open-gateway-device-swap
- collection_type: open
  name: Home Devices QoD
  slug: open-gsma-open-gateway-home-devices-quality-on-demand
- collection_type: open
  name: Know Your Customer Match
  slug: open-gsma-open-gateway-know-your-customer
- collection_type: open
  name: Number Verification
  slug: open-gsma-open-gateway-number-verification
- collection_type: open
  name: One Time Password SMS
  slug: open-gsma-open-gateway-otp-validation
- collection_type: open
  name: Population Density Data
  slug: open-gsma-open-gateway-population-density-data
- collection_type: open
  name: Quality-On-Demand
  slug: open-gsma-open-gateway-quality-on-demand
- collection_type: open
  name: SIM Swap
  slug: open-gsma-open-gateway-sim-swap
- collection_type: open
  name: Simple Edge Discovery
  slug: open-gsma-open-gateway-simple-edge-discovery
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
overview: 'GSMA publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Mobile Money API, Call Forwarding Signal, Carrier Billing, and 15 more. Tagged areas include Telecommunications, United Kingdom, Standards, Trade Association, and Network APIs.


  The GSMA catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GSMA''s developer surface includes authentication, documentation, sandbox, YouTube channel, changelog, API reference, getting-started guide, and 47 more developer resources.'
random_paper: 126
scopes:
- name: Gsma Scopes
  scope_count: 30
  slug: gsma-scopes
  summary_line: 30 scopes
score:
  band: strong
  composite: 61.0
  delta: 5.3
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 63.3
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 55.7
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
    score: 87.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/gsma/refs/heads/main/screenshots/gsma-2026-08-07T165856.png
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
