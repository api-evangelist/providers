---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Aquant Agentic Access
  operation_count: 13
  slug: aquant-agentic-access
  summary_line: 13 operations · 10 acting
api_count: 2
apis:
- description: The Aquant MCP Server exposes Aquant's service-intelligence capabilities as eleven agent-callable tools — part catalog lookup, part info and sourcing, agent (technician) data, technician proximity, ob
  name: Aquant MCP Server
  slug: mcp-server
- description: 'The Aquant Conversation Platform (ACP) API powers Voice AI and web chat with Aquant''s service agents. Clients exchange an API key and secret for a one-hour access token at POST /acp/token, then start '
  name: Aquant Conversation Platform (VoiceAI) API
  slug: acp-voiceai
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Confirm a symptom, predict the next symptom, then look up, detail and source the part.
  name: Diagnose an asset and source the right replacement part
  slug: aquant-diagnose-and-source-part
- description: Resolve an asset location, pull technician proficiency, then rank technicians by proximity.
  name: Locate an asset and rank the nearest qualified technician
  slug: aquant-dispatch-nearest-technician
- description: Health-check the service, generate the PM checklist for an asset, then produce the summary report.
  name: Run a preventive-maintenance visit and file the summary
  slug: aquant-preventive-maintenance-visit
artifact_total: 13
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/aquant-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.aquant.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aquant.ai/platform
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.aquant.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.npmjs.com/package/@aquantinc/acp-web-sdk#quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.aquant.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.aquant.ai/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AquantIO
- group: start
  title: ''
  type: Login
  url: https://login.aquant.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/687529371c5de2d8428c0a4d/688ce744542f10274811b354_Terms%20of%20Service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aquant.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.aquant.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://security.aquant.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aquant-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/aquant-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/aquant-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aquant-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aquant-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aquant-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aquant-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/aquant-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aquant-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aquant-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aquant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.aquant.ai/company/whats-new
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aquant-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aquant-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aquant-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aquant-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aquant-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aquant-diagnose-and-source-part.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aquant-dispatch-nearest-technician.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/aquant-preventive-maintenance-visit.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/aquant-mcp-server-overlay.yaml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/aquant-mcp-server-schemas.json
- group: build
  title: ''
  type: Examples
  url: examples/aquant-mcp-server-examples.yml
created: '2026-07-31'
description: 'Aquant is an agentic AI platform built for organizations that manufacture, sell, and service complex equipment. It turns a company''s own service content — manuals, service histories, parts and warranty data, case notes — and the tacit expertise in its technicians'' heads into role-specific AI agents for field technicians, call centers, customer self-service, and service leaders. The platform ships a library of prebuilt agents (Troubleshooting, Knowledge, Parts, IoT, Voice AI, Vision AI, Preventive Maintenance) plus an Agent Studio for building custom agents, and delivers them across web, mobile, voice, offline, and API channels into CRM, FSM, and support-portal workflows. Aquant exposes two public machine-readable surfaces: an MCP server at mcp.aquant.ai that publishes eleven service-intelligence tools over both JSON-RPC Streamable HTTP and REST, and the Aquant Conversation Platform (ACP) voice/chat API at voiceai-api.aquant.ai fronted by a first-party browser SDK.'
image: https://cdn.prod.website-files.com/687529371c5de2d8428c0a4d/6877cd3487c351b4d9032d3b_logo-aquant-light.svg
json_schemas:
- name: Aquant Mcp Server Schemas
  property_count: 0
  slug: aquant-mcp-server-schemas
layout: provider
mcp_servers:
- description: ''
  name: aquant-mcp.yml
  slug: aquant-mcpyml
modified: '2026-07-31'
name: Aquant
nav: Providers
network: true
overview: 'Aquant publishes 2 APIs on the [APIs.io](https://apis.io/) network: MCP Server and Conversation Platform (VoiceAI) API. Tagged areas include Company, Artificial Intelligence, Agents, Field Service, and Service Management.


  Aquant''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 31 more developer resources.'
random_paper: 70
scopes:
- name: Aquant Scopes
  scope_count: 7
  slug: aquant-scopes
  summary_line: 7 scopes · authorizationCode/implicit/deviceCode/password/refreshToken
score:
  band: developing
  composite: 48.8
  delta: 1.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.5
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aquant/refs/heads/main/screenshots/aquant-2026-08-07T161534.png
security:
- kind: authentication
  name: Aquant Authentication
  slug: aquant-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Aquant Domain Security
  slug: aquant-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aquant Trust Center
  slug: aquant-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
slug: aquant
tags:
- Company
- Artificial Intelligence
- Agents
- Field Service
- Service Management
- Manufacturing
- Medical Devices
- Industrial Equipment
- Knowledge Management
- Voice AI
- Model Context Protocol
- Predictive Maintenance
website: https://www.aquant.ai/
---
