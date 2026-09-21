---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://thirds.ai/v1
  baseurl_source: declared
  description: REST API for HTML-to-PDF, HTML-to-image, AI template generation, template editing, brand kits, rendering, and batch operations. Bearer API key auth with idempotency support.
  name: thirds.ai REST API
  slug: thirdsai-rest-api
- description: Hosted MCP server exposing thirds.ai tools (create_brand_kit, create_template, edit_template, publish_template, render, create_batch, get_status, and more) over Streamable HTTP with bearer-token auth.
  name: thirds.ai MCP Server
  slug: thirdsai-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Thirds Ai Webhooks
  slug: thirds-ai-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/security/thirds-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thirds-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/authentication/thirds-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thirds-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thirds.ai
- group: docs
  title: ''
  type: Documentation
  url: https://thirds.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://thirds.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://thirds.ai/support
- group: company
  title: ''
  type: Blog
  url: https://thirds.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirds.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirds.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://thirds.ai/changelog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/llms/thirds-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thirds-ai-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/conventions/thirds-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thirds-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/conventions/thirds-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/thirds-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/conformance/thirds-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thirds-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/lifecycle/thirds-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thirds-ai-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/plans/thirds-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thirds-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/rate-limits/thirds-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thirds-ai-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/sandbox/thirds-ai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thirds-ai-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/errors/thirds-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thirds-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/data-model/thirds-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thirds-ai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/asyncapi/thirds-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thirds-ai-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/security/thirds-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thirds-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thirds-ai/refs/heads/main/security/thirds-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thirds-ai-vulnerability-disclosure.yml
created: '2026-09-18'
description: Turn one design into content at scale. thirds.ai makes editable templates from a text prompt, HTML, a picture, or gallery and renders PDFs and images via a web app, REST API, or hosted MCP server. Outputs are PDF, PNG, JPEG, and WebP.
layout: provider
mcp_servers:
- description: Official hosted MCP server exposing thirds.ai PDF/image rendering, template, brand-kit and batch tools over Streamable HTTP with bearer-token auth. Uses the caller's existing account, credits and temp
  name: thirds.ai MCP Server
  slug: thirdsai-mcp-server
- description: ''
  name: thirds.ai MCP Server
  slug: thirdsai-mcp-server-2
modified: '2026-09-18'
name: thirds.ai
nav: Providers
network: true
overview: 'thirds.ai publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include pdf-automation, image-automation, Document Generation, HTML to PDF, and HTML to Image.


  The thirds.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  thirds.ai''s developer surface includes authentication, documentation, pricing, support, engineering blog, changelog, sandbox, and 17 more developer resources.'
plans:
- name: Thirds Ai Plans Pricing
  plan_count: 4
  slug: thirds-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Thirds Ai Rate Limits
  slug: thirds-ai-rate-limits
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.0
    catalog_earned_first_party: 24.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 63.2
    developer_ergonomics: 56.5
    discoverability: 72.2
    operational_transparency: 65.8
  previous_composite: 55.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Thirds Ai Authentication
  slug: thirds-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Thirds Ai Domain Security
  slug: thirds-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thirds Ai Vulnerability Disclosure
  slug: thirds-ai-vulnerability-disclosure
  summary_line: contact published
slug: thirds-ai
tags:
- pdf-automation
- image-automation
- Document Generation
- HTML to PDF
- HTML to Image
- template-rendering
- Branded Content
- Developer Tools
- MCP Server
- agent-native
- marketing-ops
website: https://thirds.ai
---
