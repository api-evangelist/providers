---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: 'Cadasto''s live, hosted, anonymous Model Context Protocol server for openEHR modelling work: 12 tools (CKM archetype and template search/get, openEHR terminology resolution, BMM type specification sear'
  name: openEHR Assistant MCP Server
  slug: openehr-assistant-mcp-server
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [AOM and ADL 1.4](https://specifications.openehr.org/releases/AM/latest) Operational Templates (OPTs). These templates can be created using [modelling tools](https://www.openehr.org/down
  name: Cadasto ADL1.4 API
  slug: cadasto-adl1-4-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [AOM2](https://specifications.openehr.org/releases/AM/latest/AOM2.html#_templates) templates. See also [ADL2 Template specifications](https://specifications.openehr.org/releases/AM/lates
  name: Cadasto ADL2 API
  slug: cadasto-adl2-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Admin-only actions, such as permanently deleting (destroy) episodes.
  name: Cadasto Admin API
  slug: cadasto-admin-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [AGENT](https://specifications.openehr.org/releases/RM/latest/demographic.html#_agent_class) class.
  name: Cadasto AGENT API
  slug: cadasto-agent-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [COMPOSITION](https://specifications.openehr.org/releases/RM/latest/ehr.html#_composition_class) and [VERSIONED_COMPOSITION](https://specifications.openehr.org/releases/RM/latest/ehr.htm
  name: Cadasto COMPOSITION API
  slug: cadasto-composition-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [CONTRIBUTION](https://specifications.openehr.org/releases/RM/latest/common.html#_contribution_class) class.
  name: Cadasto CONTRIBUTION API
  slug: cadasto-contribution-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of datamap definitions (XML). Defines what data is available and how it can be mapped/queried for Cadasto-specific integrations.
  name: Cadasto Datamap Definition API
  slug: cadasto-datamap-definition-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Run datamap queries and manage datamap data. Supports ad-hoc XML queries and CRUD via JSON for Cadasto.
  name: Cadasto Datamap Query API
  slug: cadasto-datamap-query-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [directory](https://specifications.openehr.org/releases/RM/latest/ehr.html#_directory) [FOLDER](https://specifications.openehr.org/releases/RM/latest/common.html#_folder_class) resou
  name: Cadasto DIRECTORY API
  slug: cadasto-directory-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Admin management of [EHRs](https://specifications.openehr.org/releases/RM/latest/ehr.html#_ehr_class).
  name: Cadasto EHR API
  slug: cadasto-ehr-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [EHR_STATUS](https://specifications.openehr.org/releases/RM/latest/ehr.html#_ehr_status_class) and [VERSIONED_EHR_STATUS](https://specifications.openehr.org/releases/RM/latest/ehr.html#_
  name: Cadasto EHR STATUS API
  slug: cadasto-ehr-status-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: CRUD on episodes within an EHR and status changes (activate/deactivate). Episodes group medical data around a clinical problem or episode of care across time and encounters.
  name: Cadasto Episode API
  slug: cadasto-episode-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [GROUP](https://specifications.openehr.org/releases/RM/latest/demographic.html#_group_class) class.
  name: Cadasto GROUP API
  slug: cadasto-group-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Health checks for monitoring and orchestration. Used for startup, liveness, and readiness probes.
  name: Cadasto Health API
  slug: cadasto-health-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [ITEM_TAG](https://specifications.openehr.org/releases/RM/latest/common.html#_item_tag_class) resources attached to demographic versioned objects (PERSON, AGENT, GROUP, ORGANISATION, ROL
  name: Cadasto ITEM TAG API
  slug: cadasto-item-tag-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: The Options API from Cadasto — 1 operation(s) for options.
  name: Cadasto Options API
  slug: cadasto-options-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [ORGANISATION](https://specifications.openehr.org/releases/RM/latest/demographic.html#_organisation_class) class.
  name: Cadasto ORGANISATION API
  slug: cadasto-organisation-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [PERSON](https://specifications.openehr.org/releases/RM/latest/demographic.html#_person_class) class.
  name: Cadasto PERSON API
  slug: cadasto-person-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of [stored (registered) queries](https://specifications.openehr.org/releases/SM/latest/openehr_platform.html#_registered_queries) in the system. Actions upon resources of this group are als
  name: Cadasto Query API
  slug: cadasto-query-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [ROLE](https://specifications.openehr.org/releases/RM/latest/demographic.html#_role_class) class.
  name: Cadasto ROLE API
  slug: cadasto-role-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Terminology helpers, such as retrieving FHIR ValueSet URLs.
  name: Cadasto Terminology API
  slug: cadasto-terminology-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: User information and caseload for the authenticated user.
  name: Cadasto User API
  slug: cadasto-user-api
- baseURL: https://{mycompany}.api.prod.cadasto.io/openehr/v1
  baseurl_source: declared
  description: Management of the [VERSIONED_PARTY](https://specifications.openehr.org/releases/RM/latest/demographic.html#_versioned_party_class) class.
  name: Cadasto VERSIONED PARTY API
  slug: cadasto-versioned-party-api
artifact_total: 43
common:
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-ehr-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-ehr-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-query-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-query-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-definition-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-definition-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-demographic-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-demographic-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-admin-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-admin-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-system-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-system-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/cadasto/overlays/cadasto-extra-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cadasto-extra-api-overlay.yaml
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
  href: https://artifacts.apis.io/cadasto/authentication/cadasto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cadasto-authentication.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/scopes/cadasto-scopes.yml
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
  href: https://artifacts.apis.io/cadasto/mcp/cadasto-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cadasto-mcp.yml
- group: build
  href: https://artifacts.apis.io/cadasto/mcp/cadasto-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cadasto-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cadasto/llms/cadasto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cadasto-llms.txt
- group: agent
  href: https://artifacts.apis.io/cadasto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/cadasto/packages/cadasto-packages.yml
  title: ''
  type: Packages
  url: packages/cadasto-packages.yml
- group: build
  href: https://artifacts.apis.io/cadasto/packages/cadasto-packages.yml
  title: ''
  type: SDKs
  url: packages/cadasto-packages.yml
- group: agent
  href: https://artifacts.apis.io/cadasto/well-known/cadasto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cadasto-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/well-known/cadasto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cadasto-security.txt
- group: auth
  href: https://artifacts.apis.io/cadasto/security/cadasto-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cadasto-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/security/cadasto-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cadasto-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/security/cadasto-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cadasto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/security/cadasto-trust-center.yml
  title: ''
  type: Compliance
  url: security/cadasto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cadasto/security/cadasto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cadasto-domain-security.yml
- group: design
  href: https://artifacts.apis.io/cadasto/conformance/cadasto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cadasto-conformance.yml
- group: design
  href: https://artifacts.apis.io/cadasto/conventions/cadasto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cadasto-conventions.yml
- group: design
  href: https://artifacts.apis.io/cadasto/errors/cadasto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cadasto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cadasto/lifecycle/cadasto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cadasto-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cadasto/data-model/cadasto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cadasto-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/cadasto/plans/cadasto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cadasto-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cadasto/rate-limits/cadasto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cadasto-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/cadasto/sandbox/cadasto-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cadasto-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/cadasto/changelog/cadasto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cadasto-changelog.yml
created: '2026-09-02'
description: 'Cadasto B.V. is a Dutch health-IT company (Alkmaar, Netherlands) that builds a vendor-neutral Clinical Data Repository on the openEHR standard. The Cadasto CDR stores structured care data as openEHR compositions and exposes the openEHR ITS-REST 1.0.3 API surface — EHR, Query (AQL), Definition, Demographic, Admin and System — plus a Cadasto-specific Additional API for Datamap (a simplified JSON projection of openEHR paths), episodes of care and terminology helpers, a bidirectional FHIR R3 facade, and SMART-on-openEHR app launch. Access is OAuth 2.0 client-credentials per tenant. Cadasto also publishes an unusually strong agent surface for its size: a live anonymous MCP server for openEHR modelling knowledge, eight packaged Agent Skills, a Claude Code plugin marketplace, an llms.txt, and a public openEHR conformance statement naming every specification version it does and does not implement.'
finops:
- has_sources: true
  method: derived
  name: Cadasto Finops
  primary_unit: ''
  service_category: ''
  slug: cadasto-finops
  template: true
image: https://www.cadasto.com/wp-content/uploads/2025/11/cropped-cadasto-favicon-192x192.png
layout: provider
mcp_servers:
- description: Cadasto B.V. publishes two MCP servers. The openEHR ASSISTANT server is live, hosted and anonymous — it serves the openEHR knowledge surface (CKM archetypes and templates, openEHR terminology, BMM typ
  name: Cadasto MCP Server
  slug: cadasto-mcp-yml
modified: '2026-09-02'
name: Cadasto
nav: Providers
network: true
overview: 'Cadasto publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including ADL1.4 API, ADL2 API, Admin API, and 21 more. Tagged areas include Healthcare, Health IT, openEHR, Electronic Health Records, and Clinical Data Repository.


  The Cadasto catalog on APIs.io includes 1 Spectral governance ruleset.


  Cadasto''s developer surface includes documentation, API reference, getting-started guide, authentication, FAQ, support, engineering blog, and 37 more developer resources.'
plans:
- name: Cadasto Plans Pricing
  plan_count: 0
  slug: cadasto-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Cadasto Rate Limits
  slug: cadasto-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Cadasto API Rules
  rule_count: 63
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 15
  slug: cadasto-rules
scopes:
- name: Cadasto Scopes
  scope_count: 2
  slug: cadasto-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 31.8
    contract_quality: 47.2
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 57.1
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/cadasto/cadasto-2026-10-11T102639.png
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
skill_count: 9
skills:
- name: aql-authoring
  slug: cadasto-aql-authoring
- name: archetype-authoring
  slug: cadasto-archetype-authoring
- name: archetype-lint
  slug: cadasto-archetype-lint
- name: cadasto-cdr-clinical-write-flow
  slug: cadasto-cdr-clinical-write-flow
- name: composition-builder
  slug: cadasto-composition-builder
- name: demographic-modeling
  slug: cadasto-demographic-modeling
- name: openehr-assistant
  slug: cadasto-openehr-assistant
- name: semantic-diff
  slug: cadasto-semantic-diff
- name: template-authoring
  slug: cadasto-template-authoring
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
