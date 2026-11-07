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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/askacharge-com/plans/askacharge-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askacharge-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askacharge-com/llms/askacharge-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askacharge-com-llms.txt
- group: other
  href: https://artifacts.apis.io/askacharge-com/hosts/askacharge-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askacharge-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askacharge.com/askacharge/en/legal-notice.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askacharge.com/askacharge/en/privacy.html
- group: start
  title: ''
  type: Login
  url: https://askacharge.com/askacharge/login
- group: company
  title: ''
  type: Blog
  url: https://askacharge.com/askacharge/blog/
- group: auth
  href: https://artifacts.apis.io/askacharge-com/security/askacharge-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askacharge-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askacharge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://askacharge.com/askacharge/docs.html
- group: commercial
  title: ''
  type: Pricing
  url: https://askacharge.com/askacharge/precios.html
coverage:
  checked: '2026-11-01'
  detail: The site provides only a consumer‑facing web portal with no public developer documentation or API endpoints.
  evidence:
  - status: 200
    url: https://askacharge.com/
  reason: tenant-only
  state: none
created: '2026-11-01'
description: Aska Charge provides a cloud‑based CSMS platform for operators of electric vehicle charging stations. The service offers real‑time monitoring, remote OCPP command control, billing integration with Stripe, multi‑brand white‑labeling, and a roaming hub for revenue sharing among operators. It supports both B2B operators and fleet managers, with features like automated tax invoicing, power‑distribution without civil works, and customizable pricing plans. The platform is SaaS, GDPR‑compliant, and available in Spanish and English, targeting hotels, parking facilities, fleets, installers, and municipalities.
layout: provider
modified: '2026-11-01'
name: Aska Charge
nav: Providers
network: true
overview: 'Aska Charge is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, Software-as-a-Service, Charging, Fleet Management, and Billing.


  Aska Charge''s developer surface includes engineering blog, documentation, pricing, and 8 more developer resources.'
plans:
- name: Askacharge Com Plans Pricing
  plan_count: 10
  slug: askacharge-com-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 15.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  previous_composite: 21.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askacharge Com Domain Security
  slug: askacharge-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askacharge-com
tags:
- Electric Vehicles
- Software-as-a-Service
- Charging
- Fleet Management
- Billing
website: https://askacharge.com/
---
