---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Mandateshield Com Agentic Access
  operation_count: 43
  slug: mandateshield-com-agentic-access
  summary_line: 43 operations · 17 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Hosted, stateless Streamable HTTP MCP server at https://mandateshield.com/api/mcp. Anonymous initialize and tools/list; three tools (check_ai_payment_authority, normalize_agent_payment_protocol, verif
  name: MandateShield MCP Server
  slug: mcp-server
- description: 'JSONRPC A2A interface at https://mandateshield.com/a2a serving A2A 1.0 and 0.3 profiles (selected by the A2A-Version header) with three skills: project agent payment fields, analyze AI payment policy,'
  name: MandateShield Payment Authority Agent (A2A)
  slug: a2a-agent
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Hosting-authenticated account-owner emergency control. The interlock governs new MandateShield-mediated strict operations inside one account regardless of provider profile. It cannot stop customer inf
  name: MandateShield Account execution control API
  phrasing_intents:
  - id: getGlobalExecutionInterlock
    intent: Check whether account-wide execution is paused
    question: Is new payment execution on my MandateShield account currently paused or running?
  - id: setGlobalExecutionInterlock
    intent: Pause or resume all new account execution
    question: How do I pause all new agent payment execution across my whole account at once?
  phrasing_ops: 2
  slug: mandateshield-com-account-execution-control-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Privacy-thresholded context. Signals can require REVIEW but do not automatically block.
  name: MandateShield Advisory intelligence API
  phrasing_intents:
  - id: getThreatIntelligence
    intent: Get cross-account threat trends
    question: What protocol and reason-code trends are showing up across other accounts?
  phrasing_ops: 1
  slug: mandateshield-com-advisory-intelligence-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Policy diagnostics that always return enforcement_authorized=false.
  name: MandateShield Analysis only API
  phrasing_intents:
  - id: evaluatePurchase
    intent: Analyze one purchase against mandate policy
    question: How can I check whether an agent's purchase would stay inside its mandate limits before paying?
  - id: evaluatePurchaseBatch
    intent: Analyze up to 25 purchases in one batch
    question: Can I analyze many agent purchases against policy in a single request?
  phrasing_ops: 2
  slug: mandateshield-com-analysis-only-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Signed, account-bound records of an externally bound subject reaching one server-observed strict live reservation and one fresh credential-bound permit redemption. The proof flow submits no payment an
  name: MandateShield Deployment activation proofs API
  phrasing_intents:
  - id: listDeploymentActivationProofs
    intent: List active deployment activation proofs
    question: Which deployments currently have a server-observed activation proof?
  - id: getDeploymentActivationProof
    intent: Get one deployment activation record
    question: What exactly does a single deployment activation proof record attest to?
  - id: getDeploymentActivationProofBadge
    intent: Get an activation-observed badge
    question: How do I get an SVG badge showing a deployment activation was observed?
  phrasing_ops: 3
  slug: mandateshield-com-deployment-activation-proofs-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Deployment Proofs API from MandateShield — 3 operation(s) for deployment proofs.
  name: MandateShield Deployment Proofs API
  phrasing_intents:
  - id: deploymentProofListOptions
    intent: Check CORS for the deployment proofs list
    question: Can a browser app call the deployment proofs list endpoint cross-origin?
  - id: deploymentProofGetOptions
    intent: Check CORS for fetching one deployment proof
    question: Is fetching a single deployment proof allowed from another origin?
  - id: deploymentProofBadgeOptions
    intent: Check CORS for the deployment proof badge
    question: Can I load the deployment proof badge SVG from a different website origin?
  phrasing_ops: 3
  slug: mandateshield-com-deployment-proofs-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Execution Authorizations API from MandateShield — 1 operation(s) for execution authorizations.
  name: MandateShield Execution Authorizations API
  phrasing_intents:
  - id: executionAuthorizationOptions
    intent: Check CORS for execution authorizations
    question: Does the execution authorizations endpoint support cross-origin requests?
  phrasing_ops: 1
  slug: mandateshield-com-execution-authorizations-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Provider-bound permit redemption, caller observation intake, Stripe API or x402 chain reconciliation that does not trust the caller assertion, autonomous terminal authorization finalization and signed
  name: MandateShield Execution evidence API
  phrasing_intents:
  - id: verifyExecutionPermit
    intent: Verify a signed execution permit
    question: How do I check that a provider-bound execution permit's signature and structure are valid?
  - id: redeemExecutionPermit
    intent: Claim an execution permit before provider submission
    question: How does a payment processor atomically claim a one-use execution permit before submitting?
  - id: reportProviderSubmission
    intent: Report a provider payment attempt for reconciliation
    question: How do I report what happened when my processor submitted a payment to the provider?
  - id: receiveStripeProviderWebhook
    intent: Receive a Stripe webhook to trigger reconciliation
    question: Where should Stripe send webhook events so payments get reconciled?
  - id: verifyExecutionReceipt
    intent: Verify a terminal execution receipt
    question: How do I verify a signed receipt proving how a payment execution finally ended?
  phrasing_ops: 5
  slug: mandateshield-com-execution-evidence-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Execution Permits API from MandateShield — 2 operation(s) for execution permits.
  name: MandateShield Execution Permits API
  phrasing_intents:
  - id: executionPermitVerificationOptions
    intent: Check CORS for permit verification
    question: Can a browser call the execution permit verify endpoint cross-origin?
  - id: executionPermitRedemptionOptions
    intent: Check CORS for permit redemption
    question: Does the execution permit redeem endpoint allow cross-origin requests?
  phrasing_ops: 2
  slug: mandateshield-com-execution-permits-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Execution Receipts API from MandateShield — 1 operation(s) for execution receipts.
  name: MandateShield Execution Receipts API
  phrasing_intents:
  - id: executionReceiptVerificationOptions
    intent: Check CORS for execution receipt verification
    question: Can I verify execution receipts from a browser on another origin?
  phrasing_ops: 1
  slug: mandateshield-com-execution-receipts-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Normalize API from MandateShield — 1 operation(s) for normalize.
  name: MandateShield Normalize API
  phrasing_intents:
  - id: normalizeProtocolOptions
    intent: Check CORS for protocol normalization
    question: Can a web app call the payment protocol normalize endpoint cross-origin?
  phrasing_ops: 1
  slug: mandateshield-com-normalize-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Preflight API from MandateShield — 1 operation(s) for preflight.
  name: MandateShield Preflight API
  phrasing_intents:
  - id: preflightOptions
    intent: Check CORS for purchase preflight analysis
    question: Does the purchase preflight analysis endpoint accept cross-origin browser calls?
  phrasing_ops: 1
  slug: mandateshield-com-preflight-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: 'Challenge, strict verification, and processor transitions. The documented eight-field invariant establishes only a RESERVED, consumable authorization; a trusted gateway must obtain the single winning '
  name: MandateShield Production authority API
  phrasing_intents:
  - id: createVerificationChallenge
    intent: Issue a one-time challenge for a mandate
    question: How do I get a fresh one-time nonce before signing purchase authority for a mandate?
  - id: verifyCryptographicAuthority
    intent: Verify signed purchase authority and get a receipt
    question: How do I verify that an agent's signed purchase is authorized under a registered mandate?
  - id: transitionExecutionAuthorization
    intent: Consume, commit, release or expire an authorization
    question: How does my processor consume a reserved authorization and get an execution permit?
  - id: verifyCryptographicAuthorityBatch
    intent: Verify up to 25 purchase authorities at once
    question: Can I run strict signed-authority verification on many purchases in one call?
  phrasing_ops: 4
  slug: mandateshield-com-production-authority-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Proof Network API from MandateShield — 5 operation(s) for proof network.
  name: MandateShield Proof Network API
  phrasing_intents:
  - id: publicProofChallengeOptions
    intent: Check CORS for proof network challenges
    question: Can a browser create proof network challenges from another origin?
  - id: publicProofAttestationOptions
    intent: Check CORS for proof network attestations
    question: Is the proof network attestations endpoint callable cross-origin?
  - id: publicProofListOptions
    intent: Check CORS for the proof list
    question: Can a web page list proof network proofs cross-origin?
  - id: publicProofGetOptions
    intent: Check CORS for one proof network proof
    question: Can I fetch a single proof-network proof from a browser on another domain?
  - id: publicProofBadgeOptions
    intent: Check CORS for a proof network badge
    question: Can other websites load a proof network self-report badge cross-origin?
  phrasing_ops: 5
  slug: mandateshield-com-proof-network-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Stateless documented-field projection for supported agent-payment inputs. X402 and MPP require a canonical payee identity whose rail-specific fields exactly match the source. A successful projection i
  name: MandateShield Protocol adapters API
  phrasing_intents:
  - id: normalizeAgentPaymentProtocol
    intent: Normalize AP2, x402 or MPP payment fields
    question: How do I convert an x402 PAYMENT-REQUIRED payload into a standard purchase envelope?
  phrasing_ops: 1
  slug: mandateshield-com-protocol-adapters-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Provider Submissions API from MandateShield — 1 operation(s) for provider submissions.
  name: MandateShield Provider Submissions API
  phrasing_intents:
  - id: providerSubmissionOptions
    intent: Check CORS for provider submissions
    question: Does the provider submissions endpoint accept cross-origin requests?
  phrasing_ops: 1
  slug: mandateshield-com-provider-submissions-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Signed externally bound self-reports. MandateShield verifies domain or exact GitHub-commit binding and claimant-report integrity; it does not run the claimant implementation, independently verify conf
  name: MandateShield Public proof network API
  phrasing_intents:
  - id: createPublicProofChallenge
    intent: Create a subject-binding proof challenge
    question: How do I get a DNS TXT or GitHub commit challenge to bind my conformance self-report to my domain?
  - id: issuePublicProofAttestation
    intent: Bind and sign a self-report attestation
    question: Once my DNS TXT record or GitHub binding is in place, how do I get the signed self-report attestation?
  - id: listPublicProofAttestations
    intent: List published self-report proofs
    question: Which externally bound self-report proofs have been published?
  - id: getPublicProofAttestation
    intent: Get one signed self-report proof
    question: Can I see the full claimant report and subject binding behind a published proof?
  - id: getPublicProofBadge
    intent: Get a self-report proof badge
    question: How do I embed an externally bound self-report badge on my site?
  phrasing_ops: 5
  slug: mandateshield-com-public-proof-network-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Zero-account, test-only and request-local lifecycle simulation. It uses ephemeral keys, contacts no external provider or independent organization, retains no lifecycle state and moves no money.
  name: MandateShield Public sandbox API
  slug: mandateshield-com-public-sandbox-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: Public-key signed-receipt verification and privacy-safe issuance lookup.
  name: MandateShield Receipts API
  phrasing_intents:
  - id: verifyDecisionReceipt
    intent: Verify a portable decision receipt
    question: How do I check that a MandateShield decision receipt's signature is genuine?
  - id: getReceiptTransparency
    intent: Look up a receipt's transparency record
    question: Where can I find the public transparency record for an issued receipt?
  phrasing_ops: 2
  slug: mandateshield-com-receipts-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Sandbox API from MandateShield — 1 operation(s) for sandbox.
  name: MandateShield Sandbox API
  slug: mandateshield-com-sandbox-api
