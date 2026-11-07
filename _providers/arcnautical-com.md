---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Arcnautical Com Agentic Access
  operation_count: 64
  slug: arcnautical-com-agentic-access
  summary_line: 64 operations · 27 acting
api_count: 2
apis:
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Usage, quotas and the access log for the authenticated key.
  name: ArcNautical Account API
  slug: arcnautical-com-account-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Commodity, origin and discharge screening against sanctions programmes and export controls.
  name: ArcNautical Cargo screening API
  slug: arcnautical-com-cargo-screening-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Standing route-risk subscriptions that deliver an event when a corridor score changes.
  name: ArcNautical Corridor monitors API
  slug: arcnautical-com-corridor-monitors-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: 'For Indian crewing agencies (RPSL holders): may Indian seafarers be placed on this ship under DGS Order 08 and DGMA Order 22 of 2026? A dated, hash-verifiable record per check, a crew list read again '
  name: ArcNautical Crew placement API
  slug: arcnautical-com-crew-placement-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: One file for a whole resource — screenings, cargo screenings, access log — instead of a paging loop.
  name: ArcNautical Exports API
  slug: arcnautical-com-exports-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Named sets of hulls with an exposure roll-up and a change feed, for asking what moved since a cursor instead of re-screening the whole book.
  name: ArcNautical Fleets API
  slug: arcnautical-com-fleets-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Unauthenticated UN/LOCODE resolution. Routes are addressed by LOCODE, so this is how a caller turns a port name into one. Every LOCODE validation error points here.
  name: ArcNautical Port lookup API
  slug: arcnautical-com-port-lookup-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Unauthenticated hull screening. IP rate-limited, cached, and not retained against a customer. Requires no key and no account — this is the endpoint the documentation leads with.
  name: ArcNautical Public vessel check API
  slug: arcnautical-com-public-vessel-check-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: A standing subscription per hull. We re-screen on our schedule and deliver an event only when the verdict moves, so a book need not be re-screened to stay current.
  name: ArcNautical Vessel monitors API
  slug: arcnautical-com-vessel-monitors-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: 'The authenticated screening record for one hull, or a batch of up to 50: every sanctions match with its source list and confidence class, ownership opacity, the graded vetting factors, and per-source '
  name: ArcNautical Vessel screening API
  slug: arcnautical-com-vessel-screening-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: Synchronous and batch route risk scoring by UN/LOCODE, retained for audit.
  name: ArcNautical Voyage assessments API
  slug: arcnautical-com-voyage-assessments-api
- baseURL: https://arcnautical.com
  baseurl_source: declared
  description: HMAC-SHA256 signed delivery of every event type, with delivery history and redelivery.
  name: ArcNautical Webhooks API
  slug: arcnautical-com-webhooks-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/arcnautical-com/agentic-access/arcnautical-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arcnautical-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/rules/arcnautical-com-rules.yml
  title: ''
  type: Spectral
  url: rules/arcnautical-com-rules.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/json-ld/arcnautical-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arcnautical-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/arcnautical-com/vocabulary/arcnautical-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arcnautical-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arcnautical-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/data-model/arcnautical-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arcnautical-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/arcnautical-com/changelog/arcnautical-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/arcnautical-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/conventions/arcnautical-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/arcnautical-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/conventions/arcnautical-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arcnautical-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://arcnautical.com/trust
- group: operate
  href: https://artifacts.apis.io/arcnautical-com/lifecycle/arcnautical-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/arcnautical-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/lifecycle/arcnautical-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arcnautical-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/errors/arcnautical-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arcnautical-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arcnautical-com/conformance/arcnautical-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arcnautical-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arcnautical-com/llms/arcnautical-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcnautical-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arcnautical-com/mcp/arcnautical-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arcnautical-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-ws-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-webservices-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-webservices-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-devportal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-devportal-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-apidocs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-apidocs-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-api-security.txt
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-api-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arcnautical-com-api-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/arcnautical-com/well-known/arcnautical-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcnautical-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcnautical-com/hosts/arcnautical-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcnautical-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcnautical-com/vendors/arcnautical-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcnautical-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/arcnautical-com/packages/arcnautical-com-packages.yml
  title: ''
  type: SDKs
  url: packages/arcnautical-com-packages.yml
