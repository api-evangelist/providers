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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Ninox API as documented publicly: 25 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Ninox API
  slug: ninoxdb-de-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/ninoxdb-de/plans/ninoxdb-de-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ninoxdb-de-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ninoxdb-de/rules/ninoxdb-de-rules.yml
  title: ''
  type: Spectral
  url: rules/ninoxdb-de-rules.yml
- group: design
  href: https://artifacts.apis.io/ninoxdb-de/json-ld/ninoxdb-de-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ninoxdb-de-context.jsonld
- group: design
  href: https://artifacts.apis.io/ninoxdb-de/vocabulary/ninoxdb-de-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ninoxdb-de-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ninoxdb-de/data-model/ninoxdb-de-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ninoxdb-de-data-model.yml
- group: operate
  href: https://artifacts.apis.io/ninoxdb-de/changelog/ninoxdb-de-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ninoxdb-de-changelog.yml
- group: design
  href: https://artifacts.apis.io/ninoxdb-de/conformance/ninoxdb-de-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ninoxdb-de-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ninoxdb-de/llms/ninoxdb-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ninoxdb-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/ninoxdb-de/well-known/ninoxdb-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ninoxdb-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/ninoxdb-de/hosts/ninoxdb-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ninoxdb-de-hosts.yml
- group: other
  href: https://artifacts.apis.io/ninoxdb-de/vendors/ninoxdb-de-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ninoxdb-de-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://ninox.com/en/resources/support
- group: company
  title: ''
  type: Newsroom
  url: https://ninox.com/en/press
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ninox.com/getting-started/getting-started
- group: auth
  href: https://artifacts.apis.io/ninoxdb-de/security/ninoxdb-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ninoxdb-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ninox.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ninox.com/home/de
- group: commercial
  title: ''
  type: Pricing
  url: https://ninox.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://ninox.com/en/resources/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ninox.com/en/legal-notices/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ninox.com/en/legal-notices/privacy
created: '2026-10-24'
description: Ninox provides a low-code platform for building custom business applications and databases. It enables users to create, share, and collaborate on data-driven apps without extensive programming knowledge. The platform offers a visual interface, powerful scripting, and integrations with various services, making it suitable for teams of all sizes to manage workflows, track assets, and automate processes. Ninox aims to simplify data management and empower organizations to build tailored solutions quickly and efficiently.
image: https://cdn.prod.website-files.com/697c688eb79bc2291521f16e/69e76da195fc67b9af8e5924_OpenGraph_Ninox.png
json_schemas:
- name: GetApiV1WorkspaceWorkspaceidModulesModulenameDefinitionRespo
  property_count: 4
  slug: ninoxdb-de-get-api-v1-workspace-workspaceid-modules-modulename-definition-respo
jsonld:
- class_count: 1
  name: Ninoxdb De Context
  property_count: 0
  slug: ninoxdb-de-context
layout: provider
modified: '2026-10-24'
name: Ninox
nav: Providers
network: true
overview: 'Ninox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, Platform, Business Apps, and Database.


  The Ninox catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ninox''s developer surface includes changelog, support, getting-started guide, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Ninoxdb De Plans Pricing
  plan_count: 4
  slug: ninoxdb-de-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Ninox API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ninoxdb-de-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.2
    catalog_earned_first_party: 12.0
    catalog_gap: 54.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 15.7
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.1
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/ninoxdb-de/ninoxdb-de-2026-11-03T140221.png
security:
- kind: domain-security
  name: Ninoxdb De Domain Security
  slug: ninoxdb-de-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ninoxdb-de
tags:
- Company
- Low-Code
- Platform
- Business Apps
- Database
website: https://ninox.com/en
---
