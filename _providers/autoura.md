---
access_model:
  confidence: high
  label: Paid subscription, with a published public test API key for evaluation
  onboarding: self-serve
  pricing: paid
  public: true
  source:
  - plans
  - docs
  trial: false
  try_now: true
api_count: 2
apis:
- description: The Autoura Experience API provides access to tourism content including cuisine guides, destination information, tour itineraries, local activities, and points of interest. Developers can integrate Au
  name: Autoura Experience API
  slug: autoura-api
- description: 'Autoura''s hosted remote Model Context Protocol server, the surface it builds for AI agents first. One endpoint carries two permission-scoped tool sets: a B2B set for brands, attractions, tour operator'
  name: Autoura MCP Server
  slug: autoura-mcp
artifact_total: 22
asyncapis:
- description: ''
  name: Autoura Webhooks
  slug: autoura-webhooks
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
  url: https://www.autoura.com/docs/api
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autoura-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/autoura-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autoura-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autoura-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autoura-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autoura-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autoura-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autoura-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/autoura-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autoura-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autoura-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/autoura-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/autoura-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/autoura-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/autoura-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autoura-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autoura-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://www.autoura.com/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.autoura.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.autoura.com/docs/api/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autoura.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.autoura.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autoura.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autoura.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.autoura.com/contact
created: '2025-03-01'
description: 'Autoura is a UK digital experience platform (DXP) for real-world tourism and travel experiences, operated by The Spontaneous Travel Company Limited. It structures and maintains experience data — venues, attractions, tours, routes, stops, accessibility and dietary signals, AI guide characters and storytelling — so travel companies, destination management organizations and, increasingly, AI agents can act on it. Autoura is agent-native rather than agent-adjacent: it advertises its own agent skill from a link rel="ai-skill" element in its homepage head, runs a hosted remote MCP server behind OAuth 2.1 with PKCE and dynamic client registration, exposes the same tool set as WebMCP on its PlanMyVisit consumer product, and addresses consumer profiles by DID with DIDComm v2 messaging. A REST API over api.autoura.com serves routes, stops, visits, characters, MoveMe audio and a consent-brokered consumer preference graph, with dietary requirements keyed on IATA airline special-meal codes.'
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
mcp_servers:
- description: ''
  name: Autoura MCP Server
  slug: autoura-mcp-server
modified: '2026-09-13'
name: Autoura
nav: Providers
network: true
overview: 'Autoura publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Tourism, Tours, Travel, Destinations, and Experience.


  The Autoura catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Autoura''s developer surface includes documentation, authentication, changelog, sandbox, API reference, getting-started guide, pricing, and 24 more developer resources.'
plans:
- name: Autoura Plans Pricing
  plan_count: 3
  slug: autoura-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Autoura Rate Limits
  slug: autoura-rate-limits
scopes:
- name: Autoura Scopes
  scope_count: 3
  slug: autoura-scopes
  summary_line: 3 scopes · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/autoura/refs/heads/main/screenshots/autoura-2026-06-20T172710.png
security:
- kind: authentication
  name: Autoura Authentication
  slug: autoura-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 6 schemes
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
