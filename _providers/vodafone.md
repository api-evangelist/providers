---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 27
apis:
- description: Frictionless mobile-number verification that confirms ownership of the MSISDN currently in use on the device, using the operator network rather than SMS one-time-passcodes. Implements the CAMARA Numbe
  name: Number Verification 2.0 (CAMARA)
  slug: number-verification-camara
- description: Earlier CAMARA Number Verification implementation, still maintained for backwards compatibility with integrations built before the 2.0 release.
  name: Number Verification 1.0 (CAMARA)
  slug: number-verification-1-camara
- description: CAMARA SIM Swap API that returns the timestamp of the most recent SIM change for a given MSISDN (latestSimChange), used by banks and fintech apps to detect SIM-swap fraud before approving high-risk op
  name: SIM Swap (CAMARA)
  slug: sim-swap-camara
- description: CAMARA-aligned identity-match API that compares user-supplied attributes (name, address, date of birth) against operator-held subscriber records and returns match/no-match indicators for KYC and onboa
  name: Match (CAMARA)
  slug: match-camara
- description: Tells callers whether a mobile number has been recycled (re-assigned to a new subscriber) since a given date, so that downstream systems can revoke stale account bindings before sending sensitive noti
  name: Number Recycling (CAMARA)
  slug: number-recycling-camara
- description: CAMARA Quality on Demand API for requesting a temporary QoS uplift on a specific UE session — used for cloud gaming, live broadcast contribution, drone control, and other latency- or throughput-sensit
  name: Quality on Demand
  slug: quality-on-demand
- description: Lists the QoS profiles a developer may request via Quality on Demand, including profile identifiers, throughput class, and latency targets.
  name: Quality of Service Profiles
  slug: qos-profiles
- description: Longer-lived QoS provisioning for enterprise customers who want a persistent QoS profile applied to a set of subscriptions. Available in DE and UK.
  name: QoS Provisioning
  slug: qos-provisioning
- description: Confirms whether an MSISDN is currently an active Vodafone subscriber. Available in UK.
  name: Active Subscriber
  slug: active-subscriber
- description: Network-based age-assurance lookup that returns whether the subscriber behind a given MSISDN is above a configured age threshold, without revealing the underlying date of birth.
  name: Age Verify
  slug: age-verify
- description: Indicates whether call forwarding is currently active on the target number — a useful signal for fraud-detection flows where divert-to- attacker is a common attack vector.
  name: Call Divert
  slug: call-divert
- description: Returns whether a subscriber is currently on their home network or roaming — useful for fraud-scoring and conditional flows that adjust behaviour based on roaming status.
  name: Home Network Check
  slug: home-network-check
- description: Resolves the underlying MVNO/host-network for a given mobile number so that callers can route their integration to the correct operator API endpoint.
  name: MVNO Discovery
  slug: mvno-discovery
- description: HLR-style lookup returning the operator, country, portability status, and basic line-type metadata for a given E.164 mobile number.
  name: Number Lookup
  slug: number-lookup
- description: Vodafone's pre-CAMARA Number Recycling lookup, retained alongside the CAMARA-aligned variant for existing integrations.
  name: Number Recycle
  slug: number-recycle
- description: Returns how long the current subscriber has held the MSISDN — short tenure is a strong signal in fraud-scoring models for newly-acquired numbers used in account takeovers.
  name: Tenure
  slug: tenure
- description: Registers a sender brand for A2P SMS and Verified Caller flows so that consumer handsets display branded sender identity rather than a raw short-code or number. Available in DE and UK.
  name: Brand Registration
  slug: brand-registration
- description: Branded-calling product that lets enterprises display a verified brand name and reason-for-call on the called party's handset. Available in UK.
  name: Verified Caller
  slug: verified-caller
- description: A2P SMS messaging gateway for sending one-time-passcodes, alerts, and marketing messages to Vodafone subscribers and onward via interconnect.
  name: SMS Messaging Hub
  slug: sms-messaging-hub
- description: Vodafone Roaming Services Network Usage Event API streams roaming network-usage events to partner operators for settlement, fraud detection, and customer-experience monitoring. Available in UK.
  name: Vodafone Roaming Services (VRS)
  slug: roaming-services
- description: Real-time, aggregated, and anonymised footfall counts per area derived from the Vodafone mobile network — used by retail, transport, and urban planning customers. Available in DE and UK.
  name: Vodafone Analytics — Real-time Footfall
  slug: analytics-realtime-footfall
- description: Orders historic, aggregated footfall datasets for a defined area and time window. Available in DE and UK.
  name: Vodafone Analytics — Footfall Historic Order
  slug: analytics-footfall-historic-order
- description: Helper API for resolving Bing-style QuadKey tile identifiers used as the spatial primary key by Vodafone Analytics Footfall products.
  name: Vodafone Analytics — Reference QuadKey Helper
  slug: analytics-reference-quadkey
