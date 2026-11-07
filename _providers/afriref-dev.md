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
    agent_card: flavored
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Pan-African government reference data for 34 countries as cited JSON, covering policy rates, VAT, wages, holidays, etc.
  name: afriref
  slug: afriref
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/afriref-dev/plans/afriref-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afriref-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/afriref-dev/rules/afriref-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/afriref-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/afriref-dev/json-ld/afriref-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/afriref-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/afriref-dev/vocabulary/afriref-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/afriref-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/afriref-dev/data-model/afriref-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/afriref-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/afriref-dev/errors/afriref-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/afriref-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/afriref-dev/conformance/afriref-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afriref-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/afriref-dev/llms/afriref-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afriref-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/afriref-dev/a2a/afriref-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afriref-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/afriref-dev/mcp/afriref-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/afriref-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/afriref-dev/mcp/afriref-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/afriref-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/afriref-dev/well-known/afriref-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/afriref-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/afriref-dev/well-known/afriref-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afriref-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/afriref-dev/hosts/afriref-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afriref-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/afriref-dev/vendors/afriref-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/afriref-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/afriref-dev/security/afriref-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/afriref-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/afriref-dev/security/afriref-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afriref-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afriref.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://afriref.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://afriref.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://afriref.dev/privacy
- group: auth
  title: ''
  type: Security
  url: https://afriref.dev/.well-known/security.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://afriref.dev/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://afriref.dev/terms
created: '2026-10-31'
description: Pan-African government reference data — every value cited to its official source, with an effective date and a last-verified date. Central-bank policy rates, VAT, minimum wages and public holidays for 34 Pan-African countries. Part of a seven-region fleet covering 128 countries plus the EU.
image: https://afriref.dev/og.png
jsonld:
- class_count: 7
  name: Afriref Dev Context
  property_count: 54
  slug: afriref-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at afriref.dev.
  name: afriref MCP Server
  slug: afriref-dev-mcp-yml
modified: '2026-10-31'
name: afriref
nav: Providers
network: true
overview: 'afriref publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Government, Africa, and Reference.


  The afriref catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  afriref''s developer surface includes documentation, pricing, and 22 more developer resources.'
plans:
- name: Afriref Dev Plans Pricing
  plan_count: 10
  slug: afriref-dev-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: afriref API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: afriref-dev-rules
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.4
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 13.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - africa
  previous_composite: 32.5
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afriref Dev Domain Security
  slug: afriref-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Afriref Dev Vulnerability Disclosure
  slug: afriref-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: afriref-dev
tags:
- Company
- Data
- Government
- Africa
- Reference
website: https://afriref.dev/
---
