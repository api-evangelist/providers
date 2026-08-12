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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Ghost Org Agentic Access
  operation_count: 56
  slug: ghost-org-agentic-access
  summary_line: 56 operations · 26 acting
api_count: 19
apis:
- description: Image uploads.
  name: Ghost Admin - Images API
  slug: ghost-org-admin-images-api
- description: Read-write member labels.
  name: Ghost Admin - Labels API
  slug: ghost-org-admin-labels-api
- description: Read-write members.
  name: Ghost Admin - Members API
  slug: ghost-org-admin-members-api
- description: Read-write newsletters.
  name: Ghost Admin - Newsletters API
  slug: ghost-org-admin-newsletters-api
- description: Read-write promotional offers.
  name: Ghost Admin - Offers API
  slug: ghost-org-admin-offers-api
- description: Read-write pages.
  name: Ghost Admin - Pages API
  slug: ghost-org-admin-pages-api
- description: Read-write posts.
  name: Ghost Admin - Posts API
  slug: ghost-org-admin-posts-api
- description: Read-only public site metadata.
  name: Ghost Admin - Site API
  slug: ghost-org-admin-site-api
- description: Read-write tags.
  name: Ghost Admin - Tags API
  slug: ghost-org-admin-tags-api
- description: Theme upload and activation.
  name: Ghost Admin - Themes API
  slug: ghost-org-admin-themes-api
- description: Read-write subscription tiers.
  name: Ghost Admin - Tiers API
  slug: ghost-org-admin-tiers-api
- description: Read-only staff users.
  name: Ghost Admin - Users API
  slug: ghost-org-admin-users-api
- description: Outbound webhook management.
  name: Ghost Admin - Webhooks API
  slug: ghost-org-admin-webhooks-api
- description: Read-only authors.
  name: Ghost Content - Authors API
  slug: ghost-org-content-authors-api
- description: Read-only published pages.
  name: Ghost Content - Pages API
  slug: ghost-org-content-pages-api
- description: Read-only published posts.
  name: Ghost Content - Posts API
  slug: ghost-org-content-posts-api
- description: Read-only public site settings.
  name: Ghost Content - Settings API
  slug: ghost-org-content-settings-api
- description: Read-only tags.
  name: Ghost Content - Tags API
  slug: ghost-org-content-tags-api
- description: Read-only public subscription tiers.
  name: Ghost Content - Tiers API
  slug: ghost-org-content-tiers-api
artifact_total: 59
asyncapis:
- description: 'Ghost Webhooks allow developers to receive real-time HTTP notifications when specific events occur within a Ghost publication, such as publishing a new post, updating a page, or gaining a new member. '
  name: Ghost Webhooks
  slug: ghost-org-webhooks-asyncapi
collections:
- collection_type: open
  name: Ghost Admin API
  slug: open-ghost-org-admin-api
- collection_type: open
  name: Ghost Content API
  slug: open-ghost-org-content-api
- collection_type: open
  name: Ghost Content and Admin APIs
  slug: open-ghost-org
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/TryGhost/Ghost/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/TryGhost/Ghost/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/TryGhost/Ghost/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/TryGhost/Ghost/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/TryGhost/Ghost/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/TryGhost/Ghost/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ghost-org-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ghost-org-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ghost-org-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ghost-foundation
- group: company
  title: ''
  type: Website
  url: https://ghost.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ghost.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TryGhost
- group: commercial
  title: ''
  type: Plans
  url: plans/ghost-org-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ghost-org-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ghost-org-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ghost.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://ghost.org/changelog
- group: start
  title: ''
  type: Portal
  url: https://docs.ghost.org/
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
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.ghost.org/llms.txt
created: '2026-07-05'
description: Ghost is an open-source (MIT) publishing platform for professional publications, newsletters, memberships, and paid subscriptions. It can be self-hosted for free or run as the managed Ghost(Pro) service, with all Ghost(Pro) revenue funding the non-profit Ghost Foundation. Every Ghost site exposes two documented public REST APIs under https://{site}/ghost/api/. The Content API is a read-only, key-authenticated interface for delivering published posts, pages, tags, authors, tiers, and settings to front-ends and static sites. The Admin API is a read-write, token-authenticated (JWT) interface for managing posts, pages, members, tags, tiers, offers, newsletters, users, media, themes, and webhooks.
finops:
- name: Ghost Org Finops
  service_category: Publishing and Content Management
  slug: ghost-org-finops
