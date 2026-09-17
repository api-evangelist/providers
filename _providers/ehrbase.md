---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The ADL 1.4 TEMPLATE API from EHRbase — 3 operation(s) for adl 1.4 template.
  name: EHRbase ADL 1.4 TEMPLATE API
  slug: ehrbase-adl-1-4-template-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The ADL 2 TEMPLATE API from EHRbase — 2 operation(s) for adl 2 template.
  name: EHRbase ADL 2 TEMPLATE API
  slug: ehrbase-adl-2-template-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Composition API from EHRbase — 1 operation(s) for admin - composition.
  name: EHRbase Admin - Composition API
  slug: ehrbase-admin-composition-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Contribution API from EHRbase — 1 operation(s) for admin - contribution.
  name: EHRbase Admin - Contribution API
  slug: ehrbase-admin-contribution-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Directory API from EHRbase — 1 operation(s) for admin - directory.
  name: EHRbase Admin - Directory API
  slug: ehrbase-admin-directory-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - EHR API from EHRbase — 1 operation(s) for admin - ehr.
  name: EHRbase Admin - EHR API
  slug: ehrbase-admin-ehr-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Heartbeat API from EHRbase — 1 operation(s) for admin - heartbeat.
  name: EHRbase Admin - Heartbeat API
  slug: ehrbase-admin-heartbeat-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Stored-Query API from EHRbase — 1 operation(s) for admin - stored-query.
  name: EHRbase Admin - Stored-Query API
  slug: ehrbase-admin-stored-query-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The Admin - Template API from EHRbase — 2 operation(s) for admin - template.
  name: EHRbase Admin - Template API
  slug: ehrbase-admin-template-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The COMPOSITION API from EHRbase — 5 operation(s) for composition.
  name: EHRbase COMPOSITION API
  slug: ehrbase-composition-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The CONTRIBUTION API from EHRbase — 2 operation(s) for contribution.
  name: EHRbase CONTRIBUTION API
  slug: ehrbase-contribution-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The DIRECTORY API from EHRbase — 2 operation(s) for directory.
  name: EHRbase DIRECTORY API
  slug: ehrbase-directory-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The EHR API from EHRbase — 2 operation(s) for ehr.
  name: EHRbase EHR API
  slug: ehrbase-ehr-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The EHR_STATUS API from EHRbase — 2 operation(s) for ehr_status.
  name: EHRbase EHR STATUS API
  slug: ehrbase-ehr-status-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The QUERY API from EHRbase — 3 operation(s) for query.
  name: EHRbase QUERY API
  slug: ehrbase-query-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: Heartbeat, Version info, Status
  name: EHRbase Status API
  slug: ehrbase-status-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The STORED_QUERY API from EHRbase — 3 operation(s) for stored_query.
  name: EHRbase STORED QUERY API
  slug: ehrbase-stored-query-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The TEMPLATE API from EHRbase — 3 operation(s) for template.
  name: EHRbase TEMPLATE API
  slug: ehrbase-template-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The VERSIONED_COMPOSITION API from EHRbase — 4 operation(s) for versioned_composition.
  name: EHRbase VERSIONED COMPOSITION API
  slug: ehrbase-versioned-composition-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The VERSIONED_EHR_STATUS API from EHRbase — 4 operation(s) for versioned_ehr_status.
  name: EHRbase VERSIONED EHR STATUS API
  slug: ehrbase-versioned-ehr-status-api
artifact_total: 27
asyncapis:
- description: ''
  name: Ehrbase Event Trigger Webhooks
  slug: ehrbase-event-trigger-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/overlays/ehrbase-openehr-rest-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ehrbase-openehr-rest-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/overlays/ehrbase-admin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ehrbase-admin-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/overlays/ehrbase-status-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ehrbase-status-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://ehrbase.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ehrbase.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ehrbase.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ehrbase.org/api/hip-ehrbase/openehr
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ehrbase.org/docs/EHRbase/Installation
- group: operate
  title: ''
  type: Support
  url: https://discourse.openehr.org/tag/ehrbase
