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
  href: https://artifacts.apis.io/bidwellhealth-com/plans/bidwellhealth-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bidwellhealth-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bidwellhealth-com/llms/bidwellhealth-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidwellhealth-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bidwellhealth-com/hosts/bidwellhealth-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidwellhealth-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bidwellhealth-com/vendors/bidwellhealth-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bidwellhealth-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidwellhealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidwellhealth.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bidwellhealth.com/press
- group: auth
  href: https://artifacts.apis.io/bidwellhealth-com/security/bidwellhealth-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidwellhealth-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidwellhealth.com/
- group: company
  title: ''
  type: Blog
  url: https://bidwellhealth.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bidwellhealth.com/pricing
- group: company
  title: ''
  type: About
  url: https://bidwellhealth.com/about
- group: operate
  title: ''
  type: Contact
  url: https://bidwellhealth.com/contact
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider’s API host.
  evidence:
  - status: DNS error
    url: https://api.bidwellhealth.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bidwell Health is a clinician‑led online telehealth practice serving adults in eleven U.S. states. It offers cash‑pay $45 clinician visits for urinary‑tract infections, bacterial vaginosis, yeast infections, erectile dysfunction, hair loss, eyelash growth, herpes, and prescription refills, all via video or chat. The service emphasizes privacy, licensed providers, and evidence‑based care.
image: https://bidwellhealth.com/assets/og-image-11-states-20261018.png
layout: provider
modified: '2026-11-02'
name: Bidwell Health
nav: Providers
network: true
overview: 'Bidwell Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Telehealth, Healthcare, Online Visits, Cash Pay, and US.


  Bidwell Health''s developer surface includes engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Bidwellhealth Com Plans Pricing
  plan_count: 1
  slug: bidwellhealth-com-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidwellhealth Com Domain Security
  slug: bidwellhealth-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bidwellhealth-com
tags:
- Telehealth
- Healthcare
- Online Visits
- Cash Pay
- US
website: https://bidwellhealth.com/
---
