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
- acting_count: 3
  human_in_the_loop: 0
  name: Jupyterlab Agentic Access
  operation_count: 12
  slug: jupyterlab-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 7
apis:
- description: JavaScript and TypeScript API used to build JupyterLab extensions and plugins. JupyterLab is composed of plugins that consume and provide services on the front-end application object.
  name: JupyterLab Extension API
  slug: jupyterlab-extension-api
- description: Third-party license reports for installed extensions.
  name: JupyterLab Licenses API
  slug: jupyterlab-licenses-api
- description: Extension manager listing data (allowed and blocked extensions).
  name: JupyterLab Listings API
  slug: jupyterlab-listings-api
- description: User-defined settings for JupyterLab plugins.
  name: JupyterLab Settings API
  slug: jupyterlab-settings-api
- description: Static theme files served to the browser.
  name: JupyterLab Themes API
  slug: jupyterlab-themes-api
- description: Locale translation bundles.
  name: JupyterLab Translations API
  slug: jupyterlab-translations-api
- description: JupyterLab user workspaces.
  name: JupyterLab Workspaces API
  slug: jupyterlab-workspaces-api
artifact_total: 19
collections:
- collection_type: open
  name: JupyterLab Server REST API
  slug: open-jupyterlab-server-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jupyterlab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jupyterlab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jupyterlab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jupyterlab-authentication.yml
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
  url: https://jupyterlab.readthedocs.io/en/stable/
- group: start
  title: ''
  type: GettingStarted
  url: https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html
- group: other
  title: ''
  type: Installation
  url: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
- group: docs
  title: ''
  type: UserGuide
  url: https://jupyterlab.readthedocs.io/en/stable/user/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jupyterlab
- group: other
  title: ''
  type: Repository
  url: https://github.com/jupyterlab/jupyterlab
- group: company
  title: ''
  type: Blog
  url: https://blog.jupyter.org/
- group: operate
  title: ''
  type: Community
  url: https://jupyter.org/community
- group: build
  title: ''
  type: CodeOfConduct
  url: https://jupyter.org/governance/conduct/code_of_conduct.html
created: '2024-01-01'
description: JupyterLab is the next-generation web-based interactive development environment for notebooks, code, and data. It is served by Jupyter Server and ships with JupyterLab Server, which provides REST APIs for user-defined settings, workspaces, themes, translations, and license reports, alongside the JavaScript and TypeScript extension API used to build JupyterLab plugins.
finops:
- name: Jupyterlab Finops
  service_category: API
  slug: jupyterlab-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jupyterlab.png
json_schemas:
- name: JupyterLab Plugin Setting
  property_count: 7
  slug: jupyterlab-setting
- name: JupyterLab Workspace
  property_count: 2
  slug: jupyterlab-workspace
jsonld:
- class_count: 6
  name: Jupyterlab Context
  property_count: 0
  slug: jupyterlab-context
layout: provider
modified: '2026-05-19'
name: JupyterLab
nav: Providers
network: true
overview: 'JupyterLab publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Licenses API, Listings API, Settings API, and 3 more. Tagged areas include Data Science, Extensions, IDE, Interactive Computing, and Notebooks.


  The JupyterLab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JupyterLab''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Jupyterlab Plans Pricing
  plan_count: 3
  slug: jupyterlab-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Jupyterlab Rate Limits
  slug: jupyterlab-rate-limits
rules:
- name: JupyterLab API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: jupyterlab-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: -4.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.9
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jupyterlab/refs/heads/main/screenshots/jupyterlab-2026-06-20T183842.png
security:
- kind: authentication
  name: Jupyterlab Authentication
  slug: jupyterlab-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Jupyterlab Domain Security
  slug: jupyterlab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jupyterlab Vulnerability Disclosure
  slug: jupyterlab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jupyterlab
tags:
- Data Science
- Extensions
- IDE
- Interactive Computing
- Notebooks
- Python
website: https://jupyter.org
---