graphqls:
- description: 'Ghost does not provide a native GraphQL API. Ghost exposes two RESTful HTTP APIs: the read-only Content API, intended for public browser clients, and the write-capable Admin API, intended for server-s'
  name: Ghost GraphQL API
  slug: ghost-org-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghost-org.png
json_schemas:
- name: Author
  property_count: 14
  slug: ghost-org-author
- name: ErrorResponse
  property_count: 1
  slug: ghost-org-errorresponse
- name: Label
  property_count: 5
  slug: ghost-org-label
- name: Ghost Member
  property_count: 16
  slug: ghost-org-member
- name: MemberInput
  property_count: 5
  slug: ghost-org-memberinput
- name: NavigationItem
  property_count: 2
  slug: ghost-org-navigationitem
- name: Newsletter
  property_count: 28
  slug: ghost-org-newsletter
- name: NewsletterInput
  property_count: 19
  slug: ghost-org-newsletterinput
- name: Offer
  property_count: 17
  slug: ghost-org-offer
- name: OfferInput
  property_count: 12
  slug: ghost-org-offerinput
- name: Page
  property_count: 0
  slug: ghost-org-page
- name: PaginationMeta
  property_count: 1
  slug: ghost-org-paginationmeta
- name: Ghost Post
  property_count: 40
  slug: ghost-org-post
- name: PostInput
  property_count: 28
  slug: ghost-org-postinput
- name: Settings
  property_count: 24
  slug: ghost-org-settings
- name: Site
  property_count: 7
  slug: ghost-org-site
- name: Subscription
  property_count: 10
  slug: ghost-org-subscription
- name: Tag
  property_count: 21
  slug: ghost-org-tag
- name: TagInput
  property_count: 8
  slug: ghost-org-taginput
- name: Theme
  property_count: 3
  slug: ghost-org-theme
- name: Tier
  property_count: 15
  slug: ghost-org-tier
- name: TierInput
  property_count: 10
  slug: ghost-org-tierinput
- name: User
  property_count: 21
  slug: ghost-org-user
- name: Webhook
  property_count: 13
  slug: ghost-org-webhook
- name: WebhookInput
  property_count: 4
  slug: ghost-org-webhookinput
json_structures:
- name: Ghost Org Structure
  property_count: 0
  slug: ghost-org-structure
jsonld:
- class_count: 0
  name: Ghost Org Context
  property_count: 9
  slug: ghost-org-context
layout: provider
modified: '2026-08-08'
name: Ghost
nav: Providers
network: true
overview: 'Ghost publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Admin - Images API, Admin - Labels API, Admin - Members API, and 16 more. Tagged areas include Publishing, Newsletters, Memberships, Subscriptions, and CMS.


  The Ghost catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Ghost''s developer surface includes authentication, documentation, engineering blog, changelog, developer portal, pricing, and 17 more developer resources.'
plans:
- name: Ghost Org Plans Pricing
  plan_count: 5
  slug: ghost-org-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 5
  name: Ghost Org Rate Limits
  slug: ghost-org-rate-limits
rules:
- name: Ghost API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: ghost-org-asyncapi-spectral-rules
- name: Ghost API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ghost-org-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.3
  delta: 3.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.9
    developer_ergonomics: 34.8
    discoverability: 81.5
    governance: 41.7
    operational_transparency: 63.2
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 42.4
      derived: 0
      marker_coverage: 0.0
      total: 33
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ghost-org/refs/heads/main/screenshots/ghost-org-2026-07-25T215752.png
security:
- kind: authentication
  name: Ghost Org Authentication
  slug: ghost-org-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ghost Org Domain Security
  slug: ghost-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ghost-org
tags:
- Publishing
- Newsletters
- Memberships
- Subscriptions
- CMS
- Open Source
- Content
website: https://ghost.org
---
