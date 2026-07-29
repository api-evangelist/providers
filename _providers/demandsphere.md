---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Demandsphere Agentic Access
  operation_count: 10
  slug: demandsphere-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 4
apis:
- description: The Keywords API from DemandSphere — 6 operation(s) for keywords.
  name: DemandSphere Keywords API
  slug: demandsphere-keywords-api
- description: The Pages API from DemandSphere — 1 operation(s) for pages.
  name: DemandSphere Pages API
  slug: demandsphere-pages-api
- description: The SearchEngines API from DemandSphere — 1 operation(s) for searchengines.
  name: DemandSphere SearchEngines API
  slug: demandsphere-searchengines-api
- description: The Sites API from DemandSphere — 2 operation(s) for sites.
  name: DemandSphere Sites API
  slug: demandsphere-sites-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/demandsphere-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/demandsphere-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/demandsphere-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/demandsphere-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://demandsphere.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.demandsphere.com/solutions/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://help.demandsphere.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.demandsphere.com/platform/apis/rest-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.demandsphere.com/platform/apis/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.demandsphere.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.demandsphere.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.demandsphere.com/resources/help-center/
- group: start
  title: ''
  type: SignUp
  url: https://www.demandsphere.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.demandsphere.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.demandsphere.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DemandSphereDev
- group: operate
  title: ''
  type: StatusPage
  url: https://status.demandsphere.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.demandsphere.com/changelog
- group: auth
  title: ''
  type: Compliance
  url: https://www.demandsphere.com/security/
- group: auth
  title: ''
  type: Security
  url: https://www.demandsphere.com/security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/demandsphere-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/demandsphere-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/demandsphere-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/demandsphere-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/demandsphere-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/demandsphere-packages.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/demandsphere-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: DemandSphere is a unified AI search visibility platform (founded 2010, Y Combinator S10) that tracks brand presence across traditional search engine results pages, AI search engines (ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode), and agentic surfaces. Its modular products cover DemandMetrics SERP analytics, DemandMetrics for Gen AI (LLM visibility and citation tracking), DemandSphere Agents workflow automation, Analytics AX log-file analytics, and Search Intelligence, a BigQuery data warehouse. The DemandSphere REST API (v5.0) exposes rank tracking, ranking trends, keyword groups, local rankings, landing matches, search-engine summaries, and site hierarchy data as JSON over api-key authentication, across 200+ markets and 10+ search engines, and is complemented by a first-party Model Context Protocol (MCP) server for agent access.
image: https://www.demandsphere.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: demandsphere-mcp.yml
  slug: demandsphere-mcpyml
modified: '2026-07-18'
name: DemandSphere
nav: Providers
network: true
overview: 'DemandSphere publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Keywords API, Pages API, SearchEngines API, and 1 more. Tagged areas include Company, SEO, Search Intelligence, SERP Analytics, and AI Search.


  DemandSphere''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 21 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 54.1
  delta: 0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 50.8
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/demandsphere/refs/heads/main/screenshots/demandsphere-2026-07-25T211708.png
security:
- kind: authentication
  name: Demandsphere Authentication
  slug: demandsphere-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Demandsphere Domain Security
  slug: demandsphere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Demandsphere Vulnerability Disclosure
  slug: demandsphere-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Demandsphere Trust Center
  slug: demandsphere-trust-center
  summary_line: GDPR
slug: demandsphere
tags:
- Company
- SEO
- Search Intelligence
- SERP Analytics
- AI Search
- LLM Visibility
- Rank Tracking
- Analytics
- API
- MCP
website: https://demandsphere.com
---