- baseURL: https://mandateshield.com/api/mcp
  baseurl_source: declared
  description: The Verify API from MandateShield — 1 operation(s) for verify.
  name: MandateShield Verify API
  phrasing_intents:
  - id: verifyOptions
    intent: Check CORS for strict authority verification
    question: Can I call the v2 verify endpoint from a browser on another origin?
  phrasing_ops: 1
  slug: mandateshield-com-verify-api
artifact_total: 39
common:
- group: other
  href: https://artifacts.apis.io/mandateshield-com/capabilities/mandateshield-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mandateshield-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mandateshield-com/agentic-access/mandateshield-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mandateshield-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mandateshield-com/security/mandateshield-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mandateshield-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mandateshield-com/security/mandateshield-com-domain-security.yml
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
  href: https://artifacts.apis.io/mandateshield-com/security/mandateshield-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/mandateshield-com-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://mandateshield.com/trust
- group: agent
  href: https://artifacts.apis.io/mandateshield-com/llms/mandateshield-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mandateshield-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://mandateshield.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/mandateshield-com/well-known/mandateshield-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mandateshield-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/mandateshield-com/well-known/mandateshield-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mandateshield-com-security.txt
- group: build
  href: https://artifacts.apis.io/mandateshield-com/packages/mandateshield-com-packages.yml
  title: ''
  type: Packages
  url: packages/mandateshield-com-packages.yml
