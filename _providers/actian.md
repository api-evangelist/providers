---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Actian Agentic Access
  operation_count: 29
  slug: actian-agentic-access
  summary_line: 29 operations · 18 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Create, list, rotate, and delete access tokens.
  name: Actian Corporation Access Tokens API
  slug: actian-access-tokens-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Create and manage the admin user, login, and authentication settings.
  name: Actian Corporation Admin User API
  slug: actian-admin-user-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Collection lifecycle management operations
  name: Actian Corporation Collections API
  slug: actian-collections-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Counting operations
  name: Actian Corporation Count API
  slug: actian-count-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Filter construction and usage
  name: Actian Corporation Filters API
  slug: actian-filters-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Point data operations
  name: Actian Corporation Points API
  slug: actian-points-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Pagination and iteration
  name: Actian Corporation Scroll API
  slug: actian-scroll-api
- baseURL: https://api.vectorai.actian.com
  baseurl_source: declared
  description: Vector similarity search operations
  name: Actian Corporation Search API
  slug: actian-search-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/actian/agentic-access/actian-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/actian-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/actian/plans/actian-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actian-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/actian/rules/actian-rules.yml
  title: ''
  type: Spectral
  url: rules/actian-rules.yml
- group: design
  href: https://artifacts.apis.io/actian/json-ld/actian-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/actian-context.jsonld
- group: design
  href: https://artifacts.apis.io/actian/vocabulary/actian-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/actian-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/actian/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/actian/data-model/actian-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actian-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.actian.com/
- group: design
  href: https://artifacts.apis.io/actian/errors/actian-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/actian-problem-types.yml
- group: design
  href: https://artifacts.apis.io/actian/conformance/actian-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actian-conformance.yml
- group: agent
  href: https://artifacts.apis.io/actian/llms/actian-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actian-llms.txt
- group: auth
  href: https://artifacts.apis.io/actian/well-known/actian-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/actian-security.txt
- group: agent
  href: https://artifacts.apis.io/actian/well-known/actian-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/actian-well-known.yml
- group: other
  href: https://artifacts.apis.io/actian/hosts/actian-hosts.yml
  title: ''
  type: Hosts
  url: hosts/actian-hosts.yml
- group: other
  href: https://artifacts.apis.io/actian/vendors/actian-vendors.yml
  title: ''
  type: Vendors
  url: vendors/actian-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.actian.com/company/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ActianCorp
- group: auth
  href: https://artifacts.apis.io/actian/authentication/actian-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actian-authentication.yml
- group: auth
  href: https://artifacts.apis.io/actian/security/actian-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/actian-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/actian/security/actian-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actian-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://actian.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.actian.com/developer/
- group: company
  title: ''
  type: Blog
  url: https://www.actian.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.actian.com/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.actian.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.actian.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.actian.com/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.actian.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.actian.com/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.actian.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/actian/workspace
created: '2026-10-19'
description: Actian Corporation provides data management, integration, and analytics solutions, including the Actian Data Intelligence platform, AI-driven data observability, and enterprise databases. The company focuses on enabling AI-powered data insights, metadata governance, and real-time data anomaly detection for enterprises.
image: https://www.actian.com/wp-content/uploads/2024/02/actian-logo-thumbnail.png
jsonld:
- class_count: 5
  name: Actian Context
  property_count: 9
  slug: actian-context
layout: provider
modified: '2026-10-19'
name: Actian Corporation
nav: Providers
network: true
overview: 'Actian Corporation publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Tokens API, Admin User API, Collections API, and 5 more. Tagged areas include Company, Data, Integration, Analytics, and Artificial Intelligence.


  The Actian Corporation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Actian Corporation''s developer surface includes authentication, engineering blog, getting-started guide, pricing, support, documentation, API reference, and 24 more developer resources.'
plans:
- name: Actian Plans Pricing
  plan_count: 4
  slug: actian-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Actian Corporation API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: actian-rules
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 54.7
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Actian Authentication
  slug: actian-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Actian Domain Security
  slug: actian-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Actian Trust Center
  slug: actian-trust-center
  summary_line: HIPAA, GDPR
skill_count: 1
skills:
- name: actian-admin-user-setup
  slug: actian-admin-user-setup
slug: actian
tags:
- Company
- Data
- Integration
- Analytics
- Artificial Intelligence
- Enterprise
website: https://actian.com/
---
