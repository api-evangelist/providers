---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Gutendex is a JSON web API for Project Gutenberg ebook metadata. It provides access to the catalog of 75,000+ public domain books with filtering by language, copyright status, topic, author lifespan, '
  name: Gutendex API
  slug: gutendex
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gutenberg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gutenberg.org/
- group: docs
  title: ''
  type: Documentation
  url: https://gutendex.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/gutenbergtools
- group: company
  title: ''
  type: Blog
  url: https://www.gutenberg.org/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://gutendex.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.gutenberg.org/
- group: other
  title: ''
  type: X
  url: https://twitter.com/gutenberg_org
- group: commercial
  title: ''
  type: Plans
  url: plans/gutenberg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gutenberg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gutenberg-finops.yml
created: '2026-06-13'
description: Project Gutenberg is a free ebook library providing access to over 75,000 public domain books via the Gutendex REST API. The API enables developers to search and retrieve bibliographic metadata for books and authors, filter by language, copyright status, topic, and MIME type, and access download links for multiple formats including EPUB, Kindle, HTML, and plain text. Project Gutenberg has pioneered free ebooks since 1971 and the Gutendex API makes its catalog programmatically accessible via a simple JSON REST interface with no authentication required.
finops:
- name: Gutenberg Finops
  service_category: ''
  slug: gutenberg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gutenberg.png
layout: provider
modified: '2026-06-13'
name: Project Gutenberg
nav: Providers
network: true
overview: 'Project Gutenberg publishes 1 API on the [APIs.io](https://apis.io/) network: Gutendex API. Tagged areas include Books, Ebooks, Public Domain, Literature, and Library.


  Project Gutenberg''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Gutenberg Plans Pricing
  plan_count: 2
  slug: gutenberg-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Gutenberg Rate Limits
  slug: gutenberg-rate-limits
score:
  band: thin
  composite: 28.5
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gutenberg/refs/heads/main/screenshots/gutenberg-2026-06-20T182441.png
security:
- kind: domain-security
  name: Gutenberg Domain Security
  slug: gutenberg-domain-security
  summary_line: TLSv1.3
slug: gutenberg
tags:
- Books
- Ebooks
- Public Domain
- Literature
- Library
- Metadata
- EPUB
website: https://www.gutenberg.org/
---