- group: build
  href: https://artifacts.apis.io/mandateshield-com/packages/mandateshield-com-packages.yml
  title: ''
  type: SDKs
  url: packages/mandateshield-com-packages.yml
- group: build
  href: https://artifacts.apis.io/mandateshield-com/cli/mandateshield-com-cli.yml
  title: ''
  type: CLI
  url: cli/mandateshield-com-cli.yml
- group: start
  href: https://artifacts.apis.io/mandateshield-com/sandbox/mandateshield-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mandateshield-com-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://mandateshield.com/sandbox
- group: commercial
  href: https://artifacts.apis.io/mandateshield-com/plans/mandateshield-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mandateshield-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/mandateshield-com/rate-limits/mandateshield-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mandateshield-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/lifecycle/mandateshield-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mandateshield-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mandateshield-com/changelog/mandateshield-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mandateshield-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://mandateshield.com/current-release.json
- group: auth
  href: https://artifacts.apis.io/mandateshield-com/authentication/mandateshield-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mandateshield-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/conventions/mandateshield-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mandateshield-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/conventions/mandateshield-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mandateshield-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/errors/mandateshield-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mandateshield-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/errors/mandateshield-com-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/mandateshield-com-error-codes.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/conformance/mandateshield-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mandateshield-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/mandateshield-com/data-model/mandateshield-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mandateshield-com-data-model.yml
