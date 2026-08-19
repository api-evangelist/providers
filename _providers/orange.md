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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Orange Agentic Access
  operation_count: 2
  slug: orange-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 15
apis:
- description: Verifies phone numbers in real time against the operator network for identity confirmation, fraud prevention, and frictionless authentication.
  name: Number Verification API
  slug: number-verification
- description: Detects recent SIM card changes for a given mobile number to help prevent account takeover and fraud.
  name: SIM Swap API
  slug: sim-swap
- description: Conducts know-your-customer matching against operator-held subscriber data to validate identities during onboarding.
  name: KYC Match API
  slug: kyc-match
- description: Identifies recent changes of the device associated with a mobile number to flag potential fraud and verify continuity of identity.
  name: Device Swap API
  slug: device-swap
- description: Identity verification suite including Live Identity Captcha and Live Identity Verify for confirming a real, present user.
  name: Live Identity API
  slug: live-identity
- description: A portfolio of messaging APIs including SMS Middle East and Africa, Messaging Pro Cameroon, Voice as a Service, Business Talk, and Contact Everyone for enterprise and regional communications.
  name: Messaging APIs
  slug: messaging
- description: Device Location Retrieval and Device Location Verification APIs that obtain or confirm a device's geographic position from the network.
  name: Device Location APIs
  slug: device-location
- description: Establishes geographic boundary alerts based on real-time device location served by the operator network.
  name: Geofencing API
  slug: geofencing
- description: Network insight APIs including Population Density Data, Quality of Service on Demand, Device Reachability Status, and Device Roaming Status.
  name: Network Dynamics APIs
  slug: network-dynamics
- description: Mobile payment platform API enabling developers to integrate Orange Money wallet transactions, transfers, and payments.
  name: Orange Money API
  slug: orange-money
- description: Direct carrier billing API allowing customers to charge purchases to their Orange mobile bill.
  name: Pay with Orange Bill API
  slug: pay-with-orange-bill
- description: A set of cloud and connectivity APIs including Cloud Avenue, Evolution Platform, EVPL Online, and Content Delivery Boost.
  name: Cloud Connectivity APIs
  slug: cloud-connectivity
- description: SIM management and device monitoring for IoT deployments across Orange's global cellular footprint.
  name: IoT Managed Global Connectivity API
  slug: iot
- description: The Device Phone Number API from Orange — 1 operation(s) for device phone number.
  name: Orange Device Phone Number API
  slug: orange-device-phone-number-api
- description: The Verify API from Orange — 1 operation(s) for verify.
  name: Orange Verify API
  slug: orange-verify-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Orange Number Verification Device Phone Number API
  slug: open-orange-device-phone-number-api
- collection_type: open
  name: Orange Number Verification Device Phone Number Verify API
  slug: open-orange-verify-api
- collection_type: open
  name: Orange Number Verification API
  slug: open-orange
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orange-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orange-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orange-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Orange-OpenSource
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange
- group: start
  title: ''
  type: Portal
  url: https://developer.orange.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/apis/
- group: start
  title: ''
  type: Signup
  url: https://developer.orange.com/user/register
- group: start
  title: ''
  type: Login
  url: https://developer.orange.com/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.orange.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.orange.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://developer.orange.com/forum
- group: company
  title: ''
  type: Website
  url: https://www.orange.com/
created: '2025-02-09'
description: Orange Developer offers a portfolio of network, communication, identity, location, payment, IoT, and cloud APIs that allow developers to build new customer experiences powered by programmable networks and Orange's telecom infrastructure across Europe, the Middle East, and Africa.
finops:
- name: Orange Finops
  service_category: API
  slug: orange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orange.png
layout: provider
modified: '2026-04-28'
name: Orange
nav: Providers
network: true
overview: 'Orange publishes 2 APIs on the [APIs.io](https://apis.io/) network: Device Phone Number API and Verify API. Tagged areas include Network, Telecom, Identity, Messaging, and Location.


  Orange''s developer surface includes authentication, developer portal, documentation, signup flow, support, and 9 more developer resources.'
plans:
- name: Orange Plans Pricing
  plan_count: 3
  slug: orange-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Orange Rate Limits
  slug: orange-rate-limits
score:
  band: thin
  composite: 32.4
  delta: -6.4
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 54.5
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 25.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/orange/refs/heads/main/screenshots/orange-2026-06-20T191151.png
security:
- kind: authentication
  name: Orange Authentication
  slug: orange-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Orange Domain Security
  slug: orange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Orange Vulnerability Disclosure
  slug: orange-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orange
tags:
- Network
- Telecom
- Identity
- Messaging
- Location
- Payment
- IoT
website: https://www.orange.com/
---
