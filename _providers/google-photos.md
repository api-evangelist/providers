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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Photos Agentic Access
  operation_count: 8
  slug: google-photos-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 4
apis:
- description: The Albums API from Google Photos Library — 2 operation(s) for albums.
  name: Google Photos Library Albums API
  slug: google-photos-albums-api
- description: The MediaItems API from Google Photos Library — 2 operation(s) for mediaitems.
  name: Google Photos Library MediaItems API
  slug: google-photos-mediaitems-api
- description: The MediaItems:search API from Google Photos Library — 1 operation(s) for mediaitems:search.
  name: Google Photos Library MediaItems:search API
  slug: google-photos-mediaitems-search-api
- description: The SharedAlbums API from Google Photos Library — 1 operation(s) for sharedalbums.
  name: Google Photos Library SharedAlbums API
  slug: google-photos-sharedalbums-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Photos Library Albums API
  slug: open-google-photos-albums-api
- collection_type: open
  name: Google Photos Library Albums MediaItems API
  slug: open-google-photos-mediaitems-api
- collection_type: open
  name: Google Photos Library Albums MediaItems:search API
  slug: open-google-photos-mediaitems-search-api
- collection_type: open
  name: Google Photos Library Albums SharedAlbums API
  slug: open-google-photos-sharedalbums-api
- collection_type: open
  name: Google Photos Library API
  slug: open-photos
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-photos-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-photos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-photos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-photos-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-photos-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googlesamples
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-photos
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/photos/library/guides/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/photos/library/guides/api-client-libraries
- group: design
  title: ''
  type: JSONLD
  url: json-ld/photos.jsonld
created: '2026-03-13'
description: The Google Photos Library API allows you to manage photos, videos, and albums in Google Photos. You can create and manage albums, upload and retrieve media items, search through your photo library, and share albums with other users. The API uses OAuth 2.0 for authentication and requires a Google account.
finops:
- name: Google Photos Finops
  service_category: API
  slug: google-photos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-photos.png
json_schemas:
- name: Google Photos Media Item
  property_count: 7
  slug: photos
jsonld:
- class_count: 13
  name: Photos Context
  property_count: 3
  slug: photos
layout: provider
modified: '2026-05-19'
name: Google Photos Library
nav: Providers
network: true
overview: 'Google Photos Library publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Albums API, MediaItems API, MediaItems:search API, and 1 more. Tagged areas include Albums, Google, Image, Media, and Photos.


  The Google Photos Library catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Photos Library''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Photos Plans Pricing
  plan_count: 3
  slug: google-photos-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Photos Rate Limits
  slug: google-photos-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Photos Library API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-photos-jsonschema-spectral-rules
scopes:
- name: Google Photos Scopes
  scope_count: 3
  slug: google-photos-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-photos/refs/heads/main/screenshots/google-photos-2026-06-20T182223.png
security:
- kind: authentication
  name: Google Photos Authentication
  slug: google-photos-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Photos Domain Security
  slug: google-photos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Photos Vulnerability Disclosure
  slug: google-photos-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-photos
tags:
- Albums
- Google
- Image
- Media
- Photos
- Sharing
- Storage
---
