---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Livekindly Agentic Access
  operation_count: 83
  slug: livekindly-agentic-access
  summary_line: 83 operations · 44 acting
api_count: 2
apis:
- description: The anonymously readable WordPress REST API that thelivekindlyco.com serves at /wp-json/wp/v2 — the corporate newsroom and LiveKindly Blog (39 posts), the corporate site pages (19), the brand director
  name: LIVEKINDLY Content API (WordPress REST wp/v2)
  slug: content
- description: A Model Context Protocol server advertised in the thelivekindlyco.com WordPress REST route index under the "mcp" namespace, with two endpoints — mcp-adapter-default-server and mcp-oauth-server. Unlike
  name: LIVEKINDLY MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://thelivekindlyco.com/
- group: company
  title: ''
  type: About
  url: https://thelivekindlyco.com/the-collective/
- group: company
  title: ''
  type: Blog
  url: https://thelivekindlyco.com/latest-news/
- group: company
  title: ''
  type: News
  url: https://thelivekindlyco.com/latest-news/
- group: operate
  title: ''
  type: Support
  url: https://thelivekindlyco.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://thelivekindlyco.com/careers/
- group: other
  title: ''
  type: Team
  url: https://thelivekindlyco.com/team/
- group: other
  title: ''
  type: Leadership
  url: https://thelivekindlyco.com/directors/
- group: other
  title: ''
  type: Products
  url: https://thelivekindlyco.com/b2b-solutions/
- group: other
  title: ''
  type: Impact
  url: https://thelivekindlyco.com/join-the-change/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thelivekindlyco.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thelivekindlyco.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-livekindly-co
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/thelivekindlyco
- group: other
  title: ''
  type: Sitemap
  url: https://thelivekindlyco.com/sitemap_index.xml
- group: build
  title: ''
  type: Packages
  url: packages/livekindly-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/livekindly-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/livekindly-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livekindly-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/livekindly-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/livekindly-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/livekindly-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livekindly-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/livekindly-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/livekindly_stock/
created: '2026-08-04'
description: LIVEKINDLY Collective (thelivekindlyco.com) is a global plant-based food company founded in March 2020 by Roger Lienhard around a mission to make plant-based living the new norm. It is a house of alternative-protein brands — Fry's Family Food Co., Like Meat, Oumph! and The No Meat Company — sold across Europe, the UK, South Africa and North America, and it also runs a B2B Solutions arm supplying plant-based protein to other food businesses. The Collective raised over half a billion dollars across its early rounds, reported profitability in November 2025, announced it was joining forces with TiNDLE Foods in December 2025, and was certified as a B Corp in June 2026. LIVEKINDLY publishes no developer platform, no documentation portal and no OpenAPI. The machine-readable surface on thelivekindlyco.com is its WordPress REST API (wp/v2), which serves the corporate newsroom, the brand and partner directories, the careers listings, pages and media library as anonymously readable JSON,
  alongside a WordPress MCP Adapter endpoint that is live and fronted by a real RFC 8414 OAuth authorization server — but is authentication-gated to a single "mcp" scope. The company is tracked on the Forge Global secondary market.
image: https://thelivekindlyco.com/wp-content/uploads/2021/10/cropped-lkc-favicon.png
layout: provider
mcp_servers:
- description: ''
  name: livekindly-mcp.yml
  slug: livekindly-mcpyml
modified: '2026-08-04'
name: LIVEKINDLY
nav: Providers
network: true
overview: 'LIVEKINDLY publishes 1 API on the [APIs.io](https://apis.io/) network: Content API (WordPress REST wp/v2). Tagged areas include Company, Food and Beverage, Plant-Based, Alternative Protein, and Consumer Packaged Goods.


  LIVEKINDLY''s developer surface includes engineering blog, product news, support, authentication, and 22 more developer resources.'
random_paper: 66
scopes:
- name: Livekindly Scopes
  scope_count: 1
  slug: livekindly-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 15.1
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Livekindly Authentication
  slug: livekindly-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Livekindly Domain Security
  slug: livekindly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: livekindly
tags:
- Company
- Food and Beverage
- Plant-Based
- Alternative Protein
- Consumer Packaged Goods
- Sustainability
- Manufacturing
- Retail
- Content
- Newsroom
website: https://thelivekindlyco.com/
---
