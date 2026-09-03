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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Swisscom Agentic Access
  operation_count: 12
  slug: swisscom-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 2
apis:
- description: Application-to-person SMS sending over the Swisscom messaging infrastructure with onward delivery to 260+ operators globally, including delivery-notification callbacks to a customer-supplied callbackU
  name: Swisscom Text Messaging (SMS) API
  slug: swisscom-text-messaging-api
- description: Two-factor authentication API that starts an SMS token validation flow against an MSISDN and then verifies the token the user received. This is Swisscom's own SMS-OTP product, not the CAMARA Number Ve
  name: Swisscom Phone Number Validation API
  slug: swisscom-phone-number-validation-api
- description: Inbound SMS API that exposes message inboxes so applications can receive texts from customers and build two-way messaging flows, alerting and device control alongside the outbound Text Messaging produ
  name: Swisscom Receive SMS API
  slug: swisscom-receive-sms-api
- description: Mobility Insights API returning estimated population density per 100m x 100m tile per hour across the whole of Switzerland, from yesterday back two years on a rolling window, with socio-demographic sp
  name: Swisscom Heatmaps API
  slug: swisscom-heatmaps-api
- description: Mobility Insights API returning a frequency distribution of observed dwell times per 500m x 500m tile per day across Switzerland, bucketed from 0-5 minutes up to 8-24 hours, for any day within a rolli
  name: Swisscom Dwell Times API
  slug: swisscom-dwell-times-api
- description: Mobility Insights API estimating the number of trips people make between two Swiss regions for weekdays and weekends over a full calendar month, including the share made by train, queryable by 1km til
  name: Swisscom Origin Destination API
  slug: swisscom-origin-destination-api
- description: Business/wholesale provisioning API covering the full NATEL go mobile subscription procurement lifecycle — activations, number portability, option and roaming configuration, SIM and eSIM ordering with
  name: Swisscom Smart Catalogs for NATEL go API
  slug: swisscom-smart-catalogs-natel-go-api
- description: 'OpenAI-compatible inference endpoints for chat, multimodal, audio, embedding, reasoning and guardrail models hosted by Swisscom on NVIDIA SuperPod infrastructure in Switzerland, including Meta Llama, '
  name: Swiss AI Platform Inference Endpoints API
  slug: swiss-ai-platform-inference-api
- description: REST API that looks up legal entities and their authorised signatories against Swiss federal and cantonal commercial registries and selected EU business registers, for KYB onboarding, compliance and d
  name: Swisscom Business Identity Validator API
  slug: swisscom-business-identity-validator-api
- description: Legacy Voice API cluster for controlling a Swisscom VoIP subscriber — placing and listing calls, managing call forwardings, simultaneous ringing and phonebooks, and subscribing to VoIP events. Secured
  name: Swisscom Voice VoIP API
  slug: swisscom-voice-voip-api
- description: Legacy Voice API for listing and retrieving recent voicemail messages for a Swisscom MSISDN, secured by OAuth 2.0 client-credentials or authorization-code grants. Documented as RAML-rendered HTML in t
  name: Swisscom Voice Mail API
  slug: swisscom-voice-mail-api
- baseURL: https://sign.swisscom.ch/system
  baseurl_source: declared
  description: Allows you to set up your process according to your needs, including adding documents, configuring invitees, setting signature options, and submitting the process for execution.
  name: 'Swisscom Process: create API'
  slug: swisscom-process-create-api
- baseURL: https://sign.swisscom.ch/system
  baseurl_source: declared
  description: Access process information and download signed or original documents once the signing is complete.
  name: 'Swisscom Process: read API'
  slug: swisscom-process-read-api
- baseURL: https://sign.swisscom.ch/system
  baseurl_source: declared
  description: The signatures API from Swisscom — 1 operation(s) for signatures.
  name: Swisscom Signatures API
  slug: swisscom-signatures-api
artifact_total: 24
asyncapis:
- description: ''
  name: Swisscom Messaging Webhooks
  slug: swisscom-messaging-webhooks
collections:
- collection_type: open
  name: All-in Signing Service REST Application
  slug: open-swisscom-all-in-signing-service
- collection_type: open
  name: Swisscom Sign Integration API
  slug: open-swisscom-sign-integration-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/swisscom-sign-integration-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/swisscom-all-in-signing-service-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/swisscom-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swisscom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/swisscom-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/swisscom-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swisscom-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/swisscom-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swisscom-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/swisscom-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/swisscom-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/swisscom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swisscom-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://trustservices.swisscom.com/en/support/developer-section/service-status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/swisscom-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/swisscom-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/swisscom-messaging-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swisscom-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trustservices.swisscom.com/en/esignature-hub/downloads-and-documents
