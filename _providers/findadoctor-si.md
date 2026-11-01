---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Findadoctor Si Agentic Access
  operation_count: 20
  slug: findadoctor-si-agentic-access
  summary_line: 20 operations
api_count: 3
apis:
- baseURL: https://api-fr.findadoctor.si
  baseurl_source: declared
  description: The About API from findadoctor-si — 1 operation(s) for about.
  name: findadoctor-si About API
  slug: findadoctor-si-about-api
- baseURL: https://api-fr.findadoctor.si
  baseurl_source: declared
  description: The Doctors API from findadoctor-si — 2 operation(s) for doctors.
  name: findadoctor-si Doctors API
  slug: findadoctor-si-doctors-api
- baseURL: https://api-nz.findadoctor.si
  baseurl_source: declared
  description: The Gp Practices API from findadoctor-si — 1 operation(s) for gp practices.
  name: findadoctor-si Gp Practices API
  slug: findadoctor-si-gp-practices-api
- baseURL: https://api-fr.findadoctor.si
  baseurl_source: declared
  description: The Procedure Volumes API from findadoctor-si — 1 operation(s) for procedure volumes.
  name: findadoctor-si Procedure Volumes API
  slug: findadoctor-si-procedure-volumes-api
- baseURL: https://api.findadoctor.si
  baseurl_source: declared
  description: The Procedures API from findadoctor-si — 1 operation(s) for procedures.
  name: findadoctor-si Procedures API
  slug: findadoctor-si-procedures-api
- baseURL: https://api-fr.findadoctor.si
  baseurl_source: declared
  description: The Search API from findadoctor-si — 1 operation(s) for search.
  name: findadoctor-si Search API
  slug: findadoctor-si-search-api
- baseURL: https://api-fr.findadoctor.si
  baseurl_source: declared
  description: The Specialties API from findadoctor-si — 1 operation(s) for specialties.
  name: findadoctor-si Specialties API
  slug: findadoctor-si-specialties-api
- baseURL: https://api.findadoctor.si
  baseurl_source: declared
  description: The Terms API from findadoctor-si — 1 operation(s) for terms.
  name: findadoctor-si Terms API
  slug: findadoctor-si-terms-api
- baseURL: https://api-nz.findadoctor.si
  baseurl_source: declared
  description: The Waitlist API from findadoctor-si — 1 operation(s) for waitlist.
  name: findadoctor-si Waitlist API
  slug: findadoctor-si-waitlist-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/findadoctor-si/agentic-access/findadoctor-si-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/findadoctor-si-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/findadoctor-si/rate-limits/findadoctor-si-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/findadoctor-si-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/findadoctor-si/rules/findadoctor-si-rules.yml
  title: ''
  type: Spectral
  url: rules/findadoctor-si-rules.yml
- group: design
  href: https://artifacts.apis.io/findadoctor-si/json-ld/findadoctor-si-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/findadoctor-si-context.jsonld
- group: design
  href: https://artifacts.apis.io/findadoctor-si/vocabulary/findadoctor-si-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/findadoctor-si-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/findadoctor-si/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/findadoctor-si/data-model/findadoctor-si-data-model.yml
  title: ''
  type: DataModel
  url: data-model/findadoctor-si-data-model.yml
- group: operate
  href: https://artifacts.apis.io/findadoctor-si/changelog/findadoctor-si-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/findadoctor-si-changelog.yml
- group: design
  href: https://artifacts.apis.io/findadoctor-si/conventions/findadoctor-si-conventions.yml
  title: ''
  type: Conventions
  url: conventions/findadoctor-si-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://findadoctor.si/support/
- group: design
  href: https://artifacts.apis.io/findadoctor-si/errors/findadoctor-si-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/findadoctor-si-problem-types.yml
- group: design
  href: https://artifacts.apis.io/findadoctor-si/conformance/findadoctor-si-conformance.yml
  title: ''
  type: Conformance
  url: conformance/findadoctor-si-conformance.yml
- group: agent
  href: https://artifacts.apis.io/findadoctor-si/llms/findadoctor-si-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/findadoctor-si-llms.txt
