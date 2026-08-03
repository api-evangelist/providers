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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Abound Agentic Access
  operation_count: 55
  slug: abound-agentic-access
  summary_line: 55 operations · 33 acting
api_count: 13
apis:
- description: The 1099-INT API from Abound — 6 operation(s) for 1099-int.
  name: Abound 1099-INT API
  slug: abound-1099-int-api
- description: The 1099-K API from Abound — 6 operation(s) for 1099-k.
  name: Abound 1099-K API
  slug: abound-1099-k-api
- description: The 1099-MISC API from Abound — 6 operation(s) for 1099-misc.
  name: Abound 1099-MISC API
  slug: abound-1099-misc-api
- description: The 1099-NEC API from Abound — 6 operation(s) for 1099-nec.
  name: Abound 1099-NEC API
  slug: abound-1099-nec-api
- description: The Access Tokens API from Abound — 1 operation(s) for access tokens.
  name: Abound Access Tokens API
  slug: abound-access-tokens-api
- description: The Electronic Delivery Consents API from Abound — 1 operation(s) for electronic delivery consents.
  name: Abound Electronic Delivery Consents API
  slug: abound-electronic-delivery-consents-api
- description: The Mailings API from Abound — 2 operation(s) for mailings.
  name: Abound Mailings API
  slug: abound-mailings-api
- description: The Tax Treaties API from Abound — 1 operation(s) for tax treaties.
  name: Abound Tax Treaties API
  slug: abound-tax-treaties-api
- description: The TIN Verifications API from Abound — 2 operation(s) for tin verifications.
  name: Abound TIN Verifications API
  slug: abound-tin-verifications-api
- description: The Users API from Abound — 2 operation(s) for users.
  name: Abound Users API
  slug: abound-users-api
- description: The W-8BEN API from Abound — 2 operation(s) for w-8ben.
  name: Abound W-8BEN API
  slug: abound-w-8ben-api
- description: The W-8BEN-E API from Abound — 2 operation(s) for w-8ben-e.
  name: Abound W-8BEN-E API
  slug: abound-w-8ben-e-api
- description: The W-9 API from Abound — 2 operation(s) for w-9.
  name: Abound W-9 API
  slug: abound-w-9-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a user, collect their Form W-9, then run and read back a real-time TIN verification against the IRS.
  name: Collect a W-9 and verify the payee TIN
  slug: abound-collect-w9-and-verify-tin.arazzo
- description: Fix a filed return - either file a correction or void it entirely. Both only work after the document is FILED.
  name: Correct or void a filed 1099-NEC
  slug: abound-correct-or-void-1099.arazzo
- description: Run the full 1099-NEC lifecycle - create the document, file it with federal and state authorities, then mail the payee copy.
  name: Create, file and mail a Form 1099-NEC
  slug: abound-file-1099-nec.arazzo
artifact_total: 22
asyncapis:
- description: 'The Abound webhook event surface: 44 HMAC-signed events covering Users, TIN Verifications, Mailings, Form 1099-INT/K/MISC/NEC and Forms W-9, W-8BEN and W-8BEN-E. Derived from the first-party Fern API '
  name: Abound API v4 - Webhooks
  slug: abound-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://withabound.com
- group: build
  title: ''
  type: Packages
  url: packages/abound-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/abound-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abound-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/abound-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/abound-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/abound-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/abound-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/abound-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/abound-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/abound-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/abound-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/abound-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/abound-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abound-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abound-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abound-agentic-access.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abound-collect-w9-and-verify-tin.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abound-file-1099-nec.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abound-correct-or-void-1099.arazzo.yml
created: '2026-07-17'
description: 'Abound was a US tax-compliance API company for platforms, marketplaces and fintechs serving the 1099 economy. Its v4 REST API covered the full information-return lifecycle: collecting Form W-9, W-8BEN and W-8BEN-E from payees, running real-time TIN verification against the IRS, then generating, filing, correcting, voiding and physically mailing Form 1099-NEC, 1099-MISC, 1099-K and 1099-INT to federal and state tax authorities. It also shipped drop-in UI components for payee onboarding, a 44-event webhook surface, and an official TypeScript SDK. Abound was acquired (announced November 2024) and the service has since been retired: the withabound.com DNS zone is fully de-delegated, the API and docs hosts no longer resolve, and the GitHub organization has been removed. This profile preserves the API surface, recovered from the first-party Fern API Definition shipped inside the official npm package.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abound.png
layout: provider
mcp_servers:
- description: ''
  name: abound-mcp.yml
  slug: abound-mcpyml
modified: '2026-07-19'
name: Abound
nav: Providers
network: true
overview: 'Abound publishes 13 APIs on the [APIs.io](https://apis.io/) network, including 1099-INT API, 1099-K API, 1099-MISC API, and 10 more. Tagged areas include Company, Taxes, Tax Compliance, Regulatory Compliance, and Financial Services.


  The Abound catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Abound''s developer surface includes authentication, sandbox, and 19 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 74.4
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 7.9
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Abound Authentication
  slug: abound-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abound Domain Security
  slug: abound-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: abound
tags:
- Company
- Taxes
- Tax Compliance
- Regulatory Compliance
- Financial Services
- Identity Verification
- Government
- Documents
- Webhooks
- Retired
website: https://withabound.com
---
