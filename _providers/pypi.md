---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 1
  human_in_the_loop: 0
  name: Pypi Agentic Access
  operation_count: 11
  slug: pypi-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 6
apis:
- description: 'The PyPI Index API implements the PEP 503 (HTML) and PEP 691 (JSON) simple repository standards for discovering and downloading Python packages. It provides a machine-readable index of all registered '
  name: PyPI Index API
  slug: index
- description: 'The PyPI Upload API is the endpoint used by tools like twine and build frontends to publish Python package distributions to the Python Package Index. Served at upload.pypi.org, it emulates the legacy '
  name: PyPI Upload API
  slug: upload
- description: 'PyPI provides RSS feeds that allow developers and tools to monitor package activity on the Python Package Index. Three feeds are available: the Newest Packages feed for recently registered projects, t'
  name: PyPI RSS Feeds
  slug: feeds
- description: Retrieve aggregate download statistics and time series data for Python packages.
  name: PyPI Downloads API
  slug: pypi-downloads-api
- description: Retrieve metadata about Python packages hosted on PyPI, including release information, download URLs, and vulnerability data.
  name: PyPI Projects API
  slug: pypi-projects-api
- description: Retrieve digital attestations and provenance information for Python package distribution files hosted on PyPI.
  name: PyPI Provenance API
  slug: pypi-provenance-api
artifact_total: 22
collections:
- collection_type: open
  name: PyPI Index API
  slug: open-pypi-index-api
- collection_type: open
  name: PyPI Integrity API
  slug: open-pypi-integrity-api
- collection_type: open
  name: PyPI JSON API
  slug: open-pypi-json-api
- collection_type: open
  name: PyPI Stats API
  slug: open-pypi-stats-api
- collection_type: open
  name: PyPI Upload API
  slug: open-pypi-upload-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pypi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pypi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pypi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pypi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pypi
- group: start
  title: ''
  type: Portal
  url: https://docs.pypi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pypi.org/api/
- group: company
  title: ''
  type: Website
  url: https://pypi.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.python.org/pypi.org/Privacy-Policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.python.org/pypi.org/Terms-of-Use/
- group: operate
  title: ''
  type: Support
  url: https://pypi.org/help/
- group: company
  title: ''
  type: Blog
  url: https://blog.pypi.org/
- group: start
  title: ''
  type: Login
  url: https://pypi.org/account/login/
created: '2025-03-01'
description: PyPI (Python Package Index) is the official third-party software repository for Python, serving as the central hub where developers publish and distribute Python packages. Their developer platform provides a suite of APIs for querying package metadata, downloading distributions, publishing packages, verifying supply chain integrity, and tracking download statistics across the Python ecosystem.
finops:
- name: Pypi Finops
  service_category: Package Registry
  slug: pypi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pypi.png
json_schemas:
- name: PyPI Project Metadata
  property_count: 24
  slug: pypi-project-metadata
- name: PyPI Provenance
  property_count: 2
  slug: pypi-provenance
jsonld:
- class_count: 0
  name: Pypi Context
  property_count: 5
  slug: pypi-context
layout: provider
modified: '2026-05-19'
name: PyPI
nav: Providers
network: true
overview: 'PyPI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Index API, Upload API, Downloads API, and 2 more. Tagged areas include Developer Tools, Open Source, Package Management, Packages, and Python.


  The PyPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PyPI''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 8 more developer resources.'
plans:
- name: Pypi Plans Pricing
  plan_count: 1
  slug: pypi-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Pypi Rate Limits
  slug: pypi-rate-limits
rules:
- name: PyPI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: pypi-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: -4.6
  facets:
    commercial_clarity: 63.2
    contract_quality: 60.2
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pypi/refs/heads/main/screenshots/pypi-2026-06-20T192329.png
security:
- kind: authentication
  name: Pypi Authentication
  slug: pypi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pypi Domain Security
  slug: pypi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pypi Vulnerability Disclosure
  slug: pypi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pypi
tags:
- Developer Tools
- Open Source
- Package Management
- Packages
- Python
website: https://pypi.org/
---
