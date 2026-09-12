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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Artsy Agentic Access
  operation_count: 53
  slug: artsy-agentic-access
  summary_line: 53 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.artsy.net/api
  baseurl_source: declared
  description: The Artsy Public API provides access to images of historic artwork and related information on artsy.net for educational and non-commercial purposes. Resources include artists, artworks, editions, fair
  name: Artsy Public API
  slug: artsy-api
- description: Metaphysics is Artsy's public GraphQL gateway — the contract that actually powers artsy.net and the Artsy iOS and Android apps. It wraps Artsy's internal services (Gravity, Exchange, Convection) behin
  name: Artsy Metaphysics GraphQL API
  slug: metaphysics
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artsy-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.artsy.net/
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
- group: docs
  title: Public API Reference
  type: APIReference
  url: https://developers.artsy.net/v2
- group: start
  title: Getting Started — obtain credentials and mint a token
  type: GettingStarted
  url: https://developers.artsy.net/v2/docs/authentication
- group: operate
  title: Artsy Help Center
  type: Support
  url: https://support.artsy.net/
- group: commercial
  title: Terms and Conditions
  type: TermsOfService
  url: https://www.artsy.net/terms
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://www.artsy.net/privacy
- group: auth
  title: Artsy Security
  type: Security
  url: https://www.artsy.net/security
- group: operate
  title: Artsy Status
  type: StatusPage
  url: https://status.artsy.net/
- group: operate
  title: Public API retirement notice
  type: Deprecation
  url: https://developers.artsy.net/
- group: auth
  title: ''
  type: Authentication
  url: authentication/artsy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/artsy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artsy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artsy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artsy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artsy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/artsy-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/artsy-packages.yml
- group: build
  title: First-party client libraries
  type: SDKs
  url: packages/artsy-packages.yml
- group: start
  title: Staging environment and playground
  type: Sandbox
  url: sandbox/artsy-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/artsy-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/artsy-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/artsy-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artsy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/artsy-mcp.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/artsy-vulnerability-disclosure.yml
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
modified: '2026-09-07'
name: Artsy
nav: Providers
network: true
overview: 'Artsy publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Art, Marketplace, Artists, Collectors, and Galleries.


  Artsy''s developer surface includes developer portal, documentation, engineering blog, signup flow, API reference, getting-started guide, support, and 28 more developer resources.'
plans:
- name: Artsy Plans Pricing
  plan_count: 0
  slug: artsy-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Artsy Rate Limits
  slug: artsy-rate-limits
scopes:
- name: Artsy Scopes
  scope_count: 1
  slug: artsy-scopes
  summary_line: 1 scope · authorizationCode/password/token-exchange
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 49.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/artsy/refs/heads/main/screenshots/artsy-2026-06-20T172452.png
security:
- kind: authentication
  name: Artsy Authentication
  slug: artsy-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Artsy Domain Security
  slug: artsy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Artsy Vulnerability Disclosure
  slug: artsy-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: artsy
tags:
- Art
- Marketplace
- Artists
- Collectors
- Galleries
- Auctions
- Museums
- Art Market
- Culture
- Images
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
