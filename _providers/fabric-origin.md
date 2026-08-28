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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fabric Origin Agentic Access
  operation_count: 23
  slug: fabric-origin-agentic-access
  summary_line: 23 operations · 5 acting
api_count: 8
apis:
- description: The Entertainment API ingests and serves metadata for movies, television shows, and games, including identifiers used to retrieve associated videos and images from sibling APIs. Responses are availabl
  name: Fabric Origin Entertainment API
  slug: entertainment-api
- description: The Celebrity API serves metadata about celebrities, including actors, directors, and other entertainment industry figures, with cross references to titles served by the Entertainment API.
  name: Fabric Origin Celebrity API
  slug: celebrity-api
- description: The Video API generates playable links for trailers and other video assets using video identifiers returned from the Entertainment API, allowing customers to embed Fabric Origin video content into the
  name: Fabric Origin Video API
  slug: video-api
- description: The Image API provides access to images hosted on Fabric Origin's servers, including posters, stills, and promotional artwork referenced from the Entertainment and Celebrity APIs. Customers are encour
  name: Fabric Origin Image API
  slug: image-api
- description: The Common Data API exposes reference data used across the Fabric Origin product family, including country codes, image type lookups, and video type lookups required when working with the Entertainmen
  name: Fabric Origin Common Data API
  slug: common-data-api
- description: The Entertainment API from Fabric Origin — 14 operation(s) for entertainment.
  name: Fabric Origin Entertainment API
  slug: fabric-origin-entertainment-api
- description: The Images API from Fabric Origin — 4 operation(s) for images.
  name: Fabric Origin Images API
  slug: fabric-origin-images-api
- description: The Videos API from Fabric Origin — 2 operation(s) for videos.
  name: Fabric Origin Videos API
  slug: fabric-origin-videos-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fabric Origin Data APIs Entertainment API
  slug: open-fabric-origin-entertainment-api
- collection_type: open
  name: Fabric Origin Data APIs Entertainment Images API
  slug: open-fabric-origin-images-api
- collection_type: open
  name: Fabric Origin Data APIs Entertainment Videos API
  slug: open-fabric-origin-videos-api
- collection_type: open
  name: Fabric Origin Entertainment Data APIs
  slug: open-fabric-origin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fabric-origin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fabric-origin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fabric-origin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fabricdata.com/
- group: other
  title: ''
  type: Knowledge Base
  url: https://knowledgebase.fabricdata.com/origin
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.origin.fabricdata.com/portal/login
- group: docs
  title: ''
  type: Documentation
  url: https://knowledgebase.fabricdata.com/origin/apis-all/
created: '2025-03-01'
description: Fabric Origin (formerly IVA) is the entertainment data platform powering content discovery experiences for movies, television, games, and trailers. Fabric Origin offers comprehensive entertainment data solutions including metadata, images, trailers, TV listings, and celebrity information through a family of REST APIs. With 30 percent more coverage than other providers and tailored products for every stage of the release cycle, Fabric Origin is an affordable, scalable solution trusted by startups and Fortune 50 companies alike.
finops:
- name: Fabric Origin Finops
  service_category: API
  slug: fabric-origin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fabric-origin.png
layout: provider
modified: '2026-04-28'
name: Fabric Origin
nav: Providers
network: true
overview: 'Fabric Origin publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entertainment API, Images API, and Videos API. Tagged areas include Entertainment, Movies, Television, Games, and Trailers.


  Fabric Origin''s developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Fabric Origin Plans Pricing
  plan_count: 3
  slug: fabric-origin-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Fabric Origin Rate Limits
  slug: fabric-origin-rate-limits
score:
  band: thin
  composite: 29.6
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.2
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fabric-origin/refs/heads/main/screenshots/fabric-origin-2026-06-20T181001.png
security:
- kind: authentication
  name: Fabric Origin Authentication
  slug: fabric-origin-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Fabric Origin Domain Security
  slug: fabric-origin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fabric-origin
tags:
- Entertainment
- Movies
- Television
- Games
- Trailers
- Metadata
website: https://www.fabricdata.com/
---
