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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Artsy Public API provides access to images of historic artwork and related information on artsy.net for educational and non-commercial purposes. Resources include artists, artworks, editions, fair
  name: Artsy Public API
  slug: artsy-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artsy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/artsyinc
- group: start
  title: Artsy Website
  type: Portal
  url: https://www.artsy.net/
- group: docs
  title: Developer Documentation
  type: Documentation
  url: https://developers.artsy.net/
- group: company
  title: Engineering Blog
  type: Blog
  url: https://artsy.github.io/
- group: build
  title: Artsy GitHub Organization
  type: GitHubOrganization
  url: https://github.com/artsy
- group: start
  title: Sign Up
  type: Signup
  url: https://www.artsy.net/signup
- group: start
  title: Login
  type: Login
  url: https://www.artsy.net/login
created: '2025-02-24'
description: Artsy is the world's largest online art marketplace, connecting collectors with artists and galleries worldwide. The platform features over 1 million artworks from 100,000+ artists and provides access to galleries, art fairs, and auction houses globally. Artsy offers a Public API providing access to images of historic artwork and related information for educational and non-commercial purposes, with access limited to public domain works. The API provides resources for artists, artworks, galleries, shows, sales, and gene (classification) data. Note that the public API may be retired; partner integrations are handled through a separate partner API program.
features:
- description: Comprehensive database of artist biographies, artwork metadata, images, dimensions, medium, and provenance for over 1 million artworks.
  name: Artist and Artwork Data
- description: Access to gallery profiles, exhibition shows, art fairs, and partner information from Artsy's global gallery network.
  name: Gallery and Show Data
- description: Artsy's proprietary gene taxonomy for classifying artworks by style, period, subject matter, and medium, enabling sophisticated art discovery and recommendation.
  name: Art Classification Genes
- description: Sale, bidder, and bid information for auction and buy-now listings on the Artsy platform.
  name: Auction and Sales Data
- description: Search across artists, artworks, galleries, and other art world entities with faceted filtering and relevance ranking.
  name: Full-Text Search
finops:
- name: Artsy Finops
  service_category: API
  slug: artsy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/artsy.png
integrations:
- description: Gallery and auction house partners integrate directly with Artsy through the Partner API for full marketplace integration including artwork listings and collector communications.
  name: Artsy Partner Program
layout: provider
modified: '2026-04-19'
name: Artsy
nav: Providers
network: true
overview: 'Artsy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Art, Marketplace, Artists, Collectors, and Galleries.


  Artsy''s developer surface includes developer portal, documentation, engineering blog, signup flow, and 4 more developer resources.'
plans:
- name: Artsy Plans Pricing
  plan_count: 3
  slug: artsy-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Artsy Rate Limits
  slug: artsy-rate-limits
score:
  band: emerging
  composite: 21.7
  delta: 4.7
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artsy/refs/heads/main/screenshots/artsy-2026-06-20T172452.png
security:
- kind: domain-security
  name: Artsy Domain Security
  slug: artsy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: artsy
tags:
- Art
- Marketplace
- Artists
- Collectors
- Galleries
use_cases:
- description: Educational platforms use the Artsy API to access public domain artwork images and artist information for art history curriculum and museum education tools.
  name: Art Education Applications
- description: Partner galleries integrate with the Artsy Partner API to manage artwork listings, track collector inquiries, and access sales analytics.
  name: Gallery Integration
- description: Developers build art recommendation and discovery applications using Artsy's gene taxonomy and artist relationship data.
  name: Art Discovery Tools
- description: Art market researchers access Artsy data to analyze trends, auction results, and artist career trajectories.
  name: Research and Analysis
website: https://www.artsy.net/
---
