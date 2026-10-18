---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hello Retail Agentic Access
  operation_count: 4
  slug: hello-retail-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://core.helloretail.com
  baseurl_source: declared
  description: Retrieve weighted customer preference data for personalization.
  name: Hello Retail Customer Bias API
  slug: hello-retail-customer-bias-api
- baseURL: https://core.helloretail.com
  baseurl_source: declared
  description: Page-driven product listings with filtering and sorting.
  name: Hello Retail Pages API
  slug: hello-retail-pages-api
- baseURL: https://core.helloretail.com
  baseurl_source: declared
  description: Managed and unmanaged product recommendation requests.
  name: Hello Retail Recommendations API
  slug: hello-retail-recommendations-api
- baseURL: https://core.helloretail.com
  baseurl_source: declared
  description: On-site search across products, categories, brands, and content.
  name: Hello Retail Search API
  slug: hello-retail-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hello Retail Customer Bias API
  slug: open-hello-retail-customer-bias-api
- collection_type: open
  name: Hello Retail Customer Bias Pages API
  slug: open-hello-retail-pages-api
- collection_type: open
  name: Hello Retail Customer Bias Recommendations API
  slug: open-hello-retail-recommendations-api
- collection_type: open
  name: Hello Retail Customer Bias Search API
  slug: open-hello-retail-search-api
- collection_type: open
  name: Hello Retail API
  slug: open-hello-retail
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/plans/hello-retail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hello-retail-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/rate-limits/hello-retail-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hello-retail-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/finops/hello-retail-finops.yml
  title: ''
  type: FinOps
  url: finops/hello-retail-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://helloretail.com/en/blog/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/agentic-access/hello-retail-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hello-retail-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/security/hello-retail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hello-retail-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/authentication/hello-retail-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hello-retail-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helloretail
- group: start
  title: ''
  type: Portal
  url: https://developer.helloretail.com/
- group: company
  title: ''
  type: Website
  url: https://www.helloretail.com/
- group: start
  title: ''
  type: Signup
  url: https://app.helloretail.com/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://helloretail.com/llms.txt
created: '2025-02-06'
description: Hello Retail is a personalization and product recommendation platform for e-commerce. It provides a REST API and JavaScript SDK for integrating personalized product recommendations, search, and behavioral tracking into retail websites.
finops:
- has_sources: false
  method: generated
  name: Hello Retail Finops
  primary_unit: ''
  service_category: API
  slug: hello-retail-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hello-retail.png
layout: provider
mcp_servers:
- description: Remote MCP server at core.helloretail.com over HTTP.
  name: Hello Retail MCP Server
  slug: hello-retail
modified: '2026-10-06'
name: Hello Retail
nav: Providers
network: true
overview: 'Hello Retail publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customer Bias API, Pages API, Recommendations API, and 1 more. Tagged areas include E-Commerce, Personalization, Product Recommendations, and Retail.


  Hello Retail''s developer surface includes engineering blog, authentication, developer portal, signup flow, and 8 more developer resources.'
plans:
- name: Hello Retail Plans Pricing
  plan_count: 3
  slug: hello-retail-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Hello Retail Rate Limits
  slug: hello-retail-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 21.4
    discoverability: 66.7
    operational_transparency: 7.9
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/hello-retail/refs/heads/main/screenshots/hello-retail-2026-06-20T182627.png
security:
- kind: authentication
  name: Hello Retail Authentication
  slug: hello-retail-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hello Retail Domain Security
  slug: hello-retail-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hello-retail
tags:
- E-Commerce
- Personalization
- Product Recommendations
- Retail
website: https://www.helloretail.com/
---
