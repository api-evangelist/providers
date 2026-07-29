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
- acting_count: 17
  human_in_the_loop: 0
  name: Orange Business Agentic Access
  operation_count: 21
  slug: orange-business-agentic-access
  summary_line: 21 operations · 17 acting
api_count: 38
apis:
- description: Orange's IoT platform (also branded Datavenue) for connecting, managing, and ingesting data from IoT devices over LoRa, NB-IoT, LTE-M, and classic cellular. REST and MQTT interfaces for device, group,
  name: Orange Business Live Objects API
  slug: orange-business-live-objects-api
- description: Manage Orange Business cellular IoT SIM fleets worldwide — activation, suspension, usage, location, diagnostics — across 200+ countries via a single REST surface. Backs the Orange Business Mobile Conn
  name: Orange Business IoT Managed Global Connectivity API
  slug: orange-business-iot-managed-global-connectivity-api
- description: Accept Orange Money mobile-wallet payments on web and mobile checkouts across Mali, Cameroon, Cote d'Ivoire, Senegal, Madagascar, Botswana, Guinea Conakry, Guinea Bissau, Sierra Leone, DR Congo, and C
  name: Orange Business Orange Money WebPay API
  slug: orange-business-orange-money-webpay-api
- description: Direct-carrier-billing API that lets merchants charge purchases to a customer's Orange mobile invoice. Aimed at digital goods, content, and microtransactions for Orange subscribers.
  name: Orange Business Pay With Orange Bill API
  slug: orange-business-pay-with-orange-bill-api
- description: A2P SMS delivery API for Orange Middle East and Africa footprint. Supports transactional, OTP, and marketing messages across Orange's African operating companies.
  name: Orange Business SMS Middle East and Africa API
  slug: orange-business-sms-mea-api
- description: Programmable voice / VoIP API for integrating outbound calls, IVR, and click-to-call into business applications on Orange's voice platform.
  name: Orange Business Voice as a Service API
  slug: orange-business-voice-as-a-service-api
- description: Multichannel contact and notification API — SMS, voice, email, and fax broadcast — used for crisis communications, mass notifications, and customer outreach campaigns by Orange Business enterprise cus
  name: Orange Business Contact Everyone API
  slug: orange-business-contact-everyone-api
- description: Programmable management for Business Talk, Orange Business's enterprise SIP trunking and IP voice service. Provision lines, manage sites, and integrate voice with UCaaS platforms.
  name: Orange Business Business Talk API
  slug: orange-business-business-talk-api
- description: REST API for Cloud Avenue, Orange Business's France-sovereign VMware-based managed IaaS — provision virtual datacenters, networks, storage, and compute resources programmatically.
  name: Orange Business Cloud Avenue API
  slug: orange-business-cloud-avenue-api
- description: Sandbox IaaS environment for testing applications on Orange Business's Evolution Platform with full REST API access to VMs, networks, and storage.
  name: Orange Business Evolution Platform IaaS API
  slug: orange-business-evolution-platform-iaas-api
- description: Order, manage, and monitor Ethernet Virtual Private Line connectivity services across Orange Business's global Ethernet backbone via REST.
  name: Orange Business EVPL Online API
  slug: orange-business-evpl-online-api
- description: Real-time monitoring API for EVPL and adjacent Orange Business network services — fetch link health, throughput, and incident state for managed enterprise connectivity.
  name: Orange Business EVPL Monitoring API
  slug: orange-business-evpl-monitoring-api
- description: Manage CDN edge caching, purge, and acceleration policies for content delivered over Orange's networks — primarily targeted at media and large enterprise customers.
  name: Orange Business Content Delivery Boost API
  slug: orange-business-content-delivery-boost-api
- description: Customer-facing inventory API for Orange Business Services — list contracts, sites, services, and product instances under a B2B account.
  name: Orange Business Core Information API
  slug: orange-business-core-information-api
- description: Place, modify, and cancel orders against the Orange Business Services product catalogue. Aligned with TM Forum Open APIs (TMF622-style product ordering).
  name: Orange Business Ordering API
  slug: orange-business-ordering-api
- description: Track the lifecycle and milestones of an Orange Business Services order — status, expected delivery, blocking issues, and milestone history.
  name: Orange Business Order Tracking API
  slug: orange-business-order-tracking-api
- description: Programmatic access to Orange Business Services M2M invoices, charges, and itemised usage records for enterprise finance and FinOps integration.
  name: Orange Business Billing API
  slug: orange-business-billing-api
