---
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Qoala Agentic Access
  operation_count: 51
  slug: qoala-agentic-access
  summary_line: 51 operations · 35 acting
api_count: 2
apis:
- description: 'Session management for the Qoala for Enterprise platform — create an authentication session from an email and security code, and refresh it with a refresh token. Returns a JWT access token, a refresh '
  name: Qoala Authentication API
  slug: qoala-authentication-api
- description: Policy API documentation consist of create policy, get policy detail or status, policy cancellation and policy activation.
  name: Qoala API Specification API
  slug: qoala-api-specification-api
artifact_total: 11
asyncapis:
- description: ''
  name: Qoala Webhooks
  slug: qoala-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qoala API Specification API
  slug: open-qoala-api-specification-api
- collection_type: open
  name: Authentication API
  slug: open-qoala-authentication-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qoala-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qoala-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qoala-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://qoala.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qoala.app/reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qoala.app/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qoala.app/reference/api-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qoala.app/reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.qoala.app/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.qoala.app/id-en/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.qoala.app/id-en/account
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qoala.app/id-en/privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qoala-engineering
- group: company
  title: ''
  type: Partners
  url: https://www.qoala.app/id-en/partnership
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qoala-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qoala-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.qoala.app/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qoala-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/qoala-tool-crosswalk.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qoala-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/qoala-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qoala-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qoala-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qoala-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qoala-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qoala-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qoala-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qoala-activate-gadget-policy.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qoala-authenticate-session.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qoala-cancel-policy.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qoala-file-and-track-claim.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/qoala-issue-policy.md
created: '2026-08-05'
description: 'Qoala is a Southeast Asian omni-channel insurtech, headquartered in Jakarta and operating across Indonesia, Malaysia, Thailand and Vietnam, that distributes personal and embedded insurance through a consumer app, an agent platform (Qoala Plus) and a partner/enterprise API. Qoala for Enterprise exposes a partner-facing REST API covering policy issuance and claim handling across travel (flight, train, bus, hotel, experience), gadget, goods, vehicle, logistics, health, credit and credit-life product lines. Policy creation is asynchronous: partners POST a quotation, receive a quotation number as acknowledgement, and are notified of the issued policy through a partner callback webhook. Authentication is by partner API key in the x-api-key header.'
image: https://assets.qoala.app/images/icons/qoala.png
layout: provider
mcp_servers:
- description: ''
  name: Qoala MCP Server
  slug: qoala-mcp-server
- description: ''
  name: Qoala for Enterprise
  slug: qoala-for-enterprise
modified: '2026-08-05'
name: Qoala
nav: Providers
network: true
overview: 'Qoala publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and API Specification API. Tagged areas include Insurance, Insurtech, Embedded Insurance, Policies, and Claims.


  The Qoala catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qoala''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, sandbox, and 26 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 39.7
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 62.2
    developer_ergonomics: 38.7
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 31.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qoala/refs/heads/main/screenshots/qoala-2026-08-17T081418.png
security:
- kind: authentication
  name: Qoala Authentication
  slug: qoala-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qoala Domain Security
  slug: qoala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qoala
tags:
- Insurance
- Insurtech
- Embedded Insurance
- Policies
- Claims
- Southeast Asia
- Indonesia
- Financial-Services
- Partner API
website: https://qoala.com/
---
