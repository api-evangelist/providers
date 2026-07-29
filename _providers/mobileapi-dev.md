---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Mobileapi Dev Agentic Access
  operation_count: 57
  slug: mobileapi-dev-agentic-access
  summary_line: 57 operations · 1 acting
api_count: 9
apis:
- description: The api API from MobileAPI.dev — 2 operation(s) for api.
  name: MobileAPI.dev api API
  slug: mobileapi-dev-api-api
- description: The api-token-auth API from MobileAPI.dev — 1 operation(s) for api-token-auth.
  name: MobileAPI.dev api-token-auth API
  slug: mobileapi-dev-api-token-auth-api
- description: The demo-x7k9m2p4 API from MobileAPI.dev — 23 operation(s) for demo-x7k9m2p4.
  name: MobileAPI.dev demo-x7k9m2p4 API
  slug: mobileapi-dev-demo-x7k9m2p4-api
- description: The devices API from MobileAPI.dev — 24 operation(s) for devices.
  name: MobileAPI.dev devices API
  slug: mobileapi-dev-devices-api
- description: The images API from MobileAPI.dev — 1 operation(s) for images.
  name: MobileAPI.dev images API
  slug: mobileapi-dev-images-api
- description: The manufacturers API from MobileAPI.dev — 2 operation(s) for manufacturers.
  name: MobileAPI.dev manufacturers API
  slug: mobileapi-dev-manufacturers-api
- description: The me API from MobileAPI.dev — 1 operation(s) for me.
  name: MobileAPI.dev me API
  slug: mobileapi-dev-me-api
- description: The payment_successful API from MobileAPI.dev — 2 operation(s) for payment_successful.
  name: MobileAPI.dev payment_successful API
  slug: mobileapi-dev-payment-successful-api
- description: The status API from MobileAPI.dev — 1 operation(s) for status.
  name: MobileAPI.dev status API
  slug: mobileapi-dev-status-api
arazzos:
- description: Confirm the account, run a natural-language device query, and load the top result's detail.
  name: MobileAPI AI Query with Account Check
  slug: mobileapi-dev-ai-query-with-account-check-workflow
- description: Resolve a device by name and gather its display, main camera, and battery specifications.
  name: MobileAPI Assemble Device Spec Sheet
  slug: mobileapi-dev-assemble-spec-sheet-workflow
- description: Turn a partial typeahead string into a confirmed device record.
  name: MobileAPI Autocomplete and Resolve Device
  slug: mobileapi-dev-autocomplete-resolve-device-workflow
- description: Look up a manufacturer in the directory, read its profile, then list its devices.
  name: MobileAPI Browse a Manufacturer Catalog
  slug: mobileapi-dev-browse-manufacturer-catalog-workflow
- description: List devices of a given type, then narrow to a launch year, branching when a slice is empty.
  name: MobileAPI Browse Devices by Type and Year
  slug: mobileapi-dev-browse-type-year-workflow
- description: Search the catalog by device name, then load the full record and gallery images for the best match.
  name: MobileAPI Search Device and Load Full Detail
  slug: mobileapi-dev-search-device-detail-workflow
artifact_total: 90
collections:
- collection_type: postman
  name: MobileAPI
  slug: postman-mobileapi
- collection_type: open
  name: MobileAPI
  slug: open-mobileapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mobileapi-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mobileapi-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobileapi-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mobileapi-dev-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mobileapidev/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-ai-query-with-account-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-assemble-spec-sheet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-autocomplete-resolve-device-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-browse-manufacturer-catalog-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-browse-type-year-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mobileapi-dev-search-device-detail-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mobileapidev
- group: start
  title: ''
  type: Portal
  url: https://mobileapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://mobileapi.dev/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://mobileapi.dev/#pricing
- group: commercial
  title: ''
  type: Plans
  url: https://mobileapi.dev/#pricing
- group: start
  title: ''
  type: Signup
  url: https://mobileapi.dev/signup/
- group: start
  title: ''
  type: Login
  url: https://mobileapi.dev/signin/
- group: company
  title: ''
  type: Blog
  url: https://mobileapi.dev/blog/
- group: operate
  title: ''
  type: Support
  url: mailto:support@mobileapi.dev
- group: operate
  title: ''
  type: Contact
  url: mailto:support@mobileapi.dev
- group: operate
  title: ''
  type: StatusPage
  url: https://mobileapi.cronitorstatus.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MobileAPI-dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MobileAPI-dev/mobileapi-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/MobileAPI-dev/mobileapi-examples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.getterms.io/view/AG2Np/terms-of-service/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.getterms.io/view/AG2Np/privacy/en-us
- group: commercial
  title: ''
  type: Plans
  url: ''
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: design
  title: ''
  type: SpectralRules
  url: rules/mobileapi-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mobileapi-dev-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mobileapi-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mobileapi-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mobileapi-dev-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://mobileapi.dev/llms.txt
