---
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
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Sunsama provides a task management and planning API documented at the Help Center. No machine‑readable contract was found; the documentation is HTML only.
  name: Sunsama API
  slug: sunsama-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/sunsama/plans/sunsama-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sunsama-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://help.sunsama.com/docs/security/vulnerability-disclosure-program
- group: design
  href: https://artifacts.apis.io/sunsama/conformance/sunsama-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sunsama-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sunsama/llms/sunsama-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sunsama-llms.txt
- group: auth
  href: https://artifacts.apis.io/sunsama/well-known/sunsama-sunsama-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sunsama-sunsama-security.txt
- group: auth
  href: https://artifacts.apis.io/sunsama/well-known/sunsama-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sunsama-security.txt
- group: auth
  href: https://artifacts.apis.io/sunsama/well-known/sunsama-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sunsama-app-security.txt
- group: agent
  href: https://artifacts.apis.io/sunsama/well-known/sunsama-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sunsama-well-known.yml
- group: other
  href: https://artifacts.apis.io/sunsama/hosts/sunsama-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sunsama-hosts.yml
- group: other
  href: https://artifacts.apis.io/sunsama/vendors/sunsama-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sunsama-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sunsama/security/sunsama-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sunsama-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sunsama/security/sunsama-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sunsama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sunsama.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sunsama.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sunsama.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sunsama.com/start/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sunsama.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.sunsama.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.sunsama.com/
coverage:
  checked: '2026-10-27'
  detail: Help Center pages are rendered via JavaScript, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.sunsama.com/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Sunsama provides a modern task manager, calendar, and daily planner designed to help professionals achieve work‑life balance. It integrates with popular tools like Asana, Google Calendar, and Slack, offering features such as focused daily planning, distraction‑free task management, and seamless workflow automation. Users can try a 14‑day free trial without a credit card, and the platform is praised for reducing chaos and improving productivity.
image: https://pub-f7ae218077e542729e28e6f8f45a9a40.r2.dev/images/632d75c435342c54efe7c40d_OG%20IMage.jpg
layout: provider
modified: '2026-10-27'
name: Sunsama
nav: Providers
network: true
overview: 'Sunsama is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Task Management, Calendar Integration, and Remote Work.


  Sunsama''s developer surface includes documentation, getting-started guide, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Sunsama Plans Pricing
  plan_count: 3
  slug: sunsama-plans-pricing
random_paper: 16
scopes:
- name: Sunsama Scopes
  scope_count: 0
  slug: sunsama-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sunsama Domain Security
  slug: sunsama-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sunsama Vulnerability Disclosure
  slug: sunsama-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sunsama
tags:
- Company
- Productivity
- Task Management
- Calendar Integration
- Remote Work
website: https://www.sunsama.com/
---
