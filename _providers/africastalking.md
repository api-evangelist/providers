---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
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
    auth_clarity: bearer
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
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Africastalking Agentic Access
  operation_count: 14
  slug: africastalking-agentic-access
  summary_line: 14 operations · 12 acting
api_count: 1
apis:
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Distribute mobile airtime to recipients.
  name: Africa's Talking Airtime API
  slug: africastalking-airtime-api
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Disburse mobile data bundles to recipients.
  name: Africa's Talking Mobile Data API
  slug: africastalking-mobile-data-api
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Mobile C2B checkout, B2C, and B2B mobile money transfers.
  name: Africa's Talking Payments API
  slug: africastalking-payments-api
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Premium SMS subscriptions and checkout tokens.
  name: Africa's Talking Premium SMS API
  slug: africastalking-premium-sms-api
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Send single and bulk SMS and fetch inbox messages.
  name: Africa's Talking SMS API
  slug: africastalking-sms-api
- baseURL: https://api.africastalking.com/version1
  baseurl_source: declared
  description: Outbound calls, transfers, queue status, and media upload.
  name: Africa's Talking Voice API
  slug: africastalking-voice-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Africa's Talking Airtime API
  slug: open-africastalking-airtime-api
- collection_type: open
  name: Africa's Talking Airtime Mobile Data API
  slug: open-africastalking-mobile-data-api
- collection_type: open
  name: Africa's Talking Airtime Payments API
  slug: open-africastalking-payments-api
- collection_type: open
  name: Africa's Talking Airtime Premium SMS API
  slug: open-africastalking-premium-sms-api
- collection_type: open
  name: Africa's Talking Airtime SMS API
  slug: open-africastalking-sms-api
- collection_type: open
  name: Africa's Talking Airtime Voice API
  slug: open-africastalking-voice-api
- collection_type: open
  name: Africa's Talking API
  slug: open-africastalking
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/africastalking-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/africastalking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/africastalking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/africastalking-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AfricasTalkingLtd
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/africa-s-talking
- group: company
  title: ''
  type: Website
  url: https://africastalking.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.africastalking.com
- group: commercial
  title: ''
  type: Plans
  url: plans/africastalking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/africastalking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/africastalking-finops.yml
created: '2026-06-20'
description: Africa's Talking is a pan-African communications platform that exposes a unified set of REST APIs for SMS, USSD, Voice, Airtime, Mobile Data, and Payments. Developers authenticate with an apiKey and username and reach mobile subscribers across Kenya, Nigeria, Uganda, Tanzania, Rwanda, and other African markets through carrier integrations.
finops:
- name: Africastalking Finops
  service_category: Communications
  slug: africastalking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/africastalking.png
layout: provider
modified: '2026-06-20'
name: Africa's Talking
nav: Providers
network: true
overview: 'Africa''s Talking publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Airtime API, Mobile Data API, Payments API, and 3 more. Tagged areas include Communications, SMS, USSD, Voice, and Airtime.


  Africa''s Talking''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Africastalking Plans Pricing
  plan_count: 2
  slug: africastalking-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Africastalking Rate Limits
  slug: africastalking-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.3
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 31.8
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
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/africastalking/refs/heads/main/screenshots/africastalking-2026-06-20T165713.png
security:
- kind: authentication
  name: Africastalking Authentication
  slug: africastalking-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Africastalking Domain Security
  slug: africastalking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: africastalking
tags:
- Communications
- SMS
- USSD
- Voice
- Airtime
- Mobile Data
- Payments
- Africa
website: https://africastalking.com
---
