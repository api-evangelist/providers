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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://memory.tulimoa.com
  baseurl_source: declared
  description: 'tulimoa-com API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: tulimoa-com API
  slug: tulimoa-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/tulimoa-com/plans/tulimoa-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tulimoa-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tulimoa-com/rules/tulimoa-com-rules.yml
  title: ''
  type: Spectral
  url: rules/tulimoa-com-rules.yml
- group: design
  href: https://artifacts.apis.io/tulimoa-com/json-ld/tulimoa-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tulimoa-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/tulimoa-com/vocabulary/tulimoa-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tulimoa-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tulimoa-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tulimoa-com/data-model/tulimoa-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tulimoa-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://tulimoa.com/trust
- group: design
  href: https://artifacts.apis.io/tulimoa-com/conformance/tulimoa-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tulimoa-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tulimoa-com/llms/tulimoa-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tulimoa-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/tulimoa-com/well-known/tulimoa-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tulimoa-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/tulimoa-com/hosts/tulimoa-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tulimoa-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tulimoa-com/vendors/tulimoa-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tulimoa-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://tulimoa.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tulimoa
- group: auth
  href: https://artifacts.apis.io/tulimoa-com/security/tulimoa-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tulimoa-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tulimoa-com/security/tulimoa-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tulimoa-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tulimoa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tulimoa.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tulimoa.com/pricing
- group: operate
  title: ''
  type: Roadmap
  url: https://tulimoa.com/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tulimoa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tulimoa.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://tulimoa.com/help
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are rendered with JavaScript and provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://docs.tulimoa.com/memory-tools
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Tulimoa operates a hand‑reviewed directory for AI and MCP software, curating tools that have been vetted by a person before being listed. The platform offers a searchable catalog, weekly radar updates, and detailed reviews, while also providing submission pathways for developers. It emphasizes quality control, with a high rejection rate for unverified submissions, and maintains sections for pricing, roadmaps, and documentation, reflecting a comprehensive resource for AI and MCP tool discovery.
image: https://tulimoa.com/og.png
json_schemas:
- name: PostImportRequest
  property_count: 3
  slug: tulimoa-com-post-import-request
- name: PostImportResponse
  property_count: 4
  slug: tulimoa-com-post-import-response
- name: PostIngestRequest
  property_count: 2
  slug: tulimoa-com-post-ingest-request
jsonld:
- class_count: 3
  name: Tulimoa Com Context
  property_count: 8
  slug: tulimoa-com-context
layout: provider
modified: '2026-10-30'
name: tulimoa-com
nav: Providers
network: true
overview: 'tulimoa-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Directory, Artificial Intelligence, MCP, and Reviews.


  The tulimoa-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tulimoa-com''s developer surface includes changelog, documentation, pricing, support, and 19 more developer resources.'
plans:
- name: Tulimoa Com Plans Pricing
  plan_count: 8
  slug: tulimoa-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: tulimoa-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: tulimoa-com-rules
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 21.4
    developer_ergonomics: 13.6
    discoverability: 73.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tulimoa-com/tulimoa-com-2026-11-03T145228.png
security:
- kind: domain-security
  name: Tulimoa Com Domain Security
  slug: tulimoa-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tulimoa Com Trust Center
  slug: tulimoa-com-trust-center
  summary_line: SOC 2, GDPR
slug: tulimoa-com
tags:
- Company
- Directory
- Artificial Intelligence
- MCP
- Reviews
website: https://tulimoa.com/
---
