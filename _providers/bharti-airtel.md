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
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Bharti Airtel Agentic Access
  operation_count: 68
  slug: bharti-airtel-agentic-access
  summary_line: 68 operations · 35 acting
api_count: 5
apis:
- description: The messaging half of Airtel IQ, Airtel's network-embedded CPaaS suite. Sends single, bulk, CSV-batch and content-moderated A2P SMS over Airtel's pan-India network, with TRAI DLT (Hyperledger-based di
  name: Airtel IQ SMS API
  slug: airtel-iq-sms-api
- description: 'The Call Detail Record (CDR) reporting surface of Airtel IQ. Returns detailed per-call records — time, date, duration, caller ID, destination number, status and call-recording URL — for voice traffic '
  name: Airtel IQ Reporting API
  slug: airtel-iq-reporting-api
- description: 'Airtel''s IoT/M2M connectivity-management API, published as a complete OpenAPI 3.0.1 catalogue of 43 operations across ten areas: account authorization, account details, inventory management, SIM lifec'
  name: Airtel IoT API
  slug: airtel-iot-api
- description: Airtel Locate is the operator's network-based device-location platform, letting enterprises track a device by MSISDN without relying on the device's GPS. Published as an OpenAPI 3.0.0 catalogue (versi
  name: Airtel Locate API
  slug: airtel-locate-api
- description: Airtel's original partner developer programme, launched in 2017 and now an unmaintained legacy portal (the site still carries a 2017 copyright). Its public documentation still describes real OAuth 2.0
  name: Airtel Smart API (legacy)
  slug: airtel-smart-api
artifact_total: 16
asyncapis:
- description: ''
  name: Bharti Airtel Webhooks
  slug: bharti-airtel-webhooks
collections:
- collection_type: open
  name: Airtel IoT
  slug: open-bharti-airtel-iot
- collection_type: open
  name: Airtel IQ API Documentation
  slug: open-bharti-airtel-iq-reporting
- collection_type: open
  name: Airtel IQ SMS Core APIs
  slug: open-bharti-airtel-iq-sms
- collection_type: open
  name: Locate API Catalog
  slug: open-bharti-airtel-locate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bharti-airtel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bharti-airtel-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bharti-airtel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bharti-airtel-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bharti-airtel-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bharti-airtel-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bharti-airtel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bharti-airtel-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bharti-airtel-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bharti-airtel-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bharti-airtel-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bharti-airtel-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bharti-airtel-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/bharti-airtel-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bharti-airtel-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bharti-airtel-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bharti-airtel-apis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-send-compliant-sms.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-locate-device-with-consent.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bharti-airtel-manage-iot-sim-lifecycle.md
- group: company
  title: ''
  type: Website
  url: https://www.airtel.in/
- group: docs
  title: ''
  type: Documentation
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/sms/overview
- group: docs
  title: ''
  type: APIReference
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/sms/sms-utility
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airtel.in/business/b2b/airtel-iq/api-docs/voice/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.airtel.in/
- group: start
  title: ''
  type: SignUp
  url: https://www.airtel.in/business/b2b/airtel-ccp/dashboard/#/signup
- group: start
  title: ''
  type: Console
  url: https://www.airtel.in/business/b2b/airtel-ccp/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://www.airtel.in/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.airtel.in/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.airtel.in/business/b2b/cpaas
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airtel.in/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airtel.in/mobile/terms-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airtel-business/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/airtelindia/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC62RQR1TkP_945zTN6Jwecg
- group: other
  title: ''
  type: Email
  url: mailto:iqsalessupport@airtel.com
created: '2026-07-25'
description: 'Bharti Airtel Limited is an Indian multinational telecommunications operator headquartered in New Delhi, and one of the two dominant mobile network operators in its home market of India alongside Reliance Jio. It runs mobile (2G/4G/5G), fixed broadband, DTH television, enterprise connectivity, data centre (Nxtra) and payments-bank businesses across India, South Asia and — through the separately listed Airtel Africa — fourteen African countries. In the telecom value chain Airtel is an access-network owner: it holds the spectrum, the SIM estate, the subscriber identity and the network signalling that the rest of the industry resells. Its API posture is split in two, and the split is the whole story. The connectivity-product side is genuinely API-native and publicly documented: Airtel IQ, the operator''s CPaaS suite, publishes open Swagger for its SMS and CDR reporting APIs and offers a self-serve trial account, while the Airtel IoT and Airtel Locate developer portals publish
  complete OpenAPI 3.0 catalogues (43 and 19 operations) as Redoc pages that need no login. The network-API side — the CAMARA and GSMA Open Gateway surface that defines this sector — is the opposite: Airtel is a GSMA Open Gateway signatory, a founding operator shareholder in Aduna (the Ericsson-led network-API joint venture), and has commercially launched a CAMARA SIM Swap API to Indian banks through a federated Jio/Vi/Airtel channel, yet it publishes no CAMARA endpoint, no CAMARA specification, no CIBA authorization surface and no network-API developer portal of its own. Developers reach Airtel''s network capabilities only through aggregators — Aduna, and Nokia''s Network as Code platform — never directly. Its own "Airtel API Marketplace" at developers.airtel.in is a login wall, and its original 2017 Smart API partner programme at openapi.airtel.in/smartapi survives as an unmaintained legacy portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: bharti-airtel-mcp.yml
  slug: bharti-airtel-mcpyml
modified: '2026-07-25'
name: Bharti Airtel
nav: Providers
network: true
overview: 'Bharti Airtel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Airtel IQ SMS API, Airtel IQ Reporting API, Airtel IoT API, and 1 more. Tagged areas include Telecommunications, India, Mobile Network Operator, Network APIs, and CAMARA.


  The Bharti Airtel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bharti Airtel''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, signup flow, developer console, and 30 more developer resources.'
random_paper: 128
scopes:
- name: Bharti Airtel Scopes
  scope_count: 4
  slug: bharti-airtel-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode/implicit
score:
  band: developing
  composite: 50.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.0
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
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
    score: 66.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bharti-airtel/refs/heads/main/screenshots/bharti-airtel-2026-08-07T162406.png
security:
- kind: authentication
  name: Bharti Airtel Authentication
  slug: bharti-airtel-authentication
  summary_line: http-basic/oauth2 · 4 schemes
- kind: domain-security
  name: Bharti Airtel Domain Security
  slug: bharti-airtel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bharti Airtel Vulnerability Disclosure
  slug: bharti-airtel-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: bharti-airtel
tags:
- Telecommunications
- India
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- CPaaS
- Messaging
- SMS
- RCS
- Voice
- IoT
- M2M
- Device Location
- Broadband
- 5G
- Identity Verification
- Carrier Billing
- Consent Management
website: https://www.airtel.in/
---
