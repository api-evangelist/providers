---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blissfully Agentic Access
  operation_count: 6
  slug: blissfully-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 7
apis:
- description: Delivers actionable pricing insights including fair price predictions and negotiation guidance tailored to the buyer's specific requirements, contract size, and vendor relationship. Powered by Vendr's
  name: Vendr Pricing API
  slug: vendr-pricing-api
- description: Enables communication of detailed purchasing needs in text or file format, whether for complex enterprise software requirements or uploaded quotes from vendors. Supports both simple and complex procur
  name: Vendr Scope API
  slug: vendr-scope-api
- description: Facilitates creation and management of webhooks for monitoring Vendr's data processing events, enabling integration with procurement workflows and notification systems.
  name: Vendr Webhooks API
  slug: vendr-webhooks-api
- baseURL: https://api.vendr.com/v1
  baseurl_source: spec
  description: Pricing intelligence and benchmarks
  name: Blissfully Pricing API
  slug: blissfully-pricing-api
- baseURL: https://api.vendr.com/v1
  baseurl_source: spec
  description: Software product catalog entries
  name: Blissfully Products API
  slug: blissfully-products-api
- baseURL: https://api.vendr.com/v1
  baseurl_source: spec
  description: Software vendors and their product portfolios
  name: Blissfully Vendors API
  slug: blissfully-vendors-api
- baseURL: https://api.vendr.com/v1
  baseurl_source: spec
  description: Webhook management for event notifications
  name: Blissfully Webhooks API
  slug: blissfully-webhooks-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vendr Catalog Pricing API
  slug: open-blissfully-pricing-api
- collection_type: open
  name: Vendr Catalog Pricing Products API
  slug: open-blissfully-products-api
- collection_type: open
  name: Vendr Catalog Pricing Vendors API
  slug: open-blissfully-vendors-api
- collection_type: open
  name: Vendr Catalog Pricing Webhooks API
  slug: open-blissfully-webhooks-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/vendr/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blissfully-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/blissfully-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blissfully-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blissfully-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blissfully
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blissfully
- group: company
  title: ''
  type: Website
  url: https://www.vendr.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendr.com
- group: start
  title: ''
  type: Signup
  url: https://www.vendr.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vendr.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vendr.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.vendr.com/blog
- group: operate
  title: ''
  type: RateLimits
  url: ''
- group: auth
  title: ''
  type: Authentication
  url: https://developers.vendr.com
created: '2026-03-27'
description: Blissfully was a SaaS management platform providing SaaS discovery, spend optimization, and workflow automation for IT and finance teams. Blissfully was acquired by Vendr in 2022 and integrated into the Vendr platform. Vendr is now a leading SaaS buying and management platform that helps companies control software spend through vendor negotiations, pricing intelligence, and procurement automation. The Vendr API provides access to software catalog data, pricing intelligence, and scope management capabilities.
examples:
- key_count: 5
  name: Blissfully Pricing Response Example
  slug: blissfully-pricing-response-example
- key_count: 7
  name: Blissfully Product Example
  slug: blissfully-product-example
- key_count: 4
  name: Blissfully Vendor Example
  slug: blissfully-vendor-example
- key_count: 4
  name: Blissfully Webhook Example
  slug: blissfully-webhook-example
features:
- description: Structured product catalog attributes derived from thousands of unstructured software quotes, covering product breadth, add-ons, and feature comparisons.
  name: Catalog API
- description: Actionable pricing insights including fair price predictions and negotiation guidance tailored to specific buyer requirements and contract sizes.
  name: Pricing API
- description: Communication of detailed purchasing needs in text or file format for complex enterprise software procurement requirements.
  name: Scope API
- description: Creation and management of webhooks for monitoring Vendr data processing events and integrating with procurement workflows.
  name: Webhooks API
- description: Model Context Protocol (MCP) integration options including Claude Desktop extension, GitHub-based local setup, and custom AI app configuration.
  name: MCP Integration
- description: Pricing benchmarks powered by Vendr's database of real software purchases across thousands of companies and vendors.
  name: SaaS Benchmarking
finops:
- name: Blissfully Finops
  service_category: SaaS Management / Procurement
  slug: blissfully-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blissfully.png
json_schemas:
- name: PricingResponse
  property_count: 5
  slug: blissfully-pricing-response
- name: Product
  property_count: 7
  slug: blissfully-product
- name: Vendor
  property_count: 4
  slug: blissfully-vendor
- name: Webhook
  property_count: 4
  slug: blissfully-webhook
json_structures:
- name: Blissfully Pricing Response Structure
  property_count: 5
  slug: blissfully-pricing-response-structure
- name: Blissfully Product Structure
  property_count: 7
  slug: blissfully-product-structure
- name: Blissfully Vendor Structure
  property_count: 4
  slug: blissfully-vendor-structure
- name: Blissfully Webhook Structure
  property_count: 4
  slug: blissfully-webhook-structure
jsonld:
- class_count: 6
  name: Blissfully Context
  property_count: 14
  slug: blissfully-context
layout: provider
modified: '2026-05-19'
name: Blissfully
nav: Providers
network: true
overview: 'Blissfully publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pricing API, Products API, Vendors API, and 1 more. Tagged areas include Procurement, SaaS Discovery, SaaS Management, Software Procurement, and Spend Optimization.


  The Blissfully catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Blissfully''s developer surface includes authentication, documentation, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Blissfully Plans Pricing
  plan_count: 2
  slug: blissfully-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Blissfully Rate Limits
  slug: blissfully-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Blissfully API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: blissfully-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Blissfully API Rules
  rule_count: 32
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 18
  slug: blissfully-spectral-rules
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.5
    catalog_earned_first_party: 0.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 13.6
    contract_quality: 22.4
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blissfully/refs/heads/main/screenshots/blissfully-2026-06-20T173353.png
security:
- kind: authentication
  name: Blissfully Authentication
  slug: blissfully-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blissfully Domain Security
  slug: blissfully-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Blissfully Trust Center
  slug: blissfully-trust-center
  summary_line: SOC 2, GDPR
slug: blissfully
tags:
- Procurement
- SaaS Discovery
- SaaS Management
- Software Procurement
- Spend Optimization
- Vendor Management
use_cases:
- description: Procurement teams access fair price benchmarks and negotiation guidance before and during software vendor negotiations.
  name: Software Pricing Intelligence
- description: Finance and IT teams gain visibility into software spend and identify optimization opportunities across the SaaS portfolio.
  name: SaaS Spend Optimization
- description: AI applications integrate Vendr catalog and pricing data via MCP or API to provide intelligent software procurement recommendations.
  name: AI-Powered Procurement
- description: Enterprise procurement platforms integrate Vendr data to enrich vendor records with pricing benchmarks and product catalog attributes.
  name: Vendor Management Integration
- description: Webhook integrations notify procurement workflows of contract renewal events and pricing change signals from the Vendr platform.
  name: Contract Renewal Automation
website: https://www.vendr.com
---
