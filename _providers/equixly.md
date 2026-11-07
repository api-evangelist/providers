---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API Discovery and Attack Surface Management platform offering continuous penetration testing and remediation.
  name: Equixly API
  slug: equixly-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/equixly/plans/equixly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/equixly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/equixly/conformance/equixly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/equixly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/equixly/llms/equixly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/equixly-llms.txt
- group: auth
  href: https://artifacts.apis.io/equixly/well-known/equixly-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/equixly-app-security.txt
- group: agent
  href: https://artifacts.apis.io/equixly/well-known/equixly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/equixly-well-known.yml
- group: other
  href: https://artifacts.apis.io/equixly/hosts/equixly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/equixly-hosts.yml
- group: other
  href: https://artifacts.apis.io/equixly/vendors/equixly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/equixly-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://equixly.com/blog/category/security/
- group: company
  title: ''
  type: Newsroom
  url: https://equixly.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/equixly
- group: auth
  href: https://artifacts.apis.io/equixly/security/equixly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/equixly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equixly.com/
- group: company
  title: ''
  type: Blog
  url: https://equixly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://equixly.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://equixly.com/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://equixly.com/platform
- group: docs
  title: ''
  type: APIReference
  url: https://equixly.com/platform/api-attack-surface-management
- group: start
  title: ''
  type: DeveloperPortal
  url: https://equixly.com/platform
- group: start
  title: ''
  type: GettingStarted
  url: https://equixly.com/start-pentest/
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://equixly.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Equixly provides an agentic AI-driven offensive security platform that continuously penetrates, tests, and remediates API and application vulnerabilities. Leveraging autonomous AI agents, the service offers real‑time attack surface management, continuous penetration testing, and automated remediation across financial services, retail, healthcare, energy, and technology sectors. The platform integrates generative AI to adapt tactics, scale testing, and deliver actionable risk insights, aiming to replace manual pen‑testing with continuous, AI‑powered security operations.
image: https://equixly.com/assets/share.png
layout: provider
modified: '2026-10-20'
name: Equixly
nav: Providers
network: true
overview: 'Equixly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Artificial Intelligence, and Penetration Testing.


  Equixly''s developer surface includes engineering blog, pricing, support, documentation, API reference, getting-started guide, and 13 more developer resources.'
plans:
- name: Equixly Plans Pricing
  plan_count: 2
  slug: equixly-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.5
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 56.3
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/equixly/equixly-2026-11-03T131619.png
security:
- kind: domain-security
  name: Equixly Domain Security
  slug: equixly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: equixly
tags:
- Company
- Security
- Artificial Intelligence
- Penetration Testing
website: https://equixly.com/
---
