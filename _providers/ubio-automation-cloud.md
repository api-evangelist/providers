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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: REST API for running automation jobs on the Automation Cloud. Clients create jobs against a service, supply initial and deferred inputs, poll job events, retrieve outputs, handle 3-D Secure challenges
  name: UBIO Automation Cloud API
  slug: ubio-automation-cloud-api
- description: Automation Cloud Vault API for exchanging sensitive payment card data for opaque tokens before passing it to automation jobs. Clients obtain a one-time password, then vault a PAN or arbitrary data obj
  name: UBIO Vault API
  slug: ubio-vault-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubio-automation-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ubio.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ubio.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubio.ai/terms
- group: docs
  title: ''
  type: APIReference
  url: https://protocol.automationcloud.net/
- group: build
  title: ''
  type: Packages
  url: packages/ubio-automation-cloud-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ubio-automation-cloud-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ubio-automation-cloud-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/ubio-automation-cloud-openid-configuration.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ubio-automation-cloud-protocol-schema.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubio-automation-cloud-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ubio-automation-cloud-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ubio-automation-cloud-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubio-automation-cloud-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ubio-automation-cloud-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ubio-automation-cloud-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ubio-automation-cloud-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ubio-automation-cloud-data-model.yml
created: '2026-07-17'
description: UBIO (ubio.ai, formerly ub.io) is a London-based, Techstars-backed web automation company. Its Automation Cloud platform runs automation scripts as jobs through a REST API, automating end-to-end website flows such as flight and hotel booking, broadband signup, insurance quotes, and job applications. Developers create jobs with inputs, receive outputs and lifecycle events, and handle deferred inputs and 3-D Secure through official JavaScript/TypeScript client libraries, with the ubio Automation Protocol defining typed input/output schemas for more than 50 automation domains.
image: https://avatars.githubusercontent.com/u/4670990?v=4
json_schemas:
- name: Ubio Automation Cloud Protocol
  property_count: 0
  slug: ubio-automation-cloud-protocol
layout: provider
mcp_servers:
- description: ''
  name: ubio-automation-cloud-mcp.yml
  slug: ubio-automation-cloud-mcpyml
modified: '2026-07-21'
name: UBIO Automation Cloud
nav: Providers
network: true
overview: 'UBIO Automation Cloud publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Web Automation, RPA, Travel, and Booking.


  UBIO Automation Cloud''s developer surface includes API reference, authentication, sandbox, and 16 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 20.5
  delta: -1.5
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 22.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ubio Automation Cloud Authentication
  slug: ubio-automation-cloud-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Ubio Automation Cloud Domain Security
  slug: ubio-automation-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ubio-automation-cloud
tags:
- Automation
- Web Automation
- RPA
- Travel
- Booking
- Jobs
- Company
website: https://ubio.ai/
---
