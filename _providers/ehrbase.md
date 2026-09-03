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
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The standard openEHR ITS-REST 1.0.2 surface - 31 paths and 45 operations covering EHR, EHR_STATUS, COMPOSITION, VERSIONED_COMPOSITION, CONTRIBUTION, DIRECTORY, operational templates (ADL 1.4 and ADL 2
  name: EHRbase openEHR REST API
  slug: openehr-rest-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: The opt-in administrative surface - 8 paths and 11 operations for physical deletion of EHRs, compositions, directories and stored queries, and for replacing or removing operational templates. Disabled
  name: EHRbase Admin API
  slug: admin-api
- baseURL: https://sandkiste.ehrbase.org/ehrbase
  baseurl_source: declared
  description: A version heartbeat at /rest/status reporting the running EHRbase, openEHR SDK, Archie, JVM, OS and PostgreSQL versions, plus the Spring Boot Actuator surface at /management providing health, liveness
  name: EHRbase Status and Metrics API
  slug: status-api
artifact_total: 10
asyncapis:
- description: ''
  name: Ehrbase Event Trigger Webhooks
  slug: ehrbase-event-trigger-webhooks
common:
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
  title: ''
  type: ChangeLog
  url: changelog/ehrbase-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ehrbase-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ehrbase-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ehrbase-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ehrbase-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ehrbase-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ehrbase-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ehrbase-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ehrbase-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ehrbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ehrbase-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ehrbase-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ehrbase-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ehrbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ehrbase-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ehrbase-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ehrbase-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ehrbase-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/ehrbase-tool-crosswalk.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ehrbase-event-trigger-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ehrbase-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ehrbase-vulnerability-disclosure.yml
- group: auth
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
overview: 'EHRbase publishes 3 APIs on the [APIs.io](https://apis.io/) network: openEHR REST API, Admin API, and Status and Metrics API. Tagged areas include Company, Healthcare, Health IT, Electronic Health Records, and Clinical Data.


  The EHRbase catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EHRbase''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 28 more developer resources.'
plans:
- name: Ehrbase Plans Pricing
  plan_count: 2
  slug: ehrbase-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ehrbase Rate Limits
  slug: ehrbase-rate-limits
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 46.1
    developer_ergonomics: 80.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 51.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 33.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Open Source
- Databases
- Standards
website: https://ehrbase.org/
---
