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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 101
  human_in_the_loop: 6
  name: Moltrust Ch Agentic Access
  operation_count: 257
  slug: moltrust-ch-agentic-access
  summary_line: 257 operations · 101 acting · 6 human-in-the-loop
api_count: 4
apis:
- description: Hosted streamable-HTTP Model Context Protocol server (serverInfo moltrust 1.28.1, protocol 2025-06-18) exposing 53 tools over the MolTrust and MoltGuard APIs - identity and credentials, MoltGuard scor
  name: MolTrust MCP Server
  slug: moltrust-mcp-server
- description: DIF Universal Resolver deployment for the did:moltrust method (and bridged did:moltrust:ext_* identifiers), returning W3C DID Documents at the standard /1.0/identifiers/{did} path. The did:moltrust me
  name: MolTrust DID Universal Resolver
  slug: moltrust-did-universal-resolver
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The A2a API from MolTrust — 2 operation(s) for a2a.
  name: MolTrust A2a API
  slug: moltrust-ch-a2a-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: 'The A2A: JSON-RPC API from MolTrust — 1 operation(s) for a2a: json-rpc.'
  name: 'MolTrust A2A: JSON-RPC API'
  slug: moltrust-ch-a2a-json-rpc-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Aae API from MolTrust — 1 operation(s) for aae.
  name: MolTrust Aae API
  slug: moltrust-ch-aae-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The AAE Enforcement API from MolTrust — 5 operation(s) for aae enforcement.
  name: MolTrust AAE Enforcement API
  slug: moltrust-ch-aae-enforcement-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: AAE permission evaluation
  name: MolTrust Aae Evaluation API
  slug: moltrust-ch-aae-evaluation-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Admin API from MolTrust — 22 operation(s) for admin.
  name: MolTrust Admin API
  slug: moltrust-ch-admin-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Anomaly flag tracking + record
  name: MolTrust Agent Flags API
  slug: moltrust-ch-agent-flags-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Endorsement graph score/neighbours/stats
  name: MolTrust Agent Graph API
  slug: moltrust-ch-agent-graph-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Wallet risk scoring + score-free samples
  name: MolTrust Agent Scoring API
  slug: moltrust-ch-agent-scoring-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Agents API from MolTrust — 4 operation(s) for agents.
  name: MolTrust Agents API
  slug: moltrust-ch-agents-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Anchoring API from MolTrust — 1 operation(s) for anchoring.
  name: MolTrust Anchoring API
  slug: moltrust-ch-anchoring-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Wallet attestation + challenge-response + hackathon
  name: MolTrust Attestation And Hackathon API
  slug: moltrust-ch-attestation-and-hackathon-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Attestations API from MolTrust — 1 operation(s) for attestations.
  name: MolTrust Attestations API
  slug: moltrust-ch-attestations-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Auth API from MolTrust — 5 operation(s) for auth.
  name: MolTrust Auth API
  slug: moltrust-ch-auth-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The AWS Marketplace API from MolTrust — 1 operation(s) for aws marketplace.
  name: MolTrust AWS Marketplace API
  slug: moltrust-ch-aws-marketplace-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Badge API from MolTrust — 1 operation(s) for badge.
  name: MolTrust Badge API
  slug: moltrust-ch-badge-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The billing-admin API from MolTrust — 1 operation(s) for billing-admin.
  name: MolTrust Billing Admin API
  slug: moltrust-ch-billing-admin-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The billing API from MolTrust — 5 operation(s) for billing.
  name: MolTrust Billing API
  slug: moltrust-ch-billing-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The caep API from MolTrust — 3 operation(s) for caep.
  name: MolTrust Caep API
  slug: moltrust-ch-caep-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Compliance API from MolTrust — 4 operation(s) for compliance.
  name: MolTrust Compliance API
  slug: moltrust-ch-compliance-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Contact API from MolTrust — 1 operation(s) for contact.
  name: MolTrust Contact API
  slug: moltrust-ch-contact-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Generic VC issuance + verify
  name: MolTrust Credential Issuance API
  slug: moltrust-ch-credential-issuance-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Credentials API from MolTrust — 3 operation(s) for credentials.
  name: MolTrust Credentials API
  slug: moltrust-ch-credentials-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Credits API from MolTrust — 8 operation(s) for credits.
  name: MolTrust Credits API
  slug: moltrust-ch-credits-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Delegation API from MolTrust — 3 operation(s) for delegation.
  name: MolTrust Delegation API
  slug: moltrust-ch-delegation-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The ExtendedAgentCard API from MolTrust — 1 operation(s) for extendedagentcard.
  name: MolTrust Extended Agent Card API
  slug: moltrust-ch-extendedagentcard-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Health API from MolTrust — 1 operation(s) for health.
  name: MolTrust Health API
  slug: moltrust-ch-health-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Identity API from MolTrust — 28 operation(s) for identity.
  name: MolTrust Identity API
  slug: moltrust-ch-identity-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Interaction API from MolTrust — 1 operation(s) for interaction.
  name: MolTrust Interaction API
  slug: moltrust-ch-interaction-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Join API from MolTrust — 1 operation(s) for join.
  name: MolTrust Join API
  slug: moltrust-ch-join-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Polymarket/Kalshi integrity checks + feed + events
  name: MolTrust Market Integrity API
  slug: moltrust-ch-market-integrity-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Music API from MolTrust — 5 operation(s) for music.
  name: MolTrust Music API
  slug: moltrust-ch-music-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Operators API from MolTrust — 2 operation(s) for operators.
  name: MolTrust Operators API
  slug: moltrust-ch-operators-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Output Provenance Admin API from MolTrust — 4 operation(s) for output provenance admin.
  name: MolTrust Output Provenance Admin API
  slug: moltrust-ch-output-provenance-admin-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Output Provenance API from MolTrust — 7 operation(s) for output provenance.
  name: MolTrust Output Provenance API
  slug: moltrust-ch-output-provenance-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Payment API from MolTrust — 1 operation(s) for payment.
  name: MolTrust Payment API
  slug: moltrust-ch-payment-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Wallet-link + leaderboard + PredictionTrackCredential
  name: MolTrust Prediction Markets API
  slug: moltrust-ch-prediction-markets-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Reputation API from MolTrust — 3 operation(s) for reputation.
  name: MolTrust Reputation API
  slug: moltrust-ch-reputation-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The reseller-admin API from MolTrust — 9 operation(s) for reseller-admin.
  name: MolTrust Reseller Admin API
  slug: moltrust-ch-reseller-admin-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The reseller API from MolTrust — 5 operation(s) for reseller.
  name: MolTrust Reseller API
  slug: moltrust-ch-reseller-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Resolve API from MolTrust — 1 operation(s) for resolve.
  name: MolTrust Resolve API
  slug: moltrust-ch-resolve-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: Brand/Product/Reseller registration + verify
  name: MolTrust Salesguard API
  slug: moltrust-ch-salesguard-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Search API from MolTrust — 1 operation(s) for search.
  name: MolTrust Search API
  slug: moltrust-ch-search-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: BuyerAgentCredential receipt + verify + issue
  name: MolTrust Shopping Vc API
  slug: moltrust-ch-shopping-vc-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Sitemap.xml API from MolTrust — 1 operation(s) for sitemap.xml.
  name: MolTrust Sitemap.xml API
  slug: moltrust-ch-sitemap-xml-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Skill API from MolTrust — 5 operation(s) for skill.
  name: MolTrust Skill API
  slug: moltrust-ch-skill-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: VerifiedSkillCredential audit + issue + verify + anchor
  name: MolTrust Skill Verification API
  slug: moltrust-ch-skill-verification-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Skills API from MolTrust — 1 operation(s) for skills.
  name: MolTrust Skills API
  slug: moltrust-ch-skills-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Sports API from MolTrust — 13 operation(s) for sports.
  name: MolTrust Sports API
  slug: moltrust-ch-sports-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Stats API from MolTrust — 1 operation(s) for stats.
  name: MolTrust Stats API
  slug: moltrust-ch-stats-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Swarm API from MolTrust — 4 operation(s) for swarm.
  name: MolTrust Swarm API
  slug: moltrust-ch-swarm-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: On-chain sybil-cluster detection
  name: MolTrust Sybil Detection API
  slug: moltrust-ch-sybil-detection-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Test Harness API from MolTrust — 1 operation(s) for test harness.
  name: MolTrust Test Harness API
  slug: moltrust-ch-test-harness-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: TrustProof history + health + info
  name: MolTrust Transparency API
  slug: moltrust-ch-transparency-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: TravelAgentCredential trip + verify + issue
  name: MolTrust Travel Vc API
  slug: moltrust-ch-travel-vc-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Trust API from MolTrust — 1 operation(s) for trust.
  name: MolTrust Trust API
  slug: moltrust-ch-trust-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Violation API from MolTrust — 4 operation(s) for violation.
  name: MolTrust Violation API
  slug: moltrust-ch-violation-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Wallet API from MolTrust — 1 operation(s) for wallet.
  name: MolTrust Wallet API
  slug: moltrust-ch-wallet-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The Webhooks API from MolTrust — 1 operation(s) for webhooks.
  name: MolTrust Webhooks API
  slug: moltrust-ch-webhooks-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The .well Known API from MolTrust — 5 operation(s) for .well known.
  name: MolTrust .well Known API
  slug: moltrust-ch-well-known-api
