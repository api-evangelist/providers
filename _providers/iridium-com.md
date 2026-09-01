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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iridium-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iridium.com
- group: other
  title: ''
  type: Services
  url: https://www.iridium.com/services/
- group: other
  title: ''
  type: CloudConnect
  url: https://www.iridium.com/services/iridium-cloudconnect/
- group: other
  title: ''
  type: NTNDirect
  url: https://www.iridium.com/services/iridium-ntn-direct/
- group: other
  title: ''
  type: PNT
  url: https://www.iridium.com/services/pnt/
- group: other
  title: ''
  type: IoTDataMessaging
  url: https://www.iridium.com/services/iot-data-messaging/
- group: auth
  title: ''
  type: SafetySecurity
  url: https://www.iridium.com/services/safety-security/
- group: other
  title: ''
  type: Voice
  url: https://www.iridium.com/services/voice/
- group: other
  title: ''
  type: Products
  url: https://www.iridium.com/products/
- group: other
  title: ''
  type: DeveloperResources
  url: https://www.iridium.com/products/develop-anything/
- group: other
  title: ''
  type: Modules
  url: https://www.iridium.com/products/iridium-9602/
- group: company
  title: ''
  type: Partners
  url: https://www.iridium.com/partners/
- group: other
  title: ''
  type: Company
  url: https://www.iridium.com/company/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.iridium.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.iridium.com/company/news-media/
- group: company
  title: ''
  type: Careers
  url: https://www.iridium.com/company/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.iridium.com/company/contact/
- group: other
  title: ''
  type: Messaging
  url: https://messaging.iridium.com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/IridiumComm
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iridium-satellite-communications
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/IridiumComm
created: '2026-05-25'
description: 'Iridium Communications Inc. (NASDAQ: IRDM) is a McLean, Virginia satellite communications company operating a constellation of 66 cross-linked Low Earth Orbit (LEO) satellites that deliver truly global L-band voice, data, IoT, and positioning/navigation/timing (PNT) services across every region of the Earth, including the polar oceans. Iridium sells satellite phones (Iridium Extreme), satellite messengers, satellite IoT modules and modems (Iridium 9602/9603, Iridium Certus 9770/9810/9704, Iridium Edge, Iridium Edge Pro, Iridium Edge Solar), Short Burst Data (SBD) messaging, broadband Certus terminals, and next-generation Iridium NTN Direct 5G Non-Terrestrial Network services built on 3GPP NB-IoT for direct-to-device smartphone and IoT connectivity. Iridium CloudConnect — co-developed with Amazon Web Services — pipes satellite IoT data as JSON into customer-owned Amazon SQS queues inside their own AWS VPC over a dedicated private Iridium-AWS interconnect, making Iridium the
  first global cloud-native satellite IoT backhaul. The company serves aviation, maritime, government/defense, land-mobile, autonomous systems, and IoT markets through a partner ecosystem of more than 500 service providers, value-added resellers, and hardware OEMs, and in May 2026 announced a planned acquisition of Aireon, operator of the world''s only space-based air traffic surveillance network. Iridium''s business model is airtime/subscription revenue plus hardware module licensing and engineering services; there is no public, self-service developer API or OpenAPI — network access is mediated through Iridium-authorized service providers, the Iridium CloudConnect AWS integration, and hardware-level AT-command and SBD interfaces on Iridium modems.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iridium-com.png
layout: provider
modified: '2026-05-25'
name: Iridium
nav: Providers
network: true
overview: 'Iridium is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Satellite Communications, LEO, L-Band, and IoT.


  Iridium''s developer surface includes YouTube channel and 21 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Iridium Com Domain Security
  slug: iridium-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iridium-com
tags:
- Satellite
- Satellite Communications
- LEO
- L-Band
- IoT
- Satellite IoT
- Short Burst Data
- SBD
- Iridium Certus
- Iridium NTN Direct
- NB-IoT
- 5G Non-Terrestrial Network
- Direct-to-Device
- Positioning Navigation And Timing
- PNT
- Maritime
- Aviation
- Defense
- Autonomous Systems
- Cloud Connect
website: https://www.iridium.com
---
