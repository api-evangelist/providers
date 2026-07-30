---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The fhir-r4-formulary-api API from Clover Health — 5 operation(s) for fhir-r4-formulary-api.
  name: Clover Health fhir-r4-formulary-api API
  slug: clover-health-fhir-r4-formulary-api-api
- description: The FHIR R4 ProviderDirectory API API from Clover Health — 17 operation(s) for fhir r4 providerdirectory api.
  name: Clover Health FHIR R4 ProviderDirectory API API
  slug: clover-health-fhir-r4-providerdirectory-api-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cloverhealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.cloverhealth.com/swagger
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.cloverhealth.com/swagger
- group: start
  title: ''
  type: SignUp
  url: https://docs.google.com/forms/d/1qhbMWXYYn3lpBg8026mW20rxGHE9SL2sHNLzVoyOS0g/edit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloverhealth.com/developers/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloverhealth.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:api-support@cloverhealth.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloverHealth
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/clover-health-fhir-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clover-health-fhir-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clover-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clover-health-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clover-health-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clover-health-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clover-health-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clover-health-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clover-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clover-health-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/clover-health-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clover-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cloverhealth.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clover-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloverhealth.com
created: '2026-07-17'
description: Clover Health is a Medicare Advantage health insurer that runs a public developer program built on healthcare interoperability standards. Its public FHIR R4 API exposes a Formulary service (covered drugs, tiers, and utilization management) and a Provider Directory service (practitioners, organizations, locations, healthcare services, and insurance plans), and a separate consent-based Patient Access API delivers a member's clinical and claims data in FHIR-native format via CareEvolution. The APIs implement the CMS Interoperability and Patient Access final rule (CMS-9115-F); Clover was the first payer to go live on a CMS-aligned/TEFCA network. Developers register for approved credentials and authenticate with HTTP Basic or a session cookie.
image: https://cdn.cloverhealth.com/filer_cloudrun_public/img/live-tile-large-310x310.png
layout: provider
mcp_servers:
- description: ''
  name: clover-health-mcp.yml
  slug: clover-health-mcpyml
modified: '2026-07-18'
name: Clover Health
nav: Providers
network: true
overview: 'Clover Health publishes 2 APIs on the [APIs.io](https://apis.io/) network: fhir-r4-formulary-api API and FHIR R4 ProviderDirectory API API. Tagged areas include Company, Healthcare, Health Insurance, Medicare Advantage, and FHIR.


  Clover Health''s developer surface includes documentation, API reference, signup flow, support, authentication, and 19 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 41.6
  delta: -3.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 46.6
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 45.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
    score: 55.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clover-health/refs/heads/main/screenshots/clover-health-2026-07-25T205721.png
security:
- kind: authentication
  name: Clover Health Authentication
  slug: clover-health-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clover Health Domain Security
  slug: clover-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clover Health Vulnerability Disclosure
  slug: clover-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clover-health
tags:
- Company
- Healthcare
- Health Insurance
- Medicare Advantage
- FHIR
- Interoperability
- Provider Directory
- Formulary
- Patient Access
- Payer
website: https://www.cloverhealth.com
---
