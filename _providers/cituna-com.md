---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AI visibility API for ChatGPT, Claude, Gemini and other models
  name: Cituna AI Visibility API
  slug: cituna-ai-visibility-api
- description: 'Cituna API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cituna API
  slug: cituna-com-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/cituna-com/plans/cituna-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cituna-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cituna-com/rules/cituna-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cituna-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cituna-com/json-ld/cituna-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cituna-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cituna-com/vocabulary/cituna-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cituna-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cituna-com/data-model/cituna-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cituna-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cituna-com/security/cituna-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cituna-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/cituna-com/conformance/cituna-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cituna-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cituna-com/llms/cituna-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cituna-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cituna-com/well-known/cituna-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cituna-com-security.txt
- group: agent
  href: https://artifacts.apis.io/cituna-com/well-known/cituna-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cituna-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cituna-com/hosts/cituna-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cituna-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cituna.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cituna.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cituna.com/pricing
- group: start
  title: ''
  type: Login
  url: https://cituna.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cituna
- group: docs
  title: ''
  type: Documentation
  url: https://cituna.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cituna.com/developers
- group: auth
  href: https://artifacts.apis.io/cituna-com/security/cituna-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cituna-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cituna-com/security/cituna-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cituna-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cituna.com/
coverage:
  checked: '2026-11-04'
  detail: Developer portal pages are rendered HTML with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://cituna.com/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Cituna is an AI visibility platform that helps brands get recommended by AI engines. It monitors AI answers, generates fixes, auto‑writes SEO articles, and publishes them across major CMSs. The platform also offers an MCP server to connect Claude and other AI agents for data integration.
image: https://cituna.com/opengraph-image?bac54b084c28ac66
json_schemas:
- name: GetApiVisibilityResponse
  property_count: 2
  slug: cituna-com-get-api-visibility-response
jsonld:
- class_count: 1
  name: Cituna Com Context
  property_count: 2
  slug: cituna-com-context
layout: provider
modified: '2026-11-03'
name: Cituna
nav: Providers
network: true
overview: 'Cituna is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, SEO, Platform, Visibility, and Marketing.


  The Cituna catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cituna''s developer surface includes pricing, documentation, and 19 more developer resources.'
plans:
- name: Cituna Com Plans Pricing
  plan_count: 4
  slug: cituna-com-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Cituna API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: cituna-com-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 17.7
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 13.2
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
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cituna Com Domain Security
  slug: cituna-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cituna Com Vulnerability Disclosure
  slug: cituna-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cituna-com
tags:
- Artificial Intelligence
- SEO
- Platform
- Visibility
- Marketing
website: https://cituna.com/
---
