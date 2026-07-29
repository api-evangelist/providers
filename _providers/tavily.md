---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tavily Agentic Access
  operation_count: 5
  slug: tavily-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- description: The Tavily Web API offers a unified set of endpoints for AI agents to search the web, extract page content, crawl sites, map sitemaps, and run AI research tasks. Endpoints are REST-based and authentic
  name: Tavily Web API
  slug: web-api
artifact_total: 9
collections:
- collection_type: open
  name: Tavily Web API
  slug: open-tavily
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/tavily-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tavily-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tavily-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tavily-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tavily-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tavily.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tavily.com
- group: company
  title: ''
  type: Blog
  url: https://blog.tavily.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tavily-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tavily.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tavily.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tavily.com/privacy
- group: operate
  title: ''
  type: Community
  url: https://community.tavily.com
- group: other
  title: ''
  type: X
  url: https://x.com/tavilyai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tavily
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@tavilyai
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tavily.com/llms.txt
created: '2026-05-23'
description: Tavily is a web access API platform optimized for LLMs and AI agents. It exposes a unified REST surface for real-time web search, page content extraction, site crawling, sitemap mapping, and AI-driven research tasks. The platform emphasizes low-latency search with a 180ms p50 on the search endpoint, a 99.99% uptime SLA, and built-in content validation safeguards. Tavily ships Python and JavaScript SDKs and integrates cleanly with major agent frameworks and LLM providers such as OpenAI, Anthropic, and Groq. Used by more than a million developers, it is trusted by enterprise customers including Databricks, IBM, JetBrains, MongoDB, and AWS.
finops:
- name: Tavily Finops
  service_category: API
  slug: tavily-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-23'
name: Tavily
nav: Providers
network: true
overview: 'Tavily publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Web Search, AI Agents, LLMs, and Extract.


  Tavily''s developer surface includes authentication, documentation, engineering blog, pricing, YouTube channel, and 12 more developer resources.'
plans:
- name: Tavily Plans Pricing
  plan_count: 1
  slug: tavily-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Tavily Rate Limits
  slug: tavily-rate-limits
score:
  band: thin
  composite: 31.2
  delta: -15.3
  facets:
    commercial_clarity: 68.4
    contract_quality: 8.1
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tavily/refs/heads/main/screenshots/tavily-2026-06-20T194930.png
security:
- kind: authentication
  name: Tavily Authentication
  slug: tavily-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tavily Domain Security
  slug: tavily-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tavily Trust Center
  slug: tavily-trust-center
  summary_line: trust center published
slug: tavily
tags:
- Search
- Web Search
- AI Agents
- LLMs
- Extract
- Crawl
- Sitemap
- Research
- REST
- LangChain
- LlamaIndex
- Real-Time
website: https://www.tavily.com
---
