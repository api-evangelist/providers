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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pepsico Agentic Access
  operation_count: 1
  slug: pepsico-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Food operations
  name: PepsiCo Food API
  slug: pepsico-food-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PepsiCo Food API
  slug: open-pepsico-food-api
- collection_type: open
  name: PepsiCo API
  slug: open-pepsico-pepsico-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pepsico-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pepsico-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pepsico-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pepsico
- group: company
  title: ''
  type: Website
  url: https://www.pepsico.com
created: '2026-03-21'
description: PepsiCo is one of the world's largest food and beverage companies, with a portfolio of brands including Pepsi-Cola, Mountain Dew, Frito-Lay, Quaker, Tropicana, and Gatorade.
finops:
- name: Pepsico Finops
  service_category: B2B Integration
  slug: pepsico-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pepsico.png
layout: provider
modified: '2026-05-19'
name: PepsiCo
nav: Providers
network: true
overview: 'PepsiCo publishes 1 API on the [APIs.io](https://apis.io/) network: Food API. Tagged areas include Beverages, Food, Retail, Supply Chain, and Fortune 100.


  PepsiCo''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Pepsico Plans Pricing
  plan_count: 1
  slug: pepsico-plans-pricing
press:
- date: '2026-05-25'
  title: Stories | PepsiCo Newsroom
  url: https://www.pepsico.com/en/newsroom/stories-category
- date: '2026-05-25'
  title: PepsiCo Announces Industry-First AI and Digital Twin ...
  url: https://www.prnewswire.com/news-releases/pepsico-announces-industry-first-ai-and-digital-twin-collaboration-with-siemens-and-nvidia-302653851.html
- date: '2026-05-25'
  title: PepsiCo is deploying AI across its operations in China to ...
  url: https://www.facebook.com/bloombergbusiness/posts/pepsico-is-deploying-ai-across-its-operations-in-china-to-improve-efficiency-rea/1355931753059581/
- date: '2026-05-25'
  title: PepsiCo Deepens AI Capabilities with Google Cloud
  url: https://www.googlecloudpresscorner.com/2026-04-22-PepsiCo-Deepens-AI-Capabilities-with-Google-Cloud
- date: '2026-05-25'
  title: PepsiCo Announces Industry-First AI and Digital Twin ...
  url: https://www.pepsico.com/newsroom/press-releases/2025/pepsico-announces-industry-first-ai-and-digital-twin-collaboration-with-siemens-and-nvidia
random_paper: 20
rate_limits:
- limit_count: 1
  name: Pepsico Rate Limits
  slug: pepsico-rate-limits
score:
  band: thin
  composite: 26.3
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 58.7
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pepsico/refs/heads/main/screenshots/pepsico-2026-06-20T191557.png
security:
- kind: authentication
  name: Pepsico Authentication
  slug: pepsico-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pepsico Domain Security
  slug: pepsico-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pepsico
tags:
- Beverages
- Food
- Retail
- Supply Chain
- Fortune 100
website: https://www.pepsico.com
---
