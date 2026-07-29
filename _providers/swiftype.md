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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing Swiftype search engines, indexing documents, controlling the web crawler and domains, running search and autocomplete queries, and retrieving query/click analytics. Authenticated
  name: Swiftype Site Search API
  slug: swiftype-site-search-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swiftype-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://swiftype.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://swiftype.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://swiftype.com/documentation/site-search/overview
- group: operate
  title: ''
  type: Support
  url: https://discuss.elastic.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
- group: operate
  title: ''
  type: StatusPage
  url: https://www.swiftypestatus.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/swiftype-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/swiftype-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/swiftype-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/swiftype-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swiftype-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/swiftype-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swiftype-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/swiftype-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swiftype-llms.txt
created: '2026-07-17'
description: Swiftype is a hosted site-search and app-search platform founded in 2012, backed by Andreessen Horowitz (a16z) and DCVC, and acquired by Elastic in 2017 where it now operates as Elastic Site Search. Swiftype gives websites and applications relevance-tuned full-text search, autocomplete, a managed web crawler, document indexing, result ranking/weighting controls, synonyms, and query and click analytics. Developers integrate through the Site Search REST API at https://search-api.swiftype.com/api/v1/ using a private auth_token for full read/write access or a public engine_key for read-only client-side search, with official client libraries for PHP, Python, Node.js, and Ruby published under the Elastic GitHub organization.
image: https://swiftype.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: swiftype-mcp.yml
  slug: swiftype-mcpyml
modified: '2026-07-21'
name: Swiftype
nav: Providers
network: true
overview: 'Swiftype publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Site Search, App Search, Full Text Search, and Autocomplete.


  Swiftype''s developer surface includes documentation, API reference, support, authentication, and 12 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Swiftype Rate Limits
  slug: swiftype-rate-limits
score:
  band: emerging
  composite: 21.4
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 22.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Swiftype Authentication
  slug: swiftype-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Swiftype Domain Security
  slug: swiftype-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swiftype
tags:
- Search
- Site Search
- App Search
- Full Text Search
- Autocomplete
- Web Crawler
- Analytics
- Developer Tools
- Elastic
website: https://swiftype.com/documentation
---
