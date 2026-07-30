---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 64
  human_in_the_loop: 0
  name: Suger Agentic Access
  operation_count: 106
  slug: suger-agentic-access
  summary_line: 106 operations · 64 acting
api_count: 11
apis:
- description: Access to API client resources
  name: Suger API API
  slug: suger-api-api
- description: Access to Billing resources, such as addon, invoice, payment, etc.
  name: Suger Billing API
  slug: suger-billing-api
- description: Access to Buyer resources
  name: Suger Buyer API
  slug: suger-buyer-api
- description: Access to Contact resources
  name: Suger Contact API
  slug: suger-contact-api
- description: Access to Entitlement resources
  name: Suger Entitlement API
  slug: suger-entitlement-api
- description: Access to Usage Metering resources
  name: Suger Metering API
  slug: suger-metering-api
- description: Access to Notification resources
  name: Suger Notification API
  slug: suger-notification-api
- description: Access to Offer resources
  name: Suger Offer API
  slug: suger-offer-api
- description: Access to Product resources
  name: Suger Product API
  slug: suger-product-api
- description: Access to revenue or usage metering Report resources
  name: Suger Report API
  slug: suger-report-api
- description: Access to Suger Support ticket resources
  name: Suger Support API
  slug: suger-support-api
artifact_total: 39
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
  name: Suger API
  slug: open-suger
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/suger/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/suger-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/suger-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/suger-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suger-domain-security.yml
- group: auth
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
- name: Suger Finops
  service_category: API
  slug: suger-finops
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
modified: '2026-05-19'
name: Suger
nav: Providers
network: true
overview: 'Suger publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API API, Billing API, Buyer API, and 8 more. Tagged areas include Cloud Marketplace, GTM, SaaS, Billing, and Entitlement.


  The Suger catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Suger''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, and 8 more developer resources.'
plans:
- name: Suger Plans Pricing
  plan_count: 3
  slug: suger-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Suger Rate Limits
  slug: suger-rate-limits
rules:
- name: Suger API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: suger-jsonschema-spectral-rules
- name: Suger API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 6
  slug: suger-rules
score:
  band: strong
  composite: 56.3
  delta: -4.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 64.9
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suger/refs/heads/main/screenshots/suger-2026-06-20T194638.png
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
  summary_line: disclosure policy published
- kind: trust-center
  name: Suger Trust Center
  slug: suger-trust-center
  summary_line: SOC 2, GDPR
slug: suger
tags:
- Cloud Marketplace
- GTM
- SaaS
- Billing
- Entitlement
- Revenue
- Co-Sell
website: https://www.suger.io/
---