created: '2026-05-06'
description: MobileAPI.dev is a commercial REST API that provides structured device specifications, product images, and metadata for over 31,500 smartphones, tablets, smartwatches, and laptops from more than 200 brands. The API exposes 12 normalized spec categories per device (Network, Body, Display, Platform, Memory, Main Camera, Selfie Camera, Sound, Comms, Features, Battery, Misc), fuzzy search, autocomplete, manufacturer indices, and a natural-language AI query endpoint, replacing in-house scraping of GSMArena-style sources for device-catalog, comparison, e-commerce, trade-in, repair, and insurance applications.
examples:
- key_count: 3
  name: Mobileapi Ai Query Example
  slug: mobileapi-ai-query-example
- key_count: 29
  name: Mobileapi Device Example
  slug: mobileapi-device-example
- key_count: 4
  name: Mobileapi Devicelist Example
  slug: mobileapi-devicelist-example
- key_count: 4
  name: Mobileapi Manufacturer Example
  slug: mobileapi-manufacturer-example
features:
- description: 31,500+ smartphones, tablets, smartwatches, and laptops across 200+ brands including Apple, Samsung, Google, OnePlus, Xiaomi, Huawei, Realme, and Infinix.
  name: Comprehensive Device Database
- description: Each device returns structured data across Network, Body, Display, Platform, Memory, Main Camera, Selfie Camera, Sound, Comms, Features, Battery, and Misc with dedicated per-category endpoints.
  name: Twelve Normalized Spec Categories
- description: Multiple official product images per device, returned as base64-encoded payloads plus 100x100 thumbnails, eliminating the need to host an image CDN.
  name: Embedded Product Images
- description: Manufacturer-aware search tolerates typos, partial names, and model number variations; a separate autocomplete endpoint powers search-as-you-type UIs.
  name: Fuzzy Search and Autocomplete
- description: A /devices/ai-query/ endpoint translates plain-English questions like 'phones with 8GB+ RAM under 200g' or 'best camera phones from 2024' into structured device results (paid plans only).
  name: AI Natural-Language Query
- description: Dedicated endpoints to list devices by manufacturer, launch year, or device type for building brand pages, new releases feeds, or category navigation.
  name: Browse-By Indices
- description: API keys can be supplied via Authorization Token, Authorization Bearer, or a key= query parameter fallback; both header formats are equivalent.
  name: Token or Bearer Authentication
- description: Every response includes X-RateLimit-Limit, X-RateLimit-Remaining, and X-RateLimit-Reset so clients can self-throttle; quota exceedance returns HTTP 429.
  name: Rate-Limit Headers
- description: A /demo-x7k9m2p4/devices/ mirror of the authenticated tree allows zero-key evaluation of every endpoint shape before signing up.
  name: Demo Endpoints (No Key Required)
- description: GET /me/ returns plan, quota, and usage metadata for the authenticated key.
  name: Account Introspection
- description: Real-time Cronitor-hosted status page with 99.9% uptime guarantee on Business and Enterprise tiers.
  name: Status Page and Uptime
finops:
- name: Mobileapi Dev Finops
  service_category: Data API - Device Specifications
  slug: mobileapi-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mobileapi-dev.png
integrations:
- description: Documented cURL recipes for /devices/search/ and other endpoints with Content-Type application/json and query-parameter API keys.
  name: cURL
- description: Documented fetch-based examples for browser and Node.js integrations.
  name: JavaScript / Fetch
- description: Documented Python requests snippets for device search and retrieval.
  name: Python / Requests
- description: Documented PHP file_get_contents plus http_build_query examples.
  name: PHP
- description: Stripe-hosted checkout flow handles plan upgrades and recurring billing (referenced in CSP allowlist and /payment_successful callback).
  name: Stripe
- description: In-app support widget powered by Help Scout for paid-plan ticketing.
  name: Help Scout Beacon
- description: Public uptime and incident history hosted on Cronitor at mobileapi.cronitorstatus.com.
  name: Cronitor Status Page
- description: Terms of Service and Privacy Policy hosted on GetTerms.io.
  name: GetTerms.io
json_schemas:
- name: Battery
  property_count: 3
  slug: mobileapi-battery
- name: Body
  property_count: 6
  slug: mobileapi-body
- name: Comms
  property_count: 7
  slug: mobileapi-comms
- name: Device
  property_count: 29
  slug: mobileapi-device
- name: DeviceList
  property_count: 16
  slug: mobileapi-devicelist
- name: Display
  property_count: 6
  slug: mobileapi-display
- name: Features
  property_count: 3
  slug: mobileapi-features
- name: Image
  property_count: 5
  slug: mobileapi-image
- name: MainCamera
  property_count: 4
  slug: mobileapi-maincamera
- name: Manufacturer
  property_count: 4
  slug: mobileapi-manufacturer
- name: Memory
  property_count: 4
  slug: mobileapi-memory
