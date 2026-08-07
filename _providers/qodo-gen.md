---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Qodo Gen Agentic Access
  operation_count: 8
  slug: qodo-gen-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 3
apis:
- description: Terminal agent runner; serve agents as HTTP APIs or MCP services.
  name: Qodo Qodo Command API
  slug: qodo-gen-qodo-command-api
- description: AI coding assistant IDE plugin - generation, chat, and test generation.
  name: Qodo Qodo Gen API
  slug: qodo-gen-qodo-gen-api
- description: Agentic pull request review Git app (built on open-source PR-Agent).
  name: Qodo Qodo Merge API
  slug: qodo-gen-qodo-merge-api
artifact_total: 10
collections:
- collection_type: open
  name: Qodo Platform (Modeled Capability Surfaces)
  slug: open-qodo-gen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qodo-gen-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qodo-gen-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qodo-gen-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qodo-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qodoai
- group: company
  title: ''
  type: Website
  url: https://www.qodo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qodo.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/qodo-gen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qodo-gen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qodo-gen-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.qodo.ai/blog/
created: '2026-07-11'
description: Qodo (formerly CodiumAI) is an AI code quality and integrity platform for the whole software development lifecycle. Its products include Qodo Gen (an AI coding assistant IDE plugin for code generation, chat, and test generation), Qodo Merge (an agentic pull request review app for GitHub, GitLab, Bitbucket, and Azure DevOps, built on the open-source PR-Agent project), Qodo Command / Qodo Gen CLI (a terminal agent runner installed via npm that can serve agents as HTTP APIs or MCP services), Qodo Cover (test coverage automation), and Qodo Aware (codebase context). Qodo's public surfaces are primarily an IDE plugin, a Git application driven by webhooks and PR comment commands, and a CLI - the hosted platform REST surface is gated. The open-source PR-Agent engine (MIT) that powers Qodo Merge is self-hostable as a CLI, GitHub Action, or webhook server.
finops:
- name: Qodo Gen Finops
  service_category: AI and Developer Tools
  slug: qodo-gen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qodo-gen.png
layout: provider
modified: '2026-07-11'
name: Qodo
nav: Providers
network: true
overview: 'Qodo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Qodo Command API, Qodo Gen API, and Qodo Merge API. Tagged areas include AI Coding Assistant, Code Review, Test Generation, Developer Tools, and LLM.


  Qodo''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Qodo Gen Plans Pricing
  plan_count: 4
  slug: qodo-gen-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Qodo Gen Rate Limits
  slug: qodo-gen-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Qodo Gen Authentication
  slug: qodo-gen-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Qodo Gen Domain Security
  slug: qodo-gen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qodo-gen
tags:
- AI Coding Assistant
- Code Review
- Test Generation
- Developer Tools
- LLM
- AI
- Pull Request Review
- Code Quality
- Agents
- Open Source
website: https://www.qodo.ai
---
