---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/contextaco-com/plans/contextaco-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contextaco-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/contextaco-com/llms/contextaco-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextaco-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/contextaco-com/well-known/contextaco-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextaco-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextaco-com/hosts/contextaco-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextaco-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextaco-com/vendors/contextaco-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextaco-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contextaco.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contextaco.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://contextaco.com/pricing
- group: start
  title: ''
  type: Login
  url: https://contextaco.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contextaco.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contextaco
- group: auth
  href: https://artifacts.apis.io/contextaco-com/security/contextaco-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextaco-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contextaco.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation at https://docs.contextaco.com/ provides no machine‑readable API contract.
  evidence:
  - status: 200
    url: https://docs.contextaco.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Contextaco provides a platform that captures and carries contextual information across sessions, people, and agents. It enables users to record insights, decisions, and data points in one place and seamlessly transfer them to subsequent interactions, fostering continuity and collaborative knowledge sharing. The service emphasizes simplicity, flexibility, and integration, allowing contexts to be reused, forked, and built upon as projects evolve.
image: https://contextaco.com/opengraph-image?87af5902116b9884
layout: provider
modified: '2026-11-04'
name: Contextaco
nav: Providers
network: true
overview: 'Contextaco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contextual, Platform, Collaboration, and Knowledge.


  Contextaco''s developer surface includes pricing, documentation, and 11 more developer resources.'
plans:
- name: Contextaco Com Plans Pricing
  plan_count: 2
  slug: contextaco-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextaco Com Domain Security
  slug: contextaco-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: contextaco-com
tags:
- Company
- Contextual
- Platform
- Collaboration
- Knowledge
website: https://contextaco.com/
---
