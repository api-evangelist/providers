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
api_count: 8
apis:
- description: OceanMedallion is Carnival Corporation's wearable IoT device and experience platform deployed across Princess Cruises and being adopted across other Carnival brands. The medallion enables keyless stat
  name: OceanMedallion
  slug: ocean-medallion
- description: The Princess MedallionClass app is the companion mobile experience for OceanMedallion. It manages pre-cruise planning, online check-in, shore-excursion booking, dining reservations, onboard purchases,
  name: Princess MedallionClass App
  slug: medallion-class-app
- description: The Carnival HUB app is the official Carnival Cruise Line companion app for managing pre-cruise check-in, daily schedules, dining reservations, shore excursions, onboard messaging with travel companio
  name: Carnival HUB App
  slug: carnival-hub-app
- description: The Holland America Navigator app is the companion mobile app for Holland America Line guests offering itinerary management, dining reservations, shore-excursion booking, account management, and onboa
  name: Holland America Navigator App
  slug: holland-america-navigator
- description: Carnival VIFP (Very Important Fun Person) Club is Carnival Cruise Line's loyalty program with tiered status based on cruise days. Members receive priority booking, onboard perks, complimentary service
  name: Carnival VIFP Club
  slug: carnival-vifp-club
- description: Princess Captain's Circle is Princess Cruises' loyalty program offering tiered membership benefits including priority embarkation, onboard perks, exclusive events, and members-only offers based on num
  name: Princess Captain's Circle
  slug: princess-captains-circle
- description: Mariner Society is Holland America Line's loyalty program offering tiered benefits including stateroom upgrades, onboard credit, complimentary internet, and priority services for repeat guests.
  name: Holland America Mariner Society
  slug: holland-america-mariner-society
- description: Each Carnival Corporation brand operates its own online booking portal for cruise search, itinerary selection, stateroom selection, payment, and reservation management. Travel-agent variants integrate
  name: Carnival Brand Booking Portals
  slug: cruise-booking-portal
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carnival-corporation-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.carnivalcorp.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carnival-corporation
- group: company
  title: ''
  type: Website
  url: https://www.carnivalcorp.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.carnivalcorp.com/investor-relations
- group: other
  title: ''
  type: Brands
  url: https://www.carnivalcorp.com/our-brands
- group: other
  title: ''
  type: Sustainability
  url: https://www.carnivalcorp.com/sustainability
created: '2026-05-05'
description: Carnival Corporation & plc is the world's largest cruise company operating eight cruise line brands (Carnival Cruise Line, Princess Cruises, Holland America Line, Seabourn, Cunard, P&O Cruises, Costa Cruises, AIDA Cruises), plus the White Pass and Yukon Route. Carnival operates the OceanMedallion wearable IoT technology and mobile experience platform, the Carnival HUB app, the Princess MedallionClass app, and a portfolio of guest-facing digital experiences across its fleet of over 90 ships.
features:
- description: OceanMedallion personalizes the onboard guest experience using BLE-based wearables.
  name: Wearable IoT Cruise Experience
- description: Brand-specific mobile apps for onboard navigation, dining, and service requests.
  name: Mobile Cruise Apps
- description: Pre-cruise digital check-in for embarkation across all Carnival brands.
  name: Online Check-In
- description: Browse and reserve port-of-call excursions through brand apps and websites.
  name: Shore Excursion Booking
- description: Make and manage specialty-dining reservations digitally.
  name: Dining Reservations
- description: Tiered repeat-guest loyalty programs across all major brands.
  name: Loyalty Programs
- description: Travel-agent-facing booking systems for all Carnival brands.
  name: Travel Agent Tools
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carnival-corporation.png
integrations:
- description: Subsidiary brand operating MedallionClass and Captain's Circle programs.
  name: Princess Cruises
- description: Subsidiary brand operating Carnival HUB app and VIFP Club loyalty.
  name: Carnival Cruise Line
- description: Subsidiary brand operating Navigator app and Mariner Society loyalty.
  name: Holland America Line
- description: Subsidiary ultra-luxury cruise brand.
  name: Seabourn
- description: Subsidiary heritage transatlantic and luxury cruise brand.
  name: Cunard
- description: UK-market cruise brand subsidiary.
  name: P&O Cruises
- description: European Mediterranean cruise brand subsidiary.
  name: Costa Cruises
- description: German-market cruise brand subsidiary.
  name: AIDA Cruises
- description: Skagway, Alaska railroad and port retail operation.
  name: White Pass and Yukon Route
layout: provider
modified: '2026-05-16'
name: Carnival Corporation
nav: Providers
network: true
overview: 'Carnival Corporation publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cruise Lines, Travel, Hospitality, Mobile Apps, and Loyalty.


  Carnival Corporation''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 39
score:
  band: minimal
  composite: 6.9
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carnival-corporation/refs/heads/main/screenshots/carnival-corporation-2026-06-20T174014.png
security:
- kind: domain-security
  name: Carnival Corporation Domain Security
  slug: carnival-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carnival-corporation
tags:
- Cruise Lines
- Travel
- Hospitality
- Mobile Apps
- Loyalty
- Wearables
use_cases:
- description: Search, book, and plan multi-segment cruise vacations across global itineraries.
  name: Cruise Vacation Planning
- description: Use wearable and mobile technology to personalize service throughout the voyage.
  name: Onboard Experience Personalization
- description: Mobile apps let family groups coordinate dining, excursions, and onboard activities.
  name: Family Cruise Coordination
- description: Encourage repeat bookings through tiered loyalty programs.
  name: Repeat-Guest Loyalty Engagement
- description: Travel-agency channel partnerships using agent-facing booking tools.
  name: Travel Agent Bookings
website: https://www.carnivalcorp.com/
---
