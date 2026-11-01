---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MCP server providing competitor analysis via a single endpoint for AI agents.
  name: Analook MCP API
  slug: analook-mcp-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/analook-com/llms/analook-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/analook-com-llms.txt
- group: other
  href: https://artifacts.apis.io/analook-com/hosts/analook-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/analook-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/analook-com/security/analook-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/analook-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://analook.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.analook.com/docs/mcp.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.analook.com/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://www.analook.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.analook.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.analook.com/privacy.html
coverage:
  checked: '2026-10-29'
  detail: Documentation provides HTML only, no OpenAPI/AsyncAPI/GraphQL spec found.
  evidence:
  - status: 200
    url: https://www.analook.com/docs/mcp.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Analook provides a free AI-powered competitor analysis platform that quickly generates comprehensive reports on SaaS products. Users can input a URL and receive insights on SEO, traffic, social signals, Product Hunt presence, GitHub activity, pricing, and AI-driven recommendations. The service offers both a free tier with limited analyses and paid plans for higher volume, supporting founders and marketers in strategic decision‑making. The platform also includes an MCP server for integration with AI agents, enabling automated competitor research within workflows.
image: https://www.analook.com/assets/og/homepage.png
layout: provider
modified: '2026-10-29'
name: analook-com
nav: Providers
network: true
overview: 'analook-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, CompetitorAnalysis, SaaS, Marketing, and FreeTool.


  analook-com''s developer surface includes documentation, pricing, engineering blog, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Analook Com Domain Security
  slug: analook-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: analook-com
tags:
- AI
- CompetitorAnalysis
- SaaS
- Marketing
- FreeTool
website: https://analook.com/
---
