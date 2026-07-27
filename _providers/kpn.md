---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 70.2
  scored_at: '2026-07-27'
api_count: 38
apis:
- description: With KPN Number Verify, you can quickly check whether the mobile number someone provides is the same as their SIM card.
  name: KPN Number Verify API
  slug: kpn-number-verify
- description: The SIM swap API provides a programmable interface for developers and other users (capabilities consumers) to request the last date of a SIM swap performed on the mobile line, or, to check whether a S
  name: KPN SIM Swap API (Account Takeover Protection)
  slug: kpn-sim-swap
- description: Seamlessly check and verify an identity.
  name: KPN Match API
  slug: kpn-match
- description: Send SMS through the KPN network.
  name: KPN SMS API
  slug: kpn-sms
- description: This API is designed to inform users about the response schema they will receive on their webhook when an SMS message is sent to their virtual number. The API provides details of the message format th
  name: KPN SMS Inbound API
  slug: kpn-sms-inbound
- description: MobileServicesManagement APIs ---
  name: KPN Mobile Services Management API
  slug: kpn-mobile-services-management
- description: A collection of crates for federated identity and access management
  name: KPN FIAM API
  slug: kpn-fiam
- description: FIAM – Eneco Data Products
  name: KPN FIAM Eneco Data Products API
  slug: kpn-fiam-eneco-data-products
- description: This API allows you to check the disturbance of the internet and the technology at an address. The API takes the postcode, house number and house extension, sends the request to the backend to retriev
  name: KPN Disturbance Check API
  slug: kpn-disturbance-check
- description: This API allows you to check the speed of the internet and the technology at an address. The API takes the postcode, house number and house extension, sends the request to the backend to retrieve real
  name: KPN Internet Speed Check API
  slug: kpn-internet-speed-check
- description: The High-Level Design FTTx API supports Fiber to the Home (FTTH) engineering jobs. It allows you to calculate the required work and cost for Fiber rollout in a provided region. Run the endpoints in th
  name: KPN High Level Design FttX API
  slug: kpn-high-level-design-ftth
- description: KPN’s Low Power Long Range (LoRa) network service compliments existing 2G, 3G, 4G and LTE-M networks. It is based on the LoRaWAN protocol for Internet of Things (IoT).
  name: KPN LoRa Device Management API
  slug: kpn-lora-device-management
- description: 'The SD-LAN SD-WAN Network View API is a modern REST API based on the OpenAPI specification. The Network View API gives users read rights to retrieve information from the `Network View API` resources. '
  name: KPN SD-LAN / SD-WAN Network View API
  slug: kpn-sd-lan-sd-wan-network-view
- description: This is Customer Connect API for KPN ServiceNow-Green Tickets. With this API KPN SN Green will be able to create new, or update existing tickets. This document provides the API specification.
  name: KPN ServiceNow Connect API
  slug: kpn-servicenow-connect
- description: 'Cisco Identity Services Engine (ISE) network access control resources exposed through the KPN API gateway, covering endpoints, endpoint groups, identity groups and internal users. The spec advertises '
  name: KPN ISE API
  slug: kpn-ise
- description: 'This API provides you different TV related content services. Currently there are 3 main calls with some of them have successive calls. The data provided consists of JSON formatted text mainly related '
  name: KPN TV Guide API
  slug: kpn-tv-guide
- description: When KPN delivers a webhook to your endpoint, signing keys are to know the request genuinely came from KPN and wasn't tampered with in transit. KPN signs every outbound webhook payload using HMAC-SHA2
  name: KPN Webhook Signing Keys API
  slug: kpn-webhook-signing-keys
- description: 'KPN delivers outbound webhook notifications — such as SMS delivery reports — to the endpoints you configure. This API lets you control two things about those deliveries: the URL they are sent to, and '
  name: KPN Webhook Privacy Config Manager API
  slug: kpn-webhook-privacy-config-manager
- description: 'KPN Wholesale Broadband Access (WBA) is a KPN Wholesale product offering copper and fiber access to wholesale customers. WBA has the following APIs available: * Functional Product Information: The Fun'
  name: KPN Wholesale Broadband Access (WBA) API
  slug: kpn-wholesale-wba
- description: 'KPN Wholesale Broadband Access (WBA) is a KPN Wholesale product offering copper and fiber access to wholesale customers. WBA has the following APIs available: * Functional Product Information: The Fun'
  name: KPN Wholesale Broadband Access FPI/CIP API
  slug: kpn-wholesale-broadband-access-fpi-cip
