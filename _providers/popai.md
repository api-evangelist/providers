---
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/popai/hosts/popai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/popai-hosts.yml
- group: other
  href: https://artifacts.apis.io/popai/vendors/popai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/popai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/popai/security/popai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/popai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.popai.health/
- group: docs
  title: ''
  type: Documentation
  url: https://www.popai.health/
- group: company
  title: ''
  type: Blog
  url: https://www.popai.health/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.popai.health/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.popai.health/contact-us
created: '2026-10-22'
description: Popai Health leverages voice AI to capture patient context from everyday conversations, turning these signals into deep insights that personalize care, improve risk detection, and enhance outcomes. By automating documentation, coaching, and engagement, Popai enables healthcare teams to understand barriers, motivations, and preferences, integrating seamlessly with existing records and workflows to drive better quality of care.
image: https://cdn.prod.website-files.com/67111c446df6f1687a001426/6aa38cc51045600a5e87fcb5_popai%20cover.jpeg
layout: provider
modified: '2026-10-22'
name: Popai
nav: Providers
network: true
overview: 'Popai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Voice AI, Patient Context, and Digital Health.


  Popai''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Popai Domain Security
  slug: popai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: popai
tags:
- Company
- Healthcare
- Voice AI
- Patient Context
- Digital Health
website: https://www.popai.health/
---
