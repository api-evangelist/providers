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
  - rate-limits
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Golden Agentic Access
  operation_count: 8
  slug: golden-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Entity API API from Golden — 2 operation(s) for entity api.
  name: Golden Entity API API
  slug: golden-entity-api-api
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Query API API from Golden — 2 operation(s) for query api.
  name: Golden Query API API
  slug: golden-query-api-api
- baseURL: https://golden.com/api/v2/public
  baseurl_source: declared
  description: The Schema API API from Golden — 4 operation(s) for schema api.
  name: Golden Schema API API
  slug: golden-schema-api-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Golden API v2 Entity API API
  slug: open-golden-entity-api-api
- collection_type: open
  name: Golden API v2 Entity API Query API API
  slug: open-golden-query-api-api
- collection_type: open
  name: Golden API v2 Entity API Schema API API
  slug: open-golden-schema-api-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.golden.com/
- group: other
  title: ''
  type: Overlay
  url: overlays/golden-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.golden.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golden.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.golden.com
- group: start
  title: ''
  type: GettingStarted
  url: https://goldenhq.notion.site/goldenhq/Golden-Guide-1eef7518f3ca43da8d6ee4d54307801b
- group: operate
  title: ''
  type: Support
  url: https://support.golden.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://golden.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://golden.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goldenrecursion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://golden.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://golden.com/about/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/golden-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/golden-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/golden-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/golden-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/golden-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/golden-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/golden-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/golden-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/golden-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/golden-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/golden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/golden-rate-limits.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golden-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golden-domain-security.yml
created: '2026-07-17'
description: 'Golden is a company-data and knowledge-graph platform that builds a continuously updated, citation-backed map of companies, technologies, people, and the relationships between them. The Golden Public API v2 gives developers programmatic, read access to that knowledge graph: retrieve entities and their properties, resolve the schema of entity types and predicates, and run natural-language Queries that return curated, source-cited lists of entities (for example, "companies in the artificial intelligence industry"). Authentication is via an API key passed in the `apikey` header, responses are cursor-paginated, and the API is documented with an OpenAPI 3.1 specification. Golden was founded in San Francisco in 2017 by Jude Gomila, raised roughly $59.5M led by a16z with DCVC, Founders Fund, Gigafund and SV Angel participating, and was acquired by financial- crime-intelligence firm ComplyAdvantage in April 2024; the product site, self-serve plans and the Public API v2 host remain
  live and reachable.'
image: https://golden.com/static/images/38d57130206f78fb48c9.png
layout: provider
modified: '2026-08-14'
name: Golden
nav: Providers
network: true
overview: 'Golden publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entity API API, Query API API, and Schema API API. Tagged areas include Company, Knowledge Graph, Company Data, Data, and Entities.


  Golden''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Golden Plans Pricing
  plan_count: 4
  slug: golden-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Golden Rate Limits
  slug: golden-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/golden/refs/heads/main/screenshots/golden-2026-07-25T220025.png
security:
- kind: authentication
  name: Golden Authentication
  slug: golden-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Golden Domain Security
  slug: golden-domain-security
  summary_line: TLSv1.3 · DMARC
slug: golden
tags:
- Company
- Knowledge Graph
- Company Data
- Data
- Entities
- Artificial Intelligence
- Search
- Business Intelligence
website: https://www.golden.com/
---
