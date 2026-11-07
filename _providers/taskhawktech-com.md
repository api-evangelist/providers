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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Hosted Streamable HTTP MCP server (protocol 2025-03-26, FastMCP, server version 0.4.1) at https://governance.taskhawktech.com/mcp/ exposing 9 tools (verify, attest, bind, verify-outcome, bundle, healt
  name: Kevros MCP Server
  slug: kevros-mcp-server
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: Payment surface discovery for clients before attempting a paid call. 1. `GET /payment/health` - rail challenge and configuration status. 2. `GET /payment/quote?endpoint=/path` - per-endpoint price acr
  name: TaskHawk Systems Billing API
  phrasing_intents:
  - id: getPaymentDiscovery
    intent: Get payment rail status and all endpoint prices
    question: Can I get rail health and the price of every paid endpoint in one call?
  - id: headPaymentDiscovery
    intent: Check payment discovery headers without a body
    question: Can I send a HEAD request to the payment discovery endpoint to see if pricing changed?
  - id: getPaymentBadge
    intent: Get a compact payment rail status badge
    question: Is there a Shields.io badge showing how many payment rails are configured?
  - id: headPaymentBadge
    intent: Check the payment badge headers without a body
    question: Can I HEAD the payment badge endpoint to confirm it is reachable?
  - id: getPaymentQuote
    intent: Get the per-rail price for one endpoint
    question: How much will a single call to a specific paid endpoint cost on each rail?
  - id: getPaymentHealth
    intent: Check payment health headers without a body
    question: Can I send a HEAD request to payment health just to see if it responds?
  - id: getPaymentHealth
    intent: Check which payment rails are configured
    question: Which payment rails are enabled right now, and why are any disabled?
  phrasing_ops: 7
  slug: taskhawktech-com-billing-api
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: 'Public governance operations: verify, attest, bind, verify-outcome, and bundle. Successful operations return endpoint-specific evidence; provenance-capable operations append audit records.'
  name: TaskHawk Systems Governance API
  phrasing_intents:
  - id: verify-action
    intent: Check a proposed agent action against policy
    question: How do I check whether an agent's proposed action is allowed by policy before it runs?
  - id: attest-action
    intent: Record a provenance attestation for an agent action
    question: How do I log what my agent did into a tamper-evident, hash-chained record?
  - id: bind-intent
    intent: Bind a declared intent to an agent command
    question: How can I prove a command was issued in service of a specific declared intent?
  - id: verify-outcome
    intent: Confirm an executed action met its declared intent
    question: How do I check that an action my agent already executed actually achieved its intent?
  - id: generate-bundle
    intent: Generate a compliance evidence bundle for an agent
    question: How do I export certifier-grade compliance evidence for one of my agents?
  - id: mpp-create-session
    intent: Open a governed streaming payment session
    question: How do I let an agent stream payments within a fixed budget and time window?
  - id: mpp-heartbeat
    intent: Report mid-session spend for a drift check
    question: How do I check an active payment session for budget overruns or unauthorized services?
  - id: mpp-close-session
    intent: Close a streaming payment session
    question: How do I end a streaming payment session and seal its provenance record?
  phrasing_ops: 8
  slug: taskhawktech-com-governance-api
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: The media API from TaskHawk Systems — 7 operation(s) for media.
  name: TaskHawk Systems Media API
  phrasing_intents:
  - id: media_capabilities_media_capabilities_get
    intent: Get the media authority's capabilities
    question: What can the media attestation service do, in machine-readable form?
  - id: media_verify_tool_media_verify_get
    intent: Open the browser media verifier page
    question: Is there a web page where a person can verify a media file without uploading it?
  - id: verify_media_media_verify_post
    intent: Verify a media file hash against its certificate
    question: How do I check that a file's hash matches its attestation certificate?
  - id: media_certificate_status_media_status__certificate_id__get
    intent: Check a media certificate's lifecycle status
    question: Has a media certificate been approved, denied or revoked?
  - id: approve_media_certificate_media_approve__certificate_id__post
    intent: Approve or deny a certificate for campaign use
    question: How do I approve an attested asset for use in a brand campaign?
  - id: revoke_media_certificate_media_revoke__certificate_id__post
    intent: Revoke a media attestation certificate
    question: How do I revoke a media certificate that should no longer be trusted?
  - id: attest_media_media_attest_post
    intent: Attest a media file's integrity by its hash
    question: How do I get a signed certificate proving a photo or video hasn't been altered?
  - id: lookup_certificate_media_verify__certificate_id__get
    intent: Look up a full media attestation certificate
    question: How do I retrieve the full attestation certificate for independent verification?
  phrasing_ops: 8
  slug: taskhawktech-com-media-api
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: 'Prompt injection detection. DeBERTa-v3 classifier with sub-second inference. Trial allowance: 10 scans/day per IP.'
  name: TaskHawk Systems Shield API
  phrasing_intents:
  - id: shield-scan
    intent: Scan a prompt for injection attacks (paid)
    question: How do I check a prompt for injection attacks with my API key?
  - id: shield-scan-free
    intent: Scan a prompt for injection attacks for free
    question: Is there a free prompt injection scan I can use without signing up?
  phrasing_ops: 2
  slug: taskhawktech-com-shield-api
