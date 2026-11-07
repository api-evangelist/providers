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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/dooit-so/llms/dooit-so-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dooit-so-llms.txt
- group: agent
  href: https://artifacts.apis.io/dooit-so/well-known/dooit-so-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dooit-so-well-known.yml
- group: other
  href: https://artifacts.apis.io/dooit-so/hosts/dooit-so-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dooit-so-hosts.yml
- group: other
  href: https://artifacts.apis.io/dooit-so/vendors/dooit-so-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dooit-so-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dooit.so/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dooit.so/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://dooit.so/blog
- group: auth
  href: https://artifacts.apis.io/dooit-so/security/dooit-so-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dooit-so-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dooit.so/
coverage:
  checked: '2026-11-05'
  detail: The provider's website offers no developer documentation or API reference, and no contract was found.
  evidence:
  - status: 200
    url: https://dooit.so/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: Dooit provides an ultra‑minimal task management web app designed to help users plan their day and achieve goals. The service emphasizes a calm, distraction‑free interface and offers features such as daily planning, goal tracking, and a simple, clean UI. It is hosted at dooit.so and targets individuals seeking a lightweight productivity tool.
layout: provider
modified: '2026-11-05'
name: Dooit
nav: Providers
network: true
overview: 'Dooit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Task Management, Minimalist, Web App, and Dooit.


  Dooit''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dooit So Domain Security
  slug: dooit-so-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dooit-so
tags:
- Productivity
- Task Management
- Minimalist
- Web App
- Dooit
website: https://dooit.so/
---
