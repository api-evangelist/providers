---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/china-southern-air-logistics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/china-southern-air-logistics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://cargo.csair.com/pages/home
- group: company
  title: ''
  type: About
  url: https://cargo.csair.com/pages/CargoIntroduction.do
- group: operate
  title: ''
  type: Support
  url: https://cargo.csair.com/pages/questionAndAnswer.do
- group: operate
  title: ''
  type: Contact
  url: https://cargo.csair.com/pages/contactInfo.do
- group: start
  title: ''
  type: SignUp
  url: https://cargo.csair.com/pages/signupPersonal.do
- group: commercial
  title: ''
  type: Pricing
  url: http://cargo.csair.com/WebFace/Tang.WebFace.RatePolicy/FreightRateCN.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cargo.csair.com/pages/privacyNotice.do
- group: company
  title: ''
  type: News
  url: https://cargo.csair.com/pages/portalList.do
- group: other
  title: ''
  type: Tracking
  url: http://cargo.csair.com/WebFace/Tang.WebFace.Cargo/AgentAwbBrower.aspx
- group: other
  title: ''
  type: ParentCompany
  url: https://www.csairgroup.cn/en/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/china-southern-air-logistics-stock
coverage:
  checked: '2026-08-09'
  detail: The Tang (唐翼) cargo portal at cargo.csair.com is the company's only system surface and it 302-redirects every unknown path back to /pages/home, so nothing under /.well-known/, /openapi.json or /api-docs exists; the one developer-shaped host linked from its own homepage, cargodev.csair.com, does not resolve in public DNS, and there is no developer portal, API reference or SDK page anywhere on cargo.csair.com, tang.csair.com or csairgroup.cn.
  evidence:
  - status: 200
    url: https://cargo.csair.com/pages/home
  - status: 302
    url: https://cargo.csair.com/openapi.json
  - status: 302
    url: https://cargo.csair.com/.well-known/agent-card.json
  - status: 404
    url: https://tang.csair.com/.well-known/agent-card.json
  - status: 404
    url: https://www.csairgroup.cn/openapi.json
  - status: 0
    url: https://cargodev.csair.com/publish_index/
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: China Southern Air Logistics Co., Ltd. (南航物流, CSAL) is the air cargo and logistics arm of China Southern Airlines, established in December 2018 and headquartered in Guangzhou. It combines the airline's freighter fleet with passenger belly capacity into an integrated air logistics network, and sells express (CZ Speed), standard, special cargo, whole-aircraft charter, intermodal truck and door-to-door products through its Tang (唐翼) online cargo system at cargo.csair.com, where agents and shippers book capacity, query freight rates, track air waybills, manage dangerous-goods accounts and request invoices. As of this profile the company publishes no developer program, no public API reference and no machine-readable specification; system-to-system integration is arranged bilaterally with agents and forwarders.
image: https://cargo.csair.com/images/tab-icon.ico
layout: provider
modified: '2026-08-09'
name: China Southern Air Logistics
nav: Providers
network: true
overview: 'China Southern Air Logistics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Air Cargo, Air Freight, Logistics, and Freight.


  China Southern Air Logistics'' developer surface includes support, signup flow, pricing, product news, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/china-southern-air-logistics/refs/heads/main/screenshots/china-southern-air-logistics-2026-09-02T145054.png
security:
- kind: domain-security
  name: China Southern Air Logistics Domain Security
  slug: china-southern-air-logistics-domain-security
  summary_line: TLSv1.2 · DMARC
slug: china-southern-air-logistics
tags:
- Company
- Air Cargo
- Air Freight
- Logistics
- Freight
- Shipping
- Transportation
- Supply Chain
- Aviation
- China
- Cargo Tracking
website: https://cargo.csair.com/pages/home
---