- group: auth
  title: ''
  type: TrustCenter
  url: security/swisscom-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.swisscom.ch/en/about/security/bug-bounty.html
- group: build
  title: ''
  type: Postman
  url: https://github.com/SwisscomTrustServices/AIS-Postman-Samples
- group: docs
  title: ''
  type: APIReference
  url: https://sign.swisscom.ch/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://sign.swisscom.ch/docs/guide/getting-started
- group: operate
  title: ''
  type: Support
  url: https://trustservices.swisscom.com/en/support
- group: company
  title: ''
  type: Blog
  url: https://trustservices.swisscom.com/en/esignature-hub/trust-blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trustservices.swisscom.com/en/privacypolicy
- group: start
  title: ''
  type: SignUp
  url: https://sign.swisscom.ch/cockpit/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/swisscom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/swisscom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swisscom-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/swisscom-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/swisscom-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.swisscom.ch/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://digital.swisscom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sign.swisscom.ch/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://digital.swisscom.com/resources/use-your-api-keys/oaut-introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swisscom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SwisscomTrustServices
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/swisscom-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swisscom
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://github.com/swisscom/bugbounty
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.swisscom.ch/.well-known/security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://digital.swisscom.com/terms
- group: other
  title: ''
  type: OpenIDConfiguration
  url: https://sign.swisscom.ch/realms/swisscom-public/.well-known/openid-configuration
created: '2026-07-25'
description: 'Swisscom is Switzerland''s largest telecommunications provider and the incumbent mobile network operator, fixed-line carrier and IT services company for the Swiss market, majority-owned by the Swiss Confederation and also operating Fastweb in Italy. In the telecom value chain it is a facilities-based MNO that owns the radio access and core network, sells mobile, broadband, TV and enterprise IT, and monetises network-derived data. Its API posture is unusual for a European incumbent: alongside the expected partner-gated enterprise surface it runs a genuine first-party API marketplace at digital.swisscom.com listing ten productive API products (SMS, SMS token 2FA, inbound SMS, mobility heatmaps, dwell times, origin-destination, NATEL go smart catalogs, AI inference endpoints and a business identity validator) served from a live api.swisscom.com gateway, plus a separately maintained, actively released Swisscom Sign Integration API with a downloadable OpenAPI 3.1 document. The catch
  is that every API reference, key and spec beyond Swisscom Sign sits behind a Swisscom login and, for several products, a signed service contract — the marketplace is a storefront, not open documentation. On network APIs Swisscom was one of the 21 founding signatories of the GSMA Open Gateway Memorandum of Understanding in February 2023, but it publishes no CAMARA API, no Open Gateway developer portal and no callable network-API endpoint; developers who want SIM-swap or phone-verification signals from the Swisscom network have historically reached them through third-party channels such as IPification rather than from Swisscom directly. Its legacy developer programme (developer.swisscom.com, the Cloud Foundry Application Cloud, the swisscom-developer GitHub SDKs) is dead or redirected, and the older Messaging and Voice APIs are still documented only as RAML-rendered HTML in a GitHub wiki.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Swisscom MCP Server
  slug: swisscom-mcp-server
modified: '2026-07-25'
name: Swisscom
nav: Providers
network: true
overview: 'Swisscom publishes 3 APIs on the [APIs.io](https://apis.io/) network: Process: create API, Process: read API, and Signatures API. Tagged areas include Telecommunications, Switzerland, Mobile Network Operator, Broadband, and Network APIs.


  The Swisscom catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Swisscom''s developer surface includes CLI, changelog, sandbox, API reference, getting-started guide, support, engineering blog, and 39 more developer resources.'
random_paper: 6
scopes:
- name: Swisscom Scopes
  scope_count: 3
  slug: swisscom-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 67.2
    developer_ergonomics: 75.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 65.6
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
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 83.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swisscom/refs/heads/main/screenshots/swisscom-2026-08-17T082213.png
security:
- kind: authentication
  name: Swisscom Authentication
  slug: swisscom-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Swisscom Domain Security
  slug: swisscom-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Swisscom Vulnerability Disclosure
  slug: swisscom-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Swisscom Trust Center
  slug: swisscom-trust-center
  summary_line: Qualified certification service provider under ZertES, Qualified trust service provider under eIDAS, Remote signature issuance conformity under ZertES
slug: swisscom
tags:
- Telecommunications
- Switzerland
- Mobile Network Operator
- Broadband
- Network APIs
- Open Gateway
- Messaging
- SMS
- Voice
- Identity Verification
- Mobility Data
- Digital Signatures
- eSIM
- Artificial Intelligence
website: https://www.swisscom.ch/
---
