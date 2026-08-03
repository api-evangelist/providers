---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Labstep REST API exposes the same generic entity surface the Labstep application uses — experiments, protocols, resources, resource items, locations, devices, device data, orders, metadata, files,
  name: Labstep API
  slug: labstep-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.labstep.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.labstep.com/en/collections/1913112-labstep-api
- group: docs
  title: ''
  type: Documentation
  url: https://labsteppy.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://labsteppy.readthedocs.io/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.labstep.com/en/articles/1786226-getting-started-with-the-labstep-api
- group: operate
  title: ''
  type: Support
  url: https://help.labstep.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.labstep.com
- group: company
  title: ''
  type: Blog
  url: https://www.labstep.com/blogs/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Labstep
- group: commercial
  title: ''
  type: Pricing
  url: https://www.labstep.com/industry-pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.labstep.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.labstep.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.labstep.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.labstep.com/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.labstep.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.labstep.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.labstep.com/en/collections/945011-release-notes
- group: build
  title: ''
  type: Packages
  url: packages/labstep-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/labstep-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/labstep-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/labstep-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/labstep-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/labstep-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/labstep-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/labstep-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/labstep-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/labstep-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/labstep-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/labstep-domain-security.yml
created: '2026-07-17'
description: Labstep is a cloud-based Electronic Lab Notebook (ELN) and research data management platform for life-science, chemistry and pharma R&D teams. It combines step-by-step interactive protocols, structured experiment data capture, inventory and sample management with QR scanning, order management, instrument/device integration, chemistry and sequence tooling, and integrated Jupyter Notebooks for analysis — all under an audit trail with electronic signatures and sample lineage. Labstep exposes a public REST API at api.labstep.com secured with a per-user API key, plus an officially maintained Python SDK (labstepPy) and an R package (labstepR) that wrap the same generic entity surface used by the application itself.
image: https://www.labstep.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Labstep
nav: Providers
network: true
overview: 'Labstep publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronic Lab Notebook, Life Sciences, Laboratory, and Research Data Management.


  Labstep''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 82
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 36.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/labstep/refs/heads/main/screenshots/labstep-2026-07-25T224425.png
security:
- kind: authentication
  name: Labstep Authentication
  slug: labstep-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Labstep Domain Security
  slug: labstep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: labstep
tags:
- Company
- Electronic Lab Notebook
- Life Sciences
- Laboratory
- Research Data Management
- Scientific Software
- Inventory Management
- Biotechnology
- Chemistry
- Compliance
website: https://www.labstep.com
---
