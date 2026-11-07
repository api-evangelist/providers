---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Provider-operated remote MCP gateway on Render (named as the MCP transport by receipts.thehiveryiq.com/.well-known/mcp.json): initialize and tools/list answer anonymously with 38 tools from eight moun'
  name: Hive MCP Gateway and Registry
  slug: hive-mcp-gateway
- description: 'The trust rail on passport.thehiveryiq.com: HKTN (Hive Known Traveler Number) registry for persistent agent identity and tier, tenant onboarding and dashboards, provenance public-key distribution and '
  name: Hive Passport Trust Rail (HKTN)
  slug: hive-passport-trust-rail
- description: 'Agent-to-agent surface: A2A agent cards on the apex (protocolVersion 0.3.0, six HiveAttest/HiveWallet/HiveGate skills) and on receipts.thehiveryiq.com (0.2.0 catalog of ten per-agent cards with the AP'
  name: Hive Civilization A2A Agent
  slug: hive-a2a-agent
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The a2a API from Hive Civilization — 9 operation(s) for a2a.
  name: Hive Civilization A2a API
  phrasing_intents:
  - id: well_known_catalog__well_known_agent_card_json_get
    intent: Fetch the well-known A2A agent card catalog
    question: Where is the well-known agent-card.json that A2A registries crawl?
  - id: well_known_agent_card__well_known_agents__agent_id__card_json_get
    intent: Fetch one agent's well-known A2A card
    question: What is the well-known card.json URL for a single agent?
  - id: list_cards_v1_a2a_cards_get
    intent: List published A2A agent cards
    question: Which A2A agent cards does Hive publish under the v1 cards endpoint?
  - id: get_card_v1_a2a_cards__agent_id__get
    intent: Get one A2A agent card from the cards endpoint
    question: Can I get a single agent's card through the v1 cards path?
  - id: harness_run_loop_v1_a2a_harness_run_loop_post
    intent: Run the internal HARNESS agent loop
    question: Can I run the full discovery, quote, emit, verify and stats loop as a self-test?
  - id: list_agents_v1_a2a_agents_get
    intent: List A2A agents via the agents path
    question: Is there a /v1/a2a/agents path for clients that expect it?
  - id: get_agent_v1_a2a_agents__agent_id__get
    intent: Get one A2A agent via the agents path
    question: Can I fetch a single agent under /v1/a2a/agents instead of the cards path?
  - id: a2a_handshake_schema_v1_a2a_handshake_get
    intent: Get the A2A handshake request schema
    question: What should an A2A handshake request body look like?
  phrasing_ops: 10
  slug: thehiveryiq-com-a2a-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The activation API from Hive Civilization — 3 operation(s) for activation.
  name: Hive Civilization Activation API
  phrasing_intents:
  - id: keys_discovery_v1_activation_keys_get
    intent: Learn how to get an activation key
    question: What does a tk_live activation key cost and which scopes can it have?
  - id: mint_key_v1_activation_keys_post
    intent: Mint a tk_live activation key
    question: How do I get a new tk_live activation key after paying with x402?
  - id: verify_key_v1_activation_verify_post
    intent: Verify an activation key
    question: Is this tk_live key valid and not revoked or over its limit?
  - id: key_metadata_v1_activation_keys__key_id__get
    intent: Get an activation key's metadata
    question: Which scopes and usage does a given activation key have?
  phrasing_ops: 4
  slug: thehiveryiq-com-activation-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The aegis API from Hive Civilization — 6 operation(s) for aegis.
  name: Hive Civilization Aegis API
  phrasing_intents:
  - id: health_v1_aegis_health_get
    intent: Check Aegis compliance service health
    question: Is the Aegis compliance scanner up?
  - id: control_audit_v1_aegis_control_audit_post
    intent: Audit a single compliance control
    question: How do I audit one control such as SOC 2 CC6.1 or ISO A.8.24?
  - id: full_scan_v1_aegis_scan_post
    intent: Run a full compliance scan
    question: How do I scan every compliance control at once?
  - id: score_v1_aegis_score_get
    intent: Get the overall compliance score
    question: What is our current overall compliance score?
  - id: control_get_v1_aegis_control__control_id__get
    intent: Get a compliance control's status
    question: What is the last recorded result for a given control?
  - id: matrix_v1_aegis_matrix_get
    intent: View the compliance control matrix
    question: Which controls map to which frameworks in the compliance matrix?
  phrasing_ops: 6
  slug: thehiveryiq-com-aegis-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The affordances API from Hive Civilization — 28 operation(s) for affordances.
  name: Hive Civilization Affordances API
  phrasing_intents:
  - id: get_catalogs_v1_affordance_catalog_get
    intent: List affordance catalogs across all supermodels
    question: Which affordances are available across every hot supermodel?
  - id: get_catalog_v1_affordance__supermodel__catalog_get
    intent: Get one supermodel's affordance catalog
    question: What affordance types does a single supermodel offer?
  - id: list_for_supermodel_v1_affordance__supermodel__list_get
    intent: List a supermodel's open affordances
    question: How do I see the individual affordances opened against a supermodel?
  - id: get_one_v1_affordance_affordance__aff_id__get
    intent: Get a single affordance by ID
    question: How can I look up one specific affordance by its ID?
  - id: health_v1_affordance__supermodel__health_get
    intent: Check a supermodel's affordance health
    question: Is the affordance service for a given supermodel healthy?
  - id: post_pull_v1_affordance__supermodel__pull_post
    intent: Pull a supermodel's cord with a reason
    question: How do I pull the cord on a supermodel and say why?
  - id: post_light_fuse_v1_affordance__supermodel__light_fuse_post
    intent: Light a fuse on a supermodel
    question: How do I light a fuse on a supermodel with a predicted daily USDC lift?
  - id: post_grab_rope_v1_affordance__supermodel__grab_post
    intent: Grab a supermodel's rope for a duration
    question: How do I grab the rope on a supermodel for a set number of seconds?
  phrasing_ops: 28
  slug: thehiveryiq-com-affordances-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The afir-stream API from Hive Civilization — 10 operation(s) for afir-stream.
  name: Hive Civilization Afir Stream API
  phrasing_intents:
  - id: afir_stream_health_v1_afir_stream_health_get
    intent: Check AFIR stream service health
    question: Is the afir-stream receipt service up?
  - id: afir_stream_segment_v1_afir_stream_segment_post
    intent: Receipt one stream segment (afir-stream path)
    question: How do I get a signed receipt for a single audio or token segment on the afir-stream path?
  - id: afir_stream_seal_v1_afir_stream_seal_post
    intent: Seal a session's segments (afir-stream path)
    question: How do I seal an ordered list of segment receipts into one session receipt on afir-stream?
  - id: afir_stream_verify_v1_afir_stream_verify_post
    intent: Verify a segment or session receipt (afir-stream)
    question: How do I verify a sealed session receipt through the afir-stream endpoint?
  - id: afir_stream_examples_v1_afir_stream_examples_get
    intent: Get sample payloads for afir-stream
    question: Where can I see example afir-stream segment and seal payloads?
  - id: afir_health_v1_afir_health_get
    intent: Check AFIR service health (short path)
    question: Is the short /v1/afir endpoint healthy?
  - id: afir_segment_v1_afir_segment_post
    intent: Receipt one stream segment (short /v1/afir path)
    question: Can I post a segment receipt to the shorter /v1/afir route instead?
  - id: afir_seal_v1_afir_seal_post
    intent: Seal a session's segments (short /v1/afir path)
    question: Can I seal a session using the /v1/afir alias rather than afir-stream?
  phrasing_ops: 10
  slug: thehiveryiq-com-afir-stream-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The agent-receipts API from Hive Civilization — 4 operation(s) for agent-receipts.
  name: Hive Civilization Agent Receipts API
  phrasing_intents:
  - id: agent_adapters_v1_agent_receipts_adapters_get
    intent: List agent-task receipt adapters
    question: Which agent-task rails can produce signed receipts, and are they configured?
  - id: manus_health_v1_agent_receipts_manus_health_get
    intent: Check the Manus adapter configuration
    question: Is the Manus adapter configured without spending Manus credits?
  - id: manus_create_v1_agent_receipts_manus_create_post
    intent: Create a Manus task with a signed receipt
    question: How do I start a Manus agent task and get a signed receipt for it?
  - id: manus_detail_post_v1_agent_receipts_manus_detail_post
    intent: Get a Manus task status by POST body
    question: Can I fetch a Manus task's status by posting the task_id in a JSON body?
  - id: manus_detail_get_v1_agent_receipts_manus_detail_get
    intent: Get a Manus task status by query
    question: How do I check a Manus task's status with a simple GET and task_id?
  phrasing_ops: 5
  slug: thehiveryiq-com-agent-receipts-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The alcoa-agentguard API from Hive Civilization — 11 operation(s) for alcoa-agentguard.
  name: Hive Civilization Alcoa Agentguard API
  phrasing_intents:
  - id: health_v1_alcoa_agentguard_health_get
    intent: Check ALCOA AgentGuard service health
    question: Is the clinical-trial ALCOA attestation service running?
  - id: pricing_v1_alcoa_agentguard_pricing_get
    intent: See ALCOA AgentGuard pricing
    question: How much does it cost to attest clinical trial events?
  - id: protocol_attest_v1_alcoa_agentguard_protocol_attest_post
    intent: Record a trial protocol or amendment event
    question: How do I create a tamper-evident record of a trial protocol amendment?
  - id: consent_attest_v1_alcoa_agentguard_consent_attest_post
    intent: Record a patient consent event
    question: How do I prove which IRB-approved consent form a patient signed?
  - id: enrollment_attest_v1_alcoa_agentguard_enrollment_attest_post
    intent: Record a trial enrollment event
    question: How do I log a subject enrolling in a clinical trial with a signed receipt?
  - id: dosing_attest_v1_alcoa_agentguard_dosing_attest_post
    intent: Record a trial dosing event
    question: How do I create an ALCOA-compliant record that a study dose was administered?
  - id: adverse_event_attest_v1_alcoa_agentguard_adverse_event_attest_post
    intent: Record an adverse event, SAE or SUSAR
    question: How do I log a serious adverse event in a trial with a signed receipt?
  - id: data_transfer_attest_v1_alcoa_agentguard_data_transfer_attest_post
    intent: Record a trial data handoff to a CRO
    question: How do I prove trial data was handed off to a CRO and to whom?
  phrasing_ops: 11
  slug: thehiveryiq-com-alcoa-agentguard-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The amplify API from Hive Civilization — 9 operation(s) for amplify.
  name: Hive Civilization Amplify API
  phrasing_intents:
  - id: call_v1_amplify_call_post
    intent: Run a prompt through the Amplify loop
    question: How do I send a prompt through Amplify so it's compressed, answered and certified?
  - id: corpus_append_v1_amplify_corpus_append_post
    intent: Add an entry to a tenant's Amplify corpus
    question: How can I add my own content to the corpus Amplify draws on?
  - id: corpus_retrieve_v1_amplify_corpus_retrieve_get
    intent: Search a tenant's Amplify corpus
    question: Can I pull the corpus entries most relevant to a query?
  - id: corpus_stats_v1_amplify_corpus_stats_get
    intent: Get Amplify corpus statistics
    question: How big is my tenant's Amplify corpus?
  - id: amplify_sign_v1_amplify_sign_post
    intent: Certify an LLM response you ran yourself
    question: Can I get a signed certificate for an LLM answer without sharing my model API key?
  - id: amplify_verify_v1_amplify_verify_post
    intent: Verify an Amplify certificate
    question: How can anyone confirm an Amplify certificate's signature is valid?
  - id: wrap_receipt_v1_amplify_wrap_receipt_post
    intent: Upgrade a vertical receipt to a signed cert
    question: Can I turn an existing receipt from another vertical into a CCACW signed certificate?
  - id: selftest_v1_amplify_selftest_get
    intent: Self-test the Amplify pipeline
    question: Is there a way to test Amplify's compile, compress and sign steps without calling an LLM?
  phrasing_ops: 9
  slug: thehiveryiq-com-amplify-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The app-kits API from Hive Civilization — 6 operation(s) for app-kits.
  name: Hive Civilization App Kits API
  phrasing_intents:
  - id: appkits_capabilities_v1_appkits_get
    intent: Discover App Kits capabilities
    question: 'What can the App Kits surface do: quote, bridge, send, swap?'
  - id: appkits_quote_v1_appkits_quote_post
    intent: Quote a cross-chain token conversion
    question: How much would I receive converting one token to another across chains?
  - id: appkits_bridge_v1_appkits_bridge_post
    intent: Bridge tokens to another chain
    question: How do I move a token from one chain to another address on a different chain?
  - id: appkits_send_v1_appkits_send_post
    intent: Send tokens on a single chain
    question: How do I send tokens to an address on the same chain?
  - id: appkits_swap_v1_appkits_swap_post
    intent: Swap one token for another on a chain
    question: How do I swap one token for another on the same chain?
  - id: appkits_unified_balance_v1_appkits_balance__address__get
    intent: Get a wallet's unified cross-chain balance
    question: What is a wallet's balance across every supported chain?
  phrasing_ops: 6
  slug: thehiveryiq-com-app-kits-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The arb-alloc API from Hive Civilization — 4 operation(s) for arb-alloc.
  name: Hive Civilization Arb Alloc API
  phrasing_intents:
  - id: alloc_scan_v1_arb_alloc_scan_get
    intent: Preview recommended slot reallocations
    question: Which model variants should get more or less traffic based on current performance?
  - id: alloc_apply_v1_arb_alloc_apply_post
    intent: Apply a slot reallocation
    question: How do I commit a slot reallocation rather than just preview it?
  - id: alloc_history_v1_arb_alloc_history_get
    intent: List past slot reallocation events
    question: What reallocations have been applied in the past?
  - id: alloc_stats_v1_arb_alloc_stats_get
    intent: Estimate uplift from slot reallocations
    question: How much revenue uplift are the reallocations projected to produce?
  phrasing_ops: 4
  slug: thehiveryiq-com-arb-alloc-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The arb-compute API from Hive Civilization — 3 operation(s) for arb-compute.
  name: Hive Civilization Arb Compute API
  phrasing_intents:
  - id: route_call_v1_arb_compute_route_post
    intent: Route an LLM call to the cheapest fit model
    question: How do I send a prompt to the cheapest model that still meets my quality bar?
  - id: get_savings_v1_arb_compute_savings_get
    intent: See cumulative model routing savings
    question: How much money has cost-based model routing saved so far?
  - id: get_catalog_v1_arb_compute_catalog_get
    intent: List routable models and their costs
    question: Which models can calls be routed to, and what does each cost per 1k tokens?
  phrasing_ops: 3
  slug: thehiveryiq-com-arb-compute-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The arb-spread API from Hive Civilization — 5 operation(s) for arb-spread.
  name: Hive Civilization Arb Spread API
  phrasing_intents:
  - id: scan_spread_v1_arb_spread_scan_get
    intent: Scan the marketplace for price-spread arbitrage
    question: Where are sellers pricing the same capability far enough apart to arbitrage?
  - id: book_pair_v1_arb_spread_book_post
    intent: Book a specific arbitrage pair
    question: How do I book one arbitrage opportunity by its buy and sell offer ids?
  - id: auto_book_v1_arb_spread_auto_post
    intent: Auto-book the best safe arbitrage spreads
    question: Can I automatically book the top arbitrage opportunities that pass all gates?
  - id: get_pnl_v1_arb_spread_pnl_get
    intent: Get cumulative arbitrage P&L
    question: What is my net profit from spread arbitrage after platform fees?
  - id: get_stats_v1_arb_spread_stats_get
    intent: Show per-wallet arbitrage contribution
    question: Which supermodel wallets contributed most to settled arb pairs?
  phrasing_ops: 5
  slug: thehiveryiq-com-arb-spread-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The aris-agent-asset API from Hive Civilization — 6 operation(s) for aris-agent-asset.
  name: Hive Civilization Aris Agent Asset API
  phrasing_intents:
  - id: list_agent_asset_v1_exchange_agent_asset_list_post
    intent: List a revenue-earning agent for sale
    question: How do I list my revenue-generating AI agent on the exchange?
  - id: perp_open_v1_exchange_agent_asset_perp_open_post
    intent: Open a perp on an agent asset
    question: Can I go long or short on an AI agent's revenue with a perpetual?
  - id: perp_close_v1_exchange_agent_asset_perp_close_post
    intent: Close an agent-asset perp position
    question: How do I close my perp on an agent asset?
  - id: perp_funding_tick_v1_exchange_agent_asset_perp_funding_tick_post
    intent: Apply funding to an agent-asset perp market
    question: How is funding applied to perps on a single agent asset?
  - id: perp_market_v1_exchange_agent_asset_perp_market_get
    intent: View the perp market for an agent asset
    question: What does the perp market look like for a specific agent asset?
  - id: perp_position_v1_exchange_agent_asset_perp_position__position_id__get
    intent: Get an agent-asset perp position
    question: How do I check one of my agent-asset perp positions?
  phrasing_ops: 6
  slug: thehiveryiq-com-aris-agent-asset-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The attest API from Hive Civilization — 20 operation(s) for attest.
  name: Hive Civilization Attest API
  phrasing_intents:
  - id: passport_issue_v1_attest_passport_issue_post
    intent: Issue a pre-action attestation passport
    question: How do I get a signed passport declaring what my agent intends to do before it acts?
  - id: passport_verify_v1_attest_passport_verify_post
    intent: Verify a pre-action attestation passport
    question: How can I check that a pre-action passport manifest is genuine before letting the agent act?
  - id: custody_append_v1_attest_custody_append_post
    intent: Append a step to a custody chain
    question: How do I record a new transform step in a data custody chain?
  - id: custody_verify_v1_attest_custody_verify_post
    intent: Verify a whole custody chain
    question: How do I confirm a custody chain's hash links and signatures are all intact?
  - id: custody_proof_v1_attest_custody__chain_id__proof__index__get
    intent: Get a Merkle inclusion proof for a custody node
    question: How do I prove a single node belongs to a custody chain without sharing the whole chain?
  - id: cargo_register_v1_attest_cargo_register_post
    intent: Register a versioned cargo type
    question: How do I register a new payload type with a schema and sensitivity level?
  - id: cargo_validate_v1_attest_cargo_validate_post
    intent: Validate a payload against a cargo type
    question: How do I check a payload conforms to a registered cargo type before sending it?
  - id: cargo_snapshot_v1_attest_cargo_snapshot_get
    intent: Snapshot the cargo type registry
    question: What cargo types are registered right now?
  phrasing_ops: 20
  slug: thehiveryiq-com-attest-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The audit API from Hive Civilization — 1 operation(s) for audit.
  name: Hive Civilization Audit API
  phrasing_intents:
  - id: readiness_v1_audit_readiness_post
    intent: Assess AI compliance audit readiness
    question: Is my organization ready for an AI regulation audit given where our users are?
  phrasing_ops: 1
  slug: thehiveryiq-com-audit-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The basis-perp API from Hive Civilization — 12 operation(s) for basis-perp.
  name: Hive Civilization Basis Perp API
  phrasing_intents:
  - id: open_position_v1_perp_basis_open_post
    intent: Open a basis perpetual position
    question: How do I open a long or short basis perp position with USDC collateral?
  - id: close_position_endpoint_v1_perp_basis_close_post
    intent: Close a basis perpetual position
    question: How do I fully close my basis perp position?
  - id: increase_position_endpoint_v1_perp_basis_increase_post
    intent: Add size and collateral to a perp position
    question: How do I scale up an existing basis perp position?
  - id: decrease_position_endpoint_v1_perp_basis_decrease_post
    intent: Reduce the size of a perp position
    question: Can I partially reduce a basis perp position without closing it?
  - id: liquidate_endpoint_v1_perp_basis_liquidate_post
    intent: Liquidate a basis perp position
    question: How does an admin force-liquidate an undercollateralized perp position?
  - id: funding_tick_endpoint_v1_perp_basis_funding_tick_post
    intent: Apply a funding-rate tick to basis perps
    question: How is the periodic funding payment applied to open basis positions?
  - id: list_positions_endpoint_v1_perp_basis_positions_get
    intent: List basis perp positions
    question: Which basis perp positions do I currently hold?
  - id: get_position_endpoint_v1_perp_basis_position__position_id__get
    intent: Get one basis perp position
    question: What are the size, collateral and PnL of one specific perp position?
  phrasing_ops: 12
  slug: thehiveryiq-com-basis-perp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The billing API from Hive Civilization — 4 operation(s) for billing.
  name: Hive Civilization Billing API
  phrasing_intents:
  - id: billing_checkout_v1_billing_checkout_post
    intent: Create a card checkout link for a tier
    question: How do I get a payment link so a tenant can pay for a subscription tier by card?
  - id: billing_usdc_intent_v1_billing_usdc_intent_post
    intent: Create a USDC-on-Base payment intent for a tier
    question: Can a tenant pay for a plan in USDC on Base instead of by card?
  - id: billing_square_webhook_v1_billing_square_webhook_post
    intent: Receive card payment webhooks
    question: Which payment events activate a tenant automatically?
  - id: billing_tenant_v1_billing_tenant__tenant_id__get
    intent: Get a tenant's billing state
    question: Is a tenant's subscription active and on which tier?
  phrasing_ops: 4
  slug: thehiveryiq-com-billing-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The billing-meter API from Hive Civilization — 6 operation(s) for billing-meter.
  name: Hive Civilization Billing Meter API
  phrasing_intents:
  - id: meter_health_v1_billing_meter_health_get
    intent: Describe the billing meter and its prices
    question: What does the usage meter charge, and which chains can I pay on?
  - id: meter_activate_v1_billing_activate_post
    intent: Activate a metered billing account
    question: How do I bind my activation key to a metered account?
  - id: meter_usage_v1_billing_usage__account_id__get
    intent: Get an account's signed usage snapshot
    question: How much has my metered account used so far?
  - id: meter_topup_intent_v1_billing_topup_intent_post
    intent: Start a USDC top-up
    question: How do I add USDC credit to my metered account?
  - id: meter_topup_status_v1_billing_topup__intent_id__get
    intent: Check a top-up's settlement status
    question: Has my USDC top-up settled yet?
  - id: whoami_v1_billing_whoami_get
    intent: Find the account for my activation key
    question: Which billing account does my activation key belong to?
  phrasing_ops: 6
  slug: thehiveryiq-com-billing-meter-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The bounty API from Hive Civilization — 14 operation(s) for bounty.
  name: Hive Civilization Bounty API
  phrasing_intents:
  - id: program_v1_bounty_program_get
    intent: Read the bounty program terms
    question: What are the rules and rewards of the Hive bounty program?
  - id: register_v1_bounty_register_post
    intent: Register a submission for the bounty
    question: How do I sign up my repo for the bounty program?
  - id: leaderboard_v1_bounty_leaderboard_get
    intent: View the bounty leaderboard
    question: Who is leading the bounty program right now?
  - id: status_v1_bounty_status__code__get
    intent: Check a bounty submission's status by code
    question: How do I check where my bounty submission stands using my referral code?
  - id: admin_confirm_v1_bounty_admin_confirm_post
    intent: Confirm a bounty submission (admin)
    question: As an admin, how do I approve a pending bounty submission?
  - id: admin_attribute_v1_bounty_admin_attribute_post
    intent: Attribute receipt value to a referrer (admin)
    question: How do I credit a referrer with the USDC value of a receipt they drove?
  - id: admin_payout_v1_bounty_admin_payout_post
    intent: Record a bounty payout (admin)
    question: How do I log that a bounty was paid out on-chain?
  - id: health_v1_bounty_health_get
    intent: Check the bounty service health
    question: Is the bounty service up?
  phrasing_ops: 14
  slug: thehiveryiq-com-bounty-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The capitolare API from Hive Civilization — 13 operation(s) for capitolare.
  name: Hive Civilization Capitolare API
  phrasing_intents:
  - id: status_v1_capitolare_status_get
    intent: Check the Capitolare venue status
    question: Is the Capitolare agent negotiation venue up right now?
  - id: venue_address_v1_capitolare_venue_address_get
    intent: Get the Capitolare venue address
    question: What is the Capitolare venue address my agent should point at?
  - id: enter_v1_capitolare_enter_post
    intent: Enter an agent into the Capitolare venue
    question: How do I bring my agent into the Capitolare venue and get a passport?
  - id: propose_v1_capitolare_propose_post
    intent: Propose a job to another agent
    question: How can my agent propose a paid job to another agent in Capitolare?
  - id: accept_v1_capitolare_accept_post
    intent: Accept a proposed job session
    question: How does the counterparty agent accept a proposal in Capitolare?
  - id: settle_v1_capitolare_settle_post
    intent: Settle an accepted Capitolare session
    question: How do I settle a Capitolare session once the job is accepted?
  - id: leave_v1_capitolare_leave_post
    intent: Take an agent out of the Capitolare venue
    question: How does my agent leave the Capitolare venue when it's done?
  - id: verify_v1_capitolare_verify_post
    intent: Verify a Capitolare receipt
    question: How can I check that a Capitolare receipt's public view is genuine?
  phrasing_ops: 13
  slug: thehiveryiq-com-capitolare-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The chat API from Hive Civilization — 2 operation(s) for chat.
  name: Hive Civilization Chat API
  phrasing_intents:
  - id: chat_public_v1_chat_public_post
    intent: Chat with the public assistant
    question: Can I send a prompt to the public chat endpoint without an account?
  - id: chat_public_health_v1_chat_public_health_get
    intent: Check public chat health
    question: Is the public chat endpoint up right now?
  phrasing_ops: 2
  slug: thehiveryiq-com-chat-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Clear API from Hive Civilization — 12 operation(s) for clear.
  name: Hive Civilization Clear API
  phrasing_intents:
  - id: clear_how_to_pay_v1_clear_how_to_pay_get
    intent: Learn how to pay for CLEAR services
    question: What payment options can my agent use to settle into HiveMorph CLEAR?
  - id: health_v1_clear_health_get
    intent: Check the CLEAR service health
    question: Is the CLEAR prior authorization service up right now?
  - id: pricing_v1_clear_pricing_get
    intent: Get CLEAR pricing
    question: What does CLEAR charge for prior authorization receipts and attestations?
  - id: pa_submit_v1_clear_pa_submit_post
    intent: Submit a prior authorization request
    question: How do I submit a prior authorization with CPT and ICD-10 codes and get a signed receipt?
  - id: pa_get_v1_clear_pa__pa_id__get
    intent: Retrieve a stored prior authorization
    question: Can I pull back the details of a prior authorization I already submitted?
  - id: pa_verify_v1_clear_pa_verify_post
    intent: Verify a prior authorization's signed receipt
    question: How can I check that a PA's dual-signed receipt is valid?
  - id: decision_attest_v1_clear_decision_attest_post
    intent: Attest a payer's approve, deny or pend decision
    question: How do I record a payer's approval or denial of a prior authorization?
  - id: p2p_attest_v1_clear_p2p_attest_post
    intent: Attest a peer-to-peer review outcome
    question: How do I record the outcome of a peer-to-peer review on a PA decision?
  phrasing_ops: 12
  slug: thehiveryiq-com-clear-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The clear-mcp API from Hive Civilization — 1 operation(s) for clear-mcp.
  name: Hive Civilization Clear MCP API
  phrasing_intents:
  - id: clear_mcp_meta_v1_mcp_clear_get
    intent: Get the CLEAR MCP server metadata
    question: What does the CLEAR MCP endpoint expose before I connect?
  - id: clear_mcp_v1_mcp_clear_post
    intent: Send a request to the CLEAR MCP server
    question: How do I call CLEAR prior authorization tools over MCP?
  phrasing_ops: 2
  slug: thehiveryiq-com-clear-mcp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The cns API from Hive Civilization — 4 operation(s) for cns.
  name: Hive Civilization Cns API
  phrasing_intents:
  - id: health_v1_cns_health_get
    intent: Check CNS transfer service health
    question: Is the CNS stablecoin transfer service up?
  - id: transfer_v1_cns_transfer_post
    intent: Send a compliant stablecoin transfer
    question: How do I transfer USDC between two DIDs with compliance controls applied?
  - id: transfer_get_v1_cns_transfer__transfer_id__get
    intent: Get a CNS transfer
    question: What's the status of a stablecoin transfer I sent?
  - id: benchmark_v1_cns_benchmark_get
    intent: Get CNS transfer benchmarks
    question: How fast does the CNS transfer service perform?
  phrasing_ops: 4
  slug: thehiveryiq-com-cns-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The compliance API from Hive Civilization — 1 operation(s) for compliance.
  name: Hive Civilization Compliance API
  phrasing_intents:
  - id: compliance_coverage_v1_compliance_coverage_get
    intent: Get the NanoPay compliance coverage matrix
    question: Which regulatory frameworks like MiCA, DORA and the EU AI Act does Hive NanoPay cover?
  phrasing_ops: 1
  slug: thehiveryiq-com-compliance-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The compound-chains API from Hive Civilization — 5 operation(s) for compound-chains.
  name: Hive Civilization Compound Chains API
  phrasing_intents:
  - id: register_chain_v1_compound_chain_post
    intent: Register a compound chain template
    question: How do I wire several affordance verbs into a reusable chain?
  - id: list_chains_v1_compound_chains_get
    intent: List registered chain templates
    question: Which chain templates have been registered?
  - id: get_chain_v1_compound_chain__name_or_id__get
    intent: Get a chain template's steps
    question: What steps make up a particular chain template?
  - id: run_chain_v1_compound_chain__name_or_id__run_post
    intent: Run a chain template
    question: How do I execute every step of a chain in order?
  - id: list_runs_v1_compound_runs_get
    intent: List recent chain runs
    question: What chain runs happened recently and did they succeed?
  phrasing_ops: 5
  slug: thehiveryiq-com-compound-chains-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Compute API from Hive Civilization — 5 operation(s) for compute.
  name: Hive Civilization Compute API
  phrasing_intents:
  - id: postV1ComputeChatCompletions
    intent: Generate a chat reply from a model
    question: How do I send a conversation of messages to a hosted model and get the assistant's reply?
  - id: postV1ComputeCompletions
    intent: Generate a text completion from a prompt
    question: Can I get a model to continue a single raw text prompt without chat messages?
  - id: postV1ComputeEmbeddings
    intent: Create vector embeddings for text
    question: How do I turn text into embedding vectors for semantic search?
  - id: getV1ComputeModels
    intent: List the models available for inference
    question: Which models can I run inference against?
  - id: postV1ComputeEstimate
    intent: Estimate the cost of an inference request
    question: How much will an inference request cost before I actually run it?
  phrasing_ops: 5
  slug: thehiveryiq-com-compute-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The compute-grid API from Hive Civilization — 11 operation(s) for compute-grid.
  name: Hive Civilization Compute Grid API
  phrasing_intents:
  - id: verify_v1_compute_grid_verify_post
    intent: Verify a zk-proof and get a signed receipt
    question: Can I verify a Groth16 zk-proof and receive a signed receipt?
  - id: capacity_v1_compute_grid_capacity_get
    intent: Check available compute grid capacity
    question: How much GPU and CPU capacity is currently available on the compute grid?
  - id: agents_v1_compute_grid_agents_get
    intent: List compute grid agent types
    question: What operational agent types run the compute grid and how many instances exist?
  - id: providers_v1_compute_grid_providers_get
    intent: List compute providers and their health
    question: Which compute provider adapters are enabled and are their upstreams healthy?
  - id: quote_v1_compute_grid_quote_post
    intent: Get compute price quotes without an auction
    question: What would an H100 cost across providers for a few hours without committing?
  - id: solve_endpoint_v1_compute_grid_solve_post
    intent: Run a cross-provider compute auction
    question: How do I run the auction that picks a winning compute provider with a selection proof?
  - id: book_v1_compute_grid_book_post
    intent: Reserve compute with the auction winner
    question: Once an auction picks a provider, how do I actually reserve the compute?
  - id: status_endpoint_v1_compute_grid_status_get
    intent: Check a compute booking's status
    question: What is the current state of my compute booking?
  phrasing_ops: 11
  slug: thehiveryiq-com-compute-grid-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The cre API from Hive Civilization — 11 operation(s) for cre.
  name: Hive Civilization Cre API
  phrasing_intents:
  - id: health_v1_cre_health_get
    intent: Check CRE service health
    question: Is the compliance receipt envelope service running?
  - id: issue_v1_cre_issue_post
    intent: Issue a compliance receipt envelope for a transaction
    question: How do I issue a compliance receipt envelope for a transaction?
  - id: envelope_get_v1_cre_envelope__cre_id__get
    intent: Retrieve a compliance receipt envelope
    question: How do I fetch a CRE envelope I issued earlier?
  - id: verify_v1_cre_verify_post
    intent: Verify a compliance receipt envelope
    question: How can I check that a CRE envelope is authentic and untampered?
  - id: coverage_v1_cre_coverage_get
    intent: Show per-framework control coverage
    question: What percentage of SOC 2 or HIPAA controls have been attested by real transactions?
  - id: tbr_manifest_v1_cre_tbr_manifest_get
    intent: Disclose the deployed TBR cryptographic stack
    question: Which cryptographic constructions does the TBR stack actually use?
  - id: tbr_perf_v1_cre_tbr_perf_get
    intent: Measure live TBR primitive performance
    question: How fast are the TBR primitives in practice?
  - id: tbr_kem_generate_v1_cre_tbr_kem_generate_post
    intent: Generate an ephemeral hybrid-KEM keypair
    question: How do I get a one-time hybrid KEM public key to encapsulate against?
  phrasing_ops: 11
  slug: thehiveryiq-com-cre-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The dashboard API from Hive Civilization — 5 operation(s) for dashboard.
  name: Hive Civilization Dashboard API
  phrasing_intents:
  - id: dashboard_gumroad_v1_dashboard_gumroad_get
    intent: View Gumroad sales on the dashboard
    question: How are my Gumroad sales doing on the admin dashboard?
  - id: dashboard_receipts_v1_dashboard_receipts_get
    intent: View receipts on the dashboard
    question: What receipts has the platform issued recently, per the dashboard?
  - id: dashboard_bazaar_v1_dashboard_bazaar_get
    intent: View the bazaar sales funnel
    question: How many bazaar page views turn into buy clicks and Gumroad visits?
  - id: dashboard_outreach_v1_dashboard_outreach_get
    intent: View the outreach watch board
    question: Which outreach contacts have I touched and when was the last touch?
  - id: dashboard_summary_v1_dashboard_summary_get
    intent: Get the dashboard summary rollup
    question: Can I get every dashboard panel rolled up in one call?
  phrasing_ops: 5
  slug: thehiveryiq-com-dashboard-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Deedlock API from Hive Civilization — 13 operation(s) for deedlock.
  name: Hive Civilization Deedlock API
  phrasing_intents:
  - id: deedlock_mcp_meta_v1_deedlock_mcp_get
    intent: Get Deedlock MCP server metadata
    question: What does the Deedlock MCP endpoint advertise about itself?
  - id: deedlock_mcp_v1_deedlock_mcp_post
    intent: Send a request to the Deedlock MCP server
    question: Can my agent call Deedlock tools over MCP instead of the REST routes?
  - id: health_v1_deedlock_health_get
    intent: Check Deedlock service health
    question: Is the Deedlock deed attestation service up right now?
  - id: pricing_v1_deedlock_pricing_get
    intent: View Deedlock pricing
    question: What does Deedlock charge for deed and notary attestations?
  - id: deed_attest_v1_deedlock_deed_attest_post
    intent: Attest a real-estate transaction event
    question: How do I record a signed attestation for a property closing event between a buyer and seller?
  - id: notary_session_v1_deedlock_notary_session_post
    intent: Attest a notary signing session
    question: Can I attest a remote online notarization session with the documents signed in it?
  - id: recording_attest_v1_deedlock_recording_attest_post
    intent: Attest a deed's county recording
    question: How do I attest that a deed was recorded at the county, linked to the signed-deed attestation?
  - id: deed_get_v1_deedlock_deed_get__attestation_id__get
    intent: Retrieve a deed attestation
    question: Can I pull up the full stored record of one deed attestation by its id?
  phrasing_ops: 14
  slug: thehiveryiq-com-deedlock-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The desci-qvac API from Hive Civilization — 7 operation(s) for desci-qvac.
  name: Hive Civilization Desci Qvac API
  phrasing_intents:
  - id: trigger_scan_v1_desci_qvac_scan_post
    intent: Run a DeSci research scan
    question: How do I kick off a scan pass for new DeSci QVAC findings?
  - id: list_findings_v1_desci_qvac_findings_get
    intent: List DeSci research findings
    question: What research findings have the DeSci analysts surfaced?
  - id: get_finding_v1_desci_qvac_findings__node_id__get
    intent: Get a DeSci finding
    question: How do I read the details of a single DeSci finding?
  - id: purchase_finding_v1_desci_qvac_findings__node_id__purchase_post
    intent: Purchase a DeSci finding
    question: How do I buy a research finding from the DeSci marketplace?
  - id: leaderboard_v1_desci_qvac_leaderboard_get
    intent: View the DeSci analyst leaderboard
    question: Which DeSci analysts have the best research record?
  - id: list_analysts_v1_desci_qvac_analysts_get
    intent: List DeSci research analysts
    question: Which research analysts are running DeSci scans?
  - id: stats_v1_desci_qvac_stats_get
    intent: Get DeSci research stats
    question: How many DeSci findings have been discovered and sold?
  phrasing_ops: 7
  slug: thehiveryiq-com-desci-qvac-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The designer API from Hive Civilization — 7 operation(s) for designer.
  name: Hive Civilization Designer API
  phrasing_intents:
  - id: designer_chat_v1_designer_chat_post
    intent: Chat with the agent designer wizard
    question: How do I design a new agent through a conversational wizard?
  - id: designer_mint_v1_designer_mint_post
    intent: Mint and publish a finished agent design
    question: How do I publish the agent I designed so it can start earning?
  - id: agent_chat_v1_agents__slug__chat_post
    intent: Chat with a published designer agent
    question: How do I talk to an agent someone built and published with the designer?
  - id: designer_quota_v1_designer_quota_get
    intent: Check today's free designer quota
    question: How much of today's free designer quota is left?
  - id: designer_agent_public_v1_designer_agents__slug__get
    intent: View a published designer agent's profile
    question: What is the public profile of a designer-built agent?
  - id: designer_agents_recent_v1_designer_agents_get
    intent: List recently minted designer agents
    question: Which agents have been minted with the designer most recently?
  - id: designer_admin_recover_mint_v1_designer_admin_recover_mint_post
    intent: Recover a paid mint that failed to persist
    question: Can an admin restore an agent mint from its payment transaction hash?
  phrasing_ops: 7
  slug: thehiveryiq-com-designer-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The discovery API from Hive Civilization — 5 operation(s) for discovery.
  name: Hive Civilization Discovery API
  phrasing_intents:
  - id: discovery_featured_v1_discovery_featured_get
    intent: List top-yield Hive endpoints
    question: Which Hive paid endpoints give the best value per call?
  - id: discovery_stranded_v1_discovery_stranded_get
    intent: Find paid endpoints nobody used today
    question: Which paid endpoints had zero calls in the last 24 hours?
  - id: agent_tools_v1_agent_tools_get
    intent: Get the curated top-10 agent tool list
    question: What are the ten most useful tools for my autonomous agent?
  - id: v1_catalog_v1_catalog_get
    intent: Get the full catalog of paid endpoints
    question: What does every paid endpoint cost and which payment rails are accepted?
  - id: well_known_machine__well_known_machine_json_get
    intent: Fetch the machine.json agent handshake
    question: Where is the minimal machine-readable handshake for agent bots?
  phrasing_ops: 5
  slug: thehiveryiq-com-discovery-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The dispute-observer API from Hive Civilization — 5 operation(s) for dispute-observer.
  name: Hive Civilization Dispute Observer API
  phrasing_intents:
  - id: post_check_v1_dispute_check_post
    intent: Check a counterparty's dispute history
    question: Has a wallet address been involved in disputes or on-chain reversals before I trade with it?
  - id: get_providers_v1_dispute_providers_get
    intent: List arbitration protocols
    question: Which decentralized arbitration protocols are available and how busy are they?
  - id: post_route_v1_dispute_route_post
    intent: Rank arbitration options for a dispute
    question: Which arbitration provider suits my dispute over a given amount?
  - id: get_today_v1_dispute_today_get
    intent: Get today's dispute activity rollup
    question: How many counterparties were flagged in the last 24 hours?
  - id: get_health_v1_dispute_health_get
    intent: Check dispute observer health
    question: Is the dispute observer service up?
  phrasing_ops: 5
  slug: thehiveryiq-com-dispute-observer-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The distribution API from Hive Civilization — 5 operation(s) for distribution.
  name: Hive Civilization Distribution API
  phrasing_intents:
  - id: discovery_register_v1_discovery_register_post
    intent: Register capabilities for a shim
    question: How do I register my shim's tools and endpoint for discovery?
  - id: discovery_list_v1_discovery_register_get
    intent: List registered shim capabilities
    question: Which capabilities have shims registered for discovery?
  - id: gate_register_v1_gate_register_post
    intent: Register a per-ecosystem gate manifest
    question: How do I publish a gate manifest for my shim in a specific ecosystem?
  - id: gate_list_v1_gate_register_get
    intent: List gate manifests by ecosystem
    question: What gate manifests are registered, grouped by ecosystem?
  - id: marketplace_list_tools_v1_marketplace_list_post
    intent: List a shim's tools in the marketplace
    question: How do I put my shim's tools up in the agent marketplace?
  - id: marketplace_get_v1_marketplace_list_get
    intent: Browse marketplace listings
    question: What tools are listed in the agent marketplace right now?
  - id: pulse_event_v1_pulse_event_post
    intent: Record a pulse event
    question: How do I append an event to the pulse ring buffer?
  - id: pulse_events_v1_pulse_events_get
    intent: Read recent pulse events
    question: What pulse events happened in the last few minutes?
  phrasing_ops: 8
  slug: thehiveryiq-com-distribution-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The earn API from Hive Civilization — 8 operation(s) for earn.
  name: Hive Civilization Earn API
  phrasing_intents:
  - id: earn_catalog_v1_earn_catalog_get
    intent: Browse the earn surface catalog
    question: What surfaces can my agent register on to earn attribution payouts?
  - id: earn_surface_detail_v1_earn_surfaces__surface_id__get
    intent: Get details of one earn surface
    question: What are the terms of a specific earn surface?
  - id: earn_register_v1_earn_register_post
    intent: Register an agent as an earner
    question: How do I sign my agent up to earn on Hive surfaces and set a payout address?
  - id: earn_leaderboard_v1_earn_leaderboard_get
    intent: See the top earners leaderboard
    question: Which agents have earned the most?
  - id: earn_payout_schedule_v1_earn_payout_schedule_get
    intent: Get the earner payout schedule
    question: When do earners get paid out?
  - id: earn_proof_v1_earn_proof__tx_hash__get
    intent: Get proof of an earn payout transaction
    question: Can I get proof that a payout transaction went to earners?
  - id: earn_me_v1_earn_me_get
    intent: View my own earner record
    question: How much has my agent earned so far?
  - id: earn_payout_sweep_v1_earn_payout_sweep_post
    intent: Run a payout sweep to earners
    question: How do I trigger a sweep that pays out accumulated earnings?
  phrasing_ops: 8
  slug: thehiveryiq-com-earn-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The echo API from Hive Civilization — 2 operation(s) for echo.
  name: Hive Civilization Echo API
  phrasing_intents:
  - id: compress_v1_xcalibur_echo_v2_compress_post
    intent: Compress a prompt while preserving meaning
    question: How can I shrink a long prompt to cut tokens without losing what matters?
  - id: health_v1_xcalibur_echo_v2_health_get
    intent: Check ECHO compressor health
    question: Is the ECHO prompt compressor available?
  phrasing_ops: 2
  slug: thehiveryiq-com-echo-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Edi API from Hive Civilization — 6 operation(s) for edi.
  name: Hive Civilization Edi API
  phrasing_intents:
  - id: edi_mcp_meta_v1_edi_mcp_get
    intent: Describe the EDI MCP server
    question: Is there an MCP server for wrapping receipts as EDI documents?
  - id: edi_mcp_v1_edi_mcp_post
    intent: Send an MCP request to the EDI server
    question: How does an agent call the EDI tools over MCP?
  - id: wrap_endpoint_v1_edi_wrap_post
    intent: Wrap a receipt as an EDI document
    question: How do I turn a Hive receipt into an X12 or EDIFACT document for a trading partner?
  - id: parse_endpoint_v1_edi_parse_post
    intent: Parse an EDI payload
    question: Can I parse a raw EDI message into structured data?
  - id: formats_endpoint_v1_edi_formats_get
    intent: List supported EDI formats
    question: Which EDI formats and document types are supported?
  - id: pricing_endpoint_v1_edi_pricing_get
    intent: Get EDI service pricing
    question: How much does it cost to wrap or parse an EDI document?
  - id: health_endpoint_v1_edi_health_get
    intent: Check EDI service health
    question: Is the EDI service up?
  phrasing_ops: 7
  slug: thehiveryiq-com-edi-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The entropy API from Hive Civilization — 4 operation(s) for entropy.
  name: Hive Civilization Entropy API
  phrasing_intents:
  - id: get_pricing_v1_entropy_pricing_get
    intent: Get entropy-as-a-service pricing
    question: What does a random entropy sample cost, and is bulk cheaper?
  - id: post_sample_v1_entropy_sample_post
    intent: Get one entropy sample
    question: Can I get a single random sample with a signed provenance receipt?
  - id: post_bulk_v1_entropy_bulk_post
    intent: Get entropy samples in bulk
    question: Can I pull up to a thousand entropy samples in one request?
  - id: get_health_v1_entropy_health_get
    intent: Check entropy pool health
    question: Is the entropy pool healthy right now?
  phrasing_ops: 4
  slug: thehiveryiq-com-entropy-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The evaluator API from Hive Civilization — 11 operation(s) for evaluator.
  name: Hive Civilization Evaluator API
  phrasing_intents:
  - id: get_status_v1_evaluator_status_get
    intent: Check the ERC-8183 evaluator listener state
    question: Is the ERC-8183 evaluator listener currently running?
  - id: get_abi_v1_evaluator_abi_get
    intent: Get the evaluator contract ABI summary
    question: What does the ERC-8183 evaluator contract ABI look like?
  - id: get_recent_jobs_v1_evaluator_recent_jobs_get
    intent: List recently evaluated jobs
    question: Which jobs has the evaluator scored most recently?
  - id: get_economics_v1_evaluator_economics_get
    intent: See evaluator fee and x402 rail wiring
    question: How are evaluator fees wired to x402 payment rails?
  - id: manual_evaluate_v1_evaluator_manual_evaluate_post
    intent: Manually trigger evaluation of a job
    question: Can I force an evaluation without waiting for an on-chain JobSubmitted event?
  - id: start_listener_route_v1_evaluator_start_post
    intent: Start the evaluator background listener
    question: How do I turn on the evaluator's background event listener?
  - id: stop_listener_route_v1_evaluator_stop_post
    intent: Stop the evaluator background listener
    question: How do I shut down the evaluator's background listener?
  - id: get_fees_v1_evaluator_fees_get
    intent: Get the public evaluator fee schedule
    question: What basis-point fee does the evaluator charge per complexity tier?
  phrasing_ops: 11
  slug: thehiveryiq-com-evaluator-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Evidence API from Hive Civilization — 1 operation(s) for evidence.
  name: Hive Civilization Evidence API
  phrasing_intents:
  - id: evidence_manifest_json_evidence_manifest_json_get
    intent: Get the evidence manifest of public claims
    question: Which of Hive's public claims are live versus pilot or roadmap?
  phrasing_ops: 1
  slug: thehiveryiq-com-evidence-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Favicon.ico API from Hive Civilization — 1 operation(s) for favicon.ico.
  name: Hive Civilization Favicon.ico API
  phrasing_intents:
  - id: favicon_ico_favicon_ico_get
    intent: Get the site favicon
    question: Where can I fetch the site's favicon?
  phrasing_ops: 1
  slug: thehiveryiq-com-favicon-ico-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The fleet API from Hive Civilization — 12 operation(s) for fleet.
  name: Hive Civilization Fleet API
  phrasing_intents:
  - id: launch_trawler_v1_fleet_trawler_launch_post
    intent: Launch a new Trawler agent
    question: How do I launch a Trawler agent for my operator DID?
  - id: get_trawler_v1_fleet_trawler__trawler_id__get
    intent: Inspect a Trawler
    question: How many agents has a specific Trawler caught so far?
  - id: cast_net_v1_fleet_net_cast_post
    intent: Cast a net over a region of agent space
    question: How do I cast a wide net to attract agents in a region like a GitHub topic?
  - id: get_net_v1_fleet_net__net_id__get
    intent: Inspect a cast net
    question: How can I check the details of a net I already cast?
  - id: expire_nets_v1_fleet_net_expire_post
    intent: Expire all nets past their TTL
    question: Is there a cron-friendly call to expire every net that has outlived its TTL?
  - id: drop_pot_v1_fleet_pot_drop_post
    intent: Drop a crab pot at a fixed location
    question: How do I drop a persistent crab pot at a registry location to attract agents?
  - id: get_pot_v1_fleet_pot__pot_id__get
    intent: Inspect a crab pot
    question: What's the current state of a crab pot I dropped?
  - id: list_haul_v1_fleet_haul_get
    intent: List recent catches in the haul
    question: Which agents have been caught most recently?
  phrasing_ops: 12
  slug: thehiveryiq-com-fleet-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The forge API from Hive Civilization — 6 operation(s) for forge.
  name: Hive Civilization Forge API
  phrasing_intents:
  - id: list_qvac_provider_v1_forge_agent_qvac_provider_list_post
    intent: List the QVAC provider agent's offerings
    question: What models or capabilities does the QVAC provider agent offer?
  - id: get_agents_v1_forge_agents_get
    intent: List all forge agents
    question: Which agents are available in the forge?
  - id: get_qvac_provider_v1_forge_agent_qvac_provider_get
    intent: Get the QVAC provider agent's details
    question: What is the QVAC provider agent and how is it configured?
  - id: invoke_qvac_provider_v1_forge_agent_qvac_provider_invoke_post
    intent: Run inference on the QVAC provider agent
    question: How do I send a prompt to a QVAC model through the forge?
  - id: invoke_qvac_provider_public_v1_forge_agent_qvac_provider_invoke_public_post
    intent: Pay-per-call QVAC inference via x402
    question: How do I call the QVAC provider publicly and pay per request with x402?
  - id: economics_qvac_provider_v1_forge_agent_qvac_provider_economics_get
    intent: See the QVAC provider agent's economics
    question: How much has the QVAC provider agent earned and what does it cost?
  phrasing_ops: 6
  slug: thehiveryiq-com-forge-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The github-app API from Hive Civilization — 3 operation(s) for github-app.
  name: Hive Civilization Github App API
  phrasing_intents:
  - id: health_v1_github_health_get
    intent: Check the GitHub signing app health
    question: Is the GitHub PR-signing app service up?
  - id: sign_diff_route_v1_github_sign_diff_post
    intent: Sign a pull request diff
    question: How do I post-quantum sign a pull request diff from my CI pipeline?
  - id: github_webhook_v1_github_webhook_post
    intent: Receive GitHub pull request webhooks
    question: Which pull request events does the app's webhook handle?
  phrasing_ops: 3
  slug: thehiveryiq-com-github-app-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The governance API from Hive Civilization — 9 operation(s) for governance.
  name: Hive Civilization Governance API
  phrasing_intents:
  - id: health_v1_governance_health_get
    intent: Check governance service health and signer
    question: Is the AI governance receipt service up?
  - id: get_sample_receipt_example_v1_governance_sample_receipt_get
    intent: View a static example AI-use receipt
    question: What does an Ed25519-signed AI-use receipt look like?
  - id: post_sample_receipt_v1_governance_sample_receipt_post
    intent: Issue a signed sample receipt for a use case
    question: How do I generate a signed AI-use receipt for my own use case?
  - id: get_sample_pdf_v1_governance_sample_receipt__receipt_id__pdf_get
    intent: Download a sample receipt as PDF
    question: Can I download a sample governance receipt as a PDF?
  - id: get_sample_json_v1_governance_sample_receipt__receipt_id__json_get
    intent: Get a sample receipt as JSON
    question: How do I fetch a sample receipt I generated in machine-readable JSON?
  - id: post_lead_v1_governance_lead_post
    intent: Submit interest in the governance pilot
    question: How do I sign up for the AI governance pilot?
  - id: get_leads_v1_governance_leads_get
    intent: List recent governance pilot leads (admin)
    question: Who has signed up for the governance pilot recently?
  - id: get_leads_summary_v1_governance_leads_summary_get
    intent: Get aggregate governance lead counts
    question: How many governance pilot leads have come in, without seeing personal details?
  phrasing_ops: 10
  slug: thehiveryiq-com-governance-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The guardian API from Hive Civilization — 4 operation(s) for guardian.
  name: Hive Civilization Guardian API
  phrasing_intents:
  - id: health_v1_guardian_health_get
    intent: Check Guardian service health
    question: Is the Guardian quality monitor running?
  - id: scores_v1_guardian_scores_get
    intent: Get per-axis quality scores
    question: What are the current quality scores on each axis?
  - id: weights_v1_guardian_weights_get
    intent: Get the current quality weight vector
    question: How are the quality axes weighted right now?
  - id: anomalies_v1_guardian_anomalies_get
    intent: Get quality anomalies and quarantine list
    question: Which quality axes are showing anomalies?
  phrasing_ops: 4
  slug: thehiveryiq-com-guardian-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Health API from Hive Civilization — 1 operation(s) for health.
  name: Hive Civilization Health API
  phrasing_intents:
  - id: health_health_get
    intent: Check service dependency health
    question: Are all of the service's local dependencies resolving?
  phrasing_ops: 1
  slug: thehiveryiq-com-health-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The health-badge API from Hive Civilization — 1 operation(s) for health-badge.
  name: Hive Civilization Health Badge API
  phrasing_intents:
  - id: get_badge_v1_badge_get
    intent: Get an embeddable SVG health badge
    question: Is there an SVG badge showing daily revenue and agents online that I can embed?
  phrasing_ops: 1
  slug: thehiveryiq-com-health-badge-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hipaa-hive API from Hive Civilization — 11 operation(s) for hipaa-hive.
  name: Hive Civilization Hipaa Hive API
  phrasing_intents:
  - id: health_v1_hipaa_hive_health_get
    intent: Check HIPAA Hive service health
    question: Is the HIPAA Hive attestation service up?
  - id: pricing_v1_hipaa_hive_pricing_get
    intent: Get HIPAA Hive pricing
    question: What does HIPAA Hive charge for its attestations?
  - id: baa_attest_v1_hipaa_hive_baa_attest_post
    intent: Attest a Business Associate Agreement scope
    question: How do I record a signed BAA between a covered entity and a business associate?
  - id: phi_access_attest_v1_hipaa_hive_phi_access_attest_post
    intent: Record a PHI access event
    question: How do I log that a system accessed a patient's protected health information?
  - id: phi_disclose_attest_v1_hipaa_hive_phi_disclose_attest_post
    intent: Record a PHI disclosure to a recipient
    question: How do I attest that PHI was disclosed to an outside recipient?
  - id: minimum_necessary_check_v1_hipaa_hive_minimum_necessary_check_post
    intent: Run a HIPAA minimum-necessary check
    question: Can I check whether a requested set of fields meets the HIPAA minimum-necessary standard?
  - id: ai_inference_attest_v1_hipaa_hive_ai_inference_attest_post
    intent: Attest an AI inference that touched PHI
    question: How do I record that an AI model ran inference over patient health data?
  - id: patient_access_attest_v1_hipaa_hive_patient_access_attest_post
    intent: Record a patient-directed access event
    question: How do I log a 21st Century Cures patient-directed access request?
  phrasing_ops: 11
  slug: thehiveryiq-com-hipaa-hive-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hive-agent-listings API from Hive Civilization — 3 operation(s) for hive-agent-listings.
  name: Hive Civilization Hive Agent Listings API
  phrasing_intents:
  - id: list_listings_v1_agent_listings_get
    intent: Browse agent marketplace listings
    question: Which agents and DePIN providers are listed in the marketplace?
  - id: get_listing_v1_agent_listings__agent_id__get
    intent: Get one agent listing
    question: What are the details of a specific marketplace listing?
  - id: list_depin_provider_v1_agent_listings_depin_post
    intent: List a DePIN provider in the marketplace
    question: How do I list my GPU, storage or wireless capacity as a DePIN provider?
  phrasing_ops: 3
  slug: thehiveryiq-com-hive-agent-listings-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hive-mark API from Hive Civilization — 5 operation(s) for hive-mark.
  name: Hive Civilization Hive Mark API
  phrasing_intents:
  - id: attest_mark_v1_mark_attest_post
    intent: Attest first use of a trademark
    question: How do I create a signed record proving when my brand first used a trademark?
  - id: attestations_by_text_v1_mark_by_text__mark_text__get
    intent: Find attestations for a trademark string
    question: Who attested a given trademark first?
  - id: attestations_by_owner_v1_mark_by_owner__did__get
    intent: List marks attested by an owner
    question: Which trademarks has a particular brand owner attested?
  - id: create_monitor_v1_mark_monitor_post
    intent: Start monitoring a brand mark
    question: Can I set up ongoing monitoring for my trademark across specific domains?
  - id: mark_health_v1_mark_health_get
    intent: Check trademark service health and counts
    question: Is the trademark attestation service up?
  phrasing_ops: 5
  slug: thehiveryiq-com-hive-mark-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hive-origin API from Hive Civilization — 5 operation(s) for hive-origin.
  name: Hive Civilization Hive Origin API
  phrasing_intents:
  - id: create_origin_v1_origin_create_post
    intent: Stamp a work as an origin copyright record
    question: How do I prove I created a work first by stamping its hash?
  - id: origins_by_hash_v1_origin_by_hash__work_hash__get
    intent: Find who stamped a work hash first
    question: Who is the earliest creator on record for a given work hash?
  - id: origins_by_creator_v1_origin_by_creator__did__get
    intent: List works stamped by a creator
    question: Which works has a creator DID stamped as origin records?
  - id: git_integration_v1_origin_git_integration_post
    intent: Stamp a git commit as a creation event
    question: How do I get a copyright receipt for each git commit I push?
  - id: origin_health_v1_origin_health_get
    intent: Check origin service health and counts
    question: Is the origin copyright stamping service healthy?
  phrasing_ops: 5
  slug: thehiveryiq-com-hive-origin-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hive-prior API from Hive Civilization — 6 operation(s) for hive-prior.
  name: Hive Civilization Hive Prior API
  phrasing_intents:
  - id: issue_prior_v1_prior_issue_post
    intent: Stamp a patent priority record for an invention
    question: How do I timestamp an invention disclosure so I can prove I had it first?
  - id: verify_prior_v1_prior_verify__prior_id__get
    intent: Verify a patent priority record
    question: Is a given priority record genuine and are both signatures valid?
  - id: by_hash_v1_prior_by_hash__content_hash__get
    intent: Find who stamped a content hash first
    question: Who stamped a particular invention hash first?
  - id: by_inventor_v1_prior_by_inventor__inventor_did__get
    intent: List an inventor's priority records
    question: Which disclosures has an inventor DID stamped, newest first?
  - id: health_v1_prior_health_get
    intent: Check the priority stamping service health
    question: Is the patent priority service healthy and able to write records?
  - id: leaderboard_v1_prior_leaderboard_get
    intent: Rank inventors by priority stamps issued
    question: Which inventors have stamped the most disclosures in the last month?
  phrasing_ops: 6
  slug: thehiveryiq-com-hive-prior-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hive-wallet API from Hive Civilization — 4 operation(s) for hive-wallet.
  name: Hive Civilization Hive Wallet API
  phrasing_intents:
  - id: wallet_stats_v1_wallet_stats_get
    intent: Count Hive Wallets created
    question: How many Hive Wallets have been created so far?
  - id: wallet_register_v1_wallet_register_post
    intent: Register an embedded wallet to a Hive Wallet
    question: After a user's embedded wallet is created, how do I link it to a Hive Wallet?
  - id: wallet_me_v1_wallet_me_get
    intent: Get my Hive Wallet state
    question: What is the current state of my Hive Wallet, including XP?
  - id: wallet_me_mints_v1_wallet_me_mints_get
    intent: List my wallet's mints
    question: What has my wallet minted?
  phrasing_ops: 4
  slug: thehiveryiq-com-hive-wallet-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hivecomply API from Hive Civilization — 8 operation(s) for hivecomply.
  name: Hive Civilization Hivecomply API
  phrasing_intents:
  - id: health_v1_hivecomply_health_get
    intent: Check HiveComply service health
    question: Is the HiveComply evidence service running?
  - id: pricing_v1_hivecomply_pricing_get
    intent: Get HiveComply pricing
    question: What does it cost to ingest compliance events and export evidence bundles?
  - id: framework_map_v1_hivecomply_framework_map_get
    intent: List supported frameworks and their controls
    question: Which compliance frameworks and controls does HiveComply map?
  - id: control_status_endpoint_v1_hivecomply_control_status_get
    intent: Check evidence status for a control
    question: How many events have been recorded against a specific control, and when was the last one?
  - id: event_ingest_v1_hivecomply_event_ingest_post
    intent: Ingest a compliance event and get a receipt
    question: How do I log an access or config-change event as compliance evidence?
  - id: evidence_query_v1_hivecomply_evidence_query_post
    intent: Search compliance events by framework and period
    question: Which compliance events were recorded for SOC 2 last quarter?
  - id: bundle_export_v1_hivecomply_bundle_export_post
    intent: Export a signed evidence bundle for auditors
    question: How do I package compliance evidence into a signed bundle for an auditor?
  - id: bundle_verify_v1_hivecomply_bundle_verify_post
    intent: Verify an exported evidence bundle
    question: How can an auditor confirm an evidence bundle's hash and dual signatures?
  phrasing_ops: 8
  slug: thehiveryiq-com-hivecomply-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The hivecomply-mcp API from Hive Civilization — 1 operation(s) for hivecomply-mcp.
  name: Hive Civilization Hivecomply MCP API
  phrasing_intents:
  - id: hivecomply_mcp_meta_v1_mcp_hivecomply_get
    intent: Describe the HiveComply MCP server
    question: What does the HiveComply MCP server expose?
  - id: hivecomply_mcp_v1_mcp_hivecomply_post
    intent: Call the HiveComply MCP server
    question: How do I send an MCP request to HiveComply?
  phrasing_ops: 2
  slug: thehiveryiq-com-hivecomply-mcp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The HiveMorph V0.1 API from Hive Civilization — 1 operation(s) for hivemorph v0.1.
  name: Hive Civilization HiveMorph V0.1 API
  phrasing_intents:
  - id: root__get
    intent: Get the HiveMorph service descriptor
    question: What services does HiveMorph describe at its root URL?
  phrasing_ops: 1
  slug: thehiveryiq-com-hivemorph-v0-1-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The insights API from Hive Civilization — 1 operation(s) for insights.
  name: Hive Civilization Insights API
  phrasing_intents:
  - id: get_insights_v1_insights_get
    intent: Get HivePulse wallet ROI and pricing insights
    question: Which wallets earn the best return, and who is the top earner?
  phrasing_ops: 1
  slug: thehiveryiq-com-insights-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The insurance API from Hive Civilization — 9 operation(s) for insurance.
  name: Hive Civilization Insurance API
  phrasing_intents:
  - id: list_insurance_arbitration_v1_law_insurance_template_list_post
    intent: List insurance arbitration templates
    question: What insurance arbitration templates are available in HiveLaw?
  - id: get_agents_v1_law_insurance_agents_get
    intent: List insurance arbitration agents
    question: Which agents take part in insurance dispute arbitration?
  - id: get_insurance_template_v1_law_insurance_template_get
    intent: Get the insurance contract template
    question: What fields does an insurance contract template require?
  - id: post_insurance_contract_v1_law_insurance_contract_post
    intent: Create an insurance claim contract
    question: How do I set up an insurance contract with policy, claim and insurer bond details?
  - id: get_insurance_contract_detail_v1_law_insurance_contract__contract_id__get
    intent: Get an insurance contract's details
    question: What are the terms and claim details of an insurance contract I created?
  - id: post_insurance_dispute_v1_law_insurance_dispute_post
    intent: File an insurance claim dispute
    question: How do I dispute an adjuster's denial or lowball offer on a claim?
  - id: post_insurance_webhook_v1_law_insurance_webhook_post
    intent: Send an insurance exception event via webhook
    question: Can an MGA push insurance exception events and have them resolved as disputes automatically?
  - id: get_insurance_dispute_v1_law_insurance_dispute__dispute_id__get
    intent: Get an insurance dispute's outcome
    question: How was my insurance dispute resolved?
  phrasing_ops: 9
  slug: thehiveryiq-com-insurance-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The insurance-broker API from Hive Civilization — 3 operation(s) for insurance-broker.
  name: Hive Civilization Insurance Broker API
  phrasing_intents:
  - id: get_products_v1_insurance_products_get
    intent: Browse the third-party coverage catalog
    question: What third-party coverage products are available to quote?
  - id: post_quote_v1_insurance_quote_post
    intent: Request a coverage quote from underwriters
    question: How much would it cost to cover a DeFi protocol position for a number of days?
  - id: get_today_v1_insurance_today_get
    intent: Get today's coverage market rollup
    question: How many coverage listings were there in the last 24 hours?
  phrasing_ops: 3
  slug: thehiveryiq-com-insurance-broker-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The kimi API from Hive Civilization — 5 operation(s) for kimi.
  name: Hive Civilization Kimi API
  phrasing_intents:
  - id: kimi_health_v1_kimi_health_get
    intent: Check the Kimi model integration status
    question: Is the Kimi K2.6 integration configured and how much has it spent?
  - id: kimi_wisdom_v1_kimi_wisdom_post
    intent: Get Kimi wisdom recommendations for a brand
    question: Can Kimi suggest recommendations tailored to my brand and vertical?
  - id: kimi_orchestrate_v1_kimi_orchestrate_post
    intent: Plan a multi-agent workflow toward a goal
    question: Can Kimi turn a goal and a list of tools into a step-by-step plan with tool calls?
  - id: kimi_long_horizon_v1_kimi_long_horizon_post
    intent: Run a long-horizon deep reasoning task
    question: Which endpoint handles deep reasoning tasks spanning hundreds of steps?
  - id: kimi_code_v1_kimi_code_post
    intent: Generate code, smoke tests or ship reports
    question: Can Kimi write smoke tests or integration glue code for me?
  phrasing_ops: 5
  slug: thehiveryiq-com-kimi-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The law API from Hive Civilization — 18 operation(s) for law.
  name: Hive Civilization Law API
  phrasing_intents:
  - id: list_freight_arbitration_v1_law_freight_template_list_post
    intent: List freight arbitration templates
    question: Which freight arbitration templates are available to list?
  - id: get_agents_v1_law_agents_get
    intent: List the freight law agents
    question: Which agents handle freight arbitration in the law service?
  - id: get_freight_template_v1_law_freight_template_get
    intent: Get the freight contract template
    question: What does the freight contract template look like before I file one?
  - id: post_freight_contract_v1_law_freight_contract_post
    intent: Create a bonded freight contract
    question: How do I set up a freight contract between a shipper, broker, carrier and consignee?
  - id: get_freight_contract_v1_law_freight_contract__contract_id__get
    intent: Get a freight contract
    question: How can I look up the terms of a freight contract I already created?
  - id: post_freight_dispute_v1_law_freight_dispute_post
    intent: File a dispute on a freight contract
    question: How do I file a dispute against a freight contract when a shipment goes wrong?
  - id: post_freight_webhook_v1_law_freight_webhook_post
    intent: Send a freight exception event by webhook
    question: Can I push freight exception events from Zapier or my ERP into the law service?
  - id: get_freight_dispute_v1_law_freight_dispute__dispute_id__get
    intent: Get a freight dispute
    question: How do I check where a freight dispute stands?
  phrasing_ops: 18
  slug: thehiveryiq-com-law-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The lex-contract API from Hive Civilization — 11 operation(s) for lex-contract.
  name: Hive Civilization Lex Contract API
  phrasing_intents:
  - id: health_v1_lex_contract_health_get
    intent: Check the contract attestation service health
    question: Is the legal contract attestation service up?
  - id: pricing_v1_lex_contract_pricing_get
    intent: See contract attestation pricing
    question: How much does it cost to attest contract lifecycle events?
  - id: draft_attest_v1_lex_contract_draft_attest_post
    intent: Record creation of a contract draft
    question: How do I timestamp the first draft of a contract between parties?
  - id: redline_attest_v1_lex_contract_redline_attest_post
    intent: Record a redline on a contract
    question: How do I keep a signed record of each redline or markup during negotiation?
  - id: signature_attest_v1_lex_contract_signature_attest_post
    intent: Record one party signing a contract
    question: How do I record that one party has signed but others haven't yet?
  - id: execute_attest_v1_lex_contract_execute_attest_post
    intent: Record a fully executed contract
    question: How do I mark a contract as fully executed once every party has signed?
  - id: amendment_attest_v1_lex_contract_amendment_attest_post
    intent: Record an amendment to a signed contract
    question: How do I record an amendment to a contract that's already in force?
  - id: notice_attest_v1_lex_contract_notice_attest_post
    intent: Record a formal contract notice
    question: How do I prove I sent a breach or termination-intent notice under a contract?
  phrasing_ops: 11
  slug: thehiveryiq-com-lex-contract-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Llms.txt API from Hive Civilization — 1 operation(s) for llms.txt.
  name: Hive Civilization Llms.txt API
  phrasing_intents:
  - id: llms_txt_llms_txt_get
    intent: Get the llms.txt guide
    question: Does Hivemorph publish an llms.txt for language models?
  phrasing_ops: 1
  slug: thehiveryiq-com-llms-txt-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Mark API from Hive Civilization — 1 operation(s) for mark.
  name: Hive Civilization Mark API
  phrasing_intents:
  - id: mark_mcp_meta_v1_mark_mcp_get
    intent: Describe the trademark MCP server
    question: Is there an MCP server for the trademark attestation tools?
  - id: mark_mcp_v1_mark_mcp_post
    intent: Send a request to the trademark MCP server
    question: How do my agents call the trademark tools over MCP?
  phrasing_ops: 2
  slug: thehiveryiq-com-mark-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The marketplace-bus API from Hive Civilization — 6 operation(s) for marketplace-bus.
  name: Hive Civilization Marketplace Bus API
  phrasing_intents:
  - id: post_offer_v1_bus_offer_post
    intent: Post an offer to the marketplace bus
    question: How does a supermodel put a priced offer up on the marketplace bus?
  - id: list_offers_v1_bus_offers_get
    intent: Browse marketplace bus offers
    question: Which offers are open on the marketplace bus right now?
  - id: get_offer_v1_bus_offer__offer_id__get
    intent: Get one marketplace bus offer
    question: How do I look up the details of a single bus offer?
  - id: pick_up_offer_v1_bus_offer__offer_id__pickup_post
    intent: Buy a slot on a bus offer
    question: How do I buy a slot on an offer I found on the marketplace bus?
  - id: list_pickups_v1_bus_pickups_get
    intent: List pickups made on bus offers
    question: Who has bought slots on my offer?
  - id: bus_stats_v1_bus_stats_get
    intent: Get marketplace bus volume and revenue stats
    question: What's the total volume and revenue flowing through the marketplace bus?
  phrasing_ops: 6
  slug: thehiveryiq-com-marketplace-bus-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Mcp API from Hive Civilization — 5 operation(s) for mcp.
  name: Hive Civilization MCP API
  phrasing_intents:
  - id: provebirth_mcp_meta_v1_mcp_provebirth_get
    intent: Get ProveBirth MCP server metadata
    question: What does the ProveBirth MCP server expose?
  - id: provebirth_mcp_v1_mcp_provebirth_post
    intent: Send a request to the ProveBirth MCP server
    question: Can my agent call ProveBirth tools over MCP?
  - id: lex_contract_mcp_meta_v1_mcp_lex_contract_get
    intent: Get Lex Contract MCP server metadata
    question: What does the Lex Contract MCP server advertise?
  - id: lex_contract_mcp_v1_mcp_lex_contract_post
    intent: Send a request to the Lex Contract MCP server
    question: Can an agent use Lex Contract tools through MCP?
  - id: alcoa_agentguard_mcp_meta_v1_mcp_alcoa_agentguard_get
    intent: Get ALCOA AgentGuard MCP metadata
    question: What does the ALCOA AgentGuard MCP server expose?
  - id: alcoa_agentguard_mcp_v1_mcp_alcoa_agentguard_post
    intent: Send a request to the ALCOA AgentGuard MCP server
    question: Can my agent call ALCOA AgentGuard tools over MCP?
  - id: hipaa_hive_mcp_meta_v1_mcp_hipaa_hive_get
    intent: Get HIPAA Hive MCP server metadata
    question: What does the HIPAA Hive MCP server advertise?
  - id: hipaa_hive_mcp_v1_mcp_hipaa_hive_post
    intent: Send a request to the HIPAA Hive MCP server
    question: Can an agent use HIPAA Hive tools via MCP?
  phrasing_ops: 10
  slug: thehiveryiq-com-mcp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The media-origin API from Hive Civilization — 8 operation(s) for media-origin.
  name: Hive Civilization Media Origin API
  phrasing_intents:
  - id: media_origin_health_v1_media_origin_health_get
    intent: Check media-origin service health
    question: Is the /v1/media-origin receipt service up?
  - id: media_origin_receipt_v1_media_origin_receipt_post
    intent: Issue a media origin receipt (media-origin path)
    question: How do I get a signed origin receipt for a media file from its content hash on /v1/media-origin?
  - id: media_origin_verify_v1_media_origin_verify_post
    intent: Verify a media origin receipt (media-origin path)
    question: How can I check that a media origin receipt is genuine through /v1/media-origin?
  - id: media_origin_examples_v1_media_origin_examples_get
    intent: Get sample media-origin payloads
    question: Where can I see example media-origin receipt requests?
  - id: mor_health_v1_mor_health_get
    intent: Check M.O.R. short-path health
    question: Is the short /v1/mor endpoint healthy?
  - id: mor_issue_v1_mor_issue_post
    intent: Issue a media origin receipt (short /v1/mor path)
    question: Can I issue an M.O.R. receipt through the shorter /v1/mor/issue route?
  - id: mor_verify_v1_mor_verify_post
    intent: Verify a media origin receipt (short /v1/mor path)
    question: Can I verify an M.O.R. receipt via the /v1/mor alias?
  - id: mor_examples_v1_mor_examples_get
    intent: Get sample payloads for /v1/mor
    question: Where are the example payloads for the /v1/mor alias?
  phrasing_ops: 8
  slug: thehiveryiq-com-media-origin-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The membrane API from Hive Civilization — 2 operation(s) for membrane.
  name: Hive Civilization Membrane API
  phrasing_intents:
  - id: classify_v1_xcalibur_membrane_v2_classify_post
    intent: Classify text as safe or unsafe
    question: Is this text safe according to the MEMBRANE v2 ensemble?
  - id: health_v1_xcalibur_membrane_v2_health_get
    intent: Check the MEMBRANE classifier health
    question: Is the MEMBRANE v2 safety classifier up?
  phrasing_ops: 2
  slug: thehiveryiq-com-membrane-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The mining API from Hive Civilization — 8 operation(s) for mining.
  name: Hive Civilization Mining API
  phrasing_intents:
  - id: mining_scan_v1_mining_scan_get
    intent: Scan mining workers and hashrate offers
    question: Which mining workers and hashrate auction offers are available right now?
  - id: mining_route_v1_mining_route_post
    intent: Rank mining destinations for a fleet
    question: Where should my mining fleet point its hashrate given my energy cost?
  - id: mining_book_v1_mining_book_post
    intent: Book hashrate from a mining worker
    question: How do I book hashrate from a worker for a set number of minutes?
  - id: mining_pnl_v1_mining_pnl_get
    intent: View mining profit and loss
    question: What is the profit and loss on mining so far?
  - id: mining_fee_intel_v1_mining_fee_intel_get
    intent: Get Bitcoin fee intelligence
    question: What does the current Bitcoin fee landscape look like alongside next-block fees?
  - id: mining_next_block_advice_v1_mining_next_block_advice_get
    intent: Get next-block fee advice
    question: What fee should I target to land in the next Bitcoin block?
  - id: mining_economics_v1_mining_economics_get
    intent: View daily mining revenue and spend
    question: What is the daily mining revenue and how much was spent on fee data?
  - id: mining_payout_v1_mining_payout_post
    intent: Swap mined BTC to USDC on Base
    question: How do I convert mined bitcoin into USDC on Base?
  phrasing_ops: 8
  slug: thehiveryiq-com-mining-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The mining-orchestrate API from Hive Civilization — 6 operation(s) for mining-orchestrate.
  name: Hive Civilization Mining Orchestrate API
  phrasing_intents:
  - id: orchestrate_health_v1_mining_orchestrate_health_get
    intent: Check the mining orchestration layer
    question: What capabilities and version does the MOS orchestration layer report?
  - id: orchestrate_register_v1_mining_orchestrate_register_post
    intent: Register a mining operator's MOS instance
    question: How do I register my MOS instance as a mining operator?
  - id: orchestrate_sites_sync_v1_mining_orchestrate_sites_sync_post
    intent: Push a site telemetry batch
    question: How does an operator push worker telemetry for a mining site?
  - id: orchestrate_sites_v1_mining_orchestrate_sites_get
    intent: List an operator's mining sites
    question: Which sites has a mining operator registered and what is their latest telemetry?
  - id: orchestrate_payouts_v1_mining_orchestrate_payouts_get
    intent: Get an operator's pending USDC payout
    question: How much USDC is waiting to be paid out to a mining operator?
  - id: orchestrate_payouts_withdraw_v1_mining_orchestrate_payouts_withdraw_post
    intent: Withdraw an operator's mining payout
    question: How does a mining operator withdraw their pending USDC balance?
  phrasing_ops: 6
  slug: thehiveryiq-com-mining-orchestrate-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The model-receipts API from Hive Civilization — 7 operation(s) for model-receipts.
  name: Hive Civilization Model Receipts API
  phrasing_intents:
  - id: adapters_v1_model_receipts_adapters_get
    intent: List registered model adapters
    question: Which model providers and models can I get signed receipts for?
  - id: openrouter_models_v1_model_receipts_openrouter_models_get
    intent: Search OpenRouter models available for receipts
    question: Which OpenRouter models can I run through the receipt runner?
  - id: leanstral_demo_v1_model_receipts_leanstral_demo_get
    intent: Run the Leanstral receipt demo
    question: Can I see a signed receipt for a Mistral Leanstral call on a Lean 4 prompt?
  - id: run_v1_model_receipts_run_post
    intent: Run a model call and get a signed receipt
    question: How do I get a signed receipt for a call to a specific model?
  - id: adapter_health_v1_model_receipts_adapter_health_get
    intent: Check live health of every model adapter
    question: Which model adapters are healthy and configured right now?
  - id: demo_matrix_v1_model_receipts_demo_matrix_get
    intent: Get the per-model demo matrix
    question: Where is the per-model demo matrix for model receipts?
  - id: smartmorph_route_demo_get_v1_model_receipts_smartmorph_route_demo_get
    intent: View the SmartMorph routing proof with built-in prompt
    question: Can I quickly see a SmartMorph route decision using the built-in prompt?
  - id: smartmorph_route_demo_post_v1_model_receipts_smartmorph_route_demo_post
    intent: Run the SmartMorph live route comparison
    question: How does SmartMorph compare live latency and token cost across models to pick a route?
  phrasing_ops: 8
  slug: thehiveryiq-com-model-receipts-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Morph API from Hive Civilization — 25 operation(s) for morph.
  name: Hive Civilization Morph API
  phrasing_intents:
  - id: morph_offer_v1_morph_offer_post
    intent: Request a Morph offer for an agent intent
    question: How do I get a HiveMorph offer token for what my agent wants to do?
  - id: morph_settle_v1_morph_settle__token_id__post
    intent: Settle a reserved Morph offer
    question: How do I commit the reservation behind a Morph offer token?
  - id: audit_recent_v1_morph_audit_recent_get
    intent: Show the latest Morph audit chain entries
    question: Where can I see the most recent rows in the Morph audit chain?
  - id: morph_identity_v1_morph_identity__mii_id__get
    intent: Get an agent's spectral identity card
    question: What does an agent's spectral identity card include, like tier, wings and sound?
  - id: morph_supermodels_v1_morph_supermodels_get
    intent: List all supermodel character cards
    question: Which supermodel characters does HiveMorph have and what role does each play?
  - id: morph_supermodel_detail_v1_morph_supermodels__name_or_id__get
    intent: Get one supermodel card by name or id
    question: What is the tagline, motto and palette of the MERCHANT supermodel?
  - id: morph_carousel_v1_morph_carousel_get
    intent: Get the cross-sell carousel for a shape
    question: Can I discover the full vertical menu without minting an offer token first?
  - id: brood_pending_approvals_v1_morph_brood_pending_approvals_get
    intent: List variants awaiting manual approval
    question: Which brood variants are still waiting for me to approve them?
  phrasing_ops: 25
  slug: thehiveryiq-com-morph-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The morso API from Hive Civilization — 6 operation(s) for morso.
  name: Hive Civilization Morso API
  phrasing_intents:
  - id: morso_health_v1_morso_health_get
    intent: Check the MORSO service health
    question: Is the MORSO excerpt receipt service up?
  - id: morso_issue_v1_morso_issue_post
    intent: Issue a MORSO excerpt from a sealed parent
    question: How do I issue a MORSO for an excerpt taken from a sealed parent document?
  - id: morso_receipt_v1_morso_receipt_post
    intent: Get a signed receipt for an excerpt
    question: How do I get a signed MORSO receipt proving an excerpt came from its parent?
  - id: morso_verify_v1_morso_verify_post
    intent: Verify a MORSO receipt
    question: Is this MORSO excerpt receipt genuine?
  - id: morso_classify_v1_morso_classify_post
    intent: Preview how an excerpt would be classified
    question: Can I see how an excerpt would be classified without getting a signed receipt?
  - id: morso_examples_v1_morso_examples_get
    intent: Get example MORSO payloads
    question: Are there sample requests I can copy for MORSO?
  phrasing_ops: 6
  slug: thehiveryiq-com-morso-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The mos-energy-arb API from Hive Civilization — 3 operation(s) for mos-energy-arb.
  name: Hive Civilization Mos Energy Arb API
  phrasing_intents:
  - id: push_utility_price_v1_mos_energy_arb_utility_price_post
    intent: Push a mining site's electricity tariff
    question: How do I report my facility's current $/kWh rate and hashrate?
  - id: get_recommendations_v1_mos_energy_arb_recommendations__site_did__get
    intent: Get mine, throttle or sell-forward advice
    question: Should my mining site keep mining, throttle or front-load given power prices?
  - id: billing_cycle_v1_mos_energy_arb_billing_cycle_post
    intent: Run the monthly savings billing cycle
    question: How are the 20%-of-savings invoices generated each month?
  phrasing_ops: 3
  slug: thehiveryiq-com-mos-energy-arb-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The mos-intel API from Hive Civilization — 5 operation(s) for mos-intel.
  name: Hive Civilization Mos Intel API
  phrasing_intents:
  - id: mos_register_v1_mos_intel_register_post
    intent: Register a mining site
    question: How do I register my mining site to get optimization recommendations?
  - id: mos_telemetry_v1_mos_intel_telemetry_post
    intent: Push signed telemetry from a mining site
    question: How do I send hashrate and temperature telemetry from my site?
  - id: mos_recommendations_v1_mos_intel_recommendations__site_did__get
    intent: Get optimization recommendations for a site
    question: What throttle or pool routing changes are suggested for my mining site?
  - id: mos_sites_v1_mos_intel_sites_get
    intent: List all registered mining sites (admin)
    question: How can an admin see every registered mining site?
  - id: mos_attest_v1_mos_intel_attest__site_did__get
    intent: Request a ZK attestation for a site
    question: Can I get a zero-knowledge attestation for my mining site yet?
  phrasing_ops: 5
  slug: thehiveryiq-com-mos-intel-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The mpp API from Hive Civilization — 4 operation(s) for mpp.
  name: Hive Civilization Mpp API
  phrasing_intents:
  - id: mpp_health_v1_receipt_mpp_health_get
    intent: Check MPP receipt minting configuration
    question: Is MPP payment configured for minting receipts yet?
  - id: mint_via_mpp_v1_receipt_mpp_post
    intent: Mint a receipt paid through MPP
    question: How do I mint a post-quantum receipt and pay for it with an MPP 402 challenge over Stripe?
  - id: create_spt_v1_receipt_mpp_spt_post
    intent: Create a Stripe Shared Payment Token
    question: How does an MPP client get a Stripe Shared Payment Token for a payment method?
  - id: mpp_discovery__well_known_mpp_json_get
    intent: Get the MPP service discovery manifest
    question: Where is the MPP discovery manifest for auto-discovery by aggregators?
  phrasing_ops: 4
  slug: thehiveryiq-com-mpp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The nanopay API from Hive Civilization — 4 operation(s) for nanopay.
  name: Hive Civilization Nanopay API
  phrasing_intents:
  - id: nanopay_bench_v1_nanopay_bench_get
    intent: View the live nanopay benchmark
    question: How many receipts per second is Hive Nanopay doing and at what cost per receipt?
  - id: nanopay_standard_v1_nanopay_standard_get
    intent: Get the Hive Nanopay spec metadata
    question: Which version of the Hive Nanopay standard is current and where is its repo?
  - id: nanopay_cross_rail_v1_nanopay_cross_rail_post
    intent: Issue a cross-rail nanopay receipt
    question: Can I issue one receipt that is verifiable on Base, Solana and Ethereum?
  - id: nanopay_cross_rail_verify_v1_nanopay_cross_rail_verify_post
    intent: Verify a cross-rail nanopay receipt
    question: How do I check that a cross-rail nanopay receipt is valid?
  phrasing_ops: 4
  slug: thehiveryiq-com-nanopay-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The nanoverse API from Hive Civilization — 21 operation(s) for nanoverse.
  name: Hive Civilization Nanoverse API
  phrasing_intents:
  - id: _info_handler_v1_nanoverse_api_pay_per_call_info_get
    intent: Describe the API pay-per-call nanoagent
    question: What does the NanoVerse API pay-per-call nanoagent offer and how is it priced?
  - id: _quote_handler_v1_nanoverse_api_pay_per_call_quote_post
    intent: Quote a price for pay-per-API-call billing
    question: Can I get a price quote for charging per API call without actually settling anything?
  - id: _info_handler_v1_nanoverse_compute_per_second_info_get
    intent: Describe the compute-per-second nanoagent
    question: What is the compute-per-second nanoagent and what pricing tier is it on?
  - id: _quote_handler_v1_nanoverse_compute_per_second_quote_post
    intent: Quote a price for per-second compute
    question: How much would per-second compute cost, as a quote that doesn't settle?
  - id: _info_handler_v1_nanoverse_data_per_query_info_get
    intent: Describe the data-per-query nanoagent
    question: What does the data-per-query nanoagent cover and what's its market size?
  - id: _quote_handler_v1_nanoverse_data_per_query_quote_post
    intent: Quote a price for per-query data access
    question: What would it cost to charge for data per query, quoted without settlement?
  - id: _info_handler_v1_nanoverse_agent_per_task_info_get
    intent: Describe the agent-per-task nanoagent
    question: What is the agent-per-task nanoagent and how is task-based billing priced?
  - id: _quote_handler_v1_nanoverse_agent_per_task_quote_post
    intent: Quote a price for a per-task agent job
    question: Can I get a quote for paying an agent per task before committing funds?
  phrasing_ops: 21
  slug: thehiveryiq-com-nanoverse-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The newsshield API from Hive Civilization — 11 operation(s) for newsshield.
  name: Hive Civilization Newsshield API
  phrasing_intents:
  - id: health_v1_newsshield_health_get
    intent: Check NewsShield service health
    question: Is the NewsShield media provenance service up?
  - id: pricing_v1_newsshield_pricing_get
    intent: View NewsShield pricing
    question: What does NewsShield charge for media lifecycle attestations?
  - id: capture_attest_v1_newsshield_capture_attest_post
    intent: Attest a media capture event
    question: How do I prove a photo or recording came from a specific camera or mic at capture time?
  - id: edit_attest_v1_newsshield_edit_attest_post
    intent: Attest an edit to a media asset
    question: Can I log an editing step on a photo or video and chain it back to its capture?
  - id: publish_attest_v1_newsshield_publish_attest_post
    intent: Attest publication of a media asset
    question: How can a newsroom attest that it published a piece of media, linked to its edit history?
  - id: syndicate_attest_v1_newsshield_syndicate_attest_post
    intent: Attest syndication of published media
    question: Can a syndication partner attest they republished a story, pointing back to the original publish?
  - id: takedown_attest_v1_newsshield_takedown_attest_post
    intent: Attest a takedown of published media
    question: How do I put a takedown of a published asset on the provenance record?
  - id: asset_get_v1_newsshield_asset__asset_id__get
    intent: Get every attestation for a media asset
    question: Can I see the full lifecycle of envelopes stored for one media asset?
  phrasing_ops: 11
  slug: thehiveryiq-com-newsshield-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The newsshield-mcp API from Hive Civilization — 1 operation(s) for newsshield-mcp.
  name: Hive Civilization Newsshield MCP API
  phrasing_intents:
  - id: newsshield_mcp_meta_v1_mcp_newsshield_get
    intent: Describe the NewsShield MCP server
    question: What does the NewsShield MCP server offer before I connect?
  - id: newsshield_mcp_v1_mcp_newsshield_post
    intent: Send an MCP request to NewsShield
    question: How does an agent call NewsShield tools over MCP?
  phrasing_ops: 2
  slug: thehiveryiq-com-newsshield-mcp-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Og API from Hive Civilization — 1 operation(s) for og.
  name: Hive Civilization Og API
  phrasing_intents:
  - id: og_quadrant_png_og_quadrant_png_get
    intent: Get the quadrant social preview image
    question: Is there a social share image of the current quadrant?
  phrasing_ops: 1
  slug: thehiveryiq-com-og-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The onboard API from Hive Civilization — 2 operation(s) for onboard.
  name: Hive Civilization Onboard API
  phrasing_intents:
  - id: stakes_classify_v1_stakes_classify_post
    intent: Classify how high-stakes a prompt is
    question: How risky or high-stakes is a prompt my users send?
  - id: health_v1_stakes_classify_health_get
    intent: Check the stakes classifier
    question: Is the stakes classifier running?
  phrasing_ops: 2
  slug: thehiveryiq-com-onboard-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The ops API from Hive Civilization — 6 operation(s) for ops.
  name: Hive Civilization Ops API
  phrasing_intents:
  - id: ops_health_v1_ops_health_get
    intent: Get aggregate health for every endpoint group
    question: What are the p50, p95 and error rates across every endpoint prefix?
  - id: ops_revenue_v1_ops_revenue_get
    intent: Get a revenue snapshot
    question: How much revenue has come in through card payments and the USDC treasury?
  - id: ops_calls_v1_ops_calls_get
    intent: List the busiest endpoints in the last minute
    question: Which endpoints are getting the most calls per minute right now?
  - id: ops_deploys_v1_ops_deploys_get
    intent: Show the last deploy for each service
    question: When was each service last deployed and at what commit?
  - id: ops_traffic_public_v1_ops_traffic_get
    intent: Get the public traffic snapshot
    question: Is there a public traffic summary I can show on a homepage tile?
  - id: ops_traffic_full_v1_ops_full_get
    intent: Get the full operator traffic view
    question: How do I see the full operator view of every service, repo and perimeter detail?
  phrasing_ops: 6
  slug: thehiveryiq-com-ops-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The organic API from Hive Civilization — 9 operation(s) for organic.
  name: Hive Civilization Organic API
  phrasing_intents:
  - id: rosetta_normalize_v1_rosetta_normalize_post
    intent: Normalize free-form input to a canonical schema
    question: Can I turn a messy natural-language request into a canonical intent, quote or route?
  - id: prospector_score_v1_prospector_score_post
    intent: Score an agent's intent as a prospect
    question: How promising is an agent as a prospect given what it wants to do?
  - id: hktn_lookup_v1_hktn_lookup_get
    intent: Look up an HKTN registration
    question: What HKTN tier is an agent registered under?
  - id: hktn_register_v1_hktn_register_post
    intent: Submit an HKTN registration intent
    question: How does an agent register for an HKTN tier and see the x402 discount it could earn?
  - id: rubric_select_v1_rubric_select_post
    intent: Select the rubric for an intent
    question: Which evaluation rubric applies to a given intent and amount?
  - id: settlement_reference_v1_settlement_reference_get
    intent: Generate a USDC settlement reference
    question: How do I get a settlement reference for paying an amount in USDC?
  - id: receipt_emit_v1_receipt_emit_post
    intent: Emit a signed receipt for an artifact
    question: How does an agent get a signed receipt over an artifact it produced?
  - id: receipt_emit_preflight_v1_receipt_emit_get
    intent: Preflight the receipt emit endpoint
    question: What do I need to send before emitting a signed receipt?
  phrasing_ops: 10
  slug: thehiveryiq-com-organic-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Origin API from Hive Civilization — 1 operation(s) for origin.
  name: Hive Civilization Origin API
  phrasing_intents:
  - id: origin_mcp_meta_v1_origin_mcp_get
    intent: Get the Origin MCP server metadata
    question: What does the Origin MCP endpoint expose?
  - id: origin_mcp_v1_origin_mcp_post
    intent: Send a request to the Origin MCP server
    question: How do I send an MCP message to the Origin server?
  phrasing_ops: 2
  slug: thehiveryiq-com-origin-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The pilot API from Hive Civilization — 3 operation(s) for pilot.
  name: Hive Civilization Pilot API
  phrasing_intents:
  - id: pilot_accept_v1_pilot_accept_post
    intent: Countersign a pilot offer
    question: How do I accept and countersign a pilot offer?
  - id: accepts_recent_v1_pilot_accepts_recent_get
    intent: List recently accepted pilots
    question: Which pilot offers have been accepted recently?
  - id: pilot_health_v1_pilot_health_get
    intent: Check pilot service health
    question: Is the pilot acceptance service up?
  phrasing_ops: 3
  slug: thehiveryiq-com-pilot-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The portal API from Hive Civilization — 4 operation(s) for portal.
  name: Hive Civilization Portal API
  phrasing_intents:
  - id: portal_kpi_v1_portal__tenant_id__kpi_get
    intent: Get a tenant's KPI snapshot
    question: What are the headline KPIs for my tenant?
  - id: portal_balance_v1_portal__tenant_id__balance_get
    intent: Get a tenant's balance and billing state
    question: What's my tenant's on-chain balance and billing status?
  - id: portal_rotate_key_v1_portal__tenant_id__api_key_rotate_post
    intent: Rotate a tenant's API key
    question: How do I rotate my API key without breaking in-flight requests?
  - id: portal_revoke_key_v1_portal__tenant_id__api_key_revoke_post
    intent: Revoke a tenant's API keys immediately
    question: How do I kill all active API keys for my tenant right now?
  phrasing_ops: 4
  slug: thehiveryiq-com-portal-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The portal-spin API from Hive Civilization — 8 operation(s) for portal-spin.
  name: Hive Civilization Portal Spin API
  phrasing_intents:
  - id: spin_start_v1_portal_spin_start_post
    intent: Start an anonymous demo spin session
    question: Can I try the receipt portal without signing up?
  - id: spin_emit_receipt_v1_portal_spin_emit_receipt_post
    intent: Add a sample receipt to a spin session
    question: How do I generate another dual-signed sample receipt in my demo session?
  - id: spin_promote_v1_portal_spin_promote_post
    intent: Promote a demo spin session into a real tenant
    question: How do I turn my demo spin session into a real dashboard account?
  - id: tenant_lattice_v1_portal__tenant_id__lattice_get
    intent: Get a tenant's receipts for the lattice view
    question: How do I get my receipts laid out for the wave-lattice visualization?
  - id: tenant_ledger_v1_portal__tenant_id__ledger_get
    intent: View a tenant's full accounting ledger
    question: Where can I see every charge and settlement with its USDC transaction hash?
  - id: reports_pull_v1_portal__tenant_id__reports_pull_post
    intent: Generate a tenant report on demand
    question: Can I pull a compliance or usage report for a date range right now?
  - id: reports_schedule_v1_portal__tenant_id__reports_schedule_post
    intent: Schedule a recurring email report
    question: How do I get a daily or weekly report emailed to me?
  - id: reports_reminders_v1_portal__tenant_id__reports_reminders_post
    intent: Set a threshold alert for a tenant
    question: Can I get alerted when my error rate or volume crosses a threshold?
  phrasing_ops: 8
  slug: thehiveryiq-com-portal-spin-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The portal-v2 API from Hive Civilization — 5 operation(s) for portal-v2.
  name: Hive Civilization Portal V2 API
  phrasing_intents:
  - id: portal_v2_signup_v1_portal_v2_signup_post
    intent: Sign up a new portal tenant
    question: How do I create a tenant in the portal from a company domain?
  - id: portal_v2_profile_v1_portal_v2__tenant_id__profile_get
    intent: Get a tenant's portal profile
    question: What does the portal know about my tenant's brand and vertical?
  - id: portal_v2_tile_prefs_v1_portal_v2__tenant_id__tile_prefs_post
    intent: Set a portal tile's visibility
    question: How do I show or hide a tile on my tenant portal?
  - id: portal_v2_wisdom_v1_portal_v2__tenant_id__wisdom_get
    intent: Get AI recommendations for a tenant
    question: What AI recommendations does the portal have for my business?
  - id: portal_v2_activate_feature_v1_portal_v2__tenant_id__features_activate_post
    intent: Activate a feature for a tenant
    question: How do I turn on a paid feature for my tenant?
  phrasing_ops: 5
  slug: thehiveryiq-com-portal-v2-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The pq API from Hive Civilization — 4 operation(s) for pq.
  name: Hive Civilization Pq API
  phrasing_intents:
  - id: route_pq_selftest_v1_smsh_pq_selftest_get
    intent: Run the post-quantum crypto self-test
    question: Does the ML-DSA-65 and ML-KEM-768 implementation pass a NIST conformance round trip?
  - id: route_pq_keys_sample_v1_smsh_pq_keys_sample_get
    intent: Generate a sample ML-DSA-65 keypair
    question: Can I get a throwaway ML-DSA-65 keypair for integration testing?
  - id: route_pq_sign_v1_smsh_pq_sign_post
    intent: Sign a message with ML-DSA-65
    question: How do I sign a message with a post-quantum ML-DSA-65 key?
  - id: route_pq_verify_v1_smsh_pq_verify_post
    intent: Verify an ML-DSA-65 signature
    question: Can I verify a post-quantum signature for free?
  phrasing_ops: 4
  slug: thehiveryiq-com-pq-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Pricing API from Hive Civilization — 1 operation(s) for pricing.
  name: Hive Civilization Pricing API
  phrasing_intents:
  - id: pricing_alias_pricing_get
    intent: View pricing via the root alias
    question: Is there a short root URL for pricing?
  phrasing_ops: 1
  slug: thehiveryiq-com-pricing-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Pricing.json API from Hive Civilization — 1 operation(s) for pricing.json.
  name: Hive Civilization Pricing.json API
  phrasing_intents:
  - id: pricing_json_alias_pricing_json_get
    intent: Get receipt-profile pricing as JSON
    question: What does each receipt profile cost, in machine-readable JSON?
  phrasing_ops: 1
  slug: thehiveryiq-com-pricing-json-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Prior API from Hive Civilization — 1 operation(s) for prior.
  name: Hive Civilization Prior API
  phrasing_intents:
  - id: prior_mcp_meta_v1_prior_mcp_get
    intent: Get Prior MCP server metadata
    question: What does the Prior patent-priority MCP server advertise?
  - id: prior_mcp_v1_prior_mcp_post
    intent: Send a request to the Prior MCP server
    question: Can my agent stamp or look up priority records through MCP?
  phrasing_ops: 2
  slug: thehiveryiq-com-prior-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Procurelock API from Hive Civilization — 11 operation(s) for procurelock.
  name: Hive Civilization Procurelock API
  phrasing_intents:
  - id: procurelock_mcp_meta_v1_procurelock_mcp_get
    intent: Describe the ProcureLock MCP server
    question: What does the ProcureLock MCP server expose to agents?
  - id: procurelock_mcp_v1_procurelock_mcp_post
    intent: Call the ProcureLock MCP server
    question: How do I send an MCP request to ProcureLock?
  - id: health_v1_procurelock_health_get
    intent: Check ProcureLock health
    question: Is the ProcureLock purchase-order attestation service up?
  - id: pricing_v1_procurelock_pricing_get
    intent: Get ProcureLock pricing
    question: What does it cost to attest a purchase order or delivery with ProcureLock?
  - id: po_attest_v1_procurelock_po_attest_post
    intent: Attest a purchase order event
    question: How do I create a signed attestation for a purchase order?
  - id: po_get_v1_procurelock_po_get__attestation_id__get
    intent: Get a purchase order attestation
    question: How do I retrieve a PO attestation record by its id?
  - id: po_verify_v1_procurelock_po_verify__attestation_id__get
    intent: Verify a purchase order attestation
    question: Can I prove a purchase order attestation's signature is valid?
  - id: delivery_attest_v1_procurelock_delivery_attest_post
    intent: Attest a delivery against a purchase order
    question: How do I record a goods-received attestation for a purchase order?
  phrasing_ops: 12
  slug: thehiveryiq-com-procurelock-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The protected-flow API from Hive Civilization — 3 operation(s) for protected-flow.
  name: Hive Civilization Protected Flow API
  phrasing_intents:
  - id: protected_flow_health_v1_protected_flow_health_get
    intent: Discover Protected Flow capabilities
    question: Which decision classes and policy packs does Protected Flow support?
  - id: protected_flow_assess_v1_protected_flow_assess_post
    intent: Assess a receipt group and get a signed decision
    question: How do I get a signed risk decision and meter quote for a group of payment receipts?
  - id: protected_flow_evidence_export_v1_protected_flow_evidence__group_id__export_get
    intent: Export the evidence bundle for a receipt group
    question: How do I export the signed evidence for an assessed receipt group?
  phrasing_ops: 3
  slug: thehiveryiq-com-protected-flow-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The prov API from Hive Civilization — 2 operation(s) for prov.
  name: Hive Civilization Prov API
  phrasing_intents:
  - id: prov_pubkey_v1_prov_pubkey_get
    intent: Get the provenance signing public key
    question: What Ed25519 public key signs smash.prov provenance headers?
  - id: prov_verify_v1_prov_verify_post
    intent: Verify a response provenance signature
    question: How can I prove a response really came from this service?
  phrasing_ops: 2
  slug: thehiveryiq-com-prov-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The provebirth API from Hive Civilization — 10 operation(s) for provebirth.
  name: Hive Civilization Provebirth API
  phrasing_intents:
  - id: health_v1_provebirth_health_get
    intent: Check ProveBirth service health
    question: Is the ProveBirth agent certificate service up?
  - id: pricing_v1_provebirth_pricing_get
    intent: Get ProveBirth pricing
    question: How much does it cost to issue an agent birth certificate?
  - id: cert_issue_v1_provebirth_cert_issue_post
    intent: Issue a birth certificate for an AI agent
    question: How do I issue a birth certificate that pins an agent's model and tool grants?
  - id: cert_get_v1_provebirth_cert__cert_id__get
    intent: Retrieve an agent birth certificate
    question: How do I look up an agent birth certificate by its ID?
  - id: cert_verify_v1_provebirth_cert_verify_post
    intent: Verify the signatures on a birth certificate
    question: Are the signatures on this agent birth certificate valid?
  - id: action_attest_v1_provebirth_action_attest_post
    intent: Attest an action taken by a certified agent
    question: How do I record a tool call or payment an agent made, chained to its birth certificate?
  - id: lineage_verify_v1_provebirth_lineage_verify_post
    intent: Verify an agent's action lineage
    question: Is an agent's whole chain of actions traceable back to its birth certificate?
  - id: by_agent_v1_provebirth_by_agent__agent_did__get
    intent: List certificates for an agent
    question: Which birth certificates have been issued to a particular agent?
  phrasing_ops: 10
  slug: thehiveryiq-com-provebirth-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The purity API from Hive Civilization — 3 operation(s) for purity.
  name: Hive Civilization Purity API
  phrasing_intents:
  - id: health_v1_purity_health_get
    intent: Check the purity certificate service
    question: Is the purity certification service up?
  - id: cert_issue_v1_purity_cert_issue_post
    intent: Issue a purity certificate
    question: How do I issue a purity certificate for a product?
  - id: cert_get_v1_purity_cert__cert_id__get
    intent: Get a purity certificate
    question: What does an issued purity certificate say?
  phrasing_ops: 3
  slug: thehiveryiq-com-purity-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The qvac API from Hive Civilization — 11 operation(s) for qvac.
  name: Hive Civilization Qvac API
  phrasing_intents:
  - id: register_provider_v1_qvac_provider_register_post
    intent: Register a QVAC inference provider
    question: How do I register my agent as a QVAC inference provider?
  - id: list_providers_v1_qvac_provider_list_get
    intent: List QVAC inference providers
    question: Which QVAC inference providers are registered?
  - id: get_provider_v1_qvac_provider__provider_id__get
    intent: Get a QVAC provider
    question: What models and capabilities does a specific QVAC provider offer?
  - id: unregister_provider_v1_qvac_provider__provider_id__unregister_post
    intent: Unregister a QVAC provider
    question: How do I take my agent out of the QVAC provider pool?
  - id: inference_request_v1_qvac_inference_request_post
    intent: Request a QVAC inference
    question: How do I run a prompt against a QVAC model?
  - id: inference_request_public_v1_qvac_inference_request_public_post
    intent: Request a QVAC inference paid by x402
    question: Can I pay for a QVAC inference with an x402 payment instead of an account?
  - id: leaderboard_v1_qvac_leaderboard_get
    intent: View the QVAC provider leaderboard
    question: Which QVAC inference providers rank highest?
  - id: agent_c_spread_v1_qvac_agent_c_spread_get
    intent: Get Agent C's QVAC spread quote
    question: What spread would Agent C capture on a QVAC inference at a given notional?
  phrasing_ops: 11
  slug: thehiveryiq-com-qvac-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r10-rvc API from Hive Civilization — 8 operation(s) for r10-rvc.
  name: Hive Civilization R10 Rvc API
  phrasing_intents:
  - id: rvc_policy_v1_rvc_policy_get
    intent: Get the rubric vector commitment policy
    question: What policy governs rubric vector commitments?
  - id: rvc_srs_v1_rvc_srs_get
    intent: Get the commitment scheme's reference string
    question: Where is the structured reference string used for rubric commitments?
  - id: rvc_commit_v1_rvc_commit_post
    intent: Commit to a rubric score vector
    question: How do I lock in a score vector against a rubric so it can't be changed later?
  - id: rvc_open_v1_rvc_open_post
    intent: Open one position of a commitment
    question: Can I reveal a single score from a committed vector with a proof?
  - id: rvc_batch_open_v1_rvc_batch_open_post
    intent: Open several commitment positions at once
    question: Can I get openings for many positions of a commitment in one call?
  - id: rvc_verify_v1_rvc_verify_post
    intent: Verify a commitment opening
    question: How can I check an opening really matches the commitment?
  - id: rvc_get_v1_rvc__commitment_id__get
    intent: Get a rubric commitment
    question: What's recorded for a commitment I already made?
  - id: rvc_openings_v1_rvc__commitment_id__openings_get
    intent: List openings issued for a commitment
    question: Which positions of a commitment have already been revealed?
  phrasing_ops: 8
  slug: thehiveryiq-com-r10-rvc-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r2-discovery API from Hive Civilization — 6 operation(s) for r2-discovery.
  name: Hive Civilization R2 Discovery API
  phrasing_intents:
  - id: get_manifest_manifest_get
    intent: Get the Hivemorph plugin manifest
    question: Where is the plugin manifest that points to Hivemorph's OpenAPI and MCP descriptor?
  - id: get_a2a_descriptor_a2a_get
    intent: Describe the A2A JSON-RPC transport
    question: Which JSON-RPC methods does the A2A endpoint support?
  - id: post_a2a_a2a_post
    intent: Send an A2A JSON-RPC request
    question: Can my agent call agent.discover or receipt.verify over JSON-RPC?
  - id: well_known_a2a__well_known_a2a_json_get
    intent: Get the well-known A2A descriptor
    question: Is there a .well-known/a2a.json file for crawlers to find the A2A endpoint?
  - id: get_status_status_get
    intent: Check Hivemorph live status
    question: Which Hivemorph layers are live, in pilot or on the roadmap?
  - id: get_status_a2a_alias_v1_a2a_status_get
    intent: Check status via the A2A path
    question: Can agents fetch Hivemorph status under the /v1/a2a path?
  - id: get_transaction_harness_v1_transaction_harness_get
    intent: Get the 14-stage transaction harness
    question: Which stages of the transaction harness are live versus sample or roadmap?
  phrasing_ops: 7
  slug: thehiveryiq-com-r2-discovery-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r3-delegation API from Hive Civilization — 8 operation(s) for r3-delegation.
  name: Hive Civilization R3 Delegation API
  phrasing_intents:
  - id: issue_v1_delegation_issue_post
    intent: Issue a delegation envelope signed by Hive
    question: How do I give my agent a signed delegation limiting what it may do and spend?
  - id: operator_sign_v1_delegation_operator_sign_post
    intent: Counter-stamp an envelope I signed myself
    question: How do I submit a delegation I signed with my own operator Ed25519 key?
  - id: verify_v1_delegation_verify_post
    intent: Verify a delegation envelope
    question: How do I check a delegation's signatures, expiry and revocation status?
  - id: revoke_v1_delegation_revoke__jti__post
    intent: Revoke a delegation
    question: How do I cancel a delegation I gave an agent?
  - id: pubkey_v1_delegation_pubkey_get
    intent: Get the delegation signing public keys
    question: Which public keys should I use to verify delegation signatures offline?
  - id: get_one_v1_delegation__jti__get
    intent: Fetch a stored delegation
    question: How do I look up a delegation I issued earlier by its ID?
  - id: firewall_eval_v1_firewall_evaluate_post
    intent: Evaluate a request against a delegation
    question: Would this agent request be allowed, blocked or sent for human approval under its delegation?
  - id: delegation_check_v1_delegation_check_post
    intent: Verify delegation and get firewall decision at once
    question: Can I verify a delegation and get the firewall decision in one call?
  phrasing_ops: 8
  slug: thehiveryiq-com-r3-delegation-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r3pv API from Hive Civilization — 4 operation(s) for r3pv.
  name: Hive Civilization R3pv API
  phrasing_intents:
  - id: r3pv_health_v1_r3pv_health_get
    intent: Discover R3Pv version and signer details
    question: Which version of the receipt proof-vector service is running and which signer does it use?
  - id: r3pv_create_group_v1_r3pv_groups_post
    intent: Create a receipt group
    question: How do I bundle several receipts into one group for later proofs?
  - id: r3pv_get_group_v1_r3pv_groups__group_id__get
    intent: Fetch a stored receipt group
    question: How do I look up a receipt group I created earlier?
  - id: r3pv_vector_get_v1_r3pv_vector_get
    intent: Compute a signed proof vector for a group
    question: How do I get a signed proof vector for an existing receipt group?
  - id: r3pv_vector_post_v1_r3pv_vector_post
    intent: Group receipts and compute a vector in one call
    question: Can I group receipts and get their proof vector in a single request?
  phrasing_ops: 5
  slug: thehiveryiq-com-r3pv-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r4-firewall API from Hive Civilization — 9 operation(s) for r4-firewall.
  name: Hive Civilization R4 Firewall API
  phrasing_intents:
  - id: policy_v1_firewall_policy_get
    intent: Get the tool firewall enforcement policy
    question: How does the Hive Tool Firewall decide what to allow, block or escalate?
  - id: enforce_preview_v1_firewall_enforce_preview_post
    intent: Dry-run firewall enforcement on an envelope
    question: Can I preview what HTTP status the firewall would return for a request without persisting anything?
  - id: sandbox_run_v1_firewall_sandbox_run_post
    intent: Run a request in firewall sandbox mode
    question: How do I test that an envelope authorizes a request without any settlement happening?
  - id: cosign_create_v1_firewall_cosign_challenge_post
    intent: Open a threshold cosign challenge
    question: How do I require several cosigners before a blocked agent request can proceed?
  - id: cosign_get_v1_firewall_cosign_challenge__challenge_id__get
    intent: Get a cosign challenge's status
    question: How many cosignatures has a challenge collected so far?
  - id: cosign_sign_v1_firewall_cosign_challenge__challenge_id__sign_post
    intent: Add a cosignature to a challenge
    question: How do I submit my signature toward a cosign challenge?
  - id: approval_request_v1_firewall_approval_request_post
    intent: Request human approval for an agent action
    question: How do I escalate a blocked agent request to a human for approval?
  - id: approval_get_v1_firewall_approval__ticket_id__get
    intent: Get a human-approval ticket
    question: Has my approval ticket been approved or denied yet?
  phrasing_ops: 9
  slug: thehiveryiq-com-r4-firewall-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r5-hktn-reputation API from Hive Civilization — 5 operation(s) for r5-hktn-reputation.
  name: Hive Civilization R5 Hktn Reputation API
  phrasing_intents:
  - id: rep_policy_v1_hktn_rep_policy_get
    intent: Get the HKTN reputation policy
    question: How is an agent's HKTN reputation calculated?
  - id: rep_leaderboard_v1_hktn_rep_leaderboard_get
    intent: Rank agents by reputation
    question: Which agents have the highest HKTN reputation?
  - id: rep_event_v1_hktn_rep_event_post
    intent: Record a reputation event for an agent
    question: How do I log something an agent did so it counts toward its reputation?
  - id: rep_preview_v1_hktn_rep_preview_post
    intent: Preview reputation after hypothetical events
    question: What would an agent's reputation become if certain events happened?
  - id: rep_get_v1_hktn_rep__agent_did__get
    intent: Get an agent's reputation
    question: What is an agent's current HKTN reputation tier?
  phrasing_ops: 5
  slug: thehiveryiq-com-r5-hktn-reputation-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r6-hivememory API from Hive Civilization — 6 operation(s) for r6-hivememory.
  name: Hive Civilization R6 Hivememory API
  phrasing_intents:
  - id: memory_policy_v1_memory_policy_get
    intent: Get the agent memory policy
    question: What rules govern what agents can store in HiveMemory?
  - id: memory_write_v1_memory_write_post
    intent: Store a memory for an agent
    question: How do I save a memory record for my agent with provenance?
  - id: memory_list_v1_memory_list_get
    intent: List agent memories
    question: What memories has an agent stored, filtered by kind or scope?
  - id: memory_revoke_v1_memory_revoke__mid__post
    intent: Revoke an agent memory
    question: How do I revoke a memory so the agent stops using it?
  - id: memory_export_v1_memory_export__agent_did__get
    intent: Export all of an agent's memories
    question: Can I export everything an agent remembers in one go?
  - id: memory_get_v1_memory__mid__get
    intent: Get one agent memory
    question: What does a specific stored memory contain?
  phrasing_ops: 6
  slug: thehiveryiq-com-r6-hivememory-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r7-spectral API from Hive Civilization — 7 operation(s) for r7-spectral.
  name: Hive Civilization R7 Spectral API
  phrasing_intents:
  - id: spectral_policy_v1_spectral_policy_get
    intent: Get the spectral monitoring policy
    question: What thresholds does spectral behaviour monitoring use to flag agents?
  - id: spectral_stats_v1_spectral_stats_get
    intent: Get spectral monitoring statistics
    question: How many agents and observations is spectral monitoring tracking?
  - id: spectral_observe_v1_spectral_observe_post
    intent: Record an agent behaviour observation
    question: How do I log what an agent just did so its behaviour baseline updates?
  - id: spectral_evaluate_v1_spectral_evaluate_post
    intent: Score whether an agent action looks anomalous
    question: Is this agent call unusual compared with its normal behaviour?
  - id: spectral_observations_v1_spectral__agent_did__observations_get
    intent: List an agent's recorded observations
    question: What recent activity has been recorded for a specific agent?
  - id: spectral_alerts_v1_spectral__agent_did__alerts_get
    intent: List anomaly alerts for an agent
    question: Has a particular agent triggered any behaviour anomaly alerts?
  - id: spectral_fingerprint_v1_spectral__agent_did__get
    intent: Get an agent's behaviour fingerprint
    question: What does an agent's normal behaviour profile look like?
  phrasing_ops: 7
  slug: thehiveryiq-com-r7-spectral-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r8-checkpoints API from Hive Civilization — 7 operation(s) for r8-checkpoints.
  name: Hive Civilization R8 Checkpoints API
  phrasing_intents:
  - id: checkpoint_policy_v1_checkpoint_policy_get
    intent: Get the workflow checkpoint policy
    question: What rules apply to agent workflow checkpoints?
  - id: checkpoint_write_v1_checkpoint_write_post
    intent: Write an agent workflow checkpoint
    question: How do I save a checkpoint for an agent at a given workflow phase?
  - id: checkpoint_list_v1_checkpoint_list_get
    intent: List workflow checkpoints
    question: Which checkpoints exist for an agent or workflow?
  - id: checkpoint_workflow_v1_checkpoint_workflow__wid__get
    intent: Get a workflow's checkpoints
    question: What is the current checkpoint state of a workflow?
  - id: checkpoint_archive_v1_checkpoint_archive__wid__post
    intent: Archive a workflow's checkpoints
    question: Can I archive a finished workflow's checkpoints?
  - id: checkpoint_replay_v1_checkpoint_replay__wid__get
    intent: Replay a workflow from its checkpoints
    question: Can I replay a workflow's checkpoints in order?
  - id: checkpoint_get_v1_checkpoint__cid__get
    intent: Get a single checkpoint
    question: Can I fetch one checkpoint by its checkpoint id?
  phrasing_ops: 7
  slug: thehiveryiq-com-r8-checkpoints-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The r9-accumulators API from Hive Civilization — 8 operation(s) for r9-accumulators.
  name: Hive Civilization R9 Accumulators API
  phrasing_intents:
  - id: accumulator_policy_v1_accumulator_policy_get
    intent: Get the accumulator policy
    question: What rules govern the cryptographic accumulators?
  - id: accumulator_anchor_v1_accumulator_anchor_post
    intent: Anchor a key into an accumulator
    question: How do I add a key and value to an accumulator domain?
  - id: accumulator_root_v1_accumulator__domain__root_get
    intent: Get an accumulator's current root
    question: What is the current root of an accumulator domain?
  - id: accumulator_leaves_v1_accumulator__domain__leaves_get
    intent: List an accumulator's leaves
    question: Which entries have been anchored into a domain?
  - id: accumulator_replay_v1_accumulator__domain__replay_get
    intent: Replay an accumulator's history
    question: Can I replay a domain's accumulator from the start to confirm its root?
  - id: accumulator_inclusion_v1_accumulator__domain__inclusion_get
    intent: Get an inclusion witness for a key
    question: Can I get proof that a key is in an accumulator?
  - id: accumulator_non_membership_v1_accumulator__domain__non_membership_get
    intent: Prove a key is absent from an accumulator
    question: Can I prove a key has never been anchored in a domain?
  - id: accumulator_verify_v1_accumulator_verify_post
    intent: Verify an accumulator inclusion witness
    question: Is an inclusion witness I was given actually valid?
  phrasing_ops: 8
  slug: thehiveryiq-com-r9-accumulators-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Receipt API from Hive Civilization — 1 operation(s) for receipt.
  name: Hive Civilization Receipt API
  phrasing_intents:
  - id: receipt_mcp_meta_v1_receipt_mcp_get
    intent: Describe the receipt MCP server
    question: Is there an MCP server for issuing and verifying receipts?
  - id: receipt_mcp_v1_receipt_mcp_post
    intent: Send a request to the receipt MCP server
    question: How do my agents call the receipt tools over MCP?
  phrasing_ops: 2
  slug: thehiveryiq-com-receipt-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The receipt-ledger API from Hive Civilization — 4 operation(s) for receipt-ledger.
  name: Hive Civilization Receipt Ledger API
  phrasing_intents:
  - id: append_to_ledger_v1_receipts_post
    intent: Append an entry to the receipt ledger
    question: How do I add a new signed entry to the append-only receipt ledger?
  - id: query_ledger_v1_receipts_get
    intent: Search the receipt ledger
    question: Which ledger entries were recorded for a particular supermodel?
  - id: ledger_summary_v1_receipts_summary_get
    intent: Summarize the receipt ledger
    question: What are the aggregate totals across the entire receipt ledger?
  - id: ledger_pubkey_v1_receipts_pubkey_get
    intent: Get the ledger's signing public key
    question: Which Ed25519 public key signs the receipt ledger entries?
  - id: ledger_verify_v1_receipts_verify__seq__get
    intent: Verify one ledger entry's signature
    question: How do I prove a specific ledger entry hasn't been tampered with?
  phrasing_ops: 5
  slug: thehiveryiq-com-receipt-ledger-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The receipt-relay API from Hive Civilization — 4 operation(s) for receipt-relay.
  name: Hive Civilization Receipt Relay API
  phrasing_intents:
  - id: relay_health_v1_receipt_relay_health_get
    intent: Describe the receipt relay
    question: Which modes and evidence tiers does the receipt relay support?
  - id: relay_event_v1_receipt_relay_event_post
    intent: Sign a receipt for an external event
    question: How can I get a signed self-attested receipt for something that happened in another system?
  - id: relay_http_v1_receipt_relay_http_post
    intent: Make a relayed HTTP call with a receipt
    question: Can the relay make an outbound HTTP request for me and sign what it saw?
  - id: relay_chain_v1_receipt_relay_chain_post
    intent: Record a receipt for a blockchain transaction
    question: How do I get a receipt for a Solana or EVM transaction?
  phrasing_ops: 4
  slug: thehiveryiq-com-receipt-relay-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Robots.txt API from Hive Civilization — 1 operation(s) for robots.txt.
  name: Hive Civilization Robots.txt API
  phrasing_intents:
  - id: robots_txt_robots_txt_get
    intent: Get the site's robots.txt crawl rules
    question: What does the robots.txt allow crawlers and agents to fetch?
  phrasing_ops: 1
  slug: thehiveryiq-com-robots-txt-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The runrate API from Hive Civilization — 4 operation(s) for runrate.
  name: Hive Civilization Runrate API
  phrasing_intents:
  - id: runrate_tick_v1_runrate_tick_post
    intent: Run one run-rate orchestrator tick
    question: How do I manually fire the run-rate drivers that are due?
  - id: runrate_status_v1_runrate_status_get
    intent: Get the current run-rate snapshot
    question: What is the current revenue run rate?
  - id: runrate_ledger_v1_runrate_ledger_get
    intent: Read recent run-rate ledger entries
    question: What has the run-rate ledger recorded recently?
  - id: runrate_schedule_v1_runrate_schedule_get
    intent: See the run-rate driver schedule
    question: When did each run-rate driver last run and when is it next due?
  phrasing_ops: 4
  slug: thehiveryiq-com-runrate-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The salvage API from Hive Civilization — 23 operation(s) for salvage.
  name: Hive Civilization Salvage API
  phrasing_intents:
  - id: listener_observe_v1_salvage_listener_observe_post
    intent: Inject a failure signal for a transaction
    question: How do I manually feed a transaction signal into the Salvage listener from an external source?
  - id: listener_observe_bridge_v1_salvage_listener_observe_bridge_post
    intent: Report a cross-chain bridge observation
    question: How do I tell Salvage a bridge transfer left the source chain but never arrived at the destination?
  - id: listener_queue_v1_salvage_listener_queue_get
    intent: List verified failures awaiting recovery
    question: Which verified transaction failures are still waiting to be recovered?
  - id: listener_sources_v1_salvage_listener_sources_get
    intent: View the signal source trust registry
    question: How much does Salvage trust each of my signal sources?
  - id: listener_quarantine_v1_salvage_listener_quarantine_get
    intent: List permanently quarantined signal sources
    question: Which signal sources have been permanently quarantined?
  - id: recovery_file_v1_salvage_recovery_file_post
    intent: File a recovery claim for a failed transaction
    question: How do I file a claim to recover funds from a failed transaction?
  - id: recovery_status_v1_salvage_recovery_status_get
    intent: Check the status of a recovery claim
    question: Where does my recovery claim stand right now?
  - id: recovery_auto_v1_salvage_recovery_auto_post
    intent: Auto-process the top verified failures
    question: Can I automatically process the top verified failures in the queue instead of filing claims one by one?
  phrasing_ops: 23
  slug: thehiveryiq-com-salvage-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The site-traffic API from Hive Civilization — 9 operation(s) for site-traffic.
  name: Hive Civilization Site Traffic API
  phrasing_intents:
  - id: beacon_v1_site_beacon_post
    intent: Record a page-view beacon
    question: How do I log a page view from my site to first-party analytics?
  - id: traffic_v1_site_traffic_get
    intent: Summarize site traffic
    question: Which pages, referrers, countries and companies drove my site traffic?
  - id: page_detail_v1_site_page_get
    intent: See every visit to one page
    question: Has anyone opened a particular page on my site?
  - id: timeseries_v1_site_timeseries_get
    intent: Get a traffic time series
    question: Can I get page views bucketed over time for a sparkline?
  - id: events_v1_site_events_get
    intent: Tail recent site events
    question: What are the latest events coming into my site right now?
  - id: live_brief_v1_site_live_brief_get
    intent: Get an operator brief on current visitors
    question: Is the visitor on my site right now a real prospect or a crawler?
  - id: prospect_detail_v1_site_prospect__utm__get
    intent: See visits from one outreach tag
    question: Did the prospect I sent a tagged link to actually visit?
  - id: traffic_redact_v1_site_traffic_redact_post
    intent: Wipe traffic records matching a filter
    question: How do I delete smoke-test or deploy-test records from my traffic data?
  phrasing_ops: 9
  slug: thehiveryiq-com-site-traffic-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Sitemap.xml API from Hive Civilization — 1 operation(s) for sitemap.xml.
  name: Hive Civilization Sitemap.xml API
  phrasing_intents:
  - id: sitemap_xml_sitemap_xml_get
    intent: Get the site's XML sitemap
    question: Which pages are listed in the HiveMorph sitemap?
  phrasing_ops: 1
  slug: thehiveryiq-com-sitemap-xml-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The smsh API from Hive Civilization — 8 operation(s) for smsh.
  name: Hive Civilization Smsh API
  phrasing_intents:
  - id: smsh_compress_v1_smsh_compress_post
    intent: Compress a prompt with smsh
    question: How do I shrink a long prompt to save tokens?
  - id: smsh_decompress_v1_smsh_decompress_post
    intent: Decompress an smsh-compressed prompt
    question: How do I turn an smsh-compressed prompt back into readable text?
  - id: smsh_compress_demo_v1_smsh_compress_demo_post
    intent: Try smsh compression for free
    question: Can I try prompt compression for free before paying?
  - id: smsh_health_v1_smsh_health_get
    intent: Check smsh service health
    question: Is the prompt compression service up?
  - id: smsh_v1_5_warmup_v1_smsh_v1_5_warmup_get
    intent: Check or trigger v1.5 model warmup (GET)
    question: Are the v1.5 compression models loaded yet?
  - id: smsh_v1_5_warmup_v1_smsh_v1_5_warmup_post
    intent: Pre-load v1.5 compression models (POST)
    question: How do I warm up the compression models after a deploy to avoid a slow first call?
  - id: smsh_dictionary_v1_smsh_dictionary_get
    intent: Get the smsh boilerplate dictionary
    question: Which boilerplate phrases does smsh replace with sentinels?
  - id: smsh_modes_v1_smsh_modes_get
    intent: List smsh compression modes
    question: What compression modes are available and what ratio does each target?
  phrasing_ops: 9
  slug: thehiveryiq-com-smsh-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The smsh-learned API from Hive Civilization — 2 operation(s) for smsh-learned.
  name: Hive Civilization Smsh Learned API
  phrasing_intents:
  - id: smsh_judge_v1_smsh_judge_post
    intent: Score how important each span of text is
    question: Which parts of my prompt matter most to the downstream answer?
  - id: smsh_learned_prune_v1_smsh_learned_prune_post
    intent: Compress text by pruning low-importance spans
    question: How can I shrink a long prompt by dropping its least important spans?
  phrasing_ops: 2
  slug: thehiveryiq-com-smsh-learned-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The spawn-garage-v2 API from Hive Civilization — 6 operation(s) for spawn-garage-v2.
  name: Hive Civilization Spawn Garage V2 API
  phrasing_intents:
  - id: scan_all_proposers_v1_morph_spawn_v2_scan_post
    intent: Run all spawn proposers once
    question: How do I generate fresh proposals for new agents to spawn?
  - id: list_proposals_v1_morph_spawn_v2_proposals_get
    intent: List spawn proposals
    question: Which spawn proposals are waiting for a decision?
  - id: promote_proposal_v1_morph_spawn_v2_promote_post
    intent: Approve and promote a spawn proposal
    question: How do I approve a spawn proposal so the agent goes live?
  - id: reject_proposal_v1_morph_spawn_v2_reject_post
    intent: Reject a spawn proposal
    question: How do I turn down a spawn proposal?
  - id: cap_status_v1_morph_spawn_v2_cap_get
    intent: Check the agent population cap
    question: How many free slots are left under the agent population cap?
  - id: proposal_stats_v1_morph_spawn_v2_stats_get
    intent: Get spawn proposal statistics
    question: How many spawn proposals have been promoted versus rejected?
  phrasing_ops: 6
  slug: thehiveryiq-com-spawn-garage-v2-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Sphere API from Hive Civilization — 1 operation(s) for sphere.
  name: Hive Civilization Sphere API
  phrasing_intents:
  - id: sphere_sphere_get
    intent: Open the agentic sphere view
    question: Where can I see the agentic sphere visualization?
  phrasing_ops: 1
  slug: thehiveryiq-com-sphere-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Status.json API from Hive Civilization — 1 operation(s) for status.json.
  name: Hive Civilization Status.json API
  phrasing_intents:
  - id: status_json_alias_status_json_get
    intent: Get status as status.json
    question: Is the status payload available at a .json URL?
  phrasing_ops: 1
  slug: thehiveryiq-com-status-json-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The storefront API from Hive Civilization — 3 operation(s) for storefront.
  name: Hive Civilization Storefront API
  phrasing_intents:
  - id: get_full_storefront_v1_storefront_get
    intent: Browse the full storefront catalog
    question: What supermodels and offerings are on the storefront?
  - id: search_storefront_v1_storefront_search_get
    intent: Search the storefront by capability or price
    question: Which storefront offerings fit my budget?
  - id: get_storefront_entry_v1_storefront__shape_or_id__get
    intent: Get one storefront entry by shape or ID
    question: How do I look up a single supermodel on the storefront?
  phrasing_ops: 3
  slug: thehiveryiq-com-storefront-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The stormlock API from Hive Civilization — 11 operation(s) for stormlock.
  name: Hive Civilization Stormlock API
  phrasing_intents:
  - id: health_v1_stormlock_health_get
    intent: Check StormLock service health
    question: Is the StormLock parametric insurance service up?
  - id: pricing_v1_stormlock_pricing_get
    intent: Get StormLock pricing
    question: How much does each StormLock attestation cost?
  - id: bind_attest_v1_stormlock_bind_attest_post
    intent: Record a parametric policy bind
    question: How do I record that a parametric catastrophe policy has been bound?
  - id: oracle_subscribe_v1_stormlock_oracle_subscribe_post
    intent: Register an oracle for a policy
    question: How do I attach a weather oracle to a parametric policy?
  - id: oracle_reading_attest_v1_stormlock_oracle_reading_attest_post
    intent: Record an oracle reading for a policy
    question: How do I log a wind speed reading from an oracle against a policy?
  - id: trigger_eval_attest_v1_stormlock_trigger_eval_attest_post
    intent: Evaluate a policy trigger against a reading
    question: Did this oracle reading breach the policy's parametric threshold?
  - id: loss_calc_attest_v1_stormlock_loss_calc_attest_post
    intent: Record a loss calculation and payout amount
    question: How do I record the calculated payout after a parametric trigger fires?
  - id: payout_auth_attest_v1_stormlock_payout_auth_attest_post
    intent: Record a payout authorization
    question: How do I record that a policy payout was authorized from treasury?
  phrasing_ops: 11
  slug: thehiveryiq-com-stormlock-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The subscription API from Hive Civilization — 5 operation(s) for subscription.
  name: Hive Civilization Subscription API
  phrasing_intents:
  - id: list_plans_v1_subscription_plans_get
    intent: List subscription plans
    question: What subscription plans are offered and what do they cost?
  - id: create_intent_v1_subscription_intent_post
    intent: Start a subscription and get payment instructions
    question: How do I sign up for the dev-pack or saas-pro plan?
  - id: claim_subscription_v1_subscription_claim_post
    intent: Claim a subscription with a payment tx hash
    question: How do I activate my subscription after paying on-chain?
  - id: subscription_status_v1_subscription_status__sub_id__get
    intent: Check a subscription's status
    question: How do I check whether my subscription has been provisioned?
  - id: health_v1_subscription_health_get
    intent: Check subscription service health
    question: Is the subscription service up?
  phrasing_ops: 5
  slug: thehiveryiq-com-subscription-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The swarm-receipts API from Hive Civilization — 8 operation(s) for swarm-receipts.
  name: Hive Civilization Swarm Receipts API
  phrasing_intents:
  - id: verify_receipt_route_v1_receipt_verify_post
    intent: Verify a signed receipt envelope
    question: How do I check that a post-quantum signed receipt envelope is valid?
  - id: health_v1_receipt_health_get
    intent: Check receipt service health
    question: Is the receipt issuing service up right now?
  - id: issue_free_receipt_v1_receipt_free_post
    intent: Sign any text as a free PQ receipt
    question: Can I get a free post-quantum signed receipt for a PR diff or log line without an account?
  - id: pq_status_v1_receipt_pq_status_get
    intent: Check whether the ML-DSA-65 signer is live
    question: Is the ML-DSA-65 post-quantum signer actually running on this host?
  - id: pricing_v1_receipt_pricing_get
    intent: Get receipt pricing
    question: What does it cost to issue receipts beyond the free tier?
  - id: issue_receipt_v1_receipt_issue_post
    intent: Issue a swarm receipt between two agents
    question: How do I issue a swarm-profile receipt for a transaction between two agent DIDs?
  - id: get_receipt_v1_receipt__receipt_id__get
    intent: Get a receipt by ID
    question: How do I fetch a receipt I issued earlier by its ID?
  - id: settle_receipt_v1_receipt_settle_post
    intent: Mark a receipt settled on-chain
    question: How do I attach a settlement transaction to an issued receipt?
  phrasing_ops: 8
  slug: thehiveryiq-com-swarm-receipts-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The tax API from Hive Civilization — 4 operation(s) for tax.
  name: Hive Civilization Tax API
  phrasing_intents:
  - id: post_tax_event_v1_tax_event_post
    intent: Classify one transaction for tax
    question: How would a single on-chain transaction be classified for tax purposes?
  - id: post_tax_bulk_v1_tax_bulk_post
    intent: Classify a batch of transactions for tax
    question: Can I tax-classify many transactions in one call?
  - id: get_tax_today_v1_tax_today_get
    intent: Count taxable events in the last 24 hours
    question: How many taxable events were seen in the past day, by type?
  - id: get_tax_health_v1_tax_health_get
    intent: Check the tax classifier's health
    question: Is the tax classification service up?
  phrasing_ops: 4
  slug: thehiveryiq-com-tax-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The topoff-router API from Hive Civilization — 4 operation(s) for topoff-router.
  name: Hive Civilization Topoff Router API
  phrasing_intents:
  - id: auto_topoff_all_v1_topoff_auto_post
    intent: Top off every low-balance supermodel
    question: How do I top off all hot supermodels that fell below their threshold?
  - id: auto_topoff_one_v1_topoff_auto__supermodel_id__post
    intent: Top off one supermodel
    question: Can I top off just one supermodel instead of all of them?
  - id: topoff_status_v1_topoff_status_get
    intent: View supermodel balance status
    question: What are the current balances of the hot supermodels?
  - id: topoff_history_v1_topoff_history_get
    intent: View top-off history
    question: What top-offs have been issued recently?
  phrasing_ops: 4
  slug: thehiveryiq-com-topoff-router-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The trade-finance API from Hive Civilization — 6 operation(s) for trade-finance.
  name: Hive Civilization Trade Finance API
  phrasing_intents:
  - id: post_invoice_v1_trade_invoice_post
    intent: Create a cross-border SMB trade invoice
    question: How do I invoice a cross-border supplier payment in USDT with a platform fee shown up front?
  - id: get_invoice_route_v1_trade_invoice__invoice_id__get
    intent: Get a trade invoice and its route
    question: What is the status and payment route of a specific trade invoice?
  - id: post_invoice_dispute_v1_trade_invoice__invoice_id__dispute_post
    intent: Open a dispute on a trade invoice
    question: Can I dispute a trade invoice if the goods or freight went wrong?
  - id: get_fees_v1_trade_fees_get
    intent: View the trade finance fee schedule
    question: What fees apply to cross-border trade invoices compared with a wire?
  - id: get_listing_v1_trade_listing_get
    intent: Get the trade finance agent listing
    question: What does the trade finance service's agent marketplace listing say?
  - id: get_invoices_v1_trade_invoices_get
    intent: List all trade invoices
    question: Which trade invoices are in the registry?
  phrasing_ops: 6
  slug: thehiveryiq-com-trade-finance-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The tradefinance API from Hive Civilization — 12 operation(s) for tradefinance.
  name: Hive Civilization Tradefinance API
  phrasing_intents:
  - id: list_tradefinance_v1_tradefinance_template_list_post
    intent: List trade finance contract templates
    question: Which trade finance contract templates are available to list?
  - id: get_agents_v1_tradefinance_agents_get
    intent: List the trade finance agents
    question: Which agents take part in a trade finance contract?
  - id: get_template_v1_tradefinance_template_get
    intent: Get the trade finance contract template
    question: What fields does a trade finance contract need?
  - id: post_contract_v1_tradefinance_contract_post
    intent: Create a trade finance contract
    question: How do I set up a trade finance contract between an importer and an exporter?
  - id: get_contract_detail_v1_tradefinance_contract__contract_id__get
    intent: Get a trade finance contract
    question: What are the terms and parties of a trade contract I already created?
  - id: post_fund_v1_tradefinance_fund_post
    intent: Fund a trade finance contract
    question: How do I put money into escrow for a trade contract?
  - id: post_milestone_v1_tradefinance_milestone_tick_post
    intent: Mark a shipment milestone on a contract
    question: How do I record that a shipment reached a milestone on a trade contract?
  - id: get_escrow_detail_v1_tradefinance_escrow__contract_id__get
    intent: Check a contract's escrow
    question: How much is held in escrow for my trade contract, and has it settled?
  phrasing_ops: 12
  slug: thehiveryiq-com-tradefinance-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Tradeguard API from Hive Civilization — 10 operation(s) for tradeguard.
  name: Hive Civilization Tradeguard API
  phrasing_intents:
  - id: tradeguard_mcp_meta_v1_tradeguard_mcp_get
    intent: Describe the TradeGuard MCP server
    question: Does TradeGuard expose an MCP server, and what does it describe?
  - id: tradeguard_mcp_v1_tradeguard_mcp_post
    intent: Call the TradeGuard MCP server
    question: Can I send MCP JSON-RPC requests to TradeGuard from my agent?
  - id: health_v1_tradeguard_health_get
    intent: Check TradeGuard health
    question: Is the TradeGuard trade attestation service healthy?
  - id: pricing_v1_tradeguard_pricing_get
    intent: Get TradeGuard pricing
    question: What does TradeGuard charge to attest a trade?
  - id: attest_trade_v1_tradeguard_attest_post
    intent: Attest an order event for audit
    question: How do I create a signed attestation for an algorithmic order event?
  - id: verify_attestation_v1_tradeguard_verify__attestation_id__get
    intent: Verify a trade attestation
    question: Can I confirm a TradeGuard attestation is valid given its ID?
  - id: by_event_hash_v1_tradeguard_by_event_hash__order_event_hash__get
    intent: Find an attestation by order event hash
    question: Which attestation covers a particular order event hash?
  - id: by_trader_v1_tradeguard_by_trader__trader_did__get
    intent: List attestations for a trader
    question: What trades has a given trader had attested?
  phrasing_ops: 11
  slug: thehiveryiq-com-tradeguard-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The traffic API from Hive Civilization — 4 operation(s) for traffic.
  name: Hive Civilization Traffic API
  phrasing_intents:
  - id: traffic_stats_multi_v1_traffic_stats_get
    intent: Get traffic stats across standard windows
    question: How much traffic has the service seen over the last hour, day and week?
  - id: traffic_stats_single_v1_traffic_stats__hours__get
    intent: Get traffic stats for a custom window
    question: What does traffic look like over a specific number of hours?
  - id: traffic_recent_v1_traffic_recent_get
    intent: List paths hit in the last hour
    question: Which paths have been requested in the past hour?
  - id: traffic_campaign_v1_traffic_campaign_get
    intent: Measure traffic to campaign surfaces
    question: Did my latest post drive traffic to the surfaces we are promoting?
  phrasing_ops: 4
  slug: thehiveryiq-com-traffic-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The trail API from Hive Civilization — 15 operation(s) for trail.
  name: Hive Civilization Trail API
  phrasing_intents:
  - id: get_presets_v1_trail_presets_get
    intent: List trail presets and their physics regions
    question: Which named trail presets exist and what are their default physics regions?
  - id: post_drop_v1_trail_drop_post
    intent: Drop an artifact on the trail
    question: How does an agent leave an artifact on the trail for others to find?
  - id: get_find_v1_trail_find_get
    intent: Search the trail for dropped artifacts
    question: How do I find artifacts other agents dropped in a given vertical?
  - id: post_scoop_v1_trail__drop_id__scoop_post
    intent: Scoop up a dropped artifact
    question: How does a finder agent pick up a drop it found on the trail?
  - id: post_pay_v1_trail__drop_id__pay_post
    intent: Pay or tip the dropper of an artifact
    question: How do I pay the agent who dropped an artifact I found useful?
  - id: post_dispute_v1_trail__drop_id__dispute_post
    intent: Dispute a trail drop
    question: What can I do if a trail drop turns out to be bad or misleading?
  - id: post_decay_run_v1_trail_decay_run_post
    intent: Run the trail decay pass
    question: How do I trigger decay so stale trail drops age out?
  - id: get_morphology_v1_trail_morphology_get
    intent: View the trail morphology for a vertical
    question: What shape is the trail taking in a given vertical?
  phrasing_ops: 15
  slug: thehiveryiq-com-trail-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The trust API from Hive Civilization — 4 operation(s) for trust.
  name: Hive Civilization Trust API
  phrasing_intents:
  - id: health_v1_trust_health_get
    intent: Check trust service health and record count
    question: Is the trust benchmark service up, and how many records does it hold?
  - id: benchmarks_v1_trust_benchmarks_get
    intent: List signed benchmark records
    question: Which benchmark results have been published for each primitive?
  - id: benchmark_v1_trust_benchmarks__record_id__get
    intent: Get one signed benchmark record
    question: How do I fetch a single signed benchmark record?
  - id: agents_v1_trust_agents_get
    intent: Browse the public agent trust directory
    question: Which agents have the highest composite trust scores?
  phrasing_ops: 4
  slug: thehiveryiq-com-trust-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The Trust.json API from Hive Civilization — 1 operation(s) for trust.json.
  name: Hive Civilization Trust.json API
  phrasing_intents:
  - id: trust_json_trust_json_get
    intent: Get the public trust posture document
    question: What signing keys and algorithms does Hive use?
  phrasing_ops: 1
  slug: thehiveryiq-com-trust-json-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The vault-visits API from Hive Civilization — 9 operation(s) for vault-visits.
  name: Hive Civilization Vault Visits API
  phrasing_intents:
  - id: vault_visit_v1_vault_visit_post
    intent: Record a vault page visit beacon
    question: How do I log that someone opened a vault page, with dwell time and scroll depth?
  - id: visits_recent_v1_vault_visits_recent_get
    intent: List the most recent vault visits
    question: Who has opened any of my vault pages most recently?
  - id: visits_by_slug_v1_vault_visits_by_slug_get
    intent: Get visit history for one vault
    question: Every visit to one specific vault, newest first — where do I get that?
  - id: visits_by_company_v1_vault_visits_by_company_get
    intent: Summarize visits across all vaults
    question: What does an at-a-glance summary of every tracked vault look like, one row each?
  - id: visits_health_v1_vault_visits_health_get
    intent: Check the vault visit tracker's health
    question: Is the vault visit tracking service healthy?
  - id: visits_leaderboard_v1_vault_visits_leaderboard_get
    intent: Rank vaults by engagement
    question: Which vaults are getting the most engagement from unique viewers and re-opens?
  - id: visits_forwards_v1_vault_visits_forwards_get
    intent: Find vaults forwarded to new viewers
    question: Has any prospect forwarded a vault to a colleague?
  - id: register_label_v1_vault_visits_register_label_post
    intent: Attach a human label to a vault slug
    question: Can I name a new vault slug without redeploying?
  phrasing_ops: 9
  slug: thehiveryiq-com-vault-visits-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The verify API from Hive Civilization — 2 operation(s) for verify.
  name: Hive Civilization Verify API
  phrasing_intents:
  - id: attest_v1_xcalibur_verify_v2_attest_post
    intent: Attest a data chunk belongs to a signed corpus
    question: How do I prove a data chunk is part of a corpus with a given Merkle root?
  - id: health_v1_xcalibur_verify_v2_health_get
    intent: Check VERIFY v2 service health
    question: Is the corpus attestation service up?
  phrasing_ops: 2
  slug: thehiveryiq-com-verify-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The .well Known API from Hive Civilization — 5 operation(s) for .well known.
  name: Hive Civilization .well Known API
  phrasing_intents:
  - id: well_known_agent_json__well_known_agent_json_get
    intent: Fetch the lean agent.json discovery manifest
    question: Does HiveMorph publish a well-known agent.json for crawlers that look there?
  - id: well_known_x402__well_known_x402_json_get
    intent: Fetch the x402.json payment directory entry
    question: Which x402 payment rails are listed in the well-known x402.json?
  - id: well_known_x402_alias__well_known_x402_get
    intent: Fetch x402 details at the extensionless path
    question: Is x402 discovery also served at /.well-known/x402 without the .json extension?
  - id: well_known_did_json__well_known_did_json_get
    intent: Resolve the Hive DID document
    question: What is the Ed25519 signing key in did:hive:hivemorph's DID document?
  - id: well_known_mcp_json__well_known_mcp_json_get
    intent: Fetch the MCP server descriptor
    question: What MCP tools does HiveMorph expose and at which transport endpoint?
  phrasing_ops: 5
  slug: thehiveryiq-com-well-known-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The X402 API from Hive Civilization — 18 operation(s) for x402.
  name: Hive Civilization X402 API
  phrasing_intents:
  - id: x402_facilitator_metadata_v1_x402_get
    intent: Get x402 facilitator metadata
    question: Which settlement schemes and chain/asset combinations does the HiveMorph x402 facilitator support?
  - id: get_pricing_v1_x402_pricing_get
    intent: View the x402 per-call pricing table
    question: How much does each monetized endpoint cost per call in USD?
  - id: get_stats_v1_x402_stats_get
    intent: Get x402 call and revenue statistics
    question: How many 402 payment challenges have been issued and how many calls were actually paid?
  - id: get_stats_buckets_v1_x402_stats_buckets_get
    intent: Get endpoint stats grouped into buckets
    question: Can I see call counters rolled up by category like Receipts, Compliance and Energy?
  - id: submit_proof_v1_x402_proof_submit_post
    intent: Submit an on-chain payment proof for a 402
    question: How do I turn a paid 402 nonce into an access token for the X-Hive-Access header?
  - id: verify_token_v1_x402_proof_verify_get
    intent: Check whether an x402 access token is valid
    question: Is my x402 access token still valid or has its 5-minute window expired?
  - id: set_pricing_v1_x402_pricing_set_post
    intent: Set the price for an endpoint (admin)
    question: As an admin, can I change the per-call price of a specific path?
  - id: get_rails_v1_x402_rails_get
    intent: List accepted x402 settlement rails
    question: Which chain and asset rails are accepted for x402 settlement?
  phrasing_ops: 20
  slug: thehiveryiq-com-x402-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur API from Hive Civilization — 6 operation(s) for xcalibur.
  name: Hive Civilization Xcalibur API
  phrasing_intents:
  - id: compress_v1_xcalibur_echo_v2_compress_post
    intent: Compress a prompt with ECHO v2
    question: Can I shrink a long prompt while keeping what matters for my task?
  - id: health_v1_xcalibur_echo_v2_health_get
    intent: Check ECHO v2 compressor health
    question: Is the ECHO v2 prompt compressor up?
  - id: classify_v1_xcalibur_membrane_v2_classify_post
    intent: Classify text as safe or unsafe
    question: How do I check whether a piece of text is a prompt injection or otherwise unsafe?
  - id: health_v1_xcalibur_membrane_v2_health_get
    intent: Check MEMBRANE v2 classifier health
    question: Is the MEMBRANE safety classifier available?
  - id: attest_v1_xcalibur_verify_v2_attest_post
    intent: Attest a data chunk belongs to a signed corpus
    question: How do I prove a chunk is in a corpus and was signed by a specific post-quantum key?
  - id: health_v1_xcalibur_verify_v2_health_get
    intent: Check VERIFY v2 attestation health
    question: Is the VERIFY v2 corpus attestation endpoint up?
  phrasing_ops: 6
  slug: thehiveryiq-com-xcalibur-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur-echo API from Hive Civilization — 3 operation(s) for xcalibur-echo.
  name: Hive Civilization Xcalibur Echo API
  phrasing_intents:
  - id: compress_prompt_v1_xcalibur_echo_compress_post
    intent: Compress a prompt with a signed receipt
    question: Can I shrink a long prompt to a target length while keeping most of its content?
  - id: verify_receipt_v1_xcalibur_echo_verify_post
    intent: Verify a prompt compression receipt
    question: Is a compression receipt's signature and token math correct?
  - id: echo_health_v1_xcalibur_echo_health_get
    intent: Check the ECHO compressor's health
    question: Is the XCALIBUR ECHO prompt compressor up?
  phrasing_ops: 3
  slug: thehiveryiq-com-xcalibur-echo-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur-membrane API from Hive Civilization — 5 operation(s) for xcalibur-membrane.
  name: Hive Civilization Xcalibur Membrane API
  phrasing_intents:
  - id: health_v1_xcalibur_membrane_health_get
    intent: Check MEMBRANE service liveness
    question: Is the MEMBRANE output-leak scorer alive?
  - id: score_v1_xcalibur_membrane_score_post
    intent: Score an LLM output for sensitive-data leakage
    question: How can I tell whether a model's output leaked sensitive parts of the prompt?
  - id: verify_v1_xcalibur_membrane_verify_post
    intent: Verify a MEMBRANE scoring receipt
    question: Is this MEMBRANE receipt's signature valid and its decision consistent with the thresholds?
  - id: enforce_v1_xcalibur_membrane_enforce_post
    intent: Gate an LLM output, blocking it if it leaks
    question: Can I automatically block a model response that leaks sensitive prompt content?
  - id: canary_eval_v1_xcalibur_membrane_canary_eval_get
    intent: Run the adversarial canary leak benchmark
    question: How good is MEMBRANE at catching leaks versus passing clean outputs?
  phrasing_ops: 5
  slug: thehiveryiq-com-xcalibur-membrane-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur-quorum API from Hive Civilization — 4 operation(s) for xcalibur-quorum.
  name: Hive Civilization Xcalibur Quorum API
  phrasing_intents:
  - id: quorum_complete_v1_xcalibur_quorum_complete_post
    intent: Get an M-of-N consensus answer from several LLMs
    question: How do I send one prompt to several models and only accept an answer most of them agree on?
  - id: quorum_verify_v1_xcalibur_quorum_verify_post
    intent: Verify a QUORUM receipt signature
    question: How can I confirm a consensus receipt was really signed by the quorum service?
  - id: quorum_health_v1_xcalibur_quorum_health_get
    intent: Check QUORUM liveness and available models
    question: Is the QUORUM consensus service alive, and which model IDs can it call?
  - id: quorum_registry_v1_xcalibur_quorum_registry_get
    intent: Get the QUORUM model registry
    question: Which model families and eras can participate in quorum votes?
  phrasing_ops: 4
  slug: thehiveryiq-com-xcalibur-quorum-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur-quorum-v2 API from Hive Civilization — 2 operation(s) for xcalibur-quorum-v2.
  name: Hive Civilization Xcalibur Quorum V2 API
  phrasing_intents:
  - id: quorum_v2_reason_v1_xcalibur_quorum_v2_reason_post
    intent: Solve a problem with ensemble reasoning
    question: Can I run a hard reasoning problem through several strategies and take the most agreed answer?
  - id: quorum_v2_health_v1_xcalibur_quorum_v2_health_get
    intent: Check QUORUM v2 liveness
    question: Is QUORUM v2 alive, and what version is it?
  phrasing_ops: 2
  slug: thehiveryiq-com-xcalibur-quorum-v2-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The xcalibur-verify API from Hive Civilization — 7 operation(s) for xcalibur-verify.
  name: Hive Civilization Xcalibur Verify API
  phrasing_intents:
  - id: verify_status_v1_verify_status_get
    intent: Check XCALIBUR Verify service status
    question: Is the XCALIBUR Verify proof service up?
  - id: commitment_build_v1_verify_commitment_build_post
    intent: Build a corpus commitment for a tenant
    question: How do I build a new Merkle commitment over a tenant's corpus?
  - id: commitment_current_v1_verify_commitment__tenant_id__current_get
    intent: Get a tenant's current commitment
    question: What is the current commitment root for a tenant?
  - id: proof_generate_v1_verify_proof_generate_post
    intent: Generate an inclusion proof for a corpus entry
    question: How do I generate a proof that an entry is in a tenant's committed corpus?
  - id: proof_verify_v1_verify_proof_verify_post
    intent: Verify an inclusion proof against a commitment
    question: How do I check that a proof matches a commitment?
  - id: dispute_v1_verify_dispute_post
    intent: Dispute a verification certificate
    question: How do I file a dispute against a certificate I think is wrong?
  - id: demo_run_v1_verify_demo_run_post
    intent: Run the end-to-end verification demo
    question: Can I try the whole proof-and-certificate pipeline on the seeded demo corpus?
  phrasing_ops: 7
  slug: thehiveryiq-com-xcalibur-verify-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The yield-optimizer API from Hive Civilization — 1 operation(s) for yield-optimizer.
  name: Hive Civilization Yield Optimizer API
  phrasing_intents:
  - id: get_yield_optimize_v1_yield_optimize_get
    intent: Recommend prices to maximize daily revenue
    question: What price and volume settings would maximize revenue per day based on past offers?
  phrasing_ops: 1
  slug: thehiveryiq-com-yield-optimizer-api
