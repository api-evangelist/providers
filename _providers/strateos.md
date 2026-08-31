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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Strateos / Transcriptic web API is a JSON:API-based interface for managing organizations, projects, runs, datasets, inventory, protocols, and packages on the robotic cloud lab. It is consumed thro
  name: Strateos Web API
  slug: strateos-web-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strateos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://strateos.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.strateos.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://developers.strateos.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://developers.strateos.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.strateos.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strateos
- group: start
  title: ''
  type: Login
  url: https://secure.strateos.com
- group: build
  title: ''
  type: Packages
  url: packages/strateos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strateos-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/strateos-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strateos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strateos-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strateos-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strateos-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strateos-llms.txt
created: '2026-07-17'
description: Strateos operates a robotic cloud laboratory for the life sciences, delivering Cloud Lab Automation-as-a-Service so scientists can design, run, and analyze wet-lab experiments remotely and programmatically. Originally founded as Transcriptic, Strateos couples high-throughput robotic lab automation with the Autoprotocol standard and a JSON:API-based web API, letting researchers submit protocols, launch runs, manage projects, inventory, and datasets, and pull results into downstream ML and data-engineering pipelines. It is backed by DCVC and Lux Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/strateos.png
layout: provider
modified: '2026-07-21'
name: Strateos
nav: Providers
network: true
overview: 'Strateos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Laboratory Automation, Robotics, and Cloud Lab.


  Strateos'' developer surface includes documentation, API reference, getting-started guide, CLI, authentication, and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Strateos Authentication
  slug: strateos-authentication
  summary_line: apiKey/httpSignature/http · 3 schemes
- kind: domain-security
  name: Strateos Domain Security
  slug: strateos-domain-security
  summary_line: DMARC
slug: strateos
tags:
- Company
- Life Sciences
- Laboratory Automation
- Robotics
- Cloud Lab
- Drug Discovery
- Biotechnology
- Autoprotocol
- JSON:API
- Research
website: https://strateos.com
---
