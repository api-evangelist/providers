---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 63.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 242
  human_in_the_loop: 8
  name: Zoom Phone Agentic Access
  operation_count: 419
  slug: zoom-phone-agentic-access
  summary_line: 419 operations · 242 acting · 8 human-in-the-loop
api_count: 3
apis:
- description: The Zoom Phone API is the administrative and operational REST API for Zoom's cloud phone system. The harvested OpenAPI 3.0 document describes 238 paths and 391 operations across 46 resource groups — U
  name: Zoom Phone API
  slug: zoom-phone-api
- description: The Zoom Phone event catalog, published as an OpenAPI 3.1 document using the top-level webhooks object. It defines 71 real-time events covering call lifecycle (phone.caller_ringing, phone.callee_answe
  name: Zoom Phone Webhooks
  slug: zoom-phone-webhooks
- description: The Number Management API provisions and manages phone number inventory for Zoom Phone, Zoom Contact Center, and Zoom Meetings accounts. The harvested OpenAPI 3.0 document describes 17 paths and 28 op
  name: Zoom Phone Number Management API
  slug: zoom-phone-number-management-api
artifact_total: 12
asyncapis:
- description: ''
  name: Zoom Phone Webhooks
  slug: zoom-phone-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoom-phone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/zoom-phone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoom-phone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoom-phone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoom-phone-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoom-phone-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoom.com/en/products/voip-phone/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zoom.us/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zoom.us/docs/api/phone/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.zoom.us/docs/integrations/oauth/
- group: design
  title: ''
  type: OAuthMetadata
  url: https://zoom.us/.well-known/oauth-authorization-server
- group: commercial
  title: ''
  type: Pricing
  url: https://zoom.us/pricing/zoom-phone
- group: other
  title: ''
  type: AppMarketplace
  url: https://marketplace.zoom.us/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/zoom-developer/zoom-public-workspace/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoom
- group: build
  title: ''
  type: SDK
  url: https://github.com/zoom/rivet-javascript
- group: company
  title: ''
  type: Blog
  url: https://developers.zoom.us/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.zoomstatus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zoom.us/docs/api/phone/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zoom.us/docs/phone/start/
- group: start
  title: ''
  type: Quickstart
  url: https://developers.zoom.us/docs/phone/first-app/
- group: operate
  title: ''
  type: Support
  url: https://developers.zoom.us/support/
- group: operate
  title: ''
  type: Community
  url: https://devforum.zoom.us/
- group: start
  title: ''
  type: SignUp
  url: https://zoom.us/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoom.com/en/trust/terms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zoom.us/docs/en-us/zoom_api_license_and_tou.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoom.com/en/trust/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zoom-developer/zoom-public-workspace/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.zoom.us/changelog/?product=phone
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoom.us/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.zoom.us/docs/build/lifecycle/
- group: auth
  title: ''
  type: Security
  url: https://www.zoom.com/en/trust/reporting-vulnerability/
- group: auth
  title: ''
  type: Compliance
  url: https://www.zoom.com/en/trust/
- group: build
  title: ''
  type: SDKs
  url: packages/zoom-phone-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zoom-phone-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/zoom-phone-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zoom-phone-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/zoom-phone-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/zoom-phone-api-catalog.json
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zoom-phone-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoom-phone-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/zoom-phone-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/zoom-phone-number-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/zoom-phone-webhooks-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/zoom-phone-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zoom-phone-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zoom-phone-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zoom-phone-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zoom-phone-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoom-phone-rate-limits.yml
- group: design
  title: ''
  type: Components
  url: components/zoom-phone-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zoom-phone-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zoom-phone-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-25'
description: 'Zoom Phone is the cloud PBX / UCaaS voice product of Zoom Communications, headquartered in San Jose, California, and sold worldwide from its United States home market. It replaces on-premise telephony with a cloud calling service — extensions, auto receptionists, IVR, call queues, shared line groups, voicemail, call recording, fax, emergency (E911) addressing, and SMS/MMS — delivered either on Zoom-provided PSTN service, on a customer''s own carrier through BYOC and Cloud Peering (Provider Exchange), or resold through carrier partners. In the telecom value chain Zoom Phone sits above the network as a UCaaS application layer that buys wholesale connectivity and number inventory from carriers rather than operating a mobile network, and its API posture reflects the software half of that split rather than the carrier half: the Zoom Phone API is fully self-serve, published as downloadable OpenAPI 3.0 with 391 documented operations across 46 resource groups, a 71-event webhook catalog,
  a separate Number Management API covering number allocation, BYOC numbers, ported number orders, SIP trunks and 10DLC SMS campaigns, OAuth 2.0 with fine-grained phone:* scopes, a public Postman workspace, and an official Node/TypeScript SDK. It is not a mobile network operator, is not a GSMA Open Gateway signatory, and exposes no CAMARA network APIs — no CAMARA reference was found anywhere in its developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: zoom-phone-mcp.yml
  slug: zoom-phone-mcpyml
modified: '2026-07-25'
name: Zoom Phone
nav: Providers
network: true
overview: 'Zoom Phone publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Number Management API, and 1 more. Tagged areas include Telecommunications, United States, UCaaS, Cloud PBX, and Voice.


  The Zoom Phone catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zoom Phone''s developer surface includes authentication, documentation, pricing, SDKs, engineering blog, API reference, getting-started guide, and 47 more developer resources.'
random_paper: 108
rate_limits:
- limit_count: 8
  name: Zoom Phone Rate Limits
  slug: zoom-phone-rate-limits
scopes:
- name: Zoom Phone Scopes
  scope_count: 435
  slug: zoom-phone-scopes
  summary_line: 435 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.5
  delta: -1.7
  facets:
    commercial_clarity: 60.5
    contract_quality: 57.2
    developer_ergonomics: 78.3
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 94.7
  previous_composite: 68.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zoom Phone Authentication
  slug: zoom-phone-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Zoom Phone Domain Security
  slug: zoom-phone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoom Phone Vulnerability Disclosure
  slug: zoom-phone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zoom Phone Trust Center
  slug: zoom-phone-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, CSA STAR
slug: zoom-phone
tags:
- Telecommunications
- United States
- UCaaS
- Cloud PBX
- Voice
- VoIP
- SIP
- Messaging
- SMS
- Phone Numbers
- Number Porting
- BYOC
- Carrier Peering
- Contact Center
- Communications
website: https://www.zoom.com/en/products/voip-phone/
---
