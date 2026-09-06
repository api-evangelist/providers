---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: What3Words Agentic Access
  operation_count: 5
  slug: what3words-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: REST API for converting between three-word addresses and latitude / longitude coordinates, with AutoSuggest, available-languages, and grid-section endpoints. JSON or GeoJSON response formats. Authenti
  name: what3words Public API
  slug: public-api
- description: Converts a latitude / longitude coordinate into a three-word address in a chosen language.
  name: what3words convert-to-3wa Endpoint
  slug: convert-to-3wa
- description: Converts a three-word address into a latitude / longitude coordinate and a bounding square.
  name: what3words convert-to-coordinates Endpoint
  slug: convert-to-coordinates
- description: Validates and autocorrects partial or imperfect three-word input, returning ranked suggestions. Supports focus, clipping by polygon, country, bounding box or circle, and voice-input modes.
  name: what3words AutoSuggest Endpoint
  slug: autosuggest
- description: Returns all supported what3words languages and locale variants.
  name: what3words available-languages Endpoint
  slug: available-languages
- description: Returns the what3words three-metre grid for a specified bounding box as JSON or GeoJSON, suitable for map overlays.
  name: what3words grid-section Endpoint
  slug: grid-section
- description: Official JavaScript wrapper around the what3words Public API for browser and Node.js applications.
  name: what3words JavaScript SDK
  slug: javascript-sdk
- description: Official Python wrapper around the what3words Public API.
  name: what3words Python SDK
  slug: python-sdk
- description: Official Java wrapper around the what3words Public API for server-side JVM applications.
  name: what3words Java SDK
  slug: java-sdk
- description: Official PHP wrapper around the what3words Public API.
  name: what3words PHP SDK
  slug: php-sdk
- description: Official Swift wrapper around the what3words Public API for iOS, iPadOS, and macOS applications.
  name: what3words Swift SDK
  slug: swift-sdk
- description: Official Android wrapper around the what3words Public API for native Android applications.
  name: what3words Android SDK
  slug: android-sdk
- description: UI components for embedding what3words grids, markers, and AutoSuggest experiences in Apple Maps-based iOS and iPadOS applications.
  name: what3words Swift Map Components
  slug: swift-components-map
- description: UI component that uses the device camera to scan three-word addresses from signage, packaging, or printed materials.
  name: what3words OCR Camera Component
  slug: ocr-component
- description: Public repository hosting the OpenAPI specification, LLM files, and reference material for the what3words Public API.
  name: what3words API Docs and OpenAPI Repository
  slug: api-docs-repo
- baseURL: https://api.what3words.com/v3
  baseurl_source: declared
  description: The Autosuggest API from what3words — 1 operation(s) for autosuggest.
  name: what3words Autosuggest API
  slug: what3words-autosuggest-api
- baseURL: https://api.what3words.com/v3
  baseurl_source: declared
  description: The Available Languages API from what3words — 1 operation(s) for available languages.
  name: what3words Available Languages API
  slug: what3words-available-languages-api
- baseURL: https://api.what3words.com/v3
  baseurl_source: declared
  description: The Convert To 3wa API from what3words — 1 operation(s) for convert to 3wa.
  name: what3words Convert To 3wa API
  slug: what3words-convert-to-3wa-api
- baseURL: https://api.what3words.com/v3
  baseurl_source: declared
  description: The Convert To Coordinates API from what3words — 1 operation(s) for convert to coordinates.
  name: what3words Convert To Coordinates API
  slug: what3words-convert-to-coordinates-api
- baseURL: https://api.what3words.com/v3
  baseurl_source: declared
  description: The Grid Section API from what3words — 1 operation(s) for grid section.
  name: what3words Grid Section API
  slug: what3words-grid-section-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: what3words Public Autosuggest API
  slug: open-what3words-autosuggest-api
- collection_type: open
  name: what3words Public Autosuggest Available Languages API
  slug: open-what3words-available-languages-api
- collection_type: open
  name: what3words Public Autosuggest Convert To 3wa API
  slug: open-what3words-convert-to-3wa-api
- collection_type: open
  name: what3words Public Autosuggest Convert To Coordinates API
  slug: open-what3words-convert-to-coordinates-api
- collection_type: open
  name: what3words Public Autosuggest Grid Section API
  slug: open-what3words-grid-section-api
- collection_type: open
  name: what3words Public API
  slug: open-what3words
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/what3words/what3words-api-docs/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/what3words-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/what3words-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/what3words-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/what3words
- group: company
  title: ''
  type: Website
  url: https://what3words.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.what3words.com/public-api/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/what3words
- group: commercial
  title: ''
  type: Plans
  url: plans/what3words-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/what3words-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/what3words-finops.yml
created: '2026-05-23'
description: what3words has divided the world into a grid of three-metre squares and given each one a unique three-word address (e.g. ///filled.count.soap). The what3words Public API converts between three-word addresses and latitude / longitude coordinates, offers an AutoSuggest with autocorrect for voice/typing input, exposes supported languages and locale variants, and returns grid sections as GeoJSON. The API is HTTPS GET only, authenticated by API key in a query parameter or X-Api-Key header, and is wrapped by official SDKs for Swift, Android, Java, JavaScript, Python, PHP, and .NET, plus UI components for map and OCR experiences.
finops:
- name: What3Words Finops
  service_category: API
  slug: what3words-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/what3words.png
layout: provider
modified: '2026-05-23'
name: what3words
nav: Providers
network: true
overview: 'what3words publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Autosuggest API, Available Languages API, Convert To 3wa API, and 2 more. Tagged areas include Geocoding, Addressing, Location, Three Word Address, and Maps.


  what3words'' developer surface includes authentication, documentation, GitHub presence, and 8 more developer resources.'
plans:
- name: What3Words Plans Pricing
  plan_count: 1
  slug: what3words-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: What3Words Rate Limits
  slug: what3words-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/what3words/refs/heads/main/screenshots/what3words-2026-06-20T201420.png
security:
- kind: authentication
  name: What3Words Authentication
  slug: what3words-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: What3Words Domain Security
  slug: what3words-domain-security
  summary_line: TLSv1.3 · DMARC
slug: what3words
tags:
- Geocoding
- Addressing
- Location
- Three Word Address
- Maps
website: https://what3words.com/
---
