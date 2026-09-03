---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Serpapi Agentic Access
  operation_count: 3
  slug: serpapi-agentic-access
  summary_line: 3 operations
api_count: 7
apis:
- description: SerpApi is a real-time API to access Google search results. We handle proxies, solve captchas, and parse all rich structured data for you.
  name: SerpApi Google Jobs API
  slug: serpapi-google-jobs-api
- description: SerpApi is a real-time API to access Google search results. We handle proxies, solve captchas, and parse all rich structured data for you.
  name: SerpApi Google Local API
  slug: serpapi-google-local-api
- description: SerpApi is a real-time API to access Google search results. We handle proxies, solve captchas, and parse all rich structured data for you.
  name: SerpApi Google Maps API
  slug: serpapi-google-maps-api
- description: SerpApi is a real-time API to access Google search results. We handle proxies, solve captchas, and parse all rich structured data for you.
  name: SerpApi Google Search API
  slug: serpapi-google-search-api
- description: SerpApi is a real-time API to access Google search results. We handle proxies, solve captchas, and parse all rich structured data for you.
  name: SerpApi Google Trends API
  slug: serpapi-google-trends-api
- baseURL: https://serpapi.com
  baseurl_source: spec
  description: The Account API from SerpApi — 1 operation(s) for account.
  name: SerpApi Account API
  slug: serpapi-account-api
- baseURL: https://serpapi.com
  baseurl_source: spec
  description: The Search API from SerpApi — 2 operation(s) for search.
  name: SerpApi Search API
  slug: serpapi-search-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SerpApi Search Account API
  slug: open-serpapi-account-api
- collection_type: open
  name: SerpApi Account Search API
  slug: open-serpapi-search-api
- collection_type: open
  name: SerpApi Search API
  slug: open-serpapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serpapi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/serpapi-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/serpapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serpapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serpapi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/serpapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/serpapi
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/serpapi/serpapi/overview
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/serpapi/serpapi-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/serpapi/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://serpapi.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://serpapi.com/blog/feed
created: '2024-11-07'
description: SerpApi is a powerful API that helps businesses and developers access search engine results in a simple and efficient way. By using SerpApi, users can retrieve data from popular search engines like Google, Bing, Yahoo, and more, without having to worry about web scraping or parsing. This tool streamlines the process of extracting information from search engine pages, making it easy to gather essential data such as search rankings, keyword performance, and more.
finops:
- name: Serpapi Finops
  service_category: API
  slug: serpapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serpapi.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: SerpApi
nav: Providers
network: true
overview: 'SerpApi publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Search API. Tagged areas include Bing, Google, Search, and Search Engines.


  SerpApi''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Serpapi Plans Pricing
  plan_count: 3
  slug: serpapi-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Serpapi Rate Limits
  slug: serpapi-rate-limits
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 35.7
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serpapi/refs/heads/main/screenshots/serpapi-2026-06-20T193722.png
security:
- kind: authentication
  name: Serpapi Authentication
  slug: serpapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Serpapi Domain Security
  slug: serpapi-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Serpapi Vulnerability Disclosure
  slug: serpapi-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Serpapi Trust Center
  slug: serpapi-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 2
skills:
- name: serpapi-web-search
  slug: serpapi-web-search-2
- name: serpapi-web-search
  slug: serpapi-web-search
slug: serpapi
tags:
- Bing
- Google
- Search
- Search Engines
---