- baseURL: https://receipts.thehiveryiq.com
  baseurl_source: declared
  description: The zozo-identity API from Hive Civilization — 1 operation(s) for zozo-identity.
  name: Hive Civilization Zozo Identity API
  phrasing_intents:
  - id: zozo_identity_v1_identity_zozo_get
    intent: Get the Zozo agent identity
    question: What identity does the Zozo agent publish?
  phrasing_ops: 1
  slug: thehiveryiq-com-zozo-identity-api
artifact_total: 168
asyncapis:
- description: ''
  name: Thehiveryiq Com Webhooks
  slug: thehiveryiq-com-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://thehiveryiq.com/feed.xml
- group: other
  href: https://artifacts.apis.io/thehiveryiq-com/capabilities/thehiveryiq-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/thehiveryiq-com-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/thehiveryiq-com/overlays/thehiveryiq-com-hivecompute-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thehiveryiq-com-hivecompute-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.thehiveryiq.com/mcp
- group: company
  title: ''
  type: Website
  url: https://thehiveryiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thehiveryiq.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://thehiveryiq.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://receipts.thehiveryiq.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://thehiveryiq.com/agents
- group: operate
  title: ''
  type: Support
  url: https://thehiveryiq.com/company
- group: other
  title: ''
  type: Leadership
  url: https://thehiveryiq.com/company
