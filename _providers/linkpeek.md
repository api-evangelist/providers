---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: GET-based HTTP image API that returns a screenshot for any given web page URI. Embeddable directly in HTML via img/anchor tags. Supports request options such as size=original and viewport for mobile/t
  name: LinkPeek Screenshot API
  slug: linkpeek-screenshot-api
- description: REST-style HTTP GET endpoint that accepts a target web page URI and returns a screenshot image. Supports size (e.g., size=original) and viewport (mobile/tablet) options. Designed for direct HTML embed
  name: LinkPeek Website Screenshot API
  slug: linkpeek-website-screenshot-api
- description: REST-style HTTP GET image API. A call to /api/v1 with query parameters (uri, size, viewport) returns a screenshot image directly. Authenticated with an apikey plus an MD5 request-signature token; requ
  name: Website Screenshot API
  slug: website-screenshot-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://linkpeek.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://linkpeek.com/
- group: docs
  title: ''
  type: Documentation
  url: https://linkpeek.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://linkpeek.com/docs/request-options
- group: commercial
  title: ''
  type: Plans
  url: https://linkpeek.com/how-much-does-linkpeek-cost
- group: operate
  title: ''
  type: Support
  url: https://linkpeek.com/contact
- group: company
  title: ''
  type: Blog
  url: https://linkpeek.com/blog
- group: start
  title: ''
  type: Login
  url: https://linkpeek.com/login
created: '2026-08-09'
description: Real-time website screenshot service that captures, stores, serves, and refreshes webpage snapshots via a simple GET-based image API. Give it a target URI and it returns a screenshot image.
layout: provider
modified: '2026-08-26'
name: LinkPeek
nav: Providers
network: true
overview: 'LinkPeek publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Screenshots, webpage-capture, website-thumbnails, Image-Generation, and Rendering.


  LinkPeek''s developer surface includes documentation, API reference, support, engineering blog, and 4 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 2
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 12.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkpeek/refs/heads/main/screenshots/linkpeek-2026-09-02T150301.png
slug: linkpeek
tags:
- Screenshots
- webpage-capture
- website-thumbnails
- Image-Generation
- Rendering
- web-scraping-adjacent
- Developer Tools
- Software-as-a-Service
- rest-image-api
- Utility API
- URL Metadata
- Link Preview
- OpenGraph
- QR Code Generation
- DNS
- WHOIS
- SSL
- Web Security Scanning
- IP Geolocation
- Data Conversion
- LLM-Compatible API
- API Utilities
- dns-whois
- openai-compatible-llm
website: https://linkpeek.com/
---
