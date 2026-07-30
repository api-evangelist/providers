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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Token-authenticated HTTPS REST API used by individual devices to read and write datastream values, batch update multiple datastreams, retrieve historical data, set widget and datastream properties, tr
  name: Blynk Device HTTPS API
  slug: blynk-device-https-api
- description: Enterprise-tier OAuth2 REST API for full programmatic CRUD across Blynk Cloud tenancy. Resources include devices (create from template, list, search, online status, tags, timeline, update, delete), us
  name: Blynk Platform HTTPS API
  slug: blynk-platform-https-api
- description: Bi-directional low-latency streaming connection protocol used by the Blynk Library and Blynk.Edgent to maintain a persistent link between devices and Blynk.Cloud. Optimized for constrained MCUs (Ardui
  name: Blynk Device Streaming Protocol
  slug: blynk-device-streaming-protocol
artifact_total: 27
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blynk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blynk.io
- group: start
  title: ''
  type: Portal
  url: https://docs.blynk.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blynk.io/en/getting-started/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blynk.io/en/getting-started
- group: start
  title: ''
  type: Signup
  url: https://blynk.cloud/dashboard/register
- group: start
  title: ''
  type: Login
  url: https://blynk.cloud/dashboard/login
- group: start
  title: ''
  type: Console
  url: https://blynk.cloud
- group: other
  title: ''
  type: MobileApp
  url: https://blynk.io/blynk-iot-mobile-app
- group: commercial
  title: ''
  type: Pricing
  url: https://blynk.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://blynk.io/pricing
- group: other
  title: ''
  type: CaseStudies
  url: https://blynk.io/case-studies
- group: other
  title: ''
  type: Customers
  url: https://blynk.io/customers
- group: company
  title: ''
  type: Blog
  url: https://blynk.io/resources/blog
- group: other
  title: ''
  type: Resources
  url: https://blynk.io/resources
- group: operate
  title: ''
  type: Forums
  url: https://community.blynk.cc
- group: operate
  title: ''
  type: Support
  url: https://blynk.io/contact-us
- group: operate
  title: ''
  type: Contact
  url: https://blynk.io/contact-us
- group: company
  title: ''
  type: AboutUs
  url: https://blynk.io/about-us
- group: company
  title: ''
  type: Careers
  url: https://blynk.io/careers
- group: company
  title: ''
  type: Partners
  url: https://blynk.io/partners
- group: auth
  title: ''
  type: Security
  url: https://blynk.io/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blynk.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blynk.io/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: https://docs.blynk.io/en/blynk.cloud/platform-https-api
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.blynk.io/en/blynk.cloud/platform-https-api
- group: design
  title: ''
  type: Webhooks
  url: https://docs.blynk.io/en/blynk.cloud/platform-https-api/webhooks.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blynkkk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/blynkkk/blynk-library
- group: build
  title: ''
  type: SDKs
  url: https://github.com/blynkkk/blynk-library
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Blynk-Technologies/Edgent-PlatformIO
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Blynk-Technologies/Blynk-NCP-Example-Arduino
- group: other
  title: ''
  type: Templates
  url: https://github.com/blynkkk/blueprints
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/us/app/blynk-iot/id1559317868
- group: other
  title: ''
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=cloud.blynk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/blynk_app
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blynkk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/blynk
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/blynkapp
created: '2026-05-25'
description: Blynk is a low-code / no-code IoT software platform that helps companies prototype, deploy, and remotely manage connected devices and applications across consumer and commercial markets. The platform combines four components — Blynk.Console (web dashboard), Blynk.Apps (white-labeled iOS and Android apps), Blynk.Edgent (device-side connection library), and Blynk.Cloud (managed backend) — into a full-stack offering that removes the need to build custom IoT infrastructure. Developers can build interactive mobile and web dashboards with a drag-and-drop builder, connect hardware over Wi-Fi, Cellular, LoRaWAN, Ethernet, or satellite, and operate fleets with provisioning, OTA firmware updates, multi-tenancy, automations, webhooks, and SOC 2 cloud infrastructure. Commercial customers use Blynk for branded consumer products, industrial monitoring, agriculture, energy and HVAC, smart cities, and smart buildings, with more than 5,000 companies and 1M+ developers on the platform. Blynk
  exposes two HTTPS REST APIs — the Device HTTPS API for telemetry and command exchange from individual hardware units, and the Platform HTTPS API (Enterprise plan) for full programmatic CRUD over devices, users, organizations, templates, automations, webhooks, and tags using OAuth2 client-credential authentication.
features:
- Drag-and-drop mobile app builder for iOS and Android (Blynk.Apps)
- Web console for device management, dashboards, and fleet operations (Blynk.Console)
- White-label branded apps for commercial deployments
- Over-the-air (OTA) firmware updates with rollout management
- Device provisioning, claiming, and lifecycle management
- Multi-tenancy with organizations and sub-organizations
- Real-time bi-directional streaming protocol via Blynk Library
- Device HTTPS API for token-authenticated telemetry and commands
- Platform HTTPS API with OAuth2 for full CRUD across devices, users, templates, automations, webhooks, tags
- MQTT support for device connectivity
- Webhooks for outbound integrations
- Automations engine (event-driven rules) and scheduling
- Multi-protocol device connectivity — Wi-Fi, Ethernet, Cellular, LoRaWAN, Satellite
- Pre-integrated with hundreds of MCU boards (Arduino, ESP32, ESP8266, Raspberry Pi, Particle, Nordic)
- Blynk.Edgent — packaged device-side connectivity stack
- Blynk.NCP — network co-processor reference design
- SOC 2 compliant managed cloud infrastructure (Blynk.Cloud)
- On-premise / private-server option for Enterprise customers
- SMS and push notifications, email alerts
- Custom branding, app store publishing for white-label apps
- Data retention from 1 week (Free) to 12 months (Production) to custom (Enterprise)
- Rate limit of 10,000 Platform API requests per minute per organization
- 99.95% uptime SLA on Production plan, 99.99% on Enterprise
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blynk.png
layout: provider
modified: '2026-05-25'
name: Blynk
nav: Providers
network: true
overview: 'Blynk publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Internet of Things, No-Code, Low-Code, and Connected Devices.


  Blynk''s developer surface includes developer portal, documentation, getting-started guide, signup flow, developer console, pricing, engineering blog, and 32 more developer resources.'
random_paper: 52
score:
  band: thin
  composite: 29.8
  delta: -2.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blynk/refs/heads/main/screenshots/blynk-2026-06-20T173539.png
security:
- kind: domain-security
  name: Blynk Domain Security
  slug: blynk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blynk
tags:
- IoT
- Internet of Things
- No-Code
- Low-Code
- Connected Devices
- Device Management
- Fleet Management
- Mobile Apps
- Dashboards
- Telemetry
- Firmware
- Over The Air Updates
- White Label
- Embedded
- Smart Home
- Smart Buildings
- Smart Cities
- Industrial
- Agriculture
- Energy
website: https://blynk.io
---
