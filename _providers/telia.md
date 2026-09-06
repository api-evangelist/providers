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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Telia Agentic Access
  operation_count: 2
  slug: telia-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: 'LSO Sonata Geographic Address API allows a buyer to retrieve a geographic address from the seller database by address id and to validate geographic address data. Designed using TM Forum TMF673 as its '
  name: Telia LSO Sonata Geographic Address Management API
  slug: telia-lso-sonata-geographic-address-management-api
- description: Determines whether it is feasible for the seller to deliver a particular product to a particular geographic location, and manages create POQ, retrieve POQ list and retrieve POQ by identifier operation
  name: Telia LSO Sonata Product Offering Qualification API
  slug: telia-lso-sonata-product-offering-qualification-api
- description: Manages quote request and completion between seller and buyer for Telia operator customers and selected B2O products. Designed using TM Forum TMF648 as its template; firm quotes are handled today with
  name: Telia LSO Sonata Quote Management API
  slug: telia-lso-sonata-quote-management-api
- description: Creates product orders covering new, change, disconnect and suspend scenarios, with the current version focused on new order creation. Designed using TM Forum TMF622 Product Order as its template. Doc
  name: Telia LSO Sonata Order Management API
  slug: telia-lso-sonata-order-management-api
- description: Buyer-registered listener API for quote and order notifications — state change, create quote, attribute change and BAFO quotes — pushed from seller to buyer. This is the event surface of the LSO Sonat
  name: Telia LSO Sonata Notification API
  slug: telia-lso-sonata-notification-api
- description: 'CAMARA Quality on Demand (QoD) API listed on Telia''s CAMARA portal, allowing an application to request a higher-quality network connection. Named and described on the anonymously readable portal home '
  name: Telia CAMARA Quality on Demand API
  slug: telia-camara-quality-on-demand-api
- description: CAMARA Device Location API listed on Telia's CAMARA portal, allowing a caller to request the area in which a user device is located. Named on the public portal home page only; the anonymous API catalo
  name: Telia CAMARA Device Location API
  slug: telia-camara-device-location-api
- description: Ngmlc_Location_ProvideLocation service operation, invoked by a service consumer towards the ENL to request the geodetic location of a single device or to subscribe to tracking of one device. This is a
  name: Telia NGMLC Location API
  slug: telia-ngmlc-location-api
- description: A request mapper proxying requests to Telia Finland's internal Catalogue Service API, deliberately limiting and restricting the functionality present in the underlying catalogue service. Named and des
  name: Telia Finland Public Catalogue Service API
  slug: telia-finland-public-catalogue-service-api
- description: Manages business mobile subscriptions for Telia Finland customers — list subscription, get subscription, update subscription information, deactivate, reactivate and terminate. Named and described on t
  name: Telia Finland Mobile Subscription API
  slug: telia-finland-mobile-subscription-api
- description: Exposes available packages and products and allows ordering them for both new and existing mobile subscriptions at Telia Finland. Named and described on the public portal home page; specification behi
  name: Telia Finland Mobile Subscription Order Service API
  slug: telia-finland-mobile-subscription-order-service-api
- description: JSON REST API for submitting mobile-terminated SMS through the Telia Company Bulk Messaging Platform, with a Submit SMS message operation (POST ~/messages) and a Submit SMS content operation for custo
  name: Telia Bulk Messaging SMS REST API
  slug: telia-bulk-messaging-sms-rest-api
- description: The webhook half of Telia's Bulk Messaging REST surface. Customers must implement a Receive SMS (mobile originated) operation and a Receive delivery report (DLR) operation to accept callbacks pushed b
  name: Telia Bulk Messaging SMS Callback API
  slug: telia-bulk-messaging-sms-callback-api
- description: SMPP v3.4-style binary protocol interface into the Telia Company Bulk Messaging Platform, reached over TLS 1.2 or better at smpp.messaging.teliacompany.com port 3550 with SNI required. Supports bind_t
  name: Telia Bulk Messaging SMPP API
  slug: telia-bulk-messaging-smpp-api
- description: Bidirectional streaming gRPC service over HTTP/2 that forwards copies of the audio streams in Telia ACE contact-centre voice calls to a customer-implemented receiver, for transcription, summarisation,
  name: Telia ACE Audio Stream Forwarding API
  slug: telia-ace-audio-stream-forwarding-api
- description: Telia Tunnistus is Telia Finland's identification broker service — an OpenID Connect and OAuth 2.0 identity provider that brokers Finnish strong electronic identification. The OpenID discovery documen
  name: Telia Tunnistus Identification Broker
  slug: telia-tunnistus-identification-broker
- description: The REST API behind Telia ACE Knowledge (formerly Humany), the self-service knowledge and contact-deflection product inside the Telia ACE contact-centre suite. Telia documents it openly on GitHub — no
  name: Telia ACE Knowledge REST API
  slug: telia-ace-knowledge-rest-api
- description: The outbound webhook surface of Telia ACE Knowledge. A contact method of type Web service forwards an end user's form submission and the current ACE Knowledge parameter context to an external HTTP end
  name: Telia ACE Knowledge Contact Method WebHook
  slug: telia-ace-knowledge-contact-method-webhook
- description: Client-side and server-side REST interface that lets an end user communicate with a Telia ACE contact centre from the customer's own website. Telia publishes it in two versions — a Client version call
  name: Telia ACE Web API
  slug: telia-ace-web-api
- description: Integration API between the Telia ACE contact-centre platform and a customer's CRM system, used to drive agent-side integration such as surfacing and updating customer records against live interaction
  name: Telia ACE Agent API
  slug: telia-ace-agent-api
