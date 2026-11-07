---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Statute-cited remote online notarization requirements for all 50 U.S. states and the District of Columbia: effective date, notary fee cap, identity-verification standard, record-retention period, sign'
  name: Remote online notarization requirements by U.S. jurisdiction
  slug: ron-laws-dataset
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Room-level, hash-chained, KMS-sealed evidence manifests.
  name: SignSealShip Partner API Closing Passports API
  slug: signsealship-closing-passports-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Verified Closing Rooms — one shareable page per transaction.
  name: SignSealShip Partner API Closing Rooms API
  slug: signsealship-closing-rooms-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Your workspace's go-live checklist and tenant-scoped analytics.
  name: SignSealShip Partner API Launchpad & Analytics API
  slug: signsealship-launchpad-analytics-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Request partner API access.
  name: SignSealShip Partner API Onboarding API
  slug: signsealship-onboarding-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: B2B order intake — create sign / notarize / ship orders, track them, and mint Stripe hosted checkout.
  name: SignSealShip Partner API Orders API
  slug: signsealship-orders-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Seal and verify a single executed PDF.
  name: SignSealShip Partner API Proof Passport API
  slug: signsealship-proof-passport-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Deterministic lifecycle simulation for TEST orders (sss_pk_test_ keys) — real state machine, real signed webhooks, no live money.
  name: SignSealShip Partner API Sandbox API
  slug: signsealship-sandbox-api
- baseURL: https://signsealship.com
  baseurl_source: spec
  description: Signed event delivery and subscription management.
  name: SignSealShip Partner API Webhooks API
  slug: signsealship-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Signsealship Webhooks
  slug: signsealship-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/signsealship/rate-limits/signsealship-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/signsealship-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/signsealship/capabilities/signsealship-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/signsealship-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://sign-seal-ship.main-kill-isr.mintlify.me/mcp
- group: other
  href: https://artifacts.apis.io/signsealship/overlays/signsealship-partner-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/signsealship-partner-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/signsealship/mcp/signsealship-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/signsealship-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.signsealship.com/
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
  href: https://artifacts.apis.io/signsealship/changelog/signsealship-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/signsealship-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/signsealship/plans/signsealship-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/signsealship-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/signsealship/packages/signsealship-packages.yml
  title: ''
  type: Packages
  url: packages/signsealship-packages.yml
- group: agent
  href: https://artifacts.apis.io/signsealship/well-known/signsealship-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/signsealship-well-known.yml
- group: other
  href: https://artifacts.apis.io/signsealship/well-known/signsealship-apis.json
  title: ''
  type: APIsJSON
  url: well-known/signsealship-apis.json
- group: agent
  href: https://artifacts.apis.io/signsealship/llms/signsealship-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/signsealship-llms.txt
- group: other
  href: https://artifacts.apis.io/signsealship/a2a/signsealship-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/signsealship-a2a.yml
- group: agent
  href: https://artifacts.apis.io/signsealship/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/signsealship/conformance/signsealship-conformance.yml
  title: ''
  type: Conformance
  url: conformance/signsealship-conformance.yml
- group: auth
  href: https://artifacts.apis.io/signsealship/security/signsealship-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/signsealship-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/signsealship/security/signsealship-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/signsealship-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signsealship/security/signsealship-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/signsealship-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/signsealship/security/signsealship-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/signsealship-trust-center.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://signsealship.com/security
created: '2026-08-31'
description: E-signature, remote online notarization coordination, document verification and physical delivery in one workflow. The API covers onboarding, orders, closing rooms, closing passports, proof passports, webhooks and a sandbox. Also indexes a free CC BY 4.0 dataset of remote online notarization requirements for all 51 U.S. jurisdictions.
finops:
- has_sources: true
  method: derived
  name: Signsealship Finops
  primary_unit: ''
  service_category: ''
  slug: signsealship-finops
  template: true
image: https://signsealship.com/brand/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: SignSealShip Partner API MCP Server
  slug: mcp
modified: '2026-09-01'
name: SignSealShip Partner API
nav: Providers
network: true
overview: 'SignSealShip Partner API publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Closing Passports API, Closing Rooms API, Launchpad & Analytics API, and 6 more. Tagged areas include Notarization, Remote Online Notarization, E-Signature, Document Verification, and Legal Tech.


  The SignSealShip Partner API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SignSealShip Partner API''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, changelog, and 26 more developer resources.'
plans:
- name: Signsealship Plans Pricing
  plan_count: 4
  slug: signsealship-plans-pricing
- name: Signsealship Price Estimates
  plan_count: 0
  slug: signsealship-price-estimates
random_paper: 18
rate_limits:
- limit_count: 5
  name: Signsealship Rate Limits
  slug: signsealship-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: SignSealShip Partner API API Rules
  rule_count: 61
  severity_counts:
    error: 48
    hint: 0
    info: 2
    warn: 11
  slug: signsealship-rules
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.5
    catalog_earned_first_party: 24.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 66.3
    developer_ergonomics: 68.3
    discoverability: 68.3
    operational_transparency: 86.8
  previous_composite: 68.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/signsealship/signsealship-2026-09-02T155438.png
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
skill_count: 4
skills:
- name: place-and-track-an-order
  slug: signsealship-place-and-track-an-order
- name: run-a-verified-closing
  slug: signsealship-run-a-verified-closing
- name: seal-and-verify-a-document
  slug: signsealship-seal-and-verify-a-document
- name: Sign
  slug: signsealship-sign-skill
slug: signsealship
tags:
- Notarization
- Remote Online Notarization
- E-Signature
- Document Verification
- Legal Tech
- Real Estate
- Title and Escrow
- Shipping
- A2A
website: https://www.signsealship.com/
---
