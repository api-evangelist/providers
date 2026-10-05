---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-04'
api_count: 3
apis:
- description: Real-Time Funding API providing transaction operations.
  name: Money API
  slug: money-api
- baseURL: https://customer.api.securenet.live
  baseurl_source: declared
  description: The Ping API from AppBrilliance — 1 operation(s) for ping.
  name: AppBrilliance Ping API
  slug: appbrilliance-ping-api
- baseURL: https://customer.api.securenet.live
  baseurl_source: declared
  description: The Transaction API from AppBrilliance — 1 operation(s) for transaction.
  name: AppBrilliance Transaction API
  slug: appbrilliance-transaction-api
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/appbrilliance/refs/heads/main/security/appbrilliance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appbrilliance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appbrilliance.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.appbrilliance.com/docs/moneyapi/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.appbrilliance.com/docs/moneyapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.appbrilliance.com/docs/moneyapi/getstarted.html
- group: operate
  title: ''
  type: Support
  url: https://appbrilliance.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appbrilliance.com/privacy-policy/
coverage:
  checked: 2026-09-25
  detail: Documentation pages are HTML shells rendered by JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://dev.appbrilliance.com/docs/moneyapi/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: AppBrilliance is revolutionizing digital transactions with its novel Agentic Payments Platform. It enables seamless integration of instant payment systems (RTP & FedNow) and open banking protocols for secure, frictionless transactions. The company holds 9 US patents and focuses on secure, agentic payment solutions for enterprises.
layout: provider
modified: '2026-09-25'
name: AppBrilliance
nav: Providers
network: true
overview: 'AppBrilliance publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Ping API, Transaction API, and 1 more. Tagged areas include Payments, Fintech, Agentic Payments, Open Banking, and Enterprise.


  AppBrilliance''s developer surface includes documentation, API reference, getting-started guide, support, and 3 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 28.6
    contract_governance: 0.0
    contract_quality: 11.7
    developer_ergonomics: 33.3
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Appbrilliance Domain Security
  slug: appbrilliance-domain-security
  summary_line: TLSv1.3 · DMARC
slug: appbrilliance
tags:
- Payments
- Fintech
- Agentic Payments
- Open Banking
- Enterprise
website: https://appbrilliance.com
---
