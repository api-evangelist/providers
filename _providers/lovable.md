---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Generates a Lovable application from a shareable URL or prompt. Programmatic entry point for creating apps and sharing links without revealing implementation details. Early release; more endpoints pla
  name: Lovable Build with URL API
  slug: build-with-url
- description: Model Context Protocol server at https://mcp.lovable.dev. Allows AI clients (Claude Desktop, Cursor, etc.) to create and manage Lovable projects through natural-language MCP tool calls.
  name: Lovable MCP Server (Research Preview)
  slug: mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lovable-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lovable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovable-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lovablelabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lovable-dev
- group: company
  title: ''
  type: Website
  url: https://lovable.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lovable.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://lovable.dev/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/lovable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lovable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lovable-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lovable.dev/llms.txt
created: '2026-05-08'
description: 'Lovable is an AI app builder that generates full-stack web applications from natural- language prompts, with live preview, GitHub sync, and Supabase / Firebase integration. Lovable''s developer-facing surface is in early release: the "Build with URL" API generates apps from a shareable URL, and the Lovable MCP Server lets AI clients (Claude Desktop, Cursor) manage Lovable projects via Model Context Protocol.'
finops:
- name: Lovable Finops
  service_category: AI
  slug: lovable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lovable.png
layout: provider
modified: '2026-05-08'
name: Lovable
nav: Providers
network: true
overview: 'Lovable publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, No-Code, App Builder, Web Development, and Generative.


  Lovable''s developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Lovable Plans Pricing
  plan_count: 1
  slug: lovable-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Lovable Rate Limits
  slug: lovable-rate-limits
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lovable/refs/heads/main/screenshots/lovable-2026-06-20T184733.png
security:
- kind: domain-security
  name: Lovable Domain Security
  slug: lovable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lovable Vulnerability Disclosure
  slug: lovable-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lovable Trust Center
  slug: lovable-trust-center
  summary_line: SOC 2, GDPR
slug: lovable
tags:
- AI
- No-Code
- App Builder
- Web Development
- Generative
- MCP
website: https://lovable.dev/
---
