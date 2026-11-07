---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: The 3D Secure API from TabaPay — 3 operation(s) for 3d secure.
  name: TabaPay 3D Secure API
  slug: tabapay-3d-secure-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's Account.
  name: TabaPay Account API
  slug: tabapay-account-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Bank.
  name: TabaPay Bank API
  slug: tabapay-bank-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Payment Card (Debit Card, PrePaid Card, or Credit Card).
  name: TabaPay Card API
  slug: tabapay-card-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client.
  name: TabaPay Client API
  slug: tabapay-client-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents an FX Rate.
  name: TabaPay FXRate API
  slug: tabapay-fxrate-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: The Health API from TabaPay — 2 operation(s) for health.
  name: TabaPay Health API
  slug: tabapay-health-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents an RSA Encryption Key.
  name: TabaPay Key API
  slug: tabapay-key-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's Ledger.
  name: TabaPay Ledger API
  slug: tabapay-ledger-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Name on the OFAC Sanctions List.
  name: TabaPay OFAC API
  slug: tabapay-ofac-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's SubClient.
  name: TabaPay SubClient API
  slug: tabapay-subclient-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: The Tag API from TabaPay — 1 operation(s) for tag.
  name: TabaPay Tag API
  slug: tabapay-tag-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's Transaction.
  name: TabaPay Transaction API
  slug: tabapay-transaction-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's User.
  name: TabaPay User API
  slug: tabapay-user-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a Client's Verification.
  name: TabaPay Verification API
  slug: tabapay-verification-api
- baseURL: https://api.tabapay.com
  baseurl_source: declared
  description: This resource represents a TransactionRequest One-time Payment Portal (>)
  name: TabaPay Transaction Request API
  slug: tabapay-transaction-request-api
artifact_total: 40
collections:
- collection_type: open
  name: TabaPay APIs 3D Secure API
  slug: open-tabapay-3d-secure-api
- collection_type: open
  name: TabaPay APIs 3D Secure Account API
  slug: open-tabapay-account-api
- collection_type: open
  name: TabaPay APIs 3D Secure Bank API
  slug: open-tabapay-bank-api
- collection_type: open
  name: TabaPay APIs 3D Secure Card API
  slug: open-tabapay-card-api
- collection_type: open
  name: TabaPay APIs 3D Secure Client API
  slug: open-tabapay-client-api
- collection_type: open
  name: TabaPay APIs 3D Secure FXRate API
  slug: open-tabapay-fxrate-api
- collection_type: open
  name: TabaPay APIs 3D Secure Health API
  slug: open-tabapay-health-api
- collection_type: open
  name: TabaPay APIs 3D Secure Key API
  slug: open-tabapay-key-api
- collection_type: open
  name: TabaPay APIs 3D Secure Ledger API
  slug: open-tabapay-ledger-api
- collection_type: open
  name: TabaPay APIs 3D Secure OFAC API
  slug: open-tabapay-ofac-api
- collection_type: open
  name: TabaPay APIs 3D Secure SubClient API
  slug: open-tabapay-subclient-api
- collection_type: open
  name: TabaPay APIs 3D Secure Tag API
  slug: open-tabapay-tag-api
- collection_type: open
  name: TabaPay APIs 3D Secure Transaction API
  slug: open-tabapay-transaction-api
- collection_type: open
  name: TabaPay APIs 3D Secure TransactionRequest API
  slug: open-tabapay-transactionrequest-api
- collection_type: open
  name: TabaPay APIs 3D Secure User API
  slug: open-tabapay-user-api
- collection_type: open
  name: TabaPay APIs 3D Secure Verification API
  slug: open-tabapay-verification-api
common:
- group: agent
  href: https://artifacts.apis.io/tabapay/skills/tabapay-3ds-transaction.md
  title: ''
  type: AgentSkill
  url: skills/tabapay-3ds-transaction.md
- group: other
  href: https://artifacts.apis.io/tabapay/overlays/tabapay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tabapay-openapi-overlay.yaml
- group: build
  title: ''
  type: SDKs
  url: https://developers.tabapay.com/reference/client
- group: auth
  href: https://artifacts.apis.io/tabapay/security/tabapay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tabapay-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tabapay/authentication/tabapay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tabapay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tabapay.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tabapay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tabapay.com/docs/learn-more
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tabapay.com/reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tabapay.com/docs/starter-guide
- group: operate
  title: ''
  type: Support
  url: https://tabapay.zendesk.com/hc/en-us/requests/new
- group: company
  title: ''
  type: Blog
  url: https://tabapay.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tabapay.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tabapay.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tabapay.com/privacy
