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
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/asynq-org/llms/asynq-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asynq-org-llms.txt
- group: other
  href: https://artifacts.apis.io/asynq-org/hosts/asynq-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asynq-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/asynq-org/vendors/asynq-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asynq-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asynq-org/security/asynq-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asynq-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asynq.org/
- group: company
  title: ''
  type: Blog
  url: https://asynq.org/blog
- group: operate
  title: ''
  type: Support
  url: https://asynq.org/adr/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asynq.org/adr/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asynq.org/adr/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://asynq.org/adr/pricing
coverage:
  checked: '2026-11-02'
  detail: Attempted to fetch OpenAPI spec at https://asynq.org/openapi.json but received 404.
  evidence:
  - status: 404
    url: https://asynq.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Asynq Labs builds thoughtful software tools for families and teams, including the Familia family planner and the Asynq Decision Registry, aiming to simplify everyday coordination and preserve decision context. Their mission is to reduce mental load by providing shared digital spaces for planning, decision tracking, and collaborative life management.
image: https://asynq.org/asynq-labs.svg
layout: provider
modified: '2026-11-01'
name: Asynq Labs
nav: Providers
network: true
overview: 'Asynq Labs is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Family, Productivity, Decision Management, Collaboration, and Software.


  Asynq Labs'' developer surface includes engineering blog, support, pricing, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 12.4
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asynq Org Domain Security
  slug: asynq-org-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: asynq-org
tags:
- Family
- Productivity
- Decision Management
- Collaboration
- Software
website: https://asynq.org/
---
