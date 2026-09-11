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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-09-10'
api_count: 1
apis:
- baseURL: https://json.astrologyapi.com/v1
  baseurl_source: declared
  description: 'The AstrologyAPI JSON API — 158 documented operations covering Vedic (Jyotish) and Western astrology, Human Design and AstroCartoGraphy. Includes birth details, planetary positions, divisional and KP '
  name: Astrology API
  slug: astrology-api
- baseURL: https://pdf.astrologyapi.com/v1
  baseurl_source: declared
  description: White-labeled PDF report generation for Vedic and Western astrology — mini, basic and professional Kundli, matchmaking, gemstone, Varshaphal, pro numerology, natal, solar return, life forecast, synast
  name: AstrologyAPI PDF Reports API
  slug: astrology-api-pdf
- baseURL: https://vision.astrologyapi.com
  baseurl_source: declared
  description: Image-based palm reading. Submit a palm photograph as a public URL or base64 data URL (jpeg, jpg, png or webp, up to 5MB) together with a date of birth and gender to obtain a palm_id, then read struct
  name: AstrologyAPI Palmistry API
  slug: astrology-api-palmistry
- baseURL: https://vision.astrologyapi.com/face-reading
  baseurl_source: declared
  description: Image-based face reading. Submit a face photograph with date of birth and gender to obtain a face_id, then read structured analysis of face shape, eyes, nose, cheeks and cheekbones, mouth, chin and ja
  name: AstrologyAPI Face Reading API
  slug: astrology-api-face-reading
- description: First-party hosted Model Context Protocol server exposing AstrologyAPI's calculation engine to LLM agents and IDEs. The provider advertises 109 tools spanning Vedic and Western astrology, configured w
  name: AstrologyAPI MCP Server
  slug: astrology-api-mcp
artifact_total: 27
asyncapis:
- description: ''
  name: Astrology Api Webhooks
  slug: astrology-api-webhooks
collections:
- collection_type: postman
  name: Astrocartography Collection
  slug: postman-ACG
- collection_type: postman
  name: Human Design APIs Collection
  slug: postman-HD_Collection
- collection_type: open
  name: API Collection
  slug: open-astrology-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.astrologyapi.com/
- group: start
  title: Developer Hub
  type: DeveloperPortal
  url: https://astrologyapi.com/developers/v1
- group: docs
  title: Documentation
  type: Documentation
  url: https://astrologyapi.com/docs
- group: docs
  title: API Reference
  type: APIReference
  url: https://astrologyapi.com/developers/v1/api-reference
- group: docs
  title: Guides & Tutorials
  type: Documentation
  url: https://astrologyapi.com/developers/v1/guides
- group: start
  title: Quick Start
  type: GettingStarted
  url: https://astrologyapi.com/developers/v1/quick-start
- group: start
  title: Sign Up — 150 free credits
  type: SignUp
  url: https://astrologyapi.com/signup
- group: start
  title: Sign In
  type: Login
  url: https://astrologyapi.com/login
- group: commercial
  title: Pricing
  type: Pricing
  url: https://astrologyapi.com/pricing
- group: operate
  title: Contact Support
  type: Support
  url: https://astrologyapi.com/contact
- group: operate
  title: FAQ
  type: HelpCenter
  url: https://www.astrologyapi.com/faq
- group: company
  title: Blog
  type: Blog
  url: https://astrologyapi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astrologyapi
- group: build
  title: Postman Collections
  type: Postman
  url: https://astrologyapi.com/developers/v1/postman-collection
- group: commercial
  title: Terms of Service
  type: TermsOfService
  url: https://astrologyapi.com/legal/terms-service
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://astrologyapi.com/legal/privacy-policy
- group: operate
  title: API Status
  type: StatusPage
  url: https://www.astrologyapi.com/api-status
- group: operate
  title: Change Log
  type: ChangeLog
  url: https://astrologyapi.com/developers/v1/change-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/astrology-api-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astrology-api-lifecycle.yml
- group: build
  title: ''
  type: SDKs
  url: packages/astrology-api-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/astrology-api-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/astrology-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/astrology-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astrology-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/astrology-api-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/astrology-api-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/astrology-api-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/astrology-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/astrology-api-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astrology-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/astrology-api-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/astrology-api-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/astrology-api-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/astrology-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/astrology-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/astrology-api-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrology-api-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/astrology-api-vulnerability-disclosure.yml
