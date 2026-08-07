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
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Mention Agentic Access
  operation_count: 37
  slug: mention-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 8
apis:
- description: The Accounts API from Mention — 3 operation(s) for accounts.
  name: Mention Accounts API
  slug: mention-accounts-api
- description: The Alerts API from Mention — 8 operation(s) for alerts.
  name: Mention Alerts API
  slug: mention-alerts-api
- description: The Authors API from Mention — 1 operation(s) for authors.
  name: Mention Authors API
  slug: mention-authors-api
- description: The Mentions API from Mention — 6 operation(s) for mentions.
  name: Mention Mentions API
  slug: mention-mentions-api
- description: The Shares API from Mention — 1 operation(s) for shares.
  name: Mention Shares API
  slug: mention-shares-api
- description: The Stats API from Mention — 1 operation(s) for stats.
  name: Mention Stats API
  slug: mention-stats-api
- description: The Tags API from Mention — 1 operation(s) for tags.
  name: Mention Tags API
  slug: mention-tags-api
- description: The Tasks API from Mention — 1 operation(s) for tasks.
  name: Mention Tasks API
  slug: mention-tasks-api
artifact_total: 14
collections:
- collection_type: open
  name: Mention API
  slug: open-mention
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mention-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mention-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mention
- group: start
  title: ''
  type: Portal
  url: https://mention.com/en/media-monitoring-api/
- group: company
  title: ''
  type: Website
  url: https://mention.com/
- group: start
  title: ''
  type: Signup
  url: https://mention.com/en/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.mention.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://mention.com/en/pricing/
- group: operate
  title: ''
  type: Support
  url: https://en.support.mention.com/
- group: company
  title: ''
  type: Blog
  url: https://mention.com/en/blog/feed/
created: '2026-03-16'
description: Mention is a media monitoring and social listening platform that monitors over one billion sources in real-time across 42 languages. Its JSON-based RESTful API gives developers programmatic access to alerts, mentions, streaming data, and account management features.
finops:
- name: Mention Finops
  service_category: API
  slug: mention-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mention.png
layout: provider
modified: '2026-05-19'
name: Mention
nav: Providers
network: true
overview: 'Mention publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Alerts API, Authors API, and 5 more. Tagged areas include Alerts, Brand Monitoring, Media Monitoring, and Social Listening.


  Mention''s developer surface includes developer portal, signup flow, pricing, support, engineering blog, and 5 more developer resources.'
plans:
- name: Mention Plans Pricing
  plan_count: 3
  slug: mention-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Mention Rate Limits
  slug: mention-rate-limits
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 48.8
    developer_ergonomics: 15.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mention/refs/heads/main/screenshots/mention-2026-06-20T185146.png
security:
- kind: domain-security
  name: Mention Domain Security
  slug: mention-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mention
tags:
- Alerts
- Brand Monitoring
- Media Monitoring
- Social Listening
website: https://mention.com/
---