- description: The Knowledge Management API allows you to organize your organization's information with knowledge management software.
  name: Polly.help Knowledge Management API
  slug: pollyhelp-knowledge-management
- description: Xdroid Speech To Text API provides a seamless audio transcription service.
  name: Xdroid Speech to Text API
  slug: xdroid-speech-to-text
- description: This API enables a secure communication between your agent/bot desktop and the client website/mobile app.
  name: Parley Secure Messenger API
  slug: parley-secure-messenger
- description: The SocialMediaWebcare API allows you to organise and manage your inbound and outbound social media channels traffic.
  name: Tracebuzz Social Media Webcare API
  slug: tracebuzz-social-media-webcare
- description: WeSeeDo Direct API allows you to set up a video communication channel between people by sending an SMS with a link to the meeting.
  name: WeSeeDo Direct API
  slug: weseedo-direct
- description: The WeSeeDo Personal API allows video calling in the right way and distinguishes itself in human contact, ease of use and safety.
  name: WeSeeDo Personal API
  slug: weseedo-personal
- description: Encapsulates multiple APIs to interact with our various channels such as WhatsApp Business, SMS, MMS, Viber, Facebook Messenger, etc. The API normalises information across all channels to abstracted t
  name: Vonage Messages API (via KPN)
  slug: vonage-messages
- description: 'The Voice API lets you create outboud calls, control in progress calls and get information about current and historical calls. The API is divided in 2 big resources blocks: - Application: Manage appli'
  name: Vonage Voice API (via KPN)
  slug: vonage-voice
- description: 'The Numbers API lets you manage your numbers and buy new virtual numbers for use with Vonage''s APIs. ## Prerequirement: Your project has to be in the production environment in order to use of this API'
  name: Vonage Phone Numbers API (via KPN)
  slug: vonage-phone-numbers
- description: Vonage's Number Insight API provides details about the validity, reachability and roaming status of a phone number, as well as giving you details on how to format the number properly in your applicati
  name: Vonage Number Insight API (via KPN)
  slug: vonage-number-insight
- description: Vonage's SMS API allows you to send and receive text messages to users around the globe through simple RESTful APIs. * Programmatically send and receive high volume of SMS anywhere in the world. * Bui
  name: Vonage SMS API (via KPN)
  slug: vonage-sms
- description: Verify API is to Verify if a phone number is valid, reachable, and accessible by the user. Verification message can be customerized. Verify API provides the following services - **Verify Request** - G
  name: Vonage Verify API (via KPN)
  slug: vonage-verify
- description: This REST API exposes actions that help your apps to interact with APIdaze’s Telco platform in mulitples ways. You can set the URL from where Apidaze fetchs XML instructions to run on Apidaze platform
  name: Apidaze Voice CPaaS API (via KPN)
  slug: apidaze-voice
- description: 'This API offers three functionalities: - User management - Emailing User management can be used to add, get and modify user information. This can be done be a user with customer admin rights, without '
  name: Registered Email API (via KPN)
  slug: registered-email
