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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 33.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Telefonica Agentic Access
  operation_count: 11
  slug: telefonica-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 6
apis:
- description: The Scam Signal API enables companies to protect their customers from phishing scams and voice fraud by detecting active scam calls in real time using Telefónica's network intelligence. Available in S
  name: Telefónica Scam Signal API
  slug: scam-signal-api
- description: The Age Verification API allows companies to confirm in real time whether a mobile user meets a specified age threshold, using carrier data for privacy-preserving age checks without sharing personal d
  name: Telefónica Age Verification API
  slug: age-verification-api
- description: The Line Tenure API indicates how long a mobile number has belonged to its current user, providing a fraud risk signal for identity validation and account security workflows. Available in Spain, Brazi
  name: Telefónica Line Tenure API
  slug: line-tenure-api
- description: The Population Density Data API provides dynamic real-time data on population density in a specific geographic area and time window, derived from anonymized and aggregated mobile network data. Used fo
  name: Telefónica Population Density Data API
  slug: population-density-data-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The Device Roaming API from Telefónica — 1 operation(s) for device roaming.
  name: Telefónica Device Roaming API
  slug: telefonica-device-roaming-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The KYC Match API from Telefónica — 1 operation(s) for kyc match.
  name: Telefónica KYC Match API
  slug: telefonica-kyc-match-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The Location Verification API from Telefónica — 1 operation(s) for location verification.
  name: Telefónica Location Verification API
  slug: telefonica-location-verification-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The Number Verification API from Telefónica — 2 operation(s) for number verification.
  name: Telefónica Number Verification API
  slug: telefonica-number-verification-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The QoD Sessions API from Telefónica — 2 operation(s) for qod sessions.
  name: Telefónica QoD Sessions API
  slug: telefonica-qod-sessions-api
- baseURL: https://opengateway.telefonica.com
  baseurl_source: declared
  description: The SIM Swap API from Telefónica — 2 operation(s) for sim swap.
  name: Telefónica SIM Swap API
  slug: telefonica-sim-swap-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Telefónica Status Device Roaming API
  slug: open-telefonica-device-roaming-api
- collection_type: open
  name: Telefónica Device Roaming Status API
  slug: open-telefonica-device-roaming
- collection_type: open
  name: Telefónica Status Device Roaming KYC Match API
  slug: open-telefonica-kyc-match-api
- collection_type: open
  name: Telefónica Know Your Customer Match API
  slug: open-telefonica-kyc-match
- collection_type: open
  name: Telefónica Status Device Roaming Location Verification API
  slug: open-telefonica-location-verification-api
- collection_type: open
  name: Telefónica Location Verification API
  slug: open-telefonica-location-verification
- collection_type: open
  name: Telefónica Status Device Roaming Number Verification API
  slug: open-telefonica-number-verification-api
- collection_type: open
  name: Telefónica Number Verification API
  slug: open-telefonica-number-verification
- collection_type: open
  name: Telefónica Status Device Roaming QoD Sessions API
  slug: open-telefonica-qod-sessions-api
- collection_type: open
  name: Telefónica Quality on Demand API
  slug: open-telefonica-quality-on-demand
- collection_type: open
  name: Telefónica Status Device Roaming SIM Swap API
  slug: open-telefonica-sim-swap-api
- collection_type: open
  name: Telefónica SIM Swap API
  slug: open-telefonica-sim-swap
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/telefonica-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/telefonica-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telefonica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telefonica-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opengateway.telefonica.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opengateway.telefonica.com/en/developer-hub
- group: docs
  title: ''
  type: Documentation
  url: https://developers.opengateway.telefonica.com/docs/initiative
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Telefonica
- group: build
  title: ''
  type: GitHub
  url: https://github.com/camaraproject
- group: other
  title: ''
  type: APIs
  url: https://opengateway.telefonica.com/en/apis
