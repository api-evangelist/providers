---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 39
  human_in_the_loop: 1
  name: Camara Project Agentic Access
  operation_count: 49
  slug: camara-project-agentic-access
  summary_line: 49 operations · 39 acting · 1 human-in-the-loop
api_count: 30
apis:
- description: Operations to verify the age of a user.
  name: CAMARA Project Age Verification API
  slug: camara-project-age-verification-api
- description: Provides information on Call Forwarding settings for the provided phone number (PhoneNumber).
  name: CAMARA Project Call Forwarding information retrieval API
  slug: camara-project-call-forwarding-information-retrieval-api
- description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: CAMARA Project Check Device Swap API
  slug: camara-project-check-device-swap-api
- description: The Check SIM swap API from CAMARA Project — 1 operation(s) for check sim swap.
  name: CAMARA Project Check SIM swap API
  slug: camara-project-check-sim-swap-api
- description: Operations to get the network type device is connected to
  name: CAMARA Project Connected Network Type API
  slug: camara-project-connected-network-type-api
- description: Operations to get the current reachability status of a device
  name: CAMARA Project Device reachability status API
  slug: camara-project-device-reachability-status-api
- description: Find the closest Edge Cloud Zone to the user device.
  name: CAMARA Project Discovery API
  slug: camara-project-discovery-api
- description: Operations to provide information related to a customer identity stored the account data bound to the customer's phone number.
  name: CAMARA Project Fill-in API
  slug: camara-project-fill-in-api
- description: Operations to manage event subscriptions on geofencing events for leaving and entering an area.
  name: CAMARA Project Geofencing subscriptions API
  slug: camara-project-geofencing-subscriptions-api
- description: QoD control operations for home devices
  name: CAMARA Project Home Devices QoD API
  slug: camara-project-home-devices-qod-api
- description: Retrieve the location of a device
  name: CAMARA Project Location retrieval API
  slug: camara-project-location-retrieval-api
- description: Verification of the location of a device
  name: CAMARA Project Location verification API
  slug: camara-project-location-verification-api
- description: Operations to match a customer identity against the account data bound to their phone number.
  name: CAMARA Project Match API
  slug: camara-project-match-api
- description: Read the network's level of confidence that it can meet the quality thresholds for a given application profile and end user device.
  name: CAMARA Project Network Quality API
  slug: camara-project-network-quality-api
- description: Operations to manage One Step Payment procedure
  name: CAMARA Project One Step Payment API
  slug: camara-project-one-step-payment-api
- description: API operations to manage OTP codes
  name: CAMARA Project OTP Management API
  slug: camara-project-otp-management-api
- description: Operations to obtain information about payments
  name: CAMARA Project Payment API
  slug: camara-project-payment-api
- description: API operation to return the phone number associated to the access token.
  name: CAMARA Project Phone number share API
  slug: camara-project-phone-number-share-api
- description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: CAMARA Project Phone number verify API
  slug: camara-project-phone-number-verify-api
- description: Operations to retrieve population density information.
  name: CAMARA Project Population Density Data API
  slug: camara-project-population-density-data-api
- description: Manage the permanent assignment of a QoS profile to a device
  name: CAMARA Project QoS Assignment API
  slug: camara-project-qos-assignment-api
- description: Manage QoS Profiles
  name: CAMARA Project QoS Profiles API
  slug: camara-project-qos-profiles-api
- description: Manage QoS sessions
  name: CAMARA Project QoS Sessions API
  slug: camara-project-qos-sessions-api
- description: Receive the last date in which the device of the end-user was swapped
  name: CAMARA Project Retrieve Device Swap Date API
  slug: camara-project-retrieve-device-swap-date-api
- description: The Retrieve SIM swap date API from CAMARA Project — 1 operation(s) for retrieve sim swap date.
  name: CAMARA Project Retrieve SIM swap date API
  slug: camara-project-retrieve-sim-swap-date-api
- description: Operation to get device roaming status and country information (if roaming) synchronously
  name: CAMARA Project Roaming status retrieval API
  slug: camara-project-roaming-status-retrieval-api
