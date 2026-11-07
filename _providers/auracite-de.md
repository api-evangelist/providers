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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/auracite-de/plans/auracite-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auracite-de-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://auracite.de/security
- group: agent
  href: https://artifacts.apis.io/auracite-de/llms/auracite-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auracite-de-llms.txt
- group: auth
  href: https://artifacts.apis.io/auracite-de/well-known/auracite-de-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/auracite-de-security.txt
- group: agent
  href: https://artifacts.apis.io/auracite-de/well-known/auracite-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auracite-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/auracite-de/hosts/auracite-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auracite-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/auracite-de/vendors/auracite-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auracite-de-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://auracite.de/content/guides/what-is-geo-guide.html
- group: auth
  href: https://artifacts.apis.io/auracite-de/security/auracite-de-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/auracite-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/auracite-de/security/auracite-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auracite-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auracite.de/
coverage:
  checked: '2026-11-02'
  detail: GraphQL endpoint https://auracite.de/api/graphql returns 401, indicating authentication is required.
  evidence:
  - status: 401
    url: https://auracite.de/api/graphql
  reason: auth-required
  state: gated
created: '2026-11-02'
description: AuraCite provides an analytics platform for Generative Engine Optimization (GEO) and AI Visibility Analytics. It tracks how large language models and AI search engines mention, describe, and cite brands, products, and companies. The service offers recurring measurements, source analysis, competitive benchmarking, and developer‑friendly workflows, including MCP‑ready integrations for programmatic data access. Pricing plans include a free brand check and paid packages for deeper insights.
image: https://auracite.de/social/og-ai-recommendation-check.png
layout: provider
modified: '2026-11-02'
name: AuraCite
nav: Providers
network: true
overview: 'AuraCite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Geo, Visibility, and Platform.


  AuraCite''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Auracite De Plans Pricing
  plan_count: 3
  slug: auracite-de-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 14.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Auracite De Domain Security
  slug: auracite-de-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Auracite De Vulnerability Disclosure
  slug: auracite-de-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: auracite-de
tags:
- Artificial Intelligence
- Analytics
- Geo
- Visibility
- Platform
- German
website: https://auracite.de/
---
