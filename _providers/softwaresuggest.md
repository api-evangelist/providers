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
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: 'The SoftwareSuggest software catalog is a browsable and searchable index of over 50,000 B2B software products across 800+ categories. Users can filter by category, features, pricing model, deployment '
  name: SoftwareSuggest Software Catalog
  slug: software-catalog
- description: The SoftwareSuggest affiliate program is a CPL (cost-per-lead) based partner program where affiliates earn commissions by driving verified leads to the platform. Affiliates place tracking links or ban
  name: SoftwareSuggest Affiliate Program
  slug: affiliate-program
- description: SoftwareSuggest appears on the Datarade data marketplace as a business data provider offering software market intelligence, product reviews, and B2B software adoption data. Organizations can contact S
  name: SoftwareSuggest Data Products
  slug: data-marketplace
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/softwaresuggest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.softwaresuggest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.softwaresuggest.com/all-categories
- group: docs
  title: ''
  type: Documentation
  url: https://www.softwaresuggest.com/vendors
- group: docs
  title: ''
  type: Documentation
  url: https://www.softwaresuggest.com/vendors/guidelines
- group: start
  title: ''
  type: Portal
  url: https://www.softwaresuggest.com/vendorsportal/index.php?r=site/login
- group: other
  title: ''
  type: Affiliate
  url: https://www.softwaresuggest.com/affiliates
- group: company
  title: ''
  type: Blog
  url: https://www.softwaresuggest.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.softwaresuggest.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.softwaresuggest.com/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/softwaresuggest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/softwaresuggest
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/SoftwareSuggest/
created: '2025-01-01'
description: SoftwareSuggest is a business software discovery and recommendation platform that helps organizations find, compare, and select the right software solutions for their needs. Founded in 2014 by AppItSimple Infotek Pvt. Ltd. and headquartered in Ahmedabad, India, the platform covers over 800 software categories, lists more than 50,000 software products, and hosts over 40,000 verified user reviews. The platform serves both software buyers looking to evaluate and purchase solutions and software vendors seeking qualified leads and market visibility. SoftwareSuggest does not currently publish a public developer API but operates as a data provider via marketplaces such as Datarade for business data products.
examples:
- key_count: 17
  name: Softwaresuggest Product Listing Example
  slug: softwaresuggest-product-listing-example
- key_count: 14
  name: Softwaresuggest Review Example
  slug: softwaresuggest-review-example
finops:
- name: Softwaresuggest Finops
  service_category: API
  slug: softwaresuggest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/softwaresuggest.png
json_schemas:
- name: Product Listing
  property_count: 17
  slug: softwaresuggest-product-listing
- name: User Review
  property_count: 14
  slug: softwaresuggest-review
json_structures:
- name: Softwaresuggest Product Listing Structure
  property_count: 0
  slug: softwaresuggest-product-listing-structure
jsonld:
- class_count: 36
  name: Softwaresuggest Context
  property_count: 4
  slug: softwaresuggest-context
layout: provider
modified: '2026-07-25'
name: SoftwareSuggest
nav: Providers
network: true
overview: 'SoftwareSuggest publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Software Discovery, Business Software, SaaS, Software Reviews, and B2B.


  The SoftwareSuggest catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SoftwareSuggest''s developer surface includes documentation, developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Softwaresuggest Plans Pricing
  plan_count: 3
  slug: softwaresuggest-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Softwaresuggest Rate Limits
  slug: softwaresuggest-rate-limits
rules:
- name: SoftwareSuggest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: softwaresuggest-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 37.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Softwaresuggest Domain Security
  slug: softwaresuggest-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: softwaresuggest
tags:
- Software Discovery
- Business Software
- SaaS
- Software Reviews
- B2B
website: https://www.softwaresuggest.com/
---
