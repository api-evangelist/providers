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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Ghost Agentic Access
  operation_count: 56
  slug: ghost-agentic-access
  summary_line: 56 operations · 24 acting
api_count: 16
apis:
- description: The Ghost Admin API provides full read/write access to posts, pages, tags, tiers, newsletters, offers, members, users, images, themes, webhooks, and site configuration. Authentication uses short-lived
  name: Ghost Admin API
  slug: ghost-admin-api
- description: The Ghost Content API is a read-only RESTful API for delivering published content (posts, pages, tags, authors, tiers, settings) to clients. It uses query-parameter Content API keys, is fully cacheabl
  name: Ghost Content API
  slug: ghost-content-api
- description: Authors represent the staff users who create content in a Ghost publication.
  name: Ghost Authors API
  slug: ghost-authors-api
- description: Upload images to the Ghost publication for use in posts, pages, and settings.
  name: Ghost Images API
  slug: ghost-images-api
- description: Manage publication members including creating, reading, updating, and deleting member records. Members are people who have signed up for the publication.
  name: Ghost Members API
  slug: ghost-members-api
- description: Manage email newsletters that members can subscribe to. Each newsletter has its own design, sender details, and subscription list.
  name: Ghost Newsletters API
  slug: ghost-newsletters-api
- description: Manage promotional offers for paid membership tiers, including discounts and trial periods.
  name: Ghost Offers API
  slug: ghost-offers-api
- description: Create, read, update, and delete pages. Pages share the same structure as posts but are used for static content.
  name: Ghost Pages API
  slug: ghost-pages-api
- description: Create, read, update, and delete posts. Posts are the primary content resource in Ghost and support rich content via the Lexical editor format.
  name: Ghost Posts API
  slug: ghost-posts-api
- description: Settings provide access to global publication settings including title, description, navigation, and other configuration values.
  name: Ghost Settings API
  slug: ghost-settings-api
- description: Read basic information about the Ghost site.
  name: Ghost Site API
  slug: ghost-site-api
- description: The Tags API from Ghost — 3 operation(s) for tags.
  name: Ghost Tags API
  slug: ghost-tags-api
- description: Upload, activate, and manage themes that control the front-end appearance of the Ghost publication.
  name: Ghost Themes API
  slug: ghost-themes-api
- description: Manage membership tiers including creating, reading, and updating tier configurations with pricing and benefits.
  name: Ghost Tiers API
  slug: ghost-tiers-api
- description: Read staff user accounts for the Ghost publication.
  name: Ghost Users API
  slug: ghost-users-api
- description: Create, update, and delete webhooks that send HTTP POST notifications when events occur within the publication.
  name: Ghost Webhooks API
  slug: ghost-webhooks-api
artifact_total: 55
asyncapis:
- description: 'Ghost Webhooks allow developers to receive real-time HTTP notifications when specific events occur within a Ghost publication, such as publishing a new post, updating a page, or gaining a new member. '
  name: Ghost Webhooks
  slug: ghost-webhooks-asyncapi
collections:
- collection_type: open
  name: Ghost Admin API
  slug: open-ghost-admin-api
- collection_type: open
  name: Ghost Content API
  slug: open-ghost-content-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ghost-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ghost-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ghost-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ghost-foundation
- group: company
  title: ''
  type: Website
  url: https://ghost.org/
- group: start
  title: ''
  type: Portal
  url: https://docs.ghost.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TryGhost
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TryGhost/Ghost
- group: operate
  title: ''
  type: Forums
  url: https://forum.ghost.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://ghost.org/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/ghost-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ghost-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ghost-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ghost.org/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://ghost.org/changelog/rss/
created: '2026-05-08'
description: Ghost is an open-source publishing platform with hosted (Ghost(Pro)) and self-hosted options. It exposes a write-capable Admin API and a read-only Content API plus webhooks.
finops:
- name: Ghost Finops
  service_category: Publishing
  slug: ghost-finops
graphqls:
- description: 'Ghost does not provide a native GraphQL API. Ghost exposes two RESTful HTTP APIs: the read-only Content API, intended for public browser clients, and the write-capable Admin API, intended for server-s'
  name: Ghost GraphQL API
  slug: ghost-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghost.png
json_schemas:
- name: Author
  property_count: 14
  slug: ghost-author
- name: ErrorResponse
  property_count: 1
  slug: ghost-errorresponse
- name: Label
  property_count: 5
  slug: ghost-label
- name: Ghost Member
  property_count: 16
  slug: ghost-member
- name: MemberInput
  property_count: 5
  slug: ghost-memberinput
- name: NavigationItem
  property_count: 2
  slug: ghost-navigationitem
- name: Newsletter
  property_count: 28
  slug: ghost-newsletter
- name: NewsletterInput
  property_count: 19
  slug: ghost-newsletterinput
- name: Offer
  property_count: 17
  slug: ghost-offer
- name: OfferInput
  property_count: 12
  slug: ghost-offerinput
- name: Page
  property_count: 0
  slug: ghost-page
- name: PaginationMeta
  property_count: 1
  slug: ghost-paginationmeta
- name: Ghost Post
  property_count: 40
  slug: ghost-post
- name: PostInput
  property_count: 28
  slug: ghost-postinput
- name: Settings
  property_count: 24
  slug: ghost-settings
- name: Site
  property_count: 7
  slug: ghost-site
- name: Subscription
  property_count: 10
  slug: ghost-subscription
- name: Tag
  property_count: 21
  slug: ghost-tag
- name: TagInput
  property_count: 8
  slug: ghost-taginput
- name: Theme
  property_count: 3
  slug: ghost-theme
- name: Tier
  property_count: 15
  slug: ghost-tier
- name: TierInput
  property_count: 10
  slug: ghost-tierinput
- name: User
  property_count: 21
  slug: ghost-user
- name: Webhook
  property_count: 13
  slug: ghost-webhook
- name: WebhookInput
  property_count: 4
  slug: ghost-webhookinput
json_structures:
- name: Ghost Structure
  property_count: 0
  slug: ghost-structure
jsonld:
- class_count: 0
  name: Ghost Context
  property_count: 9
  slug: ghost-context
layout: provider
modified: '2026-05-19'
name: Ghost
nav: Providers
network: true
overview: 'Ghost publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Authors API, Images API, Members API, and 11 more. Tagged areas include Publishing, Newsletters, Memberships, Content, and Open Source.


  The Ghost catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Ghost''s developer surface includes authentication, developer portal, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Ghost Plans Pricing
  plan_count: 5
  slug: ghost-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 3
  name: Ghost Rate Limits
  slug: ghost-rate-limits
rules:
- name: Ghost API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: ghost-asyncapi-spectral-rules
- name: Ghost API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ghost-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 78.4
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ghost/refs/heads/main/screenshots/ghost-2026-06-20T181818.png
security:
- kind: authentication
  name: Ghost Authentication
  slug: ghost-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ghost Domain Security
  slug: ghost-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ghost
tags:
- Publishing
- Newsletters
- Memberships
- Content
- Open Source
website: https://ghost.org/
---
