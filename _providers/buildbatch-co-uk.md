---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buildbatch Co Uk Agentic Access
  operation_count: 2
  slug: buildbatch-co-uk-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://buildbatch.co.uk
  baseurl_source: declared
  description: The Ask.json API from BuildBatch — 1 operation(s) for ask.json.
  name: BuildBatch Ask.json API
  slug: buildbatch-co-uk-ask-json-api
- baseURL: https://buildbatch.co.uk
  baseurl_source: declared
  description: The Plan.json API from BuildBatch — 1 operation(s) for plan.json.
  name: BuildBatch Plan.json API
  slug: buildbatch-co-uk-plan-json-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/buildbatch-co-uk/agentic-access/buildbatch-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildbatch-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/rules/buildbatch-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/buildbatch-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/json-ld/buildbatch-co-uk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildbatch-co-uk-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/vocabulary/buildbatch-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildbatch-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/data-model/buildbatch-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildbatch-co-uk-data-model.yml
- group: auth
  href: https://artifacts.apis.io/buildbatch-co-uk/security/buildbatch-co-uk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/buildbatch-co-uk-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/errors/buildbatch-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/buildbatch-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/buildbatch-co-uk/conformance/buildbatch-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildbatch-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildbatch-co-uk/llms/buildbatch-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildbatch-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildbatch-co-uk/mcp/buildbatch-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buildbatch-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/buildbatch-co-uk/well-known/buildbatch-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/buildbatch-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/buildbatch-co-uk/well-known/buildbatch-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildbatch-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildbatch-co-uk/hosts/buildbatch-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildbatch-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildbatch-co-uk/vendors/buildbatch-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildbatch-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildbatch.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildbatch.co.uk/privacy/
- group: start
  title: ''
  type: Login
  url: https://buildbatch.co.uk/account/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://buildbatch.co.uk/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://buildbatch.co.uk/llms.txt
- group: auth
  href: https://artifacts.apis.io/buildbatch-co-uk/security/buildbatch-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/buildbatch-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/buildbatch-co-uk/security/buildbatch-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildbatch-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildbatch.co.uk/
created: '2026-11-03'
description: BuildBatch provides a free UK materials calculator for paint, wallpaper, tiles, flooring, carpet, concrete, patios and more. No account is required; users input room dimensions and receive a detailed shopping list with quantities, prices, tools, and step‑by‑step guidance. The service also offers AI‑assistant integration via an OpenAPI interface, enabling programmatic access to calculations and data. It aims to simplify DIY home improvement planning for homeowners and professionals across the United Kingdom.
image: https://buildbatch.co.uk/app/brand/buildbatch-card.png
json_schemas:
- name: PlanAnswer
  property_count: 16
  slug: buildbatch-co-uk-plan-answer
- name: QuestionScript
  property_count: 8
  slug: buildbatch-co-uk-question-script
jsonld:
- class_count: 5
  name: Buildbatch Co Uk Context
  property_count: 52
  slug: buildbatch-co-uk-context
layout: provider
mcp_servers:
- description: Remote MCP server at buildbatch.co.uk.
  name: BuildBatch MCP Server
  slug: buildbatch-co-uk-mcp-yml
modified: '2026-11-03'
name: BuildBatch
nav: Providers
network: true
overview: 'BuildBatch publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Ask.json API and Plan.json API. Tagged areas include Home Improvement, DIY, MaterialsCalculator, United Kingdom, and Construction.


  The BuildBatch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BuildBatch''s developer surface includes documentation, API reference, and 20 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BuildBatch API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: buildbatch-co-uk-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 59.5
    developer_ergonomics: 8.3
    discoverability: 65.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildbatch Co Uk Domain Security
  slug: buildbatch-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Buildbatch Co Uk Vulnerability Disclosure
  slug: buildbatch-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buildbatch-co-uk
tags:
- Home Improvement
- DIY
- MaterialsCalculator
- United Kingdom
- Construction
website: https://buildbatch.co.uk/
---
