---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 23
  human_in_the_loop: 3
  name: Kajabi Agentic Access
  operation_count: 77
  slug: kajabi-agentic-access
  summary_line: 77 operations · 23 acting · 3 human-in-the-loop
api_count: 21
apis:
- description: The Authentication API from Kajabi — 2 operation(s) for authentication.
  name: Kajabi Authentication API
  slug: kajabi-authentication-api
- description: The Blog posts API from Kajabi — 2 operation(s) for blog posts.
  name: Kajabi Blog posts API
  slug: kajabi-blog-posts-api
- description: The Contact Notes API from Kajabi — 2 operation(s) for contact notes.
  name: Kajabi Contact Notes API
  slug: kajabi-contact-notes-api
- description: The Contact Tags API from Kajabi — 2 operation(s) for contact tags.
  name: Kajabi Contact Tags API
  slug: kajabi-contact-tags-api
- description: The Contacts API from Kajabi — 4 operation(s) for contacts.
  name: Kajabi Contacts API
  slug: kajabi-contacts-api
- description: The Courses API from Kajabi — 2 operation(s) for courses.
  name: Kajabi Courses API
  slug: kajabi-courses-api
- description: The Custom Fields API from Kajabi — 2 operation(s) for custom fields.
  name: Kajabi Custom Fields API
  slug: kajabi-custom-fields-api
- description: The Customers API from Kajabi — 3 operation(s) for customers.
  name: Kajabi Customers API
  slug: kajabi-customers-api
- description: The Forms API from Kajabi — 5 operation(s) for forms.
  name: Kajabi Forms API
  slug: kajabi-forms-api
- description: The Kajabi Payments Payouts API from Kajabi — 2 operation(s) for kajabi payments payouts.
  name: Kajabi Kajabi Payments Payouts API
  slug: kajabi-kajabi-payments-payouts-api
- description: The Landing pages API from Kajabi — 2 operation(s) for landing pages.
  name: Kajabi Landing pages API
  slug: kajabi-landing-pages-api
- description: The Me API from Kajabi — 1 operation(s) for me.
  name: Kajabi Me API
  slug: kajabi-me-api
- description: The Offers API from Kajabi — 3 operation(s) for offers.
  name: Kajabi Offers API
  slug: kajabi-offers-api
- description: The Orders API from Kajabi — 4 operation(s) for orders.
  name: Kajabi Orders API
  slug: kajabi-orders-api
- description: The Podcasts API from Kajabi — 2 operation(s) for podcasts.
  name: Kajabi Podcasts API
  slug: kajabi-podcasts-api
- description: The Products API from Kajabi — 2 operation(s) for products.
  name: Kajabi Products API
  slug: kajabi-products-api
- description: The Purchases API from Kajabi — 5 operation(s) for purchases.
  name: Kajabi Purchases API
  slug: kajabi-purchases-api
- description: The Sites API from Kajabi — 4 operation(s) for sites.
  name: Kajabi Sites API
  slug: kajabi-sites-api
- description: The Transactions API from Kajabi — 2 operation(s) for transactions.
  name: Kajabi Transactions API
  slug: kajabi-transactions-api
- description: The Version API from Kajabi — 1 operation(s) for version.
  name: Kajabi Version API
  slug: kajabi-version-api
- description: The Webhooks API from Kajabi — 8 operation(s) for webhooks.
  name: Kajabi Webhooks API
  slug: kajabi-webhooks-api
artifact_total: 58
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kajabi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kajabi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kajabi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.kajabi.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.kajabi.com/api-reference/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Kajabi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kajabi
- group: company
  title: ''
  type: Blog
  url: https://www.kajabi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kajabi.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kajabi.com
- group: other
  title: ''
  type: X
  url: https://x.com/Kajabi
- group: commercial
  title: ''
  type: Plans
  url: plans/kajabi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kajabi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kajabi-finops.yml
