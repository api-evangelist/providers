---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 10.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/joy-co/plans/joy-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/joy-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/joy-co/llms/joy-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joy-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/joy-co/well-known/joy-co-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/joy-co-help-security.txt
- group: agent
  href: https://artifacts.apis.io/joy-co/well-known/joy-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joy-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/joy-co/hosts/joy-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joy-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/joy-co/vendors/joy-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joy-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joy.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joy.co/privacy-policy/
- group: start
  title: ''
  type: GettingStarted
  url: https://joy.co/baby-led-weaning-a-complete-guide-to-getting-started-safely/
- group: docs
  title: ''
  type: Documentation
  url: https://help.joy.co/
- group: auth
  href: https://artifacts.apis.io/joy-co/security/joy-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joy-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joy.co
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://joy.co
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Joy offers a subscription-based parenting club that provides expert‑backed toolkits, 24/7 human support, personalized insights, and 1:1 video consultations for parents in the United States. Members can track daily baby activities, access resources on feeding, sleep, behavior, and receive exclusive discounts on family products.
image: https://joy.co/images/external/home/Homepage_Expert_Joy-v2-1700x1296.png
layout: provider
modified: '2026-10-22'
name: Joy
nav: Providers
network: true
overview: 'Joy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Parenting, Expert Advice, Tracker, Telehealth, and Family Support.


  Joy''s developer surface includes getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Joy Co Plans Pricing
  plan_count: 8
  slug: joy-co-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Joy Co Domain Security
  slug: joy-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joy-co
tags:
- Parenting
- Expert Advice
- Tracker
- Telehealth
- Family Support
website: https://joy.co
---
