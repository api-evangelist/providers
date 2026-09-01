---
access_model:
  confidence: high
  label: Paid · Contract required for organisational access; free self-serve for your own meter data via Bright
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://data.glowforindustry.com/
  - https://docs.glowmarkt.com/GlowmarktAPIDataRetrievalDocumentationIndividualUserForBright.pdf
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
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
  score: 30.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 45
  human_in_the_loop: 4
  name: Hildebrand Agentic Access
  operation_count: 106
  slug: hildebrand-agentic-access
  summary_line: 106 operations · 45 acting · 4 human-in-the-loop
api_count: 5
apis:
- description: The Account API from Hildebrand — 8 operation(s) for account.
  name: Hildebrand Account API
  slug: hildebrand-account-api
- description: The Account Profile API from Hildebrand — 2 operation(s) for account profile.
  name: Hildebrand Account Profile API
  slug: hildebrand-account-profile-api
- description: The Account Session API from Hildebrand — 1 operation(s) for account session.
  name: Hildebrand Account Session API
  slug: hildebrand-account-session-api
- description: The accountsession API from Hildebrand — 1 operation(s) for accountsession.
  name: Hildebrand Accountsession API
  slug: hildebrand-accountsession-api
- description: An application can send an alert to a customer across multiple channels (email, push, inbox) which will convey some type of specific message (defined by the alert type).
  name: Hildebrand Alert API
  slug: hildebrand-alert-api
- description: The definition of an alert, what functionality the alert represents. It is an identifier which amongst other elements will point us to the correct template. An alert type belongs to an application.
  name: Hildebrand Alerttype API
  slug: hildebrand-alerttype-api
- description: The Auth API from Hildebrand — 5 operation(s) for auth.
  name: Hildebrand Auth API
  slug: hildebrand-auth-api
- description: The Device API from Hildebrand — 5 operation(s) for device.
  name: Hildebrand Device API
  slug: hildebrand-device-api
- description: The Device Meter Point DCC inventory API from Hildebrand — 3 operation(s) for device meter point dcc inventory.
  name: Hildebrand Device Meter Point DCC inventory API
  slug: hildebrand-device-meter-point-dcc-inventory-api
- description: The DeviceType API from Hildebrand — 2 operation(s) for devicetype.
  name: Hildebrand Device Type API
  slug: hildebrand-devicetype-api
- description: The discover API from Hildebrand — 1 operation(s) for discover.
  name: Hildebrand Discover API
  slug: hildebrand-discover-api
- description: The Meter Point Consent & Verification API from Hildebrand — 5 operation(s) for meter point consent & verification.
  name: Hildebrand Meter Point Consent & Verification API
  slug: hildebrand-meter-point-consent-verification-api
- description: When an application triggeers an alert, for each channel of communication a notification is created. This enables the system to monitor seperately whant happens in each channel.
  name: Hildebrand Notification API
  slug: hildebrand-notification-api
- description: The OAuth API from Hildebrand — 2 operation(s) for oauth.
  name: Hildebrand O Auth API
  slug: hildebrand-oauth-api
- description: A Resource is a representation of data collected from a physical device, like sensor readings, or changes in an actuating device state etc.
  name: Hildebrand Resource API
  slug: hildebrand-resource-api
- description: A Resource Type defines the storage structure of the resources supported by the Glow Platform.
  name: Hildebrand Resource Type API
  slug: hildebrand-resource-type-api
- description: The template of the message that is being sent; it can be passed through as HTML or JSON. Each template has an alert type, is specific to a single channel of communication and a culrture code.
  name: Hildebrand Template API
  slug: hildebrand-template-api
- description: The User API from Hildebrand — 6 operation(s) for user.
  name: Hildebrand User API
  slug: hildebrand-user-api
- description: A Virtual Entity is an instance of the Virtual Entity Type and is tied to an owner as well as an applicationId. In order to create a Virtual Entity a user must have all the required resources.
  name: Hildebrand Virtual Entity API
  slug: hildebrand-virtual-entity-api
- description: A Virtual Entity's metadata can be used to save information that will facilitate the virtual representation of the entity. This is typically attribute data that does not change in time.
  name: Hildebrand Virtual Entity's Metadata API
  slug: hildebrand-virtual-entity-s-metadata-api
- description: APIs that return an overview of the Virtual Entities an application has (administrative API).
  name: Hildebrand Virtual Entity Statistics API
  slug: hildebrand-virtual-entity-statistics-api
- description: Entity that belongs and is managed by an application and contains the definition and combination of the Resource Types that are required to create a Virtual Entity.
  name: Hildebrand Virtual Entity Type API
  slug: hildebrand-virtual-entity-type-api