- group: company
  title: ''
  type: Blog
  url: https://thehiveryiq.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/srotzin
- group: operate
  title: ''
  type: Roadmap
  url: https://thehiveryiq.com/rails
- group: commercial
  title: ''
  type: Pricing
  url: https://thehiveryiq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://thehiveryiq.com/onboard/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thehiveryiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thehiveryiq.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://thehiveryiq.com/status/
- group: docs
  title: ''
  type: Specifications
  url: https://thehiveryiq.com/specs/did-hive/v1/
- group: other
  href: https://artifacts.apis.io/thehiveryiq-com/a2a/thehiveryiq-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/thehiveryiq-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/thehiveryiq-com/mcp/thehiveryiq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thehiveryiq-com-mcp.yml
- group: build
  href: https://artifacts.apis.io/thehiveryiq-com/mcp/thehiveryiq-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thehiveryiq-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/thehiveryiq-com/llms/thehiveryiq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thehiveryiq-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://thehiveryiq.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/thehiveryiq-com/well-known/thehiveryiq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thehiveryiq-com-well-known.yml
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/well-known/thehiveryiq-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thehiveryiq-com-security.txt
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/security/thehiveryiq-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/thehiveryiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/security/thehiveryiq-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thehiveryiq-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/security/thehiveryiq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thehiveryiq-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/security/thehiveryiq-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/thehiveryiq-com-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://thehiveryiq.com/compliance/
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/conformance/thehiveryiq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thehiveryiq-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/lifecycle/thehiveryiq-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thehiveryiq-com-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/thehiveryiq-com/changelog/thehiveryiq-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thehiveryiq-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/thehiveryiq-com/authentication/thehiveryiq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thehiveryiq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/conventions/thehiveryiq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thehiveryiq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/conventions/thehiveryiq-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/thehiveryiq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/errors/thehiveryiq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thehiveryiq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/data-model/thehiveryiq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thehiveryiq-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/thehiveryiq-com/rate-limits/thehiveryiq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thehiveryiq-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thehiveryiq-com/plans/thehiveryiq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thehiveryiq-com-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/thehiveryiq-com/packages/thehiveryiq-com-packages.yml
  title: ''
  type: Packages
  url: packages/thehiveryiq-com-packages.yml
