---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/fetchrev-com/plans/fetchrev-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fetchrev-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/fetchrev-com/hosts/fetchrev-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fetchrev-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/fetchrev-com/security/fetchrev-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fetchrev-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fetchrev.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.locbox.com/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://fetchrev.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fetchrev.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fetchrev.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://fetchrev.com/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://fetchrev.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: LocBox Labs, operating under the brand FetchRev, provides an automated marketing platform for local businesses. It enables merchants to create instant promotions, capture customer emails, and drive repeat visits through web, social, and mobile channels. The service includes pay‑per‑visit billing, a results dashboard, and integrations with point‑of‑sale systems, aiming to boost revenue and customer loyalty for venues such as family entertainment centers, health & beauty salons, and home services. Backed by 500‑global, the company focuses on effortless, data‑driven marketing automation for local enterprises.
image: https://s21644.pcdn.co/wp-content/uploads/2018/09/Dallas_BuyNow-e1543173393593.png
layout: provider
modified: '2026-10-21'
name: LocBox Labs
nav: Providers
network: true
overview: 'LocBox Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Automation, Local Business, and Software-as-a-Service.


  LocBox Labs'' developer surface includes pricing, support, and 7 more developer resources.'
plans:
- name: Fetchrev Com Plans Pricing
  plan_count: 3
  slug: fetchrev-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.1
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/fetchrev-com/fetchrev-com-2026-11-03T131939.png
security:
- kind: domain-security
  name: Fetchrev Com Domain Security
  slug: fetchrev-com-domain-security
  summary_line: TLSv1.3
slug: fetchrev-com
tags:
- Company
- Marketing
- Automation
- Local Business
- Software-as-a-Service
website: https://fetchrev.com
---
