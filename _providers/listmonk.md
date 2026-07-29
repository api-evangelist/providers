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
- acting_count: 34
  human_in_the_loop: 1
  name: Listmonk Agentic Access
  operation_count: 53
  slug: listmonk-agentic-access
  summary_line: 53 operations · 34 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: The Bounces API from listmonk — 2 operation(s) for bounces.
  name: listmonk Bounces API
  slug: listmonk-bounces-api
- description: The Campaigns API from listmonk — 8 operation(s) for campaigns.
  name: listmonk Campaigns API
  slug: listmonk-campaigns-api
- description: The Import API from listmonk — 2 operation(s) for import.
  name: listmonk Import API
  slug: listmonk-import-api
- description: The Lists API from listmonk — 3 operation(s) for lists.
  name: listmonk Lists API
  slug: listmonk-lists-api
- description: The Media API from listmonk — 2 operation(s) for media.
  name: listmonk Media API
  slug: listmonk-media-api
- description: The Subscribers API from listmonk — 10 operation(s) for subscribers.
  name: listmonk Subscribers API
  slug: listmonk-subscribers-api
- description: The Templates API from listmonk — 5 operation(s) for templates.
  name: listmonk Templates API
  slug: listmonk-templates-api
- description: The Transactional API from listmonk — 1 operation(s) for transactional.
  name: listmonk Transactional API
  slug: listmonk-transactional-api
artifact_total: 15
collections:
- collection_type: open
  name: listmonk API
  slug: open-listmonk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/listmonk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/listmonk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/listmonk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/knadh/listmonk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/in/knadh
- group: company
  title: ''
  type: Website
  url: https://listmonk.app
- group: docs
  title: ''
  type: Documentation
  url: https://listmonk.app/docs/apis/apis/
- group: commercial
  title: ''
  type: Plans
  url: plans/listmonk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/listmonk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/listmonk-finops.yml
created: '2026-06-25'
description: listmonk is a free and open-source, self-hosted newsletter and mailing-list manager built in Go with a Vue front end. Every feature in the admin UI is backed by a documented REST API on the self-hosted instance (Basic auth with an API user and token) covering subscribers, lists, campaigns, templates, media, CSV import, transactional messages, and bounces. There is no hosted SaaS - users run their own instance.
finops:
- name: Listmonk Finops
  service_category: Email and Messaging
  slug: listmonk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listmonk.png
layout: provider
modified: '2026-06-25'
name: listmonk
nav: Providers
network: true
overview: 'listmonk publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bounces API, Campaigns API, Import API, and 5 more. Tagged areas include Email, Newsletter, Mailing List, Open Source, and Self-Hosted.


  listmonk''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Listmonk Plans Pricing
  plan_count: 1
  slug: listmonk-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Listmonk Rate Limits
  slug: listmonk-rate-limits
score:
  band: thin
  composite: 32.2
  delta: -2.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 44.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listmonk/refs/heads/main/screenshots/listmonk-2026-07-25T225325.png
security:
- kind: authentication
  name: Listmonk Authentication
  slug: listmonk-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Listmonk Domain Security
  slug: listmonk-domain-security
  summary_line: TLSv1.3
slug: listmonk
tags:
- Email
- Newsletter
- Mailing List
- Open Source
- Self-Hosted
website: https://listmonk.app
---
