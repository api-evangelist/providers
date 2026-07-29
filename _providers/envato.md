---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Envato Agentic Access
  operation_count: 11
  slug: envato-agentic-access
  summary_line: 11 operations
api_count: 8
apis:
- description: REST API for ThemeForest, CodeCanyon, AudioJungle, VideoHive, GraphicRiver, 3DOcean, and PhotoDune. Endpoints cover catalog (search, popular, new files), item detail, item downloads (for buyers), user
  name: Envato Market API
  slug: market
- description: Affiliate-only API for Envato Elements (subscription-based stock media). Provides search and metadata for catalog discovery within affiliate properties; not a general-purpose download API.
  name: Envato Elements Affiliate API
  slug: elements-affiliate
- description: The Author API from Envato — 2 operation(s) for author.
  name: Envato Author API
  slug: envato-author-api
- description: The Catalog API from Envato — 2 operation(s) for catalog.
  name: Envato Catalog API
  slug: envato-catalog-api
- description: The Downloads API from Envato — 1 operation(s) for downloads.
  name: Envato Downloads API
  slug: envato-downloads-api
- description: The Items API from Envato — 1 operation(s) for items.
  name: Envato Items API
  slug: envato-items-api
- description: The Search API from Envato — 1 operation(s) for search.
  name: Envato Search API
  slug: envato-search-api
- description: The User API from Envato — 4 operation(s) for user.
  name: Envato User API
  slug: envato-user-api
artifact_total: 17
collections:
- collection_type: open
  name: Envato Market API
  slug: open-envato
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/envato-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/envato-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envato-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/envato-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/envato-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/envato
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envato
- group: company
  title: ''
  type: Website
  url: https://envato.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://build.envato.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/envato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/envato-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/envato-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://envato.com/blog/rss.xml
created: '2026-05-08'
description: Envato runs Envato Market (per-asset marketplaces like ThemeForest, CodeCanyon, AudioJungle, VideoHive, GraphicRiver, 3DOcean, PhotoDune) and Envato Elements (subscription-based unlimited stock media). The Envato API exposes Market endpoints for items, search, downloads, user accounts, and earnings; Elements has a separate affiliate API.
finops:
- name: Envato Finops
  service_category: Stock Media / Digital Marketplace
  slug: envato-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envato.png
layout: provider
modified: '2026-05-08'
name: Envato
nav: Providers
network: true
overview: 'Envato publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Author API, Catalog API, Downloads API, and 3 more. Tagged areas include Stock Media, Marketplace, Themes, Audio, and Video.


  Envato''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Envato Plans Pricing
  plan_count: 2
  slug: envato-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Envato Rate Limits
  slug: envato-rate-limits
scopes:
- name: Envato Scopes
  scope_count: 1
  slug: envato-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.3
  delta: -2.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envato/refs/heads/main/screenshots/envato-2026-06-20T180736.png
security:
- kind: authentication
  name: Envato Authentication
  slug: envato-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Envato Domain Security
  slug: envato-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Envato Vulnerability Disclosure
  slug: envato-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: envato
tags:
- Stock Media
- Marketplace
- Themes
- Audio
- Video
- Graphics
- Subscription
website: https://envato.com/
---
