---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    event_surface_described: true
    idempotency: verified
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Outbound HTTPS webhook deliveries covering nine topics across the ACH, RfP and RTP rails — transaction_completed, transaction_voided, transaction_refunded, transaction_declined, transaction_resolved, '
  name: Aeropay Webhooks
  slug: aeropay-webhooks
- description: A remote Model Context Protocol server hosted by Aeropay at https://dev.aero.inc/mcp, documented for Cursor, Windsurf and Claude Desktop. Anonymous tools/list returns four spec-driven tools — list-end
  name: Aeropay API MCP Server
  slug: aeropay-mcp
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Authentication API from Aeropay — 1 operation(s) for authentication.
  name: Aeropay Authentication API
  slug: aeropay-authentication-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Bank Connection API from Aeropay — 4 operation(s) for bank connection.
  name: Aeropay Bank Connection API
  slug: aeropay-bank-connection-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Create & Manage Transactions API from Aeropay — 12 operation(s) for create & manage transactions.
  name: Aeropay Create & Manage Transactions API
  slug: aeropay-create-manage-transactions-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Merchant Management API from Aeropay — 2 operation(s) for merchant management.
  name: Aeropay Merchant Management API
  slug: aeropay-merchant-management-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Reports API from Aeropay — 3 operation(s) for reports.
  name: Aeropay Reports API
  slug: aeropay-reports-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The User Management API from Aeropay — 2 operation(s) for user management.
  name: Aeropay User Management API
  slug: aeropay-user-management-api
- baseURL: https://api.aeropay.com/v2
  baseurl_source: declared
  description: The Webhooks API from Aeropay — 2 operation(s) for webhooks.
  name: Aeropay Webhooks API
  slug: aeropay-webhooks-api
artifact_total: 22
asyncapis:
- description: Aeropay delivers transaction and user lifecycle events to a merchant-registered callback URL over HTTPS POST. A subscription is created with POST /v2/webhook by naming a topic and a url; the same call
  name: Aeropay Webhooks
  slug: aeropay-webhooks-asyncapi
common:
- group: other
  href: https://artifacts.apis.io/aeropay/capabilities/aeropay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aeropay-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.aeropay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aeropay.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://dev.aero.inc/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://dev.aero.inc/reference/post_v2-token
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.aero.inc/docs/api-quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.aeropay.com/personal/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aeropay.com/
- group: company
  title: ''
  type: Blog
  url: https://www.aeropay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aeropay-inc
- group: start
  title: ''
  type: SignUp
  url: https://portal.aeropay.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aeropay.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeropay.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeropay.com/legal/privacy-policy
- group: auth
  href: https://artifacts.apis.io/aeropay/security/aeropay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/aeropay-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://www.aeropay.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.aeropay.com/trust-center
- group: design
  href: https://artifacts.apis.io/aeropay/conformance/aeropay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aeropay-conformance.yml
- group: auth
  href: https://artifacts.apis.io/aeropay/security/aeropay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aeropay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/aeropay/authentication/aeropay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aeropay-authentication.yml
- group: design
  href: https://artifacts.apis.io/aeropay/conventions/aeropay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aeropay-conventions.yml
- group: design
  href: https://artifacts.apis.io/aeropay/conventions/aeropay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/aeropay-conventions.yml
- group: design
  href: https://artifacts.apis.io/aeropay/errors/aeropay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aeropay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aeropay/errors/aeropay-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/aeropay-error-codes.yml
- group: build
  href: https://artifacts.apis.io/aeropay/errors/aeropay-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/aeropay-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/aeropay/data-model/aeropay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aeropay-data-model.yml
- group: design
  href: https://artifacts.apis.io/aeropay/lifecycle/aeropay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aeropay-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aeropay/changelog/aeropay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aeropay-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.aero.inc/docs/release-notes
- group: operate
  href: https://artifacts.apis.io/aeropay/rate-limits/aeropay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aeropay-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aeropay/plans/aeropay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aeropay-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/aeropay/packages/aeropay-packages.yml
  title: ''
  type: Packages
  url: packages/aeropay-packages.yml
