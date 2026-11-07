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
api_count: 1
apis:
- description: Public read‑only JSON API for browsing prompts, workflows, skills, and other resources.
  name: Amo.ng Public API
  slug: amo-ng-public-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/amo-ng/llms/amo-ng-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amo-ng-llms.txt
- group: other
  href: https://artifacts.apis.io/amo-ng/hosts/amo-ng-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amo-ng-hosts.yml
- group: other
  href: https://artifacts.apis.io/amo-ng/vendors/amo-ng-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amo-ng-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://amo.ng/prompts/pricing-packaging-evidence-review
- group: auth
  href: https://artifacts.apis.io/amo-ng/security/amo-ng-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amo-ng-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amo.ng/
- group: docs
  title: ''
  type: Documentation
  url: https://amo.ng/api
- group: docs
  title: ''
  type: APIReference
  url: https://amo.ng/api
- group: start
  title: ''
  type: GettingStarted
  url: https://amo.ng/about
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amo.ng/terms
coverage:
  checked: '2026-11-01'
  detail: The public API reference page lists endpoints but no OpenAPI or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://amo.ng/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Amo.ng provides a free library of AI prompts, workflows, and skills designed for practical real‑world tasks. Users can browse structured prompts, follow step‑by‑step workflows, and reuse skills without needing an account. The platform integrates with Workplace for private execution and offers Amo.ng Build to create websites and tools. It targets developers, founders, marketers, educators, and operators, delivering AI‑assisted resources across many domains.
image: https://amo.ng/favicon.ico
layout: provider
modified: '2026-11-01'
name: Amo.ng
nav: Providers
network: true
overview: 'Amo.ng is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Prompts, Workflows, Skills, and Productivity.


  Amo.ng''s developer surface includes pricing, documentation, API reference, getting-started guide, and 6 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amo Ng Domain Security
  slug: amo-ng-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amo-ng
tags:
- Artificial Intelligence
- Prompts
- Workflows
- Skills
- Productivity
website: https://amo.ng/
---
