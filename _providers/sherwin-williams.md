---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Sherwin-Williams Supplier API enables B2B partners to integrate supply chain workflows, manage purchase orders, submit invoices, and exchange product and inventory data with Sherwin-Williams enter
  name: Sherwin-Williams Supplier API
  slug: sherwin-williams-supplier-api
- description: Sherwin-Williams EDI integration capabilities enable trading partners to exchange electronic data interchange (EDI) documents including purchase orders, invoices, advance ship notices, and inventory f
  name: Sherwin-Williams EDI Integration
  slug: sherwin-williams-edi-integration
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sherwin-williams-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sherwin-williams
- group: start
  title: ''
  type: Supplier Portal
  url: https://suppliers.sherwin-williams.com/
- group: company
  title: ''
  type: Partner Program
  url: https://www.sherwin-williams.com/home-builders/services/paint-technology-and-application
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sherwin-williams.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sherwin-williams.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sherwin-williams-co
- group: company
  title: ''
  type: Website
  url: https://www.sherwin-williams.com
created: '2025-03-01'
description: The Sherwin-Williams Company is a global leader in the paint and coatings industry, offering products for consumers, contractors, industrial clients, and commercial builders. Sherwin-Williams provides B2B API and EDI integration capabilities for suppliers and trading partners to connect with their enterprise supply chain and retail operations.
examples:
- key_count: 3
  name: Sherwin Williams Supplier Order Example
  slug: sherwin-williams-supplier-order-example
finops:
- name: Sherwin Williams Finops
  service_category: B2B Supply Chain
  slug: sherwin-williams-finops
image: https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Sherwin-Williams_logo.svg/2560px-Sherwin-Williams_logo.svg.png
json_schemas:
- name: Sherwin-Williams Paint Product
  property_count: 22
  slug: sherwin-williams-product
- name: Sherwin-Williams Supplier
  property_count: 15
  slug: sherwin-williams-supplier
json_structures:
- name: Sherwin Williams Product Structure
  property_count: 0
  slug: sherwin-williams-product-structure
jsonld:
- class_count: 39
  name: Sherwin Williams Context
  property_count: 6
  slug: sherwin-williams-context
layout: provider
modified: '2026-05-02'
name: Sherwin-Williams
nav: Providers
network: true
overview: 'Sherwin-Williams publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Construction, Fortune 500, Paints, and Retail.


  The Sherwin-Williams catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Sherwin Williams Plans Pricing
  plan_count: 1
  slug: sherwin-williams-plans-pricing
press:
- date: '2026-05-25'
  title: 'Shermin-Williams'' AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/shermin-williams-ai-strategy-analysis-of-dominance-in-coatings/
- date: '2026-05-25'
  title: Sherwin-Williams Launches App Powered by AI Technology
  url: https://www.pcimag.com/articles/112388-sherwin-williams-launches-app-powered-by-ai-technology
- date: '2026-05-25'
  title: The Power of AI in Interior Design | Episode 7
  url: https://www.sherwin-williams.com/en-us/color/colormixology/the-power-of-ai-in-interior-design
- date: '2026-05-25'
  title: Logistics pressures intensify. Sherwin-Williams improved ...
  url: https://www.facebook.com/internationalfinancemagazine/posts/logistics-pressures-intensify-sherwin-williams-improved-freight-efficiency-11-wi/1597361705729653/
- date: '2026-05-25'
  title: Sherwin-Williams Positions Itself as the One Partner for ...
  url: https://www.prnewswire.com/news-releases/sherwin-williams-positions-itself-as-the-one-partner-for-data-center-construction-302764452.html
random_paper: 55
rate_limits:
- limit_count: 1
  name: Sherwin Williams Rate Limits
  slug: sherwin-williams-rate-limits
rules:
- name: Sherwin-Williams API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sherwin-williams-jsonschema-spectral-rules
- name: Sherwin-Williams API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: sherwin-williams-rules
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 29.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 33.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sherwin-williams/refs/heads/main/screenshots/sherwin-williams-2026-06-20T193801.png
security:
- kind: domain-security
  name: Sherwin Williams Domain Security
  slug: sherwin-williams-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sherwin-williams
tags:
- B2B
- Construction
- Fortune 500
- Paints
- Retail
- Supply Chain
website: https://www.sherwin-williams.com
---