- group: build
  href: https://artifacts.apis.io/findadoctor-si/mcp/findadoctor-si-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/findadoctor-si-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/findadoctor-si/mcp/findadoctor-si-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/findadoctor-si-mcp.yml
- group: auth
  href: https://artifacts.apis.io/findadoctor-si/well-known/findadoctor-si-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/findadoctor-si-security.txt
- group: agent
  href: https://artifacts.apis.io/findadoctor-si/well-known/findadoctor-si-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/findadoctor-si-well-known.yml
- group: other
  href: https://artifacts.apis.io/findadoctor-si/hosts/findadoctor-si-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findadoctor-si-hosts.yml
- group: other
  href: https://artifacts.apis.io/findadoctor-si/vendors/findadoctor-si-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findadoctor-si-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://findadoctor.si/us/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://findadoctor.si/us/docs/index
- group: auth
  href: https://artifacts.apis.io/findadoctor-si/security/findadoctor-si-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/findadoctor-si-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/findadoctor-si/security/findadoctor-si-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findadoctor-si-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://findadoctor.si/
- group: docs
  title: ''
  type: APIReference
  url: https://api.findadoctor.si/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://findadoctor.si/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://findadoctor.si/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://findadoctor.si/privacy/
created: '2026-10-29'
description: FindADoctor.si provides doctor data for AI agents, covering the United States, New Zealand, and France. It serves official records and facts from doctors' own hospital pages via an MCP endpoint and a standard HTTP JSON API. The service offers read‑only search over physicians, delivering sourced evidence, NPI registry information, health‑system waiting lists, and national procedure statistics. Data is regularly updated and includes procedural volume data. The platform is free during testing.
image: https://findadoctor.si/assets/hero/og-world.jpg
json_schemas:
- name: DoctorBatch
  property_count: 5
  slug: findadoctor-si-doctor-batch
- name: Doctor
  property_count: 49
  slug: findadoctor-si-doctor
- name: GpResult
  property_count: 8
  slug: findadoctor-si-gp-result
- name: HospitalVolumes
  property_count: 14
  slug: findadoctor-si-hospital-volumes
- name: Provider
  property_count: 3
  slug: findadoctor-si-provider
- name: SearchResult
  property_count: 8
  slug: findadoctor-si-search-result
- name: WaitlistRow
  property_count: 9
  slug: findadoctor-si-waitlist-row
jsonld:
- class_count: 17
  name: Findadoctor Si Context
  property_count: 146
  slug: findadoctor-si-context
layout: provider
mcp_servers:
- description: Remote MCP server at api-fr.findadoctor.si.
  name: findadoctor-si MCP Server
  slug: findadoctor-si-mcp-yml
modified: '2026-10-29'
name: findadoctor-si
nav: Providers
network: true
overview: 'findadoctor-si publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including About API, Doctors API, Gp Practices API, and 6 more. Tagged areas include Company, Healthcare, Data, AI, and Doctor.


  The findadoctor-si catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  findadoctor-si''s developer surface includes changelog, getting-started guide, API reference, support, and 24 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 6
  name: Findadoctor Si Rate Limits
  slug: findadoctor-si-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: findadoctor-si API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: findadoctor-si-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.0
    catalog_earned_first_party: 12.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 62.1
    developer_ergonomics: 39.8
    discoverability: 70.0
    operational_transparency: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Findadoctor Si Authentication
  slug: findadoctor-si-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Findadoctor Si Domain Security
  slug: findadoctor-si-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Findadoctor Si Vulnerability Disclosure
  slug: findadoctor-si-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: about-database
  slug: findadoctor-si-about-database
- name: get-doctor
  slug: findadoctor-si-get-doctor
- name: hospital-procedure-volumes
  slug: findadoctor-si-hospital-procedure-volumes
- name: list-specialties
  slug: findadoctor-si-list-specialties
- name: search-doctors
  slug: findadoctor-si-search-doctors
slug: findadoctor-si
tags:
- Company
- Healthcare
- Data
- AI
- Doctor
- International
website: https://findadoctor.si/
---
