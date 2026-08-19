---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Valueserp Agentic Access
  operation_count: 6
  slug: valueserp-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Google Image search results.
  name: ValueSERP Images API
  slug: valueserp-images-api
- description: Google News article results.
  name: ValueSERP News API
  slug: valueserp-news-api
- description: Google Maps and local places search results.
  name: ValueSERP Places API
  slug: valueserp-places-api
- description: Google product knowledge panel data (deprecated).
  name: ValueSERP Product API
  slug: valueserp-product-api
- description: Google organic web search results.
  name: ValueSERP Search API
  slug: valueserp-search-api
- description: Google Shopping product results.
  name: ValueSERP Shopping API
  slug: valueserp-shopping-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ValueSERP Search Images API
  slug: open-valueserp-images-api
- collection_type: open
  name: ValueSERP Search Images News API
  slug: open-valueserp-news-api
- collection_type: open
  name: ValueSERP Search Images Places API
  slug: open-valueserp-places-api
- collection_type: open
  name: ValueSERP Search Images Product API
  slug: open-valueserp-product-api
- collection_type: open
  name: ValueSERP Images Search API
  slug: open-valueserp-search-api
- collection_type: open
  name: ValueSERP Search Images Shopping API
  slug: open-valueserp-shopping-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valueserp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valueserp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valueserp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trajectdata.com/serp/value-serp-api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trajectdata.com/valueserp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traject-data/
- group: company
  title: ''
  type: Blog
  url: https://trajectdata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://trajectdata.com/serp/value-serp-api/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://valueserp.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/valueserp
- group: commercial
  title: ''
  type: Plans
  url: plans/valueserp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/valueserp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/valueserp-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/vocabulary/valueserp-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/json-ld/valueserp-context.jsonld
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valueserp-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/valueserp-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/valueserp-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/valueserp-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/valueserp-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/valueserp-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valueserp-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/valueserp-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/valueserp-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/valueserp-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: webhooks/valueserp-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/valueserp-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/valueserp-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trajectdata.com/valueserp/search-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trajectdata.com/valueserp/HX_zC2K66qg5OEkKe7g5p
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.trajectdata.com/valueserp/product-updates
- group: start
  title: ''
  type: SignUp
  url: https://app.valueserp.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.valueserp.com/
- group: operate
  title: ''
  type: Support
  url: https://trajectdata.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://trajectdata.com/faqs/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trajectdata.com/traject-data-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trajectdata.com/privacy-policy/
- group: other
  title: ''
  type: CaseStudies
  url: https://trajectdata.com/case-studies
created: 2026-06-13
description: ValueSERP is a real-time Google Search API providing SERP results, image search, news search, shopping results, places, and local pack data via a simple REST interface with JSON output. Operated by Traject Data, it offers low-cost, high-reliability SERP data with no queues, batch processing capabilities, and pay-as-you-go or subscription pricing starting at $50/month for 25,000 searches.
examples:
- key_count: 4
  name: Valueserp News Search Example
  slug: valueserp-news-search-example
- key_count: 4
  name: Valueserp Organic Search Example
  slug: valueserp-organic-search-example
- key_count: 4
  name: Valueserp Places Search Example
  slug: valueserp-places-search-example
- key_count: 4
  name: Valueserp Shopping Search Example
  slug: valueserp-shopping-search-example
finops:
- name: Valueserp Finops
  service_category: ''
  slug: valueserp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valueserp.png
json_schemas:
- name: ValueSERP Search Request
  property_count: 46
  slug: valueserp-search-request
- name: ValueSERP Search Response
  property_count: 16
  slug: valueserp-search-response
jsonld:
- class_count: 0
  name: Valueserp Context
  property_count: 120
  slug: valueserp-context
layout: provider
mcp_servers:
- description: ''
  name: valueserp-mcp.yml
  slug: valueserp-mcpyml
modified: 2026-08-13
name: ValueSERP
nav: Providers
network: true
overview: 'ValueSERP publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Images API, News API, Places API, and 3 more. Tagged areas include SERP, Search Engine Results, Google Search, Search API, and SEO.


  The ValueSERP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ValueSERP''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, API reference, and 32 more developer resources.'
plans:
- name: Valueserp Plans Pricing
  plan_count: 12
  slug: valueserp-plans-pricing
random_paper: 89
rate_limits:
- limit_count: 11
  name: Valueserp Rate Limits
  slug: valueserp-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ValueSERP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valueserp-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 69.9
  delta: -9.5
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 41.7
    contract_quality: 72.7
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 41.7
    operational_transparency: 81.6
  previous_composite: 79.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/screenshots/valueserp-2026-06-20T200802.png
security:
- kind: authentication
  name: Valueserp Authentication
  slug: valueserp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valueserp Domain Security
  slug: valueserp-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Valueserp Vulnerability Disclosure
  slug: valueserp-vulnerability-disclosure
  summary_line: Hackerone
slug: valueserp
tags:
- SERP
- Search Engine Results
- Google Search
- Search API
- SEO
- Web Scraping
- Shopping Results
- News Search
- Image Search
- Local Search
- Places
- Data API
website: https://trajectdata.com/serp/value-serp-api/
---