- description: The Send SMS API from CAMARA Project — 1 operation(s) for send sms.
  name: CAMARA Project Send SMS API
  slug: camara-project-send-sms-api
- description: Operation to manage event subscription on sim swap event (swapped)
  name: CAMARA Project Sim Swap Subscription API
  slug: camara-project-sim-swap-subscription-api
- description: Operations to manage Two Step Payment procedure
  name: CAMARA Project Two Step Payment API
  slug: camara-project-two-step-payment-api
- description: Provides information on Unconditional Call Forwarding settings for the provided phone number (PhoneNumber)
  name: CAMARA Project Unconditional Call Forwarding information retrieval API
  slug: camara-project-unconditional-call-forwarding-information-retrieval-api
artifact_total: 79
collections:
- collection_type: open
  name: Call Forwarding Signal
  slug: open-call-forwarding-signal
- collection_type: open
  name: Carrier Billing
  slug: open-carrier-billing
- collection_type: open
  name: Connectivity Insights
  slug: open-connectivity-insights
- collection_type: open
  name: Device Geofencing Subscriptions
  slug: open-device-location-geofencing
- collection_type: open
  name: Device Location Retrieval
  slug: open-device-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-device-location-verification
- collection_type: open
  name: Connected Network Type
  slug: open-device-status-connected-network-type
- collection_type: open
  name: Device Reachability Status
  slug: open-device-status-reachability
- collection_type: open
  name: Device Roaming Status
  slug: open-device-status-roaming
- collection_type: open
  name: Device Swap
  slug: open-device-swap
- collection_type: open
  name: Home Devices QoD
  slug: open-home-devices-qod
- collection_type: open
  name: Know Your Customer Age Verification
  slug: open-kyc-age-verification
- collection_type: open
  name: Know Your Customer Fill-in
  slug: open-kyc-fill-in
- collection_type: open
  name: Know Your Customer Match
  slug: open-kyc-match
- collection_type: open
  name: Number Verification
  slug: open-number-verification
- collection_type: open
  name: One Time Password SMS
  slug: open-one-time-password-sms
- collection_type: open
  name: Population Density Data
  slug: open-population-density-data
- collection_type: open
  name: QoS Profiles
  slug: open-qos-profiles
- collection_type: open
  name: QoS Provisioning
  slug: open-qos-provisioning
- collection_type: open
  name: Quality-On-Demand
  slug: open-quality-on-demand
- collection_type: open
  name: Sim Swap Subscriptions
  slug: open-sim-swap-subscriptions
- collection_type: open
  name: SIM Swap
  slug: open-sim-swap
- collection_type: open
  name: Simple Edge Discovery
  slug: open-simple-edge-discovery
- collection_type: open
  name: SMS API
  slug: open-sms
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camara-project-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camara-project-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camara-project-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://camaraproject.org
- group: company
  title: ''
  type: AboutUs
  url: https://camaraproject.org/about-camara/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camaraproject
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/Governance
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/Governance/blob/main/ProjectCharter.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/Commonalities
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/IdentityAndConsentManagement
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/ReleaseManagement
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/APIBacklog
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.camaraproject.org/
- group: docs
  title: ''
  type: Documentation
  url: https://camaraproject.github.io/
- group: operate
  title: ''
  type: Contact
  url: https://camaraproject.org/contact/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/camaraproject/Governance/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/camaraproject/Governance/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/camaraproject/Governance/blob/main/documentation/LICENSE.APACHE2.0
- group: operate
  title: ''
  type: Forums
  url: https://lists.camaraproject.org/g/all
- group: company
  title: ''
  type: Blog
  url: https://camaraproject.org/news-and-events/
- group: other
  title: ''
  type: Events
  url: https://camaraproject.org/events/
- group: operate
  title: ''
  type: PressRelease
  url: https://www.linuxfoundation.org/press/announcing-camara-the-telco-global-api-alliance
- group: company
  title: ''
  type: Partner
  url: https://www.gsma.com/solutions-and-impact/connectivity-for-good/external-affairs/wp-content/uploads/2024/02/Open-Gateway-Joint-Statement.pdf
