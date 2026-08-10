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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 15
apis:
- description: Charge one-off or recurring purchases directly to a verified end user's BT or EE mobile bill or pre-pay credit, enabling carrier-billed payments without re-collecting card or bank credentials.
  name: Direct Carrier Billing API
  slug: direct-carrier-billing
- description: Query when a mobile subscriber's SIM was last changed so relying parties can detect SIM-swap account-takeover attacks before sending SMS one-time passcodes or completing high-risk authentications.
  name: SIM Swap Detection API
  slug: sim-swap
- description: Determine whether a given mobile number is on the EE or BT Mobile network, or on one of EE's MVNO partners, returning an anonymised mobile subscription reference (AMSR) to minimise data exposure.
  name: Network Identity API
  slug: network-identity
- description: Place broadband orders from communications-provider systems directly into BT Wholesale's "The Hub" order platform for Broadband One products.
  name: Broadband One Order API
  slug: broadband-one
- description: Create and retrieve quotes for BT Wholesale Ethernet and Optical connectivity products as part of B2B ordering flows.
  name: Quote Management (Ethernet)
  slug: quote-management-ethernet
- description: Search the Rest of BT (RoBT) and Openreach address databases to retrieve address records and address keys for ordering, and create addresses when no matching record exists.
  name: Address Management API
  slug: address-management
- description: Book, amend, and cancel engineer appointment slots for wholesale broadband and voice provisioning workflows.
  name: Appointment Management API
  slug: appointment-management
- description: Check product and network availability at a given address or premises for wholesale broadband and voice services prior to ordering.
  name: Product and Network Availability API
  slug: product-network-availability
- description: Wholesale Hosted Centrex / Voice (WHCE) API for managing hosted voice services delivered via BT Wholesale's HubCo platform.
  name: BT Wholesale HubCo WHCE API
  slug: hubco-whce
- description: Initiate ordering of phone numbers and configuration for BT Global Voice Services consumed by multinational enterprise customers.
  name: Global Voice Services API
  slug: global-voice-services
- description: Retrieve the IMEI associated with a given MSISDN for device identification, fraud, and entitlement checks.
  name: IMEI Lookup API
  slug: imei-lookup
- description: Verify whether a customer's phone is currently connected to EE's mobile network, supporting risk decisioning and step-up authentication.
  name: Home Network API
  slug: home-network
- description: Provide strategic insights into current and future demand on the UK's railway network derived from BT's mobile network and analytics capabilities.
  name: Rail Insights API
  slug: rail-insights
- description: Access insights on footfall activity and visitor catchments across any location in London, derived from anonymised mobile network signals.
  name: Location Insights for London API
  slug: location-insights-london
- description: Platform of APIs supplying travel and journey intelligence derived from BT's network and Active Intelligence capabilities.
  name: Travel Journey API Platform
  slug: travel-journey
artifact_total: 17
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bt-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bt-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bt.com
- group: other
  title: ''
  type: Group
  url: https://www.bt.com/about
- group: other
  title: ''
  type: Developer
  url: https://developer.bt.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bt.com/api-documentation
- group: other
  title: ''
  type: Products
  url: https://developer.bt.com/products
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://developer.bt.com/knowledge-center/docs/getting-started
- group: docs
  title: ''
  type: HowToGuides
  url: https://developer.bt.com/knowledge-center/docs/how-guides
- group: start
  title: ''
  type: Signup
  url: https://developer.bt.com/user/register
- group: start
  title: ''
  type: Login
  url: https://developer.bt.com/user/login
- group: other
  title: ''
  type: Search
  url: https://developer.bt.com/search
- group: other
  title: ''
  type: BTBusiness
  url: https://business.bt.com
- group: other
  title: ''
  type: BTWholesale
  url: https://www.btwholesale.com
- group: other
  title: ''
  type: EE
  url: https://ee.co.uk
- group: other
  title: ''
  type: Plusnet
  url: https://www.plusnet.com
- group: other
  title: ''
  type: Openreach
  url: https://www.openreach.com
- group: other
  title: ''
  type: GlobalServices
  url: https://www.globalservices.bt.com
- group: company
  title: ''
  type: BTGroupInvestors
  url: https://www.bt.com/about/investors
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.bt.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/BT-OpenSource
- group: build
  title: ''
  type: GitHubBTplc
  url: https://github.com/BTplc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/bt_uk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/btgroup
- group: company
  title: ''
  type: Careers
  url: https://www.bt.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.bt.com/help/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bt.com/legal/privacy-and-cookies
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bt.com/legal/terms-of-use
created: '2026-05-25'
description: 'BT Group plc (British Telecommunications) is the United Kingdom''s largest fixed-line, broadband, and mobile communications provider, headquartered in London with operations spanning consumer, business, wholesale, and global enterprise markets. The group is organised around three customer-facing brands — BT, EE, and Plusnet — and a wholesale division that sells capacity and access to other communications providers. BT Group operates the UK''s largest mobile network (EE), runs fibre and copper access through Openreach (a legally separate group company), and provides networked IT and security services to multinational enterprises and the UK public sector. The group publishes a public developer programme at developer.bt.com that exposes a growing catalogue of REST APIs across two main domains: charging and crediting (Direct Carrier Billing, Crediting, Premium SMS) and digital identity / fraud prevention (SIM Swap, Network Identity, Call Divert Protection), alongside wholesale
  and operational APIs (Broadband One, Quote Management, Address Management, Appointment Management, Product and Network Availability, HubCo Voice, Global Voice Services, IMEI Lookup, Home Network, Rail Insights, Location Insights for London, and a Travel Journey API Platform). The portal supports sandbox onboarding with Client ID / Client Secret OAuth 2.0 credentials and progression to production under a commercial agreement with an account team. In April 2025 BT announced a federated API management partnership with Kong (Kong Konnect) to consolidate its previously fragmented API estate, strengthen governance, and offer a self-service developer experience across the group.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bt-com.png
layout: provider
modified: '2026-05-25'
name: BT Group
nav: Providers
network: true
overview: 'BT Group publishes 15 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Telco, Mobile Network, Broadband, and Fibre.


  BT Group''s developer surface includes documentation, signup flow, GitHub presence, YouTube channel, and 25 more developer resources.'
random_paper: 114
score:
  band: emerging
  composite: 17.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bt-com/refs/heads/main/screenshots/bt-com-2026-06-20T173734.png
security:
- kind: domain-security
  name: Bt Com Domain Security
  slug: bt-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bt Com Vulnerability Disclosure
  slug: bt-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bt-com
tags:
- Telecommunications
- Telco
- Mobile Network
- Broadband
- Fibre
- Wholesale
- Network Identity
- SIM Swap
- Direct Carrier Billing
- Premium SMS
- Crediting
- Fraud Prevention
- Digital Identity
- Voice
- Ethernet
- Address Management
- Appointment Management
- Quote Management
- IMEI
- Rail
- Location Insights
- Travel
- Openreach
- EE
- Plusnet
- United Kingdom
- CAMARA
- Open Gateway
website: https://www.bt.com
---
