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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
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
overview: 'Lovable publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, No-Code, App Builder, Web Development, and Generative.


  Lovable''s developer surface includes documentation, pricing, and 10 more developer resources.'
plans:
- name: Lovable Plans Pricing
  plan_count: 1
  slug: lovable-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Lovable Rate Limits
  slug: lovable-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 7
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 16.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Artificial Intelligence
- No-Code
- App Builder
- Web Development
- Generative
- MCP
website: https://lovable.dev/
---
