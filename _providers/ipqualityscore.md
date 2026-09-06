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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Ipqualityscore Agentic Access
  operation_count: 6
  slug: ipqualityscore-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The Device Fingerprint API from IPQualityScore — 1 operation(s) for device fingerprint.
  name: IPQualityScore Device Fingerprint API
  slug: ipqualityscore-device-fingerprint-api
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The Email Validation API from IPQualityScore — 1 operation(s) for email validation.
  name: IPQualityScore Email Validation API
  slug: ipqualityscore-email-validation-api
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The IP Reputation API from IPQualityScore — 1 operation(s) for ip reputation.
  name: IPQualityScore IP Reputation API
  slug: ipqualityscore-ip-reputation-api
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The Leaked Data API from IPQualityScore — 1 operation(s) for leaked data.
  name: IPQualityScore Leaked Data API
  slug: ipqualityscore-leaked-data-api
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The Phone Validation API from IPQualityScore — 1 operation(s) for phone validation.
  name: IPQualityScore Phone Validation API
  slug: ipqualityscore-phone-validation-api
- baseURL: https://www.ipqualityscore.com/api/json
  baseurl_source: declared
  description: The URL Scanner API from IPQualityScore — 1 operation(s) for url scanner.
  name: IPQualityScore URL Scanner API
  slug: ipqualityscore-url-scanner-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IPQualityScore Device Fingerprint API
  slug: open-ipqualityscore-device-fingerprint-api
- collection_type: open
  name: IPQualityScore Device Fingerprint Email Validation API
  slug: open-ipqualityscore-email-validation-api
- collection_type: open
  name: IPQualityScore Device Fingerprint IP Reputation API
  slug: open-ipqualityscore-ip-reputation-api
- collection_type: open
  name: IPQualityScore Device Fingerprint Leaked Data API
  slug: open-ipqualityscore-leaked-data-api
- collection_type: open
  name: IPQualityScore Device Fingerprint Phone Validation API
  slug: open-ipqualityscore-phone-validation-api
- collection_type: open
  name: IPQualityScore Device Fingerprint URL Scanner API
  slug: open-ipqualityscore-url-scanner-api
- collection_type: open
  name: IPQualityScore API
  slug: open-ipqualityscore
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ipqualityscore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipqualityscore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ipqualityscore-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IPQualityScore
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ipqualityscore
- group: company
  title: ''
  type: Website
  url: https://www.ipqualityscore.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ipqualityscore.com/documentation/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/ipqualityscore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ipqualityscore-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ipqualityscore-finops.yml
created: '2026-06-25'
description: IPQualityScore (IPQS) provides real-time fraud prevention and threat intelligence APIs covering proxy/VPN/Tor and IP reputation scoring, email and phone validation, malicious URL and domain scanning, device fingerprinting, transaction risk scoring, and dark-web leaked-data checks. All endpoints are delivered as a simple REST/JSON interface with the API key passed in the request path.
finops:
- name: Ipqualityscore Finops
  service_category: Identity and Security
  slug: ipqualityscore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipqualityscore.png
layout: provider
modified: '2026-06-25'
name: IPQualityScore
nav: Providers
network: true
overview: 'IPQualityScore publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Device Fingerprint API, Email Validation API, IP Reputation API, and 3 more. Tagged areas include Fraud Prevention, IP Reputation, Proxy Detection, Email Validation, and Threat Intelligence.


  IPQualityScore''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Ipqualityscore Plans Pricing
  plan_count: 5
  slug: ipqualityscore-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Ipqualityscore Rate Limits
  slug: ipqualityscore-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipqualityscore/refs/heads/main/screenshots/ipqualityscore-2026-07-25T222839.png
security:
- kind: authentication
  name: Ipqualityscore Authentication
  slug: ipqualityscore-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ipqualityscore Domain Security
  slug: ipqualityscore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ipqualityscore
tags:
- Fraud Prevention
- IP Reputation
- Proxy Detection
- Email Validation
- Threat Intelligence
website: https://www.ipqualityscore.com
---
