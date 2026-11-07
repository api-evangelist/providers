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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/meet-cedric/plans/meet-cedric-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meet-cedric-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/meet-cedric/changelog/meet-cedric-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meet-cedric-changelog.yml
- group: design
  href: https://artifacts.apis.io/meet-cedric/conformance/meet-cedric-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meet-cedric-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meet-cedric/llms/meet-cedric-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meet-cedric-llms.txt
- group: agent
  href: https://artifacts.apis.io/meet-cedric/well-known/meet-cedric-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meet-cedric-well-known.yml
- group: other
  href: https://artifacts.apis.io/meet-cedric/hosts/meet-cedric-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meet-cedric-hosts.yml
- group: other
  href: https://artifacts.apis.io/meet-cedric/vendors/meet-cedric-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meet-cedric-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meet-cedric.com/terms
- group: auth
  title: ''
  type: Security
  url: https://meet-cedric.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meet-cedric.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://meet-cedric.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://meet-cedric.com/how-to-use-cedric
- group: auth
  href: https://artifacts.apis.io/meet-cedric/security/meet-cedric-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meet-cedric-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meet-cedric.com
- group: docs
  title: ''
  type: Documentation
  url: https://meet-cedric.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://meet-cedric.com/pricing
- group: company
  title: ''
  type: About
  url: https://meet-cedric.com/about
- group: company
  title: ''
  type: Blog
  url: https://meet-cedric.com/blog
coverage:
  checked: '2026-10-27'
  detail: Documentation at https://meet-cedric.com/docs provides HTML pages but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://meet-cedric.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Cedric provides an AI employee that integrates with Slack, Telegram, Discord and web tools to automate tasks, remember context, and assist teams across sales, marketing, and development. It offers a free tier and paid plans, with real‑time collaboration and secure data handling.
image: https://meet-cedric.com/opengraph-image.png?d569e74aadcdb7b1
layout: provider
modified: '2026-10-27'
name: Cedric
nav: Providers
network: true
overview: 'Cedric is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Collaboration, and Productivity.


  Cedric''s developer surface includes changelog, getting-started guide, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Meet Cedric Plans Pricing
  plan_count: 6
  slug: meet-cedric-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.7
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/meet-cedric/meet-cedric-2026-11-03T135439.png
security:
- kind: domain-security
  name: Meet Cedric Domain Security
  slug: meet-cedric-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meet-cedric
tags:
- Company
- Artificial Intelligence
- Automation
- Collaboration
- Productivity
website: https://meet-cedric.com
---
