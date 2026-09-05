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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 1
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
- baseURL: https://api.platform.softwareone.com
  baseurl_source: declared
  description: Catalog item lifecycle management
  name: SoftwareOne Items API
  slug: softwareone-items-api
- baseURL: https://api.platform.softwareone.com
  baseurl_source: declared
  description: Marketplace listings
  name: SoftwareOne Listings API
  slug: softwareone-listings-api
- baseURL: https://api.platform.softwareone.com
  baseurl_source: declared
  description: Product media assets
  name: SoftwareOne Media API
  slug: softwareone-media-api
- baseURL: https://api.platform.softwareone.com
  baseurl_source: declared
  description: Product configuration parameters
  name: SoftwareOne Parameters API
  slug: softwareone-parameters-api
- baseURL: https://api.platform.softwareone.com
  baseurl_source: declared
  description: Catalog product lifecycle management
  name: SoftwareOne Products API
  slug: softwareone-products-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SoftwareOne Marketplace Platform Items API
  slug: open-softwareone-items-api
- collection_type: open
  name: SoftwareOne Marketplace Platform Listings API
  slug: open-softwareone-listings-api
- collection_type: open
  name: SoftwareOne Marketplace Platform Media API
  slug: open-softwareone-media-api
- collection_type: open
  name: SoftwareOne Marketplace Platform Parameters API
  slug: open-softwareone-parameters-api
- collection_type: open
  name: SoftwareOne Marketplace Platform Products API
  slug: open-softwareone-products-api
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
overview: 'SoftwareOne publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Items API, Listings API, Media API, and 2 more. Tagged areas include Marketplace, Software Procurement, Cloud Management, License Management, and Software-as-a-Service.


  The SoftwareOne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SoftwareOne''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Softwareone Plans Pricing
  plan_count: 3
  slug: softwareone-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Softwareone Rate Limits
  slug: softwareone-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SoftwareOne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: softwareone-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 30.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Software-as-a-Service
website: https://www.softwareone.com/
---
