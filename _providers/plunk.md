---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Plunk Agentic Access
  operation_count: 14
  slug: plunk-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 4
apis:
- description: Create and send marketing campaigns.
  name: Plunk Campaigns API
  slug: plunk-campaigns-api
- description: Manage contacts and their subscription state.
  name: Plunk Contacts API
  slug: plunk-contacts-api
- description: Track contact events that drive automations.
  name: Plunk Events API
  slug: plunk-events-api
- description: Send transactional email.
  name: Plunk Transactional API
  slug: plunk-transactional-api
artifact_total: 11
collections:
- collection_type: open
  name: Plunk API
  slug: open-plunk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plunk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plunk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plunk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useplunk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useplunk
- group: company
  title: ''
  type: Website
  url: https://www.useplunk.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useplunk.com
- group: commercial
  title: ''
  type: Plans
  url: plans/plunk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plunk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plunk-finops.yml
created: '2026-06-20'
description: Plunk is an open-source (AGPL-3.0) email platform for SaaS that unifies transactional email, marketing campaigns, and event-driven automations behind a single REST API. The hosted service runs at api.useplunk.com with Bearer secret / public API keys, and the entire stack can be self-hosted with Docker Compose for full data ownership and no per-email costs.
finops:
- name: Plunk Finops
  service_category: Email and Messaging
  slug: plunk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plunk.png
layout: provider
modified: '2026-06-20'
name: Plunk
nav: Providers
network: true
overview: 'Plunk publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Events API, and 1 more. Tagged areas include Email, Transactional Email, Marketing, Automation, and Open Source.


  Plunk''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Plunk Plans Pricing
  plan_count: 3
  slug: plunk-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 3
  name: Plunk Rate Limits
  slug: plunk-rate-limits
score:
  band: thin
  composite: 40.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.3
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/screenshots/plunk-2026-06-20T191814.png
security:
- kind: authentication
  name: Plunk Authentication
  slug: plunk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plunk Domain Security
  slug: plunk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plunk
tags:
- Email
- Transactional Email
- Marketing
- Automation
- Open Source
- SaaS
website: https://www.useplunk.com
---
