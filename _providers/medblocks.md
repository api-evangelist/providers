---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: Verify a training certificate issued by Medblocks.
  name: Medblocks Certificates API
  slug: medblocks-certificates-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Connections API from Medblocks — 2 operation(s) for connections.
  name: Medblocks Connections API
  slug: medblocks-connections-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Events API from Medblocks — 1 operation(s) for events.
  name: Medblocks Events API
  slug: medblocks-events-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: Machine-readable indexes of site content.
  name: Medblocks Feeds API
  slug: medblocks-feeds-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Health API from Medblocks — 1 operation(s) for health.
  name: Medblocks Health API
  slug: medblocks-health-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Launch Contexts API from Medblocks — 1 operation(s) for launch contexts.
  name: Medblocks Launch Contexts API
  slug: medblocks-launch-contexts-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Patient Sessions API from Medblocks — 2 operation(s) for patient sessions.
  name: Medblocks Patient Sessions API
  slug: medblocks-patient-sessions-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Patients API from Medblocks — 5 operation(s) for patients.
  name: Medblocks Patients API
  slug: medblocks-patients-api
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: The Webhooks API from Medblocks — 4 operation(s) for webhooks.
  name: Medblocks Webhooks API
  slug: medblocks-webhooks-api
artifact_total: 20
asyncapis:
- description: ''
  name: Medblocks Webhooks
  slug: medblocks-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://medblocks.com/rss.xml
- group: other
  href: https://artifacts.apis.io/medblocks/capabilities/medblocks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/medblocks-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/medblocks/overlays/medblocks-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/medblocks-platform-overlay.yaml
- group: other
  href: https://artifacts.apis.io/medblocks/overlays/medblocks-public-site-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/medblocks-public-site-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/medblocks/security/medblocks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medblocks-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/medblocks/authentication/medblocks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/medblocks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://medblocks.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://medblocks.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://medblocks.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://medblocks.com/docs/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://medblocks.com/docs/quickstarts
- group: operate
  title: ''
  type: Support
  url: https://medblocks.com/contact
- group: operate
  title: ''
  type: Community
  url: https://medblocks.com/community
- group: company
  title: ''
  type: Blog
  url: https://medblocks.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medblocks
- group: commercial
  title: ''
  type: Pricing
  url: https://medblocks.com/docs/billing
- group: start
  title: ''
  type: SignUp
  url: https://app.medblocks.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medblocks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medblocks.com/privacy-policy
- group: build
  href: https://artifacts.apis.io/medblocks/packages/medblocks-packages.yml
  title: ''
  type: Packages
  url: packages/medblocks-packages.yml
- group: build
  href: https://artifacts.apis.io/medblocks/packages/medblocks-packages.yml
  title: ''
  type: SDKs
  url: packages/medblocks-packages.yml
- group: agent
  href: https://artifacts.apis.io/medblocks/well-known/medblocks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/medblocks-well-known.yml
- group: other
  href: https://artifacts.apis.io/medblocks/well-known/medblocks-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/medblocks-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/medblocks/mcp/medblocks-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/medblocks-mcp.yml
- group: build
  href: https://artifacts.apis.io/medblocks/mcp/medblocks-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/medblocks-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/medblocks/llms/medblocks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/medblocks-llms.txt
- group: agent
  href: https://artifacts.apis.io/medblocks/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/medblocks/conformance/medblocks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/medblocks-conformance.yml
- group: auth
  href: https://artifacts.apis.io/medblocks/conformance/medblocks-conformance.yml
  title: ''
  type: Compliance
  url: conformance/medblocks-conformance.yml
- group: design
  href: https://artifacts.apis.io/medblocks/errors/medblocks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/medblocks-problem-types.yml
- group: design
  href: https://artifacts.apis.io/medblocks/lifecycle/medblocks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/medblocks-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/medblocks/scopes/medblocks-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/medblocks-scopes.yml
