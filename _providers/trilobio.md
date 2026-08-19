---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.3
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Python interfaces for the core T-code components that drive a Trilobot fleet — Commands, Labware, Locations, Scripts — plus the T-code Servicer client for runtime control and the Integrator client for
  name: TCode API (tcode-api)
  slug: tcode-api-tcode-api
artifact_total: 3
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/trilobio/tcode-api/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.trilo.bio/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://tcode.trilo.bio/
- group: docs
  title: ''
  type: Documentation
  url: http://tcode.trilo.bio/
- group: start
  title: ''
  type: GettingStarted
  url: http://tcode.trilo.bio/getting_started/index.html
- group: docs
  title: ''
  type: APIReference
  url: http://tcode.trilo.bio/api/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trilobio
- group: company
  title: ''
  type: Blog
  url: https://www.trilo.bio/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.trilo.bio/book-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trilo.bio/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trilo.bio/terms
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trilobio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trilobio-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Trilobio builds whole-lab automation for genetic engineering, synthetic biology, and life-science research — affordable robotics "built by biologists, for biologists." The platform pairs the Trilobot (a self-calibrating, tool-changing lab robot with 16 deck slots), interchangeable gripper/pipette tools, and Trilobio OS (no-code, GUI-driven protocol design with automatic sample layout, error checking, an automated lab notebook, and LIMS). For developers, Trilobio exposes T-code — the command language of Trilobots — through the open-source Python `tcode-api` package, which drives a Trilobot fleet via a local T-code Servicer and integrates third-party lab devices. Founded in 2021 in San Francisco by Roya Amini-Naieni and Maximilian Schommer; backed by Initialized Capital, Argon Ventures, and Lowercarbon Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trilobio.png
layout: provider
modified: '2026-07-21'
name: Trilobio
nav: Providers
network: true
overview: 'Trilobio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Lab Automation, Biotech, and Life Sciences.


  Trilobio''s developer surface includes documentation, getting-started guide, API reference, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 123
score:
  band: emerging
  composite: 24.1
  delta: 1.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.9
  provenance:
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Trilobio Authentication
  slug: trilobio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Trilobio Domain Security
  slug: trilobio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trilobio
tags:
- Company
- Frontier Tech
- Lab Automation
- Biotech
- Life Sciences
- Robotics
- Synthetic Biology
- Developer API
- Python SDK
website: https://www.trilo.bio/
---
