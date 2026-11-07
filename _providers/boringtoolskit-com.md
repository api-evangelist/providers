---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 24.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Boringtoolskit Com Agentic Access
  operation_count: 2
  slug: boringtoolskit-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://boringtoolskit.com
  baseurl_source: declared
  description: Resolve a visitor's privacy region for consent handling.
  name: BoringToolsKit Privacy region API
  slug: boringtoolskit-com-privacy-region-api
- baseURL: https://boringtoolskit.com
  baseurl_source: declared
  description: Optional, labeled, privacy-bounded usage events.
  name: BoringToolsKit Usage events API
  slug: boringtoolskit-com-usage-events-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/boringtoolskit-com/agentic-access/boringtoolskit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boringtoolskit-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/rules/boringtoolskit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boringtoolskit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/json-ld/boringtoolskit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boringtoolskit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/vocabulary/boringtoolskit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boringtoolskit-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/data-model/boringtoolskit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boringtoolskit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/errors/boringtoolskit-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boringtoolskit-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boringtoolskit-com/conformance/boringtoolskit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boringtoolskit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boringtoolskit-com/llms/boringtoolskit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boringtoolskit-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/boringtoolskit-com/well-known/boringtoolskit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boringtoolskit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boringtoolskit-com/hosts/boringtoolskit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boringtoolskit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boringtoolskit-com/vendors/boringtoolskit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boringtoolskit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boringtoolskit.com/terms/
- group: operate
  title: ''
  type: Roadmap
  url: https://boringtoolskit.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boringtoolskit.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://boringtoolskit.com/blog/crawler-week/
- group: auth
  href: https://artifacts.apis.io/boringtoolskit-com/security/boringtoolskit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boringtoolskit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boringtoolskit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://boringtoolskit.com/developers/
- group: agent
  title: ''
  type: MCPServer
  url: https://boringtoolskit.com/.well-known/mcp/server-card.json
created: '2026-11-02'
description: BoringToolsKit offers a free collection of private, no‑signup browser calculators and everyday tools covering finance, health, education, construction, and more. All calculations run locally in the user’s browser, ensuring privacy and instant results without accounts or uploads. The site provides detailed formulas, assumptions, and sources for each tool, plus editorial standards and methodology documentation.
image: https://boringtoolskit.com/assets/brand/social-preview.png?v=20261018-slope-v2
jsonld:
- class_count: 1
  name: Boringtoolskit Com Context
  property_count: 3
  slug: boringtoolskit-com-context
layout: provider
mcp_servers:
- description: ''
  name: BoringToolsKit MCP Server
  slug: server-card-json
modified: '2026-11-02'
name: BoringToolsKit
nav: Providers
network: true
overview: 'BoringToolsKit publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Privacy region API and Usage events API. Tagged areas include Tools, Finance, Health, Education, and Construction.


  The BoringToolsKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BoringToolsKit''s developer surface includes engineering blog, documentation, and 17 more developer resources.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: BoringToolsKit API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: boringtoolskit-com-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 6.0
    discoverability: 65.0
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 11.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boringtoolskit Com Domain Security
  slug: boringtoolskit-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: boringtoolskit-com
tags:
- Tools
- Finance
- Health
- Education
- Construction
- Free
website: https://boringtoolskit.com/
---
