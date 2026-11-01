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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Valueserp Agentic Access
  operation_count: 6
  slug: valueserp-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google Image search results.
  name: ValueSERP Images API
  slug: valueserp-images-api
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google News article results.
  name: ValueSERP News API
  slug: valueserp-news-api
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google Maps and local places search results.
  name: ValueSERP Places API
  slug: valueserp-places-api
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google product knowledge panel data (deprecated).
  name: ValueSERP Product API
  slug: valueserp-product-api
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google organic web search results.
  name: ValueSERP Search API
  slug: valueserp-search-api
- baseURL: https://api.valueserp.com
  baseurl_source: declared
  description: Google Shopping product results.
  name: ValueSERP Shopping API
  slug: valueserp-shopping-api
artifact_total: 33
collections:
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
- group: other
  href: https://artifacts.apis.io/valueserp/capabilities/valueserp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/valueserp-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/valueserp/overview
- group: agent
  href: https://artifacts.apis.io/valueserp/agentic-access/valueserp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/valueserp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/valueserp/security/valueserp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/valueserp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/valueserp/authentication/valueserp-authentication.yml
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
  href: https://artifacts.apis.io/valueserp/plans/valueserp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/valueserp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/valueserp/rate-limits/valueserp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/valueserp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/valueserp/finops/valueserp-finops.yml
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
  href: https://artifacts.apis.io/valueserp/llms/valueserp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/valueserp-llms.txt
- group: build
  href: https://artifacts.apis.io/valueserp/packages/valueserp-packages.yml
  title: ''
  type: Packages
  url: packages/valueserp-packages.yml
- group: agent
  href: https://artifacts.apis.io/valueserp/mcp/valueserp-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/valueserp-mcp.yml
- group: design
  href: https://artifacts.apis.io/valueserp/conventions/valueserp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/valueserp-conventions.yml
- group: design
  href: https://artifacts.apis.io/valueserp/errors/valueserp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/valueserp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/valueserp/conformance/valueserp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/valueserp-conformance.yml
- group: design
  href: https://artifacts.apis.io/valueserp/lifecycle/valueserp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/valueserp-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/valueserp/changelog/valueserp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/valueserp-changelog.yml
- group: start
  href: https://artifacts.apis.io/valueserp/sandbox/valueserp-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/valueserp-sandbox.yml
- group: design
  href: https://artifacts.apis.io/valueserp/data-model/valueserp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/valueserp-data-model.yml
- group: design
  href: https://artifacts.apis.io/valueserp/webhooks/valueserp-webhooks.yml
  title: ''
  type: Webhooks
  url: webhooks/valueserp-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/valueserp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/valueserp/security/valueserp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/valueserp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/valueserp/security/valueserp-vulnerability-disclosure.yml
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
- has_sources: true
  method: derived
  name: Valueserp Finops
  primary_unit: searches/month
  service_category: ''
  slug: valueserp-finops
  template: false
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
modified: 2026-08-13
name: ValueSERP
nav: Providers
network: true
overview: 'ValueSERP publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Images API, News API, Places API, and 3 more. Tagged areas include SERP, Search Engine Results, Google Search, SEO, and Web Scraping.


  The ValueSERP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ValueSERP''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, API reference, and 34 more developer resources.'
plans:
- name: Valueserp Plans Pricing
  plan_count: 11
  slug: valueserp-plans-pricing
- name: Valueserp Price Estimates
  plan_count: 0
  slug: valueserp-price-estimates
random_paper: 23
rate_limits:
- limit_count: 11
  name: Valueserp Rate Limits
  slug: valueserp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: ValueSERP — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valueserp-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 67.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 88.8
    catalog_earned_first_party: 24.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 84.2
    contract_governance: 28.0
    contract_quality: 63.4
    developer_ergonomics: 57.7
    discoverability: 66.1
    operational_transparency: 81.6
  previous_composite: 65.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/valueserp/valueserp-2026-06-20T200802.png
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
skill_count: 5
skills:
- name: Collect SERPs in bulk with Batches and a webhook
  slug: valueserp-bulk-collect-with-batches
- name: Capture Google AI Overviews for a query
  slug: valueserp-capture-ai-overview
- name: Monitor a business in the Google local pack
  slug: valueserp-monitor-local-pack
- name: Rank-track a keyword in a specific market
  slug: valueserp-rank-track-a-keyword
- name: Track a product across Google Shopping and News
  slug: valueserp-track-shopping-and-news
slug: valueserp
tags:
- SERP
- Search Engine Results
- Google Search
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
