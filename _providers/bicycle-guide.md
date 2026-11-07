---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bicycle Guide Agentic Access
  operation_count: 8
  slug: bicycle-guide-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://bicycle.guide
  baseurl_source: declared
  description: The published-guide registry, taxonomy and capability spine.
  name: Bicycle Guide Guide Registry API
  slug: bicycle-guide-guide-registry-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bicycle-guide/agentic-access/bicycle-guide-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bicycle-guide-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bicycle-guide/plans/bicycle-guide-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bicycle-guide-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bicycle-guide/rules/bicycle-guide-rules.yml
  title: ''
  type: Spectral
  url: rules/bicycle-guide-rules.yml
- group: design
  href: https://artifacts.apis.io/bicycle-guide/vocabulary/bicycle-guide-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bicycle-guide-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bicycle-guide/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bicycle-guide/errors/bicycle-guide-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bicycle-guide-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bicycle-guide/conformance/bicycle-guide-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bicycle-guide-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bicycle-guide/llms/bicycle-guide-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bicycle-guide-llms.txt
- group: agent
  href: https://artifacts.apis.io/bicycle-guide/mcp/bicycle-guide-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bicycle-guide-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bicycle-guide/well-known/bicycle-guide-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bicycle-guide-well-known.yml
- group: other
  href: https://artifacts.apis.io/bicycle-guide/hosts/bicycle-guide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bicycle-guide-hosts.yml
- group: other
  href: https://artifacts.apis.io/bicycle-guide/vendors/bicycle-guide-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bicycle-guide-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bicycle.guide/terms
- group: operate
  title: ''
  type: Support
  url: https://bicycle.guide/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bicycle.guide/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://bicycle.guide/guides
- group: docs
  title: ''
  type: APIReference
  url: https://bicycle.guide/llms.txt
- group: auth
  href: https://artifacts.apis.io/bicycle-guide/authentication/bicycle-guide-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bicycle-guide-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bicycle-guide/security/bicycle-guide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bicycle-guide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bicycle.guide/
created: '2026-11-02'
description: Bicycle Guide provides a curated library of guides and resources to help readers understand books, topics, and practical next steps. The platform aggregates expert content, offering searchable collections, personalized recommendations, and AI‑enhanced summaries to assist learners in navigating complex subjects and making informed decisions.
image: https://bicycle.guide/opengraph-image-1oy18k?29435694197f5727
layout: provider
mcp_servers:
- description: Remote MCP server at bicycle.guide.
  name: Bicycle Guide MCP Server
  slug: bicycle-guide-mcp-yml
modified: '2026-11-02'
name: Bicycle Guide
nav: Providers
network: true
overview: 'Bicycle Guide publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Guide Registry API. Tagged areas include Company, Guides, Artificial Intelligence, Education, and Library.


  The Bicycle Guide catalog on APIs.io includes 1 Spectral governance ruleset.


  Bicycle Guide''s developer surface includes support, documentation, API reference, authentication, and 16 more developer resources.'
plans:
- name: Bicycle Guide Plans Pricing
  plan_count: 3
  slug: bicycle-guide-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Bicycle Guide API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: bicycle-guide-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 29.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bicycle Guide Authentication
  slug: bicycle-guide-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bicycle Guide Domain Security
  slug: bicycle-guide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bicycle-guide
tags:
- Company
- Guides
- Artificial Intelligence
- Education
- Library
website: https://bicycle.guide/
---
