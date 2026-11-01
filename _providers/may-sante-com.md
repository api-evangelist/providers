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
  href: https://artifacts.apis.io/may-sante-com/hosts/may-sante-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/may-sante-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/may-sante-com/vendors/may-sante-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/may-sante-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.may.app/en/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/may-sante-com/security/may-sante-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/may-sante-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://may-sante.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.may.app/
- group: company
  title: ''
  type: Blog
  url: https://www.may.app/blog
created: '2026-10-24'
description: May is a French digital health company offering a parenting app that supports families from pregnancy through early childhood. The platform provides personalized guidance, educational content, and tools for tracking development milestones, sleep, nutrition, and health. May leverages AI to deliver tailored advice and connects parents with experts, aiming to improve child wellbeing and parental confidence.
image: https://www.may.app/wp-content/uploads/2025/05/logo_may_sapin_fond_transparent.png
layout: provider
modified: '2026-10-24'
name: May
nav: Providers
network: true
overview: 'May is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Parenting, DigitalHealth, and AI.


  May''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 8
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
    score: 7.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: May Sante Com Domain Security
  slug: may-sante-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: may-sante-com
tags:
- Company
- Health
- Parenting
- DigitalHealth
- AI
website: https://may-sante.com/
---