- description: Free-tier aggregated location dataset for evaluating Vodafone Analytics before committing to paid Footfall products.
  name: Vodafone Analytics — Free Location Dataset
  slug: analytics-free-location-dataset
- description: Partner API for blocking a SIM (e.g. lost-or-stolen) on the Vodafone network on behalf of an authenticated subscriber. Available in NL.
  name: Block SIM
  slug: block-sim
- description: Partner API for retrieving a PUK unblocking code on behalf of an authenticated subscriber whose SIM is PIN-locked. Available in NL.
  name: Get PUK Code
  slug: get-puk-code
- description: TM Forum TMF931 Onboarding And Ordering Open API exposed as part of the GSMA Open Gateway Operate APIs, so that aggregators and channel partners can onboard and order CAMARA APIs across Vodafone's foo
  name: TMF931 — Onboarding And Ordering
  slug: tmf931-onboarding-ordering
artifact_total: 28
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vodafone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vodafone.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.vodafone.com
- group: other
  title: ''
  type: APICatalogue
  url: https://developer.vodafone.com/api-catalogue
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.vodafone.com/docs/getting-started
- group: start
  title: ''
  type: Sandbox
  url: https://api-sandbox.vf-dmp.engineering.vodafone.com
- group: other
  title: ''
  type: Production
  url: https://api.vf-dmp.engineering.vodafone.com
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/vodafone-developers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/vodafone
- group: other
  title: ''
  type: CAMARA
  url: https://camaraproject.org
- group: build
  title: ''
  type: CAMARAGitHub
  url: https://github.com/camaraproject
- group: other
  title: ''
  type: OpenGateway
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
- group: other
  title: ''
  type: VodafoneBusiness
  url: https://www.vodafone.com/business
- group: other
  title: ''
  type: IoT
  url: https://www.vodafone.com/business/iot
- group: company
  title: ''
  type: Investors
  url: https://investors.vodafone.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.vodafone.com/news
- group: company
  title: ''
  type: Careers
  url: https://careers.vodafone.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/VodafoneGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vodafone
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Vodafone
- group: company
  title: ''
  type: Blog
  url: https://www.vodafone.com/news
created: '2026-05-25'
description: Vodafone Group plc is a UK-headquartered (Newbury, England) multinational telecommunications company and one of the world's largest mobile and fixed network operators, with operations in 15 country markets and partner-market agreements covering 40+ additional countries across Europe and Africa. The group serves 279 million mobile customers, 5 million business customers, and manages 215+ million IoT connections through its Vodafone IoT platform. Beyond mobile and broadband connectivity, Vodafone operates one of the largest IoT/M2M businesses in the industry, invests in 70+ subsea cables, and runs financial services like M-PESA (Africa) and Vodapay. Through Vodafone Business it sells connectivity, cloud, security, and managed-mobility services to enterprises, and through the GSMA Open Gateway and CAMARA initiative it exposes a growing portfolio of standardised network APIs (Number Verify, SIM Swap, Quality on Demand, Device Location, Match, MVNO Discovery, and more) via the Vodafone
  Developer Marketplace (developer.vodafone.com), which publishes 27+ commercial and CAMARA APIs across Identity, Mobile, Analytics, Boost/QoS, and Partner categories. The Marketplace exposes sandbox and live endpoints under api-sandbox.vf-dmp.engineering.vodafone.com and api.vf-dmp.engineering.vodafone.com, with OAuth2 (Consumer Key / Consumer Secret) authentication and Postman collections for every product. Vodafone is a premier member of the CAMARA alliance hosted at the Linux Foundation, a founding participant in the GSMA Open Gateway, and one of the principal telco operators driving network-as-an-API adoption globally.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vodafone.png
layout: provider
modified: '2026-05-25'
name: Vodafone
nav: Providers
network: true
overview: 'Vodafone publishes 27 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Telco, Mobile Network Operator, 5G, and 4G.


  Vodafone''s developer surface includes getting-started guide, sandbox, GitHub presence, YouTube channel, engineering blog, and 16 more developer resources.'
random_paper: 30
score:
  band: minimal
  composite: 12.9
  delta: -3.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vodafone/refs/heads/main/screenshots/vodafone-2026-06-20T201126.png
security:
- kind: domain-security
  name: Vodafone Domain Security
  slug: vodafone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vodafone
tags:
- Telecommunications
- Telco
- Mobile Network Operator
- 5G
- 4G
- Connectivity
- Broadband
- IoT
- Internet of Things
- Open Gateway
- CAMARA
- Network APIs
- Identity
- SIM Swap
- Number Verification
- Quality on Demand
- Quality of Service
- Roaming
- SMS
- Messaging
- Analytics
- Footfall
- Location
- Vodafone Business
- M-PESA
- Mobile Financial Services
- Enterprise
- Europe
- Africa
- United Kingdom
website: https://www.vodafone.com
---
