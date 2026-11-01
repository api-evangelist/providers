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
  href: https://artifacts.apis.io/hirundo/hosts/hirundo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hirundo-hosts.yml
- group: other
  href: https://artifacts.apis.io/hirundo/vendors/hirundo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hirundo-vendors.yml
- group: build
  href: https://artifacts.apis.io/hirundo/packages/hirundo-packages.yml
  title: ''
  type: SDKs
  url: packages/hirundo-packages.yml
- group: build
  href: https://artifacts.apis.io/hirundo/packages/hirundo-packages.yml
  title: ''
  type: Packages
  url: packages/hirundo-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hirundo.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hirundo.io/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.hirundo.io/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hirundo.io/
- group: auth
  href: https://artifacts.apis.io/hirundo/security/hirundo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hirundo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hirundo.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://hirundo.io/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Hirundo provides a machine unlearning platform that surgically removes risky knowledge and behavior from trained large language models at the model level, without retraining. The service is aimed at AI and product teams, security and privacy teams, and frontier AI labs that need to mitigate jailbreaks, hallucinations, bias, and memorized PII in production models. It enables enterprises to fix model risks quickly, reducing launch delays and improving compliance.
image: https://cdn.prod.website-files.com/660ac5137d0f7fda07d7ce65/6612706c7c1f0f80e8973596_Hirundo%20OpenGraph%20Image.png
layout: provider
modified: '2026-10-20'
name: Hirundo
nav: Providers
network: true
overview: 'Hirundo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Machine Unlearning, AI Safety, Model Security, and Data Privacy.


  Hirundo''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 39.3
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Hirundo Domain Security
  slug: hirundo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hirundo
tags:
- Machine Unlearning
- AI Safety
- Model Security
- Data Privacy
website: https://hirundo.io/
---
