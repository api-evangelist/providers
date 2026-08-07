---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 58.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Modernizing Medicine Agentic Access
  operation_count: 125
  slug: modernizing-medicine-agentic-access
  summary_line: 125 operations · 20 acting
api_count: 2
apis:
- description: ModMed's proprietary FHIR R4-style API over the EMA EHR and ModMed Practice Management. 58 operations under /fhir/v2 across Patient, Practitioner, Organization, Location, Encounter, Appointment, Slot,
  name: EMA Proprietary API
  slug: ema-proprietary-api
- description: ModMed's ONC-certified HL7 FHIR R4 API for EMA, ModMed PM, ModMed GI and gGastro. 64 read and search operations across 31 US Core resource types plus Bulk FHIR $export at Patient and Group level, auth
  name: ModMed Certified FHIR API
  slug: modmed-certified-fhir-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.modmed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.api.modmed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://portal.api.modmed.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://portal.api.modmed.com/reference/getting-started-2
- group: start
  title: ''
  type: GettingStarted
  url: https://portal.api.modmed.com/docs/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.modmed.com/synapsys/developers/
- group: operate
  title: ''
  type: Support
  url: https://www.modmed.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.modmed.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modmed.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modmed.com/privacy-policy/
- group: other
  title: ''
  type: Marketplace
  url: https://modmed.my.site.com/synapsysmarketplace/s/
- group: auth
  title: ''
  type: Authentication
  url: authentication/modernizing-medicine-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/modernizing-medicine-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modernizing-medicine-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modernizing-medicine-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modernizing-medicine-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modernizing-medicine-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://portal.api.modmed.com/reference/authentication-1
- group: design
  title: ''
  type: Conformance
  url: conformance/modernizing-medicine-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.modmed.com/onc-certification/
- group: design
  title: ''
  type: DataModel
  url: data-model/modernizing-medicine-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/modernizing-medicine-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/modernizing-medicine-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/modernizing-medicine-security.txt
- group: other
  title: ''
  type: APICatalog
  url: https://mm-fhir-endpoint-display.prod.fhir.ema-api.com/
- group: auth
  title: ''
  type: Security
  url: https://www.modmed.com/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/modernizing-medicine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modernizing-medicine-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/modernizing-medicine-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modernizing-medicine-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/modernizing-medicine-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modernizing-medicine-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/modernizing-medicine-ema-proprietary-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/modernizing-medicine-certified-fhir-api-overlay.yaml
created: '2026-08-04'
description: 'ModMed (Modernizing Medicine, Inc., Boca Raton FL) builds specialty-specific cloud healthcare software — the EMA electronic health record, ModMed Practice Management, gGastro for gastroenterology, analytics, revenue cycle management and telehealth — for allergy, dermatology, ENT, gastroenterology, OBGYN, ophthalmology, orthopedics, pain management, plastic surgery, podiatry and urology practices. It publishes two public APIs from one developer portal at portal.api.modmed.com: the EMA Proprietary API, a FHIR R4-style read/write interface under /fhir/v2 covering patients, appointments, slots, coverage, charges, documents and clinical data for synapSYS Marketplace vendors; and the ModMed Certified FHIR API, an ONC-certified HL7 FHIR R4 / US Core read-and-search interface with SMART on FHIR app launch and Bulk FHIR NDJSON export across EMA, ModMed PM, ModMed GI and gGastro. Customer FHIR service base URLs are published publicly as required by the 21st Century Cures Act.'
image: https://www.modmed.com/wp-content/uploads/2024/12/cropped-mm-favicon_512-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: modernizing-medicine-mcp.yml
  slug: modernizing-medicine-mcpyml
modified: '2026-08-04'
name: ModMed
nav: Providers
network: true
overview: 'ModMed publishes 2 APIs on the [APIs.io](https://apis.io/) network: EMA Proprietary API and Certified FHIR API. Tagged areas include Company, Healthcare, Electronic Health Records, Practice Management, and FHIR.


  ModMed''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 28 more developer resources.'
random_paper: 31
rate_limits:
- limit_count: 2
  name: Modernizing Medicine Rate Limits
  slug: modernizing-medicine-rate-limits
scopes:
- name: Modernizing Medicine Scopes
  scope_count: 76
  slug: modernizing-medicine-scopes
  summary_line: 76 scopes · authorizationCode
score:
  band: strong
  composite: 60.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 60.7
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 60.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 100.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Modernizing Medicine Authentication
  slug: modernizing-medicine-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Modernizing Medicine Domain Security
  slug: modernizing-medicine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Modernizing Medicine Vulnerability Disclosure
  slug: modernizing-medicine-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: modernizing-medicine
tags:
- Company
- Healthcare
- Electronic Health Records
- Practice Management
- FHIR
- Health IT
- Interoperability
- Medical Billing
- SMART on FHIR
- Telehealth
website: https://www.modmed.com/
---
