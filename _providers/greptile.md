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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Greptile Agentic Access
  operation_count: 4
  slug: greptile-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 4
apis:
- description: AI code-review product delivered as a GitHub App (also GitLab / Bitbucket). Installed on repositories, it reviews pull requests against full-codebase context, flagging bugs and anti-patterns. Billed p
  name: Greptile Code Review (GitHub App)
  slug: greptile-code-review-github-app
- description: Ask natural-language questions over indexed repositories.
  name: Greptile Query API
  slug: greptile-query-api
- description: Submit repositories for indexing and check indexing status.
  name: Greptile Repositories API
  slug: greptile-repositories-api
- description: Retrieve relevant code locations without a synthesized answer.
  name: Greptile Search API
  slug: greptile-search-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of Greptile's **query streaming** surface. Greptile does not publish a WebSocket API. The only asynchronous / event-style transport documented at https://docs.greptile.com/qui
  name: Greptile Query Streaming (HTTP + SSE)
  slug: greptile-asyncapi
collections:
- collection_type: open
  name: Greptile API
  slug: open-greptile
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/greptile-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/greptile-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/greptile-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greptile-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/greptile-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/greptileai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greptile
- group: company
  title: ''
  type: Website
  url: https://www.greptile.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.greptile.com
- group: commercial
  title: ''
  type: Plans
  url: plans/greptile-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/greptile-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/greptile-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.greptile.com/blog
created: '2026-06-20'
description: Greptile builds an AI layer that understands entire codebases. Its public REST API indexes Git repositories into a graph plus embeddings, then answers natural-language questions and searches over that code. Greptile also ships an AI code-review product delivered as a GitHub App that reviews pull requests for bugs and anti-patterns.
finops:
- name: Greptile Finops
  service_category: AI and Machine Learning
  slug: greptile-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greptile.png
layout: provider
modified: '2026-06-20'
name: Greptile
nav: Providers
network: true
overview: 'Greptile publishes 3 APIs on the [APIs.io](https://apis.io/) network: Query API, Repositories API, and Search API. Tagged areas include AI, Codebase Understanding, Code Review, Code Search, and Developer Tools.


  The Greptile catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Greptile''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Greptile Plans Pricing
  plan_count: 4
  slug: greptile-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 4
  name: Greptile Rate Limits
  slug: greptile-rate-limits
rules:
- name: Greptile API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: greptile-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.2
  delta: -3.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greptile/refs/heads/main/screenshots/greptile-2026-06-20T182408.png
security:
- kind: authentication
  name: Greptile Authentication
  slug: greptile-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Greptile Domain Security
  slug: greptile-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Greptile Vulnerability Disclosure
  slug: greptile-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Greptile Trust Center
  slug: greptile-trust-center
  summary_line: SOC 2
slug: greptile
tags:
- AI
- Codebase Understanding
- Code Review
- Code Search
- Developer Tools
website: https://www.greptile.com
---