artifact_total: 33
asyncapis:
- description: ''
  name: Hildebrand Event Surface
  slug: hildebrand-event-surface
collections:
- collection_type: open
  name: Device Management System
  slug: open-hildebrand-glowmarkt-device-management-system-swagger
- collection_type: open
  name: Notification System
  slug: open-hildebrand-glowmarkt-notification-system-swagger
- collection_type: open
  name: Resource System
  slug: open-hildebrand-glowmarkt-resource-system-swagger
- collection_type: open
  name: Glowmarkt User System
  slug: open-hildebrand-glowmarkt-user-system-swagger
- collection_type: open
  name: Virtual Entity System
  slug: open-hildebrand-glowmarkt-virtual-entity-system-swagger
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hildebrand-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hildebrand-glowmarkt-user-system-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hildebrand-glowmarkt-resource-system-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hildebrand-glowmarkt-virtual-entity-system-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hildebrand-glowmarkt-device-management-system-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/hildebrand-glowmarkt-notification-system-overlay.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.glowmarkt.com/GlowmarktAPIDataRetrievalDocumentationIndividualUserForBright.pdf
- group: company
  title: ''
  type: Blog
  url: https://data.glowforindustry.com/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HildebrandTechnology
- group: auth
  title: ''
  type: Compliance
  url: https://www.hildebrand.co.uk/about
- group: design
  title: ''
  type: Conformance
  url: conformance/hildebrand-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hildebrand-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hildebrand-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hildebrand-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hildebrand-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/hildebrand-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hildebrand-plans.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hildebrand-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hildebrand-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hildebrand-event-surface.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hildebrand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hildebrand-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hildebrand-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hildebrand.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://api.glowmarkt.com/api-docs/v0-1/resourcesys/
- group: docs
  title: ''
  type: APIReference
  url: https://api.glowmarkt.com/api-docs/v0-1/usersys/usertypes/
- group: start
  title: ''
  type: SignUp
  url: https://data.glowforindustry.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://data.glowforindustry.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://www.hildebrand.co.uk/contact-us
- group: operate
  title: ''
  type: Forum
  url: https://forum.glowmarkt.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hildebrand/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hildebrand.co.uk/privacy-policy
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-27'
description: 'Hildebrand Technology Limited is a London-based energy data company and, since 2019, the United Kingdom''s first independent DCC Other User with a direct connection to the Smart Data Communications Company network. It sits between Britain''s mandated smart-metering infrastructure and the applications built on top of it: it makes Glow hardware (CADs, in-home displays, sub-meters, temperature sensors), ingests and stores smart-meter reads at scale, and republishes them through the Glowmarkt Platform APIs, the consumer Bright app, and the commercial Glow Data Service. Its API posture is an honest reflection of the British market seam — Britain mandated the metering INFRASTRUCTURE, not a consumer data right, so there is no Consumer Data Right or Green Button obligation on Hildebrand and no standards-conformant data-sharing surface to point at. What exists instead is a proprietary but genuinely well-documented platform: five public Swagger 2.0 definitions are served anonymously
  from api.glowmarkt.com/api-docs, and any individual who installs Bright, creates an account and passes meter-point verification can call the same production API for their own household data with a published applicationId. Third-party organisational access to other people''s data is the closed half — it runs through Glow Data Service on a signed contract from GBP 595/month per MPxN, with consumer verification and consent captured per meter point. Hildebrand publishes no open grid or market data of any kind: every documented endpoint returns HTTP 400 without an applicationId header, so this is a closed-market-data, consent-gated-consumer-data provider.'
image: https://www.hildebrand.co.uk/images/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Hildebrand MCP Server
  slug: hildebrand-mcp-server
modified: '2026-07-27'
name: Hildebrand
nav: Providers
network: true
overview: 'Hildebrand publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account Profile API, Account Session API, and 19 more. Tagged areas include Energy, United Kingdom, Utilities, Electricity, and Gas.


  The Hildebrand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hildebrand''s developer surface includes getting-started guide, engineering blog, authentication, documentation, API reference, signup flow, pricing, and 27 more developer resources.'
plans:
- name: Hildebrand Plans
  plan_count: 3
  slug: hildebrand-plans
random_paper: 8
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 61.8
    developer_ergonomics: 49.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 52.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hildebrand/refs/heads/main/screenshots/hildebrand-2026-08-07T170207.png
security:
- kind: authentication
  name: Hildebrand Authentication
  slug: hildebrand-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Hildebrand Domain Security
  slug: hildebrand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hildebrand
tags:
- Energy
- United Kingdom
- Utilities
- Electricity
- Gas
- Smart Metering
- Energy Data
- Demand Response
- IoT
- Metering
website: https://www.hildebrand.co.uk/
---
