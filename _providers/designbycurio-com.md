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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Curio API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Curio API
  slug: designbycurio-com-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/designbycurio-com/plans/designbycurio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/designbycurio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/designbycurio-com/rules/designbycurio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/designbycurio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/designbycurio-com/vocabulary/designbycurio-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/designbycurio-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/designbycurio-com/conformance/designbycurio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/designbycurio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/designbycurio-com/llms/designbycurio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/designbycurio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/designbycurio-com/hosts/designbycurio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/designbycurio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/designbycurio-com/vendors/designbycurio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/designbycurio-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/designbycurio
- group: auth
  href: https://artifacts.apis.io/designbycurio-com/security/designbycurio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/designbycurio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://designbycurio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://designbycurio.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://designbycurio.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://designbycurio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://designbycurio.com/privacy
- group: operate
  title: ''
  type: Contact
  url: https://designbycurio.com/contact
coverage:
  checked: '2026-11-05'
  detail: The developer docs at https://designbycurio.com/docs return HTML but contain no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract files.
  evidence:
  - status: 200
    url: https://designbycurio.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Curio provides a design style library for AI agents, offering thousands of curated visual styles that can be applied to AI-generated content. Users can browse, select, and integrate designs via simple markdown files, enabling rapid customization of reports, decks, and websites. The platform updates weekly with new styles and supports multiple languages and themes.
image: https://designbycurio.com/assets/og/curio-share-en.jpg
layout: provider
modified: '2026-11-05'
name: Curio
nav: Providers
network: true
overview: 'Curio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Design, Artificial Intelligence, Style Library, Visual Assets, and Creative Tools.


  The Curio catalog on APIs.io includes 1 Spectral governance ruleset.


  Curio''s developer surface includes documentation, pricing, and 13 more developer resources.'
plans:
- name: Designbycurio Com Plans Pricing
  plan_count: 3
  slug: designbycurio-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 67
  extends:
  - spectral:oas
  name: Curio API Rules
  rule_count: 26
  severity_counts:
    error: 24
    hint: 0
    info: 1
    warn: 1
  slug: designbycurio-com-rules
score:
  band: emerging
  composite: 25.8
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
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Designbycurio Com Domain Security
  slug: designbycurio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: designbycurio-com
tags:
- Design
- Artificial Intelligence
- Style Library
- Visual Assets
- Creative Tools
website: https://designbycurio.com/
---
