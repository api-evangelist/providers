---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 97
  human_in_the_loop: 0
  name: Nokia Network As Code Agentic Access
  operation_count: 148
  slug: nokia-network-as-code-agentic-access
  summary_line: 148 operations · 97 acting
api_count: 7
apis:
- description: The single aggregated Network as Code API surface published by Nokia as one OpenAPI 3.0 document. The harvested specification declares 58 paths / 78 operations spanning device status, location, geofen
  name: Nokia Network as Code Platform API
  slug: network-as-code-platform-api
- description: Nokia's consolidated CAMARA-conformant network API specification, published as Single-NaC-API-OAS.yaml in the public network-as-code-sdks repository. OpenAPI 3.0.3, 52 paths / 70 operations, declaring
  name: Nokia Network as Code CAMARA API
  slug: camara-network-api
- description: The identity and anti-fraud product family. Capabilities advertised by the platform configuration are Call Forwarding Signal, Device Swap, KYC Age Verification, KYC Fill-in, KYC Match, Location Verifi
  name: Network as Code Digital Identity and Anti-Fraud APIs
  slug: digital-identity-and-anti-fraud
- description: The device-state product family — Device Reachability Status, Device Reachability Status Subscriptions, Device Roaming Status, Device Roaming Status Subscriptions, Geofencing Subscriptions and Locatio
  name: Network as Code Device Intelligence APIs
  slug: device-intelligence
- description: The network-control product family — Quality on Demand, Specialized Networks / Network Slice Management, Network Slice Device Attachment, Network Slice Application Attachment and eSIM Provisioning. Th
  name: Network as Code Programmable Connectivity APIs
  slug: programmable-connectivity
- description: The network-analytics product family. Advertised capabilities are Congestion Insights, Network Aware Route Optimization, Population Density Data and Consent and Identity Management. Only two are calla
  name: Network as Code Network Intelligence APIs
  slug: network-intelligence
- description: The platform's OAuth2 / OpenID Connect surface, tagged "NaC Authorization Server" and "Well Known Metadata" in the harvested specification. Real operations are GET /oauth2/v1/auth/clientcredentials (i
  name: Network as Code Authorization Server
  slug: authorization-server
artifact_total: 15
asyncapis:
- description: ''
  name: Nokia Network As Code Webhooks
  slug: nokia-network-as-code-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nokia-network-as-code-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nokia-network-as-code-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nokia-network-as-code-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nokia-network-as-code-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nokia-network-as-code-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nokia-network-as-code-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nokia-network-as-code-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nokia-network-as-code-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nokia-network-as-code-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nokia-network-as-code-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.nokia.com/we-are-nokia/security/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/nokia-network-as-code-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nokia-network-as-code-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.nokia.com/we-are-nokia/security/products/cvd/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nokia-network-as-code-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nokia-network-as-code-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/nokia-network-as-code-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nokia-network-as-code-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nokia-network-as-code-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nokia-network-as-code-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nokia-network-as-code-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nokia-network-as-code-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/nokia-network-as-code-platform-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nokia-network-as-code-camara-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/nokia/network-as-code-sdks/blob/main/network-as-code-py/network_as_code/reference.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://networkascode.nokia.io/legal/supplemental-privacy-notice
- group: company
  title: ''
  type: Website
  url: https://networkascode.nokia.io/
- group: start
  title: ''
  type: Portal
  url: https://networkascode.nokia.io/
- group: docs
  title: ''
  type: Documentation
  url: https://networkascode.nokia.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://networkascode.nokia.io/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://networkascode.nokia.io/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://networkascode.nokia.io/auth/login
- group: company
  title: ''
  type: Blog
  url: https://networkascode.nokia.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://networkascode.nokia.io/legal/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://networkascode.nokia.io/contact-support
- group: other
  title: ''
  type: Sales
  url: https://networkascode.nokia.io/contact-sales
- group: agent
  title: ''
  type: MCP
  url: https://networkascode.nokia.io/docs/mcp-server
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/nokia/network-as-code-sdks
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/network-as-code/
- group: build
  title: ''
  type: SDKs
  url: https://registry.npmjs.org/network-as-code
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nokia
- group: other
  title: ''
  type: Product
  url: https://www.nokia.com/programmable-networks/network-as-code/
