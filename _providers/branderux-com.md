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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'BranderUX API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: BranderUX API
  slug: branderux-com-api
artifact_total: 8
asyncapis:
- description: ''
  name: Branderux Com Webhooks
  slug: branderux-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/branderux-com/plans/branderux-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/branderux-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/branderux-com/rules/branderux-com-rules.yml
  title: ''
  type: Spectral
  url: rules/branderux-com-rules.yml
- group: design
  href: https://artifacts.apis.io/branderux-com/json-ld/branderux-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/branderux-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/branderux-com/vocabulary/branderux-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/branderux-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/branderux-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/branderux-com/asyncapi/branderux-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/branderux-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/branderux-com/data-model/branderux-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/branderux-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/branderux-com/conformance/branderux-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/branderux-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/branderux-com/llms/branderux-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/branderux-com-llms.txt
- group: other
  href: https://artifacts.apis.io/branderux-com/hosts/branderux-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branderux-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/branderux-com/vendors/branderux-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branderux-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/branderux-com/packages/branderux-com-packages.yml
  title: ''
  type: Packages
  url: packages/branderux-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@brander/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BranderUX
- group: auth
  href: https://artifacts.apis.io/branderux-com/security/branderux-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branderux-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branderux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://branderux.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://branderux.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://branderux.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branderux.com/legal/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://branderux.com/docs/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://branderux.com/mcp
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are rendered HTML with no machine‑readable OpenAPI or AsyncAPI spec discovered.
  evidence:
  - status: 200
    url: https://branderux.com/docs/quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BranderUX provides a platform to build agentic applications quickly, offering a no‑code interface where users input a single message and receive a fully functional AI‑driven app, complete with website, MCP integration, and runtime UI generation. The service targets businesses seeking rapid AI app deployment without deep technical expertise, emphasizing speed, customization, and live generation per customer.
image: https://branderux.com/og-image.jpg
json_schemas:
- name: PostApiAiRequest
  property_count: 1
  slug: branderux-com-post-api-ai-request
- name: PostApiAiResponse
  property_count: 1
  slug: branderux-com-post-api-ai-response
jsonld:
- class_count: 2
  name: Branderux Com Context
  property_count: 2
  slug: branderux-com-context
layout: provider
modified: '2026-11-02'
name: BranderUX
nav: Providers
network: true
overview: 'BranderUX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI App Builder, Agentic applications, MCP app, and Dashboards.


  The BranderUX catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BranderUX''s developer surface includes documentation, pricing, getting-started guide, and 19 more developer resources.'
plans:
- name: Branderux Com Plans Pricing
  plan_count: 5
  slug: branderux-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: BranderUX API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: branderux-com-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 26.7
    developer_ergonomics: 29.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branderux Com Domain Security
  slug: branderux-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: branderux-com
tags:
- AI App Builder
- Agentic applications
- MCP app
- Dashboards
website: https://branderux.com/
---
