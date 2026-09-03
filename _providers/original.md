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
  scored_at: '2026-09-02'
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
- description: No official hosted or remote MCP server was found for Bodygram. This is a candidate tool list derived from the two documented Platform API operations.
  name: Bodygram MCP Server
  slug: bodygram-mcp-server
modified: '2026-07-20'
name: Bodygram
nav: Providers
network: true
overview: 'Bodygram publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Body Measurement, Computer-Vision, Artificial Intelligence, and Sizing.


  Bodygram''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, and 9 more developer resources.'
random_paper: 13
scopes:
- name: Original Scopes
  scope_count: 0
  slug: original-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/original/refs/heads/main/screenshots/original-2026-08-07T190948.png
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
- Computer-Vision
- Artificial Intelligence
- Sizing
- Retail
- 3D Avatar
- Health
- SDK
website: https://bodygram.com
---