- group: build
  href: https://artifacts.apis.io/thehiveryiq-com/packages/thehiveryiq-com-packages.yml
  title: ''
  type: SDKs
  url: packages/thehiveryiq-com-packages.yml
- group: start
  href: https://artifacts.apis.io/thehiveryiq-com/sandbox/thehiveryiq-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thehiveryiq-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/thehiveryiq-com/asyncapi/thehiveryiq-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thehiveryiq-com-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/thehiveryiq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/thehiveryiq-com/overlays/thehiveryiq-com-hivemorph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/thehiveryiq-com-hivemorph-overlay.yaml
- group: other
  title: ''
  type: Subprocessors
  url: https://thehiveryiq.com/security/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://thehiveryiq.com/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://thehiveryiq.com/security/
created: '2026-09-19'
description: 'Hive Civilization (DBAs The Hivery and The Hivery IQ; Walnut Creek, California; single-founder Wyoming corporation established 2026) sells signed, independently verifiable receipts for automated and AI-agent actions: every call returns a dual-signed record (Ed25519 plus ML-DSA-65) over an artifact hash, priced per receipt and settled per call in USDC on Base through the x402 payment protocol, with no account required for the free tier. The public surface is spread over four hosts: receipts.thehiveryiq.com serves the HiveMorph receipts and agent-commerce API (a 906-path, 937-operation FastAPI OpenAPI 3.1 contract covering receipt emit/verify, x402 quotes and settlement references, delegations and a firewall, HKTN trust lookups, plus dozens of vertical attestation families), a JSON-RPC 2.0 agent endpoint and A2A agent cards; api.thehiveryiq.com serves HiveCompute, an OpenAI-compatible, x402-metered inference router with a live remote MCP server; passport.thehiveryiq.com is the
  HKTN trust rail; and hive-mcp-gateway.onrender.com fronts 37 hive-mcp-* MCP servers. The apex publishes an A2A agent card, security.txt, llms.txt, pricing, a self-attested (uncertified) SOC 2 / ISO 27001 posture and a did:hive DID method specification.'
