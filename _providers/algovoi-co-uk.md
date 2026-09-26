---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 84
  human_in_the_loop: 1
  name: Algovoi Co Uk Agentic Access
  operation_count: 151
  slug: algovoi-co-uk-agentic-access
  summary_line: 151 operations · 84 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://pay.algovoi.co.uk
  baseurl_source: declared
  description: 'Tenant-free, pay-per-call verification rail (OpenAPI 3.1.0 "AlgoVoi Payable Core" 1.0.0, 17 operations). No account and no API key: each paid operation (verify an x402/AP2 receipt JWS, verify an RFC 9'
  name: AlgoVoi Pay (Payable Core) API
  slug: algovoi-pay-payable-core-api
- baseURL: https://api.algovoi.co.uk
  baseurl_source: declared
  description: 'The multi-tenant payment gateway (OpenAPI 3.1.0 "AlgoVoi Gateway" 1.0.0-phase1c, 115 operations, 99 schemas) at api.algovoi.co.uk: hosted checkout links and the checkout lifecycle (QR, build/submit tx'
  name: AlgoVoi Gateway API
  slug: algovoi-gateway-api
- baseURL: https://agents.algovoi.co.uk
  baseurl_source: declared
  description: 'Free, anonymous, verify-only service at agents.algovoi.co.uk (OpenAPI 3.1.0 "AlgoVoi Verifiable-Comms Agent" 0.1.0, 9 operations): verify an RFC 9421 HTTP message signature with RFC 9530 Content-Diges'
  name: AlgoVoi RFC 9421 Clinic (Verifiable-Comms Agent) API
  slug: algovoi-rfc9421-clinic-api
- baseURL: https://agent-trust-bench.algovoi.co.uk
  baseurl_source: declared
  description: 'Open, provider-neutral x402 research surface (OpenAPI 3.1.0 "AlgoVoi Agent Trust Bench" 0.1.0, 7 operations, servers[] https://agent-trust-bench.algovoi.co.uk, MIT): GET /{profile_id} presents one of '
  name: AlgoVoi Agent Trust Bench API
  slug: algovoi-agent-trust-bench-api
- baseURL: https://verify.algovoi.co.uk
  baseurl_source: declared
  description: 'Stateless reference verifier for AlgoVoi selective-disclosure audit bundles at verify.algovoi.co.uk (OpenAPI 3.1.0 "AlgoVoi Audit Verifier" 0.1.0, 3 operations): POST /verify checks a bundle in memory'
  name: AlgoVoi Audit Verifier API
  slug: algovoi-audit-verifier-api
- baseURL: https://agents.algovoi.co.uk/mcp
  baseurl_source: declared
  description: Model Context Protocol access to AlgoVoi three ways. A hosted anonymous Streamable HTTP endpoint at https://agents.algovoi.co.uk/mcp (algovoi-mcp-server 1.29.0, protocol 2025-06-18; tools/list returns
  name: AlgoVoi MCP Server
  slug: algovoi-mcp-server
artifact_total: 16
asyncapis:
- description: ''
  name: Algovoi Co Uk Webhooks
  slug: algovoi-co-uk-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/security/algovoi-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algovoi-co-uk-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/agentic-access/algovoi-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/algovoi-co-uk-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://algovoi.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.algovoi.co.uk
- group: docs
  title: ''
  type: Documentation
  url: https://docs.algovoi.co.uk/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.algovoi.co.uk/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.algovoi.co.uk/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.algovoi.co.uk/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chopmob-cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://algovoi.co.uk/pricing.html
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.algovoi.co.uk/trial-and-pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.algovoi.co.uk/signup
- group: start
  title: ''
  type: Login
  url: https://dash.algovoi.co.uk
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algovoi.co.uk/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://algovoi.co.uk/privacy-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://algovoi.co.uk/compliance.html
- group: auth
  title: ''
  type: Compliance
  url: https://api.algovoi.co.uk/compliance/attestation
- group: auth
  title: ''
  type: Security
  url: https://docs.algovoi.co.uk/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/well-known/algovoi-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algovoi-co-uk-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://algovoi.co.uk/.well-known/security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/security/algovoi-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algovoi-co-uk-vulnerability-disclosure.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/changelog/algovoi-co-uk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/algovoi-co-uk-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.algovoi.co.uk/changelog
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/lifecycle/algovoi-co-uk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/algovoi-co-uk-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/llms/algovoi-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovoi-co-uk-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://algovoi.co.uk/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/llms/algovoi-co-uk-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovoi-co-uk-docs-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.algovoi.co.uk/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/a2a/algovoi-co-uk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/algovoi-co-uk-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/mcp/algovoi-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/algovoi-co-uk-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/mcp/algovoi-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/algovoi-co-uk-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/well-known/algovoi-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algovoi-co-uk-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://docs.algovoi.co.uk/.well-known/agent-skills/algovoi/skill.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conformance/algovoi-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algovoi-co-uk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/errors/algovoi-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/algovoi-co-uk-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/authentication/algovoi-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algovoi-co-uk-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conventions/algovoi-co-uk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/algovoi-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/conventions/algovoi-co-uk-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/algovoi-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/asyncapi/algovoi-co-uk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/algovoi-co-uk-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/rate-limits/algovoi-co-uk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/algovoi-co-uk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/plans/algovoi-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algovoi-co-uk-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/sandbox/algovoi-co-uk-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/algovoi-co-uk-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/packages/algovoi-co-uk-packages.yml
  title: ''
  type: Packages
  url: packages/algovoi-co-uk-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/packages/algovoi-co-uk-packages.yml
  title: ''
  type: SDKs
  url: packages/algovoi-co-uk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://docs.algovoi.co.uk/integrations/native-sdks
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/components/algovoi-co-uk-components.yml
  title: ''
  type: Components
  url: components/algovoi-co-uk-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/data-model/algovoi-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algovoi-co-uk-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/overlays/algovoi-co-uk-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/algovoi-co-uk-gateway-overlay.yaml
