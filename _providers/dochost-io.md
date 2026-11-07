---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'dochost API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: dochost API
  slug: dochost-io-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/dochost-io/plans/dochost-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dochost-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dochost-io/rules/dochost-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dochost-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dochost-io/vocabulary/dochost-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dochost-io-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/dochost-io/changelog/dochost-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dochost-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/dochost-io/conformance/dochost-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dochost-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dochost-io/llms/dochost-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dochost-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dochost-io/well-known/dochost-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dochost-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dochost-io/hosts/dochost-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dochost-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dochost-io/vendors/dochost-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dochost-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dochost.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dochost.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dochost.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://dochost.io/changelog
- group: company
  title: ''
  type: Blog
  url: https://dochost.io/blog
- group: auth
  href: https://artifacts.apis.io/dochost-io/security/dochost-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dochost-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dochost.io/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found on the provider's hosts.
  evidence:
  - status: 404
    url: https://dochost.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dochost provides a free, instant HTML and Markdown hosting service that converts HTML or Markdown content into shareable URLs. Users can paste HTML or Markdown, preview the rendered result, and obtain a short link without signing up. The platform supports multiple languages, offers live preview, and is designed for quick publishing of web snippets, documentation, or blog excerpts.
image: https://dochost.io/og.png
layout: provider
modified: '2026-11-05'
name: dochost
nav: Providers
network: true
overview: 'dochost is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hosting, HTML, Markdown, Free, and URLs.


  The dochost catalog on APIs.io includes 1 Spectral governance ruleset.


  dochost''s developer surface includes changelog, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Dochost Io Plans Pricing
  plan_count: 3
  slug: dochost-io-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: dochost API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: dochost-io-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dochost Io Domain Security
  slug: dochost-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dochost-io
tags:
- Hosting
- HTML
- Markdown
- Free
- URLs
website: https://dochost.io/
---
