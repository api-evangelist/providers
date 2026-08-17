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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: E-commerce integration API for the Tempur-Pedic brand enabling retailers, affiliates, and platform partners to access product catalogs, check inventory, manage orders, and track shipments for Tempur-P
  name: Tempur-Pedic E-Commerce API
  slug: tempur-pedic-e-commerce-api
- description: E-commerce integration API for the Sealy brand providing access to product catalogs, availability, and order management for Sealy Posturepedic, Sealy, and Cocoon mattress product lines across retail a
  name: Sealy E-Commerce API
  slug: sealy-e-commerce-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tempur-sealy-international-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempur-sealy-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tempur-pedic
- group: company
  title: ''
  type: Website
  url: https://www.tempursealy.com
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.tempursealy.com
- group: company
  title: ''
  type: Press Room
  url: https://www.tempursealy.com/news
- group: other
  title: ''
  type: Corporate Responsibility
  url: https://www.tempursealy.com/sustainability
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tempur-sealy-international-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tempur-sealy-international-product-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tempur-sealy-international-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://somnigroup.com/newsroom/default.aspx
created: '2026-03-24'
description: Tempur Sealy International is one of the world's largest bedding providers, developing, manufacturing, marketing, and distributing bedding products under the Tempur-Pedic, Sealy, and Stearns & Foster brands. As a Fortune 500 manufacturer and retailer, the company operates e-commerce platforms and provides retailer integration APIs for product catalogs, inventory, and order management.
examples:
- key_count: 2
  name: Tempur Sealy International Product Example
  slug: tempur-sealy-international-product-example
finops:
- name: Tempur Sealy International Finops
  service_category: API
  slug: tempur-sealy-international-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempur-sealy-international.png
json_schemas:
- name: Tempur Sealy International Product
  property_count: 14
  slug: tempur-sealy-international-product
json_structures:
- name: Tempur Sealy International Product Structure
  property_count: 0
  slug: tempur-sealy-international-product-structure
jsonld:
- class_count: 6
  name: Tempur Sealy International Context
  property_count: 12
  slug: tempur-sealy-international-context
layout: provider
modified: '2026-05-03'
name: Tempur Sealy International
nav: Providers
network: true
overview: 'Tempur Sealy International publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bedding, Manufacturing, E-Commerce, Retail, and Fortune 500.


  The Tempur Sealy International catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tempur Sealy International''s developer surface includes engineering blog and 10 more developer resources.'
plans:
- name: Tempur Sealy International Plans Pricing
  plan_count: 3
  slug: tempur-sealy-international-plans-pricing
press:
- date: '2026-05-25'
  title: Terms of Use
  url: https://www.tempursealy.com/terms-of-use/
- date: '2026-05-25'
  title: National Sleep Foundation and Tempur-Pedic Announce ...
  url: https://www.prnewswire.com/news-releases/national-sleep-foundation-and-tempur-pedic-announce-new-research-collaboration-302701117.html
- date: '2026-05-25'
  title: Tempur Sealy International, Inc., TPX
  url: https://s204.q4cdn.com/436357164/files/doc_financials/2023/q4/February-2024-FINAL-TPX-Investor-Presentation.pdf
- date: '2026-05-25'
  title: Tempur Sealy International, Inc. to Change its Name to ...
  url: https://www.prnewswire.com/news-releases/tempur-sealy-international-inc-to-change-its-name-to-somnigroup-international-inc-302368965.html
- date: '2026-05-25'
  title: Tempur Sealy integrates A.I. in newest ActiveBreeze smart ...
  url: https://www.furnituretoday.com/bedding-manufacturers/tempur-sealy-integrates-a-i-in-newest-activebreeze-smart-bed/
random_paper: 19
rate_limits:
- limit_count: 5
  name: Tempur Sealy International Rate Limits
  slug: tempur-sealy-international-rate-limits
rules:
- name: Tempur Sealy International API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tempur-sealy-international-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 17.7
    developer_ergonomics: 2.2
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 7.9
  previous_composite: 24.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tempur-sealy-international/refs/heads/main/screenshots/tempur-sealy-international-2026-06-20T195104.png
security:
- kind: domain-security
  name: Tempur Sealy International Domain Security
  slug: tempur-sealy-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tempur Sealy International Vulnerability Disclosure
  slug: tempur-sealy-international-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tempur-sealy-international
tags:
- Bedding
- Manufacturing
- E-Commerce
- Retail
- Fortune 500
- Consumer Goods
website: https://www.tempursealy.com
---
