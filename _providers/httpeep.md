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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: HTTPeep provides a modern web debugging proxy API documented at https://docs.httpeep.com/introduction
  name: HTTPeep API
  slug: httpeep-api-2
- description: 'HTTPeep API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: HTTPeep API
  slug: httpeep-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/httpeep/plans/httpeep-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/httpeep-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/httpeep/rules/httpeep-rules.yml
  title: ''
  type: Spectral
  url: rules/httpeep-rules.yml
- group: design
  href: https://artifacts.apis.io/httpeep/vocabulary/httpeep-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/httpeep-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/httpeep/cli/httpeep-cli.yml
  title: ''
  type: CLI
  url: cli/httpeep-cli.yml
- group: design
  href: https://artifacts.apis.io/httpeep/conformance/httpeep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/httpeep-conformance.yml
- group: agent
  href: https://artifacts.apis.io/httpeep/llms/httpeep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/httpeep-llms.txt
- group: other
  href: https://artifacts.apis.io/httpeep/hosts/httpeep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/httpeep-hosts.yml
- group: other
  href: https://artifacts.apis.io/httpeep/vendors/httpeep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/httpeep-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://httpeep.com/pricing
- group: auth
  href: https://artifacts.apis.io/httpeep/security/httpeep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/httpeep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://httpeep.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.httpeep.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.httpeep.com/get-started/installation
- group: operate
  title: ''
  type: Support
  url: https://docs.httpeep.com/troubleshooting
coverage:
  checked: '2026-10-18'
  detail: Docs pages return HTML shells and redirect when requesting OpenAPI files, providing no machine‑readable spec.
  evidence:
  - status: 307
    url: https://docs.httpeep.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-17'
description: HTTPeep provides a modern web debugging proxy and HTTP debugger built with Rust. It captures and inspects HTTPS traffic in real-time, supports rule‑based forwarding, mock local files, DNS overrides, and offers a CLI for Linux alongside GUI apps for macOS and Windows. The platform targets developers needing deep insight into HTTP requests and responses, with features like traffic capture, request modification, and replay, all through a composable rule engine.
image: https://httpeep.com/og-image.png
layout: provider
modified: '2026-10-17'
name: HTTPeep
nav: Providers
network: true
overview: 'HTTPeep is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Debugging, Proxy, HTTP, and Rust.


  The HTTPeep catalog on APIs.io includes 1 Spectral governance ruleset.


  HTTPeep''s developer surface includes CLI, pricing, documentation, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Httpeep Plans Pricing
  plan_count: 3
  slug: httpeep-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: HTTPeep API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: httpeep-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 20.2
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 25.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/httpeep/httpeep-2026-11-03T133511.png
security:
- kind: domain-security
  name: Httpeep Domain Security
  slug: httpeep-domain-security
  summary_line: TLSv1.3 · HSTS
slug: httpeep
tags:
- Company
- Debugging
- Proxy
- HTTP
- Rust
website: https://httpeep.com/
---
