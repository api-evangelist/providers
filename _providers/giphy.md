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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Giphy Agentic Access
  operation_count: 23
  slug: giphy-agentic-access
  summary_line: 23 operations · 2 acting
api_count: 11
apis:
- description: Pingback and action register endpoints for measuring user engagement.
  name: Giphy Analytics API
  slug: giphy-analytics-api
- description: Programmatic creation of animated text/word GIFs.
  name: Giphy Animate API
  slug: giphy-animate-api
- description: Top-level categories and subcategories used to organize GIFs.
  name: Giphy Categories API
  slug: giphy-categories-api
- description: Channel discovery and metadata.
  name: Giphy Channels API
  slug: giphy-channels-api
- description: GIFs with sound. Access is gated; contact clips@giphy.com.
  name: Giphy Clips API
  slug: giphy-clips-api
- description: GIPHY's animated emoji library and per-emoji variations.
  name: Giphy Emoji API
  slug: giphy-emoji-api
- description: Search, trending, translate, random, and lookup endpoints for animated GIFs.
  name: Giphy GIFs API
  slug: giphy-gifs-api
- description: Tag autocompletion, related search terms, and trending search queries.
  name: Giphy Search Discovery API
  slug: giphy-search-discovery-api
- description: The same surface as GIFs but scoped to transparent-background stickers.
  name: Giphy Stickers API
  slug: giphy-stickers-api
- description: Programmatic upload of GIFs and video assets.
  name: Giphy Upload API
  slug: giphy-upload-api
- description: Identifier generation and other helpers.
  name: Giphy Utilities API
  slug: giphy-utilities-api
artifact_total: 84
collections:
- collection_type: postman
  name: GIPHY Analytics API
  slug: postman-giphy-analytics-api
- collection_type: postman
  name: GIPHY Analytics Animate API
  slug: postman-giphy-animate-api
- collection_type: postman
  name: GIPHY Analytics Categories API
  slug: postman-giphy-categories-api
- collection_type: postman
  name: GIPHY Analytics Channels API
  slug: postman-giphy-channels-api
- collection_type: postman
  name: GIPHY Analytics Clips API
  slug: postman-giphy-clips-api
- collection_type: postman
  name: GIPHY Analytics Emoji API
  slug: postman-giphy-emoji-api
- collection_type: postman
  name: GIPHY Analytics GIFs API
  slug: postman-giphy-gifs-api
- collection_type: postman
  name: GIPHY Analytics Search Discovery API
  slug: postman-giphy-search-discovery-api
- collection_type: postman
  name: GIPHY Analytics Stickers API
  slug: postman-giphy-stickers-api
- collection_type: postman
  name: GIPHY Analytics Upload API
  slug: postman-giphy-upload-api
- collection_type: postman
  name: GIPHY Analytics Utilities API
  slug: postman-giphy-utilities-api
- collection_type: open
  name: GIPHY API
  slug: open-giphy
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/giphy/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/giphy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/giphy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/giphy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/giphy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/giphy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://giphy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.giphy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.giphy.com/docs/
- group: start
  title: ''
  type: Console
  url: https://developers.giphy.com/dashboard/
- group: start
  title: ''
  type: Signup
  url: https://giphy.com/join
- group: start
  title: ''
  type: Login
  url: https://giphy.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.giphy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.giphy.com/hc/en-us/articles/360032872931-GIPHY-Privacy-Policy
- group: other
  title: ''
  type: Branding
  url: https://support.giphy.com/hc/en-us/articles/360020027252-GIPHY-Brand-Guidelines
- group: operate
  title: ''
  type: Support
  url: https://support.giphy.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Giphy
- group: build
  title: Historical API Reference (archived)
  type: GitHubRepository
  url: https://github.com/Giphy/GiphyAPI
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@giphy
- group: other
  title: ''
  type: X
  url: https://x.com/giphy
- group: build
  title: GIPHY Bandwidth Saver (reference implementation)
  type: Tools
  url: https://github.com/Giphy/giphy-bandwidth-saver
- group: build
  title: Cloudflare CDN Config Reference
  type: Tools
  url: https://github.com/Giphy/cloudflare-cdn-config-ref-implementation
- group: build
  title: Fastly Compute Reference
  type: Tools
  url: https://github.com/Giphy/fastly-compute-ref-implementation
- group: design
  title: ''
  type: SpectralRules
  url: rules/giphy-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/giphy-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/giphy-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/giphy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/giphy-rate-limits.yml
- group: other
  title: FinOps Cost Tracking Profile
  type: Resources
  url: finops/giphy-finops.yml
created: '2026-05-28'
description: GIPHY is the world's largest library of GIFs, stickers, animated emoji, and Clips (GIFs with sound), with a developer API used by messaging apps, social platforms, productivity tools, ads, and creator products. GIPHY is owned by Meta. Authentication is via API key (Beta or Production tier) and all surfaces share the same envelope (data + meta + pagination) with rich, multi-rendition media payloads.
examples:
- key_count: 2
  name: Giphy Autocomplete Search Tags Example
  slug: giphy-autocomplete-search-tags-example
- key_count: 2
  name: Giphy Get Gif By Id Example
  slug: giphy-get-gif-by-id-example
- key_count: 2
  name: Giphy Get Random Gif Example
  slug: giphy-get-random-gif-example
- key_count: 2
  name: Giphy Get Related Search Terms Example
  slug: giphy-get-related-search-terms-example
- key_count: 2
  name: Giphy Get Trending Gifs Example
  slug: giphy-get-trending-gifs-example
- key_count: 2
  name: Giphy Get Trending Searches Example
  slug: giphy-get-trending-searches-example
