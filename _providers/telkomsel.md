---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Telkomsel Agentic Access
  operation_count: 27
  slug: telkomsel-agentic-access
  summary_line: 27 operations · 25 acting
api_count: 8
apis:
- description: Register customer consent required by subscriber-data products.
  name: Telkomsel Consent Management API
  slug: telkomsel-consent-management-api
- description: NIK/MSISDN pairing, KTP matching, and general ID verification against SIM-registration data.
  name: Telkomsel Identity Verification API
  slug: telkomsel-identity-verification-api
- description: Location verification scoring and last known location.
  name: Telkomsel Location API
  slug: telkomsel-location-api
- description: Telco-data scores - tScore, generic telco score, SES, interest, lifestyle, loyalist.
  name: Telkomsel Scoring and Insights API
  slug: telkomsel-scoring-and-insights-api
- description: SIM swap detection - marketplace SIM Swap v2 and the CAMARA-style /sim-swap/v0 API with CIBA auth.
  name: Telkomsel SIM Swap API
  slug: telkomsel-sim-swap-api
- description: Application-to-person SMS - regular and premium sends plus delivery-status polling.
  name: Telkomsel SMS API
  slug: telkomsel-sms-api
- description: MSISDN state - active status, subscriber type, roaming, call forwarding, recycled numbers.
  name: Telkomsel Subscriber Check API
  slug: telkomsel-subscriber-check-api
- description: USSD broadcast messaging and delivery status.
  name: Telkomsel USSD API
  slug: telkomsel-ussd-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telkomsel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telkomsel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telkomsel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telkomsel
- group: company
  title: ''
  type: Website
  url: https://www.telkomsel.com/en
- group: start
  title: ''
  type: Portal
  url: https://digihub.telkomsel.com
- group: docs
  title: ''
  type: Documentation
  url: https://digihub.telkomsel.com/documentation
- group: auth
  title: ''
  type: Authentication
  url: https://digihub.telkomsel.com/documentation/consumer-guide/api-authentication
- group: commercial
  title: ''
  type: Plans
  url: plans/telkomsel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/telkomsel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/telkomsel-finops.yml
created: '2026-07-11'
description: Telkomsel (PT Telekomunikasi Selular) is Indonesia's largest mobile network operator. Through DigiHub (digihub.telkomsel.com), its API marketplace, Telkomsel exposes network and subscriber APIs to developers and enterprises - A2P SMS and USSD messaging, subscriber status checks, identity verification (NIK/KTP matching), location verification, SIM swap detection (including a CAMARA-style API), consent management, and telco-data scoring products. Telkomsel is a GSMA Open Gateway participant, launching Number Verify, SIM Swap, and Device Location network APIs alongside the other Indonesian carriers, and partners with Vonage to distribute its network APIs globally. Access requires a DigiHub account; plans range from free sandbox trials and prepaid quota packages to enterprise tier and pay-as-you-use contracts.
finops:
- name: Telkomsel Finops
  service_category: Integration and Communication
  slug: telkomsel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telkomsel.png
layout: provider
modified: '2026-07-11'
name: Telkomsel
nav: Providers
network: true
overview: 'Telkomsel publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Consent Management API, Identity Verification API, Location API, and 5 more. Tagged areas include Telecommunications, Indonesia, SMS, Mobile Network, and CPaaS.


  Telkomsel''s developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Telkomsel Plans Pricing
  plan_count: 4
  slug: telkomsel-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Telkomsel Rate Limits
  slug: telkomsel-rate-limits
score:
  band: thin
  composite: 36.3
  delta: -5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Telkomsel Authentication
  slug: telkomsel-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Telkomsel Domain Security
  slug: telkomsel-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: telkomsel
tags:
- Telecommunications
- Indonesia
- SMS
- Mobile Network
- CPaaS
- Network APIs
- Identity Verification
website: https://www.telkomsel.com/en
---
