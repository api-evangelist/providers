---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 0
  human_in_the_loop: 0
  name: Home Depot Agentic Access
  operation_count: 1
  slug: home-depot-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Retail operations
  name: home-depot Retail API
  slug: home-depot-retail-api
artifact_total: 9
collections:
- collection_type: open
  name: Home Depot API
  slug: open-home-depot-home-depot-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/home-depot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/home-depot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/home-depot-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/homedepot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-home-depot
description: The Home Depot is the world's largest home improvement retailer, offering tools, construction products, appliances, and services through stores, websites, and apps in the United States, Canada, and Mexico.
finops:
- name: Home Depot Finops
  service_category: Retail / E-Commerce
  slug: home-depot-finops
graphqls:
- description: This conceptual GraphQL schema represents the Home Depot retail API domain, modeling the product catalog, pricing, inventory, store information, project services, and loyalty programs available throug
  name: Home Depot GraphQL Schema
  slug: home-depot-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/home-depot.png
layout: provider
modified: '2026-05-19'
name: home-depot
nav: Providers
network: true
overview: 'home-depot publishes 1 API on the [APIs.io](https://apis.io/) network: Retail API. Tagged areas include Fortune 100.


  home-depot''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Home Depot Plans Pricing
  plan_count: 1
  slug: home-depot-plans-pricing
press:
- date: '2026-05-25'
  title: The Home Depot Launches AI-Powered Material Lists to ...
  url: https://corporate.homedepot.com/news/company/home-depot-launches-ai-powered-material-lists-help-pros-save-time-building-complete
- date: '2026-05-25'
  title: 'Home Depot Uses AI Agents: 10 Ways to Use AI [In-Depth ...'
  url: https://www.klover.ai/home-depot-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025/
- date: '2026-05-25'
  title: The Home Depot and Google Cloud Launch Agentic AI ...
  url: https://corporate.homedepot.com/news/partnerships/home-depot-and-google-cloud-launch-agentic-ai-tools-help-customers-and-associates
- date: '2026-05-25'
  title: The Home Depot Delivers Customer Support Four Times ...
  url: https://www.prnewswire.com/news-releases/the-home-depot-delivers-customer-support-four-times-faster-using-google-clouds-gemini-enterprise-for-customer-experience-302749232.html
- date: '2026-05-25'
  title: The Home Depot Introduces Magic Apron, a Suite of ...
  url: https://ir.homedepot.com/news-releases/2025/03-06-2025-130241718
random_paper: 50
rate_limits:
- limit_count: 1
  name: Home Depot Rate Limits
  slug: home-depot-rate-limits
score:
  band: thin
  composite: 33.5
  delta: -0.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.2
    developer_ergonomics: 10.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/home-depot/refs/heads/main/screenshots/home-depot-2026-06-20T182823.png
security:
- kind: authentication
  name: Home Depot Authentication
  slug: home-depot-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Home Depot Domain Security
  slug: home-depot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: home-depot
tags:
- Fortune 100
---
