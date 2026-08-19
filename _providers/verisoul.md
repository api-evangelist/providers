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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Verisoul Agentic Access
  operation_count: 26
  slug: verisoul-agentic-access
  summary_line: 26 operations · 16 acting
api_count: 8
apis:
- description: The Account API from Verisoul — 3 operation(s) for account.
  name: Verisoul Account API
  slug: verisoul-account-api
- description: The Email API from Verisoul — 1 operation(s) for email.
  name: Verisoul Email API
  slug: verisoul-email-api
- description: The Enrollment API from Verisoul — 1 operation(s) for enrollment.
  name: Verisoul Enrollment API
  slug: verisoul-enrollment-api
- description: The List API from Verisoul — 3 operation(s) for list.
  name: Verisoul List API
  slug: verisoul-list-api
- description: The Phone API from Verisoul — 1 operation(s) for phone.
  name: Verisoul Phone API
  slug: verisoul-phone-api
- description: The Public API from Verisoul — 1 operation(s) for public.
  name: Verisoul Public API
  slug: verisoul-public-api
- description: The Session API from Verisoul — 4 operation(s) for session.
  name: Verisoul Session API
  slug: verisoul-session-api
- description: The Verification API from Verisoul — 3 operation(s) for verification.
  name: Verisoul Verification API
  slug: verisoul-verification-api
artifact_total: 24
asyncapis:
- description: Asynchronous results for the Verisoul Email Intelligence API are delivered to your configured endpoint as signed webhooks. When an email submitted via POST /email (or the batch endpoint) finishes anal
  name: Verisoul Email Intelligence Webhooks
  slug: verisoul-email-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Verisoul Account API
  slug: open-verisoul-account-api
- collection_type: open
  name: Verisoul Account Email API
  slug: open-verisoul-email-api
- collection_type: open
  name: Verisoul Account Enrollment API
  slug: open-verisoul-enrollment-api
- collection_type: open
  name: Verisoul Account List API
  slug: open-verisoul-list-api
- collection_type: open
  name: Verisoul Account Phone API
  slug: open-verisoul-phone-api
- collection_type: open
  name: Verisoul Account Public API
  slug: open-verisoul-public-api
- collection_type: open
  name: Verisoul Account Session API
  slug: open-verisoul-session-api
- collection_type: open
  name: Verisoul Account Verification API
  slug: open-verisoul-verification-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/verisoul-account-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verisoul-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.verisoul.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.verisoul.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.verisoul.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.verisoul.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.verisoul.ai/integration/overview
- group: operate
  title: ''
  type: Support
  url: mailto:support@verisoul.ai
- group: company
  title: ''
  type: Blog
  url: https://www.verisoul.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/verisoul
- group: commercial
  title: ''
  type: Pricing
  url: https://www.verisoul.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.verisoul.ai
- group: start
  title: ''
  type: Login
  url: https://dashboard.verisoul.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.verisoul.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.verisoul.ai/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.verisoul.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/verisoul-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verisoul-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verisoul-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/verisoul-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verisoul-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/verisoul-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verisoul-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.verisoul.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/verisoul-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verisoul-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/verisoul-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verisoul-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verisoul-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verisoul-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/verisoul-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/verisoul-packages.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/verisoul-email-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/verisoul-email-asyncapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verisoul-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Verisoul is a fake-account and fraud detection platform that helps businesses stop bots, fake signups, and multi-accounting. It combines device fingerprinting, network and location signals, bot detection, email intelligence (risk, deliverability, breach, and identity signals), phone validation, and account linking with an automated rules engine and ML models. Verisoul also offers hosted identity verification products — Face Match (liveness/selfie dedup) and ID Check (government-ID document verification) — and manages biometric capture, consent, and retention on the customer's behalf. It exposes a REST API (Account, Session, Lists, Phone, Email Intelligence, Face Match, ID Check) authenticated with an x-api-key header, plus web and mobile SDKs and signed webhooks. Verisoul is backed by 500 Global.
image: https://cdn.prod.website-files.com/6627605478f226ce86d5c27f/6a5790e9790a84c9ea0498ca_verisoul-logo_og-meta-preview.png
layout: provider
mcp_servers:
- description: ''
  name: verisoul-mcp.yml
  slug: verisoul-mcpyml
modified: '2026-07-21'
name: Verisoul
nav: Providers
network: true
overview: 'Verisoul publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Email API, Enrollment API, and 5 more. Tagged areas include Company, Fraud Detection, Identity Verification, Fake Account Detection, and Device Fingerprinting.


  The Verisoul catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Verisoul''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 144
rate_limits:
- limit_count: 0
  name: Verisoul Rate Limits
  slug: verisoul-rate-limits
score:
  band: developing
  composite: 51.3
  delta: -4.3
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 16.7
    contract_quality: 62.8
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verisoul/refs/heads/main/screenshots/verisoul-2026-08-17T082730.png
security:
- kind: authentication
  name: Verisoul Authentication
  slug: verisoul-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Verisoul Domain Security
  slug: verisoul-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Verisoul Trust Center
  slug: verisoul-trust-center
  summary_line: trust center published
slug: verisoul
tags:
- Company
- Fraud Detection
- Identity Verification
- Fake Account Detection
- Device Fingerprinting
- Email Intelligence
- Bot Detection
- KYC
- Trust and Safety
- Risk Scoring
website: https://www.verisoul.ai
---
