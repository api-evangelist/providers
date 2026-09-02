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
api_count: 1
apis:
- description: 'Flask is a lightweight WSGI web application framework for Python. It is commonly used as a foundation for building HTTP APIs and web services. While Flask itself does not expose an HTTP API, it ships '
  name: Flask
  slug: flask
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pallets/flask/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/pallets/flask/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/pallets/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/pallets/flask/blob/main/docs/contributing.rst
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flask-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flask.palletsprojects.com/
- group: docs
  title: ''
  type: Documentation
  url: https://flask.palletsprojects.com/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://flask.palletsprojects.com/en/stable/quickstart/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pallets
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pallets/flask
- group: company
  title: ''
  type: Blog
  url: https://palletsprojects.com/blog/
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/flask/
- group: build
  title: ''
  type: Extensions
  url: https://flask.palletsprojects.com/en/stable/extensions/
- group: operate
  title: ''
  type: ChangeLog
  url: https://flask.palletsprojects.com/en/stable/changes/
- group: commercial
  title: ''
  type: License
  url: https://github.com/pallets/flask/blob/main/LICENSE.txt
created: '2026-03-26'
description: Flask is a lightweight WSGI web application framework for Python, designed to make getting started quick and easy with the ability to scale up to complex applications. It provides a simple core with Jinja2 templating and Werkzeug WSGI toolkit, and is extensible through a rich ecosystem of extensions for database integration, form validation, authentication, and more. Flask is a popular foundation for building APIs and web services in Python.
finops:
- name: Flask Finops
  service_category: API
  slug: flask-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flask.png
json_schemas:
- name: Flask Application Configuration
  property_count: 42
  slug: flask-config
layout: provider
modified: '2026-04-28'
name: Flask
nav: Providers
network: true
overview: 'Flask publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Frameworks, Lightweight, Microframework, pallets, and Python.


  The Flask catalog on APIs.io includes 1 Spectral governance ruleset.


  Flask''s developer surface includes documentation, getting-started guide, engineering blog, changelog, and 11 more developer resources.'
plans:
- name: Flask Plans Pricing
  plan_count: 3
  slug: flask-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Flask Rate Limits
  slug: flask-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Flask API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: flask-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 8.0
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 24.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flask/refs/heads/main/screenshots/flask-2026-06-20T181302.png
security:
- kind: domain-security
  name: Flask Domain Security
  slug: flask-domain-security
  summary_line: TLSv1.3
slug: flask
tags:
- Frameworks
- Lightweight
- Microframework
- pallets
- Python
- Web Framework
- WSGI
website: https://flask.palletsprojects.com/
---