- description: Open, update, and track Orange Business Services support tickets via REST. Aligned with TM Forum TMF621 Trouble Ticket conventions to plug into enterprise ITSM workflows.
  name: Orange Business Incident API
  slug: orange-business-incident-api
- description: Marketplace surface for discovering Orange Business APIs — programmatic catalogue access for the Orange Business API portfolio.
  name: Orange Business API Place
  slug: orange-business-api-place-api
- description: Check broadband and fibre eligibility at a French address for operator partners — feeds B2B onboarding flows.
  name: Orange Business Operator Eligibility (France) API
  slug: orange-business-operator-eligibility-fr-api
- description: Public-initiative network (RIP) fibre eligibility check for French regional fibre rollouts, used by alternative operators to qualify customer addresses.
  name: Orange Business RIP Operator Eligibility (France) API
  slug: orange-business-rip-operator-eligibility-fr-api
- description: Real-time identity verification combining ID-document capture, liveness detection, and biometric match against the document. Targets remote onboarding for regulated industries.
  name: Orange Business Live Identity Verify API
  slug: orange-business-live-identity-verify-api
- description: Behavioural and challenge-based human-verification (captcha) API used inside Orange's Live Identity suite to gate sensitive flows against automated abuse.
  name: Orange Business Live Identity Captcha API
  slug: orange-business-live-identity-captcha-api
- description: Cameroon-specific A2P messaging platform for enterprise SMS, USSD, and rich messaging deliveries to Orange Cameroon subscribers.
  name: Orange Business Messaging Pro Cameroon API
  slug: orange-business-messagingpro-cameroon-api
- description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: Orange Business Check Device Swap API
  slug: orange-business-check-device-swap-api
- description: The Check SIM swap API from Orange Business — 1 operation(s) for check sim swap.
  name: Orange Business Check SIM swap API
  slug: orange-business-check-sim-swap-api
- description: Operations to get the current reachability status of a device
  name: Orange Business Device reachability status API
  slug: orange-business-device-reachability-status-api
- description: Operations to manage event subscriptions on geofencing events for leaving and entering an area.
  name: Orange Business Geofencing subscriptions API
  slug: orange-business-geofencing-subscriptions-api
- description: Retrieve the location of a device
  name: Orange Business Location retrieval API
  slug: orange-business-location-retrieval-api
- description: Verification of the location of a device
  name: Orange Business Location verification API
  slug: orange-business-location-verification-api
- description: Operations to match a customer identity against the account data bound to their phone number.
  name: Orange Business Match API
  slug: orange-business-match-api
- description: API operation to return the phone number associated to the access token.
  name: Orange Business Phone number share API
  slug: orange-business-phone-number-share-api
- description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: Orange Business Phone number verify API
  slug: orange-business-phone-number-verify-api
- description: Operations to retrieve population density information.
  name: Orange Business Population Density Data API
  slug: orange-business-population-density-data-api
- description: Manage QoS sessions
  name: Orange Business QoS Sessions API
  slug: orange-business-qos-sessions-api
- description: Receive the last date in which the device of the end-user was swapped
  name: Orange Business Retrieve Device Swap Date API
  slug: orange-business-retrieve-device-swap-date-api
- description: The Retrieve SIM swap date API from Orange Business — 1 operation(s) for retrieve sim swap date.
  name: Orange Business Retrieve SIM swap date API
  slug: orange-business-retrieve-sim-swap-date-api
- description: Operation to get device roaming status and country information (if roaming) synchronously
  name: Orange Business Roaming status retrieval API
  slug: orange-business-roaming-status-retrieval-api
artifact_total: 53
collections:
- collection_type: open
  name: Device Location Retrieval
  slug: open-orange-business-device-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-orange-business-device-location-verification
- collection_type: open
  name: Device Reachability Status
  slug: open-orange-business-device-reachability-status
- collection_type: open
  name: Device Roaming Status
  slug: open-orange-business-device-roaming-status
- collection_type: open
  name: Device Swap
  slug: open-orange-business-device-swap
- collection_type: open
  name: Device Geofencing Subscriptions
  slug: open-orange-business-geofencing
- collection_type: open
  name: Know Your Customer Match
  slug: open-orange-business-kyc-match
- collection_type: open
  name: Number Verification
  slug: open-orange-business-number-verification
- collection_type: open
  name: Population Density Data
  slug: open-orange-business-population-density-data
- collection_type: open
  name: Quality-On-Demand
  slug: open-orange-business-quality-on-demand
