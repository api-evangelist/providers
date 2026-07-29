---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Advancedmd Agentic Access
  operation_count: 81
  slug: advancedmd-agentic-access
  summary_line: 81 operations · 19 acting
api_count: 6
apis:
- description: Read-only HL7 FHIR R4 (4.0.1) API for single-patient data access, aligned to the HL7 FHIR US Core Implementation Guide STU 6.1.0 and published for ONC (g)(10) Cures Act certification. Supports both st
  name: AdvancedMD FHIR Single API (US Core 6.1.0)
  slug: advancedmd-fhir-single-api
- description: HL7 FHIR Bulk Data Access (Flat FHIR) API for exporting a patient group's data from AdvancedMD. Documented operations cover backend-services token acquisition (POST /v1/oauth2/token with client_assert
  name: AdvancedMD FHIR Bulk API
  slug: advancedmd-fhir-bulk-api
- description: Developer-portal helper API that mints JWT client assertions for testing the FHIR Bulk Data workflow. Documented as POST /v1/fhir-jwks/token with a grant_type=client_credentials&alg=rsa body, authoriz
  name: AdvancedMD FHIR Bulk JWKS API
  slug: advancedmd-fhir-bulk-jwks-api
- description: 'Public, unauthenticated service base URL publication required of ONC-certified API suppliers. GET https://providerapi.advancedmd.com/v1/r4/endpoints returns a FHIR Bundle of Endpoint and Organization '
  name: AdvancedMD FHIR Endpoint Directory
  slug: advancedmd-fhir-endpoint-directory
- description: Non-FHIR REST API family published on the AdvancedMD FHIR portal as "Legacy Patient APIs" and titled "AdvancedMD Application Access APIs" in its own Swagger 2.0 definition (version 1.0.1, supported Ad
  name: AdvancedMD Application Access APIs (Legacy Patient APIs)
  slug: advancedmd-application-access-apis
- description: AdvancedMD's proprietary partner API family, published in both XML-RPC and REST formats, which lets developers build companion applications that replicate functionality available in the AdvancedMD use
  name: AdvancedMD Connect APIs
  slug: advancedmd-connect-apis
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/advancedmd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancedmd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advancedmd-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.advancedmd.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fhir.advancedmd.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.advancedmd.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.advancedmd.com/group-practice/developer-solutions/
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.advancedmd.com/fhir/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://fhir.advancedmd.com/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://fhir.advancedmd.com/fhir/launch-and-authorization
- group: other
  title: ''
  type: CapabilityStatement
  url: fhir/advancedmd-fhir-r4-capabilitystatement.json
- group: other
  title: ''
  type: SMARTConfiguration
  url: fhir/advancedmd-smart-configuration.json
- group: other
  title: ''
  type: OpenIDConfiguration
  url: fhir/advancedmd-openid-configuration.json
- group: operate
  title: ''
  type: FAQ
  url: https://fhir.advancedmd.com/faq-s
- group: start
  title: ''
  type: SignUp
  url: https://www.advancedmd.com/api-connection-request/
- group: start
  title: ''
  type: Login
  url: https://login.advancedmd.com/
- group: operate
  title: ''
  type: Support
  url: https://www.advancedmd.com/support/interoperability/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.advancedmd.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.advancedmd.com/software-pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.advancedmd.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.advancedmd.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdvancedMD
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fhir.advancedmd.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.advancedmd.com/privacy-notice/
- group: auth
  title: ''
  type: Security
  url: https://www.advancedmd.com/medical-office-software/security/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.advancedmd.com/support/
- group: auth
  title: ''
  type: Compliance
  url: https://www.advancedmd.com/ai-information
- group: design
  title: ''
  type: Conformance
  url: conformance/advancedmd-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/advancedmd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advancedmd-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/advancedmd-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advancedmd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advancedmd-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advancedmd-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/advancedmd-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/advancedmd-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/advancedmd-well-known.yml
- group: other
  title: ''
  type: JSONWebKeySet
  url: well-known/advancedmd-jwks.json
- group: build
  title: ''
  type: Packages
  url: packages/advancedmd-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancedmd-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/advancedmd-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/advancedmd-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: AdvancedMD is a cloud practice-management, medical-billing and electronic health record (EHR) software company founded in 1999 and headquartered in South Jordan, Utah, serving independent ambulatory practices, mental-health and physical-medicine clinics, med spas and medical-billing services across the United States. A standalone company again since Francisco Partners acquired it from Global Payments in December 2024, AdvancedMD operates two clearly separated developer surfaces. The first is a public, no-cost HL7 FHIR R4 (4.0.1) read-only API estate published for ONC (g)(10) Cures Act certification at fhir.advancedmd.com, aligned to the US Core 6.1.0 Implementation Guide, authorized with SMART-on-FHIR OAuth 2.0 and covering both single-patient access and FHIR Bulk Data Access group export. The second is a gated proprietary Connect API estate (REST and XML-RPC) plus an ODBC data-access driver, which require a signed Certified API Developer Agreement with licensing and support
  fees before sandbox or production credentials are issued.
image: https://www.advancedmd.com/wp-content/uploads/2025/06/cropped-bird_solid_5121-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: advancedmd-mcp.yml
  slug: advancedmd-mcpyml
modified: '2026-07-27'
name: AdvancedMD
nav: Providers
network: true
overview: 'AdvancedMD publishes 3 APIs on the [APIs.io](https://apis.io/) network: FHIR Single API (US Core 6.1.0), FHIR Bulk API, and Application Access APIs (Legacy Patient APIs). Tagged areas include Healthcare, United States, EHR, EMR, and Practice Management.


  AdvancedMD''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, FAQ, signup flow, and 36 more developer resources.'
random_paper: 71
rate_limits:
- limit_count: 0
  name: Advancedmd Rate Limits
  slug: advancedmd-rate-limits
scopes:
- name: Advancedmd Scopes
  scope_count: 128
  slug: advancedmd-scopes
  summary_line: 128 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.7
  delta: -2.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 40.0
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Advancedmd Authentication
  slug: advancedmd-authentication
  summary_line: oauth2/openIdConnect/apiKey/http · 7 schemes
- kind: domain-security
  name: Advancedmd Domain Security
  slug: advancedmd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advancedmd
tags:
- Healthcare
- United States
- EHR
- EMR
- Practice Management
- Medical Billing
- FHIR
- HL7
- SMART on FHIR
- US Core
- Interoperability
- Revenue Cycle Management
- Scheduling
website: https://www.advancedmd.com/
---