- group: other
  title: ''
  type: Subprocessors
  url: https://docs.algovoi.co.uk/compliance#subprocessors
- group: operate
  title: ''
  type: IncidentNotification
  url: https://docs.algovoi.co.uk/security#incident-response
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://algovoi.co.uk/privacy-policy.html#your-rights
- group: other
  title: ''
  type: AITransparency
  url: https://algovoi.co.uk/run-by-a-secure-agent-workforce.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/algovoi-co-uk/refs/heads/main/regulatory/algovoi-co-uk-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/algovoi-co-uk-regulatory-posture.yml
- group: other
  title: ''
  type: Store
  url: https://api.algovoi.co.uk/suite-store
created: '2026-09-19'
description: 'AlgoVoi (AlgoVoi Ltd, UK; founder Christopher Hopley) builds compliance-aware, offline-verifiable payment and evidence infrastructure for AI agents across twelve mainnet chains, answering all four agent-payment protocols — x402, A2A, MPP and AP2 — from one settlement core. It runs two hosted doors: AlgoVoi Pay at pay.algovoi.co.uk, a tenant-free rail that charges 0.01 USDC per call with no account or API key (payment is the credential) and returns an Ed25519 receipt anyone can verify offline, and the multi-tenant Gateway at api.algovoi.co.uk (Bearer key + X-Tenant-Id, hosted checkout, recurring authorities, sanctions screening, hash-chained audit trail, Stripe-shaped signed webhooks). Around them sit an anonymous RFC 9421 signing clinic reachable over REST, A2A and a hosted MCP server, the Agent Trust Bench (187 adversarial x402 research profiles), an audit-bundle verifier, five OpenAPI 3.1 contracts, A2A agent cards on five hosts, a published Agent Skill, llms.txt on four
  hosts, did:web identities, and a large Apache-2.0 reference layer on npm and PyPI (RFC 9421 signer/verifier, JCS substrate, receipt formats, an MCP server). Self-hosted products (Payment Rails, Verifiable Compliance Suite, post-quantum Reseal and Evidence Auditor) sell on perpetual licences paid in USDC.'
image: https://algovoi.co.uk/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: AlgoVoi MCP Server
  slug: algovoi-mcp-server
- description: ''
  name: MCP endpoint (Streamable HTTP, anonymous)
  slug: mcp-endpoint-streamable-http-anonymous
- description: ''
  name: MCP endpoint (hosted, x402-gated)
  slug: mcp-endpoint-hosted-x402-gated
modified: '2026-09-19'
name: AlgoVoi
nav: Providers
network: true
overview: 'AlgoVoi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Pay (Payable Core) API, Gateway API, RFC 9421 Clinic (Verifiable-Comms Agent) API, and 3 more. Tagged areas include Payments, Agentic Commerce, x402, A2A, and MCP.


  The AlgoVoi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AlgoVoi''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 48 more developer resources.'
plans:
- name: Algovoi Co Uk Plans Pricing
  plan_count: 11
  slug: algovoi-co-uk-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 7
  name: Algovoi Co Uk Rate Limits
  slug: algovoi-co-uk-rate-limits
score:
  band: exemplar
  composite: 67.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 76.2
    discoverability: 90.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 20.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Algovoi Co Uk Authentication
  slug: algovoi-co-uk-authentication
  summary_line: http-bearer/apiKey(header)/payment-as-auth(x402)/payment-as-auth(mpp)/hmac-webhook-signature/session-token/none · 9 schemes
- kind: domain-security
  name: Algovoi Co Uk Domain Security
  slug: algovoi-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Algovoi Co Uk Vulnerability Disclosure
  slug: algovoi-co-uk-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: algovoi-co-uk
tags:
- Payments
- Agentic Commerce
- x402
- A2A
- MCP
- Stablecoins
- Cryptocurrency
- Blockchain
- Compliance
- Digital Signature
- Post-Quantum Cryptography
- Verification
- Fintech
- Agent-Native
- Algorand
- United Kingdom
website: https://algovoi.co.uk/
---