- baseURL: https://api.moltrust.ch
  baseurl_source: declared
  description: The X402 API from MolTrust — 2 operation(s) for x402.
  name: MolTrust X402 API
  slug: moltrust-ch-x402-api
artifact_total: 80
asyncapis:
- description: ''
  name: Moltrust Ch Event Surface
  slug: moltrust-ch-event-surface
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://moltrust.ch/blog/feed.xml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/capabilities/moltrust-ch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moltrust-ch-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/overlays/moltrust-ch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moltrust-ch-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/overlays/moltrust-ch-moltguard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moltrust-ch-moltguard-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/moltrust-ch/agentic-access/moltrust-ch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moltrust-ch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/moltrust-ch/security/moltrust-ch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moltrust-ch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://moltrust.ch/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://moltrust.ch/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://api.moltrust.ch/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.moltrust.ch/redoc
- group: start
  title: ''
  type: GettingStarted
  url: https://moltrust.ch/developers.html
- group: operate
  title: ''
  type: Support
  url: https://moltrust.ch/contact.html
- group: company
  title: ''
  type: Blog
  url: https://moltrust.ch/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MoltyCel
- group: commercial
  title: ''
  type: Pricing
  url: https://moltrust.ch/pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://moltrust.ch/developers.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moltrust.ch/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moltrust.ch/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moltrust.ch/
