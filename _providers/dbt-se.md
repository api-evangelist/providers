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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 115
  human_in_the_loop: 2
  name: Dbt Se Agentic Access
  operation_count: 306
  slug: dbt-se-agentic-access
  summary_line: 306 operations · 115 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: The Agents API from DBT Capital — 1 operation(s) for agents.
  name: DBT Capital Agents API
  slug: dbt-se-agents-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Banking and payment operations
  name: DBT Capital Banking API
  slug: dbt-se-banking-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Bookkeeping and accounting
  name: DBT Capital Bookkeeping API
  slug: dbt-se-bookkeeping-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Document management
  name: DBT Capital Documents API
  slug: dbt-se-documents-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: File operations
  name: DBT Capital Files API
  slug: dbt-se-files-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Identity and authentication
  name: DBT Capital Identity API
  slug: dbt-se-identity-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: AI and language model operations
  name: DBT Capital LLM API
  slug: dbt-se-llm-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Email and notification delivery
  name: DBT Capital Notification API
  slug: dbt-se-notification-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Client portfolio management
  name: DBT Capital Portfolio API
  slug: dbt-se-portfolio-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Prospect and deal management
  name: DBT Capital Prospect API
  slug: dbt-se-prospect-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Regulatory and compliance records
  name: DBT Capital Regulatory Records API
  slug: dbt-se-regulatory-records-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: UC credit information
  name: DBT Capital UC API
  slug: dbt-se-uc-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: File uploads
  name: DBT Capital Upload API
  slug: dbt-se-upload-api
- baseURL: https://api.p.dbt.se
  baseurl_source: declared
  description: Analysis workbooks and models
  name: DBT Capital Workbooks API
  slug: dbt-se-workbooks-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/agentic-access/dbt-se-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dbt-se-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/rules/dbt-se-rules.yml
  title: ''
  type: Spectral
  url: rules/dbt-se-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/json-ld/dbt-se-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dbt-se-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/vocabulary/dbt-se-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dbt-se-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/data-model/dbt-se-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dbt-se-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/errors/dbt-se-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dbt-se-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/conformance/dbt-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dbt-se-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/llms/dbt-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dbt-se-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/well-known/dbt-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dbt-se-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/hosts/dbt-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dbt-se-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/vendors/dbt-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dbt-se-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dbt.se/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/authentication/dbt-se-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dbt-se-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dbt-se/refs/heads/main/security/dbt-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dbt-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dbt.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dbt.se/foretagslan
- group: operate
  title: ''
  type: Support
  url: https://www.dbt.se/kontakt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dbt.se/privacy-policy
created: '2026-10-15'
description: DBT Capital provides corporate loans to growing businesses in Sweden, offering financing from 5 to 150 million SEK for acquisitions, growth, refinancing, or working capital. The company emphasizes flexible loan terms and partners with the European Investment Fund (EIF) to guarantee financing, aiming to support companies throughout their development stages.
image: https://www.dbt.se/hubfs/Google%20omslagsbild.png
json_schemas:
- name: BaseSummationAccountPlanAdjustmentRequestBody
  property_count: 3
  slug: dbt-se-base-summation-account-plan-adjustment-request-body
- name: CollateralValuationResponseBody
  property_count: 15
  slug: dbt-se-collateral-valuation-response-body
- name: GetLGDPotentialResponseBody
  property_count: 4
  slug: dbt-se-get-lgdpotential-response-body
- name: HealthChecksResolvedStatusResponseBody
  property_count: 2
  slug: dbt-se-health-checks-resolved-status-response-body
- name: Organization
  property_count: 8
  slug: dbt-se-organization
- name: PortfolioOrganization
  property_count: 22
  slug: dbt-se-portfolio-organization
jsonld:
- class_count: 120
  name: Dbt Se Context
  property_count: 199
  slug: dbt-se-context
layout: provider
modified: '2026-10-15'
name: DBT Capital
nav: Providers
network: true
overview: 'DBT Capital publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Banking API, Bookkeeping API, and 11 more. Tagged areas include Company, Finance, Loans, Sweden, and Business.


  The DBT Capital catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DBT Capital''s developer surface includes authentication, documentation, support, and 16 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: DBT Capital API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 5
  slug: dbt-se-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 60.9
    developer_ergonomics: 28.0
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Dbt Se Authentication
  slug: dbt-se-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Dbt Se Domain Security
  slug: dbt-se-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dbt-se
tags:
- Company
- Finance
- Loans
- Sweden
- Business
website: https://dbt.se/
---
