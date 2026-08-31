---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/django-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/django-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/django-software-foundation
- group: company
  title: ''
  type: Website
  url: https://www.djangoproject.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.djangoproject.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/django/django
- group: company
  title: ''
  type: Blog
  url: https://www.djangoproject.com/rss/weblog/
created: '2025-01-01'
description: A high-level Python web framework that encourages rapid development and clean, pragmatic design. Django follows the model-template-views architectural pattern and includes an ORM, automatic admin interface, robust template system, and quick internationalization support. The current release line is Django 6.0, supported by the non-profit Django Software Foundation, and it powers some of the busiest websites globally.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/django.png
layout: provider
modified: '2026-04-28'
name: Django
nav: Providers
network: true
overview: 'Django is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, MVC, ORM, Python, and Web Framework.


  Django''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/django/refs/heads/main/screenshots/django-2026-06-20T180055.png
security:
- kind: domain-security
  name: Django Domain Security
  slug: django-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Django Vulnerability Disclosure
  slug: django-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: django
tags:
- Backend
- MVC
- ORM
- Python
- Web Framework
website: https://www.djangoproject.com/
---
