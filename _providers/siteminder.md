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
api_count: 5
apis:
- description: pmsXchange is SiteMinder's integration API for property management systems (PMS), revenue management systems (RMS), and central reservation systems (CRS) that need to synchronize rooms, rates, availab
  name: SiteMinder pmsXchange API
  slug: pmsxchange-api
- description: SiteConnect is SiteMinder's integration API for booking channels such as online travel agencies, wholesalers, global distribution systems, and metasearch partners that contract directly with hotels. T
  name: SiteMinder SiteConnect API
  slug: siteconnect-api
- description: Channels Plus is SiteMinder's REST and JSON booking channel API that lets partners connect to many SiteMinder properties through a single integration without negotiating individual hotel contracts. It
  name: SiteMinder Channels Plus API
  slug: channels-plus-api
- description: SMX is SiteMinder's API for metasearch publishers and hotel application providers that need a single standardized connection to the SiteMinder platform and its network of connected property management
  name: SiteMinder SMX API
  slug: smx-api
- description: The Direct Booking API is a REST and JSON service that lets hotel groups on SiteMinder's Multi-Property platform power custom direct booking flows on their own websites and mobile apps. It exposes pro
  name: SiteMinder Direct Booking API
  slug: direct-booking-api
artifact_total: 40
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/siteminder-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siteminder-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.siteminder.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.siteminder.com/get-started/get-started
- group: start
  title: ''
  type: Signup
  url: https://www.siteminder.com/developer-guide/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.siteminder.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://developer.siteminder.com/integration-support/integration-support
- group: operate
  title: ''
  type: FAQ
  url: https://developer.siteminder.com/get-started/resources/faq
- group: other
  title: ''
  type: Glossary
  url: https://developer.siteminder.com/get-started/resources/glossary
- group: company
  title: ''
  type: Blog
  url: https://www.siteminder.com/r/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.siteminder.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.siteminder.com/legal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SiteMinder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/siteminder
- group: company
  title: ''
  type: Careers
  url: https://www.siteminder.com/careers/
- group: company
  title: ''
  type: PartnerPrograms
  url: https://www.siteminder.com/partner-programs/
created: '2026-05-25'
description: SiteMinder is an Australian hotel commerce platform (ASX SDR) that connects hotels with more than 450 online distribution channels, including OTAs (Booking.com, Expedia, Airbnb, Agoda), metasearch sites (Google, Trivago, TripAdvisor), and global distribution systems. Through its developer portal at developer.siteminder.com, SiteMinder publishes five integration APIs spanning property management system connectivity (pmsXchange), booking channel distribution (SiteConnect, Channels Plus), metasearch publication (SMX), and direct booking flows (Direct Booking API). The platform serves more than 53,000 properties across 150 countries and manages over three million hotel rooms.
features:
- description: Distribute room inventory, rates, and restrictions across 450+ online distribution channels including OTAs, GDS systems, metasearch, and wholesalers from a single platform.
  name: Channel Distribution
- description: Two-way synchronization with property management, revenue management, and central reservation systems through the pmsXchange API.
  name: PMS, RMS, and CRS Connectivity
- description: Centralized control of inventory, rates, and bookings across hotel groups via SiteMinder's Multi-Property platform.
  name: Multi-Property Management
- description: Programmatic access to property data, room types, rates, and quotes for building branded direct booking flows on hotel-owned web and mobile properties.
  name: Direct Booking Engine
- description: SMX API standardizes connectivity between hotel applications and metasearch publishers for real-time availability and rate publication.
  name: Metasearch Publishing
- description: Channels Plus Net Rates Program allows wholesale-style distribution with contracted net pricing between SiteMinder properties and connecting channels.
  name: Net Rates and Wholesale Distribution
- description: Channels Plus exposes a companion MCP server so AI agents can shop, lock, and confirm reservations against SiteMinder inventory.
  name: Model Context Protocol Server
