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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: The fetch API from Zipline Ai — 4 operation(s) for fetch.
  name: Zipline Ai fetch API
  slug: zipline-ai-fetch-api
- description: The health API from Zipline Ai — 2 operation(s) for health.
  name: Zipline Ai health API
  slug: zipline-ai-health-api
- description: The schema API from Zipline Ai — 5 operation(s) for schema.
  name: Zipline Ai schema API
  slug: zipline-ai-schema-api
- description: The workflow API from Zipline Ai — 1 operation(s) for workflow.
  name: Zipline Ai workflow API
  slug: zipline-ai-workflow-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zipline-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zipline-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zipline.ai/
created: '2026-07-17'
description: Zipline Ai is a company surfaced as a portfolio company of wing-venture-capital and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zipline-ai.png
layout: provider
modified: '2026-07-17'
name: Zipline Ai
nav: Providers
network: true
overview: 'Zipline Ai publishes 4 APIs on the [APIs.io](https://apis.io/) network, including fetch API, health API, schema API, and 1 more. Tagged areas include Company.


  Zipline Ai''s developer surface includes authentication and 2 more developer resources.'
random_paper: 106
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.8
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Zipline Ai Authentication
  slug: zipline-ai-authentication
  summary_line: http/oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Zipline Ai Domain Security
  slug: zipline-ai-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Zipline Ai Trust Center
  slug: zipline-ai-trust-center
  summary_line: trust center published
slug: zipline-ai
tags:
- Company
website: https://zipline.ai/
---
