---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 3
  name: Shotkiln Com Agentic Access
  operation_count: 16
  slug: shotkiln-com-agentic-access
  summary_line: 16 operations · 11 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Billing API from shotkiln-com — 1 operation(s) for billing.
  name: shotkiln-com Billing API
  slug: shotkiln-com-billing-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Checkout API from shotkiln-com — 1 operation(s) for checkout.
  name: shotkiln-com Checkout API
  slug: shotkiln-com-checkout-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Keys API from shotkiln-com — 5 operation(s) for keys.
  name: shotkiln-com Keys API
  slug: shotkiln-com-keys-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Mcp API from shotkiln-com — 1 operation(s) for mcp.
  name: shotkiln-com MCP API
  slug: shotkiln-com-mcp-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Og API from shotkiln-com — 2 operation(s) for og.
  name: shotkiln-com Og API
  slug: shotkiln-com-og-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Pdf API from shotkiln-com — 1 operation(s) for pdf.
  name: shotkiln-com PDF API
  slug: shotkiln-com-pdf-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Screenshot API from shotkiln-com — 1 operation(s) for screenshot.
  name: shotkiln-com Screenshot API
  slug: shotkiln-com-screenshot-api
- baseURL: https://shotkiln.com
  baseurl_source: declared
  description: The Usage API from shotkiln-com — 1 operation(s) for usage.
  name: shotkiln-com Usage API
  slug: shotkiln-com-usage-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/shotkiln-com/agentic-access/shotkiln-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shotkiln-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/shotkiln-com/plans/shotkiln-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shotkiln-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/shotkiln-com/rules/shotkiln-com-rules.yml
  title: ''
  type: Spectral
  url: rules/shotkiln-com-rules.yml
- group: design
  href: https://artifacts.apis.io/shotkiln-com/json-ld/shotkiln-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shotkiln-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/shotkiln-com/vocabulary/shotkiln-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shotkiln-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/shotkiln-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/shotkiln-com/data-model/shotkiln-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shotkiln-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/shotkiln-com/authentication/shotkiln-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shotkiln-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/shotkiln-com/errors/shotkiln-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shotkiln-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shotkiln-com/conformance/shotkiln-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shotkiln-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/shotkiln-com/llms/shotkiln-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shotkiln-com-llms.txt
- group: other
  href: https://artifacts.apis.io/shotkiln-com/hosts/shotkiln-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shotkiln-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/shotkiln-com/vendors/shotkiln-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shotkiln-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://shotkiln.com/guides/screenshot-tool-for-claude-code
- group: auth
  href: https://artifacts.apis.io/shotkiln-com/security/shotkiln-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shotkiln-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shotkiln.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shotkiln.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://shotkiln.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://shotkiln.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shotkiln.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shotkiln.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://shotkiln.com/contact
created: '2026-10-31'
description: Shotkiln provides a Screenshot API that renders any web page into PNG, PDF, or Open Graph images. It offers a simple HTTP endpoint where you send a URL and receive a rendered image, PDF, or OG image in seconds, using real browser rendering. The service includes pricing tiers, a free key, and documentation for developers, and is positioned as a tool for automating visual capture of web content.
image: https://shotkiln.com/examples/og-card.png
jsonld:
- class_count: 1
  name: Shotkiln Com Context
  property_count: 1
  slug: shotkiln-com-context
layout: provider
modified: '2026-10-31'
name: shotkiln-com
nav: Providers
network: true
overview: 'shotkiln-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Checkout API, Keys API, and 5 more. Tagged areas include Company, Screenshots, Web, and Automation.


  The shotkiln-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  shotkiln-com''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, support, and 16 more developer resources.'
plans:
- name: Shotkiln Com Plans Pricing
  plan_count: 4
  slug: shotkiln-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: shotkiln-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: shotkiln-com-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 50.5
    developer_ergonomics: 30.4
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shotkiln-com/shotkiln-com-2026-11-03T143143.png
security:
- kind: authentication
  name: Shotkiln Com Authentication
  slug: shotkiln-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Shotkiln Com Domain Security
  slug: shotkiln-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: shotkiln-com-create-signed-og-image
  slug: shotkiln-com-create-signed-og-image
slug: shotkiln-com
tags:
- Company
- Screenshots
- Web
- Automation
website: https://shotkiln.com/
---
