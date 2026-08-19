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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Zenserp Agentic Access
  operation_count: 13
  slug: zenserp-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 5
apis:
- description: 'Asynchronous batch endpoint for very large SERP datasets. Jobs are submitted together and results are POSTed back to a caller-supplied webhook_url, or polled by batch id. Available on the Medium plan '
  name: Zenserp Batch API
  slug: zenserp-batch-api
- description: 'Reference list endpoints publishing the enumerations the Search API parameters must draw from: supported interface languages (hl), countries (gl), canonical Google geo-targeting locations, and search-'
  name: Zenserp Lists API
  slug: zenserp-lists-api
- description: Core search endpoint. One GET operation returns Google web, image, video, news, shopping and maps results (selected with tbm) plus Bing, Yandex, DuckDuckGo and YouTube results (selected with search_en
  name: Zenserp Search API
  slug: zenserp-search-api
- description: Google Shopping product page endpoint, resolving a single product variant by product_id or a full product cluster across all merchants by gpc_id. Product ids are obtained from a shopping search. Serve
  name: Zenserp Shopping Product Page API
  slug: zenserp-shopping-api
- description: Google Trends endpoints exposing keyword interest over time for one or more keywords, and the currently trending searches for a category, language and region. Served from the v1 base, not v2.
  name: Zenserp Trends API
  slug: zenserp-trends-api
artifact_total: 24
asyncapis:
- description: ''
  name: Zenserp Batch Webhooks
  slug: zenserp-batch-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zenserp Batch API
  slug: open-zenserp-batch-api
- collection_type: open
  name: Zenserp Lists API
  slug: open-zenserp-lists-api
- collection_type: open
  name: Zenserp Search API
  slug: open-zenserp-search-api
- collection_type: open
  name: Zenserp Shopping Product Page API
  slug: open-zenserp-shopping-api
- collection_type: open
  name: Zenserp Trends API
  slug: open-zenserp-trends-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenserp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenserp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenserp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zenserp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.zenserp.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://zenserp.com/pricing-plans/
- group: company
  title: ''
  type: Blog
  url: https://zenserp.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zenserp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer/
- group: other
  title: ''
  type: X
  url: https://twitter.com/apilayer
- group: commercial
  title: ''
  type: Plans
  url: plans/zenserp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenserp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zenserp-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/zenserp-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zenserp-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zenserp-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/zenserp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zenserp-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zenserp-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zenserp-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zenserp-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zenserp-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zenserp-batch-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zenserp-search-overlay.yaml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/collections/a888b56749cd50cc525d
- group: docs
  title: ''
  type: APIReference
  url: https://app.zenserp.com/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.zenserp.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.zenserp.com/register
- group: start
  title: ''
  type: Login
  url: https://app.zenserp.com/login
- group: operate
  title: ''
  type: Support
  url: https://apilayer.com/support
- group: operate
  title: ''
  type: Contact
  url: https://zenserp.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zenserp.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zenserp.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenserp
created: '2026-06-13'
description: Zenserp is a Google SERP API that enables developers to fetch live, structured search engine results in real time without interruption. The API supports web, image, video, news, shopping, maps, YouTube, Bing, Yandex, DuckDuckGo, reverse image, and trends search types across 200+ countries, returning clean JSON responses. It offers geolocation-based queries, batch endpoints, keyword search volume and CPC data, and a bulk index checker tool, with a 99.9% uptime SLA.
examples:
- key_count: 2
  name: Zenserp Batch Search Example
  slug: zenserp-batch-search-example
- key_count: 3
  name: Zenserp Image Search Example
  slug: zenserp-image-search-example
- key_count: 6
  name: Zenserp Web Search Example
  slug: zenserp-web-search-example
finops:
- name: Zenserp Finops
  service_category: ''
  slug: zenserp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenserp.png
json_schemas:
- name: Zenserp Search Response
  property_count: 14
  slug: zenserp-search-response
jsonld:
- class_count: 17
  name: Zenserp Context
  property_count: 59
  slug: zenserp-context
layout: provider
modified: '2026-08-13'
name: Zenserp
nav: Providers
network: true
overview: 'Zenserp publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Batch API, Lists API, Search API, and 2 more. Tagged areas include SERP, Search Engine Results, Google Search, Web Scraping, and SEO.


  The Zenserp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Zenserp''s developer surface includes authentication, documentation, pricing, engineering blog, sandbox, API reference, signup flow, and 28 more developer resources.'
plans:
- name: Zenserp Plans Pricing
  plan_count: 6
  slug: zenserp-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 7
  name: Zenserp Rate Limits
  slug: zenserp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zenserp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenserp-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.0
  delta: -11.6
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 26.5
    contract_quality: 73.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 26.5
    operational_transparency: 42.1
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zenserp/refs/heads/main/screenshots/zenserp-2026-06-20T201820.png
security:
- kind: authentication
  name: Zenserp Authentication
  slug: zenserp-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Zenserp Domain Security
  slug: zenserp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenserp
tags:
- SERP
- Search Engine Results
- Google Search
- Web Scraping
- SEO
- Image Search
- News Search
- Shopping Search
- Maps
- YouTube Search
- Bing
- Yandex
- DuckDuckGo
- Geolocation
- Keyword Research
website: https://zenserp.com/
---
