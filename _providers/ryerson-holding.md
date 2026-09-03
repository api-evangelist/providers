---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ryerson-holding-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ryerson
- group: company
  title: ''
  type: Website
  url: https://www.ryerson.com
- group: other
  title: ''
  type: ECommerce
  url: https://www.ryerson.com/
- group: company
  title: ''
  type: About
  url: https://www.ryerson.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.ryerson.com/blog
- group: company
  title: ''
  type: Investors
  url: https://investors.ryerson.com
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ryerson-holding/refs/heads/main/vocabulary/ryerson-holding-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ryerson-holding/refs/heads/main/json-ld/ryerson-holding-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ryerson-holding/refs/heads/main/json-schema/ryerson-metal-product-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://www.ryerson.com/llms.txt
created: '2026-03-24'
description: Ryerson Holding Corporation is a leading value-added processor and distributor of industrial metals, with operations across the United States, Canada, Mexico, China, and Brazil. The company offers a broad range of stainless steel, aluminum, carbon steel, and alloy steels in various shapes and forms. Ryerson operates an e-commerce platform at Ryerson.com enabling online metal ordering, order status tracking, and shipment management. The company has integrated its CRM (Salesforce) with ERP (SAP) for streamlined order management and uses EDI and API-based integration for wholesale distribution operations.
examples:
- key_count: 11
  name: Ryerson Metal Product Example
  slug: ryerson-metal-product-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ryerson-holding.png
json_schemas:
- name: Ryerson Metal Product
  property_count: 11
  slug: ryerson-metal-product
json_structures:
- name: Ryerson Metal Product Structure
  property_count: 0
  slug: ryerson-metal-product-structure
jsonld:
- class_count: 0
  name: Ryerson Holding Context
  property_count: 15
  slug: ryerson-holding-context
layout: provider
modified: '2026-05-02'
name: Ryerson Holding
nav: Providers
network: true
overview: 'Ryerson Holding is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial Metals, Manufacturing, Metal Distribution, and Steel.


  The Ryerson Holding catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ryerson Holding''s developer surface includes engineering blog and 10 more developer resources.'
press:
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1481582/000095017024118271/ryi-20241029.htm
- date: '2026-05-25'
  title: SOUNW SoundHound warrants face uncertainty as quarterly ...
  url: https://www.ibhe.org/first-dry/SOUNW-SoundHound-warrants-face-uncertainty-as-quarterly-earnings-data-remains-unavailable-to-investors-10-11208
- date: '2026-05-25'
  title: 'Earnings call transcript: Ryerson Holding Corp sees robust ...'
  url: https://www.investing.com/news/transcripts/earnings-call-transcript-ryerson-holding-corp-sees-robust-q1-2026-growth-with-olympic-steel-integration-93CH-4669757
- date: '2026-05-25'
  title: Ryerson Holding Corporation Stockholders and Olympic ...
  url: https://www.prnewswire.com/news-releases/ryerson-holding-corporation-stockholders-and-olympic-steel-inc-shareholders-approve-proposals-related-to-pending-transaction-302686611.html
- date: '2026-05-25'
  title: Ryerson targets $120M in annual synergies post-Olympic ...
  url: https://seekingalpha.com/news/4554819-ryerson-targets-120m-in-annual-synergies-post-olympic-steel-merger-as-demand-rebounds
random_paper: 18
rules:
- effective_rule_count: 5
  extends: []
  name: Ryerson Holding API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ryerson-holding-jsonschema-spectral-rules
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 76.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 48.1
    governance: 25.0
    operational_transparency: 0.0
  previous_composite: 10.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Ryerson Holding Domain Security
  slug: ryerson-holding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ryerson-holding
tags:
- Industrial Metals
- Manufacturing
- Metal Distribution
- Steel
website: https://www.ryerson.com
---
