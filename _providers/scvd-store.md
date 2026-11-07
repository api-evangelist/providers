---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Scvd Store Agentic Access
  operation_count: 196
  slug: scvd-store-agentic-access
  summary_line: 196 operations · 34 acting
api_count: 1
apis:
- description: Three remote Model Context Protocol servers on the apex host, all Streamable HTTP and all answering initialize, tools/list and resources/list anonymously at protocol version 2025-06-18 (serverInfo 0.5
  name: SCVD General Store MCP Servers
  slug: scvd-mcp-servers
- description: 'Agent2Agent protocol surface: an agent card served from https://scvd.store/.well-known/agent-card.json (and byte-identically at /.well-known/agent.json and /.well-known/a2a.json; protocolVersion 0.3.0'
  name: SCVD Evidence Agent (A2A)
  slug: scvd-evidence-agent
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The A2a API from SCVD General Store — 4 operation(s) for a2a.
  name: SCVD General Store A2a API
  phrasing_intents:
  - id: get_api_a2a_check
    intent: Read the free A2A check's instructions
    question: What are the limits of the free A2A card check?
  - id: post_api_a2a_check
    intent: Run a free A2A 0.3.0 card check
    question: Is my A2A agent card valid against 0.3.0?
  - id: get_api_a2a_runner_mjs
    intent: Download the A2A regression runner
    question: Where can I download the Node regression runner for my A2A agent?
  - id: get_api_a2a_kits_kit_id
    intent: Read an A2A repair kit
    question: What does my A2A repair kit say, and what is left of its card watch?
  - id: post_api_a2a_kits_kit_id_recheck
    intent: Use an A2A repair kit's included recheck
    question: How do I use the one recheck included with my A2A repair kit?
  phrasing_ops: 5
  slug: scvd-store-a2a-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The A2a Desk.json API from SCVD General Store — 1 operation(s) for a2a desk.json.
  name: SCVD General Store A2a Desk.json API
  phrasing_intents:
  - id: get_a2a_desk_json
    intent: Read the A2A repair desk contract and prices
    question: What does the A2A repair desk cost and what are its limits?
  phrasing_ops: 1
  slug: scvd-store-a2a-desk-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Almanac API from SCVD General Store — 3 operation(s) for almanac.
  name: SCVD General Store Almanac API
  phrasing_intents:
  - id: get_almanac
    intent: List the keeper's almanac pages
    question: Which almanac journal pages has the keeper written?
  - id: get_almanac_notes_from_a_tuesday_in_oak_city
    intent: Buy the Notes from a Tuesday in Oak City page
    question: Can I read Notes from a Tuesday in Oak City?
  - id: get_almanac_slug
    intent: Read an almanac page by its slug
    question: How do I read a specific current almanac page?
  phrasing_ops: 3
  slug: scvd-store-almanac-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Anchor API from SCVD General Store — 1 operation(s) for anchor.
  name: SCVD General Store Anchor API
  phrasing_intents:
  - id: get_api_anchor_anchor_id
    intent: Read back a stored context anchor
    question: How does my agent read back a memory it stored last session?
  phrasing_ops: 1
  slug: scvd-store-anchor-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Ask API from SCVD General Store — 2 operation(s) for ask.
  name: SCVD General Store Ask API
  phrasing_intents:
  - id: get_ask
    intent: Ask the store a question about itself
    question: Can I ask the store in plain words which item or instrument fits my need?
  - id: post_ask
    intent: Ask the store a question with a JSON body
    question: Can I send my question to the store as a JSON body instead of a query string?
  - id: get_ask_feed_json
    intent: Read the full askable index feed
    question: What entries can the ask endpoint return, in ranked order?
  phrasing_ops: 3
  slug: scvd-store-ask-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Attestation API from SCVD General Store — 1 operation(s) for attestation.
  name: SCVD General Store Attestation API
  phrasing_intents:
  - id: get_attestation
    intent: Read what the store signs and what it proves
    question: What does each of the store's signatures cover, and what doesn't it prove?
  phrasing_ops: 1
  slug: scvd-store-attestation-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Auth.md API from SCVD General Store — 1 operation(s) for auth.md.
  name: SCVD General Store Auth.md API
  phrasing_intents:
  - id: get_auth_md
    intent: Read how an agent authenticates here
    question: Does this store need an API key, account or OAuth?
  phrasing_ops: 1
  slug: scvd-store-auth-md-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Before You Pay API from SCVD General Store — 1 operation(s) for before you pay.
  name: SCVD General Store Before You Pay API
  phrasing_intents:
  - id: get_api_before_you_pay_v1
    intent: Read how the payment dry run works
    question: What does the before-you-pay dry run tell me, and what can't it?
  - id: post_api_before_you_pay_v1
    intent: Dry-run whether my client will pay an x402 door
    question: Will my x402 client pay this door, and which accept would it sign?
  phrasing_ops: 2
  slug: scvd-store-before-you-pay-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Bell API from SCVD General Store — 2 operation(s) for bell.
  name: SCVD General Store Bell API
  phrasing_intents:
  - id: get_bell
    intent: Open the bell page in a browser
    question: Where is the bell page a person can visit?
  - id: post_bell
    intent: Ring the bell from the browser form
    question: Can I ring the bell from a web form and see my card?
  - id: post_api_bell
    intent: Ring the bell as an agent
    question: How often can an agent ring the store's bell through the API?
  phrasing_ops: 3
  slug: scvd-store-bell-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Bitcoin Anchor API from SCVD General Store — 1 operation(s) for bitcoin anchor.
  name: SCVD General Store Bitcoin Anchor API
  phrasing_intents:
  - id: get_api_bitcoin_anchor_anchor_id
    intent: Check a Bitcoin anchor's proof status
    question: Has my digest been committed into Bitcoin yet?
  phrasing_ops: 1
  slug: scvd-store-bitcoin-anchor-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Bot Auth API from SCVD General Store — 1 operation(s) for bot auth.
  name: SCVD General Store Bot Auth API
  phrasing_intents:
  - id: post_api_bot_auth_check
    intent: Check a Web Bot Auth key directory for free
    question: Is my Web Bot Auth key directory valid?
  phrasing_ops: 1
  slug: scvd-store-bot-auth-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Bot Auth Card API from SCVD General Store — 1 operation(s) for bot auth card.
  name: SCVD General Store Bot Auth Card API
  phrasing_intents:
  - id: get_api_bot_auth_card_card_id
    intent: Read a purchased signature-agent card
    question: Where is the signed card my signature-agent purchase produced?
  phrasing_ops: 1
  slug: scvd-store-bot-auth-card-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Bounties API from SCVD General Store — 2 operation(s) for bounties.
  name: SCVD General Store Bounties API
  phrasing_intents:
  - id: get_bounties
    intent: Open the Bounty Board page
    question: Where is the crawlable Bounty Board page with the rules in full?
  - id: get_api_bounties
    intent: Poll the open mystery-shopping bounties
    question: Which mystery-shopping bounties are open right now?
  - id: post_api_bounties
    intent: Claim a mystery-shopping bounty
    question: How do I claim a bounty after paying the listed door?
  phrasing_ops: 3
  slug: scvd-store-bounties-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Buy API from SCVD General Store — 35 operation(s) for buy.
  name: SCVD General Store Buy API
  phrasing_intents:
  - id: get_api_buy_spot_check
    intent: Look up what is on record about an x402 host
    question: What does the observatory already know about an x402 host before I pay it?
  - id: get_api_buy_settlement_attestation
    intent: Attest that one x402 payment settled on chain
    question: How can I prove to a third party that a single x402 payment actually settled?
  - id: get_api_buy_small_blessing
    intent: Buy a half-cent blessing to test a real payment
    question: What is the cheapest real x402 purchase I can make to test my wallet?
  - id: get_api_buy_settlement_reconciliation
    intent: Reconcile a payment against its authorized ceiling
    question: Did my agent's payment move more USDC than it was authorized to?
  - id: get_api_buy_daily_fortune
    intent: Buy today's fortune
    question: What is today's fortune at the store?
  - id: get_api_buy_the_confession
    intent: Make an anonymous confession to the store
    question: Where can my agent confess a phantom success anonymously?
  - id: get_api_buy_attestation_bundle
    intent: Attest up to 20 payments in one purchase
    question: Can I get settlement attestations for a whole batch of transactions at once?
  - id: get_api_buy_the_mandate
    intent: Record an agent's spending mandate with a third party
    question: How do I record what my agent is authorized to spend before it pays anything?
  phrasing_ops: 35
  slug: scvd-store-buy-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Card API from SCVD General Store — 1 operation(s) for card.
  name: SCVD General Store Card API
  phrasing_intents:
  - id: get_api_card_card_id
    intent: Read a trading card's signed record
    question: What is the signed record behind a trading card I pulled?
  phrasing_ops: 1
  slug: scvd-store-card-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Case API from SCVD General Store — 1 operation(s) for case.
  name: SCVD General Store Case API
  phrasing_intents:
  - id: get_case_case_id
    intent: Read a purchased case file
    question: What did the store observe about the purchase in my case file?
  phrasing_ops: 1
  slug: scvd-store-case-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Catalog API from SCVD General Store — 1 operation(s) for catalog.
  name: SCVD General Store Catalog API
  phrasing_intents:
  - id: get_api_catalog_v1
    intent: Search the shelf or read one item
    question: Which store items cost under a given USDC price?
  phrasing_ops: 1
  slug: scvd-store-catalog-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Claims API from SCVD General Store — 2 operation(s) for claims.
  name: SCVD General Store Claims API
  phrasing_intents:
  - id: post_api_claims_challenge
    intent: Start a purchase-recovery claim
    question: My agent's context reset after paying — how do I start recovering the purchase?
  - id: get_api_claims
    intent: Read how purchase recovery works
    question: How does the store's purchase-recovery door work?
  - id: post_api_claims
    intent: Recover what a wallet paid for
    question: Can I recover everything my wallet bought after losing the response?
  phrasing_ops: 3
  slug: scvd-store-claims-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Conformance API from SCVD General Store — 2 operation(s) for conformance.
  name: SCVD General Store Conformance API
  phrasing_intents:
  - id: get_api_conformance_v1_fixtures
    intent: Get signed envelope test fixtures
    question: Are there valid, expired and tampered signed fixtures I can test my integration against?
  - id: get_api_conformance_v1
    intent: Read how the conformance desk works
    question: What request shape does the free conformance desk take?
  - id: post_api_conformance_v1
    intent: Check an x402 signed offer or receipt
    question: Is this issuer's x402 signed offer or receipt valid?
  phrasing_ops: 3
  slug: scvd-store-conformance-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Conformance Watch API from SCVD General Store — 1 operation(s) for conformance watch.
  name: SCVD General Store Conformance Watch API
  phrasing_intents:
  - id: get_api_conformance_watch_watch_id
    intent: Read a conformance watch's daily record
    question: What did my conformance watch find each day?
  phrasing_ops: 1
  slug: scvd-store-conformance-watch-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Corpus API from SCVD General Store — 9 operation(s) for corpus.
  name: SCVD General Store Corpus API
  phrasing_intents:
  - id: get_corpus_index_json
    intent: Page through the compact corpus index
    question: Can I page through snapshot metadata without downloading every snapshot body?
  - id: get_corpus_host_host_json
    intent: Read one host's recorded corpus history
    question: What history has the corpus recorded for one x402 host?
  - id: get_corpus_sequence_evidence_host_json
    intent: Read the raw evidence capture behind a sealed row
    question: Where is the raw probe capture that a sealed row's evidence digest commits to?
  - id: get_corpus_asked_json
    intent: See hosts people asked about that were never probed
    question: Which hosts have people asked about that the signed chain never probed?
  - id: get_corpus_tiers_json
    intent: List every host's passport tier
    question: What passport tier does each host carry, and from what fraction of rounds?
  - id: get_corpus_trajectory_json
    intent: Read the corpus as a time series
    question: How have x402 verdict counts changed across the signed weekly snapshots?
  - id: get_corpus_battery_delta_json
    intent: Compare what the v2 battery catches over v1
    question: How many doors would v1 call ready that the stricter v2 battery catches?
  - id: get_corpus_wallet_facts_json
    intent: Count receiving addresses shared across doors
    question: How many receiving addresses are shared across more than one x402 door?
  phrasing_ops: 9
  slug: scvd-store-corpus-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Corpus.json API from SCVD General Store — 1 operation(s) for corpus.json.
  name: SCVD General Store Corpus.json API
  phrasing_intents:
  - id: get_corpus_json
    intent: Read the full signed x402 corpus
    question: Where are the weekly signed observations of the x402 ecosystem?
  phrasing_ops: 1
  slug: scvd-store-corpus-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Corrections API from SCVD General Store — 1 operation(s) for corrections.
  name: SCVD General Store Corrections API
  phrasing_intents:
  - id: get_corrections
    intent: Read the store's corrections
    question: Which claims has the store corrected?
  phrasing_ops: 1
  slug: scvd-store-corrections-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Credit API from SCVD General Store — 2 operation(s) for credit.
  name: SCVD General Store Credit API
  phrasing_intents:
  - id: get_credit
    intent: Read the regulars' credit rebate scheme
    question: What rebate do regulars earn here, and is it transferable?
  - id: get_api_credit_wallet
    intent: Check a wallet's rebate balance
    question: How much rebate credit has my wallet earned?
  phrasing_ops: 2
  slug: scvd-store-credit-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Declare Door API from SCVD General Store — 1 operation(s) for declare door.
  name: SCVD General Store Declare Door API
  phrasing_intents:
  - id: get_api_declare_door
    intent: Read how to declare a door
    question: How does a host the discovery feed misses get into the census?
  - id: post_api_declare_door
    intent: Declare a host's doors into the census
    question: Can I get my host's x402 doors added to this week's census roster?
  phrasing_ops: 2
  slug: scvd-store-declare-door-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Defects.json API from SCVD General Store — 1 operation(s) for defects.json.
  name: SCVD General Store Defects.json API
  phrasing_intents:
  - id: get_defects_json
    intent: Read the x402 defect vocabulary
    question: What are the named ways an x402 endpoint can be broken?
  phrasing_ops: 1
  slug: scvd-store-defects-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Deprecation API from SCVD General Store — 1 operation(s) for deprecation.
  name: SCVD General Store Deprecation API
  phrasing_intents:
  - id: get_deprecation
    intent: Read the versioning and deprecation policy
    question: How much notice does the store give before retiring an API version?
  phrasing_ops: 1
  slug: scvd-store-deprecation-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Developers API from SCVD General Store — 1 operation(s) for developers.
  name: SCVD General Store Developers API
  phrasing_intents:
  - id: get_developers
    intent: Read the developer documentation index
    question: Where is the store's developer documentation?
  phrasing_ops: 1
  slug: scvd-store-developers-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Directory API from SCVD General Store — 1 operation(s) for directory.
  name: SCVD General Store Directory API
  phrasing_intents:
  - id: get_directory
    intent: Read the Town Directory reviews
    question: What does the Town Directory say about the neighbors?
  phrasing_ops: 1
  slug: scvd-store-directory-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Doors API from SCVD General Store — 1 operation(s) for doors.
  name: SCVD General Store Doors API
  phrasing_intents:
  - id: get_doors
    intent: Browse every checked door
    question: Which x402 endpoints has the weekly ward round checked?
  phrasing_ops: 1
  slug: scvd-store-doors-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Doors.json API from SCVD General Store — 1 operation(s) for doors.json.
  name: SCVD General Store Doors.json API
  phrasing_intents:
  - id: get_doors_json
    intent: List every observed endpoint
    question: Which hosts has the signed chain carried, with their latest verdict?
  phrasing_ops: 1
  slug: scvd-store-doors-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Fresh Set API from SCVD General Store — 1 operation(s) for fresh set.
  name: SCVD General Store Fresh Set API
  phrasing_intents:
  - id: get_fresh_set
    intent: List doors that passed the latest census
    question: Which x402 doors answered correctly in the latest census?
  phrasing_ops: 1
  slug: scvd-store-fresh-set-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Gazette API from SCVD General Store — 1 operation(s) for gazette.
  name: SCVD General Store Gazette API
  phrasing_intents:
  - id: get_gazette
    intent: List archived Gazette issues
    question: Where are the archived Gazette issues?
  phrasing_ops: 1
  slug: scvd-store-gazette-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Good Buyer API from SCVD General Store — 1 operation(s) for good buyer.
  name: SCVD General Store Good Buyer API
  phrasing_intents:
  - id: get_api_good_buyer_reading_id
    intent: Read a purchased payment dry run
    question: What did my purchased dry run say my client would sign?
  phrasing_ops: 1
  slug: scvd-store-good-buyer-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Guestbook API from SCVD General Store — 1 operation(s) for guestbook.
  name: SCVD General Store Guestbook API
  phrasing_intents:
  - id: get_api_guestbook
    intent: Read the guestbook
    question: What have visitors written in the store's guestbook?
  - id: post_api_guestbook
    intent: Sign the guestbook
    question: Can I sign the store's guestbook and get a sticker?
  phrasing_ops: 2
  slug: scvd-store-guestbook-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Health API from SCVD General Store — 1 operation(s) for health.
  name: SCVD General Store Health API
  phrasing_intents:
  - id: get_health
    intent: Check the store's liveness
    question: Is the store's Worker up?
  phrasing_ops: 1
  slug: scvd-store-health-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Launch Check API from SCVD General Store — 1 operation(s) for launch check.
  name: SCVD General Store Launch Check API
  phrasing_intents:
  - id: get_api_launch_check_check_id
    intent: Read a purchased launch check record
    question: Did my launch check settle or get refused?
  phrasing_ops: 1
  slug: scvd-store-launch-check-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Ledger API from SCVD General Store — 2 operation(s) for ledger.
  name: SCVD General Store Ledger API
  phrasing_intents:
  - id: get_ledger
    intent: List the Week's Ledger readings
    question: Which weeks does the Week's Ledger cover?
  - id: get_ledger_week_json
    intent: Read one signed week's ledger
    question: What happened in the x402 neighbourhood in a given signed week?
  phrasing_ops: 2
  slug: scvd-store-ledger-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Letter API from SCVD General Store — 2 operation(s) for letter.
  name: SCVD General Store Letter API
  phrasing_intents:
  - id: post_api_letter
    intent: Post a private letter to the keeper
    question: Can I write a private letter to the keeper?
  - id: get_api_letter_letter_id
    intent: Check a letter's status and replies
    question: Has the keeper read or replied to my letter?
  phrasing_ops: 2
  slug: scvd-store-letter-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Look API from SCVD General Store — 1 operation(s) for look.
  name: SCVD General Store Look API
  phrasing_intents:
  - id: get_api_look_v1
    intent: Read how the look works
    question: What does the look answer about a door?
  - id: post_api_look_v1
    intent: Look at what the store holds about a door
    question: What does the store hold about an x402 door right now, next to a live probe?
  phrasing_ops: 2
  slug: scvd-store-look-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Lucky API from SCVD General Store — 1 operation(s) for lucky.
  name: SCVD General Store Lucky API
  phrasing_intents:
  - id: get_api_lucky_lucky_id
    intent: Read a lucky charm's record
    question: Which animal did my lucky charm draw?
  phrasing_ops: 1
  slug: scvd-store-lucky-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Mandate API from SCVD General Store — 1 operation(s) for mandate.
  name: SCVD General Store Mandate API
  phrasing_intents:
  - id: post_api_mandate_mandate_id
    intent: Counter-sign a mandate
    question: Can I counter-sign someone's mandate with my own key?
  - id: get_api_mandate_mandate_id
    intent: Read a purchased mandate record
    question: What does a recorded mandate say, and who counter-signed it?
  phrasing_ops: 2
  slug: scvd-store-mandate-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Mcp API from SCVD General Store — 1 operation(s) for mcp.
  name: SCVD General Store MCP API
  phrasing_intents:
  - id: post_mcp
    intent: Call the store's MCP server
    question: Can I use this store as an MCP server?
  phrasing_ops: 1
  slug: scvd-store-mcp-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Mcp Ward.json API from SCVD General Store — 1 operation(s) for mcp ward.json.
  name: SCVD General Store Mcp Ward.json API
  phrasing_intents:
  - id: get_mcp_ward_json
    intent: Read the MCP registry ward
    question: How many MCP registry servers has the store counted?
  phrasing_ops: 1
  slug: scvd-store-mcp-ward-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Menu API from SCVD General Store — 1 operation(s) for menu.
  name: SCVD General Store Menu API
  phrasing_intents:
  - id: get_menu_item_id
    intent: Read one menu item up close
    question: What inputs and price does an item need?
  phrasing_ops: 1
  slug: scvd-store-menu-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Menu.json API from SCVD General Store — 1 operation(s) for menu.json.
  name: SCVD General Store Menu.json API
  phrasing_intents:
  - id: get_menu_json
    intent: Read the full menu catalog
    question: What does the store sell and at what prices?
  phrasing_ops: 1
  slug: scvd-store-menu-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Onpage API from SCVD General Store — 1 operation(s) for onpage.
  name: SCVD General Store Onpage API
  phrasing_intents:
  - id: get_api_onpage_v1
    intent: Read how the on-page desk works
    question: What does the free on-page desk check?
  - id: post_api_onpage_v1
    intent: Check what a page serves a machine reader
    question: What title, meta description and JSON-LD does my page serve a crawler?
  phrasing_ops: 2
  slug: scvd-store-onpage-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Onpage Audit API from SCVD General Store — 1 operation(s) for onpage audit.
  name: SCVD General Store Onpage Audit API
  phrasing_intents:
  - id: get_api_onpage_audit_audit_id
    intent: Read a purchased on-page audit
    question: Where is my on-page audit report?
  phrasing_ops: 1
  slug: scvd-store-onpage-audit-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Open For Business API from SCVD General Store — 2 operation(s) for open for business.
  name: SCVD General Store Open For Business API
  phrasing_intents:
  - id: get_open_for_business
    intent: List Open for Business issues
    question: Which Open for Business issues are available for sellers?
  - id: get_open_for_business_week
    intent: Buy one Open for Business issue
    question: How do I buy a week's Open for Business issue?
  phrasing_ops: 2
  slug: scvd-store-open-for-business-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Operator Statement API from SCVD General Store — 1 operation(s) for operator statement.
  name: SCVD General Store Operator Statement API
  phrasing_intents:
  - id: get_api_operator_statement_statement_id
    intent: Read a month-long operator statement
    question: What inflows did my receiving address see this month?
  phrasing_ops: 1
  slug: scvd-store-operator-statement-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Order API from SCVD General Store — 1 operation(s) for order.
  name: SCVD General Store Order API
  phrasing_intents:
  - id: get_api_order_order_id
    intent: Poll a human-fulfilled order
    question: Is my human-fulfilled order done yet?
  phrasing_ops: 1
  slug: scvd-store-order-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Pack API from SCVD General Store — 1 operation(s) for pack.
  name: SCVD General Store Pack API
  phrasing_intents:
  - id: get_api_pack_pack_id
    intent: Read a pack's signed manifest
    question: Which five cards were in my pack?
  phrasing_ops: 1
  slug: scvd-store-pack-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Passport API from SCVD General Store — 2 operation(s) for passport.
  name: SCVD General Store Passport API
  phrasing_intents:
  - id: get_passport
    intent: Read what an endpoint passport is
    question: What is an endpoint passport?
  - id: get_passport_host
    intent: Get one host's endpoint passport
    question: Is this x402 host's passport fresh, aging or expired?
  phrasing_ops: 2
  slug: scvd-store-passport-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Patronage API from SCVD General Store — 1 operation(s) for patronage.
  name: SCVD General Store Patronage API
  phrasing_intents:
  - id: get_api_patronage_pass_id
    intent: Check a patronage pass
    question: Is my patronage pass current?
  phrasing_ops: 1
  slug: scvd-store-patronage-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Paywall API from SCVD General Store — 8 operation(s) for paywall.
  name: SCVD General Store Paywall API
  phrasing_intents:
  - id: get_api_paywall_binder_wallet
    intent: List the cards a wallet has pulled
    question: Which trading cards has a wallet pulled, newest first?
  - id: get_api_paywall_seed_date
    intent: Get the day seed and its commit
    question: Can I recompute a day's pack pulls from the published seed?
  - id: get_api_paywall_set
    intent: Read the season's card set
    question: Which cards are in the season set and how rare is each?
  - id: get_api_paywall_window
    intent: See the shop window's last five pressings
    question: Which five cards were pulled most recently store-wide?
  - id: get_api_paywall_releases
    intent: Read the release wheel for one-of-one cards
    question: When will the one-of-one Keeper and CV cards be released?
  - id: post_api_paywall_challenge
    intent: Get a credit-desk challenge to sign
    question: How do I get a challenge to sign before burning or redeeming cards?
  - id: post_api_paywall_burn
    intent: Burn duplicate cards into pack credit
    question: Can I trade in duplicate commons for a pack of credit?
  - id: post_api_paywall_redeem
    intent: Spend pack credit on a pack or window pick
    question: How do I spend a pack of credit I earned from burning cards?
  phrasing_ops: 8
  slug: scvd-store-paywall-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Phantom API from SCVD General Store — 1 operation(s) for phantom.
  name: SCVD General Store Phantom API
  phrasing_intents:
  - id: get_api_phantom_check_id
    intent: Pick up a phantom check attestation
    question: Is my phantom check ready?
  phrasing_ops: 1
  slug: scvd-store-phantom-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Porch API from SCVD General Store — 1 operation(s) for porch.
  name: SCVD General Store Porch API
  phrasing_intents:
  - id: get_porch
    intent: Sit on the porch
    question: What is happening on the porch tonight?
  phrasing_ops: 1
  slug: scvd-store-porch-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Practice API from SCVD General Store — 2 operation(s) for practice.
  name: SCVD General Store Practice API
  phrasing_intents:
  - id: get_api_practice
    intent: List the practice obstacle course
    question: Are there deliberately broken x402 doors to test my client against?
  - id: get_api_practice_scenario
    intent: Hit one practice scenario
    question: Can I safely hit a malformed 402 door from CI?
  phrasing_ops: 2
  slug: scvd-store-practice-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Preflight API from SCVD General Store — 4 operation(s) for preflight.
  name: SCVD General Store Preflight API
  phrasing_intents:
  - id: post_api_preflight_batch
    intent: Preflight up to ten x402 doors at once
    question: Can I check several x402 endpoints' payment challenges in one call?
  - id: get_api_preflight_checks
    intent: Read the preflight battery manifest
    question: Which stable check IDs make up each preflight battery?
  - id: get_api_preflight_v1
    intent: Read the v1 preflight criteria
    question: What does each v1 preflight check test and what falsifies it?
  - id: post_api_preflight_v1
    intent: Check an x402 endpoint's challenge shape with v1
    question: Does my x402 endpoint return a parseable PAYMENT-REQUIRED header under the v1 battery?
  - id: get_api_preflight_v2
    intent: Read the v2 preflight criteria
    question: What extra checks does the v2 preflight battery add?
  - id: post_api_preflight_v2
    intent: Check an x402 endpoint's challenge shape with v2
    question: Will my x402 endpoint pass the stricter v2 preflight, including Solana receivability?
  phrasing_ops: 6
  slug: scvd-store-preflight-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Pricing API from SCVD General Store — 1 operation(s) for pricing.
  name: SCVD General Store Pricing API
  phrasing_intents:
  - id: get_pricing
    intent: Read the signed pricing charter
    question: How does the store set prices?
  phrasing_ops: 1
  slug: scvd-store-pricing-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Pricing.md API from SCVD General Store — 1 operation(s) for pricing.md.
  name: SCVD General Store Pricing.md API
  phrasing_intents:
  - id: get_pricing_md
    intent: Read the pricing charter as markdown
    question: Is there a markdown version of the pricing charter?
  phrasing_ops: 1
  slug: scvd-store-pricing-md-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Profiles API from SCVD General Store — 2 operation(s) for profiles.
  name: SCVD General Store Profiles API
  phrasing_intents:
  - id: get_profiles
    intent: List hosted trust profiles
    question: Which endpoints have a hosted trust profile right now?
  - id: get_profiles_host
    intent: Read one host's hosted trust profile
    question: What does a host's commissioned trust profile show?
  phrasing_ops: 2
  slug: scvd-store-profiles-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Pulse.json API from SCVD General Store — 1 operation(s) for pulse.json.
  name: SCVD General Store Pulse.json API
  phrasing_intents:
  - id: get_pulse_json
    intent: Read the store's sales funnel
    question: How many 402s turned into settlements?
  phrasing_ops: 1
  slug: scvd-store-pulse-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Purchase Status API from SCVD General Store — 1 operation(s) for purchase status.
  name: SCVD General Store Purchase Status API
  phrasing_intents:
  - id: get_api_purchase_status_purchase_id
    intent: Read a retained purchase status
    question: Is my purchase still pending recovery?
  phrasing_ops: 1
  slug: scvd-store-purchase-status-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Reconciliation API from SCVD General Store — 1 operation(s) for reconciliation.
  name: SCVD General Store Reconciliation API
  phrasing_intents:
  - id: get_api_reconciliation_reconciliation_id
    intent: Read a settlement reconciliation
    question: What did my reconciliation find about authorized versus taken?
  phrasing_ops: 1
  slug: scvd-store-reconciliation-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Refund API from SCVD General Store — 1 operation(s) for refund.
  name: SCVD General Store Refund API
  phrasing_intents:
  - id: get_api_refund_refund_id
    intent: Check a refund's status
    question: Has my refund been paid?
  phrasing_ops: 1
  slug: scvd-store-refund-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Registry API from SCVD General Store — 1 operation(s) for registry.
  name: SCVD General Store Registry API
  phrasing_intents:
  - id: get_registry
    intent: Read the state of the x402 registry
    question: How many listed x402 doors actually work?
  phrasing_ops: 1
  slug: scvd-store-registry-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Replay API from SCVD General Store — 1 operation(s) for replay.
  name: SCVD General Store Replay API
  phrasing_intents:
  - id: get_api_replay_cert_id
    intent: Replay a paid call as an integration test
    question: Can I replay a paid call without trusting the store?
  phrasing_ops: 1
  slug: scvd-store-replay-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Request API from SCVD General Store — 1 operation(s) for request.
  name: SCVD General Store Request API
  phrasing_intents:
  - id: post_api_request
    intent: Commission something not on the shelf
    question: Can I ask the keeper for something not on the menu?
  phrasing_ops: 1
  slug: scvd-store-request-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Rights API from SCVD General Store — 1 operation(s) for rights.
  name: SCVD General Store Rights API
  phrasing_intents:
  - id: get_rights
    intent: Read what I own after buying
    question: Do I own what I buy here?
  phrasing_ops: 1
  slug: scvd-store-rights-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Samples API from SCVD General Store — 2 operation(s) for samples.
  name: SCVD General Store Samples API
  phrasing_intents:
  - id: get_samples
    intent: See free samples of paid artifacts
    question: Can I see a sample of a paid artifact before buying?
  - id: get_samples_once_over_json
    intent: Get the free Once-Over audit specimen
    question: What fields does a $5 service audit contain?
  phrasing_ops: 2
  slug: scvd-store-samples-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Service Audit API from SCVD General Store — 1 operation(s) for service audit.
  name: SCVD General Store Service Audit API
  phrasing_intents:
  - id: get_api_service_audit_audit_id
    intent: Read a purchased endpoint audit
    question: What verdict did my service audit give?
  phrasing_ops: 1
  slug: scvd-store-service-audit-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Sites API from SCVD General Store — 1 operation(s) for sites.
  name: SCVD General Store Sites API
  phrasing_intents:
  - id: get_sites
    intent: List sites the ask endpoint answers for
    question: Which sites does ask answer for?
  phrasing_ops: 1
  slug: scvd-store-sites-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Sources.json API from SCVD General Store — 1 operation(s) for sources.json.
  name: SCVD General Store Sources.json API
  phrasing_intents:
  - id: get_sources_json
    intent: See where the store's numbers come from
    question: Which public directories feed the store's figures?
  phrasing_ops: 1
  slug: scvd-store-sources-json-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Stamp API from SCVD General Store — 1 operation(s) for stamp.
  name: SCVD General Store Stamp API
  phrasing_intents:
  - id: post_api_stamp
    intent: Get a free weekly visit stamp
    question: Can I get a signed visit stamp?
  phrasing_ops: 1
  slug: scvd-store-stamp-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Standing Note API from SCVD General Store — 1 operation(s) for standing note.
  name: SCVD General Store Standing Note API
  phrasing_intents:
  - id: get_api_standing_note
    intent: Read how to attach a standing note
    question: How can I attach my own statement to a door the store observed?
  - id: post_api_standing_note
    intent: Attach a standing note to a subject
    question: Can I post my own dated statement about my door or wallet?
  phrasing_ops: 2
  slug: scvd-store-standing-note-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Statement API from SCVD General Store — 1 operation(s) for statement.
  name: SCVD General Store Statement API
  phrasing_intents:
  - id: get_api_statement_statement_id
    intent: Read a purchased wallet statement
    question: What transfers are in my wallet statement?
  phrasing_ops: 1
  slug: scvd-store-statement-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Tab API from SCVD General Store — 2 operation(s) for tab.
  name: SCVD General Store Tab API
  phrasing_intents:
  - id: post_api_tab_delta
    intent: Contribute an anonymized tab delta
    question: Can I contribute to the pooled tab corpus?
  - id: get_api_tab_pool
    intent: See the pooled tab corpus sample sizes
    question: How big is the pooled tab corpus?
  phrasing_ops: 2
  slug: scvd-store-tab-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Tip API from SCVD General Store — 1 operation(s) for tip.
  name: SCVD General Store Tip API
  phrasing_intents:
  - id: post_api_tip
    intent: Leave a Trading Post tip
    question: Can I submit a tip to the Trading Post?
  phrasing_ops: 1
  slug: scvd-store-tip-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Trade API from SCVD General Store — 9 operation(s) for trade.
  name: SCVD General Store Trade API
  phrasing_intents:
  - id: get_api_trade_contract
    intent: Read the trade counter's contract
    question: How does a marketplace order from the shelf on account?
  - id: get_api_trade_ledger
    intent: Read every trade account's books
    question: What does each trade account owe, and what has been paid?
  - id: get_api_trade_catalog
    intent: Read the trade listing feed
    question: Which items can a marketplace list from the trade counter, at what trade price?
  - id: post_api_trade_sandbox_check
    intent: Test trade request signing in the sandbox
    question: Can I check my HMAC trade signature in the sandbox before ordering?
  - id: post_api_trade_sandbox_item_id
    intent: Order an item on the sandbox trade account
    question: How do I place a test trade order on the sandbox account?
  - id: post_api_trade_partner_check
    intent: Test a partner's trade signing without ordering
    question: Will my partner account's signed request pass all four checks before I order?
  - id: get_api_trade_partner_claim
    intent: Recover a trade delivery by order reference
    question: How can a marketplace recover a customer's lost receipt by order reference?
  - id: get_api_trade_partner_statement
    intent: Read a trade account's signed statement
    question: Which deliveries and payouts are on my trade account?
  phrasing_ops: 9
  slug: scvd-store-trade-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Trade.md API from SCVD General Store — 1 operation(s) for trade.md.
  name: SCVD General Store Trade.md API
  phrasing_intents:
  - id: get_trade_md
    intent: Read the trade counter as markdown
    question: Is the trade counter available as markdown?
  phrasing_ops: 1
  slug: scvd-store-trade-md-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Trust API from SCVD General Store — 1 operation(s) for trust.
  name: SCVD General Store Trust API
  phrasing_intents:
  - id: get_trust
    intent: Open the trust panel
    question: Where is every trust surface?
  phrasing_ops: 1
  slug: scvd-store-trust-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Verify API from SCVD General Store — 1 operation(s) for verify.
  name: SCVD General Store Verify API
  phrasing_intents:
  - id: get_api_verify_id
    intent: Verify a store signature
    question: Is this certificate genuinely signed by the store?
  phrasing_ops: 1
  slug: scvd-store-verify-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Verify Receipt API from SCVD General Store — 1 operation(s) for verify receipt.
  name: SCVD General Store Verify Receipt API
  phrasing_intents:
  - id: get_api_verify_receipt
    intent: Read how receipt verification works
    question: What does the receipt verification desk check and not check?
  - id: post_api_verify_receipt
    intent: Verify any signed receipt
    question: Is this receipt from any issuer valid?
  phrasing_ops: 2
  slug: scvd-store-verify-receipt-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Watch API from SCVD General Store — 1 operation(s) for watch.
  name: SCVD General Store Watch API
  phrasing_intents:
  - id: get_api_watch_watch_id
    intent: Read a standing watch's hourly history
    question: What did my standing watch see each hour?
  phrasing_ops: 1
  slug: scvd-store-watch-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The .well Known API from SCVD General Store — 11 operation(s) for .well known.
  name: SCVD General Store .well Known API
  phrasing_intents:
  - id: get_well_known_oauth_protected_resource
    intent: Read the protected-resource metadata
    question: Does this store publish RFC 9728 protected-resource metadata?
  - id: get_well_known_api_catalog
    intent: Read the RFC 9727 API catalog
    question: Which API surfaces does this origin serve, as an RFC 9727 linkset?
  - id: get_well_known_ard_json
    intent: Read the Agentic Resource Discovery manifest
    question: What agentic resources does the store publish in its ARD manifest?
  - id: get_well_known_ai_catalog_json
    intent: Read the ARD manifest at its predecessor path
    question: Is ai-catalog.json still served for scanners that know only the old path?
  - id: get_well_known_mcp_json
    intent: Read the MCP manifest at the .json alias
    question: Is the MCP manifest also available at mcp.json?
  - id: get_well_known_http_message_signatures_directory
    intent: Read the store's Web Bot Auth key directory
    question: Which ed25519 key does the store sign its outbound probes with?
  - id: get_well_known_x402
    intent: Read the minimal x402 discovery listing
    question: What is the de-facto x402 indexer entry point for this store?
  - id: get_well_known_x402_json
    intent: Read the full x402 catalog of payable resources
    question: Where is the richer origin-hosted catalog of payable x402 resources?
  phrasing_ops: 11
  slug: scvd-store-well-known-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The What API from SCVD General Store — 1 operation(s) for what.
  name: SCVD General Store What API
  phrasing_intents:
  - id: get_what
    intent: Open the Operator Glance
    question: What is this store, in ten seconds?
  phrasing_ops: 1
  slug: scvd-store-what-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Wind Down API from SCVD General Store — 1 operation(s) for wind down.
  name: SCVD General Store Wind Down API
  phrasing_intents:
  - id: get_wind_down
    intent: Read the wind-down plan
    question: What happens to my artifacts if the store closes?
  phrasing_ops: 1
  slug: scvd-store-wind-down-api
- baseURL: https://scvd.store/mcp
  baseurl_source: declared
  description: The Zodiac API from SCVD General Store — 3 operation(s) for zodiac.
  name: SCVD General Store Zodiac API
  phrasing_intents:
  - id: get_zodiac
    intent: Open the archived Systems Almanac
    question: Where is the archived Systems Almanac?
  - id: get_zodiac_address
    intent: Read a wallet's archived sign
    question: What is the archived wallet sign for an address?
  - id: get_zodiac_archive
    intent: List the archived Season One almanac pages
    question: Which Season One Systems Almanac pages are archived?
  phrasing_ops: 3
  slug: scvd-store-zodiac-api
artifact_total: 107
asyncapis:
- description: ''
  name: Scvd Store Webhooks
  slug: scvd-store-webhooks
common:
- group: other
  href: https://artifacts.apis.io/scvd-store/capabilities/scvd-store-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scvd-store-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/scvd-store/overlays/scvd-store-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scvd-store-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://scvd.store/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://scvd.store/developers
- group: docs
  title: ''
  type: Documentation
  url: https://scvd.store/developers
- group: docs
  title: ''
  type: APIReference
  url: https://scvd.store/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://scvd.store/agents.md
- group: start
  href: https://artifacts.apis.io/scvd-store/sandbox/scvd-store-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/scvd-store-sandbox.yml
- group: start
  title: ''
  type: Sandbox
  url: https://scvd.store/try
- group: commercial
  title: ''
  type: Pricing
  url: https://scvd.store/pricing
- group: commercial
  href: https://artifacts.apis.io/scvd-store/plans/scvd-store-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scvd-store-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scvd.store/rights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scvd.store/privacy
- group: operate
  title: ''
  type: Support
  url: https://scvd.store/what
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seancrecord
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/seancrecord/scvd-general-store-repo
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/seancrecord/scvd-general-store-repo/blob/main/ROADMAP.md
- group: operate
  title: ''
  type: StatusPage
  url: https://scvd.store/.well-known/liveness.json
- group: operate
  title: ''
  type: Deprecation
  url: https://scvd.store/deprecation
- group: design
  href: https://artifacts.apis.io/scvd-store/lifecycle/scvd-store-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scvd-store-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/scvd-store/changelog/scvd-store-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scvd-store-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://scvd.store/feeds/corrections.xml
- group: agent
  href: https://artifacts.apis.io/scvd-store/llms/scvd-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scvd-store-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://scvd.store/llms.txt
- group: other
  title: ''
  type: AgentsMd
  url: https://scvd.store/agents.md
- group: agent
  href: https://artifacts.apis.io/scvd-store/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://scvd.store/skill.md
- group: other
  href: https://artifacts.apis.io/scvd-store/a2a/scvd-store-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/scvd-store-a2a.yml
- group: agent
  href: https://artifacts.apis.io/scvd-store/mcp/scvd-store-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scvd-store-mcp.yml
- group: build
  href: https://artifacts.apis.io/scvd-store/mcp/scvd-store-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/scvd-store-tool-crosswalk.yml
- group: agent
  title: ''
  type: WebMCP
  url: https://scvd.store/webmcp.js
- group: agent
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scvd-store-well-known.yml
- group: auth
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/scvd-store-security.txt
- group: auth
  title: ''
  type: Security
  url: https://scvd.store/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/scvd-store/security/scvd-store-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/scvd-store-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/scvd-store/security/scvd-store-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scvd-store-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://scvd.store/trust
- group: auth
  href: https://artifacts.apis.io/scvd-store/security/scvd-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scvd-store-domain-security.yml
- group: other
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/scvd-store-api-catalog.json
- group: build
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/scvd-store-ai-plugin.json
- group: other
  title: ''
  type: ContentSignal
  url: https://scvd.store/robots.txt
- group: other
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-agent-instructions.json
  title: ''
  type: AgentInstructions
  url: well-known/scvd-store-agent-instructions.json
- group: other
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-x402.json
  title: ''
  type: X402
  url: well-known/scvd-store-x402.json
- group: other
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-ucp.json
  title: ''
  type: UCP
  url: well-known/scvd-store-ucp.json
- group: other
  href: https://artifacts.apis.io/scvd-store/well-known/scvd-store-ard.json
  title: ''
  type: ARD
  url: well-known/scvd-store-ard.json
- group: auth
  href: https://artifacts.apis.io/scvd-store/authentication/scvd-store-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scvd-store-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: https://scvd.store/auth.md
- group: design
  href: https://artifacts.apis.io/scvd-store/conventions/scvd-store-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scvd-store-conventions.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/conventions/scvd-store-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/scvd-store-conventions.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/errors/scvd-store-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scvd-store-problem-types.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/errors/scvd-store-defects.json
  title: ''
  type: ErrorCatalog
  url: errors/scvd-store-defects.json
- group: operate
  href: https://artifacts.apis.io/scvd-store/rate-limits/scvd-store-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scvd-store-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/conformance/scvd-store-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scvd-store-conformance.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/asyncapi/scvd-store-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/scvd-store-webhooks.yml
- group: build
  href: https://artifacts.apis.io/scvd-store/packages/scvd-store-packages.yml
  title: ''
  type: Packages
  url: packages/scvd-store-packages.yml
- group: build
  href: https://artifacts.apis.io/scvd-store/packages/scvd-store-packages.yml
  title: ''
  type: SDKs
  url: packages/scvd-store-packages.yml
- group: build
  href: https://artifacts.apis.io/scvd-store/cli/scvd-store-cli.yml
  title: ''
  type: CLI
  url: cli/scvd-store-cli.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/components/scvd-store-components.yml
  title: ''
  type: Components
  url: components/scvd-store-components.yml
- group: design
  href: https://artifacts.apis.io/scvd-store/data-model/scvd-store-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scvd-store-data-model.yml
- group: agent
  href: https://artifacts.apis.io/scvd-store/agentic-access/scvd-store-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scvd-store-agentic-access.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://scvd.store/stack
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://scvd.store/privacy
- group: operate
  title: ''
  type: SupportLifetime
  url: https://scvd.store/deprecation
- group: other
  title: ''
  type: ExitAssistance
  url: https://scvd.store/wind-down
created: '2026-09-19'
description: 'Record Creative Co. LLC is the one-person Oak City, North Carolina company that operates scvd.store — "Sean-Claude Van Damme''s General Store", an evidence observatory for agentic commerce and a general store for AI agents. It independently verifies x402 payment endpoints, signed offers and receipts: a free preflight that checks whether any x402 door serves a well-formed, payable v2 challenge, a free conformance desk for any issuer''s JWS-signed offers and receipts, a named 31-class defect vocabulary, and a weekly Bitcoin-anchored, hash-chained corpus of the public x402 web. Paid instruments (35 doors from $0.001 to $1,500) — settlement attestations, endpoint watches, launch checks, conformance audits, A2A repair kits, agent memory anchors and the labor of a named human — are bought per call in USDC over x402 v2 on Base, Polygon, Arbitrum, World or Solana with no account, key or signup; every purchase ends in an Ed25519-signed artifact verifiable free forever. One host publishes
  the whole surface: a 196-operation OpenAPI 3.1 contract, three remote MCP servers (20 tools, MCP Apps cards), an A2A 0.3.0 agent card, a UCP business profile, an RFC 9727 API catalog, RFC 9728 protected-resource metadata, llms.txt, agents.md, SKILL.md files, an official CLI and nine more open-source packages.'
finops:
- has_sources: true
  method: derived
  name: Scvd Store Finops
  primary_unit: usdc fixed, one-off
  service_category: ''
  slug: scvd-store-finops
  template: false
image: https://scvd.store/og.png
layout: provider
mcp_servers:
- description: 'SCVD General Store operates THREE remote MCP servers on its apex host, all Streamable HTTP (POST), all answering initialize, tools/list and resources/list anonymously, all at serverInfo version 0.5.0 '
  name: SCVD General Store MCP Server
  slug: scvd-store-mcp-yml
- description: ''
  name: SCVD x402 Verifier MCP endpoint
  slug: scvd-x402-verifier-mcp-endpoint
- description: ''
  name: SCVD Store Docs MCP endpoint
  slug: scvd-store-docs-mcp-endpoint
modified: '2026-09-19'
name: SCVD General Store
nav: Providers
network: true
overview: 'SCVD General Store publishes 91 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2a API, A2a Desk.json API, Almanac API, and 88 more. Tagged areas include Agents, Agentic Commerce, x402, Payments, and Micropayments.


  The SCVD General Store catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SCVD General Store''s developer surface includes documentation, API reference, getting-started guide, sandbox, pricing, support, changelog, and 57 more developer resources.'
plans:
- name: Scvd Store Plans Pricing
  plan_count: 38
  slug: scvd-store-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Scvd Store Rate Limits
  slug: scvd-store-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: SCVD General Store API Rules
  rule_count: 65
  severity_counts:
    error: 48
    hint: 0
    info: 4
    warn: 13
  slug: scvd-store-rules
score:
  band: strong
  composite: 65.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 63.2
    contract_governance: 31.8
    contract_quality: 62.5
    developer_ergonomics: 61.9
    discoverability: 85.0
    operational_transparency: 77.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 75.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 89
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/scvd-store/scvd-store-2026-10-11T125602.png
security:
- kind: authentication
  name: Scvd Store Authentication
  slug: scvd-store-authentication
  summary_line: none (anonymous)/x402 payment signature (per-call)/http bearer (one narrow scope)/http basic (back office, not for agents) · 5 schemes
- kind: domain-security
  name: Scvd Store Domain Security
  slug: scvd-store-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Scvd Store Vulnerability Disclosure
  slug: scvd-store-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Scvd Store Trust Center
  slug: scvd-store-trust-center
  summary_line: trust center published
skill_count: 3
skills:
- name: execution-contract
  slug: scvd-store-execution-contract
- name: scvd-general-store
  slug: scvd-store-general-store
- name: scvd-x402-verification
  slug: scvd-store-x402-verification
slug: scvd-store
tags:
- Agents
- Agentic Commerce
- x402
- Payments
- Micropayments
- Stablecoins
- USDC
- Verification
- Conformance
- Attestation
- Observability
- MCP
- A2A
- Universal Commerce Protocol
- Signatures
- Agent-Native
- United States
website: https://scvd.store/
---
