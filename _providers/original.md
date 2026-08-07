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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API to generate accurate body measurements and a 3D avatar from a person's stats, and (with two photos) body composition and posture data. Requests use a secret API key in the Authorization heade
  name: Bodygram Platform API
  slug: bodygram-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://bodygram.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.bodygram.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bodygram.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bodygram.com/platform/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bodygram.com/platform
- group: start
  title: ''
  type: SignUp
  url: https://www.platform.bodygram.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://platform.bodygram.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bodygram
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bodygram.com/en/policies
- group: operate
  title: ''
  type: Support
  url: https://bodygram.com/en/contact-form
- group: build
  title: ''
  type: Packages
  url: packages/original-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/original-packages.yml
- group: design
  title: ''
  type: Components
  url: components/original-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/original-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/original-domain-security.yml
created: '2026-07-17'
description: Bodygram is an AI-powered body measurement company whose technology extracts 35+ body measurements, body composition, posture data, and a 3D avatar from a smartphone photo or a person's basic stats. The Bodygram Platform API and the Body2Fit and Headless JavaScript SDKs let retail, fashion, uniform, health, and wellness businesses embed accurate sizing and body scanning into their own apps and websites to increase conversion and reduce returns. Surfaced as a 500 Global portfolio company and enriched from Bodygram's public developer surface (docs.bodygram.com).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/original.png
layout: provider
mcp_servers:
- description: ''
  name: original-mcp.yml
  slug: original-mcpyml
modified: '2026-07-20'
name: Bodygram
nav: Providers
network: true
overview: 'Bodygram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Body Measurement, Computer Vision, Artificial Intelligence, and Sizing.


  Bodygram''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, and 9 more developer resources.'
random_paper: 62
scopes:
- name: Original Scopes
  scope_count: 0
  slug: original-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 26.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 26.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Original Authentication
  slug: original-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Original Domain Security
  slug: original-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: original
tags:
- Company
- Body Measurement
- Computer Vision
- Artificial Intelligence
- Sizing
- Retail
- 3D Avatar
- Health
- SDK
website: https://bodygram.com
---
