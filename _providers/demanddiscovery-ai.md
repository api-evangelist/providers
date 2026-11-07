---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote MCP connector (streamable HTTP, server demand-discovery-ai v1.3.26, protocol 2025-03-26) that lets founders validate a startup idea inside Claude, ChatGPT, Cursor, Replit, Lovable, v0, Bolt and
  name: Demand Discovery AI MCP Server
  slug: demand-discovery-mcp-server
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/demanddiscovery-ai/plans/demanddiscovery-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/demanddiscovery-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/demanddiscovery-ai/authentication/demanddiscovery-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/demanddiscovery-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/demanddiscovery-ai/llms/demanddiscovery-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/demanddiscovery-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/demanddiscovery-ai/hosts/demanddiscovery-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demanddiscovery-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/demanddiscovery-ai/integrations/demanddiscovery-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/demanddiscovery-ai-integration-edges.yml
- group: company
  title: ''
  type: Website
  url: https://demanddiscovery.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://demanddiscovery.ai/mcp-server-startup-idea-validation
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.demanddiscovery.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://demanddiscovery.ai/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://demanddiscovery.ai/pricing
- group: operate
  title: ''
  type: HelpCenter
  url: https://demanddiscovery.ai/faq
- group: company
  title: ''
  type: Blog
  url: https://demanddiscovery.ai/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demanddiscovery.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demanddiscovery.ai/privacy
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@demand.discovery
- group: other
  title: ''
  type: Email
  url: mailto:hi@demanddiscovery.ai
- group: auth
  href: https://artifacts.apis.io/demanddiscovery-ai/security/demanddiscovery-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demanddiscovery-ai-domain-security.yml
created: '2026-11-05'
description: Demand Discovery AI (styled Demand Discovery AI™, demanddiscovery.ai) is an evidence-based startup idea validation platform for founders and vibe coders. Its reports compile real people, quoted in their own words and linked to the source, asking for what a founder wants to build, drawn from public content on Reddit, YouTube, Hacker News, Product Hunt, X and Indie Hackers, plus a Startup Demand Score, free market research, landing pages and prospect outreach drafts. It is also delivered as an MCP server (mcp.demanddiscovery.ai) usable from Claude, ChatGPT, Cursor, Replit, Lovable, v0, Bolt and Base44. Its Terms of Service are governed by the laws of Delaware, United States.
image: https://demanddiscovery.ai/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Demand Discovery AI MCP Server
  slug: https-mcp-demanddiscovery-ai
- description: ''
  name: Demand Discovery AI MCP Server
  slug: mcp
modified: '2026-11-05'
name: Demand Discovery AI
nav: Providers
network: true
overview: 'Demand Discovery AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Startup Idea Validation, Market Research, Demand Discovery, and Artificial Intelligence.


  Demand Discovery AI''s developer surface includes authentication, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Demanddiscovery Ai Plans Pricing
  plan_count: 5
  slug: demanddiscovery-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Demanddiscovery Ai Rate Limits
  slug: demanddiscovery-ai-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 71.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Demanddiscovery Ai Authentication
  slug: demanddiscovery-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Demanddiscovery Ai Domain Security
  slug: demanddiscovery-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demanddiscovery-ai
tags:
- Company
- Startup Idea Validation
- Market Research
- Demand Discovery
- Artificial Intelligence
- MCP
- Customer Discovery
website: https://demanddiscovery.ai/
---