- description: KPN Grip is a KPN identity and access management solution that acts as a central identity hub, letting developers integrate user registration, authentication and authorization (SAML 2.0, OpenID Connec
  name: KPN GRIP API
  slug: kpn-grip
- description: KPN PiM ID generates tamper-proof, company-specific encrypted QR codes from validated customer data (POST /image on https://api-prd.kpn.com/kpn/qrcodegenerator). The codes are embedded in surfaces suc
  name: KPN PIM ID API
  slug: kpn-pim-id
- description: Send and schedule bulk SMS campaigns over the KPN network. Documented on the KPN Developer portal; no public OpenAPI definition was found for this product on KPN's SwaggerHub organisation as of the ha
  name: KPN SMS Campaigns API
  slug: kpn-sms-campaigns
- description: Converts inbound email into SMS messages delivered over the KPN network. Documented on the KPN Developer portal; no public OpenAPI definition was found for this product on KPN's SwaggerHub organisatio
  name: KPN Email-to-SMS API
  slug: kpn-email-to-sms
artifact_total: 45
asyncapis:
- description: ''
  name: Kpn Webhooks
  slug: kpn-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kpn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kpn-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kpn-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kpn-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kpn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kpn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kpn.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kpn.com/page/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.kpn.com/dashboard/register
- group: start
  title: ''
  type: Login
  url: https://developer.kpn.com/dashboard/login
- group: other
  title: ''
  type: Products
  url: https://developer.kpn.com/products
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.kpn.com/tutorials
- group: company
  title: ''
  type: Blog
  url: https://developer.kpn.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.kpn.com/status
- group: operate
  title: ''
  type: Support
  url: https://developer.kpn.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.kpn.com/page/legal
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://developer.kpn.com/page/responsible-disclosure
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://app.swaggerhub.com/search?owner=kpn
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kpndeveloper
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kpn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kpn
- group: other
  title: ''
  type: Wholesale
  url: https://www.kpn-wholesale.com/
- group: other
  title: ''
  type: Standard
  url: https://github.com/camaraproject/
- group: other
  title: ''
  type: Standard
  url: https://coin.nl/camara
- group: build
  title: ''
  type: Packages
  url: packages/kpn-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kpn-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kpn-security.txt
- group: auth
  title: ''
  type: Security
  url: https://developer.kpn.com/page/responsible-disclosure
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kpn-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kpn-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/kpn-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kpn-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kpn-sms-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kpn-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.kpn.com/documentation-response-headers
- group: design
  title: ''
  type: Conventions
  url: conventions/kpn-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kpn-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kpn-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kpn-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kpn-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kpn-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://app.swaggerhub.com/search?owner=kpn
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kpn.com/algemeen/missie-en-privacy-statement/privacy-statement.htm
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.kpn.com/algemeen/cookies.htm
created: '2026-07-25'
description: 'Koninklijke KPN N.V. is the incumbent telecommunications and IT provider of the Netherlands, operating the country''s national fixed (copper and fibre) and mobile networks and selling telephony, broadband, television, IoT connectivity and managed IT services to consumers, businesses and — through KPN Wholesale — to other operators. In the telecom API value chain KPN sits on the network-operator side, but it is a conspicuous exception to the carrier norm: rather than routing developers exclusively through aggregators, KPN runs a genuine self-serve developer portal at developer.kpn.com where anyone can register a free account, get a client ID and secret, test in a sandbox at no cost, and see per-transaction pricing, then upgrade to production via a KRN company number or an iDIN identity check. Thirty-four OpenAPI/Swagger definitions are published anonymously downloadable under KPN''s public SwaggerHub organisation, all fronted by an Apigee-style gateway at api-prd.kpn.com with
  OAuth 2.0 client-credentials. KPN is listed in the official CAMARA landscape as an operator and, with Odido and Vodafone under the COIN association and GSMA Open Gateway, launched CAMARA-standard fraud-prevention APIs for the Dutch market in October 2025; its SIM Swap definition points explicitly at github.com/camaraproject as its product documentation. KPN is not an Aduna shareholder and does not reach developers through that JV. Notably, KPN also resells Vonage and Apidaze CPaaS products through its own portal — the aggregator layer appearing inside the carrier''s own catalogue rather than the other way round.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: kpn-mcp.yml
  slug: kpn-mcpyml
modified: '2026-07-25'
name: KPN
nav: Providers
network: true
overview: 'KPN publishes 34 APIs on the [APIs.io](https://apis.io/) network, including Number Verify API, SIM Swap API (Account Takeover Protection), Match API, and 31 more. Tagged areas include Telecommunications, Netherlands, Mobile Network Operator, Broadband, and Network APIs.


  The KPN catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KPN''s developer surface includes authentication, documentation, getting-started guide, signup flow, engineering blog, support, changelog, and 38 more developer resources.'
random_paper: 57
rate_limits:
- limit_count: 3
  name: Kpn Rate Limits
  slug: kpn-rate-limits
scopes:
- name: Kpn Scopes
  scope_count: 0
  slug: kpn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 59.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.1
    developer_ergonomics: 78.3
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 94.7
  previous_composite: 59.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Kpn Authentication
  slug: kpn-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Kpn Domain Security
  slug: kpn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kpn Vulnerability Disclosure
  slug: kpn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kpn
tags:
- Telecommunications
- Netherlands
- Mobile Network Operator
- Broadband
- Network APIs
- CAMARA
- Open Gateway
- SIM Swap
- Identity Verification
- Messaging
- SMS
- Voice
- IoT
- LoRaWAN
- Fiber
- Wholesale
- 5G
- Europe
website: https://www.kpn.com/
---
