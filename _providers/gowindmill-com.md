---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
  score: 30.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Programmatic access to Windmill performance management features.
  name: Windmill API
  slug: windmill-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/gowindmill-com/plans/gowindmill-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gowindmill-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/gowindmill-com/llms/gowindmill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gowindmill-com-llms.txt
- group: other
  href: https://artifacts.apis.io/gowindmill-com/a2a/gowindmill-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gowindmill-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gowindmill-com/well-known/gowindmill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gowindmill-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gowindmill-com/hosts/gowindmill-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gowindmill-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gowindmill-com/vendors/gowindmill-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gowindmill-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://help.gowindmill.com/security/pii
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.gowindmill.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.gowindmill.com/getting-started/initial-setup
- group: auth
  href: https://artifacts.apis.io/gowindmill-com/security/gowindmill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gowindmill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gowindmill.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://gowindmill.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://gowindmill.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.gowindmill.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gowindmill.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gowindmill.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gowindmill.com/legal/privacy-policy/
coverage:
  detail: Documentation pages are served as markdown via llms.txt but no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://help.gowindmill.com/llms.txt
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Windmill provides an AI‑powered performance management platform that automates reviews, 1‑on‑1 agendas, onboarding, continuous feedback and calibration. It helps modern teams run faster, achieve higher employee satisfaction and gain data‑driven insights, with integrations for Slack, Jira, Notion and more. The service targets HR and people‑ops professionals seeking to modernize performance reviews with AI.
image: https://gowindmill.com/index.png/
layout: provider
modified: '2026-10-29'
name: Windmill
nav: Providers
network: true
overview: 'Windmill is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Performance-Management, HRTech, and SaaS.


  Windmill''s developer surface includes changelog, getting-started guide, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Gowindmill Com Plans Pricing
  plan_count: 3
  slug: gowindmill-com-plans-pricing
random_paper: 2
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gowindmill Com Domain Security
  slug: gowindmill-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gowindmill-com
tags:
- Company
- AI
- Performance-Management
- HRTech
- SaaS
website: https://gowindmill.com/
---