- group: auth
  title: ''
  type: Compliance
  url: https://moltrust.ch/compliance.html
- group: other
  href: https://artifacts.apis.io/moltrust-ch/a2a/moltrust-ch-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/moltrust-ch-a2a.yml
- group: agent
  href: https://artifacts.apis.io/moltrust-ch/mcp/moltrust-ch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moltrust-ch-mcp.yml
- group: build
  href: https://artifacts.apis.io/moltrust-ch/mcp/moltrust-ch-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/moltrust-ch-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/moltrust-ch/llms/moltrust-ch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moltrust-ch-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://moltrust.ch/llms.txt
- group: agent
  href: https://artifacts.apis.io/moltrust-ch/well-known/moltrust-ch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moltrust-ch-well-known.yml
- group: build
  href: https://artifacts.apis.io/moltrust-ch/packages/moltrust-ch-packages.yml
  title: ''
  type: Packages
  url: packages/moltrust-ch-packages.yml
- group: build
  href: https://artifacts.apis.io/moltrust-ch/packages/moltrust-ch-packages.yml
  title: ''
  type: SDKs
  url: packages/moltrust-ch-packages.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/conventions/moltrust-ch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moltrust-ch-conventions.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/conformance/moltrust-ch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moltrust-ch-conformance.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/errors/moltrust-ch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moltrust-ch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/lifecycle/moltrust-ch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moltrust-ch-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/moltrust-ch/changelog/moltrust-ch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moltrust-ch-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/moltrust-ch/plans/moltrust-ch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moltrust-ch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/moltrust-ch/rate-limits/moltrust-ch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moltrust-ch-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/moltrust-ch/sandbox/moltrust-ch-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moltrust-ch-sandbox.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/components/moltrust-ch-components.yml
  title: ''
  type: Components
  url: components/moltrust-ch-components.yml
- group: design
  href: https://artifacts.apis.io/moltrust-ch/data-model/moltrust-ch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moltrust-ch-data-model.yml
