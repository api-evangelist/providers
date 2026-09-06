---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Partner-facing REST API for distributing prepaid vehicle access. Documented resources include wallet creation and management, PSP-orchestrated top-ups, ledger / transaction history, and webhook regist
  name: Mobillis Open API
  slug: mobillis-open-api
artifact_total: 3
asyncapis:
- description: ''
  name: Mobillis Webhooks
  slug: mobillis-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobillis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mobillis.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auth.mobillis.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auth.mobillis.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://auth.mobillis.com/
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mobillis-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mobillis-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mobillis-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobillis-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobillis-llms.txt
created: '2026-07-17'
description: Mobillis, operated by Reflex Mobility, Inc., is a fintech mobility platform that turns vehicle fleet inventory into a prepaid billing and access product. It sits as an overlay on top of legacy rental and fleet systems rather than replacing them, letting fleet operators collect payment upfront and reach new "everyday driver" segments, while non-fleet distribution partners resell vehicle access through referral links, a white-label front end, or the Mobillis Open APIs. The documented API surface covers wallet creation and management, PSP-orchestrated top-ups, ledger and transaction-history access, and webhook events for low-balance alerts and billing triggers. Mobillis operates from Johannesburg and New York.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mobillis.png
layout: provider
modified: '2026-07-20'
name: Mobillis
nav: Providers
network: true
overview: 'Mobillis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Mobility, Payments, and Wallets.


  The Mobillis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mobillis'' developer surface includes signup flow and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 0.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 23.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobillis/refs/heads/main/screenshots/mobillis-2026-08-07T183851.png
security:
- kind: domain-security
  name: Mobillis Domain Security
  slug: mobillis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mobillis
tags:
- Company
- Fintech
- Mobility
- Payments
- Wallets
- Fleet Management
- Prepaid
- Webhook
- Ledger
website: https://mobillis.com/
---