created: '2025-01-07'
description: AstrologyAPI (astrologyapi.com) is a developer-first astrology calculation platform, in production since 2013, providing 300+ REST endpoints across Vedic (Jyotish) and Western traditions under a single API key. Coverage includes Kundli and divisional charts, Vimshottari and Yogini dashas, KP sub-lords, Lal Kitab, Varshaphal, Shadbala and Bhavabala strength scoring, panchang and muhurta, Ashtakoot and Dashakoot matchmaking, natal, synastry, composite and solar-return charts, transits, AstroCartoGraphy, Human Design, numerology, tarot, palmistry and face reading, plus multi-language horoscope content feeds and white-labeled PDF report generation. The platform also runs a hosted MCP server exposing its calculation tools to LLM agents, and a chart-grounded AI chat product. Billing is a pay-as-you-go credit wallet in INR with optional suite subscriptions.
features:
- description: Vedic astrology data including birth chart basics, horoscope dosha analysis, yearly predictions (Varshaphal), daily nakshatra forecasts, and panchang (Hindu almanac) data.
  name: Indian (Vedic) Astrology
- description: Western astrology data including birth chart basics, numerology, synastry (relationship analysis), moon phases, planetary transits, and zodiac compatibility.
  name: Western Astrology
- description: Daily, weekly, and monthly horoscope predictions for all sun signs in both Western and Vedic astrology traditions.
  name: Horoscope Predictions
- description: General tarot card readings and yes/no tarot predictions for integrating tarot functionality into applications.
  name: Tarot API
- description: Generate detailed PDF horoscope reports in five types covering both Western and Indian astrology formats for end-user delivery.
  name: PDF Report Generation
finops:
- name: Astrology Api Finops
  service_category: API
  slug: astrology-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astrology-api.png
integrations:
- description: Official Postman collection available for testing Astrology API endpoints before integration.
  name: Postman Collection
- description: Language-specific SDK downloads available for easier integration with the Astrology API.
  name: SDK Downloads
layout: provider
mcp_servers:
- description: AstrologyAPI operates a first-party hosted MCP server that exposes its astrology calculation engine to LLM agents and IDEs. The endpoint, the header name and the tool count below are quoted from the p
  name: AstrologyAPI MCP Server
  slug: astrologyapi-mcp-server
modified: '2026-09-07'
name: Astrology API
nav: Providers
network: true
overview: 'Astrology API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Astrology API, AstrologyAPI PDF Reports API, AstrologyAPI Palmistry API, and 1 more. Tagged areas include Astrology, Horoscopes, Zodiac, Vedic Astrology, and Western Astrology.


  The Astrology API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Astrology API''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 33 more developer resources.'
plans:
- name: Astrology Api Plans Pricing
  plan_count: 5
  slug: astrology-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Astrology Api Rate Limits
  slug: astrology-api-rate-limits
scopes:
- name: Astrology Api Scopes
  scope_count: 0
  slug: astrology-api-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 60.7
    developer_ergonomics: 78.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 61.1
  provenance:
    conformance: first-party
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/astrology-api/refs/heads/main/screenshots/astrology-api-2026-06-20T172511.png
security:
- kind: authentication
  name: Astrology Api Authentication
  slug: astrology-api-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Astrology Api Domain Security
  slug: astrology-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Astrology Api Vulnerability Disclosure
  slug: astrology-api-vulnerability-disclosure
  summary_line: Hackerone
slug: astrology-api
tags:
- Astrology
- Horoscopes
- Zodiac
- Vedic Astrology
- Western Astrology
- Kundli
- Panchang
- Numerology
- Tarot
- Palmistry
- Human Design
- Astrocartography
- PDF Reports
- MCP
- Ephemeris
use_cases:
- description: Developers build mobile and web astrology applications integrating daily horoscopes, birth charts, and compatibility analysis.
  name: Astrology App Development
- description: Content websites add personalized horoscope sections using the Astrology API's daily and monthly prediction endpoints.
  name: Horoscope Website Integration
- description: Astrology consultation platforms use the Vedic API for birth chart calculations and panchang data to support professional astrologers.
  name: Vedic Consultation Platforms
website: https://www.astrologyapi.com/
---
