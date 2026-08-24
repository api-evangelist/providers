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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Django Cms Agentic Access
  operation_count: 23
  slug: django-cms-agentic-access
  summary_line: 23 operations
api_count: 7
apis:
- description: Page breadcrumb trails
  name: Django CMS Breadcrumbs API
  slug: django-cms-breadcrumbs-api
- description: Health check endpoint for monitoring
  name: Django CMS Health API
  slug: django-cms-health-api
- description: Site language configuration
  name: Django CMS Languages API
  slug: django-cms-languages-api
- description: Navigation menu structures
  name: Django CMS Menus API
  slug: django-cms-menus-api
- description: CMS page content and tree structure
  name: Django CMS Pages API
  slug: django-cms-pages-api
- description: Placeholder content with nested plugin data
  name: Django CMS Placeholders API
  slug: django-cms-placeholders-api
- description: Plugin type definitions and schema
  name: Django CMS Plugins API
  slug: django-cms-plugins-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: djangocms-rest Breadcrumbs API
  slug: open-django-cms-breadcrumbs-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Health API
  slug: open-django-cms-health-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Languages API
  slug: open-django-cms-languages-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Menus API
  slug: open-django-cms-menus-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Pages API
  slug: open-django-cms-pages-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Placeholders API
  slug: open-django-cms-placeholders-api
- collection_type: open
  name: djangocms-rest Breadcrumbs Plugins API
  slug: open-django-cms-plugins-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/django-cms/djangocms-rest/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/django-cms/djangocms-rest/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/django-cms/djangocms-rest/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/django-cms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/django-cms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.django-cms.org/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.django-cms.org/en/latest/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/django-cms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/django-cms-association
- group: company
  title: ''
  type: Blog
  url: https://www.django-cms.org/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.django-cms.org/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.django-cms.org/
- group: other
  title: ''
  type: X
  url: https://x.com/djangocms
- group: commercial
  title: ''
  type: Plans
  url: plans/django-cms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/django-cms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/django-cms-finops.yml
created: '2026-06-13'
description: Django CMS is an open-source, enterprise-grade content management system built on Django and Python. It provides a REST API via the djangocms-rest package (built on Django REST Framework and drf-spectacular) that exposes pages, plugins, placeholders, navigation menus, breadcrumbs, and content structures as a browsable, read-only JSON/OpenAPI 3 interface. The API enables headless CMS deployments, allowing decoupled frontend applications — SPAs, static site generators, and mobile apps — to consume CMS-managed content with full multi-language and multi-site support.
finops:
- name: Django Cms Finops
  service_category: ''
  slug: django-cms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/django-cms.png
json_schemas:
- name: Django CMS Page Content
  property_count: 22
  slug: djangocms-page-content
jsonld:
- class_count: 0
  name: Djangocms Context
  property_count: 47
  slug: djangocms-context
layout: provider
modified: '2026-06-13'
name: Django CMS
nav: Providers
network: true
overview: 'Django CMS publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Breadcrumbs API, Health API, Languages API, and 4 more. Tagged areas include CMS, Content Management, Django, Python, and Headless CMS.


  The Django CMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Django CMS''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Django Cms Plans Pricing
  plan_count: 3
  slug: django-cms-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Django Cms Rate Limits
  slug: django-cms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Django CMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: django-cms-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 57.8
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 57.9
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/django-cms/refs/heads/main/screenshots/django-cms-2026-06-20T180058.png
security:
- kind: domain-security
  name: Django Cms Domain Security
  slug: django-cms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: django-cms
tags:
- CMS
- Content Management
- Django
- Python
- Headless CMS
- REST API
- Open-Source
- Pages
- Plugins
- Placeholders
website: https://www.django-cms.org/en/
---
