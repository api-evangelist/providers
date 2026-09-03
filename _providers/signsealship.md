---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Create and track orders that combine e-signature, remote online notarization and tracked delivery. 35 documented paths across Onboarding, Orders, Sandbox, Closing Rooms, Closing Passports, Proof Passp
  name: SignSealShip Partner API
  slug: partner-api
- description: 'Statute-cited remote online notarization requirements for all 50 U.S. states and the District of Columbia: effective date, notary fee cap, identity-verification standard, record-retention period, sign'
  name: Remote online notarization requirements by U.S. jurisdiction
  slug: ron-laws-dataset
artifact_total: 11
asyncapis:
- description: ''
  name: Signsealship Webhooks
  slug: signsealship-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signsealship.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signsealship.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.signsealship.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.signsealship.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://signsealship.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://signsealship.com/faq
- group: start
  title: ''
  type: Login
  url: https://signsealship.com/login
- group: start
  title: ''
  type: SignUp
  url: https://signsealship.com/partner
- group: commercial
  title: ''
  type: Pricing
  url: https://signsealship.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signsealship.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signsealship.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://signsealship.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.signsealship.com/changelog/overview
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/signsealship-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/signsealship-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/signsealship-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signsealship-well-known.yml
- group: other
  title: ''
  type: APIsJSON
  url: well-known/signsealship-apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signsealship-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/signsealship-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/signsealship-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signsealship-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signsealship-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/signsealship-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signsealship-trust-center.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://signsealship.com/security
created: '2026-08-31'
description: E-signature, remote online notarization coordination, document verification and physical delivery in one workflow. The API covers onboarding, orders, closing rooms, closing passports, proof passports, webhooks and a sandbox. Also indexes a free CC BY 4.0 dataset of remote online notarization requirements for all 51 U.S. jurisdictions.
image: https://signsealship.com/brand/icon-512.png
layout: provider
mcp_servers:
- description: 'Mintlify DOCUMENTATION-SEARCH MCP on a mintlify.me preview host -- not the Partner API and not a first-party host. Answers initialize with 200. Declared in docs.signsealship.com/.well-known/mcp.json, '
  name: SignSealShip Partner API MCP Server
  slug: signsealship-partner-api-mcp-server
- description: 'Probed profile of the declared MCP server, including the required deployment block (mode: remote, auth: none, verified: probed).'
  name: SignSealShip Partner API MCP Server
  slug: signsealship-partner-api-mcp-server-2
modified: '2026-09-01'
name: SignSealShip Partner API
nav: Providers
network: true
overview: 'SignSealShip Partner API publishes 1 API on the [APIs.io](https://apis.io/) network: SignSealShip Partner API. Tagged areas include notarization, remote online notarization, electronic signature, document verification, and legal technology.


  The SignSealShip Partner API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SignSealShip Partner API''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, changelog, and 20 more developer resources.'
plans:
- name: Signsealship Plans Pricing
  plan_count: 4
  slug: signsealship-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Signsealship Rate Limits
  slug: signsealship-rate-limits
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 57.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 48.1
    developer_ergonomics: 69.0
    discoverability: 70.4
    governance: 4.5
    operational_transparency: 86.8
  previous_composite: 61.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signsealship/refs/heads/main/screenshots/signsealship-2026-09-02T155438.png
security:
- kind: authentication
  name: Signsealship Authentication
  slug: signsealship-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Signsealship Domain Security
  slug: signsealship-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Signsealship Vulnerability Disclosure
  slug: signsealship-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Signsealship Trust Center
  slug: signsealship-trust-center
  summary_line: count, named, note
slug: signsealship
tags:
- notarization
- remote online notarization
- electronic signature
- document verification
- legal technology
- real estate
- title and escrow
- shipping
website: https://signsealship.com/developers
---