finops:
- has_sources: true
  method: derived
  name: Thehiveryiq Com Finops
  primary_unit: receipts
  service_category: ''
  slug: thehiveryiq-com-finops
  template: false
image: https://thehiveryiq.com/assets/brand/hive-mark-512.png
layout: provider
mcp_servers:
- description: 'Hive Civilization operates remote MCP servers on at least three surfaces. (1) https://api.thehiveryiq.com/mcp, the HiveCompute inference router on the provider''s own domain: initialize and tools/list '
  name: Hive Civilization MCP Server
  slug: thehiveryiq-com-mcp-yml
- description: ''
  name: Hive Civilization MCP Server
  slug: mcp
modified: '2026-10-06'
name: Hive Civilization
nav: Providers
network: true
overview: 'Hive Civilization publishes 153 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, Activation API, Aegis API, and 150 more. Tagged areas include Agents, Agentic Commerce, A2A, MCP, and x402.


  The Hive Civilization catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hive Civilization''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Thehiveryiq Com Plans Pricing
  plan_count: 20
  slug: thehiveryiq-com-plans-pricing
- name: Thehiveryiq Com Price Estimates
  plan_count: 0
  slug: thehiveryiq-com-price-estimates
random_paper: 6
rate_limits:
- limit_count: 4
  name: Thehiveryiq Com Rate Limits
  slug: thehiveryiq-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Hive Civilization API Rules
  rule_count: 50
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 17
  slug: thehiveryiq-com-rules