- baseURL: https://governance.taskhawktech.com
  baseurl_source: declared
  description: Self-serve API key provisioning. No email or credit card required. 1,000-call trial allowance.
  name: TaskHawk Systems Signup API
  phrasing_intents:
  - id: signup
    intent: Get a trial API key for an agent
    question: How do I get a trial API key without a credit card or email?
  phrasing_ops: 1
  slug: taskhawktech-com-signup-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/taskhawktech-com/capabilities/taskhawktech-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/taskhawktech-com-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://taskhawktech.com/
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/security/taskhawktech-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/taskhawktech-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/security/taskhawktech-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/taskhawktech-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/authentication/taskhawktech-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/taskhawktech-com-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://governance.taskhawktech.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://governance.taskhawktech.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://governance.taskhawktech.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://governance.taskhawktech.com/for-agents.txt
- group: operate
  title: ''
  type: Support
  url: https://taskhawktech.com/legal/support
- group: commercial
  title: ''
  type: Pricing
  url: https://taskhawktech.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://governance.taskhawktech.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taskhawktech.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taskhawktech.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://governance.taskhawktech.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://taskhawktech.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taskhawk-systems
- group: agent
  href: https://artifacts.apis.io/taskhawktech-com/llms/taskhawktech-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/taskhawktech-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://taskhawktech.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/taskhawktech-com/mcp/taskhawktech-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/taskhawktech-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/taskhawktech-com/a2a/taskhawktech-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/taskhawktech-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/taskhawktech-com/well-known/taskhawktech-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/taskhawktech-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/well-known/taskhawktech-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/taskhawktech-com-security.txt
- group: build
  href: https://artifacts.apis.io/taskhawktech-com/packages/taskhawktech-com-packages.yml
  title: ''
  type: Packages
  url: packages/taskhawktech-com-packages.yml
- group: build
  href: https://artifacts.apis.io/taskhawktech-com/packages/taskhawktech-com-packages.yml
  title: ''
  type: SDKs
  url: packages/taskhawktech-com-packages.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/conformance/taskhawktech-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/taskhawktech-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/conformance/taskhawktech-com-conformance.yml
  title: ''
  type: Compliance
  url: conformance/taskhawktech-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/errors/taskhawktech-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/taskhawktech-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/lifecycle/taskhawktech-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/taskhawktech-com-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/scopes/taskhawktech-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/taskhawktech-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/conventions/taskhawktech-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/taskhawktech-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/conventions/taskhawktech-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/taskhawktech-com-conventions.yml
- group: operate
  href: https://artifacts.apis.io/taskhawktech-com/changelog/taskhawktech-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/taskhawktech-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/taskhawktech-com/data-model/taskhawktech-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/taskhawktech-com-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/taskhawktech-com/plans/taskhawktech-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/taskhawktech-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/taskhawktech-com/rate-limits/taskhawktech-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/taskhawktech-com-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/taskhawktech-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/taskhawktech-com/security/taskhawktech-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/taskhawktech-com-vulnerability-disclosure.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://taskhawktech.com/legal/privacy
