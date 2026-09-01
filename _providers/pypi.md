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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pypi Agentic Access
  operation_count: 11
  slug: pypi-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 3
apis:
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
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PyPI Index Downloads API
  slug: open-pypi-downloads-api
- collection_type: open
  name: PyPI Downloads Index API
  slug: open-pypi-index-api
- collection_type: open
  name: PyPI Integrity API
  slug: open-pypi-integrity-api
- collection_type: open
  name: PyPI JSON API
  slug: open-pypi-json-api
- collection_type: open
  name: PyPI Index Downloads Projects API
  slug: open-pypi-projects-api
- collection_type: open
  name: PyPI Index Downloads Provenance API
  slug: open-pypi-provenance-api
- collection_type: open
  name: PyPI Stats API
  slug: open-pypi-stats-api
- collection_type: open
  name: PyPI Index Downloads Upload API
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
overview: 'PyPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Downloads API, Projects API, and Provenance API. Tagged areas include Developer Tools, Open-Source, Package Management, Packages, and Python.


  The PyPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PyPI''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 8 more developer resources.'
plans:
- name: Pypi Plans Pricing
  plan_count: 1
  slug: pypi-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Pypi Rate Limits
  slug: pypi-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: PyPI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: pypi-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 64.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 9.8
    contract_quality: 56.5
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Open-Source
- Package Management
- Packages
- Python
website: https://pypi.org/
---