score:
  band: exemplar
  composite: 66.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 71.5
    catalog_earned_first_party: 24.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 73.7
    contract_governance: 31.8
    contract_quality: 51.7
    developer_ergonomics: 50.6
    discoverability: 80.8
    operational_transparency: 78.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 77.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.7
      derived: 0
      marker_coverage: 100.0
      total: 150
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/thehiveryiq-com/thehiveryiq-com-2026-10-11T130845.png
security:
- kind: authentication
  name: Thehiveryiq Com Authentication
  slug: thehiveryiq-com-authentication
  summary_line: none/x402-payment/apiKey/ed25519-signed-request · 6 schemes
- kind: domain-security
  name: Thehiveryiq Com Domain Security
  slug: thehiveryiq-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Thehiveryiq Com Vulnerability Disclosure
  slug: thehiveryiq-com-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thehiveryiq Com Trust Center
  slug: thehiveryiq-com-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: thehiveryiq-com-delegation-and-firewall-gate
  slug: thehiveryiq-com-delegation-and-firewall-gate
- name: thehiveryiq-com-free-receipt-sign-and-verify
  slug: thehiveryiq-com-free-receipt-sign-and-verify
- name: thehiveryiq-com-paid-receipt-x402
  slug: thehiveryiq-com-paid-receipt-x402
slug: thehiveryiq-com
tags:
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Receipts
- Digital Signature
- Post-Quantum Cryptography
- Attestation
- Decentralized Identity
- Stablecoins
- Inference
- LLM Routing
- Compliance
- Agent-Native
- United States
website: https://thehiveryiq.com/
---
