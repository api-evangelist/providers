---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Shazam Agentic Access
  operation_count: 12
  slug: shazam-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- description: 'ShazamKit is Apple''s official framework for integrating Shazam music recognition into iOS, macOS, tvOS, visionOS, watchOS, and Android applications. It supports matching audio against Shazam''s global '
  name: ShazamKit
  slug: shazamkit
- description: Album metadata
  name: Shazam Albums API
  slug: shazam-albums-api
- description: Artist profiles and albums
  name: Shazam Artists API
  slug: shazam-artists-api
- description: Music charts by country, city, and genre
  name: Shazam Charts API
  slug: shazam-charts-api
- description: Audio fingerprint recognition against the Shazam catalog
  name: Shazam Recognition API
  slug: shazam-recognition-api
- description: Full-text search across Shazam's track and artist catalog
  name: Shazam Search API
  slug: shazam-search-api
- description: Track metadata, related tracks, and listening counters
  name: Shazam Tracks API
  slug: shazam-tracks-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shazam REST Albums API
  slug: open-shazam-albums-api
- collection_type: open
  name: Shazam REST Albums Artists API
  slug: open-shazam-artists-api
- collection_type: open
  name: Shazam REST Albums Charts API
  slug: open-shazam-charts-api
- collection_type: open
  name: Shazam REST Albums Recognition API
  slug: open-shazam-recognition-api
- collection_type: open
  name: Shazam REST Albums Search API
  slug: open-shazam-search-api
- collection_type: open
  name: Shazam REST Albums Tracks API
  slug: open-shazam-tracks-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/apple/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shazam-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shazam-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shazam-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shazam.com
- group: other
  title: ''
  type: Developer
  url: https://developer.apple.com/shazamkit/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shazamio
- group: auth
  title: ''
  type: Authentication
  url: https://developer.apple.com/help/account/capabilities/create-a-media-identifier-and-private-key/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apple.com/legal/internet-services/terms/site.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/legal/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shazam
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Shazam
- group: operate
  title: ''
  type: Forums
  url: https://developer.apple.com/forums/tags/shazamkit
created: '2024-01-01'
description: Shazam is Apple's music recognition service that identifies songs from audio fingerprints. The Shazam API provides song recognition, music charts, and artist and track metadata retrieval. Originally launched in 2002 and acquired by Apple in 2018, Shazam processes over 1 billion song identifications per month. Official developer access is available via Apple's ShazamKit framework for iOS, macOS, tvOS, visionOS, watchOS, and Android. A third-party REST API is also available through RapidAPI for song detection, chart data, and artist lookups.
examples:
- key_count: 6
  name: Recognize Response
  slug: recognize-response
- key_count: 2
  name: Track Search Response
  slug: track-search-response
finops:
- name: Shazam Finops
  service_category: Music Recognition
  slug: shazam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shazam.png
json_schemas:
- name: Shazam Recognize Request
  property_count: 5
  slug: shazam-recognize-request
- name: Shazam Track
  property_count: 10
  slug: shazam-track
jsonld:
- class_count: 16
  name: Shazam Context
  property_count: 9
  slug: shazam-context
layout: provider
modified: '2026-06-13'
name: Shazam
nav: Providers
network: true
overview: 'Shazam publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Albums API, Artists API, Charts API, and 3 more. Tagged areas include Music, Audio Recognition, Song Identification, Charts, and Artists.


  The Shazam catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shazam''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Shazam Plans Pricing
  plan_count: 7
  slug: shazam-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 11
  name: Shazam Rate Limits
  slug: shazam-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Shazam API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: shazam-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 39.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shazam/refs/heads/main/screenshots/shazam-2026-06-20T193748.png
security:
- kind: authentication
  name: Shazam Authentication
  slug: shazam-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Shazam Domain Security
  slug: shazam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shazam
tags:
- Music
- Audio Recognition
- Song Identification
- Charts
- Artists
- Tracks
- Fingerprinting
website: https://www.shazam.com
---
