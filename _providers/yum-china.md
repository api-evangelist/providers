---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: The KFC China Super App is Yum China's digital ordering and loyalty platform providing members with digital ordering, personalized recommendations, loyalty points, and an AI ordering assistant. The pl
  name: KFC China Super App Platform
  slug: kfc-super-app
- description: Pizza Hut China's digital ordering and loyalty platform, part of Yum China's integrated membership ecosystem with shared loyalty infrastructure.
  name: Pizza Hut China Digital Platform
  slug: pizza-hut-digital
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yum-china-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yumchina
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yum-china
- group: company
  title: ''
  type: Website
  url: https://www.yumchina.com
- group: company
  title: ''
  type: Investors
  url: https://ir.yumchina.com
- group: company
  title: ''
  type: Blog
  url: https://www.yumchina.com/en/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yumchina.com/en/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/yum-china-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yum-china-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yum-china-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/yum-china-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/yum-china-context.jsonld
created: '2026-03-21'
description: Yum China Holdings is the largest restaurant company in China by system sales, operating KFC, Pizza Hut, Taco Bell, Lavazza, Little Sheep, and Huang Ji Huang restaurants. As the exclusive licensee of Yum! Brands in mainland China, Yum China serves over 16,000 restaurants across China and operates Super App platforms with over 590 million loyalty members.
features:
- name: Digital Ordering
- name: Super App Platform
- name: AI Ordering Assistant
- name: Q-Smart AI Restaurant Manager Assistant
- name: Loyalty Programs (590M+ Members)
- name: Super Brain AI Operations
- name: KCOFFEE
- name: Delivery Management
- name: Smart Kitchen Operations
finops:
- name: Yum China Finops
  service_category: API
  slug: yum-china-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yum-china.png
jsonld:
- class_count: 10
  name: Yum China Context
  property_count: 21
  slug: yum-china-context
layout: provider
modified: '2026-06-03'
name: Yum China
nav: Providers
network: true
overview: 'Yum China publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Fast Food, Quick Service Restaurant, Digital Ordering, and Loyalty.


  The Yum China catalog on APIs.io includes 1 JSON-LD context.


  Yum China''s developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Yum China Plans Pricing
  plan_count: 3
  slug: yum-china-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Yum China Rate Limits
  slug: yum-china-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 10.5
  previous_composite: 16.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yum-china/refs/heads/main/screenshots/yum-china-2026-06-20T201757.png
security:
- kind: domain-security
  name: Yum China Domain Security
  slug: yum-china-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yum-china
solutions:
- name: China Restaurant Operations
- name: Digital Customer Engagement
- name: AI-Powered Store Management
- name: Franchise Technology Platform
tags:
- Restaurant
- Fast Food
- Quick Service Restaurant
- Digital Ordering
- Loyalty
- China
- Food Technology
website: https://www.yumchina.com
---
