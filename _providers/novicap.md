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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Confirming (reverse factoring) invoices and payment instructions.
  name: Novicap Confirming Standard API
  slug: novicap-confirming-standard-api
- description: Dynamic discounting suppliers, invoices, payment instructions and adjustments.
  name: Novicap Dynamic Discounting API
  slug: novicap-dynamic-discounting-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Novicap Confirming Standard API
  slug: open-novicap-confirming-standard-api
- collection_type: open
  name: Novicap Confirming Standard Dynamic Discounting API
  slug: open-novicap-dynamic-discounting-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/novicap-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://novicap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.novicap.com/
- group: company
  title: ''
  type: Blog
  url: https://novicap.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.novicap.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: mailto:support@novicap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novicap.com/aviso-legal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/novicap-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/novicap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/novicap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/novicap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/novicap-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/novicap-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/novicap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/novicap-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/novicap-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/novicap-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/novicap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://novicap.com/.well-known/security.txt
created: '2026-07-17'
description: 'Novicap is a Spanish working-capital and supply-chain-finance fintech that helps companies optimize their circulating capital. Its REST API (base URL https://api.novicap.com/v1) lets partners programmatically register suppliers, submit and manage invoices, and create payment instructions and adjustments across two products: Dynamic Discounting and Confirming Standard (reverse factoring). The API uses Bearer API-key authentication with a required product_id scope, JSON payloads, and URI-path versioning, and is documented in a public developer reference. Novicap is backed by Partech and Techstars.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novicap.png
layout: provider
mcp_servers:
- description: ''
  name: Novicap MCP Server
  slug: novicap-mcp-server
modified: '2026-07-20'
name: Novicap
nav: Providers
network: true
overview: 'Novicap publishes 2 APIs on the [APIs.io](https://apis.io/) network: Confirming Standard API and Dynamic Discounting API. Tagged areas include Company, Financial-Services, Fintech, Working Capital, and Invoice Finance.


  Novicap''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 24.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novicap/refs/heads/main/screenshots/novicap-2026-08-07T185613.png
security:
- kind: authentication
  name: Novicap Authentication
  slug: novicap-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: vulnerability-disclosure
  name: Novicap Vulnerability Disclosure
  slug: novicap-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: novicap
tags:
- Company
- Financial-Services
- Fintech
- Working Capital
- Invoice Finance
- Supply Chain Finance
- Dynamic Discounting
- Confirming
- Reverse Factoring
- Spain
website: https://novicap.com/
---
