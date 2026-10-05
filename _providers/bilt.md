---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: External backend contract for integrators using the Bilt Checkout SDK, documented at developers.bilt.com. No owned OpenAPI spec found on Bilt's own domain.
  name: Bilt Checkout SDK
  slug: bilt-checkout-sdk
- baseURL: https://partnerapi.biltrewards.com
  baseurl_source: spec
  description: Read-only lookup of a customer's current default payment-method summary for display and pre-flight checks. Bilt resolves the default again at charge time, so it may change between lookup and payment.
  name: BILT Default payment method API
  slug: bilt-default-payment-method-api
- baseURL: https://partnerapi.biltrewards.com
  baseurl_source: spec
  description: Charge a customer's current default Bilt payment method with no Bilt UI, for subscriptions, autopay, or other off-session payments. The outcome arrives as a `payment.*` webhook.
  name: BILT Headless payments API
  slug: bilt-headless-payments-api
- baseURL: https://partnerapi.biltrewards.com
  baseurl_source: spec
  description: Open a checkout session that renders Bilt-hosted checkout in the Checkout SDK. The customer confirms the payment themselves; the outcome arrives as a `checkout.session.*` webhook.
  name: BILT One-time payments API
  slug: bilt-one-time-payments-api
artifact_total: 8
asyncapis:
- description: ''
  name: Bilt Webhooks
  slug: bilt-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/rules/bilt-rules.yml
  title: ''
  type: Spectral
  url: rules/bilt-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/json-ld/bilt-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bilt-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/vocabulary/bilt-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bilt-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/asyncapi/bilt-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bilt-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/data-model/bilt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bilt-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/conventions/bilt-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bilt-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/conventions/bilt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bilt-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/errors/bilt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bilt-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/conformance/bilt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bilt-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/overlays/bilt-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bilt-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/llms/bilt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bilt-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/hosts/bilt-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bilt-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/vendors/bilt-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bilt-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.bilt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bilt.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bilt.com/docs/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bilt/refs/heads/main/security/bilt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bilt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bilt.com
coverage:
  checked: '2026-09-28'
  detail: The only OpenAPI spec found is hosted at partnerapi.biltrewards.com, not on Bilt's own domain.
  evidence:
  - status: 200
    url: https://developers.bilt.com/docs/specs/checkout-sdk.yml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: BILT is a financial technology company offering a loyalty and payments platform that lets members earn rewards on rent and mortgage payments. It provides a co‑branded credit card, rent‑payment reporting to credit bureaus, and a suite of neighborhood benefits, aiming to transform housing expenses into valuable points and perks for users.
image: https://framerusercontent.com/assets/YTMxpEJv31tk1JFEEX3t2rIls.png
jsonld:
- class_count: 18
  name: Bilt Context
  property_count: 33
  slug: bilt-context
layout: provider
modified: '2026-09-28'
name: BILT
nav: Providers
network: true
overview: 'BILT publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Default payment method API, Headless payments API, One-time payments API, and 1 more. Tagged areas include Fintech, Loyalty, Payments, RentRewards, and Credit Cards.


  The BILT catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BILT''s developer surface includes documentation, API reference, and 16 more developer resources.'
random_paper: 9
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: BILT API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: bilt-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    contract_governance: 22.0
    contract_quality: 64.6
    developer_ergonomics: 16.7
    discoverability: 64.3
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bilt Domain Security
  slug: bilt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bilt
tags:
- Fintech
- Loyalty
- Payments
- RentRewards
- Credit Cards
- Real Estate
website: https://www.bilt.com
---
