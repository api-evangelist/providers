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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: false
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
  score: 3.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agentrequest Dev Agentic Access
  operation_count: 5
  slug: agentrequest-dev-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Free MCP API for reporting blocked fetches and retrieving demo reports. Provides endpoints /api/request, /api/demand, /api/key, /api/report.
  name: Agent Request Desk API
  slug: agent-request-desk-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/agentrequest-dev/agentic-access/agentrequest-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentrequest-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/rules/agentrequest-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/agentrequest-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/json-ld/agentrequest-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentrequest-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/vocabulary/agentrequest-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentrequest-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentrequest-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/data-model/agentrequest-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentrequest-dev-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://agentrequest.dev/privacy
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/errors/agentrequest-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentrequest-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentrequest-dev/conformance/agentrequest-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentrequest-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentrequest-dev/llms/agentrequest-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrequest-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentrequest-dev/well-known/agentrequest-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentrequest-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/agentrequest-dev/well-known/agentrequest-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentrequest-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentrequest-dev/hosts/agentrequest-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrequest-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentrequest-dev/vendors/agentrequest-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentrequest-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentrequest-dev/security/agentrequest-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentrequest-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentrequest-dev/security/agentrequest-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrequest-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrequest.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://agentrequest.dev/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentrequest.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentrequest.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://agentrequest.dev/report
- group: start
  title: ''
  type: GettingStarted
  url: https://agentrequest.dev/mcp
- group: auth
  href: https://artifacts.apis.io/agentrequest-dev/security/agentrequest-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentrequest-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentrequest-dev/security/agentrequest-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrequest-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrequest.dev/
created: '2026-11-01'
description: Agent Request Desk provides a free MCP server that helps AI agents report and diagnose failures when accessing external sites. It captures blocked URLs, missing data, and error reasons, offering private reports without requiring accounts. The service aggregates public issue data, supports multiple client integrations (Claude, Cursor, VS Code, n8n), and supplies pointers to official APIs or datasets when available. Operated by Patrick Hussey in the UK, it aims to improve agent reliability and transparency.
jsonld:
- class_count: 3
  name: Agentrequest Dev Context
  property_count: 19
  slug: agentrequest-dev-context
layout: provider
modified: '2026-11-01'
name: Agent Request Desk
nav: Providers
network: true
overview: 'Agent Request Desk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, MCP, Diagnostics, and Free.


  The Agent Request Desk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agent Request Desk''s developer surface includes API reference, engineering blog, getting-started guide, and 22 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Agent Request Desk API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentrequest-dev-rules
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 12.5
    discoverability: 62.5
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 22.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrequest Dev Domain Security
  slug: agentrequest-dev-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Agentrequest Dev Vulnerability Disclosure
  slug: agentrequest-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: agentrequest-dev-report-need
  slug: agentrequest-dev-report-need
slug: agentrequest-dev
tags:
- Company
- Artificial Intelligence
- MCP
- Diagnostics
- Free
- United Kingdom
website: https://agentrequest.dev/
---
