---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Verizon Network APIs provide authentication, fraud prevention, and device intelligence capabilities leveraging Verizon's mobile network. Includes Number Verification API for seamless device authentica
  name: Verizon Network APIs
  slug: network-apis
- description: ThingSpace gives organizations of all sizes tools to build IoT solutions, manage connected devices, and solve business problems end-to-end. Provides device connectivity management, diagnostics, softwa
  name: Verizon ThingSpace IoT API
  slug: thingspace
- description: Verizon 5G Edge API enables developers to build ultra-low-latency applications by leveraging Verizon's multi-access edge computing (MEC) infrastructure. Provides discovery, session management, and loc
  name: Verizon 5G Edge API
  slug: 5g-edge
- description: Verizon provides a suite of TM Forum certified service management APIs exposing ITIL functions for inventory management, incident management, change management, event management, problem management, o
  name: Verizon TM Forum Service Management APIs
  slug: service-management
- description: Verizon Communications Platform as a Service (CPaaS) offering provides APIs for inbound and outbound IP interactive voice response (IPIVR) and call detail reporting. Available exclusively for IP Conta
  name: Verizon Voice API (CPaaS)
  slug: voice-api
artifact_total: 25
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verizon-communications-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verizon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verizon
- group: company
  title: ''
  type: Website
  url: https://www.verizon-communications.com
- group: start
  title: ''
  type: Portal
  url: https://developers.verizon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.verizon.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.verizon.com/#/apis/ns/documentation/help
- group: operate
  title: ''
  type: FAQ
  url: https://developers.verizon.com/#/apis/ns/documentation/frequently-asked-questions
- group: start
  title: ''
  type: Login
  url: https://secure.verizon.com/signin?goto=https://developers.verizon.com/apis/sec/v1/login
- group: start
  title: ''
  type: Signup
  url: https://secure.verizon.com/account/register/start?goto=https%3A%2F%2Fdevelopers.verizon.com%2Fapis%2Fsec%2Fv1%2Flogin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.verizon.com/about/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.verizon.com/about/terms-conditions/
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.verizon.com/llms.txt
created: '2026-05-03'
description: Verizon Communications is one of the world's leading providers of technology and communications services, offering wireless, wireline, broadband, and global enterprise services to consumers, businesses, and government customers. Verizon exposes developer APIs for network capabilities including SIM swap detection, number verification, IoT device management via ThingSpace, 5G edge computing, contact center voice APIs, and TM Forum-certified service management APIs for enterprise customers.
features:
- description: Seamless authentication of end-user mobile devices via network-based verification, eliminating passwords and one-time codes.
  name: Number Verification
- description: Check if a SIM card associated with a phone number has been recently changed to detect account takeover fraud.
  name: SIM Swap Detection
- description: Full lifecycle management of IoT devices including connectivity, diagnostics, software updates, and location tracking via ThingSpace.
  name: IoT Device Management
- description: Multi-access edge computing APIs for deploying ultra-low-latency applications on Verizon's 5G MEC infrastructure.
  name: 5G Edge Computing
- description: TM Forum-certified ITIL APIs for enterprise service management including inventory, incident, change, order, and billing management.
  name: TM Forum Open APIs
- description: CPaaS APIs for customized IP interactive voice response (IPIVR) and call detail reporting for contact center operations.
  name: Contact Center Voice APIs
finops:
- name: Verizon Communications Finops
  service_category: Telecommunications
  slug: verizon-communications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verizon-communications.png
integrations:
- description: Integrate TM Forum service management APIs with ITSM platforms like ServiceNow for automated incident and change management.
  name: ITSM Platforms
- description: Embed Number Verification and SIM Swap APIs into authentication flows and identity provider SDKs.
  name: Identity Providers
- description: Connect ThingSpace device management APIs to IoT platforms and enterprise data lakes.
  name: IoT Platforms
- description: Deploy 5G Edge applications across Verizon's MEC nodes in partnership with AWS Wavelength and Google Cloud.
  name: Edge Cloud Providers
layout: provider
modified: '2026-05-03'
name: Verizon Communications
nav: Providers
network: true
overview: 'Verizon Communications publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, Wireless, Network APIs, IoT, and 5G.


  Verizon Communications'' developer surface includes developer portal, documentation, support, FAQ, signup flow, and 8 more developer resources.'
plans:
- name: Verizon Communications Plans Pricing
  plan_count: 1
  slug: verizon-communications-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Verizon Communications Rate Limits
  slug: verizon-communications-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -3.3
  facets:
    commercial_clarity: 63.2
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verizon-communications/refs/heads/main/screenshots/verizon-communications-2026-06-20T200941.png
security:
- kind: domain-security
  name: Verizon Communications Domain Security
  slug: verizon-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verizon-communications
tags:
- Telecommunications
- Wireless
- Network APIs
- IoT
- 5G
- Enterprise
- Identity
- Fortune 100
use_cases:
- description: Use SIM Swap and Number Verification APIs to protect users from account takeover and SIM-swapping fraud.
  name: Fraud Prevention
- description: Authenticate users seamlessly via mobile network without passwords using Number Verification API.
  name: Passwordless Authentication
- description: Manage large-scale IoT device fleets with connectivity monitoring, remote diagnostics, and over-the-air software updates.
  name: IoT Fleet Management
- description: Build edge-native applications leveraging ultra-low latency of Verizon's 5G MEC infrastructure.
  name: 5G Application Development
- description: Automate IT service management workflows using TM Forum-certified APIs integrated with ITSM platforms.
  name: Enterprise Service Automation
- description: Build customized IVR and call routing solutions using Verizon's CPaaS Voice API.
  name: Contact Center Modernization
website: https://www.verizon-communications.com
---