- group: start
  title: ''
  type: Login
  url: https://clientcentral.tabapay.net/dashboard/authentication/
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/tabapaydevs/workspace/tabapay-developers
- group: operate
  href: https://artifacts.apis.io/tabapay/changelog/tabapay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tabapay-changelog.yml
- group: agent
  href: https://artifacts.apis.io/tabapay/llms/tabapay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tabapay-llms.txt
- group: agent
  href: https://artifacts.apis.io/tabapay/mcp/tabapay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tabapay-mcp.yml
- group: build
  href: https://artifacts.apis.io/tabapay/packages/tabapay-packages.yml
  title: ''
  type: Packages
  url: packages/tabapay-packages.yml
- group: build
  href: https://artifacts.apis.io/tabapay/packages/tabapay-packages.yml
  title: ''
  type: SDKs
  url: packages/tabapay-packages.yml
- group: agent
  href: https://artifacts.apis.io/tabapay/well-known/tabapay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tabapay-well-known.yml
- group: design
  href: https://artifacts.apis.io/tabapay/conformance/tabapay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tabapay-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://developers.tabapay.com/reference/pcisoc
- group: design
  href: https://artifacts.apis.io/tabapay/errors/tabapay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tabapay-problem-types.yml
- group: build
  href: https://artifacts.apis.io/tabapay/errors/tabapay-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/tabapay-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/tabapay/lifecycle/tabapay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tabapay-lifecycle.yml
- group: start
  href: https://artifacts.apis.io/tabapay/sandbox/tabapay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tabapay-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tabapay/conventions/tabapay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tabapay-conventions.yml
- group: design
  href: https://artifacts.apis.io/tabapay/conventions/tabapay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tabapay-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tabapay/rate-limits/tabapay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tabapay-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tabapay/components/tabapay-components.yml
  title: ''
  type: Components
  url: components/tabapay-components.yml
- group: design
  href: https://artifacts.apis.io/tabapay/data-model/tabapay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tabapay-data-model.yml
- group: agent
  href: https://artifacts.apis.io/tabapay/skills/_index.yml
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-07-17'
description: 'TabaPay is an instant money movement platform for fintechs, banks, and payment companies. One Unified API accepts payments (pull) and sends payouts (push) across debit and credit card networks (Visa, Mastercard, Discover, American Express, Accel, STAR), RTP by The Clearing House, and ACH, with cross-border push-to-card, 3D Secure, account verification (AVS, ANI, OFAC), tokenized card storage, KYB/KYC verifications, ledgers, and real-time transaction monitoring. TabaPay is a PCI DSS Level 1 service provider, SOC 1 and SOC 2 Type II certified, and backed by SoftBank Vision Fund. APIs are not publicly self-serve: clients board through TabaPay and receive a dedicated FQDN plus bearer credentials for sandbox and production.'
image: https://cdn.prod.website-files.com/69d506915e199fb590336928/69efd4e2e784c73028ca53f7_Website.svg
layout: provider
mcp_servers:
- description: Official hosted MCP server at https://developers.tabapay.com/mcp (Streamable HTTP) — list/search/get endpoints from the API reference and execute live requests.
  name: TabaPay Developers MCP Server
  slug: tabapay-developers
modified: '2026-07-21'
name: TabaPay
nav: Providers
network: true
overview: 'TabaPay publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including 3D Secure API, Account API, Bank API, and 13 more. Tagged areas include Company, Fintech, Payments, Instant Payments, and Money Movement.


  The TabaPay catalog on APIs.io includes 1 Spectral governance ruleset.


  TabaPay''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 28 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 2
  name: Tabapay Rate Limits
  slug: tabapay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: TabaPay API Rules
  rule_count: 61
  severity_counts:
    error: 48
    hint: 0
    info: 4
    warn: 9
  slug: tabapay-rules
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.9
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 47.2
    developer_ergonomics: 78.0
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 50.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tabapay/tabapay-2026-08-17T082233.png
security:
- kind: authentication
  name: Tabapay Authentication
  slug: tabapay-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tabapay Domain Security
  slug: tabapay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Run a 3D Secure card transaction with TabaPay
  slug: tabapay-3ds-transaction
- name: Accept a pull payment with TabaPay
  slug: tabapay-pull-payment
- name: Send an instant payout (push to card) with TabaPay
  slug: tabapay-push-to-card
slug: tabapay
tags:
- Company
- Fintech
- Payments
- Instant Payments
- Money Movement
- Payouts
- Cards
- Real-Time Payments
- ACH
website: https://tabapay.com
---
