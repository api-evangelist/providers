---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 41
  human_in_the_loop: 2
  name: Rivery Agentic Access
  operation_count: 83
  slug: rivery-agentic-access
  summary_line: 83 operations · 41 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Listing accounts
  name: Rivery Accounts API
  slug: rivery-accounts-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Get the Boomi Data Integration activities data with various of GET operations
  name: Rivery Activities API
  slug: rivery-activities-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Listing account's audit events
  name: Rivery Audit Events API
  slug: rivery-audit-events-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Management of connection entities
  name: Rivery Connections API
  slug: rivery-connections-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Internal endpoints for data flow metadata
  name: Rivery Data Flows Metadata API
  slug: rivery-data-flows-metadata-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Management of dataframe entities
  name: Rivery Dataframes API
  slug: rivery-dataframes-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Listing account's environments
  name: Rivery Environments API
  slug: rivery-environments-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Management of the Logic Python feature
  name: Rivery Logicode API
  slug: rivery-logicode-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Endpoints exposed by the Boomi Data Integration MCP server. Each carries the tool's usage instructions (parameters, prerequisites, gotchas).
  name: Rivery MCP API
  slug: rivery-mcp-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Management of the status response of any given asynchronous operation ID
  name: Rivery Operations API
  slug: rivery-operations-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: The River Source API from Rivery — 1 operation(s) for river source.
  name: Rivery River Source API
  slug: rivery-river-source-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: The Users API from Rivery — 9 operation(s) for users.
  name: Rivery Users API
  slug: rivery-users-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: The Variables API from Rivery — 1 operation(s) for variables.
  name: Rivery Variables API
  slug: rivery-variables-api
- baseURL: https://api.rivery.io
  baseurl_source: declared
  description: Management of data flows
  name: Rivery Dataflows API
  slug: rivery-dataflows-api
artifact_total: 26
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/agentic-access/rivery-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rivery-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/plans/rivery-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rivery-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/rules/rivery-rules.yml
  title: ''
  type: Spectral
  url: rules/rivery-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/json-ld/rivery-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rivery-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/vocabulary/rivery-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rivery-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/data-model/rivery-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rivery-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/conventions/rivery-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rivery-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/authentication/rivery-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rivery-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/errors/rivery-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rivery-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/conformance/rivery-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rivery-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/hosts/rivery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rivery-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/vendors/rivery-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rivery-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://rivery.io/integration/webhook/
- group: company
  title: ''
  type: Blog
  url: https://rivery.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.boomi.com/docs/Atomsphere/Platform/quickstart_guides
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.rivery.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rivery/refs/heads/main/security/rivery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rivery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rivery.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.boomi.com/docs/Atomsphere/Data_Integration/Data_Integration_Overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.rivery.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://rivery.io/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rivery.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rivery.io/terms-of-use
created: '2026-10-03'
description: Rivery provides a cloud ELT (Extract, Load, Transform) platform that enables organizations to integrate, orchestrate, and automate data pipelines across a wide range of sources and destinations. The low‑code solution supports data ingestion, transformation, CDC replication, reverse ETL, and data‑ops management, offering a unified interface for building scalable data workflows. Rivery’s platform is designed for both technical and business users, featuring AI‑assisted pipeline creation, extensive connector library, and robust security controls, positioning it as a comprehensive data integration tool now part of Boomi.
image: https://rivery.io/wp-content/uploads/2021/07/more_than_an_etl_.jpg
json_schemas:
- name: AuditEventsResponse
  property_count: 15
  slug: rivery-audit-events-response
- name: EnvironmentsFields
  property_count: 16
  slug: rivery-environments-fields
- name: RiverActivityRun
  property_count: 21
  slug: rivery-river-activity-run
- name: RiverVersions
  property_count: 13
  slug: rivery-river-versions
- name: UserModel
  property_count: 20
  slug: rivery-user-model
- name: WriteRiverInput
  property_count: 14
  slug: rivery-write-river-input
jsonld:
- class_count: 120
  name: Rivery Context
  property_count: 241
  slug: rivery-context
layout: provider
modified: '2026-10-03'
name: Rivery
nav: Providers
network: true
overview: 'Rivery publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Audit Events API, and 11 more. Tagged areas include Data Integration, ELT, Cloud, Low-Code, and Boomi.


  The Rivery catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rivery''s developer surface includes authentication, engineering blog, getting-started guide, API reference, documentation, pricing, and 18 more developer resources.'
plans:
- name: Rivery Plans Pricing
  plan_count: 4
  slug: rivery-plans-pricing
random_paper: 13
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Rivery API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: rivery-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 7.9
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
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Rivery Authentication
  slug: rivery-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Rivery Domain Security
  slug: rivery-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rivery
tags:
- Data Integration
- ELT
- Cloud
- Low-Code
- Boomi
website: https://rivery.io/
---
