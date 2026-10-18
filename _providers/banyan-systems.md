---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Banyan Systems Agentic Access
  operation_count: 40
  slug: banyan-systems-agentic-access
  summary_line: 40 operations · 17 acting
api_count: 3
apis:
- description: Banyan's OAuth2 REST API for submitting receipt and transaction data, retrieving enriched (item-level) transactions, managing card-linked-offer campaigns/offers/activations, receipt search, consumer c
  name: Banyan API
  slug: banyan-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Authentication API from Banyan Systems — 2 operation(s) for authentication.
  name: Banyan Systems Authentication API
  slug: banyan-systems-authentication-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Card Linked Offer API from Banyan Systems — 9 operation(s) for card linked offer.
  name: Banyan Systems Card Linked Offer API
  slug: banyan-systems-card-linked-offer-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Consent API from Banyan Systems — 3 operation(s) for consent.
  name: Banyan Systems Consent API
  slug: banyan-systems-consent-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Enriched Data API from Banyan Systems — 3 operation(s) for enriched data.
  name: Banyan Systems Enriched Data API
  slug: banyan-systems-enriched-data-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Enriched Data - Merchant Service Provider API from Banyan Systems — 1 operation(s) for enriched data - merchant service provider.
  name: Banyan Systems Enriched Data - Merchant Service Provider API
  slug: banyan-systems-enriched-data-merchant-service-provider-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The History API from Banyan Systems — 1 operation(s) for history.
  name: Banyan Systems History API
  slug: banyan-systems-history-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Receipt API from Banyan Systems — 4 operation(s) for receipt.
  name: Banyan Systems Receipt API
  slug: banyan-systems-receipt-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Tag Counter API from Banyan Systems — 1 operation(s) for tag counter.
  name: Banyan Systems Tag Counter API
  slug: banyan-systems-tag-counter-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Transaction API from Banyan Systems — 2 operation(s) for transaction.
  name: Banyan Systems Transaction API
  slug: banyan-systems-transaction-api
- baseURL: https://api.banyan.com
  baseurl_source: declared
  description: The Webhook API from Banyan Systems — 5 operation(s) for webhook.
  name: Banyan Systems Webhook API
  slug: banyan-systems-webhook-api
artifact_total: 30
asyncapis:
- description: ''
  name: Banyan Systems Webhooks
  slug: banyan-systems-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/agentic-access/banyan-systems-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/banyan-systems-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/rules/banyan-systems-rules.yml
  title: ''
  type: Spectral
  url: rules/banyan-systems-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/json-ld/banyan-systems-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/banyan-systems-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/vocabulary/banyan-systems-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/banyan-systems-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/data-model/banyan-systems-data-model.yml
  title: ''
  type: DataModel
  url: data-model/banyan-systems-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/hosts/banyan-systems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banyan-systems-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/vendors/banyan-systems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/banyan-systems-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.banyan.com/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/scopes/banyan-systems-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/banyan-systems-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.banyan.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.banyan.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developers.banyan.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developers.banyan.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.banyan.com/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.banyan.com/blog-featured
- group: operate
  title: ''
  type: Support
  url: https://www.banyan.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.banyan.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.banyan.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/changelog/banyan-systems-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/banyan-systems-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/authentication/banyan-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/banyan-systems-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/conventions/banyan-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/banyan-systems-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/errors/banyan-systems-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/banyan-systems-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/lifecycle/banyan-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/banyan-systems-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/conformance/banyan-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/banyan-systems-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/asyncapi/banyan-systems-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/banyan-systems-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/mcp/banyan-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/banyan-systems-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/llms/banyan-systems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banyan-systems-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/well-known/banyan-systems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banyan-systems-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/security/banyan-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banyan-systems-domain-security.yml
created: '2026-07-17'
description: Banyan is a privacy-first, item-level receipt data infrastructure platform that acts as middleware between merchants, banks, fintechs, and merchant service providers so they can securely share and enrich transaction data without bilateral contracts. Merchants send receipt and item detail to Banyan (via REST API or batch), and financial institutions submit card transactions to be matched and enriched with SKU-level line items, powering products like card-linked offers (CLO), expense management, and receipt display inside banking apps. Banyan has processed over 21 billion receipts across a network of 40,000+ merchant stores and 5,000+ financial institutions. Founded in 2013, backed by Battery Ventures, Fin Capital, M13, TTV Capital and others, and acquired by Bilt Rewards in March 2025. The public developer platform at developers.banyan.com exposes an OAuth2 REST API (api.banyan.com/rest/v1) plus a webhook egress surface for enriched transactions and offer redemptions.
image: https://cdn.prod.website-files.com/64cf554e262e35556d264e52/66423c7fdfa3c29d470e52e2_Banyan%20Logo_OGI.png
json_schemas:
- name: ConsentEgressJSON
  property_count: 5
  slug: banyan-systems-consent-egress-json
- name: ConsentIngressJSON
  property_count: 5
  slug: banyan-systems-consent-ingress-json
- name: CreateConsentRecordIDJSON
  property_count: 1
  slug: banyan-systems-create-consent-record-idjson
- name: Error
  property_count: 3
  slug: banyan-systems-error-json
- name: FindConsentInputJSON
  property_count: 4
  slug: banyan-systems-find-consent-input-json
- name: FindConsentOutputJSON
  property_count: 1
  slug: banyan-systems-find-consent-output-json
- name: OfferEntityJSON
  property_count: 25
  slug: banyan-systems-offer-entity-json
- name: OfferIngressJSON
  property_count: 21
  slug: banyan-systems-offer-ingress-json
- name: ReceiptHotelJSON
  property_count: 16
  slug: banyan-systems-receipt-hotel-json
- name: ReceiptMerchantJSON
  property_count: 19
  slug: banyan-systems-receipt-merchant-json
- name: ReceiptRetailJSON
  property_count: 16
  slug: banyan-systems-receipt-retail-json
- name: TransactionEgressJSON
  property_count: 12
  slug: banyan-systems-transaction-egress-json
jsonld:
- class_count: 117
  name: Banyan Systems Context
  property_count: 230
  slug: banyan-systems-context
layout: provider
modified: '2026-07-18'
name: Banyan Systems
nav: Providers
network: true
overview: 'Banyan Systems publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Card Linked Offer API, Consent API, and 8 more. Tagged areas include Company, Receipt Data, Transaction Enrichment, Item-Level Data, and Card-Linked Offers.


  The Banyan Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Banyan Systems'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 22 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Banyan Systems API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: banyan-systems-rules
scopes:
- name: Banyan Systems Scopes
  scope_count: 0
  slug: banyan-systems-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.1
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 68.4
    developer_ergonomics: 38.1
    discoverability: 80.4
    operational_transparency: 15.8
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/banyan-systems/refs/heads/main/screenshots/banyan-systems-2026-07-25T202351.png
security:
- kind: authentication
  name: Banyan Systems Authentication
  slug: banyan-systems-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Banyan Systems Domain Security
  slug: banyan-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: banyan-systems
tags:
- Company
- Receipt Data
- Transaction Enrichment
- Item-Level Data
- Card-Linked Offers
- Fintech
- Payments
- Data Collaboration
- Webhook
- Data Enrichment
website: https://www.banyan.com/
---
