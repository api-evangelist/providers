---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Clearspeed Agentic Access
  operation_count: 4
  slug: clearspeed-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 1
apis:
- description: REST API for embedding Clearspeed voice-based risk assessment into an existing system. Create participants against a questionnaire, update outcome tracking, and create or delete scoped API keys. Asses
  name: Clearspeed Integration API
  slug: integration-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.clearspeed.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clearspeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clearspeed.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clearspeed.com/apis/public/integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clearspeed.com/
- group: operate
  title: ''
  type: Support
  url: https://www.clearspeed.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.clearspeed.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.clearspeed.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearspeed.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearspeed.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.clearspeed.com/security-commitment
- group: auth
  title: ''
  type: TrustCenter
  url: security/clearspeed-trust-center.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/clearspeed-integration-api-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clearspeed-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clearspeed-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clearspeed-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clearspeed-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clearspeed-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clearspeed-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clearspeed-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clearspeed-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/clearspeed-integration-api-examples.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clearspeed-integration-api-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clearspeed-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clearspeed-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clearspeed-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/clearspeed-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearspeed-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clearspeed-agentic-access.yml
created: '2026-08-02'
description: Clearspeed is a voice-based risk assessment company whose AI analyzes involuntary vocal characteristics — tone, cadence, hesitation and stress — in a subject's spoken yes/no answers to produce an objective, language-independent risk indicator without requiring PII. Founded in 2016, it serves insurance claims and underwriting, government and defense vetting, financial services fraud and AML/KYC, plus hiring and vendor screening. Clearspeed exposes the Clearspeed Integration API, a REST contract on regional US and UK hosts that lets customers create participants against a questionnaire, track outcomes, and manage scoped API keys, with assessment results delivered back by webhook rather than polling.
image: https://www.clearspeed.com/opengraph.jpg
layout: provider
mcp_servers:
- description: ''
  name: clearspeed-mcp.yml
  slug: clearspeed-mcpyml
modified: '2026-08-02'
name: Clearspeed
nav: Providers
network: true
overview: 'Clearspeed publishes 1 API on the [APIs.io](https://apis.io/) network: Integration API. Tagged areas include Company, Risk Assessment, Fraud Detection, Voice Analytics, and Artificial Intelligence.


  Clearspeed''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 49.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Clearspeed Authentication
  slug: clearspeed-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Clearspeed Domain Security
  slug: clearspeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearspeed
tags:
- Company
- Risk Assessment
- Fraud Detection
- Voice Analytics
- Artificial Intelligence
- Insurance
- Identity Verification
- Screening
- Security
website: https://www.clearspeed.com/
---
