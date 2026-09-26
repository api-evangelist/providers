---
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
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- baseURL: https://trustly.one/api/v1
  baseurl_source: declared
  description: REST API (OpenAPI 3.1, 31 operations, 10 documented webhook events) for Trustly Pay by Bank in the United States and Canada. Establish and authorize a transaction through the Trustly Lightbox or Selec
  name: Trustly North America API
  slug: trustly-north-america-api
- description: JSON-RPC 1.1 API for Trustly Pay by Bank in Europe and the UK. Methods cover Deposit, Withdraw/AccountPayout, Refund, SelectAccount, RegisterAccount, VerifyAccount, Charge and recurring direct debit (
  name: Trustly Europe API
  slug: trustly-europe-api
artifact_total: 11
asyncapis:
- description: ''
  name: Trustly North America Webhooks
  slug: trustly-north-america-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/security/trustly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/trustly-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/security/trustly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/trustly-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/security/trustly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trustly-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/authentication/trustly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trustly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.trustly.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://amer.developers.trustly.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trustly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://amer.developers.trustly.com/api-reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://amer.developers.trustly.com/integrate/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.trustly.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://amer.developers.trustly.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.trustly.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trustly
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrustlyInc
- group: start
  title: ''
  type: Login
  url: https://backoffice.trustly.com/
- group: start
  title: ''
  type: Login
  url: https://paywithmybank.com/merchant-portal/
- group: start
  title: ''
  type: SignUp
  url: https://www.trustly.com/contact-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trustly.com/about-us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trustly.com/about-us/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trustly.net/
- group: auth
  title: ''
  type: Security
  url: https://www.trustly.com/security/disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://www.trustly.com/security
- group: company
  title: ''
  type: Careers
  url: https://www.trustly.com/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trustly/
- group: other
  title: ''
  type: X
  url: https://x.com/Trustly
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/TrustlySE
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/packages/trustly-packages.yml
  title: ''
  type: Packages
  url: packages/trustly-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/packages/trustly-packages.yml
  title: ''
  type: SDKs
  url: packages/trustly-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/well-known/trustly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/trustly-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/well-known/trustly-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/trustly-api-catalog.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/conformance/trustly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trustly-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/conformance/trustly-conformance.yml
  title: ''
  type: Compliance
  url: conformance/trustly-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/lifecycle/trustly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trustly-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/lifecycle/trustly-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/trustly-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/rate-limits/trustly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trustly-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/plans/trustly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trustly-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/components/trustly-components.yml
  title: ''
  type: Components
  url: components/trustly-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/conventions/trustly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trustly-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/conventions/trustly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/trustly-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/errors/trustly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trustly-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/llms/trustly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trustly-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/mcp/trustly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/trustly-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/asyncapi/trustly-north-america-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/trustly-north-america-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/sandbox/trustly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/trustly-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/data-model/trustly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trustly-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/security/trustly-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/trustly-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trustly/refs/heads/main/overlays/trustly-north-america-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trustly-north-america-overlay.yaml
created: '2026-09-18'
description: Trustly is a Pay by Bank payments company operating two developer surfaces. Trustly Europe (Trustly Group AB, Stockholm, a licensed Swedish payment institution) exposes a JSON-RPC 1.1 API at api.trustly.com for deposits, withdrawals/payouts, refunds, account tokenisation (SelectAccount/RegisterAccount), recurring direct debit (Autogiro, BACS, SEPA), local methods (Swish, iDEAL, MB Way, Bancontact) and settlement/ledger reporting, with RSA-signed requests and notifications. Trustly North America (Trustly Inc., formerly PayWithMyBank) exposes a REST API at trustly.one/api/v1 for establishing and authorizing bank transactions, capture, deposit, payout, refund, account verification and tokenization, Trustly ID identity data and event-notification webhooks, documented with a public OpenAPI 3.1, an llms.txt and a hosted MCP docs server.
image: https://cdn.prod.website-files.com/6798a4db9ed2b5ffc8c81f32/67efd2d42cacfccbc8be80ed_OG%20Image.jpg
layout: provider
mcp_servers:
- description: ''
  name: Trustly Group MCP Server
  slug: trustly-group-mcp-server
- description: Hosted MCP server advertised in the Trustly North America llms.txt ("For AI client integration (Claude Code, Cursor, etc.), connect to the MCP server at https://amer.developers.trustly.com/_mcp/server
  name: Trustly North America docs MCP server
  slug: trustly-north-america-docs-mcp-server
modified: '2026-09-18'
name: Trustly Group
nav: Providers
network: true
overview: 'Trustly Group publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Trustly North America API, and 1 more. Tagged areas include Company, Payments, Pay by Bank, Open Banking, and Account-to-Account.


  The Trustly Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trustly Group''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 41 more developer resources.'
plans:
- name: Trustly Plans Pricing
  plan_count: 0
  slug: trustly-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Trustly Rate Limits
  slug: trustly-rate-limits
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 60.1
    developer_ergonomics: 82.7
    discoverability: 85.0
    operational_transparency: 44.7
  previous_composite: 70.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 61.1
security:
- kind: authentication
  name: Trustly Authentication
  slug: trustly-authentication
  summary_line: http/signature · 5 schemes
- kind: domain-security
  name: Trustly Domain Security
  slug: trustly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trustly Vulnerability Disclosure
  slug: trustly-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Trustly Trust Center
  slug: trustly-trust-center
  summary_line: ISO 27001, GDPR
slug: trustly
tags:
- Company
- Payments
- Pay by Bank
- Open Banking
- Account-to-Account
- Payouts
- Direct Debit
- Bank Account Verification
- Identity Verification
- Fintech
- Webhook
- MCP
website: https://www.trustly.com/
---
