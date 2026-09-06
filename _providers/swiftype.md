---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for managing Swiftype search engines, indexing documents, controlling the web crawler and domains, running search and autocomplete queries, and retrieving query/click analytics. Authenticated
  name: Swiftype Site Search API
  slug: swiftype-site-search-api
artifact_total: 5
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/elastic/
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
  type: X-MCPServerCandidate
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
  name: Swiftype MCP Server
  slug: swiftype-mcp-server
modified: '2026-07-21'
name: Swiftype
nav: Providers
network: true
overview: 'Swiftype publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Search, Site Search, App Search, Full-Text Search, and Autocomplete.


  Swiftype''s developer surface includes documentation, API reference, support, authentication, and 13 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 0
  name: Swiftype Rate Limits
  slug: swiftype-rate-limits
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 20.5
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swiftype/refs/heads/main/screenshots/swiftype-2026-09-02T161401.png
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
- Full-Text Search
- Autocomplete
- Web Crawler
- Analytics
- Developer Tools
- Elastic
website: https://swiftype.com/documentation
---