- description: Curated marketplace where SiteMinder properties discover and connect certified PMS, RMS, CRS, and application partners.
  name: Hotel App Store
- description: Self-service portal where Channels Plus partners manage deals, invoicing, cancellation policies, commissions, and API keys.
  name: Partner Portal
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siteminder.png
integrations:
- description: Online travel agency distribution partner connected through SiteMinder's channel manager.
  name: Booking.com
- description: Online travel agency distribution partner including Hotels.com and Vrbo brands.
  name: Expedia
- description: Vacation rental and alternative accommodation distribution partner.
  name: Airbnb
- description: Asia-Pacific online travel agency distribution partner.
  name: Agoda
- description: Metasearch and free booking links distribution partner.
  name: Google Hotels
- description: Metasearch distribution partner for hotel rates and availability.
  name: Trivago
- description: Reviews and metasearch distribution partner.
  name: TripAdvisor
- description: Cloud-native property management system integrated through pmsXchange.
  name: Mews
- description: Hospitality management platform integrated through pmsXchange.
  name: Cloudbeds
- description: OPERA and Suite8 property management systems integrated through pmsXchange.
  name: Oracle Hospitality
- description: Open API-first property management platform integrated through pmsXchange.
  name: Apaleo
- description: Global distribution systems integrated through SiteConnect for corporate travel and travel agent distribution.
  name: Amadeus, Sabre, and Travelport
layout: provider
mcp_servers:
- description: ''
  name: overview
  slug: overview
modified: '2026-05-25'
name: SiteMinder
nav: Providers
network: true
overview: 'SiteMinder publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, Hotel Distribution, Channel Manager, Booking Engine, and Travel.


  SiteMinder''s developer surface includes developer portal, getting-started guide, signup flow, pricing, support, FAQ, engineering blog, and 9 more developer resources.'
random_paper: 32
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siteminder/refs/heads/main/screenshots/siteminder-2026-06-20T193959.png
security:
- kind: domain-security
  name: Siteminder Domain Security
  slug: siteminder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Siteminder Vulnerability Disclosure
  slug: siteminder-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: siteminder
solutions:
- description: Single-property channel management, booking engine, and revenue tooling for independent operators.
  name: Independent Hotels
- description: Multi-Property platform with centralized rates, inventory, and reporting plus the Direct Booking API for branded booking flows.
  name: Hotel Groups and Chains
- description: SiteConnect and Channels Plus for OTAs, wholesalers, GDS, and metasearch providers connecting to SiteMinder's property network.
  name: Booking Channel Partners
- description: pmsXchange integration program with App Store listing and access to 47,000+ connected properties.
  name: PMS, RMS, and CRS Vendors
- description: SMX API for upsell, guest experience, housekeeping, and revenue management applications that need a single integration into the SiteMinder PMS network.
  name: Hotel Application Providers
tags:
- Hospitality
- Hotel Distribution
- Channel Manager
- Booking Engine
- Travel
- Property Management
- Reservations
use_cases:
- description: Property staff push availability, restrictions, and rates to hundreds of booking channels and ingest reservations through a single API integration.
  name: Hotel Channel Distribution
- description: Property management system vendors connect their software to SiteMinder via pmsXchange to give shared customers two-way distribution and reservation sync.
  name: PMS Integration
- description: Online travel agencies and wholesalers integrate with SiteConnect or Channels Plus to access bookable inventory across thousands of hotels.
  name: OTA and Wholesaler Connectivity
- description: Hotel groups build custom branded booking websites and mobile apps that pull property, room, and rate data live from SiteMinder via the Direct Booking API.
  name: Direct Booking Site Build
- description: Metasearch publishers and hotel applications use SMX to publish rates and availability and ingest bookings across SiteMinder's PMS network.
  name: Metasearch Publication
- description: AI agents and assistants shop and book hotel inventory through the Channels Plus MCP server using Model Context Protocol tools.
  name: AI Agent Booking
website: https://developer.siteminder.com/
---
