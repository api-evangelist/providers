---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
  href: https://artifacts.apis.io/cardcenteringtool-com/plans/cardcenteringtool-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardcenteringtool-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cardcenteringtool-com/llms/cardcenteringtool-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardcenteringtool-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cardcenteringtool-com/hosts/cardcenteringtool-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardcenteringtool-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardcenteringtool-com/vendors/cardcenteringtool-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardcenteringtool-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardcenteringtool.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardcenteringtool.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.cardcenteringtool.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.cardcenteringtool.com/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cardcenteringtool.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.cardcenteringtool.com/
- group: auth
  href: https://artifacts.apis.io/cardcenteringtool-com/security/cardcenteringtool-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardcenteringtool-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardcenteringtool.com/
coverage:
  checked: '2026-11-03'
  detail: The provider offers a card grading web app but publishes no public API documentation or machine‑readable contracts.
  evidence:
  - status: 200
    url: https://www.cardcenteringtool.com/
  reason: tenant-only
  state: none
created: '2026-11-03'
description: Card Centering Tool provides a platform for grading, centering measurement, live pricing, and portfolio tracking of trading cards, including Pokémon, TCG, sports and entertainment cards. Users can measure card centering, obtain AI-driven grades, view real-time market values for over 1.5 million cards, and manage their collections through a comprehensive dashboard.
image: https://www.cardcenteringtool.com/og-card.png
layout: provider
modified: '2026-11-03'
name: Card Centering Tool
nav: Providers
network: true
overview: 'Card Centering Tool is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cards, Grading, Trading Cards, and Marketplace.


  Card Centering Tool''s developer surface includes documentation, changelog, engineering blog, and 9 more developer resources.'
plans:
- name: Cardcenteringtool Com Plans Pricing
  plan_count: 1
  slug: cardcenteringtool-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 39.3
    operational_transparency: 7.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardcenteringtool Com Domain Security
  slug: cardcenteringtool-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cardcenteringtool-com
tags:
- Cards
- Grading
- Trading Cards
- Marketplace
website: https://www.cardcenteringtool.com/
---
