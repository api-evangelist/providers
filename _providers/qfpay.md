---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer portal providing OpenAPI documentation and integration guides for QFPay payment solutions.
  name: QFPay Developer Centre
  slug: qfpay-developer-centre
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/qfpay/llms/qfpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qfpay-llms.txt
- group: other
  href: https://artifacts.apis.io/qfpay/a2a/qfpay-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/qfpay-a2a.yml
- group: other
  href: https://artifacts.apis.io/qfpay/hosts/qfpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qfpay-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qfpay.global/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qfpay.global/documents/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://qfpay.global/news/
- group: company
  title: ''
  type: Blog
  url: https://qfpay.global/blog/
- group: auth
  href: https://artifacts.apis.io/qfpay/security/qfpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qfpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qfpay.global/
coverage:
  checked: '2026-10-27'
  detail: Developer portal provides an OpenAPI file but it describes a sample plant store, not QFPay's API.
  evidence:
  - status: 200
    url: https://sdk.qfapi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: QFPay provides payment solutions including credit card and QR code payments, enabling businesses to accept online payments quickly, securely, and efficiently. The company positions itself as a best‑in‑class payment partner helping merchants thrive in the cashless era, with services spanning pay‑in, pay‑out, financing, and developer tools.
image: https://qfpay.global/wp-content/uploads/2023/11/talking-cashier-2.png
layout: provider
modified: '2026-10-27'
name: QFPay
nav: Providers
network: true
overview: 'QFPay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payment, FinTech, API, and Payments.


  QFPay''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qfpay Domain Security
  slug: qfpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qfpay
tags:
- Company
- Payment
- FinTech
- API
- Payments
website: https://qfpay.global/
---
