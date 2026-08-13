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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 8
apis:
- description: The SoftwareOne Marketplace Platform API provides programmatic access to the marketplace catalog, enabling clients and partners to browse products, manage subscriptions, track orders, and access billi
  name: SoftwareOne Marketplace Platform API
  slug: marketplace-platform-api
- description: APIs for tracking and optimizing cloud spend across AWS, Azure, and Google Cloud environments. Provides usage data, cost analytics, rightsizing recommendations, and reservation management capabilities
  name: SoftwareOne Cloud Spend Optimization API
  slug: cloud-spend-optimization
- description: APIs for software asset management (SAM) workflows including license inventory, compliance reporting, entitlement reconciliation, and vendor audit preparation across on-premises and cloud software est
  name: SoftwareOne Software Asset Management API
  slug: software-asset-management
- description: Catalog item lifecycle management
  name: SoftwareOne Items API
  slug: softwareone-items-api
- description: Marketplace listings
  name: SoftwareOne Listings API
  slug: softwareone-listings-api
- description: Product media assets
  name: SoftwareOne Media API
  slug: softwareone-media-api
- description: Product configuration parameters
  name: SoftwareOne Parameters API
  slug: softwareone-parameters-api
- description: Catalog product lifecycle management
  name: SoftwareOne Products API
  slug: softwareone-products-api
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/softwareone-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/softwareone-platform
- group: company
  title: ''
  type: Website
  url: https://www.softwareone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.platform.softwareone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.softwareone.com/en/solutions
- group: company
  title: ''
  type: Partners
  url: https://www.softwareone.com/en/partners
- group: company
  title: ''
  type: Blog
  url: https://www.softwareone.com/en/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/softwareone
- group: other
  title: ''
  type: X
  url: https://twitter.com/SoftwareOne
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.platform.softwareone.com/llms.txt
created: '2025-02-17'
description: SoftwareOne is a global software and cloud solutions provider that helps organizations acquire, manage, and optimize their technology investments. The SoftwareOne Marketplace Platform is a comprehensive digital marketplace connecting vendors and clients, enabling software procurement, license management, cloud spend optimization, and partner ecosystem integration. The platform exposes REST APIs for clients and partners to automate software purchasing, subscription management, reporting, and catalog operations.
examples:
- key_count: 10
  name: Softwareone Order Example
  slug: softwareone-order-example
- key_count: 13
  name: Softwareone Subscription Example
  slug: softwareone-subscription-example
finops:
- name: Softwareone Finops
  service_category: API
  slug: softwareone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/softwareone.png
json_schemas:
- name: Order
  property_count: 10
  slug: softwareone-order
- name: Subscription
  property_count: 13
  slug: softwareone-subscription
json_structures:
- name: Softwareone Order Structure
  property_count: 0
  slug: softwareone-order-structure
jsonld:
- class_count: 30
  name: Softwareone Context
  property_count: 5
  slug: softwareone-context
layout: provider
modified: '2026-05-02'
name: SoftwareOne
nav: Providers
network: true
overview: 'SoftwareOne publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Items API, Listings API, Media API, and 2 more. Tagged areas include Marketplace, Software Procurement, Cloud Management, License Management, and SaaS.


  The SoftwareOne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SoftwareOne''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Softwareone Plans Pricing
  plan_count: 3
  slug: softwareone-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 5
  name: Softwareone Rate Limits
  slug: softwareone-rate-limits
rules:
- name: SoftwareOne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: softwareone-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 61.2
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 37.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/softwareone/refs/heads/main/screenshots/softwareone-2026-06-20T194144.png
security:
- kind: domain-security
  name: Softwareone Domain Security
  slug: softwareone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: softwareone
tags:
- Marketplace
- Software Procurement
- Cloud Management
- License Management
- SaaS
website: https://www.softwareone.com/
---
