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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 38
  human_in_the_loop: 7
  name: Bics Network Agentic Access
  operation_count: 76
  slug: bics-network-agentic-access
  summary_line: 76 operations · 38 acting · 7 human-in-the-loop
api_count: 24
apis:
- description: Phone number verification and mobile authentication for anti-fraud, KYC and onboarding - validating that a mobile number is real, active, and controlled by the user, including OTP-based flows. Markete
  name: BICS Number Verification API
  slug: bics-number-verification-api
- description: Network-signal services for fraud prevention and mobile identity - HLR and reachability lookup (operator, ported status, active/blocked SIM state), SIM-swap detection, and device-location signals used
  name: BICS Fraud Prevention and Reachability API
  slug: bics-fraud-prevention-reachability-api
- description: Manage your addresses
  name: BICS Address Management API
  slug: bics-network-address-management-api
- description: The following methods allows you to request your Call Detail Records (CDRs), request the status of your requests and download your CDRs. The CDRs are available for both Inbound and Outbound calls term
  name: BICS CDR API
  slug: bics-network-cdr-api
- description: The Connections Management API from BICS — 3 operation(s) for connections management.
  name: BICS Connections Management API
  slug: bics-network-connections-management-api
- description: The Conversions API from BICS — 1 operation(s) for conversions.
  name: BICS Conversions API
  slug: bics-network-conversions-api
- description: The Conversionsinfos API from BICS — 1 operation(s) for conversionsinfos.
  name: BICS Conversionsinfos API
  slug: bics-network-conversionsinfos-api
- description: Manage your disconnection order
  name: BICS Disconnection Services API
  slug: bics-network-disconnection-services-api
- description: The Document Management API from BICS — 1 operation(s) for document management.
  name: BICS Document Management API
  slug: bics-network-document-management-api
- description: Manage your emergency services request
  name: BICS Emergency Services API
  slug: bics-network-emergency-services-api
- description: The Inbound API from BICS — 2 operation(s) for inbound.
  name: BICS Inbound API
  slug: bics-network-inbound-api
- description: The Interconnects List API from BICS — 1 operation(s) for interconnects list.
  name: BICS Interconnects List API
  slug: bics-network-interconnects-list-api
- description: Query the numbers you have bought over time.
  name: BICS inventory API
  slug: bics-network-inventory-api
- description: The number API from BICS — 1 operation(s) for number.
  name: BICS number API
  slug: bics-network-number-api
- description: Purchase a number from the stock.
  name: BICS order API
  slug: bics-network-order-api
- description: The Outbound API from BICS — 3 operation(s) for outbound.
  name: BICS Outbound API
  slug: bics-network-outbound-api
- description: The porting API from BICS — 4 operation(s) for porting.
  name: BICS porting API
  slug: bics-network-porting-api
- description: Recive porting specification
  name: BICS Porting Specification API
  slug: bics-network-porting-specification-api
- description: Query your pricelist.
  name: BICS pricelist API
  slug: bics-network-pricelist-api
- description: Query BICS reference data.
  name: BICS reference API
  slug: bics-network-reference-api
- description: The Reference Data API from BICS — 1 operation(s) for reference data.
  name: BICS Reference Data API
  slug: bics-network-reference-data-api
- description: Modify routing details for customer numbers.
  name: BICS routing API
  slug: bics-network-routing-api
- description: The specification API from BICS — 1 operation(s) for specification.
  name: BICS specification API
  slug: bics-network-specification-api
- description: Query the available stock.
  name: BICS stock API
  slug: bics-network-stock-api
artifact_total: 29
common:
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


  BICS''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Bics Network Plans Pricing
  plan_count: 0
  slug: bics-network-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Bics Network Rate Limits
  slug: bics-network-rate-limits
score:
  band: emerging
  composite: 26.7
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.7
  schema_version: 0.5
  scored_at: '2026-07-27'
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
