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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 67.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'The hosted MCP mesh: ninety-two endpoints under tooloracle.io (plus five on feedoracle.io / mcp.feedoracle.io) answered an anonymous tools/list on 2026-09-19/20 with 1,178 tool entries and 919 unique '
  name: OracleNet MCP Servers
  slug: oraclenet-mcp-servers
- description: A2A 0.3 JSON-RPC agent at https://tooloracle.io/a2a/jsonrpc (message/send, tasks/*, push-notification configs, authenticated extended card) fronting ten category-level skills that route to the MCP mes
  name: OracleNet A2A Agent
  slug: oraclenet-a2a-agent
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The agent-readiness API from FeedOracle Technologies — 1 operation(s) for agent-readiness.
  name: FeedOracle Technologies Agent Readiness API
  phrasing_intents:
  - id: v2_agent_card_a2a_readiness_v1
    intent: Check an agent card for A2A readiness
    question: Can I find out whether my public agent card is ready for A2A discovery?
  phrasing_ops: 1
  slug: tooloracle-io-agent-readiness-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The agent-safety API from FeedOracle Technologies — 5 operation(s) for agent-safety.
  name: FeedOracle Technologies Agent Safety API
  phrasing_intents:
  - id: v2_agent_preflight
    intent: Pre-flight an agent action for GO or STOP
    question: Should my agent go ahead with this action, or is there a reason to stop?
  - id: v2_uvo_quick
    intent: Quickly gate an agent action proposal
    question: Is there a fast, fail-fast validation I can run on an agent's proposed action?
  - id: v2_uvo_citation_check
    intent: Verify legal and academic citations in a claim
    question: Can I catch a made-up MiCA or DORA article number before it goes into a report?
  - id: v2_uvo_full
    intent: Run the full UVO validation on an agent action
    question: What does the full UVO action gate return when I need the complete validation, not the quick one?
  - id: v2_uvo_academic_verify
    intent: Deep-verify academic sources for a claim
    question: Can I check whether a research paper's journal is predatory?
  phrasing_ops: 5
  slug: tooloracle-io-agent-safety-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Agent Trust Management API from FeedOracle Technologies — 2 operation(s) for agent trust management.
  name: FeedOracle Technologies Agent Trust Management API
  phrasing_intents:
  - id: postAiAgentRegister
    intent: Register an AI agent and get its API key
    question: How do I register a new AI agent and get an API key for it?
  - id: postAiAgentByAgentIdRotateKey
    intent: Rotate an AI agent's API key
    question: How do I rotate my agent's API key before its 90 days run out?
  phrasing_ops: 2
  slug: tooloracle-io-agent-trust-management-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'Runtime agent security & governance. 20 tools across 4 layers: pre-execution, payload security, governance, post-execution. Agent state machine with automatic escalation.'
  name: FeedOracle Technologies Agent Guard API
  phrasing_intents:
  - id: agentguardMcp
    intent: Call AgentGuard tools over JSON-RPC at /guard/mcp
    question: Can I call policy_preflight or output_safety_scan through the /guard/mcp JSON-RPC endpoint?
  - id: agentGuardMcp
    intent: Use the guard-oracle runtime security MCP server
    question: Where can I connect an MCP client for runtime security like emergency kill and scope checking?
  phrasing_ops: 2
  slug: tooloracle-io-agentguard-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: AI Agent feeds (Key required)
  name: FeedOracle Technologies Agents API
  phrasing_intents:
  - id: getAgentsRanking
    intent: Rank AI agent tokens
    question: Which AI agent tokens rank highest right now?
  - id: getAgentsTrends
    intent: See trends across AI agent tokens
    question: What trends are showing up across AI agent tokens?
  - id: getAgent
    intent: Get data for one AI agent token
    question: Can I look up a single AI agent token by its symbol?
  - id: getAgentsHealth
    intent: Check the AI agents feed health
    question: Is the AI agents data feed healthy and up to date?
  phrasing_ops: 4
  slug: tooloracle-io-agents-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The AI Gateway API from FeedOracle Technologies — 4 operation(s) for ai gateway.
  name: FeedOracle Technologies AI Gateway API
  phrasing_intents:
  - id: postAiQuery
    intent: Ask a compliance question and get signed evidence
    question: Can I ask a plain-English compliance question and get a signed evidence bundle back?
  - id: postAiExplain
    intent: Explain why an asset got its compliance grade
    question: Why did a stablecoin receive the compliance grade it got?
  - id: postAiProvenance
    intent: Trace the data provenance behind an evidence bundle
    question: Where did the source data in an evidence bundle come from?
  - id: postEvidenceBundle
    intent: Bundle evidence across several compliance frameworks
    question: Can I get MiCA, DORA and RWA evidence for one asset in a single request?
  phrasing_ops: 4
  slug: tooloracle-io-ai-gateway-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Anti-money laundering and sanctions screening — 12 tools, 87k+ watchlist entries
  name: FeedOracle Technologies AML Oracle API
  phrasing_intents:
  - id: amlOracleMcp
    intent: Screen sanctions and PEPs over MCP
    question: Can my agent screen a name against OFAC, EU and UN sanctions lists over MCP?
  phrasing_ops: 1
  slug: tooloracle-io-aml-oracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Sanctions, PEP, KYC (12 tools)
  name: FeedOracle Technologies AML Oracle API
  phrasing_intents:
  - id: amlMcp
    intent: Run sanctions, PEP and KYC tools over MCP
    question: Is there an MCP server with sanctions, PEP and KYC tools I can plug into my agent?
  phrasing_ops: 1
  slug: tooloracle-io-amloracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DORA traffic light system (25 tools)
  name: FeedOracle Technologies Ampel Oracle API
  phrasing_intents:
  - id: ampelMcp
    intent: Use the DORA traffic-light MCP server
    question: Can I get a red, yellow or green DORA readiness signal through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-ampeloracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DAP attestation (Public)
  name: FeedOracle Technologies Attestation API
  phrasing_intents:
  - id: getAttestationStatus
    intent: Check the attestation system status
    question: What is the current merkle root of the attestation system?
  - id: getAttestationChains
    intent: Check anchor status on each chain
    question: Are attestations anchored on Ethereum, Polygon, Arbitrum and Base right now?
  - id: getAttestationActivity
    intent: List recent attestation anchor activity
    question: When were attestations last anchored on-chain?
  - id: verifyAttestation
    intent: Verify an attestation by its ID
    question: Can I confirm a v2 attestation is genuine using its attestation ID?
  phrasing_ops: 4
  slug: tooloracle-io-attestation-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Attestations API from FeedOracle Technologies — 2 operation(s) for attestations.
  name: FeedOracle Technologies Attestations API
  phrasing_intents:
  - id: getAttestation
    intent: Get an attestation record
    question: Can I fetch the full record of a v3 attestation?
  - id: verifyAttestationV3
    intent: Verify an attestation on-chain
    question: Is this attestation actually anchored on-chain?
  phrasing_ops: 2
  slug: tooloracle-io-attestations-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Audit Trail API from FeedOracle Technologies — 1 operation(s) for audit trail.
  name: FeedOracle Technologies Audit Trail API
  phrasing_intents:
  - id: audit_log
    intent: Log a compliance decision to the audit trail
    question: Can I record a compliance decision in a tamper-proof, chain-linked audit trail?
  phrasing_ops: 1
  slug: tooloracle-io-audit-trail-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Billing API from FeedOracle Technologies — 1 operation(s) for billing.
  name: FeedOracle Technologies Billing API
  phrasing_intents:
  - id: postApiBillingRegister
    intent: Sign up for a free API key
    question: How do I get a free ToolOracle API key without a credit card?
  phrasing_ops: 1
  slug: tooloracle-io-billing-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: '13 blockchain oracles: Arbitrum, Solana, TON, Sui, ETH, XLM, XRPL, BNB, Aptos, Base, Hedera, BTC, Flare'
  name: FeedOracle Technologies Blockchain API
  phrasing_intents:
  - id: arbitrumMcp
    intent: Query Arbitrum data over MCP
    question: Is there an MCP server for Arbitrum on-chain data?
  - id: solanaMcp
    intent: Query Solana data over MCP
    question: Is there an MCP server for Solana data?
  - id: tonMcp
    intent: Query TON blockchain data over MCP
    question: Is there an MCP server for the TON blockchain?
  - id: suiMcp
    intent: Query Sui data over MCP
    question: Is there an MCP server for Sui chain data?
  - id: ethMcp
    intent: Query Ethereum data over MCP
    question: Is there an MCP server for Ethereum mainnet data?
  - id: xlmMcp
    intent: Query Stellar data over MCP
    question: Is there an MCP server for Stellar (XLM) data?
  - id: postXrplMcp
    intent: Use the free XRP Ledger and RLUSD MCP server
    question: Is there a free MCP server with XRP Ledger account, DEX and AMM tools?
  - id: bnbMcp
    intent: Query BNB Chain data over MCP
    question: Is there an MCP server for BNB Chain data?
  phrasing_ops: 13
  slug: tooloracle-io-blockchain-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The blockchain-risk API from FeedOracle Technologies — 1 operation(s) for blockchain-risk.
  name: FeedOracle Technologies Blockchain Risk API
  phrasing_intents:
  - id: v2_meme_rug_check
    intent: Check a memecoin for rug-pull risk
    question: Is this memecoin likely a rug pull or a honeypot?
  phrasing_ops: 1
  slug: tooloracle-io-blockchain-risk-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Business API from FeedOracle Technologies — 3 operation(s) for business.
  name: FeedOracle Technologies Business API
  phrasing_intents:
  - id: getBusiness
    intent: Get a US business conditions overview
    question: What's the overall picture for US business activity, credit and delinquency?
  - id: getProduction
    intent: Get industrial production and capacity use
    question: What is the latest industrial production index reading?
  - id: getBizCredit
    intent: Get business and consumer credit data
    question: How are commercial loans and consumer credit trending?
  phrasing_ops: 3
  slug: tooloracle-io-business-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Carbon data (Key required)
  name: FeedOracle Technologies Carbon API
  phrasing_intents:
  - id: getCarbonChains
    intent: Get carbon data for 49 blockchains
    question: How much CO2 and energy does each blockchain network use?
  - id: getCarbonSummary
    intent: Get blockchain carbon summary stats
    question: What are the headline carbon statistics across blockchains in the feed?
  - id: getCarbonChainsAlt
    intent: Get public carbon data for 50+ chains
    question: Is there a public endpoint for carbon data on 50+ blockchains?
  - id: getCarbonSummaryAlt
    intent: Get carbon summary from the alternate path
    question: Is there an alternate carbon summary path outside the feeds API?
  - id: getCarbonMica
    intent: Get MiCA Article 66 carbon data for a token
    question: Can I get sustainability data formatted for MiCA Article 66 disclosure?
  phrasing_ops: 5
  slug: tooloracle-io-carbon-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: EU ETS, grid intensity (11 tools)
  name: FeedOracle Technologies Carbon Oracle API
  phrasing_intents:
  - id: carbonMcp
    intent: Use the carbon and grid-intensity MCP server
    question: Can my agent look up EU ETS carbon prices over MCP?
  phrasing_ops: 1
  slug: tooloracle-io-carbonoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'DORA cloud monitoring: live AWS/GCP/Azure status, concentration risk, CTPP check.'
  name: FeedOracle Technologies Cloud Oracle API
  phrasing_intents:
  - id: cloudOracleMcp
    intent: Use the CloudOracle MCP server
    question: What does the CloudOracle MCP server offer?
  phrasing_ops: 1
  slug: tooloracle-io-cloudoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Commodities API from FeedOracle Technologies — 3 operation(s) for commodities.
  name: FeedOracle Technologies Commodities API
  phrasing_intents:
  - id: getCommodities
    intent: Get an energy and metals overview
    question: What are commodity prices doing across energy and metals?
  - id: getEnergy
    intent: Get energy commodity prices
    question: What are WTI and Brent crude trading at?
  - id: getMetals
    intent: Get precious metals prices
    question: What's the latest gold and silver price?
  phrasing_ops: 3
  slug: tooloracle-io-commodities-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The compliance API from FeedOracle Technologies — 4 operation(s) for compliance.
  name: FeedOracle Technologies Compliance API
  phrasing_intents:
  - id: v2_compliance_preflight
    intent: Get a MiCA PASS/WARN/BLOCK verdict for a stablecoin
    question: Can I quickly get a PASS, WARN or BLOCK verdict on whether a stablecoin is MiCA compliant?
  - id: v2_mica_stablecoin_check
    intent: Run a full MiCA traffic-light audit on a stablecoin
    question: Can I see a red, yellow or green rating for a stablecoin across all 12 MiCA articles?
  - id: v2_sanctions_screen
    intent: Screen a name against sanctions lists
    question: Is this person or company on the OFAC, EU, UN or UK sanctions lists?
  - id: v2_xrpl_rlusd_integrity
    intent: Cross-check RLUSD peg, supply and liquidity
    question: Does RLUSD's on-chain XRPL supply match what's reported?
  phrasing_ops: 4
  slug: tooloracle-io-compliance-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Credit API from FeedOracle Technologies — 4 operation(s) for credit.
  name: FeedOracle Technologies Credit API
  phrasing_intents:
  - id: getSOFR
    intent: Get the current SOFR rate
    question: What is the Secured Overnight Financing Rate today?
  - id: getCreditSpreads
    intent: Get corporate credit spreads
    question: What's the BAA minus AAA corporate bond spread?
  - id: getLending
    intent: Get bank lending conditions
    question: Are banks tightening lending standards?
  - id: getFedRates
    intent: Get Fed overnight rates
    question: What are EFFR, OBFR and the reverse repo rate today?
  phrasing_ops: 4
  slug: tooloracle-io-credit-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The cross-border API from FeedOracle Technologies — 1 operation(s) for cross-border.
  name: FeedOracle Technologies Cross Border API
  phrasing_intents:
  - id: v2_nomos_preflight
    intent: Check whether a cross-border data transfer is allowed
    question: Can I send customer data from the EU to India under GDPR and DPDP?
  phrasing_ops: 1
  slug: tooloracle-io-cross-border-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Crypto API from FeedOracle Technologies — 2 operation(s) for crypto.
  name: FeedOracle Technologies Crypto API
  phrasing_intents:
  - id: getCrypto
    intent: Get BTC and ETH reference prices
    question: What are Bitcoin and Ether trading at in US dollars?
  - id: getCryptoSingle
    intent: Get one crypto price by symbol
    question: Can I look up just one cryptocurrency's price by symbol?
  phrasing_ops: 2
  slug: tooloracle-io-crypto-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: v3 Sustainability disclosure (Public)
  name: FeedOracle Technologies Disclosure API
  phrasing_intents:
  - id: getDisclosureNetworks
    intent: List networks with sustainability disclosures
    question: Which blockchain networks have an attested sustainability disclosure?
  - id: getDisclosureSustainability
    intent: Get one network's sustainability report
    question: Can I pull the sustainability report for a single blockchain network?
  phrasing_ops: 2
  slug: tooloracle-io-disclosure-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Well-known endpoints for agent discovery (ANP/A2A-compatible).
  name: FeedOracle Technologies Discovery API
  phrasing_intents:
  - id: getWellKnownMeshEconomics
    intent: Discover the mesh economics dashboard data
    question: Where is the machine-readable mesh economics file for pricing and rewards?
  - id: getWellKnownAgentPulse
    intent: Read the mesh agent pulse
    question: What is the current gravity score of the agent mesh?
  - id: getWellKnownMetaTools
    intent: See emergent meta-tool candidates
    question: Which tool combinations are agents chaining together often enough to become meta-tools?
  phrasing_ops: 3
  slug: tooloracle-io-discovery-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'DORA traffic-light compliance system — 49 tools, 26 articles, 39 checks, 67 controls, 6 entities. Closed-loop: Control→Finding→Owner→ReTest→Close. Escalation, What-if, Board-View, Dependency Graph, Ev'
  name: FeedOracle Technologies DORA Ampel API
  phrasing_intents:
  - id: doraAmpelMcp
    intent: Run DORA compliance traffic-light tools over MCP
    question: Can I onboard an entity and get a DORA gap report over MCP?
  phrasing_ops: 1
  slug: tooloracle-io-dora-ampel-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Multi-agent orchestrator. 16 tools coordinating all 16 DORA OS oracles. Workflows, event reactions, board briefings, remediation planning.
  name: FeedOracle Technologies DORA OS Conductor API
  phrasing_intents:
  - id: conductorMcp
    intent: Orchestrate DORA OS tools via the Conductor
    question: Is there a master orchestrator that coordinates the DORA OS oracles?
  phrasing_ops: 1
  slug: tooloracle-io-dora-os-conductor-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: CVE/KEV, CERT-Bund, cloud status (15 tools)
  name: FeedOracle Technologies DORA Oracle API
  phrasing_intents:
  - id: doraMcp
    intent: Track ICT threats for DORA over MCP
    question: Can my agent check CVE and known-exploited vulnerability data for DORA through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-doraoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Self-healing compliance drift detection. Regulatory changes, evidence staleness, cloud drift, auto-remediation.
  name: FeedOracle Technologies Drift Oracle API
  phrasing_intents:
  - id: driftOracleMcp
    intent: Detect and heal configuration drift over MCP
    question: Is there an MCP server for self-healing drift detection?
  phrasing_ops: 1
  slug: tooloracle-io-driftoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The ECB API from FeedOracle Technologies — 7 operation(s) for ecb.
  name: FeedOracle Technologies ECB API
  phrasing_intents:
  - id: getECB
    intent: Get a eurozone overview from the ECB
    question: What's the ECB key rate, EUR/USD and eurozone inflation at a glance?
  - id: getECBRates
    intent: Get ECB policy rates and EURIBOR
    question: What are the ECB refi, deposit and marginal lending rates?
  - id: getECBFX
    intent: Get ECB euro exchange rates
    question: What is the euro trading at against the dollar, pound and yen?
  - id: getECBInflation
    intent: Get eurozone inflation
    question: What is eurozone HICP and core HICP inflation right now?
  - id: getECBEconomy
    intent: Get eurozone growth and money supply
    question: How fast is the eurozone economy growing?
  - id: getECBYields
    intent: Get euro-area government bond yields
    question: What is the 10-year AAA euro government bond yield?
  - id: getECBSeries
    intent: Get one ECB data series
    question: Can I pull just one of the 20 ECB series by its ID?
  phrasing_ops: 7
  slug: tooloracle-io-ecb-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Enterprise Trust Layer API from FeedOracle Technologies — 2 operation(s) for enterprise trust layer.
  name: FeedOracle Technologies Enterprise Trust Layer API
  phrasing_intents:
  - id: getVerifySdk
    intent: Get the evidence validation SDK details
    question: Which languages does the evidence verification SDK support?
  - id: getVerifySelfTest
    intent: Run a live self-test of the validation SDK
    question: Can I prove the verification SDK works by running a live self-test?
  phrasing_ops: 2
  slug: tooloracle-io-enterprise-trust-layer-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The EPM API from FeedOracle Technologies — 1 operation(s) for epm.
  name: FeedOracle Technologies EPM API
  phrasing_intents:
  - id: verifyEPM
    intent: Verify a signed EPM manifest
    question: Can I check that a DSSE-wrapped EPM manifest has valid signatures?
  phrasing_ops: 1
  slug: tooloracle-io-epm-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Equities API from FeedOracle Technologies — 2 operation(s) for equities.
  name: FeedOracle Technologies Equities API
  phrasing_intents:
  - id: getEquities
    intent: Get major US stock index levels
    question: Where are the S&P 500, NASDAQ and Dow trading?
  - id: getEquity
    intent: Get one stock index by symbol
    question: Can I look up a single stock index by symbol?
  phrasing_ops: 2
  slug: tooloracle-io-equities-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The ESMA Register API from FeedOracle Technologies — 8 operation(s) for esma register.
  name: FeedOracle Technologies ESMA Register API
  phrasing_intents:
  - id: getApiV1Esma
    intent: See what the ESMA register service offers
    question: Which endpoints does the ESMA register service expose?
  - id: getApiV1EsmaCasps
    intent: List authorized crypto-asset service providers
    question: Which crypto-asset service providers are authorized under MiCA in Germany?
  - id: getApiV1EsmaEmtIssuers
    intent: List e-money token issuers
    question: Who issues e-money token stablecoins under MiCA?
  - id: getApiV1EsmaNonCompliant
    intent: List entities flagged for MiCA violations
    question: Which crypto entities have been flagged as non-compliant with MiCA?
  - id: getApiV1EsmaPending
    intent: List pending MiCA applications
    question: Which companies are still waiting on MiCA authorization?
  - id: getApiV1EsmaSearch
    intent: Search the ESMA crypto register
    question: Is a given exchange listed anywhere in the ESMA register?
  - id: getApiV1EsmaStats
    intent: Get ESMA register statistics
    question: How are authorized crypto firms spread across countries and service types?
  - id: getApiV1EsmaSummary
    intent: Get the ESMA register summary
    question: How many CASPs, EMT issuers, non-compliant and pending entities are in the register?
  phrasing_ops: 8
  slug: tooloracle-io-esma-register-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Official ESMA MiCA register — CASPs, non-compliant entities, white papers
  name: FeedOracle Technologies ESMA Oracle API
  phrasing_intents:
  - id: esmaOracleMcp
    intent: Check CASP authorization via esma-oracle path
    question: Can my agent check whether a crypto-asset service provider is authorized, via the esma-oracle endpoint?
  - id: esmaMcp
    intent: Search the ESMA MiCA register via /esma
    question: Is there a short /esma MCP path for searching the ESMA MiCA register?
  phrasing_ops: 2
  slug: tooloracle-io-esmaoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The EU Carbon Intelligence API from FeedOracle Technologies — 2 operation(s) for eu carbon intelligence.
  name: FeedOracle Technologies EU Carbon Intelligence API
  phrasing_intents:
  - id: getApiV1EuEtsPrice
    intent: Get the EU ETS carbon price
    question: What is the current EU Emissions Trading System carbon price?
  - id: getApiV1EmberIntensityByCountryCode
    intent: Get a country's grid carbon intensity
    question: How carbon-intensive is Germany's electricity grid?
  phrasing_ops: 2
  slug: tooloracle-io-eu-carbon-intelligence-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The EU Energy API from FeedOracle Technologies — 1 operation(s) for eu energy.
  name: FeedOracle Technologies EU Energy API
  phrasing_intents:
  - id: getApiV1EuEnergyGenerationByCountry
    intent: Get a country's live power generation mix
    question: What is France generating its electricity from right now?
  phrasing_ops: 1
  slug: tooloracle-io-eu-energy-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: EU financial regulation intelligence — 12 regulations, article lookup, cross-references, deadlines
  name: FeedOracle Technologies EU Law Oracle API
  phrasing_intents:
  - id: euLawOracleMcp
    intent: Look up EU regulation articles via eulaw-oracle
    question: Can my agent pull article-level text from 12 EU regulations via the eulaw-oracle endpoint?
  - id: eulawMcp
    intent: Use the /eulaw EU regulations MCP path
    question: Is there a shorter /eulaw path for the EU law MCP tools?
  phrasing_ops: 2
  slug: tooloracle-io-eulaworacle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Real-time event processing. Webhook receiver, 12 routing rules, auto-dispatch to Conductor.
  name: FeedOracle Technologies Event Fabric API
  phrasing_intents:
  - id: eventFabricMcp
    intent: Use the EventFabric MCP server
    question: What does the EventFabric MCP server provide?
  phrasing_ops: 1
  slug: tooloracle-io-eventfabric-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The finance API from FeedOracle Technologies — 1 operation(s) for finance.
  name: FeedOracle Technologies Finance API
  phrasing_intents:
  - id: v2_macro_snapshot
    intent: Get a one-call US macro snapshot
    question: Can I get Fed funds, CPI, PPI and the yield curve in one call?
  phrasing_ops: 1
  slug: tooloracle-io-finance-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Fiscal API from FeedOracle Technologies — 3 operation(s) for fiscal.
  name: FeedOracle Technologies Fiscal API
  phrasing_intents:
  - id: getFiscal
    intent: Get a US federal debt overview
    question: How big is the US federal debt and deficit right now?
  - id: getFiscalDebt
    intent: Get US federal debt figures
    question: What is the total US federal debt?
  - id: getFiscalTrade
    intent: Get the US trade balance and dollar index
    question: What is the latest US trade balance?
  phrasing_ops: 3
  slug: tooloracle-io-fiscal-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Flight search (8 tools)
  name: FeedOracle Technologies Flight Oracle API
  phrasing_intents:
  - id: flightMcp
    intent: Search flights over MCP
    question: Can my agent search for flights through an MCP server?
  phrasing_ops: 1
  slug: tooloracle-io-flightoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: System health endpoints (Public)
  name: FeedOracle Technologies Health API
  phrasing_intents:
  - id: getFeedsHealth
    intent: Check overall feed API health
    question: Are all the data feeds healthy right now?
  - id: getCarbonHealth
    intent: Check the carbon feed health
    question: Is the carbon data feed up and current?
  - id: getEvents
    intent: List system events
    question: What system events have happened recently?
  - id: getFeedHealthSymbol
    intent: Check feed health for one symbol
    question: Is the data for one specific symbol fresh?
  phrasing_ops: 4
  slug: tooloracle-io-health-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Hotel search (8 tools)
  name: FeedOracle Technologies Hotel Oracle API
  phrasing_intents:
  - id: hotelMcp
    intent: Search hotels over MCP
    question: Can my agent search for hotels through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-hoteloracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: NatCat, GLEIF (12 tools)
  name: FeedOracle Technologies Insurance Oracle API
  phrasing_intents:
  - id: insuranceMcp
    intent: Get natural catastrophe and entity data over MCP
    question: Can my agent check natural catastrophe risk through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-insuranceoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Cross-source validation, baselines, and verifiable credentials
  name: FeedOracle Technologies Integrity Suite API
  phrasing_intents:
  - id: postApiV1VcVerify
    intent: Verify a JWS signature
    question: How do I check that a signed JWS credential is genuine?
  phrasing_ops: 1
  slug: tooloracle-io-integrity-suite-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The International API from FeedOracle Technologies — 3 operation(s) for international.
  name: FeedOracle Technologies International API
  phrasing_intents:
  - id: getIntlBonds
    intent: Get international 10-year bond yields
    question: What are German, UK and Japanese 10-year yields?
  - id: getIntlFX
    intent: Get dollar exchange rates from FRED
    question: What are the dollar exchange rates for EUR, GBP, JPY and INR?
  - id: getIntlSpreads
    intent: Get sovereign yield spreads
    question: What's the spread between US and German 10-year yields?
  phrasing_ops: 3
  slug: tooloracle-io-international-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Financial messaging (12 tools)
  name: FeedOracle Technologies ISO20022 Oracle API
  phrasing_intents:
  - id: iso20022Mcp
    intent: Work with ISO 20022 messaging over MCP
    question: Is there an MCP server for ISO 20022 financial messaging?
  phrasing_ops: 1
  slug: tooloracle-io-iso20022oracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Job market (8 tools)
  name: FeedOracle Technologies Job Oracle API
  phrasing_intents:
  - id: jobMcp
    intent: Explore job market data over MCP
    question: Can my agent look up job market data through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-joboracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Knowledge base (Key required)
  name: FeedOracle Technologies Knowledge API
  phrasing_intents:
  - id: getKnowledgeAssets
    intent: List knowledge base assets
    question: Which assets are in the knowledge base?
  - id: getKnowledgeStats
    intent: Get knowledge base statistics
    question: How large is the knowledge base?
  - id: getKnowledgeStatus
    intent: Check knowledge system status
    question: Is the knowledge system running?
  - id: getKnowledgeHealth
    intent: Check knowledge feed health
    question: Is the knowledge feed healthy?
  phrasing_ops: 4
  slug: tooloracle-io-knowledge-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The KYA - Know Your Agent API from FeedOracle Technologies — 1 operation(s) for kya - know your agent.
  name: FeedOracle Technologies KYA - Know Your Agent API
  phrasing_intents:
  - id: kya_register
    intent: Register an AI agent's identity
    question: How do I register my AI agent to get a trust score?
  phrasing_ops: 1
  slug: tooloracle-io-kya-know-your-agent-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Layer 2 fee oracle (Public)
  name: FeedOracle Technologies L2 API
  phrasing_intents:
  - id: getL2Cheapest
    intent: Find the cheapest healthy L2 chain
    question: Which layer 2 has the lowest gas cost right now?
  - id: getL2Health
    intent: Check L2 sequencer health
    question: Are the Arbitrum, Optimism and Base sequencers up?
  - id: getL2All
    intent: Get data for all L2 chains
    question: Can I get all the layer 2 chain data in one response?
  - id: getL2Status
    intent: Get one L2 chain's status
    question: Can I check the status of a single L2 chain?
  phrasing_ops: 4
  slug: tooloracle-io-l2-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'Multi-jurisdiction legal intelligence MCP server. 20 tools, 9 data sources, 4 jurisdictions (US, EU, UK, DE). Obligation mapping, article extraction, DORA OS bridge. Endpoint: https://tooloracle.io/la'
  name: FeedOracle Technologies Law Oracle API
  phrasing_intents:
  - id: lawOracleMcp
    intent: Search multi-jurisdiction law over MCP
    question: Can my agent search EU, US, UK and German law through one MCP server?
  phrasing_ops: 1
  slug: tooloracle-io-laworacle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Lead enrichment (7 tools)
  name: FeedOracle Technologies Lead Oracle API
  phrasing_intents:
  - id: leadMcp
    intent: Enrich sales leads over MCP
    question: Can my agent enrich a sales lead through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-leadoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Macro economic (Key required)
  name: FeedOracle Technologies Macro API
  phrasing_intents:
  - id: getMacroProofs
    intent: Get attestation proofs for macro data
    question: Can I get cryptographic proofs that the macro data wasn't altered?
  - id: getMacroVerifiedAll
    intent: Get all verified macro data
    question: Can I pull every macro indicator that has been verified?
  - id: getMacroVerificationStatus
    intent: Check macro data verification status
    question: Has the latest macro data been verified yet?
  phrasing_ops: 3
  slug: tooloracle-io-macro-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Macro Core API from FeedOracle Technologies — 9 operation(s) for macro core.
  name: FeedOracle Technologies Macro Core API
  phrasing_intents:
  - id: getMacroHealth
    intent: Get the Economic Health Index
    question: Is the US economy expanding, stable or contracting?
  - id: getMacroAll
    intent: Get all core macro indicators
    question: Can I pull every core economic indicator together?
  - id: getMacroFed
    intent: Get the Fed funds rate and FOMC outlook
    question: When is the next FOMC meeting and what's the rate outlook?
  - id: getMacroInflation
    intent: Get US CPI and PCE inflation
    question: What is US CPI inflation year over year?
  - id: getMacroYields
    intent: Get key Treasury yields
    question: What are the 2-year, 10-year and 30-year Treasury yields?
  - id: getMacroGDP
    intent: Get US GDP growth
    question: What was last quarter's real GDP growth annualized?
  - id: getMacroEmployment
    intent: Get US employment data
    question: What is the US unemployment rate?
  - id: getMacroRisk
    intent: Get recession probability
    question: What's the probability of a US recession?
  phrasing_ops: 9
  slug: tooloracle-io-macro-core-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: US macro-economic data from FRED — health index, inflation, GDP, fed rates, yield curve
  name: FeedOracle Technologies Macro Oracle API
  phrasing_intents:
  - id: getDefiMacroBundle
    intent: Get a macro data bundle for DeFi
    question: Is there a macro bundle built for DeFi and RWA protocols?
  phrasing_ops: 1
  slug: tooloracle-io-macro-oracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Macro economic intelligence — ECB + FRED + BLS + World Bank
  name: FeedOracle Technologies Macro Oracle API
  phrasing_intents:
  - id: macroOracleMcp
    intent: Query FRED, ECB, World Bank and BLS over MCP
    question: Can my agent pull FRED, ECB, World Bank and BLS data through one MCP server?
  phrasing_ops: 1
  slug: tooloracle-io-macrooracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Location intelligence (12 tools)
  name: FeedOracle Technologies Map Oracle API
  phrasing_intents:
  - id: mapMcp
    intent: Get location intelligence over MCP
    question: Can my agent get location intelligence through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-maporacle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The market-integrity API from FeedOracle Technologies — 3 operation(s) for market-integrity.
  name: FeedOracle Technologies Market Integrity API
  phrasing_intents:
  - id: v2_orderbook_risk
    intent: Score a Kalshi orderbook for fragility
    question: Is this Kalshi market's orderbook too thin to trade safely?
  - id: v2_candidate_conflict_check
    intent: Check a Kalshi market for candidate self-interest
    question: Could a candidate be trading on their own election market?
  - id: v2_suspicious_timing_scan
    intent: Scan a Polymarket market for suspicious timing
    question: Were there big pre-event bets from new wallets on this Polymarket market?
  phrasing_ops: 3
  slug: tooloracle-io-market-integrity-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The MCP Auth API from FeedOracle Technologies — 3 operation(s) for mcp auth.
  name: FeedOracle Technologies MCP Auth API
  phrasing_intents:
  - id: postMcpRegister
    intent: Register an OAuth client for MCP access
    question: How do I register a machine-to-machine client for the MCP server?
  - id: postMcpToken
    intent: Get an OAuth bearer token for MCP
    question: How does an agent get a bearer token without a browser?
  - id: postMcpRevoke
    intent: Revoke an MCP access token
    question: How do I revoke an access token I no longer need?
  phrasing_ops: 3
  slug: tooloracle-io-mcp-auth-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The MCP Transport API from FeedOracle Technologies — 3 operation(s) for mcp transport.
  name: FeedOracle Technologies MCP Transport API
  phrasing_intents:
  - id: getMcpSse
    intent: Open the compliance MCP SSE stream
    question: How do I connect to the compliance MCP server over Server-Sent Events?
  - id: postMcpMessages
    intent: Send a JSON-RPC message to a compliance MCP session
    question: How do I send JSON-RPC calls to an open compliance SSE session?
  - id: getMcpRiskSse
    intent: Open the stablecoin risk MCP SSE stream
    question: Is there an SSE MCP stream for stablecoin peg and reserve risk?
  phrasing_ops: 3
  slug: tooloracle-io-mcp-transport-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'Agent-native economic layer: append-only ledger, fresh/cached pricing, originator + referrer rewards.'
  name: FeedOracle Technologies Mesh Economics API
  phrasing_intents:
  - id: getEconomicsApiHealth
    intent: Check the mesh economics service health
    question: Is the mesh economics service up?
  - id: postEconomicsApiPrice
    intent: Price a tool call before running it
    question: How much will a tool call cost my wallet, fresh or cached?
  - id: postEconomicsApiCommit
    intent: Book an executed call into the ledger
    question: How do I record a tool call in the ledger after it runs?
  - id: getEconomicsApiBalanceByWallet
    intent: Get a wallet's mesh ledger balance
    question: What is my wallet's balance in the mesh ledger?
  - id: postEconomicsApiReferral
    intent: Register a direct referral between wallets
    question: How do I register that one wallet referred another?
  - id: getEconomicsApiStats
    intent: Get live, uncached mesh economics stats
    question: Can I get mesh economics stats generated live instead of the five-minute cached copy?
  - id: getWellKnownMeshEconomics
    intent: Get the cached mesh economics dashboard payload
    question: Where is the public machine-readable mesh economics file refreshed every five minutes?
  - id: getEconomicsHtml
    intent: Open the human-readable economics dashboard
    question: Is there a web page where I can look at mesh economics myself?
  phrasing_ops: 8
  slug: tooloracle-io-mesh-economics-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: 'Live mesh signals for autonomous agents: gravity, emergent patterns, meta-tool candidates.'
  name: FeedOracle Technologies Mesh Nervous System API
  phrasing_intents:
  - id: getWellKnownAgentPulse
    intent: Read the mesh agent pulse
    question: What is the current gravity score of the agent mesh?
  - id: getWellKnownMetaTools
    intent: See emergent meta-tool candidates
    question: Which tool combinations are agents chaining often enough to become meta-tools?
  phrasing_ops: 2
  slug: tooloracle-io-mesh-nervous-system-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: MiCA stablecoin compliance monitoring — 24 tools, 17 tokens, 13 issuers
  name: FeedOracle Technologies MiCA Ampel API
  phrasing_intents:
  - id: micaAmpelMcp
    intent: Run MiCA stablecoin compliance tools over MCP
    question: Can I assess a stablecoin issuer and validate its whitepaper under MiCA over MCP?
  phrasing_ops: 1
  slug: tooloracle-io-mica-ampel-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: MiCA regulatory compliance evidence (Art. 22-58) for stablecoins and token issuers
  name: FeedOracle Technologies MiCA Compliance API
  phrasing_intents:
  - id: getApiV1FeedsMicaCustodyRiskByProtocol
    intent: Get the MiCA custody risk feed for a protocol
    question: What custody risks does a crypto protocol carry under MiCA Articles 26, 27 and 54?
  - id: getApiV1FeedsMicaDocumentComplianceBySymbol
    intent: Check a stablecoin's MiCA document compliance
    question: Does a stablecoin's white paper and disclosure set meet MiCA Articles 29, 30, 37 and 55?
  - id: getApiV1FeedsMicaFullPackBySymbol
    intent: Get the full MiCA evidence pack for a stablecoin
    question: Can I get one complete MiCA evidence pack covering Articles 22 to 58 for a stablecoin?
  - id: getApiV1FeedsMicaInterestCheckBySymbol
    intent: Check a stablecoin against the MiCA interest ban
    question: Does a stablecoin break MiCA's prohibition on paying interest to holders?
  - id: getApiV1FeedsMicaReserveQualityBySymbol
    intent: Assess a stablecoin's MiCA reserve quality
    question: How good are a stablecoin's reserve assets under MiCA Articles 24, 25, 36 and 53?
  - id: getApiV1FeedsMicaSignificantIssuerBySymbol
    intent: Check if a stablecoin issuer is significant under MiCA
    question: Would a stablecoin be classified as significant under MiCA Articles 45 and 58?
  - id: getApiV1Mica
    intent: List the available MiCA compliance endpoints
    question: What MiCA compliance endpoints does this API expose?
  - id: getEcbMicaReserve
    intent: Get ECB data for MiCA reserve management
    question: What ECB rates and EURIBOR benchmarks matter for managing EUR stablecoin reserves under MiCA?
  phrasing_ops: 8
  slug: tooloracle-io-mica-compliance-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: MiCA stablecoin compliance (24 tools)
  name: FeedOracle Technologies Mi CA Oracle API
  phrasing_intents:
  - id: micaMcp
    intent: Check MiCA stablecoin compliance over MCP
    question: Is there an MCP server for MiCA stablecoin compliance?
  phrasing_ops: 1
  slug: tooloracle-io-micaoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Film & entertainment (12 tools)
  name: FeedOracle Technologies Movie Oracle API
  phrasing_intents:
  - id: movieMcp
    intent: Look up film and entertainment data over MCP
    question: Can my agent look up movies and entertainment data through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-movieoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: News & trends (9 tools)
  name: FeedOracle Technologies News Oracle API
  phrasing_intents:
  - id: newsMcp
    intent: Get news and trends over MCP
    question: Can my agent pull news and trending topics through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-newsoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The nomos API from FeedOracle Technologies — 1 operation(s) for nomos.
  name: FeedOracle Technologies Nomos API
  phrasing_intents:
  - id: v2_nomos_full_chain_verification
    intent: Run a verified action through the NOMOS chain
    question: Can I get a signed receipt proving an agent action went through the full NOMOS trust chain?
  phrasing_ops: 1
  slug: tooloracle-io-nomos-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The NOMOS Execution Receipts API from FeedOracle Technologies — 1 operation(s) for nomos execution receipts.
  name: FeedOracle Technologies NOMOS Execution Receipts API
  phrasing_intents:
  - id: getV1NomosExecutionReceiptsByExecutionId
    intent: Read the signed receipt for a call
    question: How do I get the signed execution receipt for a request I made?
  phrasing_ops: 1
  slug: tooloracle-io-nomos-execution-receipts-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Self-learning agent mesh protocol. Neural routing, W3C DIDs, VCs, on-chain escrow (Base + XRPL), PROV-O provenance.
  name: FeedOracle Technologies Oracle Net API
  phrasing_intents:
  - id: postXrplMcp
    intent: Use the free XRP Ledger and RLUSD MCP server
    question: Is there a free MCP server with XRP Ledger account, DEX and AMM tools?
  - id: xrplPaidMcp
    intent: Run the paid RLUSD integrity check over x402
    question: Can I pay per call in USDC on Base to run the RLUSD integrity check?
  - id: postQuantumMcp
    intent: Join the OracleNet mesh and check trust over MCP
    question: How can my agent join the OracleNet mesh in a single call?
  - id: getOraclenetBeacon
    intent: Check live OracleNet mesh status
    question: Is the OracleNet mesh up right now, and what is its uptime?
  - id: getMeshRegistryJson
    intent: Browse the OracleNet oracle registry
    question: Which oracles are registered in the OracleNet mesh and what can each do?
  phrasing_ops: 5
  slug: tooloracle-io-oraclenet-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DORA ICT policy lifecycle. 12 tools, 12 RTS-required policies, gap check, version control.
  name: FeedOracle Technologies Policy Oracle API
  phrasing_intents:
  - id: policyOracleMcp
    intent: Govern DORA ICT policies over MCP
    question: Is there an MCP server for DORA ICT policy governance?
  phrasing_ops: 1
  slug: tooloracle-io-policyoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Predictive risk engine. Score trajectories, evidence decay, early warnings, what-if scenarios.
  name: FeedOracle Technologies Predict Oracle API
  phrasing_intents:
  - id: predictOracleMcp
    intent: Get predictive risk over MCP
    question: Can my agent get predictive risk scores through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-predictoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Price comparison (7 tools)
  name: FeedOracle Technologies Price Oracle API
  phrasing_intents:
  - id: priceMcp
    intent: Compare product prices over MCP
    question: Can my agent compare prices for a product through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-priceoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Real Estate API from FeedOracle Technologies — 3 operation(s) for real estate.
  name: FeedOracle Technologies Real Estate API
  phrasing_intents:
  - id: getRealEstate
    intent: Get a US housing market overview
    question: How is the US housing market doing overall?
  - id: getREPrices
    intent: Get US home price indices
    question: What is the Case-Shiller index showing?
  - id: getMortgage
    intent: Get US mortgage rates
    question: What are 30-year and 15-year fixed mortgage rates today?
  phrasing_ops: 3
  slug: tooloracle-io-real-estate-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Regulatory watch — US Federal Register + EU regulatory feeds
  name: FeedOracle Technologies Reg Watch Oracle API
  phrasing_intents:
  - id: regWatchOracleMcp
    intent: Watch regulations via the regwatch-oracle path
    question: Can my agent monitor the US Federal Register through the regwatch-oracle endpoint?
  - id: regwatchMcp
    intent: Follow EU and US regulatory feeds via /regwatch
    question: Is there a short /regwatch path that reads EU RSS regulatory feeds?
  phrasing_ops: 2
  slug: tooloracle-io-regwatchoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DORA NCA reporting MCP server. 14 tools, incident reports, RoI export, TLPT results, annual reports.
  name: FeedOracle Technologies Reporting Oracle API
  phrasing_intents:
  - id: reportingOracleMcp
    intent: Use the ReportingOracle MCP server
    question: What does the ReportingOracle MCP server do?
  phrasing_ops: 1
  slug: tooloracle-io-reportingoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: PDF reports (Pro+ tier)
  name: FeedOracle Technologies Reports API
  phrasing_intents:
  - id: getReportMica
    intent: Download the MiCA Article 66 PDF
    question: Can I download a MiCA Article 66 sustainability disclosure as a PDF?
  - id: getReportCsrd
    intent: Download the CSRD/ESRS PDF
    question: Can I get a CSRD sustainability report in ESRS format?
  - id: getReportDora
    intent: Download the DORA operational resilience PDF
    question: Can I download a DORA operational resilience report?
  - id: getReportsCatalog
    intent: List available reports
    question: What reports can I download?
  - id: getReportsDisclosure
    intent: Get the disclosure report
    question: Where can I view the disclosure report?
  - id: getReportsDisclosureJson
    intent: Get the disclosure report as JSON
    question: Can I get the disclosure report in machine-readable JSON?
  - id: getReportsAuditExport
    intent: Export the audit data
    question: Can I export the audit records for my auditors?
  phrasing_ops: 7
  slug: tooloracle-io-reports-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Scientific research intelligence — 200M+ papers, compliance topics
  name: FeedOracle Technologies Research Oracle API
  phrasing_intents:
  - id: researchOracleMcp
    intent: Search research papers via research-oracle
    question: Can my agent search 200M+ papers, arXiv and Crossref through the research-oracle endpoint?
  - id: researchMcp
    intent: Search Semantic Scholar via /research
    question: Is there a short /research path for Semantic Scholar paper search?
  phrasing_ops: 2
  slug: tooloracle-io-researchoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Gold/silver, RWA tokens (11 tools)
  name: FeedOracle Technologies Reserve Oracle API
  phrasing_intents:
  - id: reserveMcp
    intent: Check gold, silver and RWA token reserves over MCP
    question: Can my agent check gold and silver backed token reserves through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-reserveoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Product reviews (8 tools)
  name: FeedOracle Technologies Review Oracle API
  phrasing_intents:
  - id: reviewMcp
    intent: Look up product reviews over MCP
    question: Can my agent read product reviews through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-revieworacle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: RLUSD stablecoin transparency (Public)
  name: FeedOracle Technologies RLUSD API
  phrasing_intents:
  - id: getRlusdStatus
    intent: Check the RLUSD service status
    question: Is the RLUSD monitoring service up?
  - id: getCciCompact
    intent: Get RLUSD's compact CCI score
    question: What is RLUSD's CCI score in brief?
  - id: getCciDetailed
    intent: Get RLUSD's detailed CCI risk breakdown
    question: Can I see the full component breakdown behind RLUSD's CCI risk score?
  - id: getSupplyBreakdown
    intent: Get RLUSD supply by chain
    question: How much RLUSD is on each chain?
  - id: getPegQuality
    intent: Check RLUSD peg quality
    question: Is RLUSD holding its dollar peg?
  - id: getEvidenceLatest
    intent: Get the latest RLUSD evidence pack
    question: Can I download the latest evidence pack for RLUSD?
  - id: getHolders
    intent: Get RLUSD holder distribution
    question: Who holds RLUSD and how concentrated is it?
  - id: getWebhookEvents
    intent: List RLUSD webhook event types
    question: Which RLUSD webhook events can I subscribe to?
  phrasing_ops: 9
  slug: tooloracle-io-rlusd-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Webhook subscriptions for real-time notifications
  name: FeedOracle Technologies RWA Alerts API
  phrasing_intents:
  - id: getV1RwaAlerts
    intent: List RWA webhook subscriptions
    question: Which RWA alert webhooks have I set up?
  - id: postV1RwaAlertsSubscribe
    intent: Subscribe a webhook to RWA alerts
    question: How do I get webhook alerts when an RWA protocol changes?
  - id: deleteV1RwaAlertsById
    intent: Delete an RWA webhook subscription
    question: How do I stop receiving RWA alerts on a webhook?
  phrasing_ops: 3
  slug: tooloracle-io-rwa-alerts-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Real World Assets (Key required)
  name: FeedOracle Technologies RWA API
  phrasing_intents:
  - id: getRwaAssets
    intent: List tokenized real-world assets
    question: Which tokenized real-world assets are tracked?
  - id: getRwaAsset
    intent: Get one tokenized asset's details
    question: Can I see the details for one tokenized real-world asset?
  - id: getRwaTreasuries
    intent: List tokenized Treasury bill products
    question: Which tokenized T-bill products exist?
  - id: getRwaTreasuryTrust
    intent: Get trust scores for tokenized treasuries
    question: How trustworthy are the tokenized treasury products?
  - id: getRwaRedemptions
    intent: Get RWA redemption data
    question: How much is being redeemed from tokenized assets?
  - id: getRwaRedemptionStress
    intent: Get RWA redemption stress test results
    question: Could tokenized assets handle a wave of redemptions?
  - id: getRwaClassify
    intent: Get RWA classifications
    question: How are the tokenized assets classified?
  - id: getRwaStatus
    intent: Check the RWA system status
    question: Is the RWA data system running?
  phrasing_ops: 9
  slug: tooloracle-io-rwa-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Jurisdiction access, sanctions screening, MiCA/DORA/GENIUS status
  name: FeedOracle Technologies RWA Compliance API
  phrasing_intents:
  - id: getV1RwaCompliance
    intent: Get the compliance overview for all RWA protocols
    question: How do tokenized asset protocols compare on MiCA, DORA and sanctions screening?
  - id: getV1RwaComplianceBySlug
    intent: Get one RWA protocol's compliance profile
    question: What KYC level and investor requirements does a specific RWA protocol have?
  - id: getV1RwaComplianceJurisdictionByCode
    intent: List RWA protocols available in a jurisdiction
    question: Which tokenized asset protocols can investors in Singapore access?
  - id: getV1RwaComplianceCheck
    intent: Check cross-border access to an RWA protocol
    question: Can an investor in one country move into an RWA protocol based in another?
  - id: getV1RwaComplianceStats
    intent: Get RWA compliance statistics
    question: How many RWA protocols pass sanctions screening overall?
  phrasing_ops: 5
  slug: tooloracle-io-rwa-compliance-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Compliance document registry with source URLs and integrity hashes
  name: FeedOracle Technologies RWA Documents API
  phrasing_intents:
  - id: getV1RwaDocuments
    intent: Get the RWA document registry overview
    question: Which compliance documents are available per RWA protocol?
  - id: getV1RwaDocumentsBySlug
    intent: List one RWA protocol's documents
    question: Where can I find the attestation reports and prospectus for a tokenized fund?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-documents-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Chain-weighted carbon footprint scoring
  name: FeedOracle Technologies RWA ESG API
  phrasing_intents:
  - id: getV1RwaEsgBySlug
    intent: Get an RWA protocol's ESG carbon score
    question: What is the carbon footprint of a tokenized asset protocol?
  phrasing_ops: 1
  slug: tooloracle-io-rwa-esg-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Risk events, governance changes, anomaly alerts
  name: FeedOracle Technologies RWA Events API
  phrasing_intents:
  - id: getV1RwaEvents
    intent: List recent events across RWA protocols
    question: What has happened recently across tokenized asset protocols?
  - id: getV1RwaEventsBySlug
    intent: List events for one RWA protocol
    question: What events have occurred for a particular tokenized fund?
  - id: getV1RwaEventsStats
    intent: Get RWA event statistics
    question: How many RWA events have been recorded, and of what types?
  phrasing_ops: 3
  slug: tooloracle-io-rwa-events-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Historical score tracking and trend analysis
  name: FeedOracle Technologies RWA History API
  phrasing_intents:
  - id: getV1RwaHistory
    intent: Get score history for all RWA protocols
    question: How have RWA protocol risk scores changed over time?
  - id: getV1RwaHistoryBySlug
    intent: Get one RWA protocol's score timeline
    question: How has a specific protocol's score trended?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-history-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Contract powers, transfer finality, dispute resolution
  name: FeedOracle Technologies RWA Legal State API
  phrasing_intents:
  - id: getV1RwaLegalState
    intent: Get the legal structure of all RWA protocols
    question: How are tokenized asset protocols structured legally?
  - id: getV1RwaLegalStateBySlug
    intent: Get one RWA protocol's legal details
    question: Who holds contract powers and how are disputes resolved for a protocol?
  - id: getV1RwaLegalStateSearch
    intent: Search RWA legal states by keyword
    question: Which RWA protocols use a multisig or timelock?
  - id: getV1RwaLegalStateStats
    intent: Get RWA legal state statistics
    question: How common are different legal structures among RWA protocols?
  phrasing_ops: 4
  slug: tooloracle-io-rwa-legal-state-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: On-chain DEX liquidity depth and volume analysis
  name: FeedOracle Technologies RWA Liquidity API
  phrasing_intents:
  - id: getV1RwaLiquidity
    intent: Get DEX liquidity for all RWA protocols
    question: How much DEX liquidity do tokenized assets have?
  - id: getV1RwaLiquidityBySlug
    intent: Get detailed liquidity for one RWA protocol
    question: How liquid is a specific tokenized asset on DEXs?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-liquidity-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Smart contract transparency and activity verification
  name: FeedOracle Technologies RWA On-Chain API
  phrasing_intents:
  - id: getV1RwaOnchain
    intent: Get on-chain transparency for all RWA protocols
    question: How transparent are tokenized asset protocols on-chain?
  - id: getV1RwaOnchainBySlug
    intent: Get on-chain analysis for one RWA protocol
    question: What does on-chain data show about a specific tokenized fund?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-on-chain-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Multi-source consensus price feeds with disagreement detection
  name: FeedOracle Technologies RWA Oracle Feeds API
  phrasing_intents:
  - id: getV1RwaOracleFeedsBySlug
    intent: Get a consensus price for an RWA protocol
    question: What is the consensus price of a tokenized asset across Chainlink, Pyth and CoinGecko?
  - id: getV1RwaOracleStatus
    intent: Check RWA oracle infrastructure status
    question: Are the RWA price oracle sources healthy right now?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-oracle-feeds-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Time-to-Cash / institutional liquidity profiles (settlement, gates, fees)
  name: FeedOracle Technologies RWA Redemption API
  phrasing_intents:
  - id: getV1RwaRedemption
    intent: Compare redemption terms across RWA protocols
    question: How quickly can institutions exit tokenized assets, and with what gates?
  - id: getV1RwaRedemptionBySlug
    intent: Get time-to-cash for one RWA protocol
    question: How long does it take to redeem a specific tokenized fund for cash?
  phrasing_ops: 2
  slug: tooloracle-io-rwa-redemption-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Token metadata, issuer details, underlying asset classification (LEI, ISIN)
  name: FeedOracle Technologies RWA Registry API
  phrasing_intents:
  - id: getV1RwaRegistry
    intent: List identifiers for all RWA protocols
    question: Where can I get LEI and ISIN identifiers for tokenized assets?
  - id: getV1RwaRegistryBySlug
    intent: Get one RWA protocol's identifiers
    question: What are the token metadata and issuer details for a specific protocol?
  - id: getV1RwaRegistrySearch
    intent: Search the RWA registry by name, symbol or ISIN
    question: Can I look up a tokenized asset by its ISIN?
  - id: getV1RwaRegistryStats
    intent: Get RWA registry statistics
    question: How many protocols are in the RWA registry?
  phrasing_ops: 4
  slug: tooloracle-io-rwa-registry-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Multi-vector risk scores with letter grades (A-F) for 60+ tokenized asset protocols
  name: FeedOracle Technologies RWA Risk Scoring API
  phrasing_intents:
  - id: getV1RwaRisk
    intent: List risk scores for all RWA protocols
    question: What are the risk scores for tokenized asset protocols?
  - id: getV1RwaRiskBySlug
    intent: Get one RWA protocol's full risk profile
    question: What are the nine risk vector scores and reason codes for a protocol?
  - id: getV1RwaRiskBySlugPdf
    intent: Download an RWA protocol's PDF risk report
    question: Can I download a risk report as a PDF for a protocol?
  - id: getV1RwaMarket
    intent: Get the RWA market overview
    question: How big is the tokenized asset market overall?
  - id: getV1RwaDiscovery
    intent: List newly discovered RWA protocols
    question: Which new tokenized asset protocols were found on-chain but are not scored yet?
  phrasing_ops: 5
  slug: tooloracle-io-rwa-risk-scoring-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The security API from FeedOracle Technologies — 1 operation(s) for security.
  name: FeedOracle Technologies Security API
  phrasing_intents:
  - id: v2_cve_lookup
    intent: Search NIST NVD for CVEs
    question: Are there known CVEs for a product I'm running?
  phrasing_ops: 1
  slug: tooloracle-io-security-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: SEO intelligence (7 tools)
  name: FeedOracle Technologies SEO Oracle API
  phrasing_intents:
  - id: seoMcp
    intent: Get SEO intelligence over MCP
    question: Can my agent run SEO analysis through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-seooracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Live sports data (12 tools)
  name: FeedOracle Technologies Sport Oracle API
  phrasing_intents:
  - id: sportMcp
    intent: Get live sports data over MCP
    question: Can my agent get live sports scores through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-sportoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Stablecoin analytics covering 105+ coins — peg health, reserves, MiCA classification
  name: FeedOracle Technologies Stablecoin API
  phrasing_intents:
  - id: getApiV1FeedsStablecoin
    intent: Get data on the whole stablecoin universe
    question: Can I get market cap, peg status and risk scores for every stablecoin?
  - id: getApiV1FeedsStablecoinMeta
    intent: Get stablecoin feed metadata
    question: What sources does the stablecoin feed use and how often is it updated?
  - id: getApiV1FeedsStablecoinBySymbol
    intent: Get the status of a single stablecoin
    question: Is a particular stablecoin holding its peg?
  phrasing_ops: 3
  slug: tooloracle-io-stablecoin-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Stress API from FeedOracle Technologies — 3 operation(s) for stress.
  name: FeedOracle Technologies Stress API
  phrasing_intents:
  - id: getStress
    intent: Get the composite financial stress score
    question: How stressed are financial markets right now?
  - id: getVolatility
    intent: Get VIX volatility and regime
    question: What is the VIX at right now?
  - id: getExpectations
    intent: Get consumer inflation expectations
    question: What inflation do consumers expect?
  phrasing_ops: 3
  slug: tooloracle-io-stress-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Supply chain tracking (Key required)
  name: FeedOracle Technologies Supply Chain API
  phrasing_intents:
  - id: getSupplychainStatus
    intent: Check supply chain system status
    question: Is the supply chain tracking system running?
  - id: getSupplychainStats
    intent: Get supply chain statistics
    question: How many products and transfers are being tracked?
  - id: getSupplychainCarbon
    intent: Get supply chain carbon tracking
    question: What's the carbon footprint across the supply chain?
  - id: getSupplychainTransfers
    intent: List supply chain transfers
    question: What goods have changed hands recently?
  - id: getSupplychainProduct
    intent: Track one product through the supply chain
    question: Where is a specific product in the supply chain?
  - id: getSupplychainHealth
    intent: Check supply chain feed health
    question: Is the supply chain feed healthy?
  phrasing_ops: 6
  slug: tooloracle-io-supplychain-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DORA Art. 24-27 resilience testing MCP server. 16 tools, 12 scenarios, TLPT tracking, AmpelOracle sync.
  name: FeedOracle Technologies Test Oracle API
  phrasing_intents:
  - id: testOracleMcp
    intent: Manage DORA resilience testing over MCP
    question: Can I set up a DORA resilience testing programme through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-testoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Trading signals (Key required)
  name: FeedOracle Technologies Trading API
  phrasing_intents:
  - id: getTradingRadar
    intent: Get trading radar opportunities
    question: What trading opportunities are showing up in real time?
  - id: getTradingAlpha
    intent: Get alpha signals
    question: Are there any alpha signals right now?
  - id: getTradingBias
    intent: Get market bias indicators
    question: Is the market leaning bullish or bearish?
  - id: getTradingTokens
    intent: List tracked trading tokens
    question: Which tokens does the trading feed track?
  - id: getTradingAsset
    intent: Get trading data for one asset
    question: Can I get trading data for a single token?
  - id: getRsi
    intent: Get RSI indicators
    question: Which tokens look overbought or oversold on RSI?
  - id: getTreasury
    intent: Get treasury feed data
    question: What does the treasury data feed show?
  - id: getTrustCombined
    intent: Get the combined trust score
    question: What is the combined trust score?
  phrasing_ops: 8
  slug: tooloracle-io-trading-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: DORA ICT security awareness and training. 13 tools, 7 programmes, phishing simulation.
  name: FeedOracle Technologies Training Oracle API
  phrasing_intents:
  - id: trainingOracleMcp
    intent: Manage DORA ICT security training over MCP
    question: Is there an MCP server for DORA ICT security training?
  phrasing_ops: 1
  slug: tooloracle-io-trainingoracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Trust API from FeedOracle Technologies — 1 operation(s) for trust.
  name: FeedOracle Technologies Trust API
  phrasing_intents:
  - id: postQuantumMcp
    intent: Join the OracleNet mesh and check trust over MCP
    question: How can my agent join the OracleNet mesh in a single call?
  phrasing_ops: 1
  slug: tooloracle-io-trust-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Unified Integrity API from FeedOracle Technologies — 2 operation(s) for unified integrity.
  name: FeedOracle Technologies Unified Integrity API
  phrasing_intents:
  - id: getApiV1IntegrityRlusd
    intent: Run the RLUSD integrity check
    question: Is RLUSD holding its peg and fully reserved right now?
  - id: getApiV1IntegrityRlusdBaselines
    intent: Get RLUSD peg, reserve and CCI baselines
    question: What are the baseline peg, reserve and CCI values for RLUSD?
  phrasing_ops: 2
  slug: tooloracle-io-unified-integrity-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Generate, download, and verify cryptographically signed PDF evidence reports. Each report is hashed (SHA-256), signed (ECDSA secp256k1), and anchored on XRPL blockchain.
  name: FeedOracle Technologies Verified Reports API
  phrasing_intents:
  - id: postReportsApiReportGenerate
    intent: Generate a signed evidence report
    question: How do I generate a PDF evidence report anchored on the XRP Ledger?
  phrasing_ops: 1
  slug: tooloracle-io-verified-reports-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Unit-based billing — check balance, view packages, purchase units via Stripe
  name: FeedOracle Technologies Wallet API
  phrasing_intents:
  - id: getWalletBalance
    intent: Check my API key's unit balance
    question: How many units are left on my API key?
  - id: postWalletStripeCheckout
    intent: Buy a unit package via Stripe checkout
    question: How do I buy more units for my API key?
  phrasing_ops: 2
  slug: tooloracle-io-wallet-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Real-time weather (10 tools)
  name: FeedOracle Technologies Weather Oracle API
  phrasing_intents:
  - id: weatherMcp
    intent: Get real-time weather over MCP
    question: Can my agent get real-time weather through MCP?
  phrasing_ops: 1
  slug: tooloracle-io-weatheroracle-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The x402 API from FeedOracle Technologies — 1 operation(s) for x402.
  name: FeedOracle Technologies X402 API
  phrasing_intents:
  - id: xrplPaidMcp
    intent: Run the paid RLUSD integrity check over x402
    question: Can I pay per call in USDC on Base to run the RLUSD integrity check?
  phrasing_ops: 1
  slug: tooloracle-io-x402-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: XRP/RLUSD feeds (Key required)
  name: FeedOracle Technologies XRP API
  phrasing_intents:
  - id: getXrpRlusd
    intent: Get RLUSD stablecoin metrics
    question: What are the latest Ripple USD stablecoin metrics?
  - id: getXrpMarket
    intent: Get XRP market data
    question: What is XRP trading at?
  - id: getXrpRwa
    intent: Get XRP Ledger RWA tokenization data
    question: What real-world assets are tokenized on the XRP Ledger?
  - id: getXrpWhale
    intent: Track XRP whale activity
    question: Are XRP whales moving large amounts?
  - id: getXrpHealth
    intent: Check XRP feed health
    question: Is the XRP data feed healthy?
  phrasing_ops: 5
  slug: tooloracle-io-xrp-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The XRPL API from FeedOracle Technologies — 2 operation(s) for xrpl.
  name: FeedOracle Technologies XRPL API
  phrasing_intents:
  - id: postXrplMcp
    intent: Use the free XRP Ledger and RLUSD MCP server
    question: Is there a free MCP server with all 31 XRP Ledger and RLUSD tools, not just the paid integrity check?
  - id: xrplPaidMcp
    intent: Run the paid RLUSD integrity check over x402
    question: Can I pay per call in USDC on Base to run the RLUSD integrity check?
  phrasing_ops: 2
  slug: tooloracle-io-xrpl-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: The Yields API from FeedOracle Technologies — 3 operation(s) for yields.
  name: FeedOracle Technologies Yields API
  phrasing_intents:
  - id: getYieldCurve
    intent: Get the full Treasury yield curve
    question: What does the Treasury yield curve look like from 1 month to 30 years?
  - id: getYieldSpreads
    intent: Get yield curve spreads and inversion signals
    question: What are the 3-month to 10-year and 5s30s spreads?
  - id: getYieldTIPS
    intent: Get TIPS real yields and breakevens
    question: What are real yields on TIPS?
  phrasing_ops: 3
  slug: tooloracle-io-yields-api
