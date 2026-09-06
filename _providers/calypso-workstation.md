---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Calypso Workstation is the end-user desktop application for the Nasdaq Calypso platform. It delivers real-time market data, trade entry, order management, risk monitoring, P&L, scenario analysis, and '
  name: Calypso Workstation
  slug: calypso-workstation
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calypso-workstation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nasdaq.com/products/fintech/calypso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaq.com/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasdaq.com/legal
- group: operate
  title: ''
  type: Support
  url: https://www.nasdaq.com/contact-us
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nasdaq.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: security/calypso-workstation-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/calypso-workstation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/calypso-workstation-vulnerability-disclosure.yml
- group: learn
  title: ''
  type: Learning
  url: https://learncalypso.nasdaq.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/calypso-workstation-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Nasdaq publishes no API reference for Calypso at all — the product and Front Office Workstation pages contain zero mentions of an API — and the Calypso technical documentation reachable from them lives in the Okta-authenticated Nasdaq Customer Portal, where /client/resources 302s to /auth/login; the pre-acquisition calypso.com domain that once carried the developer surface now resolves to 72.167.45.186 and times out on both 80 and 443.
  evidence:
  - status: 302
    url: https://customerportal.nasdaq.com/client/resources
  - status: 200
    url: https://www.nasdaq.com/products/fintech/calypso
  - status: 404
    url: https://www.nasdaq.com/openapi.json
  - status: 0
    url: https://www.calypso.com/
  reason: customer-only-docs
  state: gated
created: '2024-01-15'
description: Nasdaq Calypso Workstation is the user-facing desktop component of the Nasdaq Calypso (formerly Adenza / Calypso Technology) capital markets platform. It gives capital markets professionals access to market data, trading operations, risk management, and portfolio analytics across asset classes. The Workstation is an integrated client application rather than a publicly documented REST API; programmatic integration is delivered through the broader Calypso platform interfaces used by banks, asset managers, central banks, and clearing houses.
finops:
- name: Calypso Workstation Finops
  service_category: API
  slug: calypso-workstation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calypso-workstation.png
layout: provider
modified: '2026-04-23'
name: Calypso Workstation
nav: Providers
network: true
overview: 'Calypso Workstation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Financial Technology, Market Data, Portfolio-Management, and Risk Management.


  Calypso Workstation''s developer surface includes support and 10 more developer resources.'
plans:
- name: Calypso Workstation Plans Pricing
  plan_count: 0
  slug: calypso-workstation-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Calypso Workstation Rate Limits
  slug: calypso-workstation-rate-limits
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 30.3
    commercial_clarity: 30.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calypso-workstation/refs/heads/main/screenshots/calypso-workstation-2026-06-20T173905.png
security:
- kind: domain-security
  name: Calypso Workstation Domain Security
  slug: calypso-workstation-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Calypso Workstation Vulnerability Disclosure
  slug: calypso-workstation-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Calypso Workstation Trust Center
  slug: calypso-workstation-trust-center
  summary_line: trust center published
slug: calypso-workstation
tags:
- Capital Markets
- Financial Technology
- Market Data
- Portfolio-Management
- Risk Management
- Trading
website: https://www.nasdaq.com/products/fintech/calypso
---