- description: Work-item management API for the Telia ACE contact centre, covering prioritisation, queue management and forwarding of tasks across the platform. Named and described on Telia's ACE marketplace; no spe
  name: Telia ACE Workitem API
  slug: telia-ace-workitem-api
- description: Screen-pop integration API for Telia ACE that automatically opens the matching customer profile in the agent's business system when an interaction arrives, which Telia states saves 10 to 20 seconds pe
  name: Telia ACE Screen Pop API
  slug: telia-ace-screen-pop-api
- description: 'Export API against Telia ACE Interaction View that allows content and data from recorded contact-centre interactions to be exported to external systems for analytics, quality management or archiving. '
  name: Telia ACE Interaction View API
  slug: telia-ace-interaction-view-api
- baseURL: https://api-garden.teliacompany.com/v1/api/mef/geographicSiteManagement
  baseurl_source: declared
  description: Retrieves a list of geographic sites based on the provided site id or other fields.
  name: Telia Company List Geographic Site API
  slug: telia-listgeographicsite-api
- baseURL: https://api-garden.teliacompany.com/v1/api/mef/geographicSiteManagement
  baseurl_source: declared
  description: Retrieves detailed information for a specific geographic site using its ID.
  name: Telia Company Retrieve Geographic Site API
  slug: telia-retrievegeographicsite-api
artifact_total: 32
asyncapis:
- description: ''
  name: Telia Webhooks
  slug: telia-webhooks
collections:
- collection_type: open
  name: B2X-Global-SiteManagement-API-v1
  slug: open-telia-lso-sonata-site-management
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/telia-oss/ace-audio-stream-forwarding-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/telia-oss/ace-audio-stream-forwarding-api/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/telia-oss/ace-audio-stream-forwarding-api/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/telia-lso-site-lookup.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/telia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/telia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/telia-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/telia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telia-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/telia-cli.yml
- group: design
  title: ''
  type: Components
  url: components/telia-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telia-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/telia-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/telia-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telia-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/telia-lso-sonata-site-management-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/telia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telia-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.telia.se/support/driftinformation-mobilt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/telia-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telia-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telia-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telia-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telia-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: proto/telia-ace-audio-stream-forwarding-v1.proto
- group: company
  title: ''
  type: Website
  url: https://www.teliacompany.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.teliacompany.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.teliacompany.io/
- group: start
  title: ''
  type: APIPortal
  url: https://camara.teliacompany.com/
- group: start
  title: ''
  type: APIPortal
  url: https://lso.teliacompany.com/
- group: start
  title: ''
  type: APIPortal
  url: https://developer.telia.fi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/telia-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telia-company
- group: operate
  title: ''
  type: Support
  url: mailto:camara@teliacompany.com
- group: operate
  title: ''
  type: Support
  url: mailto:mef-lso.team@teliacompanyspace.onmicrosoft.com
- group: start
  title: ''
  type: GettingStarted
  url: https://lso.teliacompany.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://lso.teliacompany.com/register
- group: company
  title: ''
  type: Blog
  url: https://ace-showcase.com/blog/
- group: docs
  title: ''
  type: APIReference
  url: https://cdn.messaging.teliacompany.com/documents/developer/index.html
created: '2026-07-25'
description: Telia Company is the Nordic and Baltic telecommunications group headquartered in Solna, Sweden, operating mobile and fixed networks in Sweden, Finland, Norway, Denmark, Lithuania, Latvia and Estonia, plus a global carrier and IoT business. As a mobile network operator it sits on the connectivity side of the telecom value chain rather than the developer-facing side, and its API posture reflects that split. Telia runs a real first-party developer hub at developer.teliacompany.io that fronts exactly two programmes — LSO Sonata (MEF/Mplify and TM Forum derived wholesale ordering APIs) and CAMARA (GSMA Open Gateway network APIs) — but both catalogs sit on Apigee portals that require an existing commercial agreement with Telia, a whitelisted corporate email domain and manual support approval before any specification or credential is issued. Only one OpenAPI definition is downloadable anonymously across the whole estate. Its CAMARA portal names Quality on Demand and Device Location
  but publishes nothing callable without login, and Telia reaches network-API developers mainly through Nokia's Network as Code aggregator platform rather than directly. The genuinely open surface is a public Bulk Messaging implementation guide covering an SMPP endpoint and an SMS REST API, and a gRPC audio-forwarding contract for its Telia ACE contact-centre product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Telia Company
nav: Providers
network: true
overview: 'Telia Company publishes 2 APIs on the [APIs.io](https://apis.io/) network: List Geographic Site API and Retrieve Geographic Site API. Tagged areas include Telecommunications, Sweden, Nordics, Baltics, and Mobile Network Operator.


  The Telia Company catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telia Company''s developer surface includes authentication, CLI, changelog, sandbox, documentation, support, getting-started guide, and 37 more developer resources.'
random_paper: 2
scopes:
- name: Telia Scopes
  scope_count: 2
  slug: telia-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 51.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 62.4
    developer_ergonomics: 67.3
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 81.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telia/refs/heads/main/screenshots/telia-2026-08-17T082306.png
security:
- kind: authentication
  name: Telia Authentication
  slug: telia-authentication
  summary_line: oauth2/http-basic/mutualTLS/openIdConnect/ip-allowlist/smpp-bind · 8 schemes
- kind: domain-security
  name: Telia Domain Security
  slug: telia-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Telia Vulnerability Disclosure
  slug: telia-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: telia
tags:
- Telecommunications
- Sweden
- Nordics
- Baltics
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- Messaging
- SMS
- SMPP
- IoT
- 5G
- Broadband
- Identity Verification
- BSS
- OSS
- TM Forum
- MEF
- Standards
website: https://www.teliacompany.com/
---
