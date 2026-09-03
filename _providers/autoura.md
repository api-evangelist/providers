---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Autoura Experience API provides access to tourism content including cuisine guides, destination information, tour itineraries, local activities, and points of interest. Developers can integrate Au
  name: Autoura Experience API
  slug: autoura-api
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autoura-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Autoura
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/autoura
- group: company
  title: ''
  type: Website
  url: https://www.autoura.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.autoura.com/docs/api/cuisines
- group: agent
  title: ''
  type: LlmsText
  url: https://www.autoura.com/llms.txt
created: '2025-03-01'
description: Autoura is a digital experience platform for real-world tourism and travel experiences. They develop software and APIs that enable travel companies, destination management organizations, and developers to access and integrate tourism content including destination information, tour itineraries, cuisine guides, activities, and interactive local experience recommendations.
features:
- description: Access rich destination content including local attractions, points of interest, neighborhood guides, and cultural highlights for tourism applications and travel content platforms.
  name: Destination Content API
- description: Comprehensive cuisine data including local dishes, restaurant types, food tours, and gastronomic experience recommendations for culinary tourism applications.
  name: Cuisine and Food Guide API
- description: Pre-built tour itineraries and self-guided tour content for destinations, enabling travel apps to offer structured sightseeing experiences.
  name: Tour Itineraries
- description: Activity and experience data for destinations including outdoor activities, cultural experiences, adventure tourism, and seasonal events.
  name: Activity Recommendations
- description: Context-aware recommendation engine for suggesting local experiences based on traveler preferences, location, and time of visit.
  name: Personalized Recommendations
finops:
- name: Autoura Finops
  service_category: API
  slug: autoura-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autoura.png
integrations:
- description: Integration with travel booking platforms to surface Autoura activity and experience content alongside accommodation and transport bookings.
  name: Booking Platforms
- description: Combine Autoura POI and destination content with Google Maps, Mapbox, or Apple Maps for location-aware tourism applications.
  name: Mapping Services
- description: Embed Autoura destination content into CMS-based tourism websites using API integrations for dynamic content delivery.
  name: CMS Platforms
layout: provider
modified: '2026-04-19'
name: Autoura
nav: Providers
network: true
overview: 'Autoura publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tourism, Tours, Travel, Destinations, and Experience.


  Autoura''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Autoura Plans Pricing
  plan_count: 3
  slug: autoura-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Autoura Rate Limits
  slug: autoura-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autoura/refs/heads/main/screenshots/autoura-2026-06-20T172710.png
security:
- kind: domain-security
  name: Autoura Domain Security
  slug: autoura-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autoura
tags:
- Tourism
- Tours
- Travel
- Destinations
- Experience
- Digital Tourism
use_cases:
- description: Integrate Autoura destination content into travel booking apps and tourism portals to enhance destination discovery and trip planning.
  name: Travel App Integration
- description: Destination management organizations embed Autoura experience content into tourism websites to promote local attractions and activities.
  name: Destination Marketing
- description: Food and travel platforms use the Cuisine API to build gastronomic guides and food tour features for culinary travelers.
  name: Culinary Tourism
- description: Build digital tour guide applications with self-guided audio tours, interactive maps, and Autoura destination content.
  name: Digital Tour Guide Apps
website: https://www.autoura.com
---
