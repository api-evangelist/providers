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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hello Retail Agentic Access
  operation_count: 4
  slug: hello-retail-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 4
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
artifact_total: 11
collections:
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
random_paper: 63
rate_limits:
- limit_count: 5
  name: Hello Retail Rate Limits
  slug: hello-retail-rate-limits
score:
  band: thin
  composite: 37.9
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
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
