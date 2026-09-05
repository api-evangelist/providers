---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Western Union Agentic Access
  operation_count: 12
  slug: western-union-agentic-access
  summary_line: 12 operations · 4 acting
api_count: 1
apis:
- description: Western Union's PSD2-compliant Open Banking API enables Payment Service Providers to access account information (AIS) and initiate payments (PIS) in compliance with European Payment Services Directive
  name: Western Union Open Banking API
  slug: open-banking
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: Holding balance inquiry.
  name: western-union Balances API
  slug: western-union-balances-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: Payment batch lifecycle management.
  name: western-union Batches API
  slug: western-union-batches-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: Customer account management.
  name: western-union Customers API
  slug: western-union-customers-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: API health check.
  name: western-union Health API
  slug: western-union-health-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: Payment order management.
  name: western-union Orders API
  slug: western-union-orders-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: Individual payment management within a batch.
  name: western-union Payments API
  slug: western-union-payments-api
- baseURL: https://api.westernunion.com
  baseurl_source: declared
  description: FX rate and payment quote generation.
  name: western-union Quotes API
  slug: western-union-quotes-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Western Union Mass Payments Balances API
  slug: open-western-union-balances-api
- collection_type: open
  name: Western Union Mass Payments Balances Batches API
  slug: open-western-union-batches-api
- collection_type: open
  name: Western Union Mass Payments Balances Customers API
  slug: open-western-union-customers-api
- collection_type: open
  name: Western Union Mass Payments Balances Health API
  slug: open-western-union-health-api
- collection_type: open
  name: Western Union Mass Payments API
  slug: open-western-union-mass-payments
- collection_type: open
  name: Western Union Mass Payments Balances Orders API
  slug: open-western-union-orders-api
- collection_type: open
  name: Western Union Mass Balances Payments API
  slug: open-western-union-payments-api
- collection_type: open
  name: Western Union Mass Payments Balances Quotes API
  slug: open-western-union-quotes-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/western-union-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/western-union-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/western-union-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/western-union-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/western-union
- group: company
  title: ''
  type: Website
  url: https://www.westernunion.com
- group: other
  title: ''
  type: BusinessSolutions
  url: https://business.westernunion.com
- group: start
  title: ''
  type: Portal
  url: https://developer.westernunion.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.westernunion.com/getting-started.html
- group: operate
  title: ''
  type: Contact
  url: https://corporate.westernunion.com/fi-partnerships/solutions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.westernunion.com/us/en/privacy-statement.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.westernunion.com/us/en/digital-service-agreement.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/western-union
description: The Western Union Company is a global leader in cross-border, cross-currency money movement, providing money transfer, money order, and other financial services to consumers and businesses worldwide. Western Union's Partnership APIs enable financial institutions, fintech companies, and enterprise customers to integrate WU's global payment network for money transfers, batch payments, FX quotes, and account management across 200+ countries and territories in 130+ currencies. Authentication uses mTLS with client certificates.
examples:
- key_count: 2
  name: Western Union Add Payment Example
  slug: western-union-add-payment-example
- key_count: 2
  name: Western Union Create Batch Example
  slug: western-union-create-batch-example
- key_count: 2
  name: Western Union Create Quote Example
  slug: western-union-create-quote-example
finops:
- name: Western Union Finops
  service_category: Payments
  slug: western-union-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/western-union.png
json_schemas:
- name: Western Union Payment Batch
  property_count: 7
  slug: western-union-batch
- name: Western Union Payment
  property_count: 16
  slug: western-union-payment
json_structures:
- name: Western Union Payment Structure
  property_count: 0
  slug: western-union-payment-structure
jsonld:
- class_count: 0
  name: Western Union Context
  property_count: 29
  slug: western-union-context
layout: provider
modified: '2026-05-19'
name: The Western Union Company
nav: Providers
network: true
overview: 'The Western Union Company publishes 7 APIs on the [APIs.io](https://apis.io/) network, including western-union Balances API, western-union Batches API, western-union Customers API, and 4 more. Tagged areas include Fortune 500.


  The The Western Union Company catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Western Union Company''s developer surface includes authentication, developer portal, getting-started guide, and 10 more developer resources.'
plans:
- name: Western Union Plans Pricing
  plan_count: 1
  slug: western-union-plans-pricing
press:
- date: '2026-05-25'
  title: Western Union forms strategic partnership with HCLTech to ...
  url: https://www.prnewswire.com/news-releases/western-union-forms-strategic-partnership-with-hcltech-to-transition-to-an-ai-led-platform-operating-model-302409306.html
- date: '2026-05-25'
  title: Western Union Banks On First-Party Data To Woo Brands ...
  url: https://www.adexchanger.com/commerce/western-union-is-banking-on-first-party-data-to-woo-brands-to-its-new-media-network/
- date: '2026-05-25'
  title: Techstars & Western Union Accelerator Announce 2020 Class ...
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2020/Techstars--Western-Union-Accelerator-Announce-2020-Class-Leading-the-Future-of-Inclusive-Finance/default.aspx
- date: '2026-05-25'
  title: Western Union to Tap Stablecoins and AI for Greater ...
  url: https://www.pymnts.com/news/cross-border-commerce/cross-border-payments/2025/western-union-to-tap-stablecoins-and-ai-for-greater-efficiencies/
- date: '2026-05-25'
  title: Western Union Builds on Accelerator Momentum with New ...
  url: https://ir.westernunion.com/news/archived-press-releases/press-release-details/2019/Western-Union-Builds-on-Accelerator-Momentum-with-New-Artificial-Intelligence-Projects/default.aspx
random_paper: 9
rate_limits:
- limit_count: 2
  name: Western Union Rate Limits
  slug: western-union-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Western Union Company API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: western-union-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: The Western Union Company API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: western-union-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 63.3
    developer_ergonomics: 36.9
    discoverability: 53.7
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/western-union/refs/heads/main/screenshots/western-union-2026-06-20T201410.png
security:
- kind: authentication
  name: Western Union Authentication
  slug: western-union-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Western Union Domain Security
  slug: western-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: western-union
tags:
- Fortune 500
website: https://www.westernunion.com
---
