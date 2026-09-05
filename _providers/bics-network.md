---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 7
  name: Bics Network Agentic Access
  operation_count: 76
  slug: bics-network-agentic-access
  summary_line: 76 operations · 38 acting · 7 human-in-the-loop
api_count: 8
apis:
- description: Phone number verification and mobile authentication for anti-fraud, KYC and onboarding - validating that a mobile number is real, active, and controlled by the user, including OTP-based flows. Markete
  name: BICS Number Verification API
  slug: bics-number-verification-api
- description: Network-signal services for fraud prevention and mobile identity - HLR and reachability lookup (operator, ported status, active/blocked SIM state), SIM-swap detection, and device-location signals used
  name: BICS Fraud Prevention and Reachability API
  slug: bics-fraud-prevention-reachability-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Manage your addresses
  name: BICS Address Management API
  slug: bics-network-address-management-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The following methods allows you to request your Call Detail Records (CDRs), request the status of your requests and download your CDRs. The CDRs are available for both Inbound and Outbound calls term
  name: BICS CDR API
  slug: bics-network-cdr-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Connections Management API from BICS — 3 operation(s) for connections management.
  name: BICS Connections Management API
  slug: bics-network-connections-management-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Conversions API from BICS — 1 operation(s) for conversions.
  name: BICS Conversions API
  slug: bics-network-conversions-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Conversionsinfos API from BICS — 1 operation(s) for conversionsinfos.
  name: BICS Conversionsinfos API
  slug: bics-network-conversionsinfos-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Manage your disconnection order
  name: BICS Disconnection Services API
  slug: bics-network-disconnection-services-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Document Management API from BICS — 1 operation(s) for document management.
  name: BICS Document Management API
  slug: bics-network-document-management-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Manage your emergency services request
  name: BICS Emergency Services API
  slug: bics-network-emergency-services-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Inbound API from BICS — 2 operation(s) for inbound.
  name: BICS Inbound API
  slug: bics-network-inbound-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Interconnects List API from BICS — 1 operation(s) for interconnects list.
  name: BICS Interconnects List API
  slug: bics-network-interconnects-list-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Query the numbers you have bought over time.
  name: BICS inventory API
  slug: bics-network-inventory-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The number API from BICS — 1 operation(s) for number.
  name: BICS number API
  slug: bics-network-number-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Purchase a number from the stock.
  name: BICS order API
  slug: bics-network-order-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Outbound API from BICS — 3 operation(s) for outbound.
  name: BICS Outbound API
  slug: bics-network-outbound-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The porting API from BICS — 4 operation(s) for porting.
  name: BICS porting API
  slug: bics-network-porting-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Recive porting specification
  name: BICS Porting Specification API
  slug: bics-network-porting-specification-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Query your pricelist.
  name: BICS pricelist API
  slug: bics-network-pricelist-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Query BICS reference data.
  name: BICS reference API
  slug: bics-network-reference-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The Reference Data API from BICS — 1 operation(s) for reference data.
  name: BICS Reference Data API
  slug: bics-network-reference-data-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Modify routing details for customer numbers.
  name: BICS routing API
  slug: bics-network-routing-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: The specification API from BICS — 1 operation(s) for specification.
  name: BICS specification API
  slug: bics-network-specification-api
- baseURL: https://api.bics.com/sms/v3
  baseurl_source: declared
  description: Query the available stock.
  name: BICS stock API
  slug: bics-network-stock-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: connect Address Management API
  slug: open-bics-network-address-management-api
- collection_type: open
  name: connect Address Management CDR API
  slug: open-bics-network-cdr-api
- collection_type: open
  name: connect Address Management Connections Management API
  slug: open-bics-network-connections-management-api
- collection_type: open
  name: connect Address Management Conversions API
  slug: open-bics-network-conversions-api
- collection_type: open
  name: connect Address Management Conversionsinfos API
  slug: open-bics-network-conversionsinfos-api
- collection_type: open
  name: connect Address Management Disconnection Services API
  slug: open-bics-network-disconnection-services-api
- collection_type: open
  name: connect Address Management Document Management API
  slug: open-bics-network-document-management-api
- collection_type: open
  name: connect Address Management Emergency Services API
  slug: open-bics-network-emergency-services-api
- collection_type: open
  name: connect Address Management Inbound API
  slug: open-bics-network-inbound-api
- collection_type: open
  name: connect Address Management Interconnects List API
  slug: open-bics-network-interconnects-list-api
- collection_type: open
  name: connect Address Management inventory API
  slug: open-bics-network-inventory-api
- collection_type: open
  name: connect Address Management number API
  slug: open-bics-network-number-api
- collection_type: open
  name: connect Address Management order API
  slug: open-bics-network-order-api
- collection_type: open
  name: connect Address Management Outbound API
  slug: open-bics-network-outbound-api
- collection_type: open
  name: connect Address Management porting API
  slug: open-bics-network-porting-api
- collection_type: open
  name: connect Address Management Porting Specification API
  slug: open-bics-network-porting-specification-api
- collection_type: open
  name: connect Address Management pricelist API
  slug: open-bics-network-pricelist-api
- collection_type: open
  name: connect Address Management reference API
  slug: open-bics-network-reference-api
- collection_type: open
  name: connect Address Management Reference Data API
  slug: open-bics-network-reference-data-api
- collection_type: open
  name: connect Address Management routing API
  slug: open-bics-network-routing-api
- collection_type: open
  name: connect Address Management specification API
  slug: open-bics-network-specification-api
- collection_type: open
  name: connect Address Management stock API
  slug: open-bics-network-stock-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bics-network-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bics-network-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bics-network-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bics
- group: company
  title: ''
  type: Website
  url: https://www.bics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bics.com/portal/apis
- group: commercial
  title: ''
  type: Plans
  url: plans/bics-network-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bics-network-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bics-network-finops.yml
created: '2026-07-11'
description: BICS is an international communications enabler and wholesale carrier, part of Proximus Global (alongside Telesign and Route Mobile). Its developer portal exposes OAuth2-secured REST APIs at api.bics.com for A2P SMS and OTP delivery, global number provisioning and portability (MyNumbers), call detail records, emergency services, and carrier-grade cloud connectivity. BICS also offers mobile identity capabilities - phone number verification, HLR/reachability lookup, SIM-swap detection and device-location signals for anti-fraud and KYC - as partner and carrier contract products across the Proximus Global network rather than as self-serve endpoints.
finops:
- name: Bics Network Finops
  service_category: ''
  slug: bics-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bics-network.png
layout: provider
modified: '2026-07-11'
name: BICS
nav: Providers
network: true
overview: 'BICS publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Address Management API, CDR API, Connections Management API, and 19 more. Tagged areas include Number Verification, Telecom, Mobile Identity, Anti-Fraud, and Device Location.


  BICS''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Bics Network Plans Pricing
  plan_count: 0
  slug: bics-network-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Bics Network Rate Limits
  slug: bics-network-rate-limits
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 52.1
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bics-network/refs/heads/main/screenshots/bics-network-2026-07-25T202908.png
security:
- kind: authentication
  name: Bics Network Authentication
  slug: bics-network-authentication
  summary_line: 0 schemes
slug: bics-network
tags:
- Number Verification
- Telecom
- Mobile Identity
- Anti-Fraud
- Device Location
- OTP
- SMS
- Numbering
- Number Portability
- Fraud Prevention
- Carrier
- CPaaS
website: https://www.bics.com/
---
