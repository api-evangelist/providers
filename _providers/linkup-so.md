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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Linkup So Agentic Access
  operation_count: 5
  slug: linkup-so-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: The Credits API from Linkup — 1 operation(s) for credits.
  name: Linkup Credits API
  slug: linkup-so-credits-api
- description: The Fetch API from Linkup — 1 operation(s) for fetch.
  name: Linkup Fetch API
  slug: linkup-so-fetch-api
- description: The Research API from Linkup — 2 operation(s) for research.
  name: Linkup Research API
  slug: linkup-so-research-api
- description: The Search API from Linkup — 1 operation(s) for search.
  name: Linkup Search API
  slug: linkup-so-search-api
artifact_total: 12
collections:
- collection_type: open
  name: Linkup API
  slug: open-linkup-so
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linkup-so-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/linkup-so-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linkup-so-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linkup-so-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LinkupPlatform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linkup-platform
- group: company
  title: ''
  type: Website
  url: https://www.linkup.so
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linkup.so
- group: commercial
  title: ''
  type: Plans
  url: plans/linkup-so-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linkup-so-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.linkup.so/blog
- group: commercial
  title: ''
  type: FinOps
  url: finops/linkup-so-finops.yml
created: '2026-06-20'
description: Linkup is a production-grade web search and answer API for AI agents and LLMs. Its /search endpoint grounds model responses in real-time web context, returning ranked results, sourced answers with citations, or structured output, plus /fetch for clean LLM-ready markdown, an async /research endpoint, and a credits balance endpoint - all authenticated with a Bearer API key.
finops:
- name: Linkup So Finops
  service_category: AI and Machine Learning
  slug: linkup-so-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linkup-so.png
layout: provider
modified: '2026-06-20'
name: Linkup
nav: Providers
network: true
overview: 'Linkup publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Credits API, Fetch API, Research API, and 1 more. Tagged areas include AI, LLM, Web Search, Grounding, and RAG.


  Linkup''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Linkup So Plans Pricing
  plan_count: 3
  slug: linkup-so-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 3
  name: Linkup So Rate Limits
  slug: linkup-so-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -2.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 57.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linkup-so/refs/heads/main/screenshots/linkup-so-2026-06-20T184547.png
security:
- kind: authentication
  name: Linkup So Authentication
  slug: linkup-so-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Linkup So Domain Security
  slug: linkup-so-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Linkup So Trust Center
  slug: linkup-so-trust-center
  summary_line: SOC 2
slug: linkup-so
tags:
- AI
- LLM
- Web Search
- Grounding
- RAG
website: https://www.linkup.so
---