created: 2026-06-12
description: Kajabi is an all-in-one creator platform that enables entrepreneurs and knowledge creators to build, market, and sell digital products including online courses, membership sites, coaching programs, and communities. The Kajabi Public API provides a RESTful interface for managing contacts, products, offers, purchases, orders, transactions, forms, webhooks, and more. API access requires OAuth 2.0 authentication and is available exclusively on the Pro plan. The API base URL is https://api.kajabi.com with versioned endpoints under /v1, and an OpenAPI specification is published in the public_api_docs GitHub repository.
examples:
- key_count: 8
  name: Kajabi Contacts Create Example
  slug: kajabi-contacts-create-example
- key_count: 8
  name: Kajabi Contacts List Example
  slug: kajabi-contacts-list-example
- key_count: 8
  name: Kajabi Offers List Example
  slug: kajabi-offers-list-example
- key_count: 8
  name: Kajabi Orders List Example
  slug: kajabi-orders-list-example
- key_count: 8
  name: Kajabi Products List Example
  slug: kajabi-products-list-example
- key_count: 8
  name: Kajabi Purchases List Example
  slug: kajabi-purchases-list-example
- key_count: 8
  name: Kajabi Transactions List Example
  slug: kajabi-transactions-list-example
- key_count: 8
  name: Kajabi Webhooks List Example
  slug: kajabi-webhooks-list-example
finops:
- name: Kajabi Finops
  service_category: ''
  slug: kajabi-finops
graphqls:
- description: 'This document describes a conceptual GraphQL schema for the Kajabi creator and online course platform. Kajabi''s public API is RESTful (base URL: `https://api.kajabi.com/v1`, OAuth 2.0 required on the '
  name: Kajabi GraphQL Schema
  slug: kajabi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kajabi.png
json_schemas:
- name: Blog Posts
  property_count: 9
  slug: blog_posts_attributes
- name: Contact Notes
  property_count: 3
  slug: contact_notes_attributes
- name: Contact Tags
  property_count: 1
  slug: contact_tags_attributes
- name: Contacts
  property_count: 17
  slug: contacts_attributes
- name: Courses
  property_count: 4
  slug: courses_attributes
- name: Custom Fields
  property_count: 4
  slug: custom_fields_attributes
- name: Customers
  property_count: 14
  slug: customers_attributes
- name: Form
  property_count: 6
  slug: form_attributes
- name: Form Submission
  property_count: 13
  slug: form_submission_attributes
- name: Hooks
  property_count: 5
  slug: hooks_attributes
- name: Landing Pages
  property_count: 5
  slug: landing_pages_attributes
- name: Me
  property_count: 4
  slug: me_attributes
- name: Offers
  property_count: 16
  slug: offers_attributes
- name: Orders
  property_count: 11
  slug: orders_attributes
- name: Podcasts
  property_count: 19
  slug: podcasts_attributes
- name: Products
  property_count: 10
  slug: products_attributes
- name: Purchases
  property_count: 17
  slug: purchases_attributes
- name: Sites
  property_count: 4
  slug: sites_attributes
- name: Transactions
  property_count: 9
  slug: transactions_attributes
- name: Website Pages
  property_count: 4
  slug: website_pages_attributes
jsonld:
- class_count: 69
  name: Kajabi Context
  property_count: 8
  slug: kajabi-context
layout: provider
modified: 2026-06-12
name: Kajabi
nav: Providers
network: true
overview: 'Kajabi publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Blog posts API, Contact Notes API, and 18 more. Tagged areas include Creator Economy, Online Courses, Memberships, E-Commerce, and Digital Products.


  The Kajabi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kajabi''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Kajabi Plans Pricing
  plan_count: 4
  slug: kajabi-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Kajabi Rate Limits
  slug: kajabi-rate-limits
rules:
- name: Kajabi API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kajabi-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.8
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 53.6
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kajabi/refs/heads/main/screenshots/kajabi-2026-06-20T183859.png
security:
- kind: authentication
  name: Kajabi Authentication
  slug: kajabi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kajabi Domain Security
  slug: kajabi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kajabi
tags:
- Creator Economy
- Online Courses
- Memberships
- E-Commerce
- Digital Products
- Contacts
- Webhooks
- Payments
website: https://www.kajabi.com
---
