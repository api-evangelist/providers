---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/designstripe-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/designstripe-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/designstripe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/designstripe-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/designstripe-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DesignStripe
- group: company
  title: ''
  type: Website
  url: https://designstripe.com/
- group: company
  title: ''
  type: Website
  url: https://visual.app/
- group: company
  title: ''
  type: Blog
  url: https://visual.app/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://visual.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://visual.app/contact
coverage:
  checked: '2026-08-13'
  detail: Visual markets a design-agents API on the homepage ("every agent is an endpoint") but ships no developer surface behind it — /docs, /api and /developers all 404, no docs/developer/api subdomain resolves in DNS, and the only API-shaped host (api.designstripe.com) answers every path with a Google Cloud IAP challenge, while the product itself is reachable only by joining a waitlist.
  evidence:
  - status: 200
    url: https://visual.app/
  - status: 404
    url: https://visual.app/docs
  - status: 404
    url: https://visual.app/developers
  - status: 302
    url: https://api.designstripe.com/
  - status: 404
    url: https://visual.app/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-07-17'
description: 'The designstripe.com domain, blog and social handles were acquired by Visual (visual.app) in March 2025. Visual states on its own site that it acquired the marketing assets only and that Designstripe Inc. continues to operate independently, so this is an asset purchase rather than a rebrand. designstripe.com now 308-redirects to visual.app, an AI-first presentation and design-agent product for go-to-market teams — it generates presentations, proposals, QBRs and campaign assets through conversational agents with brand-lock consistency for sales, marketing and customer success. The legacy designstripe illustration marketplace and AI ad-maker have been retired. As of August 2026 the product is waitlist-only and markets an API on its homepage ("every agent is an endpoint... integrate design agents with your existing automation workflows or applications using our API"), but publishes no developer portal, API reference, OpenAPI definition, GraphQL endpoint, MCP server, SDK on any
  package registry, pricing page, or /.well-known discovery document. The one API-shaped host, api.designstripe.com, sits behind Google Cloud Identity-Aware Proxy and answers every request with "Invalid IAP credentials: empty token" while presenting a TLS certificate for an unrelated host. This profile was surfaced as an Insight Partners portfolio lead and enriched by the API Evangelist pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/designstripe.png
layout: provider
modified: '2026-08-13'
name: designstripe
nav: Providers
network: true
overview: 'designstripe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Design, Artificial Intelligence, and Presentations.


  designstripe''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Designstripe Plans Pricing
  plan_count: 0
  slug: designstripe-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Designstripe Rate Limits
  slug: designstripe-rate-limits
score:
  band: minimal
  composite: 8.9
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.9
  provenance:
    mcp: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Designstripe Domain Security
  slug: designstripe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: designstripe
tags:
- Company
- Consumer
- Design
- Artificial Intelligence
- Presentations
- Go-To-Market
- Marketing
- Generative AI
- Software-as-a-Service
website: https://designstripe.com/
---
