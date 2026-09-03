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
api_count: 3
apis:
- description: Skechers operates a direct-to-consumer digital commerce platform at skechers.com that enables online shopping for footwear, apparel, and accessories. The platform integrates with e-commerce infrastruc
  name: Skechers E-Commerce API
  slug: ecommerce-api
- description: The Skechers Plus loyalty program enables customers to earn and redeem points across all purchase channels (online, in-store, and mobile). The loyalty system integrates with the e-commerce platform, i
  name: Skechers Plus Loyalty API
  slug: loyalty-api
- description: Skechers operates over 4,700 retail stores globally across company-owned, franchise, and licensed formats. The store locator functionality provides geographic search for nearby Skechers retail locatio
  name: Skechers Store Locator API
  slug: store-locator-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/skechers-usa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skechers-usa-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skechers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skechers
- group: company
  title: ''
  type: Website
  url: https://www.skechers.com
- group: start
  title: ''
  type: Portal
  url: https://www.skechers.com/partners
- group: design
  title: ''
  type: JSONLD
  url: json-ld/skechers-usa-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/skechers-usa-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://about.skechers.com/feed
created: '2026-03-21'
description: Skechers U.S.A. is an American lifestyle and performance footwear company (Fortune 500) that designs, develops, and markets a diverse range of footwear for men, women, and children across 170+ countries. Skechers operates direct-to-consumer digital commerce through its website and mobile app, wholesale partnerships with retailers, and a global network of owned and franchised retail stores. Their digital commerce infrastructure relies on e-commerce APIs for product catalog management, inventory, order management, customer accounts, and loyalty programs.
finops:
- name: Skechers Usa Finops
  service_category: API
  slug: skechers-usa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skechers-usa.png
json_schemas:
- name: Skechers Product
  property_count: 17
  slug: skechers-usa-product
json_structures:
- name: Skechers Usa Structure
  property_count: 0
  slug: skechers-usa-structure
jsonld:
- class_count: 41
  name: Skechers Usa Context
  property_count: 1
  slug: skechers-usa-context
layout: provider
modified: '2026-05-02'
name: Skechers U.S.A.
nav: Providers
network: true
overview: 'Skechers U.S.A. publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Footwear, Retail, E-Commerce, Fortune 500, and Direct to Consumer.


  The Skechers U.S.A. catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Skechers U.S.A.''s developer surface includes developer portal, engineering blog, and 7 more developer resources.'
plans:
- name: Skechers Usa Plans Pricing
  plan_count: 3
  slug: skechers-usa-plans-pricing
press:
- date: '2026-05-25'
  title: SKECHERS | Business Wire - Via Ritzau
  url: https://via.ritzau.dk/pressemeddelelse/13951664/skechers?publisherId=90456
- date: '2026-05-25'
  title: o9 Solutions Partners With Skechers to Digitally Transform ...
  url: https://www.businesswire.com/news/home/20240122515552/en/o9-Solutions-Partners-With-Skechers-to-Digitally-Transform-the-Companys-Retail-Planning-Processes
- date: '2026-05-25'
  title: 오나인솔루션즈, 글로벌 스포츠 브랜드 스케쳐스(Skechers) ...
  url: https://o9solutions.com/ko/news/customer-case-skechers-o9-digital-brain
- date: '2026-05-25'
  title: The problem with generative AI, and how it relates to Skechers ...
  url: https://www.instagram.com/reel/DU_LgGaFSxG/
- date: '2026-05-25'
  title: 'When IR Met AI: How the Technology Is Shaping Earnings- ...'
  url: https://www.wsj.com/articles/when-ir-met-ai-how-the-technology-is-shaping-earnings-day-prep-5054a057
random_paper: 12
rate_limits:
- limit_count: 5
  name: Skechers Usa Rate Limits
  slug: skechers-usa-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Skechers U.S.A. API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: skechers-usa-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 13
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 19.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skechers-usa/refs/heads/main/screenshots/skechers-usa-2026-06-20T194019.png
security:
- kind: domain-security
  name: Skechers Usa Domain Security
  slug: skechers-usa-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Skechers Usa Vulnerability Disclosure
  slug: skechers-usa-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: skechers-usa
tags:
- Footwear
- Retail
- E-Commerce
- Fortune 500
- Direct to Consumer
- Lifestyle
website: https://www.skechers.com
---