- group: other
  href: https://artifacts.apis.io/mandateshield-com/overlays/mandateshield-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mandateshield-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mandateshield-com/skills/_index.yml
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
  href: https://artifacts.apis.io/mandateshield-com/regulatory/mandateshield-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/mandateshield-com-regulatory-posture.yml
- group: other
  title: ''
  type: JWKS
  url: https://mandateshield.com/.well-known/jwks.json
created: '2026-09-19'
description: MandateShield is a fail-closed authority-verification and execution-evidence boundary for autonomous AI-agent purchases, operated from Bern, Switzerland. It binds a signed purchase approval (AP2, TAP, UCP, x402, MPP, ACP or a custom envelope) to a registered mandate and a pinned issuer key, reserves cumulative budget atomically, consumes the reservation into a one-use provider-bound execution permit for an exact Stripe PaymentIntent or x402 request, and then checks the provider outcome without trusting the caller before issuing a signed terminal receipt. The hosted service never moves money or holds payment credentials. It publishes an OpenAPI 3.1 contract with 26 operations, a remote MCP server whose tools/list answers anonymously, a signed A2A agent card, llms.txt, an SPDX SBOM, a JWKS, a 91-code reason registry, a 19-vector conformance suite and self-hosted JavaScript, Python and Go clients.
finops:
- has_sources: true
  method: derived
  name: Mandateshield Com Finops
  primary_unit: decisions
  service_category: ''
  slug: mandateshield-com-finops
  template: false
image: https://mandateshield.com/icon-512.png
layout: provider
mcp_servers:
- description: One hosted, stateless Streamable HTTP MCP server at https://mandateshield.com/api/mcp. Anonymous initialize and tools/list both succeed (probed 2026-09-19); three tools are exposed and two of them (ch
  name: MandateShield MCP Server
  slug: mandateshield-com-mcp-yml
- description: ''
  name: MCP endpoint, no-auth plugin profile
  slug: mcp-endpoint-no-auth-plugin-profile
- description: ''
  name: MCP registry server.json
  slug: mcp-registry-server-json
modified: '2026-09-19'
name: MandateShield
nav: Providers
network: true
overview: 'MandateShield publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account execution control API, Advisory intelligence API, Analysis only API, and 19 more. Tagged areas include Company, Payments, Agentic Commerce, AI Agents, and Payment Authorization.


  The MandateShield catalog on APIs.io includes 1 Spectral governance ruleset.


  MandateShield''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 43 more developer resources.'
plans:
- name: Mandateshield Com Plans Pricing
  plan_count: 5
  slug: mandateshield-com-plans-pricing
- name: Mandateshield Com Price Estimates
  plan_count: 0
  slug: mandateshield-com-price-estimates
random_paper: 23
rate_limits:
- limit_count: 2
  name: Mandateshield Com Rate Limits
  slug: mandateshield-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: MandateShield API Rules
  rule_count: 63
  severity_counts:
    error: 51
    hint: 0
    info: 5
    warn: 7
  slug: mandateshield-com-rules
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 73.5
    catalog_earned_first_party: 20.0
    catalog_gap: 41.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 58.7
    developer_ergonomics: 61.3
    discoverability: 75.0
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 77.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/mandateshield-com/mandateshield-com-2026-10-11T110655.png
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
skill_count: 4
skills:
- name: Analysis-only payment authority check (no account)
  slug: mandateshield-com-analysis-only-authority-check
- name: 'Strict lifecycle: challenge, verify, consume, redeem, reconcile'
  slug: mandateshield-com-strict-lifecycle-reserve-consume-redeem
- name: Verify decision, permit and execution receipts
  slug: mandateshield-com-verify-receipts-offline-and-online
- name: Rehearse the full lifecycle in the zero-account sandbox
  slug: mandateshield-com-zero-account-lifecycle-sandbox
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
