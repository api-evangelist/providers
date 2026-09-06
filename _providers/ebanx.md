---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Ebanx Agentic Access
  operation_count: 29
  slug: ebanx-agentic-access
  summary_line: 29 operations · 29 acting
api_count: 3
apis:
- baseURL: https://api.ebanxpay.com
  baseurl_source: declared
  description: Tokenize cards on EBANX so PAN never touches merchant servers, and refresh CVVs on stored tokens before high-risk reuse. Reusable tokens power one-click checkout, subscriptions, and stored-card flows.
  name: EBANX Tokenization API
  slug: ebanx-tokenization-api
- baseURL: https://api.ebanxpay.com
  baseurl_source: declared
  description: Quote current FX rates between a merchant pricing currency (typically USD or EUR) and EBANX market currencies, and mint a short-lived FX token to lock a rate so a quoted price is honored when the unde
  name: EBANX FX API
  slug: ebanx-fx-api
- description: 'Signed HTTP POST callbacks delivered to a merchant-configured Notification URL whenever a payment, refund, chargeback, or Pix MED return request changes state. Each callback carries the EBANX hash so '
  name: EBANX Payment Notifications
  slug: ebanx-notifications
- baseURL: https://api.ebanxpay.com
  baseurl_source: declared
  description: The PaymentPage API from EBANX — 1 operation(s) for paymentpage.
  name: EBANX PaymentPage API
  slug: ebanx-paymentpage-api
- baseURL: https://api.ebanxpay.com
  baseurl_source: declared
  description: The Payments API from EBANX — 12 operation(s) for payments.
  name: EBANX Payments API
  slug: ebanx-payments-api
- baseURL: https://api.ebanxpay.com
  baseurl_source: declared
  description: The Payouts API from EBANX — 12 operation(s) for payouts.
  name: EBANX Payouts API
  slug: ebanx-payouts-api
artifact_total: 37
asyncapis:
- description: EBANX sends HTTP POST callbacks to a merchant-configured Notification URL whenever a payment changes state — approved, pending, cancelled, refunded, or chargeback. Each request includes a digital sign
  name: EBANX Payment Notifications
  slug: ebanx-notifications-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EBANX FX API
  slug: open-ebanx-fx-api
- collection_type: open
  name: EBANX Pay-in Direct API
  slug: open-ebanx-pay-in-direct-api
- collection_type: open
  name: EBANX Payment Page API
  slug: open-ebanx-payment-page-api
- collection_type: open
  name: EBANX FX PaymentPage API
  slug: open-ebanx-paymentpage-api
- collection_type: open
  name: EBANX FX Payments API
  slug: open-ebanx-payments-api
- collection_type: open
  name: EBANX Payout API
  slug: open-ebanx-payout-api
- collection_type: open
  name: EBANX FX Payouts API
  slug: open-ebanx-payouts-api
- collection_type: open
  name: EBANX FX Tokenization API
  slug: open-ebanx-tokenization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ebanx-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ebanx-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ebanx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ebanx-authentication.yml
created: '2026-05-24'
description: EBANX is a Brazil-founded payments processor specializing in pay-in, payout, and cross-border payments for Latin America and other emerging markets. The EBANX API ecosystem covers Pay-in (Direct API, Payment Page, Payment Link, Drop-in), Payouts (local and cross-border), Foreign Exchange, Card Tokenization, and signed Payment Notifications across 19+ countries including Brazil, Mexico, Colombia, Chile, Argentina, Peru, Ecuador, Bolivia, Uruguay, Paraguay, Costa Rica, Guatemala, Panama, Dominican Republic, India, the Philippines, Kenya, Nigeria, South Africa, and Egypt. EBANX is best known for connecting global merchants to local payment methods like Pix, Pix Automatico, Boleto, OXXO, SPEI, PSE, Efecty, PagoEfectivo, Nequi, Mercado Pago, NuPay, PicPay, and dozens of others, plus an expanding recurring-payments product on top of alternative payment methods.
examples:
- key_count: 2
  name: Ebanx Create Direct Payment Card Example
  slug: ebanx-create-direct-payment-card-example
- key_count: 2
  name: Ebanx Create Direct Payment Pix Example
  slug: ebanx-create-direct-payment-pix-example
- key_count: 2
  name: Ebanx Create Payout Example
  slug: ebanx-create-payout-example
- key_count: 3
  name: Ebanx Payment Notification Example
  slug: ebanx-payment-notification-example
finops:
- name: Ebanx Finops
  service_category: ''
  slug: ebanx-finops
image: https://www.ebanx.com/static/images/ebanx-symbol-yellow.svg
json_schemas:
- name: EBANX Card Token
  property_count: 5
  slug: ebanx-card-token
- name: EBANX Payment
  property_count: 14
  slug: ebanx-payment
- name: EBANX Payout
  property_count: 13
  slug: ebanx-payout
- name: EBANX Refund
  property_count: 8
  slug: ebanx-refund
json_structures:
- name: Ebanx Payment Structure
  property_count: 13
  slug: ebanx-payment-structure
- name: Ebanx Payout Structure
  property_count: 13
  slug: ebanx-payout-structure
jsonld:
- class_count: 35
  name: Ebanx Context
  property_count: 0
  slug: ebanx-context
layout: provider
modified: '2026-05-24'
name: EBANX
nav: Providers
network: true
overview: 'EBANX publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Tokenization API, FX API, Payment Notifications, and 3 more. Tagged areas include Payments, Pay-In, Payouts, Foreign Exchange, and Tokenization.


  The EBANX catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  EBANX''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Ebanx Plans Pricing
  plan_count: 2
  slug: ebanx-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Ebanx Rate Limits
  slug: ebanx-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: EBANX API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: ebanx-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: EBANX API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ebanx-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: EBANX API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: ebanx-rules
score:
  band: developing
  composite: 44.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 80.5
    catalog_earned_first_party: 0.0
    catalog_gap: 34.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 73.0
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 44.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ebanx/refs/heads/main/screenshots/ebanx-2026-06-20T180446.png
security:
- kind: authentication
  name: Ebanx Authentication
  slug: ebanx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ebanx Domain Security
  slug: ebanx-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Ebanx Trust Center
  slug: ebanx-trust-center
  summary_line: ISO 27001
slug: ebanx
tags:
- Payments
- Pay-In
- Payouts
- Foreign Exchange
- Tokenization
- LatAm
- Emerging Markets
- Pix
- Boleto
- OXXO
- SPEI
- PSE
- Cross-Border
- Webhook
---