- baseURL: https://tooloracle.io/mcp/
  baseurl_source: declared
  description: Zero-knowledge evidence layer. Privacy-preserving proofs, merkle trees, verifiable credentials, selective disclosure.
  name: FeedOracle Technologies ZK Evidence Oracle API
  phrasing_intents:
  - id: zkOracleMcp
    intent: Use the zero-knowledge evidence MCP server
    question: Is there an MCP server for zero-knowledge evidence?
  phrasing_ops: 1
  slug: tooloracle-io-zkevidenceoracle-api
artifact_total: 133
asyncapis:
- description: ''
  name: Tooloracle Io Webhooks
  slug: tooloracle-io-webhooks
common:
- group: other
  href: https://artifacts.apis.io/tooloracle-io/capabilities/tooloracle-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tooloracle-io-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/tooloracle-io/overlays/tooloracle-io-mcp-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tooloracle-io-mcp-platform-overlay.yaml
- group: other
  href: https://artifacts.apis.io/tooloracle-io/overlays/tooloracle-io-x402-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tooloracle-io-x402-v2-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tooloracle-io/skills/tooloracle-io-pay-per-call-x402-v2.md
  title: ''
  type: AgentSkill
  url: skills/tooloracle-io-pay-per-call-x402-v2.md
- group: other
  href: https://artifacts.apis.io/tooloracle-io/overlays/tooloracle-io-feedoracle-compliance-evidence-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tooloracle-io-feedoracle-compliance-evidence-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/tooloracle-io/security/tooloracle-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tooloracle-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tooloracle-io/security/tooloracle-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tooloracle-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tooloracle.io/
