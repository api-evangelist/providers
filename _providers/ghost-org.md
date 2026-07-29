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
artifact_total: 26
collections:
- collection_type: open
  name: Ghost Content and Admin APIs
  slug: open-ghost-org
common:
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
created: '2026-07-05'
description: Ghost is an open-source (MIT) publishing platform for professional publications, newsletters, memberships, and paid subscriptions. It can be self-hosted for free or run as the managed Ghost(Pro) service, with all Ghost(Pro) revenue funding the non-profit Ghost Foundation. Every Ghost site exposes two documented public REST APIs under https://{site}/ghost/api/. The Content API is a read-only, key-authenticated interface for delivering published posts, pages, tags, authors, tiers, and settings to front-ends and static sites. The Admin API is a read-write, token-authenticated (JWT) interface for managing posts, pages, members, tags, tiers, offers, newsletters, users, media, themes, and webhooks.
finops:
- name: Ghost Org Finops
  service_category: Publishing and Content Management
  slug: ghost-org-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ghost-org.png
layout: provider
modified: '2026-07-05'
name: Ghost
nav: Providers
network: true
overview: 'Ghost publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Admin - Images API, Admin - Labels API, Admin - Members API, and 16 more. Tagged areas include Publishing, Newsletters, Memberships, Subscriptions, and CMS.


  Ghost''s developer surface includes authentication, documentation, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Ghost Org Plans Pricing
  plan_count: 5
  slug: ghost-org-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Ghost Org Rate Limits
  slug: ghost-org-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -3.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
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
