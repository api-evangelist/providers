---
access_model:
  confidence: high
  label: Enterprise · Partner/approval onboarding · No public self-serve API
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - website
  - legal
  - postman
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api-{tenant-id}.developer.commure.com
  baseurl_source: declared
  description: The auth API from Commure — 6 operation(s) for auth.
  name: Commure Auth API
  slug: commure-auth-api
- baseURL: https://api-{tenant-id}.developer.commure.com
  baseurl_source: declared
  description: The FHIR API from Commure — 49 operation(s) for fhir.
  name: Commure FHIR API
  slug: commure-fhir-api
artifact_total: 10
collections:
- collection_type: open
  name: Commure FHIR API
  slug: open-commure-fhir
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/commure-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.commure.com/
- group: other
  title: ''
  type: Company
  url: https://www.commure.com/company
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/commure/commure/documentation/vp76tv7/commure-fhir-api
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/commure/commure/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/commure-fhir-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commure-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/commure-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/commure-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/commure-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/commure-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/commure-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/commure-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/commure-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/commure-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.commure.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/commure-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commure-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.commure.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.commure.com/trust-center
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/commure-fhir-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commure-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/commure-packages.yml
- group: design
  title: ''
  type: Components
  url: components/commure-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/commure-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/commure-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/commure-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/commure-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.commure.com/pricing
- group: other
  title: ''
  type: Resources
  url: https://www.commure.com/resources
- group: company
  title: ''
  type: Careers
  url: https://www.commure.com/careers
- group: other
  title: ''
  type: Events
  url: https://www.commure.com/events
- group: design
  title: ''
  type: RealWorldTesting
  url: https://www.commure.com/real-world-testing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.commure.com/signin/register
- group: start
  title: ''
  type: Login
  url: https://accounts.commure.com/signin
- group: company
  title: ''
  type: Blog
  url: https://www.commure.com/blog
- group: company
  title: ''
  type: News
  url: https://www.commure.com/news
- group: company
  title: ''
  type: Partners
  url: https://www.commure.com/partners
- group: operate
  title: ''
  type: Support
  url: https://www.commure.com/contact
- group: other
  title: ''
  type: Customers
  url: https://www.commure.com/customers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commure.com/legal/general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commure.com/legal/privacy-policy
- group: commercial
  title: ''
  type: DeveloperUserAgreement
  url: https://www.commure.com/legal/developer-user-agreement
- group: commercial
  title: ''
  type: BusinessAssociateAgreement
  url: https://www.commure.com/legal/business-associate-agreement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commure
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commure
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/commure_stock/
created: '2026-07-24'
description: Commure is a San Francisco-based AI-native healthcare technology company that operates an integrated clinical and operational platform for United States health systems following its 2023 combination with Athelas. Its products span Ambient AI clinical documentation (Scribe/Dictation), end-to-end Revenue Cycle Management (RCM), Call Center Agents, referral Orchestrator, patient Engage coordination, Commure Pro clinical intelligence, Strongline staff-safety alerting, and Athelas Home point-of-care diagnostics, integrating with 60+ EHRs across 130+ health systems processing over $25B in annual claims. Commure launched a FHIR-native open developer platform in 2020; that public developer portal (developer.commure.com) and its tenant API hosts (api-{tenant-id}.developer.commure.com) no longer resolve, and today the API surface is a gated, partner-only offering governed by a Developer User Agreement (Sandbox Environment + Developer Services). The one surviving first-party machine-readable
  contract is Commure's public Postman workspace, which publishes a 59-request "Commure FHIR API" collection covering the HL7 FHIR RESTful, terminology and Bulk Data operations plus the OpenID Connect / SMART App Launch authentication endpoints, alongside five clinical-scenario collections. Home market is the United States.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Commure MCP Server
  slug: commure-mcp-server
modified: '2026-08-15'
name: Commure
nav: Providers
network: true
overview: 'Commure publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auth API and FHIR API. Tagged areas include Healthcare, United States, Clinical AI, Ambient AI, and Revenue Cycle Management.


  Commure''s developer surface includes API reference, authentication, sandbox, pricing, signup flow, engineering blog, product news, and 41 more developer resources.'
plans:
- name: Commure Plans Pricing
  plan_count: 0
  slug: commure-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Commure Rate Limits
  slug: commure-rate-limits
scopes:
- name: Commure Scopes
  scope_count: 5
  slug: commure-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 52.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 51.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 82.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commure/refs/heads/main/screenshots/commure-2026-07-25T210143.png
security:
- kind: authentication
  name: Commure Authentication
  slug: commure-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Commure Domain Security
  slug: commure-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Commure Trust Center
  slug: commure-trust-center
  summary_line: SOC 2 Type II, HIPAA, HITECH Act, CCPA
slug: commure
tags:
- Healthcare
- United States
- Clinical AI
- Ambient AI
- Revenue Cycle Management
- FHIR
- SMART on FHIR
- Interoperability
- EHR
- Remote Monitoring
- Health System
- Terminology Services
website: https://www.commure.com/
---
