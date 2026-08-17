---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The BookStack REST API provides programmatic access to manage the full content hierarchy of a BookStack instance including books, chapters, pages, shelves, attachments, image galleries, comments, role
  name: BookStack REST API
  slug: bookstack-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bookstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bookstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bookstackapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bookstackapp.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://codeberg.org/bookstack/bookstack
- group: company
  title: ''
  type: Blog
  url: https://www.bookstackapp.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bookstackapp.com/blog/index.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bookstackapp.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bookstackapp.com/
- group: other
  title: ''
  type: X
  url: https://fosstodon.org/@bookstack
- group: commercial
  title: ''
  type: Plans
  url: plans/bookstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bookstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bookstack-finops.yml
created: 2026-06-13
description: BookStack is a free, open-source, self-hosted wiki and documentation platform built with PHP and Laravel. It provides a REST API for managing the full content hierarchy including books, chapters, pages, and shelves, as well as attachments, image galleries, comments, roles, users, audit logs, imports, search, tags, and content permissions across hierarchical knowledge bases.
finops:
- name: Bookstack Finops
  service_category: ''
  slug: bookstack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bookstack.png
layout: provider
modified: 2026-06-13
name: BookStack
nav: Providers
network: true
overview: 'BookStack publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Wiki, Documentation, Knowledge Base, Self-Hosted, and Open Source.


  BookStack''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Bookstack Plans Pricing
  plan_count: 1
  slug: bookstack-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 1
  name: Bookstack Rate Limits
  slug: bookstack-rate-limits
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 22.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bookstack/refs/heads/main/screenshots/bookstack-2026-06-20T173603.png
security:
- kind: domain-security
  name: Bookstack Domain Security
  slug: bookstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bookstack Vulnerability Disclosure
  slug: bookstack-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bookstack
tags:
- Wiki
- Documentation
- Knowledge Base
- Self-Hosted
- Open Source
- Content Management
website: https://www.bookstackapp.com/
---