- group: design
  href: https://artifacts.apis.io/medblocks/conventions/medblocks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/medblocks-conventions.yml
- group: operate
  href: https://artifacts.apis.io/medblocks/changelog/medblocks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/medblocks-changelog.yml
- group: start
  href: https://artifacts.apis.io/medblocks/sandbox/medblocks-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/medblocks-sandbox.yml
- group: design
  href: https://artifacts.apis.io/medblocks/components/medblocks-components.yml
  title: ''
  type: Components
  url: components/medblocks-components.yml
- group: design
  href: https://artifacts.apis.io/medblocks/data-model/medblocks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/medblocks-data-model.yml
- group: design
  href: https://artifacts.apis.io/medblocks/asyncapi/medblocks-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/medblocks-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/medblocks/plans/medblocks-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/medblocks-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/medblocks/rate-limits/medblocks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/medblocks-rate-limits.yml
created: '2026-09-02'
description: Medblocks is a health-data integration platform that gives applications a single API for a patient's longitudinal health record. Its Medblocks Platform API brokers patient-mediated connections to EHRs, payers and health information networks (Epic, Cerner/Oracle Health, athenahealth, eClinicalWorks, Meditech, CMS Blue Button, UnitedHealthcare and wearables), normalizes what comes back into FHIR R4, and delivers it through cursor-paginated record reads, signed webhooks, and export destinations such as a customer FHIR server or S3. It also ships clinician-workflow surfaces (SMART App Launch, CDS Hooks), backend/bulk services, a hosted Model Context Protocol server for AI assistants, a TypeScript SDK, and the open-source medblocks-ui web-component library and openFHIR openEHR-to-FHIR mapping engine. Founded by Sidharth Ramesh, Medblocks also runs FHIR and openEHR training bootcamps.
finops:
- has_sources: true
  method: derived
  name: Medblocks Finops
  primary_unit: workspace
  service_category: ''
  slug: medblocks-finops
  template: false
image: https://medblocks.com/_astro/f266b99b-2c21-44ba-b819-c3911c15a61b.CZlakJ61_1CWv2n.jpeg
layout: provider
mcp_servers:
- description: 'Hosted, remote MCP server that gives an AI assistant access to a Medblocks Platform workspace: orient in the workspace, search health systems, start a patient-portal connection session, read the FHIR '
  name: Medblocks MCP Server
  slug: medblocks-platform
modified: '2026-10-06'
name: Medblocks
nav: Providers
network: true
overview: 'Medblocks publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Certificates API, Connections API, Events API, and 6 more. Tagged areas include Health, Healthcare, FHIR, openEHR, and Interoperability.


  The Medblocks catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Medblocks'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Medblocks Plans Pricing
  plan_count: 2
  slug: medblocks-plans-pricing
- name: Medblocks Price Estimates
  plan_count: 0
  slug: medblocks-price-estimates
random_paper: 12
rate_limits:
- limit_count: 1
  name: Medblocks Rate Limits
  slug: medblocks-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Medblocks API Rules
  rule_count: 60
  severity_counts:
    error: 50
    hint: 0
    info: 4
    warn: 6
  slug: medblocks-rules
scopes:
- name: Medblocks Scopes
  scope_count: 10
  slug: medblocks-scopes
  summary_line: 10 scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 60.5
    catalog_earned_first_party: 16.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 68.4
    contract_governance: 31.8
    contract_quality: 61.1
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 64.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 22.2
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/medblocks/medblocks-2026-10-11T110907.png
security:
- kind: authentication
  name: Medblocks Authentication
  slug: medblocks-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Medblocks Domain Security
  slug: medblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: medblocks
  slug: medblocks-skill
slug: medblocks
tags:
- Health
- Healthcare
- FHIR
- openEHR
- Interoperability
- Electronic Health Records
- Patient Access
- Health Data
- SMART on FHIR
- Webhook
- MCP
- Company
website: https://medblocks.com/
---
