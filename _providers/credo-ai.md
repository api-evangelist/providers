---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-26'
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
  name: Credo AI MCP Server
  slug: credo-ai-mcp-server
modified: '2026-08-11'
name: Credo AI
nav: Providers
network: true
overview: 'Credo AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Governance Platform API (v2) and Audit Logs & Shadow AI API. Tagged areas include Company, AI Governance, ai-risk-management, Responsible AI, and Compliance.


  Credo AI''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 19 more developer resources.'
plans:
- name: Credo Ai Plans Pricing
  plan_count: 0
  slug: credo-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Credo Ai Rate Limits
  slug: credo-ai-rate-limits
score:
  band: developing
  composite: 48.2
  delta: 2.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 30.3
    contract_quality: 33.3
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 13.2
  previous_composite: 45.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/credo-ai/refs/heads/main/screenshots/credo-ai-2026-08-17T080838.png
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
- AI Governance
- ai-risk-management
- Responsible AI
- Compliance
- Regulatory Technology
- Model Registry
- Vendor Risk
- EU AI Act
- NIST AI RMF
- ISO 42001
- Shadow AI
- Agent Governance
- Audit
- JSON:API
- Agent Skills
website: https://www.credo.ai/
---
