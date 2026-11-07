---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 0
  name: Suger Agentic Access
  operation_count: 106
  slug: suger-agentic-access
  summary_line: 106 operations · 63 acting
api_count: 1
apis:
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Billing resources, such as addon, invoice, payment, etc.
  name: Suger Billing API
  slug: suger-billing-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Buyer resources
  name: Suger Buyer API
  slug: suger-buyer-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Contact resources
  name: Suger Contact API
  slug: suger-contact-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Entitlement resources
  name: Suger Entitlement API
  slug: suger-entitlement-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Usage Metering resources
  name: Suger Metering API
  slug: suger-metering-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Notification resources
  name: Suger Notification API
  slug: suger-notification-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Offer resources
  name: Suger Offer API
  slug: suger-offer-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Product resources
  name: Suger Product API
  slug: suger-product-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to revenue or usage metering Report resources
  name: Suger Report API
  slug: suger-report-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: Access to Suger Support ticket resources
  name: Suger Support API
  slug: suger-support-api
- baseURL: https://api.suger.cloud
  baseurl_source: declared
  description: The Org API from Suger — 2 operation(s) for org.
  name: Suger Org API
  slug: suger-org-api
artifact_total: 51
collections:
- collection_type: postman
  name: Suger API API
  slug: postman-suger-api-api
- collection_type: postman
  name: Suger API Billing API
  slug: postman-suger-billing-api
- collection_type: postman
  name: Suger API Buyer API
  slug: postman-suger-buyer-api
- collection_type: postman
  name: Suger API Contact API
  slug: postman-suger-contact-api
- collection_type: postman
  name: Suger API Entitlement API
  slug: postman-suger-entitlement-api
- collection_type: postman
  name: Suger API Metering API
  slug: postman-suger-metering-api
- collection_type: postman
  name: Suger API Notification API
  slug: postman-suger-notification-api
- collection_type: postman
  name: Suger API Offer API
  slug: postman-suger-offer-api
- collection_type: postman
  name: Suger API Product API
  slug: postman-suger-product-api
- collection_type: postman
  name: Suger API Report API
  slug: postman-suger-report-api
- collection_type: postman
  name: Suger API Support API
  slug: postman-suger-support-api
- collection_type: open
  name: Suger API API
  slug: open-suger-api-api
- collection_type: open
  name: Suger API Billing API
  slug: open-suger-billing-api
- collection_type: open
  name: Suger API Buyer API
  slug: open-suger-buyer-api
- collection_type: open
  name: Suger API Contact API
  slug: open-suger-contact-api
- collection_type: open
  name: Suger API Entitlement API
  slug: open-suger-entitlement-api
- collection_type: open
  name: Suger API Metering API
  slug: open-suger-metering-api
- collection_type: open
  name: Suger API Notification API
  slug: open-suger-notification-api
- collection_type: open
  name: Suger API Offer API
  slug: open-suger-offer-api
- collection_type: open
  name: Suger API Product API
  slug: open-suger-product-api
- collection_type: open
  name: Suger API Report API
  slug: open-suger-report-api
- collection_type: open
  name: Suger API Support API
  slug: open-suger-support-api
- collection_type: open
  name: Suger API
  slug: open-suger
common:
- group: commercial
  href: https://artifacts.apis.io/suger/plans/suger-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/suger-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/suger/rate-limits/suger-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/suger-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/suger/finops/suger-finops.yml
  title: ''
  type: FinOps
  url: finops/suger-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.fours.com/resources/blog/
- group: other
  href: https://artifacts.apis.io/suger/capabilities/suger-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/suger-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/suger/overview
- group: agent
  href: https://artifacts.apis.io/suger/agentic-access/suger-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/suger-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/suger/security/suger-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/suger-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/suger/security/suger-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/suger-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/suger/security/suger-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suger-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/suger/authentication/suger-authentication.yml
  title: ''
  type: Authentication
  url: authentication/suger-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/suger-inc
- group: start
  title: ''
  type: Portal
  url: https://www.suger.io/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.suger.io/
- group: company
  title: ''
  type: Website
  url: https://www.suger.io/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sugerio
- group: start
  title: ''
  type: GettingStarted
  url: https://www.suger.io/docs/get-started/api-client
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suger.io/pricing
created: '2025-02-21'
description: Suger is the fastest and easiest way for ISVs to list, transact, and co-sell on cloud marketplaces including AWS Marketplace, Azure Marketplace, GCP Marketplace, and Snowflake Marketplace. Suger provides a full API for managing products, offers, entitlements, buyers, usage metering, and revenue reporting.
examples:
- key_count: 4
  name: Suger Create Entitlement Example
  slug: suger-create-entitlement-example
- key_count: 4
  name: Suger List Products Example
  slug: suger-list-products-example
finops:
- has_sources: true
  method: derived
  name: Suger Finops
  primary_unit: ''
  service_category: ''
  slug: suger-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suger.png
json_schemas:
- name: Suger Entitlement
  property_count: 14
  slug: suger-entitlement
- name: Suger Product
  property_count: 11
  slug: suger-product
json_structures:
- name: Suger Product Structure
  property_count: 0
  slug: suger-product-structure
jsonld:
- class_count: 16
  name: Suger Context
  property_count: 7
  slug: suger-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.suger.io over HTTP; 2 tools listed.
  name: Suger MCP Server
  slug: suger
modified: '2026-10-06'
name: Suger
nav: Providers
network: true
overview: 'Suger publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Buyer API, Contact API, and 8 more. Tagged areas include Cloud Marketplace, Go-To-Market, Software-as-a-Service, Billing, and Entitlements.


  The Suger catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Suger''s developer surface includes engineering blog, authentication, developer portal, documentation, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Suger Plans Pricing
  plan_count: 5
  slug: suger-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Suger Rate Limits
  slug: suger-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Suger — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: suger-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Suger API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 6
  slug: suger-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.5
    catalog_earned_first_party: 12.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 57.3
    developer_ergonomics: 41.7
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/suger/suger-2026-06-20T194638.png
security:
- kind: authentication
  name: Suger Authentication
  slug: suger-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Suger Domain Security
  slug: suger-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Suger Vulnerability Disclosure
  slug: suger-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Suger Trust Center
  slug: suger-trust-center
  summary_line: SOC 2, GDPR
slug: suger
tags:
- Cloud Marketplace
- Go-To-Market
- Software-as-a-Service
- Billing
- Entitlements
- Revenue
- Co-Sell
- Usage-Based Billing
website: https://www.suger.io/
---
