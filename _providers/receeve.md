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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 34
  human_in_the_loop: 2
  name: Receeve Agentic Access
  operation_count: 46
  slug: receeve-agentic-access
  summary_line: 46 operations · 34 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: A formal business arrangement providing for regular dealings or services (such as banking, advertising, or store credit) and involving the establishment and maintenance of an account
  name: Receeve Account API
  slug: receeve-account-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The AccountMandate API from Receeve — 3 operation(s) for accountmandate.
  name: Receeve AccountMandate API
  slug: receeve-accountmandate-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: A claim is an outstanding payment that is owed. You can always update this balance if multiple payments are missed and you want to aggregate the amounts.
  name: Receeve Claim API
  slug: receeve-claim-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The CustomTriggers API from Receeve — 1 operation(s) for customtriggers.
  name: Receeve CustomTriggers API
  slug: receeve-customtriggers-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Debtor API from Receeve — 1 operation(s) for debtor.
  name: Receeve Debtor API
  slug: receeve-debtor-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: Event that happened in Receive systems, for example, claim created or email delivered.
  name: Receeve Event API
  slug: receeve-event-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Files API from Receeve — 1 operation(s) for files.
  name: Receeve Files API
  slug: receeve-files-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Finance Instalments V2 API from Receeve — 5 operation(s) for finance instalments v2.
  name: Receeve Finance Instalments V2 API
  slug: receeve-finance-instalments-v2-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Finance Settlements API from Receeve — 5 operation(s) for finance settlements.
  name: Receeve Finance Settlements API
  slug: receeve-finance-settlements-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: This is the overall strategy to resolve the outstanding payment or debt.
  name: Receeve Journey API
  slug: receeve-journey-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Landing Page of the Debtor, used to display, pay the Claims (or other use cases).
  name: Receeve LandingPage API
  slug: receeve-landingpage-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: Communication message in .eml format that was sent to Debtor.
  name: Receeve Message API
  slug: receeve-message-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The PromiseToPay API from Receeve — 1 operation(s) for promisetopay.
  name: Receeve PromiseToPay API
  slug: receeve-promisetopay-api
- baseURL: https://api.receive-demo.com
  baseurl_source: declared
  description: The Security API from Receeve — 1 operation(s) for security.
  name: Receeve Security API
  slug: receeve-security-api
artifact_total: 34
asyncapis:
- description: Signed outbound webhook event catalog for InDebted's Receive (formerly Receeve) debt servicing platform. Every event is delivered as an HTTP POST with a common envelope and an RSA/SHA-256 signature (b
  name: Receive (Receeve) Webhook Events
  slug: receeve-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: InDebted Receive API Documentation Account API
  slug: open-receeve-account-api
- collection_type: open
  name: InDebted Receive API Documentation Account AccountMandate API
  slug: open-receeve-accountmandate-api
- collection_type: open
  name: InDebted Receive API Documentation Account Claim API
  slug: open-receeve-claim-api
- collection_type: open
  name: InDebted Receive API Documentation Account CustomTriggers API
  slug: open-receeve-customtriggers-api
- collection_type: open
  name: InDebted Receive API Documentation Account Debtor API
  slug: open-receeve-debtor-api
- collection_type: open
  name: InDebted Receive API Documentation Account Event API
  slug: open-receeve-event-api
- collection_type: open
  name: InDebted Receive API Documentation Account Files API
  slug: open-receeve-files-api
- collection_type: open
  name: InDebted Receive API Documentation Account Finance Instalments V2 API
  slug: open-receeve-finance-instalments-v2-api
- collection_type: open
  name: InDebted Receive API Documentation Account Finance Settlements API
  slug: open-receeve-finance-settlements-api
- collection_type: open
  name: InDebted Receive API Documentation Account Journey API
  slug: open-receeve-journey-api
- collection_type: open
  name: InDebted Receive API Documentation Account LandingPage API
  slug: open-receeve-landingpage-api
- collection_type: open
  name: InDebted Receive API Documentation Account Message API
  slug: open-receeve-message-api
- collection_type: open
  name: InDebted Receive API Documentation Account PromiseToPay API
  slug: open-receeve-promisetopay-api
- collection_type: open
  name: InDebted Receive API Documentation Account Security API
  slug: open-receeve-security-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/receeve-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/receeve-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/receeve-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.receeve.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.indebted.co/docs/receive/
- group: docs
  title: ''
  type: APIReference
  url: https://api.receeve.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.indebted.co/docs/receive/integration/tl-dr
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.indebted.co/
- group: auth
  title: ''
  type: Authentication
  url: authentication/receeve-authentication.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/receeve-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/receeve-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/receeve-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/receeve-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/receeve-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/receeve-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/receeve-problem-types.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/receeve-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/receeve-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/receeve-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/receeve-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/receeve-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/receeve-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Receeve is a no-code debt collection and receivables management SaaS platform, founded in Hamburg, Germany and backed by Speedinvest. It was acquired by InDebted and now operates as the "Receive" product — a debt servicing platform that lets creditors, banks, lenders, utilities and collection agencies automate the full collections lifecycle: importing accounts and claims, running configurable dunning strategies and journeys, sending multi-channel communications (email, SMS, letters, calls), generating hosted debtor landing pages, and reconciling payments, promises-to-pay, instalment plans and settlements. The Receive Client API is an OpenAPI 3.0 REST API secured with OAuth2 client-credentials (Bearer tokens) and emits an extensive catalog of signed webhooks for account, claim, communication, finance, landing-page and strategy events.'
image: https://www.indebted.co/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Receeve MCP Server
  slug: receeve-mcp-server
modified: '2026-07-21'
name: Receeve
nav: Providers
network: true
overview: 'Receeve publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, AccountMandate API, Claim API, and 11 more. Tagged areas include Company, Debt Collection, Receivables Management, Debt Servicing, and Collection.


  The Receeve catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Receeve''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 18 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 4.5
    contract_quality: 60.3
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/receeve/refs/heads/main/screenshots/receeve-2026-09-02T153040.png
security:
- kind: authentication
  name: Receeve Authentication
  slug: receeve-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Receeve Domain Security
  slug: receeve-domain-security
  summary_line: TLSv1.3 · DMARC
slug: receeve
tags:
- Company
- Debt Collection
- Receivables Management
- Debt Servicing
- Collection
- Fintech
- Payments
- Webhook
- Financial-Services
- Dunning
website: https://api.receeve.com/
---