created: '2026-05-25T00:00:00.000Z'
description: CAMARA is the Telco Global API Alliance — an open-source project hosted by the Linux Foundation that defines, builds, and tests a unified set of network APIs across the world's mobile operators. Working alongside the GSMA Open Gateway commercialization initiative, CAMARA produces operator-neutral OpenAPI 3.0 specifications for 60+ telco network capabilities including Number Verification, SIM Swap, Device Location, Quality on Demand, KYC, Carrier Billing, Edge Discovery, Device Status, SMS, and more — all published under Apache 2.0. The project is organized into Sandbox, Incubating, and Graduated sub-projects with cross-cutting Commonalities, Identity and Consent Management, and Release Management working groups. Major contributors include Deutsche Telekom, Orange, Telefonica, Vodafone, T-Mobile, Verizon, AT&T, KDDI, SK Telecom, China Mobile, and dozens of other operators and vendors.
features:
- 60+ telco network APIs designed as a unified, operator-neutral surface
- Hosted by the Linux Foundation as the open governance home for telco network APIs
- Joint initiative with GSMA Open Gateway — the carrier commercialization program
- OpenAPI 3.0.3 specs for every API, published under Apache 2.0
- CloudEvents-based webhook subscriptions for event-driven APIs (sim-swap, geofencing, device-status)
- Three-tier repository maturity model — Sandbox, Incubating, Graduated
- Centralized Commonalities working group defining cross-API design guidelines and shared models
- Centralized Identity And Consent Management working group (OIDC CIBA + purpose-bound consent)
- Quarterly coordinated releases via the Release Management working group
- Provider Implementation repos (`*_PI*`) demonstrating real operator deployments
- Anti-fraud bundle - Number Verification, SIM Swap, Device Swap, Call Forwarding Signal
- Network capability bundle - Quality on Demand, QoS Profiles, Simple Edge Discovery, Connectivity Insights
- Identity bundle - KYC Match, KYC Fill-In, KYC Age Verification, Tenure
- Location bundle - Location Retrieval, Location Verification, Geofencing Subscriptions
- Device bundle - Device Status, Device Location, Device Swap, Device Identifier, Device Authenticity
- Messaging bundle - SMS, OTP via SMS, Voice Notification, Voice Verification Code, Call Forwarding
- Commercial bundle - Carrier Billing Checkout, Sponsored Data
- Analytics bundle - Population Density Data, Connectivity Insights, Network Insights, Customer Insights
- Edge cloud bundle - Simple Edge Discovery, Optimal Edge Discovery, Application Endpoint Discovery, Application Endpoint Registration, Edge Application Management
- IoT bundle - IoT Device Management, IoT SIM Fraud Prevention, IoT Network Optimization, eSIM Remote Management
- Powered by major operators - Deutsche Telekom, Orange, Telefonica, Vodafone, T-Mobile, Verizon, AT&T, KDDI, SK Telecom, China Mobile, Telenor, TIM, BT, Singtel, and others
- Cross-operator aggregator integrations through GSMA Open Gateway (Vonage, Infobip, Aduna, others)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camara-project.png
layout: provider
modified: '2026-05-25'
name: CAMARA Project
nav: Providers
network: true
overview: 'CAMARA Project publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Age Verification API, Call Forwarding information retrieval API, Check Device Swap API, and 27 more. Tagged areas include API Standards, CAMARA, GSMA, Linux Foundation, and Network APIs.


  CAMARA Project''s developer surface includes authentication, developer portal, documentation, engineering blog, and 19 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 24.0
  delta: -3.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.2
    developer_ergonomics: 30.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camara-project/refs/heads/main/screenshots/camara-project-2026-06-20T173902.png
security:
- kind: authentication
  name: Camara Project Authentication
  slug: camara-project-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Camara Project Domain Security
  slug: camara-project-domain-security
  summary_line: TLSv1.3 · HSTS
slug: camara-project
tags:
- API Standards
- CAMARA
- GSMA
- Linux Foundation
- Network APIs
- Open API
- Open Gateway
- Open Source
- Standards
- Telco
- Telco API Alliance
- Telecom
- Telecommunications
website: https://camaraproject.org
---