- group: company
  title: ''
  type: Website
  url: https://feedoracle.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tooloracle.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://tooloracle.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://tooloracle.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://tooloracle.io/docs/mcp-auth.html
- group: operate
  title: ''
  type: Support
  url: https://feedoracle.io/contact.html
- group: company
  title: ''
  type: Blog
  url: https://tooloracle.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ToolOracle
- group: commercial
  title: ''
  type: Pricing
  url: https://tooloracle.io/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://feedoracle.io/console/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tooloracle.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tooloracle.io/datenschutz.html
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.feedoracle.io/status/feedoracle
- group: agent
  href: https://artifacts.apis.io/tooloracle-io/llms/tooloracle-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tooloracle-io-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://tooloracle.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/tooloracle-io/mcp/tooloracle-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tooloracle-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/tooloracle-io/mcp/tooloracle-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tooloracle-io-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/tooloracle-io/a2a/tooloracle-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/tooloracle-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/tooloracle-io/well-known/tooloracle-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tooloracle-io-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tooloracle-io/well-known/tooloracle-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tooloracle-io-security.txt
- group: other
  href: https://artifacts.apis.io/tooloracle-io/well-known/tooloracle-io-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/tooloracle-io-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/tooloracle-io/authentication/tooloracle-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tooloracle-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tooloracle-io/scopes/tooloracle-io-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tooloracle-io-scopes.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/conformance/tooloracle-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tooloracle-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/errors/tooloracle-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tooloracle-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/lifecycle/tooloracle-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tooloracle-io-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tooloracle-io/changelog/tooloracle-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tooloracle-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/conventions/tooloracle-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tooloracle-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/conventions/tooloracle-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/tooloracle-io-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tooloracle-io/rate-limits/tooloracle-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tooloracle-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tooloracle-io/plans/tooloracle-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tooloracle-io-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/tooloracle-io/sandbox/tooloracle-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tooloracle-io-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/data-model/tooloracle-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tooloracle-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/tooloracle-io/asyncapi/tooloracle-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tooloracle-io-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/tooloracle-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://tooloracle.io/responsible-disclosure
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://tooloracle.io/datenschutz.html
- group: other
  title: ''
  type: Subprocessors
  url: https://feedoracle.io/assets/dpa-feedoracle.html