- group: agent
  href: https://artifacts.apis.io/moltrust-ch/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: Subprocessors
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/moltrust-ch/regulatory/moltrust-ch-regulatory-posture.yml
  title: ''
  type: DataResidency
  url: regulatory/moltrust-ch-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/moltrust-ch/security/moltrust-ch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/moltrust-ch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/moltrust-ch/security/moltrust-ch-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/moltrust-ch-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'CryptoKRI GmbH (Zurich, CHE-115.481.407) operates MolTrust, a trust registry for autonomous AI agents: W3C DID identity (did:moltrust, did:web), W3C Verifiable Credential issuance and verification, Agent Authorization Envelopes (AAE, an IETF Internet-Draft) with UCAN delegation and stateless mandate enforcement, behavioural trust scores signed with Ed25519, EU AI Act compliance endpoints (risk classification, Annex V declarations as VCs, Article 73 incidents), ERC-8004 on-chain registration and Merkle-batched evidence anchoring on Base L2. The MoltGuard sub-API adds wallet trust scoring, sybil detection, prediction-market integrity and vertical credentials (shopping, travel, skills, music, sports, brand provenance) paid per call in USDC via x402. Published surfaces: two OpenAPI 3.1 documents, a signed A2A agent card, a hosted MCP server with 53 tools, llms.txt on both hosts, JWKS / DID documents / x402 discovery under /.well-known, npm and PyPI SDKs, and an Upptime status page.'
finops:
- has_sources: true
  method: derived
  name: Moltrust Ch Finops
  primary_unit: active agent
  service_category: ''
  slug: moltrust-ch-finops
  template: false
image: https://moltrust.ch/img/moltrust-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.moltrust.ch over streamable HTTP requiring an API key; 53 tools listed.
  name: MolTrust MCP Server
  slug: moltrust
modified: '2026-10-06'
name: MolTrust
nav: Providers
network: true
overview: 'MolTrust publishes 63 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, A2A: JSON-RPC API, Aae API, and 60 more. Tagged areas include AI Agents, Agent Identity, Decentralized Identity, Verifiable Credentials, and Trust and Safety.


  The MolTrust catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MolTrust''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Moltrust Ch Plans Pricing
  plan_count: 8
  slug: moltrust-ch-plans-pricing
- name: Moltrust Ch Price Estimates
  plan_count: 0
  slug: moltrust-ch-price-estimates
random_paper: 2
rate_limits:
- limit_count: 0
  name: Moltrust Ch Rate Limits
  slug: moltrust-ch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: MolTrust API Rules
  rule_count: 55
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 12
  slug: moltrust-ch-rules
score:
  band: exemplar
  composite: 68.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 53.7
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 44.7
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 23.3
      derived: 0
      marker_coverage: 100.0
      total: 61
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 47.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/moltrust-ch/moltrust-ch-2026-10-11T111216.png
security:
- kind: authentication
  name: Moltrust Ch Authentication
  slug: moltrust-ch-authentication
  summary_line: apiKey/http-bearer (declared, not live)/x402-payment/admin-key (undeclared) · 6 schemes
- kind: domain-security
  name: Moltrust Ch Domain Security
  slug: moltrust-ch-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Moltrust Ch Vulnerability Disclosure
  slug: moltrust-ch-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 6
skills:
- name: Configure an AAE mandate and enforce an action against it
  slug: moltrust-ch-configure-a-mandate-and-enforce-an-action
- name: 'EU AI Act: classify a system, issue an Annex V declaration, record an incident'
  slug: moltrust-ch-eu-ai-act-classify-declare-and-report
- name: Issue and verify a W3C Verifiable Credential
  slug: moltrust-ch-issue-and-verify-a-verifiable-credential
- name: Pay-per-call wallet trust check with x402
  slug: moltrust-ch-pay-per-call-wallet-trust-check-with-x402
- name: Poll CAEP trust-change events and verify signed scores
  slug: moltrust-ch-poll-caep-events-and-verify-signed-scores
- name: Register an agent and read its trust score
  slug: moltrust-ch-register-an-agent-and-read-its-trust-score
slug: moltrust-ch
tags:
- AI Agents
- Agent Identity
- Decentralized Identity
- Verifiable Credentials
- Trust and Safety
- Agent Authorization
- Compliance
- Blockchain
- A2A
- MCP
- x402
- Agent-Native
website: https://moltrust.ch/
---
