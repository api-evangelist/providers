---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for BoxToPlay services
  name: BoxToPlay API
  slug: boxtoplay-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/boxtoplay-com/plans/boxtoplay-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boxtoplay-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/boxtoplay-com/conformance/boxtoplay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boxtoplay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boxtoplay-com/llms/boxtoplay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boxtoplay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/boxtoplay-com/well-known/boxtoplay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boxtoplay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boxtoplay-com/hosts/boxtoplay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boxtoplay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boxtoplay-com/vendors/boxtoplay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boxtoplay-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boxtoplay.com/en/privacy
- group: auth
  href: https://artifacts.apis.io/boxtoplay-com/security/boxtoplay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boxtoplay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boxtoplay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.boxtoplay.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.boxtoplay.com/docs
- group: operate
  title: ''
  type: Support
  url: https://www.boxtoplay.com/en/faq
- group: company
  title: ''
  type: Blog
  url: https://www.boxtoplay.com/en/news
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.boxtoplay.com/v1/openapi.json
  - status: 401
    url: https://api.boxtoplay.com/mcp
  - status: 200
    url: https://boxtoplay.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: BoxToPlay provides high‑performance Minecraft, VPS, and TeamSpeak server hosting with 24/7 support, a feature‑rich control panel, and optional free Minecraft server trials. Customers can choose from a variety of plans, manage servers via a web dashboard, and integrate with popular modpacks. The service also offers a Discord community, API & MCP access, and mobile apps for iOS and Android, catering to gamers and developers seeking reliable game server infrastructure.
image: https://www.boxtoplay.com/assets/frontend/img/boxtoplay-og-en.png
layout: provider
modified: '2026-11-02'
name: BoxToPlay
nav: Providers
network: true
overview: 'BoxToPlay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, Gaming, Minecraft, VPS, and TeamSpeak.


  BoxToPlay''s developer surface includes documentation, API reference, support, engineering blog, and 9 more developer resources.'
plans:
- name: Boxtoplay Com Plans Pricing
  plan_count: 5
  slug: boxtoplay-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boxtoplay Com Domain Security
  slug: boxtoplay-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: boxtoplay-com
tags:
- Hosting
- Gaming
- Minecraft
- VPS
- TeamSpeak
website: https://boxtoplay.com/
---
