---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fashn Agentic Access
  operation_count: 2
  slug: fashn-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Predictions API from FASHN AI — 2 operation(s) for predictions.
  name: FASHN AI Predictions API
  slug: fashn-predictions-api
artifact_total: 8
collections:
- collection_type: open
  name: FASHN AI API
  slug: open-fashn
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fashn-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fashn-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fashn-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fashn-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fashn
- group: company
  title: ''
  type: Website
  url: https://fashn.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://fashn.ai/products/api
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.fashn.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.fashn.ai/api
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.fashn.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://fashn.ai/blog
created: '2025-03-01'
description: FASHN AI is an AI-first company specializing in human-centric generative image models tailored for fashion applications. The public API offers an asynchronous prediction workflow against a catalog of models including Try-On Max, Product to Model, Face to Model, Model Create, Model Swap, Edit, Reframe, Image to Video, and Background Remove.
finops:
- name: Fashn Finops
  service_category: API
  slug: fashn-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fashn.png
layout: provider
modified: '2026-05-19'
name: FASHN AI
nav: Providers
network: true
overview: 'FASHN AI publishes 1 API on the [APIs.io](https://apis.io/) network: Predictions API. Tagged areas include AI, Clothing, Fashion, and Virtual Try-On.


  FASHN AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Fashn Plans Pricing
  plan_count: 3
  slug: fashn-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 5
  name: Fashn Rate Limits
  slug: fashn-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 62.7
    developer_ergonomics: 37.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fashn/refs/heads/main/screenshots/fashn-2026-06-20T181047.png
security:
- kind: authentication
  name: Fashn Authentication
  slug: fashn-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fashn Domain Security
  slug: fashn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fashn
tags:
- AI
- Clothing
- Fashion
- Virtual Try-On
website: https://fashn.ai/
---
