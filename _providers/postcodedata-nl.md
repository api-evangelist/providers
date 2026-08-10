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
api_count: 1
apis:
- description: Provide geolocation data based on postcode for Dutch addresses
  name: PostcodeData.nl
  slug: postcodedatanl
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postcodedata-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provide geolocation data based on postcode for Dutch addresses
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postcodedata-nl.png
layout: provider
modified: '2026-05-28'
name: PostcodeData.nl
nav: Providers
network: true
overview: PostcodeData.nl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geocoding and Public APIs.
random_paper: 30
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postcodedata-nl/refs/heads/main/screenshots/postcodedata-nl-2026-06-20T191951.png
security:
- kind: domain-security
  name: Postcodedata Nl Domain Security
  slug: postcodedata-nl-domain-security
  summary_line: DNSSEC
slug: postcodedata-nl
tags:
- Geocoding
- Public APIs
website: http://api.postcodedata.nl/v1/postcode/?postcode=1211EP&streetnumber=60&ref=domeinnaam.nl&type=json
---