- group: start
  title: ''
  type: Signup
  url: https://opengateway.telefonica.com/en/developer-hub/join
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/telefonica
- group: other
  title: ''
  type: X
  url: https://x.com/Telefonica
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.opengateway.telefonica.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.telefonica.com/en/feed/
created: '2025-03-01'
description: Telefónica is one of the world's leading telecommunications companies, operating in Europe and Latin America. Through its Open Gateway initiative, Telefónica exposes standardized network capabilities as APIs following the CAMARA (Cloud and Edge for Mobile Access and Real-time Execution) open standards developed by the GSMA. The Open Gateway APIs enable developers and enterprises to build applications leveraging Telefónica's network infrastructure for authentication, fraud prevention, location services, quality of service, and device management. APIs are available in Spain, Germany, Brazil, and the United Kingdom through the Telefónica Open Gateway sandbox and partner program.
examples:
- key_count: 2
  name: Telefonica Kyc Match Example
  slug: telefonica-kyc-match-example
- key_count: 2
  name: Telefonica Location Verification Example
  slug: telefonica-location-verification-example
- key_count: 2
  name: Telefonica Number Verification Example
  slug: telefonica-number-verification-example
- key_count: 2
  name: Telefonica Sim Swap Check Example
  slug: telefonica-sim-swap-check-example
finops:
- name: Telefonica Finops
  service_category: Telecommunications / Network APIs
  slug: telefonica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/telefonica.png
json_schemas:
- name: ApplicationServer
  property_count: 2
  slug: telefonica-applicationserver
- name: Area
  property_count: 4
  slug: telefonica-area
- name: CreateSessionRequest
  property_count: 6
  slug: telefonica-createsessionrequest
- name: Telefónica CAMARA Device
  property_count: 4
  slug: telefonica-device
- name: ErrorResponse
  property_count: 3
  slug: telefonica-errorresponse
- name: KycMatchRequest
  property_count: 20
  slug: telefonica-kycmatchrequest
- name: KycMatchResponse
  property_count: 8
  slug: telefonica-kycmatchresponse
- name: LocationVerificationRequest
  property_count: 3
  slug: telefonica-locationverificationrequest
- name: LocationVerificationResponse
  property_count: 3
  slug: telefonica-locationverificationresponse
- name: NumberVerificationRequest
  property_count: 2
  slug: telefonica-numberverificationrequest
- name: NumberVerificationResponse
  property_count: 1
  slug: telefonica-numberverificationresponse
- name: Telefónica Quality on Demand Session
  property_count: 7
  slug: telefonica-qod-session
- name: RoamingStatusResponse
  property_count: 4
  slug: telefonica-roamingstatusresponse
- name: SessionInfo
  property_count: 7
  slug: telefonica-sessioninfo
- name: SimSwapCheckRequest
  property_count: 2
  slug: telefonica-simswapcheckrequest
- name: SimSwapCheckResponse
  property_count: 1
  slug: telefonica-simswapcheckresponse
json_structures:
- name: Telefonica Device Structure
  property_count: 0
  slug: telefonica-device-structure
- name: Telefonica Structure
  property_count: 0
  slug: telefonica-structure
jsonld:
- class_count: 38
  name: Telefonica Context
  property_count: 0
  slug: telefonica-context
layout: provider
modified: '2026-05-19'
name: Telefónica
nav: Providers
network: true
overview: 'Telefónica publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Device Roaming API, KYC Match API, Location Verification API, and 3 more. Tagged areas include Telecommunications, Mobile Network, CAMARA, Open Gateway, and Authentication.


  The Telefónica catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Telefónica''s developer surface includes authentication, documentation, GitHub presence, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Telefonica Plans Pricing
  plan_count: 2
  slug: telefonica-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Telefonica Rate Limits
  slug: telefonica-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Telefónica API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: telefonica-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Telefónica API Rules
  rule_count: 11
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 6
  slug: telefonica-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 68.9
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telefonica/refs/heads/main/screenshots/telefonica-2026-06-20T195129.png
security:
- kind: authentication
  name: Telefonica Authentication
  slug: telefonica-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Telefonica Domain Security
  slug: telefonica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telefonica
tags:
- Telecommunications
- Mobile Network
- CAMARA
- Open Gateway
- Authentication
- Fraud Prevention
- Location Services
website: https://opengateway.telefonica.com/en
---
