---
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://app.medblocks.com
  baseurl_source: declared
  description: Server-to-server developer API for the Medblocks Platform. Create patients, start hosted PatientSessions that authorize a patient against one or more EHRs, inspect the resulting connections, read unif
  name: Medblocks Platform API
  slug: medblocks-platform-api
- baseURL: https://medblocks.com
  baseurl_source: declared
  description: 'A narrow, unauthenticated, read-only API that medblocks.com publishes for third-party and automated use: training-certificate verification plus the machine-readable blog RSS feed and sitemap index. De'
  name: Medblocks Public Site API
  slug: medblocks-public-site-api
artifact_total: 9
asyncapis:
- description: ''
  name: Medblocks Webhooks
  slug: medblocks-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medblocks-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/medblocks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/medblocks-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medblocks-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/medblocks-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/medblocks-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/medblocks-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medblocks-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/medblocks-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/medblocks-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/medblocks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/medblocks-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/medblocks-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/medblocks-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/medblocks-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/medblocks-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/medblocks-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/medblocks-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/medblocks-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/medblocks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medblocks-rate-limits.yml
created: '2026-09-02'
description: Medblocks is a health-data integration platform that gives applications a single API for a patient's longitudinal health record. Its Medblocks Platform API brokers patient-mediated connections to EHRs, payers and health information networks (Epic, Cerner/Oracle Health, athenahealth, eClinicalWorks, Meditech, CMS Blue Button, UnitedHealthcare and wearables), normalizes what comes back into FHIR R4, and delivers it through cursor-paginated record reads, signed webhooks, and export destinations such as a customer FHIR server or S3. It also ships clinician-workflow surfaces (SMART App Launch, CDS Hooks), backend/bulk services, a hosted Model Context Protocol server for AI assistants, a TypeScript SDK, and the open-source medblocks-ui web-component library and openFHIR openEHR-to-FHIR mapping engine. Founded by Sidharth Ramesh, Medblocks also runs FHIR and openEHR training bootcamps.
image: https://medblocks.com/_astro/f266b99b-2c21-44ba-b819-c3911c15a61b.CZlakJ61_1CWv2n.jpeg
layout: provider
mcp_servers:
- description: 'Hosted, remote MCP server that gives an AI assistant access to a Medblocks Platform workspace: orient in the workspace, search health systems, start a patient-portal connection session, read the FHIR '
  name: Medblocks MCP Server
  slug: medblocks-mcp-server
modified: '2026-09-02'
name: Medblocks
nav: Providers
network: true
overview: 'Medblocks publishes 2 APIs on the [APIs.io](https://apis.io/) network: Platform API and Public Site API. Tagged areas include Health, Healthcare, FHIR, openEHR, and Interoperability.


  The Medblocks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Medblocks'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Medblocks Plans Pricing
  plan_count: 2
  slug: medblocks-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Medblocks Rate Limits
  slug: medblocks-rate-limits
scopes:
- name: Medblocks Scopes
  scope_count: 0
  slug: medblocks-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 63.5
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 67.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Medblocks Authentication
  slug: medblocks-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Medblocks Domain Security
  slug: medblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Webhooks
- Model Context Protocol
- Company
website: https://medblocks.com/
---