- group: other
  title: ''
  type: DataResidency
  url: https://tooloracle.io/datenschutz.html
- group: operate
  title: ''
  type: IncidentNotification
  url: https://feedoracle.io/assets/dpa-feedoracle.html
- group: other
  title: ''
  type: AITransparency
  url: https://tooloracle.io/terms.html
- group: other
  href: https://artifacts.apis.io/tooloracle-io/regulatory/tooloracle-io-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/tooloracle-io-regulatory-posture.yml
- group: build
  href: https://artifacts.apis.io/tooloracle-io/packages/tooloracle-io-packages.yml
  title: ''
  type: Packages
  url: packages/tooloracle-io-packages.yml
created: '2026-09-19'
description: FeedOracle Technologies (Herford, Germany) operates two agent-facing brands on one shared OAuth 2.1 identity layer. ToolOracle / OracleNet at tooloracle.io is a capability router and hosted mesh of about ninety Model Context Protocol servers for autonomous agents (1,178 tool entries across blockchain intelligence, EU regulatory compliance, finance, business intelligence, travel and agent trust), reachable over MCP Streamable HTTP, an A2A 0.3 agent with a published Agent Card, a free ANP soft-handshake router, and x402 v2 pay-per-call settlement in USDC on Base for eighteen priced /v2 compliance and agent-safety REST routes. FeedOracle at feedoracle.io is the sibling compliance-evidence API (227-path OpenAPI 3.1 at api.feedoracle.io, ES256K-signed responses) and hosts the RFC 8414 / RFC 7591 authorization server both brands use.
finops:
- has_sources: true
  method: derived
  name: Tooloracle Io Finops
  primary_unit: call
  service_category: ''
  slug: tooloracle-io-finops
  template: false
