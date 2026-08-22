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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Reliance Jio Agentic Access
  operation_count: 29
  slug: reliance-jio-agentic-access
  summary_line: 29 operations · 19 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Server-to-server REST API for the JioMeet video meeting platform, documented publicly at dev.jiomeet.com. Covers creating dynamic meetings, creating, fetching, updating and deleting scheduled meetings
  name: JioMeet Platform Server API
  slug: jiomeet-platform-server-api
- description: User-authorized REST API for JioMeet, using OAuth 2.0. An access and refresh token are obtained from the /api/oauth2/v2/token endpoint using HTTP Basic authentication with an OAuth client id and secre
  name: JioMeet Platform OAuth API
  slug: jiomeet-platform-oauth-api
- description: Server-side REST API for JioEvents, Jio's webinar and virtual event platform, documented alongside JioMeet at dev.jiomeet.com. Covers creating, fetching, updating and deleting scheduled webinars, crea
  name: JioEvents Platform Server API
  slug: jioevents-platform-server-api
- description: In-app purchase and digital content payment API for applications published on the Jio set-top box, distributed by Jio Platforms as a downloadable PDF API specification (v1.1) from the JioDevelopers se
  name: JioPayments Set-Top-Box API
  slug: jiopayments-stb-api
artifact_total: 13
collections:
- collection_type: open
  name: JioEvents Platform APIs
  slug: open-reliance-jio-jioevents-platform
- collection_type: open
  name: JioMeet User OAuth APIs
  slug: open-reliance-jio-jiomeet-oauth
- collection_type: open
  name: JioMeet Platform APIs
  slug: open-reliance-jio-jiomeet-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reliance-jio-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reliance-jio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reliance-jio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reliance-jio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reliance-jio-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/reliance-jio-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reliance-jio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reliance-jio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reliance-jio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://s3.us-east-1.amazonaws.com/tmf-sfdc-public/Conformance/CON-01539/JIO-Certification%20Report-TMF653%20API-Aug2022.pdf
- group: build
  title: ''
  type: Packages
  url: packages/reliance-jio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reliance-jio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/reliance-jio-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reliance-jio-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reliance-jio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reliance-jio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/reliance-jio-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reliance-jio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://jiomeetpro.jio.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reliance-jio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.jiomeet.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.jio.com/
- group: start
  title: ''
  type: SignUp
  url: https://platform.jiomeet.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JioMeet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jio/
- group: operate
  title: ''
  type: Support
  url: https://stackoverflow.com/questions/tagged/jiomeet
- group: docs
  title: ''
  type: Documentation
  url: https://publish.jiogames.com/documents/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.jiogames.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jio.com/business/services/jiocx/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jio.com/business/services/iot/
- group: auth
  title: ''
  type: Certification
  url: https://s3.us-east-1.amazonaws.com/tmf-sfdc-public/Conformance/CON-01539/JIO-Certification%20Report-TMF653%20API-Aug2022.pdf
- group: operate
  title: ''
  type: PressRelease
  url: https://www.gsma.com/newsroom/press-release/indian-mobile-operators-help-online-businesses-combat-scams-and-identity-theft-through-new-federated-network-services-supported-by-gsma-open-gateway/
- group: company
  title: ''
  type: Partner
  url: https://adunaglobal.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.jiomeet.com/docs/quick-start/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://dev.jiomeet.com/docs/JioMeet%20Platform%20Server%20APIs/jiomeet-platform-apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jio.com/jcms/en-in/general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jio.com/jcms/en-in/jio-privacy-policy/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.jio.com/help/
created: '2026-07-25'
description: Reliance Jio Infocomm, the telecom arm of Jio Platforms Limited and Reliance Industries, is India's largest mobile network operator, serving roughly half a billion subscribers on an all-IP 4G/5G network from its home market of India, alongside JioFiber broadband, JioAirFiber fixed wireless, IoT connectivity, and an enterprise CPaaS business branded JioCX. Jio sits at the network-operator layer of the telecom value chain and its API posture is split in two. Its BSS/OSS side is unusually standards-forward - Jio was the first communications service provider to reach TM Forum Open API Platinum conformance, with more than twenty certified Open APIs - but those interfaces are internal supplier-integration contracts, not a public developer product. Its network APIs are genuinely live, since Jio launched the CAMARA SIM Swap API alongside Bharti Airtel and Vodafone Idea under GSMA Open Gateway, and Jio is one of the twelve carrier equity owners of Aduna, the Ericsson-led network-API
  joint venture. There is, however, no first-party Open Gateway developer portal - opengateway.jio.com and developers.opengateway.jio.com do not resolve - so those network APIs are partner-gated and reachable only through the Aduna aggregation channel, the GSMA federated hub, and CPaaS partners rather than directly from Jio. What Jio does publish self-serve is a real developer portal for its SaaS products at dev.jiomeet.com, covering the JioMeet and JioEvents platform REST APIs with JWT and OAuth 2.0 auth and thirty-four public client SDK repositories, plus a set-top-box app developer programme at developer.jio.com. Jio serves no downloadable OpenAPI or Swagger document anywhere across those surfaces, but the dev.jiomeet.com reference is generated by the docusaurus-openapi-docs plugin and its build embeds the real OpenAPI operation objects - method, path, servers, parameters, request bodies, responses and security schemes - which API Evangelist harvested into three OpenAPI 3.0.3 documents
  covering 29 operations on two previously undocumented hosts, jiomeetpro.jio.com and jioevents.com.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: reliance-jio-mcp.yml
  slug: reliance-jio-mcpyml
modified: '2026-07-25'
name: Reliance Jio
nav: Providers
network: true
overview: 'Reliance Jio publishes 3 APIs on the [APIs.io](https://apis.io/) network: JioMeet Platform Server API, JioMeet Platform OAuth API, and JioEvents Platform Server API. Tagged areas include Telecommunications, India, Mobile Network Operator, Network APIs, and CAMARA.


  Reliance Jio''s developer surface includes authentication, code examples, documentation, signup flow, support, getting-started guide, API reference, and 33 more developer resources.'
random_paper: 5
scopes:
- name: Reliance Jio Scopes
  scope_count: 6
  slug: reliance-jio-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 58.8
  delta: 6.7
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 30.3
    contract_quality: 53.4
    developer_ergonomics: 63.7
    discoverability: 83.3
    governance: 30.3
    operational_transparency: 13.2
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 100.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/reliance-jio/refs/heads/main/screenshots/reliance-jio-2026-08-17T081508.png
security:
- kind: authentication
  name: Reliance Jio Authentication
  slug: reliance-jio-authentication
  summary_line: http/jwt-bearer/oauth2 · 3 schemes
- kind: domain-security
  name: Reliance Jio Domain Security
  slug: reliance-jio-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Reliance Jio Vulnerability Disclosure
  slug: reliance-jio-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: reliance-jio
tags:
- Telecommunications
- India
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- CPaaS
- Messaging
- Voice
- IoT
- Broadband
- 5G
- BSS
- OSS
- Standards
- Video Conferencing
website: https://www.jio.com/
---