- group: company
  title: ''
  type: Blog
  url: https://www.ehrbase.org/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ehrbase
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ehrbase/ehrbase
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ehrbase.org/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://github.com/ehrbase/ehrbase/blob/develop/LICENSE
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/changelog/ehrbase-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ehrbase-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/lifecycle/ehrbase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ehrbase-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/lifecycle/ehrbase-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ehrbase-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/authentication/ehrbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ehrbase-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/conventions/ehrbase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ehrbase-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/conventions/ehrbase-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ehrbase-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/errors/ehrbase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ehrbase-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/data-model/ehrbase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ehrbase-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/conformance/ehrbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ehrbase-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/packages/ehrbase-packages.yml
  title: ''
  type: Packages
  url: packages/ehrbase-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/packages/ehrbase-packages.yml
  title: ''
  type: SDKs
  url: packages/ehrbase-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/cli/ehrbase-cli.yml
  title: ''
  type: CLI
  url: cli/ehrbase-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/sandbox/ehrbase-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ehrbase-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/plans/ehrbase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ehrbase-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/rate-limits/ehrbase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ehrbase-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/llms/ehrbase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ehrbase-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/well-known/ehrbase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ehrbase-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/mcp/ehrbase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ehrbase-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/mcp/ehrbase-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ehrbase-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/asyncapi/ehrbase-event-trigger-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ehrbase-event-trigger-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/security/ehrbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ehrbase-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/security/ehrbase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ehrbase-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ehrbase/refs/heads/main/security/ehrbase-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ehrbase-vulnerability-disclosure.yml
created: '2026-09-02'
description: EHRbase is an open source openEHR Clinical Data Repository (CDR) - a standards-based backend for storing, versioning and querying structured clinical data. It implements the official openEHR REST API (ITS-REST 1.0.2) against openEHR Reference Model 1.1.0, is queried with the Archetype Query Language (AQL), and adds Simplified Data Template projections (flat and structured JSON web templates) that make deeply nested openEHR compositions practical to write against. It is Apache-2.0 software each organization self-hosts - no vendor API host, no signup, no metering - maintained by vitagroup AG with the openEHR community, with a commercial distribution (HIP EHRbase) adding multi-tenancy, IHE ATNA audit logging, AQL event triggers, Saga-pattern transaction compensation and SLAs. A public credential-free sandbox at sandkiste.ehrbase.org serves its live OpenAPI 3.1.0 contract of 63 operations.
image: https://raw.githubusercontent.com/ehrbase/ehrbase/develop/ehrbase.png
layout: provider
mcp_servers:
- description: ''
  name: EHRbase MCP Server
  slug: ehrbase-mcp-server
modified: '2026-09-02'
name: EHRbase
nav: Providers
network: true
overview: 'EHRbase publishes 20 APIs on the [APIs.io](https://apis.io/) network, including ADL 1.4 TEMPLATE API, ADL 2 TEMPLATE API, Admin - Composition API, and 17 more. Tagged areas include Company, Healthcare, Health IT, Electronic Health Records, and Clinical Data.


  The EHRbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EHRbase''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 31 more developer resources.'
plans:
- name: Ehrbase Plans Pricing
  plan_count: 2
  slug: ehrbase-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Ehrbase Rate Limits
  slug: ehrbase-rate-limits
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 44.7
  previous_composite: 51.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Ehrbase Authentication
  slug: ehrbase-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ehrbase Domain Security
  slug: ehrbase-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Ehrbase Vulnerability Disclosure
  slug: ehrbase-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: ehrbase
tags:
- Company
- Healthcare
- Health IT
- Electronic Health Records
- Clinical Data
- openEHR
- Interoperability
- Open-Source
- Database
- Standards
website: https://ehrbase.org/
---