image: https://tooloracle.io/favicon.ico
layout: provider
mcp_servers:
- description: 'ToolOracle / OracleNet is not one MCP server but a hosted mesh: 92 distinct endpoints under tooloracle.io (plus five on feedoracle.io / mcp.feedoracle.io) answered an anonymous tools/list with 1178 to'
  name: FeedOracle Technologies MCP Server
  slug: tooloracle-io-mcp-yml
- description: ''
  name: OracleNet mesh front door (quantum)
  slug: oraclenet-mesh-front-door-quantum
modified: '2026-09-19'
name: FeedOracle Technologies
nav: Providers
network: true
overview: 'FeedOracle Technologies publishes 119 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Readiness API, Agent Safety API, Agent Trust Management API, and 116 more. Tagged areas include Company, MCP, Agent Infrastructure, A2A, and x402.


  The FeedOracle Technologies catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  FeedOracle Technologies'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Tooloracle Io Plans Pricing
  plan_count: 17
  slug: tooloracle-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Tooloracle Io Rate Limits
  slug: tooloracle-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: FeedOracle Technologies API Rules
  rule_count: 57
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 11
  slug: tooloracle-io-rules
scopes:
- name: Tooloracle Io Scopes
  scope_count: 8
  slug: tooloracle-io-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 32
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 61.8
    contract_governance: 31.8
    contract_quality: 59.8
    developer_ergonomics: 45.2
    discoverability: 80.0
    operational_transparency: 71.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 73.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 96.6
      total: 117
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 52.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tooloracle-io/tooloracle-io-2026-10-11T131011.png
security:
- kind: authentication
  name: Tooloracle Io Authentication
  slug: tooloracle-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Tooloracle Io Domain Security
  slug: tooloracle-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tooloracle Io Vulnerability Disclosure
  slug: tooloracle-io-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Route an intent through OracleNet and call the tool (free-first)
  slug: tooloracle-io-free-first-route-and-call
- name: oraclenet-mesh
  slug: tooloracle-io-oraclenet-mesh-SKILL
- name: Buy one compliance or safety verdict with x402 v2
  slug: tooloracle-io-pay-per-call-x402-v2
slug: tooloracle-io
tags:
- Company
- MCP
- Agent Infrastructure
- A2A
- x402
- Micropayments
- Compliance
- RegTech
- Blockchain
- Sanctions Screening
- Agent Discovery
- Germany
website: https://tooloracle.io/
---
