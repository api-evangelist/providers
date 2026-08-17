---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'The nine partner APIs Flash publishes for Flash PARCS and Flash Valet: eParking (inject and manage parking reservations), Locations (real-time occupancy, garage status and active pricing), Monthly (mo'
  name: Flash Platform Partner APIs
  slug: flash-platform-apis
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flashparking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flashparking.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.flashos.com/support/home
- group: docs
  title: ''
  type: APIReference
  url: https://help.flashos.com/support/solutions/articles/60001639636-api-integrations-with-flash-parcs-and-flash-valet
- group: operate
  title: ''
  type: Support
  url: https://help.flashos.com/support/tickets/new
- group: company
  title: ''
  type: Blog
  url: https://www.flashparking.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.flashparking.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FlashParking-Inc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flashparking.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.flashparking.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://www.flashparking.com/sign-in/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flashparking.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flashparking.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flashparking.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.flashos.com/support/solutions/60000334952
- group: auth
  title: ''
  type: Compliance
  url: https://www.flashparking.com/news-press/flashparkings-innovative-system-passes-annual-pci-dss-compliance-audit/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flashparking-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flashparking-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flashparking-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flashparking-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flashparking-llms.txt
coverage:
  checked: '2026-08-16'
  detail: Flash names nine partner APIs in a single Freshdesk help-center article but publishes no base URL, no authentication model and no specification for any of them - the article ends at "contact sales@flashparking.com for pricing", and sandbox certification plus production access are sold as a paid monthly add-on.
  evidence:
  - status: 200
    url: https://help.flashos.com/support/solutions/articles/60001639636-api-integrations-with-flash-parcs-and-flash-valet
  - status: 0
    url: https://developer.flashparking.com/
  - status: 0
    url: https://api.flashparking.com/
  - status: 404
    url: https://www.flashparking.com/openapi.json
  - status: 404
    url: https://www.flashparking.com/developers/
  - status: 404
    url: https://www.flashparking.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-08-16'
description: 'Flash (formerly FlashParking) is an Austin, Texas parking technology company that sells an end-to-end mobility platform to parking asset owners and operators: cloud software (FlashOS), purpose-built PARCS gate and kiosk hardware, Flash Vision LPR/computer-vision cameras, valet and enforcement applications, EV charging, accounts-receivable automation, and a consumer Demand Network reached through its ParkWhiz/Arrive brands. Flash publishes a named catalog of nine partner APIs for Flash PARCS and Flash Valet - eParking, Locations, Monthly, Validations, Customer Service, Price Manager, FlashPass, Vehicle Request and Flash Receipt - used by partners including Ticketmaster, SpotHero, LAZ Parking, Genea and Daktronics. Those APIs are commercially gated: the help center documents what each API does but publishes no base URL, no authentication model and no machine-readable specification, and sandbox certification plus production access carry monthly fees arranged through sales@flashparking.com.'
image: https://www.flashparking.com/wp-content/uploads/flash-fallback.jpg
layout: provider
modified: '2026-08-16'
name: Flashparking
nav: Providers
network: true
overview: 'Flashparking publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Parking, Mobility, Transportation, and Payments.


  Flashparking''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, changelog, and 14 more developer resources.'
plans:
- name: Flashparking Plans Pricing
  plan_count: 0
  slug: flashparking-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 0
  name: Flashparking Rate Limits
  slug: flashparking-rate-limits
score:
  band: thin
  composite: 30.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 37.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
security:
- kind: domain-security
  name: Flashparking Domain Security
  slug: flashparking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flashparking
tags:
- Company
- Parking
- Mobility
- Transportation
- Payments
- Internet of Things
- Computer Vision
- Real Estate
- Electric Vehicle Charging
- Reservations
website: https://www.flashparking.com/
---
