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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Core API from Evervault — 9 operation(s) for core.
  name: Evervault Core API
  slug: evervault-core-api
- description: The Payments API from Evervault — 17 operation(s) for payments.
  name: Evervault Payments API
  slug: evervault-payments-api
- description: The Webhooks API from Evervault — 2 operation(s) for webhooks.
  name: Evervault Webhooks API
  slug: evervault-webhooks-api
- description: The Evervault API API from Evervault — 0 operation(s) for evervault api.
  name: Evervault Evervault API
  slug: evervault-evervault-api-api
artifact_total: 34
asyncapis:
- description: ''
  name: Evervault Webhooks
  slug: evervault-webhooks
collections:
- collection_type: postman
  name: Evervault 3D Secure API
  slug: postman-evervault-3d-secure-api
- collection_type: postman
  name: Evervault Acquirers API
  slug: postman-evervault-acquirers-api
- collection_type: postman
  name: Evervault Card Account Updates API
  slug: postman-evervault-card-account-updates-api
- collection_type: postman
  name: Evervault Client Tokens API
  slug: postman-evervault-client-tokens-api
- collection_type: postman
  name: Evervault Core API
  slug: postman-evervault-core-api
- collection_type: postman
  name: Evervault Functions API
  slug: postman-evervault-functions-api
- collection_type: postman
  name: Evervault Insights API
  slug: postman-evervault-insights-api
- collection_type: postman
  name: Evervault Merchants API
  slug: postman-evervault-merchants-api
- collection_type: postman
  name: Evervault Network Tokens API
  slug: postman-evervault-network-tokens-api
- collection_type: postman
  name: Evervault Payments API
  slug: postman-evervault-payments-api
- collection_type: postman
  name: Evervault Relays API
  slug: postman-evervault-relays-api
- collection_type: postman
  name: Evervault Webhooks API
  slug: postman-evervault-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evervault 3D Secure API
  slug: open-evervault-3d-secure-api
- collection_type: open
  name: Evervault Acquirers API
  slug: open-evervault-acquirers-api
- collection_type: open
  name: Evervault Card Account Updates API
  slug: open-evervault-card-account-updates-api
- collection_type: open
  name: Evervault Client Tokens API
  slug: open-evervault-client-tokens-api
- collection_type: open
  name: Evervault Core API
  slug: open-evervault-core-api
- collection_type: open
  name: Evervault Functions API
  slug: open-evervault-functions-api
- collection_type: open
  name: Evervault Insights API
  slug: open-evervault-insights-api
- collection_type: open
  name: Evervault Merchants API
  slug: open-evervault-merchants-api
- collection_type: open
  name: Evervault Network Tokens API
  slug: open-evervault-network-tokens-api
- collection_type: open
  name: Evervault Payments API
  slug: open-evervault-payments-api
- collection_type: open
  name: Evervault Relays API
  slug: open-evervault-relays-api
- collection_type: open
  name: Evervault Webhooks API
  slug: open-evervault-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/evervault-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/evervault/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.evervault.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.evervault.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.evervault.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.evervault.com/core-concepts
- group: company
  title: ''
  type: Blog
  url: https://evervault.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evervault
- group: commercial
  title: ''
  type: Pricing
  url: https://evervault.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.evervault.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evervault.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evervault.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evervault.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://evervault.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/evervault-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/evervault-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/evervault-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/evervault-cli.yml
- group: design
  title: ''
  type: Components
  url: components/evervault-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/evervault-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/evervault-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evervault-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/evervault-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/evervault-security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/evervault-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/evervault-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/evervault-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/evervault-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/evervault-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/evervault-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.evervault.com/compliance/pci-compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evervault-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/evervault-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://evervault.com/.well-known/security.txt
- group: company
  title: ''
  type: Website
  url: https://evervault.com
created: '2026-07-17'
description: 'Evervault is a data-security and payments-infrastructure platform that lets developers encrypt, tokenize, and process sensitive data - especially cardholder data - without it touching their own infrastructure. Its model stores encryption keys on Evervault''s side while customers hold the ciphertext, reducing breach scope. Core products include Relay (an encrypting/decrypting proxy), Functions (secure serverless runtimes), Enclaves (AWS Nitro Enclave workloads), UI Components for PCI-compliant card collection, plus payments tooling: network tokens, 3D Secure, BIN lookup, card account updater, and multi-PSP routing. Evervault is PCI DSS Level 1 and SOC 2 Type II, and supports HIPAA and GDPR.'
image: https://evervault.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Evervault MCP Server
  slug: evervault-mcp-server
modified: '2026-07-19'
name: Evervault
nav: Providers
network: true
overview: 'Evervault publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Core API, Payments API, Webhooks API, and 1 more. Tagged areas include Company, Data, Security, Encryption, and Payments.


  The Evervault catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Evervault''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 29 more developer resources.'
random_paper: 3
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 62.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evervault/refs/heads/main/screenshots/evervault-2026-08-07T165228.png
security:
- kind: authentication
  name: Evervault Authentication
  slug: evervault-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Evervault Domain Security
  slug: evervault-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Evervault Vulnerability Disclosure
  slug: evervault-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: evervault
tags:
- Company
- Data
- Security
- Encryption
- Payments
- PCI Compliance
- Tokenization
- Cards
- Developer Tools
website: https://evervault.com
---