- key_count: 2
  name: Giphy List Emoji Example
  slug: giphy-list-emoji-example
- key_count: 2
  name: Giphy List Gif Categories Example
  slug: giphy-list-gif-categories-example
- key_count: 2
  name: Giphy Register Search Action Example
  slug: giphy-register-search-action-example
- key_count: 2
  name: Giphy Search Clips Example
  slug: giphy-search-clips-example
- key_count: 2
  name: Giphy Search Gifs Example
  slug: giphy-search-gifs-example
- key_count: 2
  name: Giphy Search Stickers Example
  slug: giphy-search-stickers-example
- key_count: 2
  name: Giphy Translate Gif Example
  slug: giphy-translate-gif-example
- key_count: 2
  name: Giphy Upload Gif Example
  slug: giphy-upload-gif-example
features:
- description: Query millions of GIFs/stickers/emoji or fetch curated trending content.
  name: Search & Trending
- description: Convert any phrase to a single contextually relevant GIF or sticker.
  name: Translate
- description: Surface a random GIF or sticker, optionally tag-filtered.
  name: Random
- description: Programmatically generate animated text GIFs.
  name: Animate
- description: Short-form videos with sound, gated behind approval.
  name: Clips
- description: Every result includes 20+ pre-encoded renditions (GIF, MP4, WebP) for any surface.
  name: Multi-Rendition Assets
- description: Per-result onload/onclick/onsent URLs power view/click/share telemetry.
  name: Analytics Pingbacks
- description: Upload GIFs or videos to GIPHY (up to 100 MB) via upload.giphy.com.
  name: Programmatic Upload
- description: Native iOS, Android, React Native, Flutter, and Web SDKs ship UI-ready pickers.
  name: First-Party SDKs
finops:
- name: Giphy Finops
  service_category: ''
  slug: giphy-finops
image: https://giphy.com/static/img/giphy-be-animated-logo.gif
integrations:
- description: GIPHY is the GIF search backbone across Meta surfaces.
  name: Meta (Facebook, Instagram, Messenger, WhatsApp)
- description: GIPHY powers in-chat GIF reactions across major chat platforms.
  name: Slack, Discord, Microsoft Teams
- description: Native and third-party stickers via the SDKs.
  name: iMessage / Telegram / Signal
- description: GIF picker integration.
  name: Twitter / X
- description: Stickers and clips in creative-tool integrations.
  name: Adobe Express / Canva / Mobile Editors
json_schemas:
- name: GIPHY Analytics Pingbacks
  property_count: 3
  slug: giphy-analytics
- name: GIPHY Category
  property_count: 4
  slug: giphy-category
- name: GIPHY Channel
  property_count: 14
  slug: giphy-channel
- name: GIPHY Clip
  property_count: 0
  slug: giphy-clip
- name: GIPHY GIF
  property_count: 24
  slug: giphy-gif
- name: GIPHY Images
  property_count: 0
  slug: giphy-images
- name: GIPHY Meta
  property_count: 3
  slug: giphy-meta
- name: GIPHY Pagination
  property_count: 3
  slug: giphy-pagination
- name: GIPHY User
  property_count: 10
  slug: giphy-user
json_structures:
- name: Giphy Channel Structure
  property_count: 13
  slug: giphy-channel-structure
- name: Giphy Clip Structure
  property_count: 1
  slug: giphy-clip-structure
- name: Giphy Gif Structure
  property_count: 22
  slug: giphy-gif-structure
- name: Giphy Images Structure
  property_count: 0
  slug: giphy-images-structure
jsonld:
- class_count: 17
  name: Giphy Context
  property_count: 20
  slug: giphy-context
layout: provider
modified: '2026-05-30'
name: Giphy
nav: Providers
network: true
overview: 'Giphy publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Animate API, Categories API, and 8 more. Tagged areas include Photography, Media, GIFs, Stickers, and Emoji.


  The Giphy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Giphy''s developer surface includes authentication, documentation, developer console, signup flow, support, engineering blog, tooling, and 22 more developer resources.'
plans:
- name: Giphy Plans Pricing
  plan_count: 3
  slug: giphy-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 0
  name: Giphy Rate Limits
  slug: giphy-rate-limits
rules:
- name: Giphy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: giphy-jsonschema-spectral-rules
- name: Giphy API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: giphy-rules
score:
  band: strong
  composite: 59.5
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 76.5
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/giphy/refs/heads/main/screenshots/giphy-2026-06-20T181827.png
security:
- kind: authentication
  name: Giphy Authentication
  slug: giphy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Giphy Domain Security
  slug: giphy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Giphy Vulnerability Disclosure
  slug: giphy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Giphy Trust Center
  slug: giphy-trust-center
  summary_line: HIPAA, GDPR
slug: giphy
solutions:
- description: Free, rate-limited API access for development.
  name: Beta Key
- description: Reviewed access with higher throughput, custom pricing.
  name: Production Key
- description: Gated access to GIFs-with-sound endpoints.
  name: Clips Access
tags:
- Photography
- Media
- GIFs
- Stickers
- Emoji
- Video
- Messaging
- Social
- Meta
use_cases:
- description: Drop-in GIF/sticker picker for chat apps using the GIPHY SDKs.
  name: Messaging GIF Picker
- description: Animated stickers and emoji for stories and posts.
  name: Story / Post Stickers
- description: Trending and search-driven discovery for GIF-led products.
  name: Content Discovery
- description: Branded stickers and channels for marketing campaigns.
  name: Brand & Ad Creative
- description: Clips and stickers embedded in mobile video editors.
  name: Video Editor Integrations
- description: Reactions, lightweight expressions in productivity software.
  name: Productivity / Reactions
website: https://giphy.com/
---
