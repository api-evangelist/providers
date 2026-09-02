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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: Core Python built-in modules and standard library.
  name: Python Standard Library
  slug: python-standard-library
- description: HTTP library for Python - elegant and simple HTTP requests.
  name: Requests
  slug: requests
- description: Lightweight WSGI web application framework.
  name: Flask
  slug: flask
- description: High-level Python web framework for rapid development.
  name: Django
  slug: django
- description: Data analysis and manipulation library.
  name: Pandas
  slug: pandas
- description: Fundamental package for scientific computing with Python.
  name: NumPy
  slug: numpy
- description: Modern, fast web framework for building APIs with Python 3.7+.
  name: FastAPI
  slug: fastapi
- description: SQL toolkit and Object-Relational Mapping (ORM) library.
  name: SQLAlchemy
  slug: sqlalchemy
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/python-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thepsf
- group: company
  title: ''
  type: Website
  url: https://www.python.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.python.org/3/
- group: operate
  title: ''
  type: Community
  url: https://www.python.org/community/
created: '2024-01-01'
description: A collection of commonly used Python APIs and libraries including the standard library and popular frameworks like Flask, Django, FastAPI, Pandas, and NumPy.
finops:
- name: Python Finops
  service_category: API
  slug: python-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/python.png
layout: provider
modified: '2026-04-28'
name: Python Standard Library and Popular
nav: Providers
network: true
overview: 'Python Standard Library and Popular publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Frameworks, Libraries, Programming Language, and Python.


  Python Standard Library and Popular''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Python Plans Pricing
  plan_count: 3
  slug: python-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Python Rate Limits
  slug: python-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/python/refs/heads/main/screenshots/python-2026-06-20T192330.png
security:
- kind: domain-security
  name: Python Domain Security
  slug: python-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: python
tags:
- Frameworks
- Libraries
- Programming Language
- Python
website: https://www.python.org
---
