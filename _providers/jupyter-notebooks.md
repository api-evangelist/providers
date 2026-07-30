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
- acting_count: 16
  human_in_the_loop: 2
  name: Jupyter Notebooks Agentic Access
  operation_count: 25
  slug: jupyter-notebooks-agentic-access
  summary_line: 25 operations · 16 acting · 2 human-in-the-loop
api_count: 5
apis:
- description: Notebook and file contents.
  name: Jupyter Notebooks Contents API
  slug: jupyter-notebooks-contents-api
- description: Running kernels.
  name: Jupyter Notebooks Kernels API
  slug: jupyter-notebooks-kernels-api
- description: Available kernel specs.
  name: Jupyter Notebooks KernelSpecs API
  slug: jupyter-notebooks-kernelspecs-api
- description: Notebook sessions.
  name: Jupyter Notebooks Sessions API
  slug: jupyter-notebooks-sessions-api
- description: Terminal sessions.
  name: Jupyter Notebooks Terminals API
  slug: jupyter-notebooks-terminals-api
artifact_total: 16
collections:
- collection_type: open
  name: Jupyter Notebook Server REST API
  slug: open-jupyter-notebooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyter-notebooks-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyter-notebooks-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyter-notebooks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyter-notebooks-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/project-jupyter
- group: company
  title: ''
  type: Website
  url: https://jupyter.org
- group: docs
  title: ''
  type: Documentation
  url: https://jupyter-notebook.readthedocs.io/en/stable/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyter
- group: operate
  title: ''
  type: Community
  url: https://discourse.jupyter.org/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jupyter-notebooks-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/feed
created: '2024-01-15'
description: Jupyter Notebooks is the original web application for creating and sharing computational documents. APIs cover the notebook server, kernels, sessions, contents, and terminal management.
finops:
- name: Jupyter Notebooks Finops
  service_category: API
  slug: jupyter-notebooks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyter-notebooks.png
json_schemas:
- name: Jupyter Notebook (nbformat 4)
  property_count: 4
  slug: jupyter-notebook-format
jsonld:
- class_count: 13
  name: Jupyter Notebooks Context
  property_count: 0
  slug: jupyter-notebooks-context
layout: provider
modified: '2026-05-19'
name: Jupyter Notebooks
nav: Providers
network: true
overview: 'Jupyter Notebooks publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contents API, Kernels API, KernelSpecs API, and 2 more. Tagged areas include Data Science, Interactive Computing, Jupyter, Notebooks, and Python.


  The Jupyter Notebooks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Jupyter Notebooks'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Jupyter Notebooks Plans Pricing
  plan_count: 3
  slug: jupyter-notebooks-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Jupyter Notebooks Rate Limits
  slug: jupyter-notebooks-rate-limits
rules:
- name: Jupyter Notebooks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyter-notebooks-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.0
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 26.1
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyter-notebooks/refs/heads/main/screenshots/jupyter-notebooks-2026-06-20T183840.png
security:
- kind: authentication
  name: Jupyter Notebooks Authentication
  slug: jupyter-notebooks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jupyter Notebooks Domain Security
  slug: jupyter-notebooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyter Notebooks Vulnerability Disclosure
  slug: jupyter-notebooks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyter-notebooks
tags:
- Data Science
- Interactive Computing
- Jupyter
- Notebooks
- Python
website: https://jupyter.org
---
