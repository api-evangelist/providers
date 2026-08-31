---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Fumadocs Agentic Access
  operation_count: 8
  slug: fumadocs-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 2
apis:
- description: Fumadocs is an open-source documentation framework built on Next.js and React for creating fast, modern developer documentation sites. It provides a full stack of composable packages including fumadoc
  name: Fumadocs
  slug: fumadocs
- description: HTTP proxy endpoints that forward requests to external API servers on behalf of the browser-based OpenAPI playground to avoid CORS issues.
  name: Fumadocs Proxy API
  slug: fumadocs-proxy-api
- description: Search endpoints for querying documentation content. Results include pages, headings, and text segments ranked by relevance.
  name: Fumadocs Search API
  slug: fumadocs-search-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fumadocs OpenAPI Proxy API
  slug: open-fumadocs-openapi-proxy
- collection_type: open
  name: Fumadocs OpenAPI Proxy API
  slug: open-fumadocs-proxy-api
- collection_type: open
  name: Fumadocs OpenAPI Proxy Search API
  slug: open-fumadocs-search-api
- collection_type: open
  name: Fumadocs Search API
  slug: open-fumadocs-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fumadocs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fumadocs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fumadocs.dev
- group: docs
  title: ''
  type: Documentation
  url: https://fumadocs.dev/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/fuma-nama/fumadocs
- group: docs
  title: ''
  type: Documentation
  url: https://fumadocs.dev/docs/ui/components
- group: docs
  title: ''
  type: Documentation
  url: https://fumadocs.dev/docs/headless/search/orama
- group: docs
  title: ''
  type: Documentation
  url: https://fumadocs.dev/docs/ui/openapi
- group: other
  title: ''
  type: Distribution
  url: https://www.npmjs.com/package/fumadocs-core
- group: other
  title: ''
  type: Distribution
  url: https://www.npmjs.com/package/fumadocs-ui
- group: other
  title: ''
  type: Distribution
  url: https://www.npmjs.com/package/fumadocs-openapi
- group: commercial
  title: ''
  type: License
  url: https://github.com/fuma-nama/fumadocs/blob/main/LICENSE
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fumadocs-page-tree-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fumadocs-page-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fumadocs-meta-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fumadocs-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://fumadocs.dev/blog/rss.xml
created: '2026-03-18'
description: Fumadocs is a modern documentation framework built on Next.js for building developer documentation sites. It provides a complete set of composable packages for content loading, navigation tree generation, full-text search, UI components, and interactive API reference generation from OpenAPI specifications.
finops:
- name: Fumadocs Finops
  service_category: Developer Tools
  slug: fumadocs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fumadocs.png
json_schemas:
- name: Fumadocs Meta
  property_count: 7
  slug: fumadocs-meta
- name: Fumadocs Page
  property_count: 5
  slug: fumadocs-page
- name: Fumadocs Page Tree
  property_count: 0
  slug: fumadocs-page-tree
- name: Fumadocs Search Result
  property_count: 5
  slug: fumadocs-search-result
jsonld:
- class_count: 0
  name: Fumadocs Context
  property_count: 7
  slug: fumadocs-context
layout: provider
modified: '2026-05-19'
name: Fumadocs
nav: Providers
network: true
overview: 'Fumadocs publishes 2 APIs on the [APIs.io](https://apis.io/) network: Proxy API and Search API. Tagged areas include Documentation, Framework, Next.js, and React.


  The Fumadocs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fumadocs'' developer surface includes documentation, GitHub presence, engineering blog, and 14 more developer resources.'
plans:
- name: Fumadocs Plans Pricing
  plan_count: 1
  slug: fumadocs-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Fumadocs Rate Limits
  slug: fumadocs-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Fumadocs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: fumadocs-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 66.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fumadocs/refs/heads/main/screenshots/fumadocs-2026-06-20T181650.png
security:
- kind: domain-security
  name: Fumadocs Domain Security
  slug: fumadocs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fumadocs
tags:
- Documentation
- Framework
- Next.js
- React
website: https://fumadocs.dev
---
