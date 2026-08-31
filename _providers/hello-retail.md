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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hello Retail Agentic Access
  operation_count: 4
  slug: hello-retail-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: Retrieve weighted customer preference data for personalization.
  name: Hello Retail Customer Bias API
  slug: hello-retail-customer-bias-api
- description: Page-driven product listings with filtering and sorting.
  name: Hello Retail Pages API
  slug: hello-retail-pages-api
- description: Managed and unmanaged product recommendation requests.
  name: Hello Retail Recommendations API
  slug: hello-retail-recommendations-api
- description: On-site search across products, categories, brands, and content.
  name: Hello Retail Search API
  slug: hello-retail-search-api
artifact_total: 16
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hello-retail-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hello-retail-domain-security.yml
- group: auth
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
- name: Hello Retail Finops
  service_category: API
  slug: hello-retail-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hello-retail.png
layout: provider
modified: '2026-05-19'
name: Hello Retail
nav: Providers
network: true
overview: 'Hello Retail publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customer Bias API, Pages API, Recommendations API, and 1 more. Tagged areas include E-Commerce, Personalization, Product Recommendations, and Retail.


  Hello Retail''s developer surface includes authentication, developer portal, signup flow, and 5 more developer resources.'
plans:
- name: Hello Retail Plans Pricing
  plan_count: 3
  slug: hello-retail-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Hello Retail Rate Limits
  slug: hello-retail-rate-limits
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.7
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
