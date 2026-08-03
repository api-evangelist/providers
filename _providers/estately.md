---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estately-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.estately.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/estately
- group: build
  title: ''
  type: Packages
  url: packages/estately-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/estately-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/estately-llms.txt
created: '2026-07-17'
description: Estately is a Seattle-based, MLS-based residential real estate search platform for browsing homes for sale, recently sold homes, home values, and neighborhood information, and for connecting buyers and sellers with agents. Estately does not publish a public developer API or developer portal; its notable developer-facing surface is the open-source `rets` Ruby library it maintains for fetching data from RETS (Real Estate Transaction Standard) servers, distributed on RubyGems with a bundled command-line client. This profile was surfaced from VC-portfolio signals (500 Global, Uncork Capital) and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/estately.png
layout: provider
modified: '2026-07-19'
name: Estately
nav: Providers
network: true
overview: Estately is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Homes for Sale, MLS, and Property Search.
random_paper: 20
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 7.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Estately Domain Security
  slug: estately-domain-security
  summary_line: TLSv1.2 · DMARC
slug: estately
tags:
- Company
- Real Estate
- Homes for Sale
- MLS
- Property Search
- RETS
- Open Source
website: https://www.estately.com
---