- group: build
  href: https://artifacts.apis.io/arcnautical-com/packages/arcnautical-com-packages.yml
  title: ''
  type: Packages
  url: packages/arcnautical-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://arcnautical.com/security
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/authentication/arcnautical-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arcnautical-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/security/arcnautical-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arcnautical-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/security/arcnautical-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arcnautical-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arcnautical-com/security/arcnautical-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcnautical-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcnautical.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arcnautical.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://arcnautical.com/developers/reference/
- group: docs
  title: ''
  type: APIReference
  url: https://arcnautical.com/api/v1/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://arcnautical.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcnautical.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcnautical.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arcnautical.com
created: '2026-11-01'
description: ArcNautical provides vessel sanctions and ownership screening APIs that allow users to check any vessel against OFAC, EU, UN sanctions and ownership chains. The service offers free, no‑key endpoint access for basic checks and detailed risk scoring for voyages, supporting compliance, insurance and financing decisions. It includes a public API with OpenAPI spec, pricing information, blog updates, and security documentation.
image: https://arcnautical.com/og-image.png
json_schemas:
- name: CreateScreeningRequest
  property_count: 4
  slug: arcnautical-com-create-screening-request
- name: CrewCheck
  property_count: 20
  slug: arcnautical-com-crew-check
- name: PublicVesselCheck
  property_count: 18
  slug: arcnautical-com-public-vessel-check
- name: Screening
  property_count: 22
  slug: arcnautical-com-screening
- name: UsageSummary
  property_count: 6
  slug: arcnautical-com-usage-summary
- name: VoyageAssessment
  property_count: 20
  slug: arcnautical-com-voyage-assessment
jsonld:
- class_count: 115
  name: Arcnautical Com Context
  property_count: 336
  slug: arcnautical-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.arcnautical.com.
  name: ArcNautical MCP Server
  slug: arcnautical-com-mcp-yml
modified: '2026-11-01'
name: ArcNautical
nav: Providers
network: true
overview: 'ArcNautical publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Cargo screening API, Corridor monitors API, and 9 more. Tagged areas include Company, Maritime, Compliance, Data, and Screening.


  The ArcNautical catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ArcNautical''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, and 36 more developer resources.'
plans:
- name: Arcnautical Com Plans Pricing
  plan_count: 2
  slug: arcnautical-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Arcnautical Com Rate Limits
  slug: arcnautical-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: ArcNautical API Rules
  rule_count: 72
  severity_counts:
    error: 53
    hint: 0
    info: 4
    warn: 15
  slug: arcnautical-com-rules
scopes:
- name: Arcnautical Com Scopes
  scope_count: 8
  slug: arcnautical-com-scopes
  summary_line: 8 scopes
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 78.8
    catalog_earned_first_party: 16.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 65.4
    developer_ergonomics: 35.1
    discoverability: 65.0
    operational_transparency: 57.9
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcnautical Com Authentication
  slug: arcnautical-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Arcnautical Com Domain Security
  slug: arcnautical-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arcnautical Com Vulnerability Disclosure
  slug: arcnautical-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arcnautical Com Trust Center
  slug: arcnautical-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 5
skills:
- name: check-vessel-public
  slug: arcnautical-com-check-vessel-public
- name: arcnautical-com-create-and-manage-fleet
  slug: arcnautical-com-create-and-manage-fleet
- name: arcnautical-com-create-and-retrieve-vessel-monitor
  slug: arcnautical-com-create-and-retrieve-vessel-monitor
- name: arcnautical-com-create-get-list-cargo-screening
  slug: arcnautical-com-create-get-list-cargo-screening
- name: create-vessel-monitor
  slug: arcnautical-com-create-vessel-monitor
slug: arcnautical-com
tags:
- Company
- Maritime
- Compliance
- Data
- Screening
website: https://arcnautical.com/
---