- name: Misc
  property_count: 5
  slug: mobileapi-misc
- name: Network
  property_count: 7
  slug: mobileapi-network
- name: Platform
  property_count: 5
  slug: mobileapi-platform
- name: SelfieCamera
  property_count: 4
  slug: mobileapi-selfiecamera
- name: Sound
  property_count: 3
  slug: mobileapi-sound
json_structures:
- name: Mobileapi Battery Structure
  property_count: 0
  slug: mobileapi-battery-structure
- name: Mobileapi Body Structure
  property_count: 0
  slug: mobileapi-body-structure
- name: Mobileapi Comms Structure
  property_count: 0
  slug: mobileapi-comms-structure
- name: Mobileapi Device Structure
  property_count: 0
  slug: mobileapi-device-structure
- name: Mobileapi Devicelist Structure
  property_count: 0
  slug: mobileapi-devicelist-structure
- name: Mobileapi Display Structure
  property_count: 0
  slug: mobileapi-display-structure
- name: Mobileapi Features Structure
  property_count: 0
  slug: mobileapi-features-structure
- name: Mobileapi Image Structure
  property_count: 0
  slug: mobileapi-image-structure
- name: Mobileapi Maincamera Structure
  property_count: 0
  slug: mobileapi-maincamera-structure
- name: Mobileapi Manufacturer Structure
  property_count: 0
  slug: mobileapi-manufacturer-structure
- name: Mobileapi Memory Structure
  property_count: 0
  slug: mobileapi-memory-structure
- name: Mobileapi Misc Structure
  property_count: 0
  slug: mobileapi-misc-structure
- name: Mobileapi Network Structure
  property_count: 0
  slug: mobileapi-network-structure
- name: Mobileapi Platform Structure
  property_count: 0
  slug: mobileapi-platform-structure
- name: Mobileapi Selfiecamera Structure
  property_count: 0
  slug: mobileapi-selfiecamera-structure
- name: Mobileapi Sound Structure
  property_count: 0
  slug: mobileapi-sound-structure
jsonld:
- class_count: 43
  name: Mobileapi Dev Context
  property_count: 7
  slug: mobileapi-dev-context
layout: provider
modified: '2026-05-06'
name: MobileAPI.dev
nav: Providers
network: true
overview: 'MobileAPI.dev publishes 9 APIs on the [APIs.io](https://apis.io/) network, including api API, api-token-auth API, demo-x7k9m2p4 API, and 6 more. Tagged areas include Data API, Developer Tools, Device Specifications, Mobile Data, and Phone Specs.


  The MobileAPI.dev catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MobileAPI.dev''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, support, and 26 more developer resources.'
plans:
- name: Mobileapi Dev Plans Pricing
  plan_count: 3
  slug: mobileapi-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Mobileapi Dev Rate Limits
  slug: mobileapi-dev-rate-limits
rules:
- name: MobileAPI.dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mobileapi-dev-jsonschema-spectral-rules
- name: MobileAPI.dev API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 4
  slug: mobileapi-rules
score:
  band: strong
  composite: 63.5
  delta: -4.2
  facets:
    commercial_clarity: 84.2
    contract_quality: 67.4
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobileapi-dev/refs/heads/main/screenshots/mobileapi-dev-2026-06-20T185631.png
security:
- kind: authentication
  name: Mobileapi Dev Authentication
  slug: mobileapi-dev-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mobileapi Dev Domain Security
  slug: mobileapi-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mobileapi Dev Vulnerability Disclosure
  slug: mobileapi-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mobileapi-dev
tags:
- Data API
- Developer Tools
- Device Specifications
- Mobile Data
- Phone Specs
- REST API
- SaaS
use_cases:
- description: Power product catalog and side-by-side spec comparison pages with up-to-date specs and images for current and historical devices.
  name: Device Catalog and Comparison Sites
- description: Identify a device by name, model number, or autocomplete suggestion and pull structured specs for valuation and resale workflows.
  name: Trade-In and Buyback Platforms
- description: Look up displays, batteries, cameras, and connectivity details to drive parts selection and pricing in repair-shop applications.
  name: Repair and Service Workflows
- description: Resolve user-supplied device names to canonical models and risk-tier specs for handset insurance and warranty premium calculations.
  name: Insurance and Warranty Quoting
- description: Auto-fill product detail pages with normalized specs and base64 images for marketplace listings, retail sites, and affiliate stores.
  name: E-commerce Product Pages
- description: Use the AI natural-language query endpoint to power conversational device recommendations grounded in real specifications.
  name: AI Assistants and Recommender Bots
- description: Match the network bands (2G/3G/4G/5G) of a customer's device against carrier coverage to drive bring-your-own-device flows.
  name: Carrier and MVNO Compatibility Tools
- description: Embed structured spec sheets in reviews and news posts without scraping or maintaining an in-house spec database.
  name: Reviews and Tech Editorial Sites
website: https://mobileapi.dev/
---
