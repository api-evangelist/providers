---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Optus Agentic Access
  operation_count: 15
  slug: optus-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- description: Hosted two-factor authentication API that creates an SMS one-time-code challenge for a mobile handset with POST /challenges and validates the user's entry with POST /responses, with customisable messa
  name: Optus SMS Suite 2FA REST API
  slug: optus-sms-suite-2fa-rest-api
- description: Companion REST API to the SMS gateway for scheduling and sending plain-text transactional email over a separate endpoint, returning a 64-bit message ID for later retrieval and firing DLR callbacks whe
  name: Optus SMS Suite REST Email API
  slug: optus-sms-suite-rest-email-api
- description: Legacy GET-based HTTPS interface for SMS integration, covering message sending, delivery receipts, and inbound (mobile-originated) message callbacks for systems that cannot build a JSON REST client. N
  name: Optus SMS Suite HTTPS API
  slug: optus-sms-suite-https-api
- description: WSDL-described SOAP interface for SMS integration supporting custom source addressing, message classification, and structured error handling, published for legacy enterprise middleware. The WSDL is se
  name: Optus SMS Suite SOAP API
  slug: optus-sms-suite-soap-api
- description: Implementation of the 3GPP MM7 SOAP protocol for sending and receiving MMS, carrying text, image, audio, video, and SMIL content in multipart MIME requests to /mm7, with MO message and delivery-report
  name: Optus SMS Suite MMS MM7 API
  slug: optus-sms-suite-mms-mm7-api
- description: Direct SMSC connectivity over SMPP 3.3 and 3.4 with mandatory TLS, offering high-throughput binary messaging, custom character encoding, and detailed delivery reporting. A wire protocol rather than an
  name: Optus SMS Suite SMPP API
  slug: optus-sms-suite-smpp-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Delete Multiple Lists API from Optus — 1 operation(s) for delete multiple lists.
  name: Optus Delete Multiple Lists API
  slug: optus-delete-multiple-lists-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The documentation API from Optus — 1 operation(s) for documentation.
  name: Optus Documentation API
  slug: optus-documentation-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Lists API from Optus — 2 operation(s) for lists.
  name: Optus Lists API
  slug: optus-lists-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Messages API from Optus — 3 operation(s) for messages.
  name: Optus Messages API
  slug: optus-messages-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Report API from Optus — 1 operation(s) for report.
  name: Optus Report API
  slug: optus-report-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Scheduled Campaigns API from Optus — 1 operation(s) for scheduled campaigns.
  name: Optus Scheduled Campaigns API
  slug: optus-scheduled-campaigns-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Services API from Optus — 1 operation(s) for services.
  name: Optus Services API
  slug: optus-services-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Status API from Optus — 1 operation(s) for status.
  name: Optus Status API
  slug: optus-status-api
- baseURL: https://api.sms.optus.com.au/rest/gateway
  baseurl_source: declared
  description: The Templates API from Optus — 1 operation(s) for templates.
  name: Optus Templates API
  slug: optus-templates-api
artifact_total: 25
asyncapis:
- description: Derived event description for the callbacks The Optus SMS Suite POSTs to subscriber-hosted URLs. Optus publishes NO AsyncAPI document; this file was derived by API Evangelist from two sources that are
  name: The Optus SMS Suite Callback Surface
  slug: optus-sms-suite-asyncapi
collections:
- collection_type: open
  name: Campaign Manager
  slug: open-optus-sms-suite-campaign-manager
- collection_type: open
  name: The Optus SMS Suite REST API
  slug: open-optus-sms-suite-rest-v1
- collection_type: open
  name: SMS Gateway REST APIv2
  slug: open-optus-sms-suite-rest-v2
- collection_type: open
  name: Omni Status API
  slug: open-optus-sms-suite-status
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/optus-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/optus-sms-suite-rest-v1-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/optus-sms-suite-rest-v2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/optus-send-and-reconcile-sms.md
- group: other
  title: ''
  type: Overlay
  url: overlays/optus-sms-suite-campaign-manager-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/optus-run-sms-campaign.md
- group: other
  title: ''
  type: Overlay
  url: overlays/optus-sms-suite-status-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/optus-check-service-health.md
- group: company
  title: ''
  type: Website
  url: https://www.optus.com.au/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sms.optus.com.au/docs/en/developer-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sms.optus.com.au/docs/en/developer-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sms.optus.com.au/docs/en/integrations/messaging-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://sms.optus.com.au/docs/en/developer-getting-started/
- group: start
  title: ''
  type: SignUp
  url: https://sms.optus.com.au/customer/online_signup
- group: start
  title: ''
  type: Login
  url: https://sms.optus.com.au/login
- group: operate
  title: ''
  type: Support
  url: https://www.optus.com.au/business/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://sms.optus.com.au/docs/en/support-centre/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optus.com.au/about/legal/standard-forms-agreement/business
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optus.com.au/about/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/optus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/optus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/optus-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/optus-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sms.optus.com.au/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/optus-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/optus-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/optus-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://sms.optus.com.au/docs/en/solution-sheets/safe-secure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/optus-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/optus-vdp-pro
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/optus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optus-domain-security.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/optus-sms-suite-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/optus-sms-suite-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/optus-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/optus-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/optus-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optus-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/optus-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/optus-packages.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optus
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Optus
created: '2026-07-25'
description: 'Optus (Singtel Optus Pty Limited) is Australia''s second-largest telecommunications carrier, wholly owned by Singapore''s Singtel and headquartered in Macquarie Park, Sydney. It runs a national mobile network reaching over 99% of the Australian population, alongside NBN and cable broadband, satellite capacity inherited from AUSSAT, enterprise and government connectivity, IoT/M2M services, and consumer media. Its API posture is split in two. The only genuinely public, self-serve developer surface Optus operates is The Optus SMS Suite — an enterprise messaging platform white-labelled from New Zealand''s Modica Group at sms.optus.com.au, which publishes open documentation, downloadable OpenAPI/Swagger definitions, a WSDL, delivery-receipt callbacks, and a free-trial signup. Everything else is partner-gated: the IoT Control Centre is a Cisco/Jasper platform behind a referral-coded starter kit, and Optus has no first-party network-API portal — developer.optus.com.au and api.optus.com.au
  resolve on Akamai but return HTTP 403 Access Denied. On network APIs Optus is a stated GSMA Open Gateway participant and an endorser of the Bridge Alliance API Exchange (BAEx), but as of this review no CAMARA API is callable from Optus directly; its route to developers runs through its parent Singtel''s Paragon-powered BAEx and Aduna, not through anything Optus publishes itself.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Optus
nav: Providers
network: true
overview: 'Optus publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Delete Multiple Lists API, Documentation API, Lists API, and 6 more. Tagged areas include Telecommunications, Australia, Mobile Network Operator, Messaging, and SMS.


  The Optus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Optus'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 36 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 51.9
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 53.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 62.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optus/refs/heads/main/screenshots/optus-2026-08-07T190818.png
security:
- kind: authentication
  name: Optus Authentication
  slug: optus-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Optus Domain Security
  slug: optus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Optus Vulnerability Disclosure
  slug: optus-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Optus Trust Center
  slug: optus-trust-center
  summary_line: ISO 27001, SOC 2, IRAP
slug: optus
tags:
- Telecommunications
- Australia
- Mobile Network Operator
- Messaging
- SMS
- MMS
- Two-Factor Authentication
- Network APIs
- CAMARA
- Open Gateway
- IoT
- 5G
- Broadband
- Satellite
- Enterprise
website: https://www.optus.com.au/
---
