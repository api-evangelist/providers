---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Mandateshield Com Agentic Access
  operation_count: 43
  slug: mandateshield-com-agentic-access
  summary_line: 43 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://mandateshield.com
  baseurl_source: spec
  description: 'REST contract for the authority lifecycle: analysis-only v1 preflight, strict v2 challenges and cryptographic verification, execution-authorization transitions, one-use execution permits, provider-sub'
  name: MandateShield Payment Authority API
  slug: payment-authority-api
- description: Hosted, stateless Streamable HTTP MCP server at https://mandateshield.com/api/mcp. Anonymous initialize and tools/list; three tools (check_ai_payment_authority, normalize_agent_payment_protocol, verif
  name: MandateShield MCP Server
  slug: mcp-server
- description: 'JSONRPC A2A interface at https://mandateshield.com/a2a serving A2A 1.0 and 0.3 profiles (selected by the A2A-Version header) with three skills: project agent payment fields, analyze AI payment policy,'
  name: MandateShield Payment Authority Agent (A2A)
  slug: a2a-agent
artifact_total: 14
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/agentic-access/mandateshield-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mandateshield-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/security/mandateshield-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mandateshield-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/security/mandateshield-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mandateshield-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mandateshield.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mandateshield.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://mandateshield.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://mandateshield.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://mandateshield.com/connect
- group: operate
  title: ''
  type: Support
  url: https://mandateshield.com/legal
- group: company
  title: ''
  type: Blog
  url: https://mandateshield.com/resources
- group: company
  title: ''
  type: BlogRSS
  url: https://mandateshield.com/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://mandateshield.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mandateshield.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mandateshield.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mandateshield.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://mandateshield.com/status
- group: auth
  title: ''
  type: Security
  url: https://mandateshield.com/responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/security/mandateshield-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mandateshield-com-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://mandateshield.com/trust
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/llms/mandateshield-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mandateshield-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://mandateshield.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/well-known/mandateshield-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mandateshield-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/well-known/mandateshield-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mandateshield-com-security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/packages/mandateshield-com-packages.yml
  title: ''
  type: Packages
  url: packages/mandateshield-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/packages/mandateshield-com-packages.yml
  title: ''
  type: SDKs
  url: packages/mandateshield-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/cli/mandateshield-com-cli.yml
  title: ''
  type: CLI
  url: cli/mandateshield-com-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/sandbox/mandateshield-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mandateshield-com-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://mandateshield.com/sandbox
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/plans/mandateshield-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mandateshield-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/rate-limits/mandateshield-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mandateshield-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/lifecycle/mandateshield-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mandateshield-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/changelog/mandateshield-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mandateshield-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://mandateshield.com/current-release.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/authentication/mandateshield-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mandateshield-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/conventions/mandateshield-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mandateshield-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/conventions/mandateshield-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mandateshield-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/errors/mandateshield-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mandateshield-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/errors/mandateshield-com-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/mandateshield-com-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/conformance/mandateshield-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mandateshield-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/data-model/mandateshield-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mandateshield-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/overlays/mandateshield-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mandateshield-com-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: SBOM
  url: https://mandateshield.com/evidence/v1.13.0/sbom.spdx.json
- group: other
  title: ''
  type: Subprocessors
  url: https://mandateshield.com/subprocessors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://mandateshield.com/dpa
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://mandateshield.com/privacy
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://mandateshield.com/privacy
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/mandateshield-com/refs/heads/main/regulatory/mandateshield-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/mandateshield-com-regulatory-posture.yml
- group: other
  title: ''
  type: JWKS
  url: https://mandateshield.com/.well-known/jwks.json
created: '2026-09-19'
description: MandateShield is a fail-closed authority-verification and execution-evidence boundary for autonomous AI-agent purchases, operated from Bern, Switzerland. It binds a signed purchase approval (AP2, TAP, UCP, x402, MPP, ACP or a custom envelope) to a registered mandate and a pinned issuer key, reserves cumulative budget atomically, consumes the reservation into a one-use provider-bound execution permit for an exact Stripe PaymentIntent or x402 request, and then checks the provider outcome without trusting the caller before issuing a signed terminal receipt. The hosted service never moves money or holds payment credentials. It publishes an OpenAPI 3.1 contract with 26 operations, a remote MCP server whose tools/list answers anonymously, a signed A2A agent card, llms.txt, an SPDX SBOM, a JWKS, a 91-code reason registry, a 19-vector conformance suite and self-hosted JavaScript, Python and Go clients.
image: https://mandateshield.com/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: MandateShield MCP Server
  slug: mandateshield-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP)
  slug: mcp-endpoint-streamable-http
- description: ''
  name: MCP endpoint, no-auth plugin profile
  slug: mcp-endpoint-no-auth-plugin-profile
- description: ''
  name: MCP registry server.json
  slug: mcp-registry-serverjson
modified: '2026-09-19'
name: MandateShield
nav: Providers
network: true
overview: 'MandateShield publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Payment Authority API, and 2 more. Tagged areas include Company, Payments, Agentic Commerce, AI Agents, and Payment Authorization.


  MandateShield''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 42 more developer resources.'
plans:
- name: Mandateshield Com Plans Pricing
  plan_count: 4
  slug: mandateshield-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Mandateshield Com Rate Limits
  slug: mandateshield-com-rate-limits
score:
  band: exemplar
  composite: 73.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 20.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 80.4
    discoverability: 66.7
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 75.3
  provenance:
    agentic_access: derived
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
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 66.7
security:
- kind: authentication
  name: Mandateshield Com Authentication
  slug: mandateshield-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Mandateshield Com Domain Security
  slug: mandateshield-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mandateshield Com Vulnerability Disclosure
  slug: mandateshield-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Mandateshield Com Trust Center
  slug: mandateshield-com-trust-center
  summary_line: trust center published
slug: mandateshield-com
tags:
- Company
- Payments
- Agentic Commerce
- AI Agents
- Payment Authorization
- Fraud Prevention
- Cryptographic Verification
- MCP
- A2A
- x402
- AP2
- Stripe
- Agent-Native
- Switzerland
website: https://mandateshield.com/
---
