---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
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
  score: 23.9
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Multi-tenant JSON:API REST interface to the Credo AI Governance Platform. 300 operations across 26 tags cover use cases, use case questionnaires, risk scenarios, controls, policy packs, reports, revie
  name: Credo AI Governance Platform API (v2)
  slug: credo-ai-governance-platform-api-v2
- description: OpenAPI 3.0.0 contract covering the audit-log and Shadow AI slice of the Credo AI v2 API — listing, filtering, exporting and retrieving audit log entries, and ingesting, listing, bulk-loading and dele
  name: Credo AI Audit Logs & Shadow AI API
  slug: credo-ai-audit-logs-shadow-ai-api
- description: Provider-published Model Context Protocol server ("governance-hub") distributed as the npm package @credoai/governance-hub-mcp and run over stdio via npx. Grounds the Credo AI Claude Code Agent Skills
  name: Credo AI Governance Intelligence Pro MCP Server
  slug: credo-ai-governance-intelligence-pro-mcp-server
artifact_total: 12
collections:
- collection_type: open
  name: Credo AI API
  slug: open-credo-ai-audit-logs-shadow-ai
- collection_type: open
  name: Credo AI server API
  slug: open-credo-ai-governance-platform-swagger
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.credo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sdk.credo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sdk.credo.ai/docs/intro/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sdk.credo.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sdk.credo.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.credo.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.credo.ai/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/credo-ai
- group: start
  title: ''
  type: SignUp
  url: https://www.credo.ai/get-started
- group: start
  title: ''
  type: Login
  url: https://app.credo.ai/
- group: commercial
  title: ''
  type: Pricing
  url: plans/credo-ai-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.credo.ai/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.credo.ai/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.credo.ai/legal/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/credo-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/credo-ai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/credo-ai-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/credo-ai-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/credo-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/credo-ai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credo-ai-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/credo-ai-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/credo-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/credo-ai-rate-limits.yml
created: '2026-08-11'
description: Credo AI is an enterprise AI governance, risk, and compliance platform used to discover, register, risk-classify, and continuously govern every AI model, application, agent, and third-party AI vendor an organization runs. The platform pairs an AI Registry (use cases, models, vendors, agents, shadow-AI discovery) with a policy engine that turns regulatory frameworks — the EU AI Act, NIST AI RMF, ISO/IEC 42001, NYC Local Law 144, Colorado SB21-169, OMB M-25 — into machine-enforced policy packs, controls, questionnaires, risk scenarios, and audit-ready evidence artifacts. Programmatic access is delivered through a multi-tenant JSON:API REST surface at api.credo.ai (300 operations across use cases, models, vendors, questionnaires, policy packs, policy controls, risks, tasks, teams, users, triggers, and Shadow AI), a first-party Python SDK (pycredoai) and TypeScript SDK (@credo-ai/sdk), and a published Claude Code plugin marketplace of eleven AI-governance Agent Skills backed by
  a gated Governance Intelligence Pro MCP server.
image: https://cdn.prod.website-files.com/649d808ba8385965c74d94df/6a27d15ec3da571348386f01_OPENGRAPGH-light.png
layout: provider
mcp_servers:
- description: ''
  name: credo-ai-mcp.yml
  slug: credo-ai-mcpyml
modified: '2026-08-11'
name: Credo AI
nav: Providers
network: true
overview: 'Credo AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Governance Platform API (v2) and Audit Logs & Shadow AI API. Tagged areas include Company, ai-governance, ai-risk-management, responsible-ai, and compliance.


  Credo AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 19 more developer resources.'
plans:
- name: Credo Ai Plans Pricing
  plan_count: 0
  slug: credo-ai-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 0
  name: Credo Ai Rate Limits
  slug: credo-ai-rate-limits
score:
  band: developing
  composite: 43.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 54.3
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 43.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Credo Ai Authentication
  slug: credo-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Credo Ai Domain Security
  slug: credo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Credo Ai Vulnerability Disclosure
  slug: credo-ai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Credo Ai Trust Center
  slug: credo-ai-trust-center
  summary_line: SOC 2 Type II
slug: credo-ai
tags:
- Company
- ai-governance
- ai-risk-management
- responsible-ai
- compliance
- regulatory-technology
- model-registry
- vendor-risk
- eu-ai-act
- nist-ai-rmf
- iso-42001
- shadow-ai
- agent-governance
- audit
- json-api
- agent-skills
website: https://www.credo.ai/
---
