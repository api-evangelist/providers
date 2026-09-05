---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-04'
api_count: 9
apis:
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST EHR API as implemented and published by Cadasto: create and read EHRs, read and update EHR_STATUS, commit/retrieve/update/logically-delete versioned COMPOSITIONs, manage the DIREC'
  name: Cadasto EHR API
  slug: cadasto-ehr-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST Query API: execute ad-hoc Archetype Query Language (AQL) queries with bound parameters, and execute stored queries by qualified name and version, over GET or POST. 6 operations. A'
  name: Cadasto Query API (AQL)
  slug: cadasto-query-api-aql
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST Definition API: upload, list and retrieve ADL 1.4 Operational Templates (OPT) and ADL 2 templates, fetch a generated example composition for a template, and store, list and versio'
  name: Cadasto Definition API
  slug: cadasto-definition-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST Demographic API: create, read, update and delete PERSON, ORGANISATION, ROLE, AGENT and GROUP parties, read versioned parties and their revision history, create demographic CONTRIB'
  name: Cadasto Demographic API
  slug: cadasto-demographic-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST Admin API: privileged, physically destructive operations — delete a single EHR, delete all EHRs, merge two EHRs, delete a composition outright, and delete a template. 5 operations'
  name: Cadasto Admin API
  slug: cadasto-admin-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: 'The openEHR ITS-REST System API: a single OPTIONS operation returning server capabilities, the openEHR specification versions the server implements, and its conformance profile. This is the machine-re'
  name: Cadasto System API
  slug: cadasto-system-api
- baseURL: https://api.customer.cadasto.io
  baseurl_source: declared
  description: Cadasto's own extension surface on top of openEHR REST, described by the vendor as "Cadasto-specific... This API only works within Cadasto". 27 operations across Datamap definitions and Datamap data (
  name: Cadasto Additional API
  slug: cadasto-additional-api
- baseURL: https://auth.customer.cadasto.io
  baseurl_source: declared
  description: A deliberately minimal OpenAPI document that acts as a discovery pointer to the SMART on openEHR specification for app launch, service discovery and third-party app authorization against a Cadasto ten
  name: Cadasto SMART on openEHR
  slug: cadasto-smart-on-openehr
- description: 'Cadasto''s live, hosted, anonymous Model Context Protocol server for openEHR modelling work: 12 tools (CKM archetype and template search/get, openEHR terminology resolution, BMM type specification sear'
  name: openEHR Assistant MCP Server
  slug: openehr-assistant-mcp-server
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.cadasto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cadasto.io/docs/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cadasto.io/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cadasto.io/ehr-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cadasto.io/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/cadasto-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cadasto-scopes.yml
- group: operate
  title: ''
  type: FAQ
  url: https://docs.cadasto.io/docs/faq
- group: operate
  title: ''
  type: Support
  url: https://www.cadasto.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.cadasto.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cadasto.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cadasto
- group: start
  title: ''
  type: SignUp
  url: https://www.cadasto.com/get-started/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cadasto.com/privacy-and-cookie-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cadasto/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cadasto-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cadasto-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cadasto-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/cadasto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cadasto-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cadasto-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cadasto-security.txt
- group: auth
  title: ''
  type: Security
  url: security/cadasto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cadasto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cadasto-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/cadasto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cadasto-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cadasto-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cadasto-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cadasto-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cadasto-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cadasto-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cadasto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cadasto-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cadasto-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cadasto-changelog.yml
created: '2026-09-02'
description: 'Cadasto B.V. is a Dutch health-IT company (Alkmaar, Netherlands) that builds a vendor-neutral Clinical Data Repository on the openEHR standard. The Cadasto CDR stores structured care data as openEHR compositions and exposes the openEHR ITS-REST 1.0.3 API surface — EHR, Query (AQL), Definition, Demographic, Admin and System — plus a Cadasto-specific Additional API for Datamap (a simplified JSON projection of openEHR paths), episodes of care and terminology helpers, a bidirectional FHIR R3 facade, and SMART-on-openEHR app launch. Access is OAuth 2.0 client-credentials per tenant. Cadasto also publishes an unusually strong agent surface for its size: a live anonymous MCP server for openEHR modelling knowledge, eight packaged Agent Skills, a Claude Code plugin marketplace, an llms.txt, and a public openEHR conformance statement naming every specification version it does and does not implement.'
image: https://www.cadasto.com/wp-content/uploads/2025/11/cropped-cadasto-favicon-192x192.png
layout: provider
mcp_servers:
- description: Cadasto B.V. publishes two MCP servers. The openEHR ASSISTANT server is live, hosted and anonymous — it serves the openEHR knowledge surface (CKM archetypes and templates, openEHR terminology, BMM typ
  name: Cadasto MCP Server
  slug: cadasto-mcp-server
modified: '2026-09-02'
name: Cadasto
nav: Providers
network: true
overview: 'Cadasto publishes 8 APIs on the [APIs.io](https://apis.io/) network, including EHR API, Query API (AQL), Definition API, and 5 more. Tagged areas include Healthcare, Health IT, openEHR, Electronic Health Records, and Clinical Data Repository.


  Cadasto''s developer surface includes documentation, API reference, getting-started guide, authentication, FAQ, support, engineering blog, and 30 more developer resources.'
plans:
- name: Cadasto Plans Pricing
  plan_count: 0
  slug: cadasto-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Cadasto Rate Limits
  slug: cadasto-rate-limits
scopes:
- name: Cadasto Scopes
  scope_count: 0
  slug: cadasto-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 50.6
    developer_ergonomics: 78.6
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 56.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 68.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: authentication
  name: Cadasto Authentication
  slug: cadasto-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Cadasto Domain Security
  slug: cadasto-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cadasto Vulnerability Disclosure
  slug: cadasto-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cadasto Trust Center
  slug: cadasto-trust-center
  summary_line: ISO 9001, ISO/IEC 27001, NEN 7510
slug: cadasto
tags:
- Healthcare
- Health IT
- openEHR
- Electronic Health Records
- Clinical Data Repository
- Interoperability
- FHIR
- Vendor Neutral Archive
- Clinical Data
- AQL
- MCP
- Agent Skills
- Netherlands
website: https://www.cadasto.com/
---
