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
api_count: 1
apis:
- description: Analytics API referenced in the developer docs
  name: Clamp API
  slug: clamp-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/clamp-sh/plans/clamp-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clamp-sh-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/clamp-sh/llms/clamp-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clamp-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/clamp-sh/well-known/clamp-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clamp-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/clamp-sh/hosts/clamp-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clamp-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/clamp-sh/vendors/clamp-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clamp-sh-vendors.yml
- group: build
  href: https://artifacts.apis.io/clamp-sh/packages/clamp-sh-packages.yml
  title: ''
  type: SDKs
  url: packages/clamp-sh-packages.yml
- group: build
  href: https://artifacts.apis.io/clamp-sh/packages/clamp-sh-packages.yml
  title: ''
  type: Packages
  url: packages/clamp-sh-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clamp.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clamp.sh/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clamp.sh/pricing
- group: start
  title: ''
  type: Login
  url: https://clamp.sh/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clamp-sh
- group: docs
  title: ''
  type: Documentation
  url: https://clamp.sh/docs/guides
- group: operate
  title: ''
  type: ChangeLog
  url: https://clamp.sh/changelog
- group: company
  title: ''
  type: Blog
  url: https://clamp.sh/blog
- group: docs
  title: ''
  type: APIReference
  url: https://clamp.sh/docs/sdk/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://clamp.sh/docs
- group: auth
  href: https://artifacts.apis.io/clamp-sh/security/clamp-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clamp-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clamp.sh/
coverage:
  checked: '2026-11-03'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or gRPC specs were found.
  evidence:
  - status: 404
    url: https://api.clamp.sh/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Analytics built for humans and agents. Clamp provides a readable dashboard with AI‑assisted insights, offering free, Pro, Growth, and Business plans. It integrates metrics, segment analysis, and automated handoff to Claude, Cursor, or ChatGPT, enabling agents to investigate why a metric changed rather than just reporting it.
image: https://clamp.sh/opengraph-image.png?opengraph-image.00380qrwqwa~e.png
layout: provider
modified: '2026-11-03'
name: Clamp
nav: Providers
network: true
overview: 'Clamp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Dashboards, Artificial Intelligence, and Metrics.


  Clamp''s developer surface includes pricing, documentation, changelog, engineering blog, API reference, getting-started guide, and 13 more developer resources.'
plans:
- name: Clamp Sh Plans Pricing
  plan_count: 4
  slug: clamp-sh-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clamp Sh Domain Security
  slug: clamp-sh-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clamp-sh
tags:
- Company
- Analytics
- Dashboards
- Artificial Intelligence
- Metrics
- Monitoring
website: https://clamp.sh/
---
