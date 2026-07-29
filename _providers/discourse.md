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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 53
  human_in_the_loop: 2
  name: Discourse Agentic Access
  operation_count: 93
  slug: discourse-agentic-access
  summary_line: 93 operations · 53 acting · 2 human-in-the-loop
api_count: 16
apis:
- description: The Admin API from Discourse — 10 operation(s) for admin.
  name: Discourse Admin API
  slug: discourse-admin-api
- description: The Backups API from Discourse — 2 operation(s) for backups.
  name: Discourse Backups API
  slug: discourse-backups-api
- description: The Badges API from Discourse — 3 operation(s) for badges.
  name: Discourse Badges API
  slug: discourse-badges-api
- description: The Categories API from Discourse — 5 operation(s) for categories.
  name: Discourse Categories API
  slug: discourse-categories-api
- description: The Discourse Calendar - Events API from Discourse — 2 operation(s) for discourse calendar - events.
  name: Discourse Discourse Calendar - Events API
  slug: discourse-discourse-calendar-events-api
- description: The Groups API from Discourse — 8 operation(s) for groups.
  name: Discourse Groups API
  slug: discourse-groups-api
- description: The Invites API from Discourse — 4 operation(s) for invites.
  name: Discourse Invites API
  slug: discourse-invites-api
- description: The Notifications API from Discourse — 2 operation(s) for notifications.
  name: Discourse Notifications API
  slug: discourse-notifications-api
- description: The Posts API from Discourse — 5 operation(s) for posts.
  name: Discourse Posts API
  slug: discourse-posts-api
- description: The Private Messages API from Discourse — 3 operation(s) for private messages.
  name: Discourse Private Messages API
  slug: discourse-private-messages-api
- description: The Search API from Discourse — 1 operation(s) for search.
  name: Discourse Search API
  slug: discourse-search-api
- description: The Site API from Discourse — 2 operation(s) for site.
  name: Discourse Site API
  slug: discourse-site-api
- description: The Tags API from Discourse — 4 operation(s) for tags.
  name: Discourse Tags API
  slug: discourse-tags-api
- description: The Topics API from Discourse — 14 operation(s) for topics.
  name: Discourse Topics API
  slug: discourse-topics-api
- description: The Uploads API from Discourse — 7 operation(s) for uploads.
  name: Discourse Uploads API
  slug: discourse-uploads-api
- description: The Users API from Discourse — 23 operation(s) for users.
  name: Discourse Users API
  slug: discourse-users-api
artifact_total: 24
collections:
- collection_type: open
  name: Discourse API Documentation
  slug: open-discourse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/discourse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/discourse-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/discourse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discourse-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civilized-discourse-construction-kit-inc
- group: company
  title: ''
  type: Website
  url: https://www.discourse.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.discourse.org/
- group: operate
  title: ''
  type: Community
  url: https://meta.discourse.org/
- group: commercial
  title: ''
  type: Plans
  url: https://www.discourse.org/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.discourse.org/
- group: build
  title: ''
  type: Plugins
  url: https://www.discourse.org/plugins
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/discourse/discourse
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/discourse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.discourse.org/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.discourse.org/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.discourse.org/
- group: operate
  title: ''
  type: Support
  url: https://meta.discourse.org/c/support/api/52
created: '2023-11-13'
description: At Discourse, our mission is to democratize online community and teamwork by raising the standard of civilized discourse on the Internet. We achieve this through delivering the best community and forum software. The Discourse API exposes administrative and content endpoints for categories, topics, posts, users, groups, tags, uploads, badges, and more.
finops:
- name: Discourse Finops
  service_category: API
  slug: discourse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/discourse.png
layout: provider
modified: '2026-05-19'
name: Discourse
nav: Providers
network: true
overview: 'Discourse publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Backups API, Badges API, and 13 more. Tagged areas include Communities, Forums, and Open Source.


  Discourse''s developer surface includes documentation, engineering blog, support, and 14 more developer resources.'
plans:
- name: Discourse Plans Pricing
  plan_count: 3
  slug: discourse-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Discourse Rate Limits
  slug: discourse-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -3.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 41.6
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/discourse/refs/heads/main/screenshots/discourse-2026-06-20T180038.png
security:
- kind: domain-security
  name: Discourse Domain Security
  slug: discourse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Discourse Vulnerability Disclosure
  slug: discourse-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Discourse Trust Center
  slug: discourse-trust-center
  summary_line: SOC 2, ISO 27001
slug: discourse
tags:
- Communities
- Forums
- Open Source
website: https://www.discourse.org/
---
