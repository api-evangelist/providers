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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Wagtail REST API v2 exposes site content — pages, images, documents, and redirects — as JSON. Endpoints support filtering by field value, tree relationships (child_of, ancestor_of, descendant_of),
  name: Wagtail API v2
  slug: wagtail-api-v2
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wagtail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wagtail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wagtail.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wagtail.org/en/latest/advanced_topics/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wagtail
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wagtail-cms
- group: company
  title: ''
  type: Blog
  url: https://wagtail.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://wagtail.org/services/
- group: other
  title: ''
  type: X
  url: https://twitter.com/WagtailCMS
- group: commercial
  title: ''
  type: Plans
  url: plans/wagtail-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wagtail-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wagtail-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wagtail.json
created: 2026-06-13
description: Wagtail is a leading open-source Python content management system built on Django. It provides a REST API v2 for accessing pages, images, documents, snippets, and custom content types in both headless and traditional deployments. The API delivers JSON-formatted content to web, mobile, and other non-web clients, supporting filtering, full-text search, field selection, and pagination. Wagtail is used by NASA, Google, NHS, Mozilla, MIT, and thousands of other organisations worldwide.
finops:
- name: Wagtail Finops
  service_category: ''
  slug: wagtail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wagtail.png
layout: provider
modified: 2026-06-13
name: Wagtail
nav: Providers
network: true
overview: 'Wagtail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, Django, Python, and Headless CMS.


  Wagtail''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Wagtail Plans Pricing
  plan_count: 5
  slug: wagtail-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Wagtail Rate Limits
  slug: wagtail-rate-limits
score:
  band: emerging
  composite: 19.9
  delta: 0.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wagtail/refs/heads/main/screenshots/wagtail-2026-06-20T201200.png
security:
- kind: domain-security
  name: Wagtail Domain Security
  slug: wagtail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wagtail Vulnerability Disclosure
  slug: wagtail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wagtail
tags:
- CMS
- Content Management
- Django
- Python
- Headless CMS
- Open Source
- REST API
- Pages
- Images
- Documents
website: https://wagtail.org
---