- collection_type: open
  name: SIM Swap
  slug: open-orange-business-sim-swap
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orange-business-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orange-business-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orange-business-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orange-business-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.orange.com/
- group: start
  title: ''
  type: Portal
  url: https://www.orange-business.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.orange.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/products/network-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/blog/orange-open-gateway-the-new-era-of-digital-services/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/blog/orange-livenet-a-new-business-unit-to-market-network-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma_orgs/orange-2/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/camaraproject
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Orange-OpenSource
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/hurl
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/Orange-Boosted-Bootstrap
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-flutter
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/towards5gs-helm
- group: company
  title: ''
  type: Blog
  url: https://developer.orange.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.orange-business.com/en/blogs
- group: docs
  title: ''
  type: Documentation
  url: https://5glab.orange.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.orange.com/en/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange-business/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/orangebusiness
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orange-business.com/en/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orange-business.com/en/personal-data-protection
- group: operate
  title: ''
  type: Support
  url: https://developer.orange.com/contact
- group: operate
  title: ''
  type: Support
  url: https://developer.orange.com/talk-to-sales/
- group: start
  title: ''
  type: Signup
  url: https://developer.orange.com/register
- group: docs
  title: ''
  type: Documentation
  url: https://www.orange-business.com/en/our-solutions
- group: docs
  title: ''
  type: Documentation
  url: https://www.orange-business.com/en/products/live-intelligence
- group: start
  title: ''
  type: Portal
  url: https://liveobjects.orange-business.com/
- group: start
  title: ''
  type: Portal
  url: https://cloud.orange-business.com/
description: Orange Business is the B2B, telco-cloud, and developer arm of Orange S.A. — France's leading telecommunications group operating across Europe, the Middle East, and Africa. The company markets itself as "an operator, integrator, and platform player" and serves 30,000+ enterprise customers across 65 countries with cloud, cybersecurity, SD-WAN/SASE, 5G, IoT, data, AI, and digital-workplace services. Orange's developer surface is split across two tracks. The Orange Developer portal (developer.orange.com) publishes the Orange Open Gateway — Orange's implementation of GSMA Open Gateway / CAMARA standardised network APIs (Number Verification, SIM Swap, Device Swap, KYC Match, Device Location, Geofencing, Device Status, Quality on Demand, Population Density Data) — alongside Orange-specific APIs for IoT (Live Objects, IoT Global Connectivity), payments (Orange Money WebPay, Pay With Orange Bill, carrier billing across Orange Africa), communications (Voice, SMS MEA, Business Talk, Contact
  Everyone), cloud (Cloud Avenue sovereign IaaS, Evolution Platform), and identity (Live Identity Verify, Live Identity Captcha). The Orange Business Services portfolio adds a B2B TM Forum–aligned API track for ordering, billing, incident management, eligibility, and order tracking. The Orange-OpenSource GitHub org backs the developer ecosystem with 427+ repos including Hurl (the popular Rust HTTP testing CLI with 18K+ stars), the Boosted accessible Bootstrap framework, the OUDS Orange Unified Design System for iOS / Android / Flutter, and 5G Kubernetes Helm charts. Orange has also stood up Orange LiveNet, a business unit dedicated to commercialising programmable network capabilities, and is one of the founding operators of the GSMA Open Gateway initiative with the CAMARA Linux Foundation project.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orange-business.png
layout: provider
name: Orange Business
nav: Providers
network: true
overview: 'Orange Business publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Check Device Swap API, Check SIM swap API, Device reachability status API, and 11 more. Tagged areas include 5G, AI, B2B, CAMARA, and Cloud.


  Orange Business'' developer surface includes authentication, developer portal, documentation, tooling, engineering blog, support, signup flow, and 28 more developer resources.'
random_paper: 37
score:
  band: thin
  composite: 34.7
  delta: -5.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 54.6
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 36.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/orange-business/refs/heads/main/screenshots/orange-business-2026-06-20T191153.png
security:
- kind: authentication
  name: Orange Business Authentication
  slug: orange-business-authentication
  summary_line: http/openIdConnect · 2 schemes
- kind: domain-security
  name: Orange Business Domain Security
  slug: orange-business-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Orange Business Vulnerability Disclosure
  slug: orange-business-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orange-business
tags:
- 5G
- AI
- B2B
- CAMARA
- Cloud
- Communications
- Cybersecurity
- Developer Platform
- Digital Workplace
- Enterprise
- France
- IoT
- Identity
- Mobile Money
- Network APIs
- Open Gateway
- Orange
- Payments
- SD-WAN
- SMS
- SASE
- Telco
- Voice
website: https://developer.orange.com/
---
