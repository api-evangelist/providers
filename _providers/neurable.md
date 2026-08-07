---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: 'Handles the full lifecycle of EEG analytics for Neurable customers and internal applications: a chunked recording upload flow (start session, PUT chunks up to 10MB, finalize), recording download by pr'
  name: Neurable Analytics Service
  slug: neurable-analytics-service
- description: Real-time data processing service for analyzing EEG sensor data from Neurable hardware, which doubles as the Neurable identity provider. It is a standards-conformant OpenID Connect authorization serve
  name: Neurable Pipe Service
  slug: neurable-pipe-service
- description: 'Brain Health Service manages calculating user statistics related to Brain Health so that different reports can be flexibly and quickly generated. The service publishes an OpenAPI 3.1.0 description at '
  name: Neurable Brain Health Service
  slug: neurable-brain-health-service
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neurable-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.neurable.com/
- group: company
  title: ''
  type: About
  url: https://www.neurable.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.neurable.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.neurable.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.neurable.com/faqs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/neurable
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.neurable.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.neurable.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/neurable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/neurable-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/neurable-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/neurable-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/neurable-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/neurable-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/neurable-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/neurable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/neurable-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Neurable is a Boston, Massachusetts neurotechnology company, founded in 2015 on University of Michigan EEG signal-processing research, that builds non-invasive brain-computer interface (BCI) hardware and the AI models that interpret the signal. Its consumer product is the MW75 Neuro — Master & Dynamic over-ear headphones with dry conductive-fabric EEG electrodes that measure focus, fatigue and cognitive load — and it also ships an MW75 Neuro Research Kit (12-channel, 500 Hz raw EEG plus accelerometer/gyroscope, exported for LSL and BrainVision toolchains) and a partner Development Kit for hardware and software OEMs embedding Neurable sensing into their own devices. Neurable publishes no public developer portal or API reference, but its production backend services expose FastAPI-generated OpenAPI 3.1.0 descriptions at their host roots: an Analytics Service handling the EEG recording lifecycle and headset feature licensing, a real-time data processing pipe service that is also
  a full OpenID Connect authorization server, and a Brain Health Service.'
image: https://cdn.prod.website-files.com/65773cb2354a620eb230d1e4/657b30529e7a3d9845248e54_Neurable-December-Opengraph%20(2).jpg
layout: provider
modified: '2026-08-04'
name: Neurable
nav: Providers
network: true
overview: 'Neurable publishes 3 APIs on the [APIs.io](https://apis.io/) network: Analytics Service, Pipe Service, and Brain Health Service. Tagged areas include neurotechnology, brain-computer-interface, eeg, neuroscience, and wearables.


  Neurable''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
random_paper: 55
scopes:
- name: Neurable Scopes
  scope_count: 5
  slug: neurable-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 30.9
  delta: -1.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 41.9
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 31.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Neurable Authentication
  slug: neurable-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Neurable Domain Security
  slug: neurable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: neurable
tags:
- neurotechnology
- brain-computer-interface
- eeg
- neuroscience
- wearables
- biosignals
- hardware
- consumer-electronics
- research-tools
- cognitive-analytics
- health-data
- oauth
- openid-connect
website: https://www.neurable.com/
---
