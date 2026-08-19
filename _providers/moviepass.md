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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.moviepass.com
- group: start
  title: ''
  type: SignUp
  url: https://app.moviepass.com/register/basic
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moviepass.com/plans
- group: operate
  title: ''
  type: Support
  url: https://www.moviepass.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moviepass.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moviepass.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moviepass-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moviepass-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moviepass-domain-security.yml
created: '2026-07-17'
description: 'MoviePass is a consumer movie-theater subscription service that lets members see films in theaters nationwide for a low monthly fee. The relaunched service (led by co-founder Stacy Spikes after reacquiring the brand) uses a credit-based system: members choose a monthly plan, earn credits, and redeem them for showtimes at over 4,000 participating US theaters, including major chains and independent cinemas, with plans starting around $10/month and no long-term commitment. Members browse showtimes and book through the MoviePass iOS and Android apps. MoviePass was surfaced in the API Evangelist network as a portfolio company of Canaan Partners; it is a direct-to-consumer app business and does not publish a traditional public developer API. Its marketing site is Wix-powered and exposes a hosted Wix Site MCP server plus an llms.txt for agentic access to public site content.'
image: https://static.wixstatic.com/media/f5d875_a9c258a5531b44a58f56443581eb7a9b~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: moviepass-mcp.yml
  slug: moviepass-mcpyml
modified: '2026-07-20'
name: Moviepass
nav: Providers
network: true
overview: 'Moviepass is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Movies, Entertainment, Subscription, and Consumer.


  Moviepass'' developer surface includes signup flow, pricing, support, and 6 more developer resources.'
random_paper: 89
score:
  band: emerging
  composite: 15.6
  delta: -1.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.3
  provenance:
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moviepass/refs/heads/main/screenshots/moviepass-2026-08-07T184400.png
security:
- kind: domain-security
  name: Moviepass Domain Security
  slug: moviepass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moviepass
tags:
- Company
- Movies
- Entertainment
- Subscription
- Consumer
- Streaming and Media
- Ticketing
website: https://www.moviepass.com
---
