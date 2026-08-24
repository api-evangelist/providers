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
  score: 0.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'OAuth 2.0 protected REST API for the AstroPrint cloud 3D printing platform. Manage printers, designs, and print jobs. Confirmed live: https://api.astroprint.com/v2/printers returns HTTP 401 without a '
  name: AstroPrint Cloud API
  slug: astroprint-cloud-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3dagogo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.astroprint.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.astroprint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://astroprint.github.io/3d-print-api-sample/
- group: docs
  title: ''
  type: APIReference
  url: https://astroprint.github.io/3d-print-api-sample/
- group: company
  title: ''
  type: Blog
  url: https://blog.astroprint.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/astroprint
- group: operate
  title: ''
  type: Support
  url: https://astroprint.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: Forum
  url: https://forum.astroprint.com/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.astroprint.com/account/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.astroprint.com/plans-and-pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://astroprint.statuspage.io
- group: build
  title: ''
  type: Packages
  url: packages/3dagogo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/3dagogo-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3dagogo-llms.txt
created: '2026-07-17'
description: 3DaGoGo, Inc. is a San Diego based technology company and the maker of AstroPrint, a cloud platform for consumer and professional 3D printing. AstroPrint provides browser-based cloud slicing, AI-powered model generation from text prompts, remote WiFi printer control, live video print monitoring, print-queue management, multi-user access controls, and analytics, serving more than 260,000 users across 130+ countries with over 5 million objects printed. AstroPrint exposes an OAuth 2.0 protected REST API (api.astroprint.com/v2) plus a client-side 3D Print API so third parties can build applications on top of the platform. 3DaGoGo was surfaced as a portfolio company of 500 Global and has been enriched from its public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/3dagogo.png
layout: provider
modified: '2026-07-17'
name: 3DaGoGo
nav: Providers
network: true
overview: '3DaGoGo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Cloud, Manufacturing, and IoT.


  3DaGoGo''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, and 9 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 25.0
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/3dagogo/refs/heads/main/screenshots/3dagogo-2026-07-25T181146.png
security:
- kind: authentication
  name: 3Dagogo Authentication
  slug: 3dagogo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: 3Dagogo Domain Security
  slug: 3dagogo-domain-security
  summary_line: DMARC
slug: 3dagogo
tags:
- Company
- 3D Printing
- Cloud
- Manufacturing
- IoT
- Developer API
- Authentication
website: https://www.astroprint.com
---
