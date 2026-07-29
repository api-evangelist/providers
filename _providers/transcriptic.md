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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: JSON:API-compliant REST API for the Transcriptic / Strateos robotic cloud lab — organizations, projects, runs, datasets, containers and aliquots, plus Autoprotocol experiment submission. Authenticates
  name: Transcriptic / Strateos REST API
  slug: transcriptic-strateos-rest-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://transcriptic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.strateos.com
- group: docs
  title: ''
  type: Documentation
  url: https://transcriptic.readthedocs.io/en/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.strateos.com/docs/getting-started-with-the-cli
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
  url: packages/transcriptic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/transcriptic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/transcriptic-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/transcriptic-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/transcriptic-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/transcriptic-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transcriptic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transcriptic-llms.txt
created: '2026-07-17'
description: 'Transcriptic is a robotic cloud laboratory for the life sciences, now operating as Strateos following a merger with 3Scan. It lets researchers design, submit and run wet-lab biology experiments remotely on automated robotic infrastructure: experiments are specified in Autoprotocol (an open JSON standard) and submitted to a JSON:API-compliant REST API at https://secure.strateos.com, where organizations, projects, runs, datasets, containers and aliquots are managed programmatically and the resulting datasets are fetched back for analysis. Transcriptic publishes an official Python client library and command-line interface (TxPy, `pip install transcriptic`), with Jupyter-notebook integration, and was backed by GV.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transcriptic.png
layout: provider
modified: '2026-07-21'
name: Transcriptic
nav: Providers
network: true
overview: 'Transcriptic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Laboratory Automation, Cloud Lab, and Drug Discovery.


  Transcriptic''s developer surface includes documentation, getting-started guide, CLI, authentication, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 22.6
  delta: -2.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 25.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Transcriptic Authentication
  slug: transcriptic-authentication
  summary_line: apiKey/http/custom-signature · 4 schemes
- kind: domain-security
  name: Transcriptic Domain Security
  slug: transcriptic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transcriptic
tags:
- Company
- Life Sciences
- Laboratory Automation
- Cloud Lab
- Drug Discovery
- Biotechnology
- REST API
- JSON:API
- Autoprotocol
website: http://transcriptic.com
---
