---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Modiqo Agentic Access
  operation_count: 1
  slug: modiqo-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- baseURL: https://www.modiqo.ai
  baseurl_source: declared
  description: Contact Modiqo about rote plans and deployment.
  name: Modiqo Sales API
  slug: modiqo-sales-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/modiqo/agentic-access/modiqo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/modiqo-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/modiqo/plans/modiqo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modiqo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/modiqo/rules/modiqo-rules.yml
  title: ''
  type: Spectral
  url: rules/modiqo-rules.yml
- group: design
  href: https://artifacts.apis.io/modiqo/json-ld/modiqo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/modiqo-context.jsonld
- group: design
  href: https://artifacts.apis.io/modiqo/vocabulary/modiqo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/modiqo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/modiqo/data-model/modiqo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/modiqo-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://www.modiqo.ai/legal/TERMS_OF_SERVICE.md
- group: design
  href: https://artifacts.apis.io/modiqo/errors/modiqo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/modiqo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/modiqo/conformance/modiqo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/modiqo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/modiqo/llms/modiqo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/modiqo-llms.txt
- group: auth
  href: https://artifacts.apis.io/modiqo/well-known/modiqo-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/modiqo-security.txt
- group: agent
  href: https://artifacts.apis.io/modiqo/well-known/modiqo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/modiqo-well-known.yml
- group: other
  href: https://artifacts.apis.io/modiqo/hosts/modiqo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/modiqo-hosts.yml
- group: other
  href: https://artifacts.apis.io/modiqo/vendors/modiqo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/modiqo-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.modiqo.ai/signin
- group: docs
  title: ''
  type: APIReference
  url: https://www.modiqo.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/modiqo/security/modiqo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/modiqo-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/modiqo/security/modiqo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modiqo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.modiqo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.modiqo.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.modiqo.ai/docs/run-your-first-play
- group: commercial
  title: ''
  type: Pricing
  url: https://www.modiqo.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modiqo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modiqo.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.modiqo.ai/blog
created: '2026-10-30'
description: Modiqo builds Rote, a platform that enables teams to capture, reuse, and share AI agent workflows as modular Plays. Users can document successful AI interactions, run them with new inputs, and distribute methods across agents like Claude, Codex, and Cursor. The service offers a marketplace of reusable workflows, integrates with popular AI tools, and provides documentation, pricing, and community resources to help organizations streamline AI-driven processes.
image: https://www.modiqo.ai/assets/brand/modiqo_logo_orange_1024.png
json_schemas:
- name: SalesLeadRequest
  property_count: 14
  slug: modiqo-sales-lead-request
- name: SalesLeadSuccess
  property_count: 3
  slug: modiqo-sales-lead-success
jsonld:
- class_count: 4
  name: Modiqo Context
  property_count: 21
  slug: modiqo-context
layout: provider
modified: '2026-10-30'
name: Modiqo
nav: Providers
network: true
overview: 'Modiqo publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Sales API. Tagged areas include Company, AI, Workflow, Automation, and Platform.


  The Modiqo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Modiqo''s developer surface includes API reference, documentation, getting-started guide, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Modiqo Plans Pricing
  plan_count: 4
  slug: modiqo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Modiqo Rate Limits
  slug: modiqo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Modiqo API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: modiqo-rules
scopes:
- name: Modiqo Scopes
  scope_count: 0
  slug: modiqo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 58.7
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Modiqo Authentication
  slug: modiqo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Modiqo Domain Security
  slug: modiqo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Modiqo Vulnerability Disclosure
  slug: modiqo-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: submit-sales-lead
  slug: modiqo-submit-sales-lead
slug: modiqo
tags:
- Company
- AI
- Workflow
- Automation
- Platform
website: https://www.modiqo.ai
---
