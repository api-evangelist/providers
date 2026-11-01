---
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Popsql Agentic Access
  operation_count: 13
  slug: popsql-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.popsql.com/v1
  baseurl_source: declared
  description: The Data Catalog API from PopSQL — 7 operation(s) for data catalog.
  name: PopSQL Data Catalog API
  slug: popsql-data-catalog-api
- baseURL: https://api.popsql.com/v1
  baseurl_source: declared
  description: The Query Runs API from PopSQL — 1 operation(s) for query runs.
  name: PopSQL Query Runs API
  slug: popsql-query-runs-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/popsql/agentic-access/popsql-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/popsql-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/popsql/rules/popsql-rules.yml
  title: ''
  type: Spectral
  url: rules/popsql-rules.yml
- group: design
  href: https://artifacts.apis.io/popsql/json-ld/popsql-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/popsql-context.jsonld
- group: design
  href: https://artifacts.apis.io/popsql/vocabulary/popsql-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/popsql-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/popsql/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/popsql/data-model/popsql-data-model.yml
  title: ''
  type: DataModel
  url: data-model/popsql-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://popsql.com/security
- group: design
  href: https://artifacts.apis.io/popsql/conformance/popsql-conformance.yml
  title: ''
  type: Conformance
  url: conformance/popsql-conformance.yml
- group: other
  href: https://artifacts.apis.io/popsql/overlays/popsql-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/popsql-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/popsql/llms/popsql-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/popsql-llms.txt
- group: other
  href: https://artifacts.apis.io/popsql/hosts/popsql-hosts.yml
  title: ''
  type: Hosts
  url: hosts/popsql-hosts.yml
- group: other
  href: https://artifacts.apis.io/popsql/vendors/popsql-vendors.yml
  title: ''
  type: Vendors
  url: vendors/popsql-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://popsql.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://popsql.com/static/press/popsql-presskit-2023.zip
- group: operate
  title: ''
  type: ChangeLog
  url: https://popsql.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/popsql
- group: auth
  href: https://artifacts.apis.io/popsql/authentication/popsql-authentication.yml
  title: ''
  type: Authentication
  url: authentication/popsql-authentication.yml
- group: auth
  href: https://artifacts.apis.io/popsql/security/popsql-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/popsql-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/popsql/security/popsql-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/popsql-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/popsql/security/popsql-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/popsql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://popsql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.popsql.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.popsql.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.popsql.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.popsql.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://popsql.com/contact
- group: company
  title: ''
  type: Blog
  url: https://popsql.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://popsql.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://popsql.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://popsql.com/privacy
created: '2026-10-29'
description: PopSQL is a unified SQL collaboration workspace that connects everyone in the data analysis process so you can obtain better insights by asking the right questions, together. It offers a collaborative SQL editor, visual query builder, and powerful data sharing tools for teams to work on queries, dashboards, and reports in real time.
image: https://images.ctfassets.net/iv1sg9nibjwl/L9cy5FXJHXiAvZABkKvwa/5308dd58add6c033ac404c556010f445/homepage_og.jpg
json_schemas:
- name: ColumnSearchResult
  property_count: 4
  slug: popsql-column-search-result
- name: TableSearchResult
  property_count: 4
  slug: popsql-table-search-result
- name: UpdateColumnRequest
  property_count: 4
  slug: popsql-update-column-request
- name: UpdateTableRequest
  property_count: 3
  slug: popsql-update-table-request
jsonld:
- class_count: 4
  name: Popsql Context
  property_count: 5
  slug: popsql-context
layout: provider
modified: '2026-10-29'
name: PopSQL
nav: Providers
network: true
overview: 'PopSQL publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Data Catalog API and Query Runs API. Tagged areas include Company, SQL, Collaboration, Data-Analytics, and Cloud.


  The PopSQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PopSQL''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: PopSQL API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: popsql-rules
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 63.6
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Popsql Authentication
  slug: popsql-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Popsql Domain Security
  slug: popsql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Popsql Vulnerability Disclosure
  slug: popsql-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Popsql Trust Center
  slug: popsql-trust-center
  summary_line: SOC 2, GDPR
slug: popsql
tags:
- Company
- SQL
- Collaboration
- Data-Analytics
- Cloud
website: https://popsql.com/
---
