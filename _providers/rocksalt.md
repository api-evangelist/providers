---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocksalt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rocksalt.ai/
- group: company
  title: ''
  type: About
  url: https://www.rocksalt.ai/about
- group: docs
  title: ''
  type: Documentation
  url: https://www.rocksalt.ai/rocksalt-help-documentation-and-product-guides
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.rocksalt.ai/rocksalt-help-documentation-and-product-guides
- group: operate
  title: ''
  type: Support
  url: mailto:support@rocksalt.ai
- group: company
  title: ''
  type: Blog
  url: https://blog.rocksalt.ai/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.rocksalt.ai/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rocksalt.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/rocksalt-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rocksalt-llms.txt
- group: start
  title: ''
  type: SignUp
  url: https://on.rocksalt.ai/
- group: start
  title: ''
  type: Login
  url: https://app.rocksalt.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rocksalt.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rocksalt.ai/privacy-policy
coverage:
  checked: '2026-08-13'
  detail: Rocksalt ships only an end-user web app and browser extension — its full 37-URL sitemap has no developer path, api.rocksalt.ai and docs.rocksalt.ai do not resolve in DNS, and app.rocksalt.ai answers 200 with the same SPA HTML shell for /openapi.json and /.well-known/agent-card.json alike, so those 200s are soft-404s rather than a hidden contract.
  evidence:
  - status: 200
    url: https://www.rocksalt.ai/sitemap.xml
  - status: 404
    url: https://www.rocksalt.ai/openapi.json
  - status: 404
    url: https://www.rocksalt.ai/llms.txt
  - status: 404
    url: https://www.rocksalt.ai/.well-known/agent-card.json
  - status: 200
    url: https://www.rocksalt.ai/rocksalt-help-documentation-and-product-guides
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Rocksalt is a B2B inbound and social-engagement platform, headquartered in Redwood City, California and founded in 2023 by Arjun Moorthy (CEO), Anita Moorthy (CMO), and Ajoy Sojan (CTO). The product helps founders, executives, and subject-matter experts build visibility and win business on LinkedIn and Reddit in roughly ten minutes a day: an AI-powered digest surfaces the industry conversations worth joining, suggests personalized comments grounded in the user''s expertise, assists with post creation, and adds team collaboration workflows plus analytics and HubSpot CRM sync. Rocksalt raised seed funding from Lightspeed Venture Partners in 2025. It is a marketing SaaS application delivered through a web app rather than a public developer API; this profile was surfaced from the Lightspeed portfolio and enriched with the company''s public identity and web properties.'
image: https://www.rocksalt.ai/hubfs/Rocksalt_Logo_Header.svg
layout: provider
modified: '2026-08-13'
name: Rocksalt
nav: Providers
network: true
overview: 'Rocksalt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Social Media, Sales Enablement, and Content.


  Rocksalt''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Rocksalt Plans Pricing
  plan_count: 5
  slug: rocksalt-plans-pricing
random_paper: 122
rate_limits:
- limit_count: 0
  name: Rocksalt Rate Limits
  slug: rocksalt-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 8.2
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: domain-security
  name: Rocksalt Domain Security
  slug: rocksalt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rocksalt
tags:
- Company
- Marketing
- Social Media
- Sales Enablement
- Content
- Customer Relationship Management (CRM)
- Artificial Intelligence
- SaaS
website: https://www.rocksalt.ai/
---