- group: build
  href: https://artifacts.apis.io/taskhawktech-com/mcp/taskhawktech-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/taskhawktech-com-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/taskhawktech-com/overlays/taskhawktech-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/taskhawktech-com-openapi-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/taskhawktech-com/openapi/taskhawktech-com-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/taskhawktech-com-openapi.yml
created: '2026-09-19'
description: 'TaskHawk Systems, LLC (Charlottesville, Virginia) builds operational verification infrastructure for autonomous AI and software systems. Its commercial product, Kevros, is a verified release and evidence gateway: before an agent spends, deploys, sends or actuates, it POSTs the proposed action to the Kevros Governance API and receives a signed ALLOW, CONSTRAIN or DENY decision with a release token, recorded in a hash-chained, post-quantum-signed provenance ledger. The gateway at governance.taskhawktech.com publishes an OpenAPI 3.1 contract (23 operations: verify, attest, bind, verify-outcome, bundle, prompt-injection shield scan, media hash attestation, MPP payment sessions), a hosted Streamable HTTP MCP server with 9 tools, an A2A agent card, RFC 8414 authorization-server metadata, and per-call machine payment discovery over x402 (USDC on Base), L402 (Lightning) and MPP (Stripe) rails with a 1,000-call trial allowance via POST /signup.'
finops:
- has_sources: true
  method: derived
  name: Taskhawktech Com Finops
  primary_unit: subscription
  service_category: ''
  slug: taskhawktech-com-finops
  template: false
image: https://taskhawktech.com/assets/brand/wordmark-light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at governance.taskhawktech.com over streamable HTTP requiring an API key; 9 tools listed.
  name: TaskHawk Systems MCP Server
  slug: kevros-governance-api
modified: '2026-09-19'
name: TaskHawk Systems
nav: Providers
network: true
overview: 'TaskHawk Systems publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Governance API, Media API, and 3 more. Tagged areas include AI Governance, Agent Security, Runtime Enforcement, Policy Enforcement, and Provenance.


  The TaskHawk Systems catalog on APIs.io includes 1 Spectral governance ruleset.


  TaskHawk Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Taskhawktech Com Plans Pricing
  plan_count: 4
  slug: taskhawktech-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Taskhawktech Com Rate Limits
  slug: taskhawktech-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: TaskHawk Systems API Rules
  rule_count: 70
  severity_counts:
    error: 61
    hint: 0
    info: 5
    warn: 4
  slug: taskhawktech-com-rules
scopes:
- name: Taskhawktech Com Scopes
  scope_count: 7
  slug: taskhawktech-com-scopes
  summary_line: 7 scopes
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 69.7
    contract_governance: 31.8
    contract_quality: 55.3
    developer_ergonomics: 42.3
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 72.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/taskhawktech-com/taskhawktech-com-2026-10-11T130651.png
security:
- kind: authentication
  name: Taskhawktech Com Authentication
  slug: taskhawktech-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Taskhawktech Com Domain Security
  slug: taskhawktech-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Taskhawktech Com Vulnerability Disclosure
  slug: taskhawktech-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Bind an intent, verify its outcome, export the evidence
  slug: taskhawktech-com-bind-intent-and-audit
- name: Issue and verify a media authority certificate
  slug: taskhawktech-com-media-attest-and-verify
- name: Verify an action before executing it
  slug: taskhawktech-com-verify-before-act
slug: taskhawktech-com
tags:
- AI Governance
- Agent Security
- Runtime Enforcement
- Policy Enforcement
- Provenance
- Compliance
- Prompt Injection Detection
- Media Attestation
- Post-Quantum Cryptography
- Formal Verification
- x402
- L402
- Machine Payments
- MCP
- A2A
- Agent-Native
- Government
- Defense
website: https://taskhawktech.com/
---
