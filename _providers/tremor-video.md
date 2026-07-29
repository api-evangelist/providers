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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for the Nexxen DSP (formerly Amobee / Tremor Video DSP) to manage programmatic advertising objects — advertisers, insertion orders, line items, packages and creatives. OAuth2 client-credentia
  name: Nexxen DSP API
  slug: nexxen-dsp-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tremor-video-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nexxen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/nexxen-api/nexxen/documentation/9md8q3a/nexxen-dsp-apis
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/nexxen-api/nexxen/collection/9md8q3a/nexxen-dsp-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://www.postman.com/nexxen-api/nexxen/collection/9md8q3a/nexxen-dsp-apis
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/nexxen-api/nexxen/
- group: start
  title: ''
  type: Login
  url: https://login.amobee.com/portal/amobee/dsp/login
- group: auth
  title: ''
  type: Authentication
  url: authentication/tremor-video-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tremor-video-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tremor-video-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tremor-video-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tremor-video-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/tremor-video-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tremor-video-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tremor-video-lifecycle.yml
created: '2026-07-17'
description: Tremor Video DSP is the demand-side platform originally built by Tremor Video and Tremor International; following the consolidation of Tremor Video DSP and Amobee it is now marketed as the Nexxen DSP, part of the unified Nexxen advertising stack (DSP, SSP, Ad Server and Data Platform). It offers a REST API for programmatic and connected-TV (CTV) advertising operations, letting partners manage advertisers, insertion orders, line items, packages and creatives. The Nexxen DSP API authenticates with OAuth2 client-credentials (client ID and client secret) and is documented publicly through a Nexxen Postman workspace.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tremor-video.png
layout: provider
mcp_servers:
- description: ''
  name: tremor-video-mcp.yml
  slug: tremor-video-mcpyml
modified: '2026-07-21'
name: Tremor Video
nav: Providers
network: true
overview: 'Tremor Video publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Martech, Advertising, AdTech, and DSP.


  Tremor Video''s developer surface includes documentation, API reference, getting-started guide, authentication, and 11 more developer resources.'
random_paper: 45
score:
  band: emerging
  composite: 20.4
  delta: -1.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tremor Video Authentication
  slug: tremor-video-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tremor Video Domain Security
  slug: tremor-video-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tremor-video
tags:
- Company
- Martech
- Advertising
- AdTech
- DSP
- Programmatic
- CTV
- Video Advertising
website: https://nexxen.com/
---