- group: build
  href: https://artifacts.apis.io/aeropay/packages/aeropay-packages.yml
  title: ''
  type: SDKs
  url: packages/aeropay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://dev.aero.inc/docs/npm-sdk
- group: design
  href: https://artifacts.apis.io/aeropay/components/aeropay-components.yml
  title: ''
  type: Components
  url: components/aeropay-components.yml
- group: start
  href: https://artifacts.apis.io/aeropay/sandbox/aeropay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aeropay-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/aeropay/mcp/aeropay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aeropay-mcp.yml
- group: build
  href: https://artifacts.apis.io/aeropay/mcp/aeropay-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aeropay-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/aeropay/asyncapi/aeropay-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/aeropay-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/aeropay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/aeropay/llms/aeropay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aeropay-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dev.aero.inc/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.aeropay.com/llms.txt
- group: other
  href: https://artifacts.apis.io/aeropay/overlays/aeropay-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aeropay-v2-overlay.yaml
created: '2026-09-10'
description: Aeropay is a Chicago-based fintech operating a pay-by-bank network that moves money directly between consumer bank accounts and merchants over ACH, Request for Payment (RfP) and RTP rails, without cards. The product suite is Aerosync (branded bank linking and account connectivity), Pay (merchant acceptance of bank payments), Payout (real-time merchant-to-consumer credits) and Guard (risk decisioning and fraud prevention). Integrators use the Aeropay v2 REST API — a 32-operation OpenAPI 3.0.0 contract covering token issuance, user creation and MFA confirmation, bank linking through an aggregator widget, standard, preauthorized, payout and reversal transactions, transaction search, payment links, webhook subscriptions, reporting and merchant reputation — alongside first-party Aerosync bank-linking SDKs for web, React Native, Android, iOS and Flutter. Aeropay publishes a documentation llms.txt, a remote MCP server for the API reference, a nine-topic webhook catalog, a 91-entry
  error glossary, a NACHA ACH return-code glossary and a substantial sandbox exception-scenario harness. It is SOC 2 compliant and audits its ACH operations annually against NACHA standards.
finops:
- has_sources: true
  method: derived
  name: Aeropay Finops
  primary_unit: ''
  service_category: ''
  slug: aeropay-finops
  template: true
image: https://cdn.prod.website-files.com/6883a0f9156861b50901e79e/68d3ffdc98b692fcb2df6fa4_Aeropay-256xv2.png
layout: provider
mcp_servers:
- description: Remote MCP server at dev.aero.inc over HTTP; 4 tools listed.
  name: Aeropay MCP Server
  slug: api-aeropay
modified: '2026-09-10'
name: Aeropay
nav: Providers
network: true
overview: 'Aeropay publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Bank Connection API, Create & Manage Transactions API, and 6 more. Tagged areas include Payments, Pay by Bank, ACH, Open Banking, and Fintech.


  The Aeropay catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Aeropay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 37 more developer resources.'
plans:
- name: Aeropay Plans Pricing
  plan_count: 0
  slug: aeropay-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aeropay Rate Limits
  slug: aeropay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Aeropay API Rules
  rule_count: 53
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 5
  slug: aeropay-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 54.3
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 49.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 29.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aeropay Authentication
  slug: aeropay-authentication
  summary_line: http-bearer/credentials-exchange · 2 schemes
- kind: domain-security
  name: Aeropay Domain Security
  slug: aeropay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Aeropay Trust Center
  slug: aeropay-trust-center
  summary_line: SOC 2, Nacha ACH Operating Rules
skill_count: 4
skills:
- name: aeropay-payout-and-refund
  slug: aeropay-payout-and-refund
- name: aeropay-preauthorized-transaction
  slug: aeropay-preauthorized-transaction
- name: aeropay-standard-transaction
  slug: aeropay-standard-transaction
- name: aeropay-webhooks-and-reconciliation
  slug: aeropay-webhooks-and-reconciliation
slug: aeropay
tags:
- Payments
- Pay by Bank
- ACH
- Open Banking
- Fintech
- Bank linking
- Financial Services
- Real-Time Payments
- Webhook
- Payouts
- MCP
- Risk & fraud
website: https://www.aeropay.com/
---