- group: other
  title: ''
  type: Product
  url: https://www.nokia.com/networks/programmable-networks/network-as-code/network-as-code-for-csps/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/playlist?list=PLgKNvl454Bxdl7Qk5z6bD4QqKHUtG5vQA
created: '2026-07-25'
description: 'Nokia Network as Code is the network-API exposure and aggregation platform operated by Nokia Oyj from Espoo, Finland, launched in September 2023 to make CAMARA-standardised mobile network capabilities commercially reachable by ordinary application developers. It sits in the middle of the telecom value chain: beneath it, Nokia''s Network Exposure Platform (NEP) is deployed inside a mobile operator''s core to expose that operator''s network; above it, the Network as Code developer platform aggregates many operators'' networks behind one contract, one credential and one set of SDKs, so a developer integrates once instead of negotiating per-carrier. Nokia states more than 75 partners in the ecosystem — telecom providers, CPaaS platforms, systems integrators and vertical ISVs — with named operator agreements including Deutsche Telekom, Globe (Philippines), Orange (France and Spain), Rakuten Mobile, Tata Communications, Telefónica, TELUS and Vodafone (UK, Netherlands, Germany, Spain,
  Greece). Its API posture is unusually open for this tier and should be read honestly: the full platform OpenAPI is published verbatim in a public Apache-2.0 GitHub repository (nokia/network-as-code-sdks), generated Python and TypeScript SDKs ship on PyPI and npm, signup at networkascode.nokia.io is self-serve and a SIMULATOR plan exists — but the developer console, the API catalogue and the in-portal specification viewer all sit behind a login wall, the documentation site is a client-rendered SPA that returns HTTP 200 for any path and serves no crawlable content, and reaching a real subscriber on a real network in a given market still depends on Nokia having a commercial agreement with that market''s operator. The platform is delivered through a white-labelled RapidAPI Enterprise Hub, and every production call is routed through the RapidAPI gateway host network-as-code.p-eu.rapidapi.com rather than a Nokia-owned API hostname. Nokia reaches the market directly and through Google Cloud Marketplace
  rather than through Aduna, the rival Ericsson-led carrier joint venture.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: nokia-network-as-code-mcp.yml
  slug: nokia-network-as-code-mcpyml
modified: '2026-07-25'
name: Nokia Network as Code
nav: Providers
network: true
overview: 'Nokia Network as Code publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Platform API, CAMARA API, Network as Code Digital Identity and Anti-Fraud APIs, and 4 more. Tagged areas include Telecommunications, Finland, Network APIs, CAMARA, and Open Gateway.


  The Nokia Network as Code catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nokia Network as Code''s developer surface includes authentication, changelog, sandbox, API reference, developer portal, documentation, getting-started guide, and 38 more developer resources.'
random_paper: 64
scopes:
- name: Nokia Network As Code Scopes
  scope_count: 65
  slug: nokia-network-as-code-scopes
  summary_line: 65 scopes
score:
  band: strong
  composite: 61.2
  delta: 4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.9
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
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
  name: Nokia Network As Code Authentication
  slug: nokia-network-as-code-authentication
  summary_line: apiKey/openIdConnect/oauth2 · 3 schemes
- kind: domain-security
  name: Nokia Network As Code Domain Security
  slug: nokia-network-as-code-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nokia Network As Code Vulnerability Disclosure
  slug: nokia-network-as-code-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Nokia Network As Code Trust Center
  slug: nokia-network-as-code-trust-center
  summary_line: ISO/IEC 27001:2022
slug: nokia-network-as-code
tags:
- Telecommunications
- Finland
- Network APIs
- CAMARA
- Open Gateway
- Network API Exposure
- Network API Aggregator
- 5G
- Identity Verification
- SIM Swap
- Number Verification
- Device Location
- Quality on Demand
- Network Slicing
- Anti-Fraud
- KYC
- IoT
- eSIM
- Roaming
- Network Exposure
website: https://networkascode.nokia.io/
---
