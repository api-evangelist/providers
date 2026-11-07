---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/befana-app/rules/befana-app-rules.yml
  title: ''
  type: Spectral
  url: rules/befana-app-rules.yml
- group: design
  href: https://artifacts.apis.io/befana-app/json-ld/befana-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/befana-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/befana-app/vocabulary/befana-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/befana-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/befana-app/data-model/befana-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/befana-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/befana-app/errors/befana-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/befana-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/befana-app/conformance/befana-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/befana-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/befana-app/llms/befana-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/befana-app-llms.txt
- group: other
  href: https://artifacts.apis.io/befana-app/hosts/befana-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/befana-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/befana-app/vendors/befana-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/befana-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/befana-app/security/befana-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/befana-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://befana.app/
coverage:
  checked: '2026-11-02'
  detail: The provider's website serves a JavaScript‑rendered shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://befana.app/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Befana Gifting is a web‑based gifting platform that enables users to create, manage, and send personalized gifts. The application provides a gift workspace where users can organize orders, view pending gifts, and send gift references. Built on Vercel, the service offers a clean, browser‑based interface for gifting workflows and integrates with modern web technologies. While the site is primarily a single‑page app, it presents core gifting features without requiring account creation for browsing.
image: https://befana.app/icon-512.png
jsonld:
- class_count: 18
  name: Befana App Context
  property_count: 107
  slug: befana-app-context
layout: provider
modified: '2026-11-02'
name: Befana
nav: Providers
network: true
overview: 'Befana publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Gifting, Web App, Platform, E-Commerce, and Vercel.


  The Befana catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Befana App Plans Pricing
  plan_count: 0
  slug: befana-app-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Befana App Rate Limits
  slug: befana-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Befana API Rules
  rule_count: 65
  severity_counts:
    error: 51
    hint: 0
    info: 3
    warn: 11
  slug: befana-app-rules
scopes:
- name: Befana App Scopes
  scope_count: 0
  slug: befana-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 27
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Befana App Authentication
  slug: befana-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Befana App Domain Security
  slug: befana-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: befana-app
tags:
- Gifting
- Web App
- Platform
- E-Commerce
- Vercel
website: https://befana.app/
---
