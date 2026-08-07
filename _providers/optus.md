---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Optus Agentic Access
  operation_count: 15
  slug: optus-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 10
apis:
- description: JSON REST API for sending single and bulk SMS from The Optus SMS Suite, including scheduled sends, broadcast to a list, and retrieval of a submitted message by 64-bit message ID. Authenticated with HT
  name: Optus SMS Suite REST API v1
  slug: optus-sms-suite-rest-api-v1
- description: High-volume asynchronous SMS API using UUID-based message tracking, mandatory delivery-receipt (DLR) callbacks, and advanced scheduling. Requests are authenticated with HTTP Basic credentials passed i
  name: Optus SMS Suite SMS Gateway REST API v2
  slug: optus-sms-suite-rest-api-v2
- description: REST API v1 for programmatic control of SMS marketing campaigns — creating and managing recipient lists, message templates, scheduled campaigns, and per-campaign reporting, scoped to a named SMS Suite
  name: Optus SMS Suite Campaign Manager API
  slug: optus-sms-suite-campaign-manager-api
- description: 'Unauthenticated status API returning near real-time availability for individual Optus SMS Suite services (rest, smpp, and others), polled every 60 seconds from an external, geographically distributed '
  name: Optus SMS Suite Health Monitoring API
  slug: optus-sms-suite-health-monitoring-api
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
artifact_total: 17
asyncapis:
- description: Derived event description for the callbacks The Optus SMS Suite POSTs to subscriber-hosted URLs. Optus publishes NO AsyncAPI document; this file was derived by API Evangelist from two sources that are
  name: The Optus SMS Suite Callback Surface
  slug: optus-sms-suite-asyncapi
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: optus-mcp.yml
  slug: optus-mcpyml
modified: '2026-07-25'
name: Optus
nav: Providers
network: true
overview: 'Optus publishes 4 APIs on the [APIs.io](https://apis.io/) network, including SMS Suite REST API v1, SMS Suite SMS Gateway REST API v2, SMS Suite Campaign Manager API, and 1 more. Tagged areas include Telecommunications, Australia, Mobile Network Operator, Messaging, and SMS.


  The Optus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Optus'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 28 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 54.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.1
    developer_ergonomics: 53.8
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 57.9
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 68.1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
