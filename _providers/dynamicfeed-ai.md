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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Hosted, keyless Model Context Protocol server at https://dynamicfeed.ai/mcp (Streamable HTTP with legacy HTTP+SSE auto-detected; explicit SSE at /sse) exposing all 94 read-only live-data tools with re
  name: Dynamic Feed MCP Server
  slug: dynamic-feed-mcp-server
- description: A2A 1.0 JSON-RPC agent at https://dynamicfeed.ai/a2a with a JWS-signed agent card (graded conformant) declaring eight keyless skills — live weather, natural hazards, macro and rates, security intel, c
  name: Dynamic Feed A2A Agent
  slug: dynamic-feed-a2a-agent
- description: 'Push-on-change webhooks registered per key at POST /v1/webhooks (SSRF-validated URL, one-time secret, HMAC-SHA256 X-DynamicFeed-Signature on every delivery) and a keyless Server-Sent Events stream at '
  name: Dynamic Feed Webhooks and Live Stream
  slug: dynamic-feed-webhooks-and-stream
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Advisories API from Dynamic Feed — 2 operation(s) for advisories.
  name: Dynamic Feed Advisories API
  phrasing_intents:
  - id: advisories_advisories_get
    intent: Browse recent security advisories
    question: What critical security advisories were published recently for npm packages?
  - id: advisories_check_advisories_check_get
    intent: Check if a package version is vulnerable
    question: Is lodash 4.17.10 vulnerable, and which version fixes it?
  phrasing_ops: 2
  slug: dynamicfeed-ai-advisories-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The agent API from Dynamic Feed — 53 operation(s) for agent.
  name: Dynamic Feed Agent API
  phrasing_intents:
  - id: v1_discover_get_v1_discover_get
    intent: Find live data capabilities for a need
    question: Which Dynamic Feed tool should my agent use for live rainfall data in a given city?
  - id: v1_discover_post_v1_discover_post
    intent: Discover capabilities with a JSON request body
    question: Is there a POST version of capability discovery that takes the need as a JSON body?
  - id: schemas_index_schemas_index_json_get
    intent: List the receipt schema family
    question: What receipt schemas does Dynamic Feed publish, and which mint endpoint goes with each?
  - id: v1_bundles_v1_bundles_get
    intent: List curated tool bundles by domain
    question: What curated tool bundles exist so I can pick tools for my agent's use case?
  - id: v1_bundle_v1_bundles__bundle_id__get
    intent: Get one curated tool bundle
    question: Which tools are in the devsecops bundle?
  - id: v1_batch_v1_batch_post
    intent: Run up to 20 data tool calls in one request
    question: Can I fetch weather and earthquakes together in a single free request?
  - id: v1_pro_tool_v1_pro_tool__tool__post
    intent: Make a paid, signed single tool call
    question: Can my agent pay per call in USDC for one signed datapoint without signing up?
  - id: v1_pro_tool_discover_v1_pro_tool__tool__get
    intent: See the x402 price for a paid tool call
    question: What does a single paid call to a given tool cost, and what asset is it paid in?
  phrasing_ops: 61
  slug: dynamicfeed-ai-agent-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Agent Stats API from Dynamic Feed — 1 operation(s) for agent stats.
  name: Dynamic Feed Agent Stats API
  phrasing_intents:
  - id: agent_stats_v1_agent_stats_get
    intent: View public agent traffic stats
    question: How many tool calls are AI agents making to Dynamic Feed?
  phrasing_ops: 1
  slug: dynamicfeed-ai-agent-stats-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Ai Models API from Dynamic Feed — 1 operation(s) for ai models.
  name: Dynamic Feed Ai Models API
  phrasing_intents:
  - id: ai_models_ep_ai_models_get
    intent: Find trending open AI models
    question: What open-weight models are trending on Hugging Face this week?
  phrasing_ops: 1
  slug: dynamicfeed-ai-ai-models-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Air Quality API from Dynamic Feed — 1 operation(s) for air quality.
  name: Dynamic Feed Air Quality API
  phrasing_intents:
  - id: air_quality_air_quality_get
    intent: Get current air quality for a place
    question: What is the air quality index in Delhi right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-air-quality-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Airport Delays API from Dynamic Feed — 1 operation(s) for airport delays.
  name: Dynamic Feed Airport Delays API
  phrasing_intents:
  - id: airport_delays_airport_delays_get
    intent: Check live US airport delays
    question: Are there any ground stops or delays at LaGuardia right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-airport-delays-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Benchmarks API from Dynamic Feed — 2 operation(s) for benchmarks.
  name: Dynamic Feed Benchmarks API
  phrasing_intents:
  - id: benchmarks_benchmarks_get
    intent: Compare AI provider latency and uptime
    question: Which AI provider has the fastest response times right now?
  - id: benchmarks_history_benchmarks_history_get
    intent: Get historical AI provider latency data
    question: Can I get the daily latency and uptime archive for one AI provider?
  phrasing_ops: 2
  slug: dynamicfeed-ai-benchmarks-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Billing API from Dynamic Feed — 3 operation(s) for billing.
  name: Dynamic Feed Billing API
  phrasing_intents:
  - id: checkout_billing_checkout_post
    intent: Start checkout to upgrade an API key
    question: How much do the pro, ultra and mega plans cost per month?
  - id: billing_success_billing_success_get
    intent: Show the post-payment success page
    question: What page do I land on after completing a plan payment?
  - id: billing_webhook_billing_webhook_post
    intent: Receive payment confirmation events
    question: How does my key get upgraded or downgraded after a payment event?
  phrasing_ops: 3
  slug: dynamicfeed-ai-billing-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Carbon Intensity API from Dynamic Feed — 1 operation(s) for carbon intensity.
  name: Dynamic Feed Carbon Intensity API
  phrasing_intents:
  - id: carbon_intensity_carbon_intensity_get
    intent: Get Great Britain grid carbon intensity
    question: How clean is the British electricity grid right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-carbon-intensity-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The China API from Dynamic Feed — 1 operation(s) for china.
  name: Dynamic Feed China API
  phrasing_intents:
  - id: china_ep_china_get
    intent: Get China markets and macro data
    question: Where are the Shanghai Composite and Hang Seng trading today?
  phrasing_ops: 1
  slug: dynamicfeed-ai-china-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Cite API from Dynamic Feed — 1 operation(s) for cite.
  name: Dynamic Feed Cite API
  phrasing_intents:
  - id: cite_ep_cite_get
    intent: Get a citeable source for a datapoint
    question: Where can I cite current earthquake data from, with a timestamp?
  phrasing_ops: 1
  slug: dynamicfeed-ai-cite-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Consensus API from Dynamic Feed — 1 operation(s) for consensus.
  name: Dynamic Feed Consensus API
  phrasing_intents:
  - id: consensus_consensus_get
    intent: Get cross-exchange price consensus
    question: What is the real price of BTC across exchanges and how much do venues disagree?
  phrasing_ops: 1
  slug: dynamicfeed-ai-consensus-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Convert API from Dynamic Feed — 1 operation(s) for convert.
  name: Dynamic Feed Convert API
  phrasing_intents:
  - id: convert_ep_convert_get
    intent: Convert money between currencies
    question: How many US dollars is 250 euros at today's reference rate?
  phrasing_ops: 1
  slug: dynamicfeed-ai-convert-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Countdown API from Dynamic Feed — 1 operation(s) for countdown.
  name: Dynamic Feed Countdown API
  phrasing_intents:
  - id: countdown_ep_countdown_get
    intent: Count down to a live event
    question: How long until the NYSE opens?
  phrasing_ops: 1
  slug: dynamicfeed-ai-countdown-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Dataset API from Dynamic Feed — 8 operation(s) for dataset.
  name: Dynamic Feed Dataset API
  phrasing_intents:
  - id: dataset_index_dataset_get
    intent: List the open dataset snapshots
    question: Are there free crawlable snapshots of Dynamic Feed's data for AI training?
  - id: dataset_models_dataset_models_json_get
    intent: Download the AI models dataset snapshot
    question: Can I download a snapshot of the AI model pricing data as JSON?
  - id: dataset_servers_dataset_servers_json_get
    intent: Download the MCP servers dataset snapshot
    question: Is there a downloadable snapshot of the MCP server registry data?
  - id: dataset_status_dataset_status_json_get
    intent: Download the service status dataset snapshot
    question: Can I download a snapshot of AI and dev service status data?
  - id: dataset_news_dataset_news_json_get
    intent: Download the AI news dataset snapshot
    question: Is there a JSON snapshot of the AI news feed I can crawl?
  - id: dataset_consensus_dataset_consensus_json_get
    intent: Download the price consensus dataset snapshot
    question: Can I download a snapshot of the cross-exchange price consensus data?
  - id: dataset_versions_dataset_versions_json_get
    intent: Download the software versions dataset snapshot
    question: Is there a static JSON snapshot of latest software versions and end-of-life dates?
  - id: dataset_advisories_dataset_advisories_json_get
    intent: Download the security advisories dataset snapshot
    question: Can I download a snapshot of the security advisories feed?
  phrasing_ops: 8
  slug: dynamicfeed-ai-dataset-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The dev API from Dynamic Feed — 3 operation(s) for dev.
  name: Dynamic Feed Dev API
  phrasing_intents:
  - id: github_releases_ep_github_releases_get
    intent: List the latest releases for a repo
    question: What are the most recent releases of a GitHub repository?
  - id: hacker_news_ep_hacker_news_get
    intent: Get live Hacker News stories
    question: What are the top stories on Hacker News right now?
  - id: dns_ep_dns_get
    intent: Look up live DNS records for a domain
    question: What are the current MX records for a domain?
  phrasing_ops: 3
  slug: dynamicfeed-ai-dev-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Drought API from Dynamic Feed — 1 operation(s) for drought.
  name: Dynamic Feed Drought API
  phrasing_intents:
  - id: drought_drought_get
    intent: Get US drought severity by week
    question: What share of the US is in severe drought this week?
  phrasing_ops: 1
  slug: dynamicfeed-ai-drought-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Drug Shortages API from Dynamic Feed — 1 operation(s) for drug shortages.
  name: Dynamic Feed Drug Shortages API
  phrasing_intents:
  - id: drug_shortages_drug_shortages_get
    intent: Check US drug shortages
    question: Is amoxicillin in shortage in the US right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-drug-shortages-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Dynamic Feed — Live Data For AI API from Dynamic Feed — 1 operation(s) for dynamic feed — live data for ai.
  name: Dynamic Feed Dynamic Feed — Live Data For AI API
  phrasing_intents:
  - id: home__get
    intent: Open the landing page
    question: Where is the main landing page with the live demo widget?
  phrasing_ops: 1
  slug: dynamicfeed-ai-dynamic-feed-live-data-for-ai-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Earthquakes API from Dynamic Feed — 1 operation(s) for earthquakes.
  name: Dynamic Feed Earthquakes API
  phrasing_intents:
  - id: earthquakes_earthquakes_get
    intent: List recent earthquakes worldwide
    question: Were there any big earthquakes in the past day?
  phrasing_ops: 1
  slug: dynamicfeed-ai-earthquakes-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Energy API from Dynamic Feed — 1 operation(s) for energy.
  name: Dynamic Feed Energy API
  phrasing_intents:
  - id: energy_grid_energy_get
    intent: Get live US electricity grid data
    question: What is current electricity demand on the ERCOT grid?
  phrasing_ops: 1
  slug: dynamicfeed-ai-energy-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Exploited Vulnerabilities API from Dynamic Feed — 1 operation(s) for exploited vulnerabilities.
  name: Dynamic Feed Exploited Vulnerabilities API
  phrasing_intents:
  - id: exploited_vulnerabilities_exploited_vulnerabilities_get
    intent: List vulnerabilities exploited in the wild
    question: Which Microsoft vulnerabilities are being actively exploited right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-exploited-vulnerabilities-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Federal Register API from Dynamic Feed — 1 operation(s) for federal register.
  name: Dynamic Feed Federal Register API
  phrasing_intents:
  - id: federal_register_federal_register_get
    intent: Search recent Federal Register documents
    question: What executive orders has the President signed recently?
  phrasing_ops: 1
  slug: dynamicfeed-ai-federal-register-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Flights API from Dynamic Feed — 1 operation(s) for flights.
  name: Dynamic Feed Flights API
  phrasing_intents:
  - id: flights_flights_get
    intent: Track live aircraft positions
    question: What planes are flying over London right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-flights-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Forecast API from Dynamic Feed — 1 operation(s) for forecast.
  name: Dynamic Feed Forecast API
  phrasing_intents:
  - id: forecast_forecast_get
    intent: Get a multi-day weather forecast
    question: Will it rain in Paris over the next week?
  phrasing_ops: 1
  slug: dynamicfeed-ai-forecast-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Global Disasters API from Dynamic Feed — 1 operation(s) for global disasters.
  name: Dynamic Feed Global Disasters API
  phrasing_intents:
  - id: global_disasters_ep_global_disasters_get
    intent: Get global disaster alerts
    question: Are there any red-level disaster alerts anywhere in the world right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-global-disasters-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Gps Interference API from Dynamic Feed — 1 operation(s) for gps interference.
  name: Dynamic Feed Gps Interference API
  phrasing_intents:
  - id: gps_interference_gps_interference_get
    intent: Check GPS jamming or spoofing in an area
    question: Is there GPS jamming over the Baltic right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-gps-interference-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Health API from Dynamic Feed — 1 operation(s) for health.
  name: Dynamic Feed Health API
  phrasing_intents:
  - id: health_health_get
    intent: Check service health
    question: Is the Dynamic Feed service up and healthy?
  phrasing_ops: 1
  slug: dynamicfeed-ai-health-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The History API from Dynamic Feed — 1 operation(s) for history.
  name: Dynamic Feed History API
  phrasing_intents:
  - id: history_v1_history_get
    intent: See what the permanent archive covers
    question: Which tools are captured in the permanent archive?
  phrasing_ops: 1
  slug: dynamicfeed-ai-history-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Info API from Dynamic Feed — 1 operation(s) for info.
  name: Dynamic Feed Info API
  phrasing_intents:
  - id: info_info_get
    intent: Get service information
    question: What general information does the service publish about itself?
  phrasing_ops: 1
  slug: dynamicfeed-ai-info-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Internet Outages API from Dynamic Feed — 1 operation(s) for internet outages.
  name: Dynamic Feed Internet Outages API
  phrasing_intents:
  - id: internet_outages_internet_outages_get
    intent: Check BGP reachability for a network
    question: Is a given ASN losing global reachability right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-internet-outages-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Iss API from Dynamic Feed — 1 operation(s) for iss.
  name: Dynamic Feed Iss API
  phrasing_intents:
  - id: iss_iss_get
    intent: Locate the International Space Station
    question: Where is the ISS right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-iss-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Launches API from Dynamic Feed — 1 operation(s) for launches.
  name: Dynamic Feed Launches API
  phrasing_intents:
  - id: launches_launches_get
    intent: List upcoming rocket launches
    question: What rocket launches are coming up this week?
  phrasing_ops: 1
  slug: dynamicfeed-ai-launches-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Macro API from Dynamic Feed — 1 operation(s) for macro.
  name: Dynamic Feed Macro API
  phrasing_intents:
  - id: global_macro_macro_get
    intent: Get macro indicators for a country
    question: What is Brazil's latest inflation rate?
  phrasing_ops: 1
  slug: dynamicfeed-ai-macro-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Market Hours API from Dynamic Feed — 1 operation(s) for market hours.
  name: Dynamic Feed Market Hours API
  phrasing_intents:
  - id: market_hours_market_hours_get
    intent: Check whether a market is open
    question: Is the London Stock Exchange open right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-market-hours-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Models API from Dynamic Feed — 1 operation(s) for models.
  name: Dynamic Feed Models API
  phrasing_intents:
  - id: models_models_get
    intent: Search AI models by price and context
    question: Which AI model is cheapest per million input tokens with vision support?
  phrasing_ops: 1
  slug: dynamicfeed-ai-models-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Movers API from Dynamic Feed — 1 operation(s) for movers.
  name: Dynamic Feed Movers API
  phrasing_intents:
  - id: movers_movers_get
    intent: List the biggest market movers
    question: What are the biggest crypto gainers in the last 24 hours?
  phrasing_ops: 1
  slug: dynamicfeed-ai-movers-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Natural Events API from Dynamic Feed — 1 operation(s) for natural events.
  name: Dynamic Feed Natural Events API
  phrasing_intents:
  - id: natural_events_natural_events_get
    intent: List active natural events worldwide
    question: What natural events are happening on Earth right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-natural-events-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The News API from Dynamic Feed — 1 operation(s) for news.
  name: Dynamic Feed News API
  phrasing_intents:
  - id: news_news_get
    intent: Get the latest AI news and releases
    question: What has been announced in AI news today?
  phrasing_ops: 1
  slug: dynamicfeed-ai-news-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Orbital Datacenters API from Dynamic Feed — 1 operation(s) for orbital datacenters.
  name: Dynamic Feed Orbital Datacenters API
  phrasing_intents:
  - id: orbital_datacenters_orbital_datacenters_get
    intent: List data centers in orbit
    question: Which AI compute spacecraft are in orbit today?
  phrasing_ops: 1
  slug: dynamicfeed-ai-orbital-datacenters-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Rates API from Dynamic Feed — 1 operation(s) for rates.
  name: Dynamic Feed Rates API
  phrasing_intents:
  - id: rates_rates_get
    intent: Get live US benchmark interest rates
    question: What is the current fed funds rate?
  phrasing_ops: 1
  slug: dynamicfeed-ai-rates-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Reality Check API from Dynamic Feed — 1 operation(s) for reality check.
  name: Dynamic Feed Reality Check API
  phrasing_intents:
  - id: reality_check_ep_reality_check_get
    intent: Fact-check a statement against live data
    question: Is it true that BTC is at $90,000 right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-reality-check-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Recalls API from Dynamic Feed — 1 operation(s) for recalls.
  name: Dynamic Feed Recalls API
  phrasing_intents:
  - id: recalls_recalls_get
    intent: Search US product recalls
    question: Has this brand of peanut butter been recalled?
  phrasing_ops: 1
  slug: dynamicfeed-ai-recalls-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The robot API from Dynamic Feed — 10 operation(s) for robot.
  name: Dynamic Feed Robot API
  phrasing_intents:
  - id: v1_anchor_daily_v1_anchor_daily_get
    intent: Get the RFC 3161 anchor for a day's snapshot
    question: Is each day's world-state snapshot timestamped so I can prove what was reported?
  - id: v1_awareness_v1_awareness_post
    intent: Get a go/no-go verdict for a robot at a location
    question: Can one call tell my robot whether it is safe to operate at a location?
  - id: v1_preflight_v1_preflight_post
    intent: Run a drone pre-flight safety check
    question: Is it safe to fly my drone here right now given wind, air quality and space weather?
  - id: v1_road_v1_road_post
    intent: Check road hazards for an autonomous vehicle
    question: Are there weather or earthquake hazards along my autonomous vehicle's route?
  - id: v1_humanoid_v1_humanoid_post
    intent: Run a humanoid robot pre-operation check
    question: Is it safe for my humanoid robot to work among people given wind and icy ground?
  - id: v1_marine_v1_marine_post
    intent: Run a marine vessel pre-operation check
    question: Is wave height too high for my uncrewed surface vessel to operate today?
  - id: v1_robot_receipt_v1_robot_receipt_post
    intent: Witness a robot decision as a black-box receipt
    question: Can I record a signed black-box receipt of what my robot was told when it acted?
  - id: v1_robot_receipt_sample_v1_robot_receipt_sample_get
    intent: Get a sample robot decision receipt
    question: What does a robot black-box receipt look like?
  phrasing_ops: 10
  slug: dynamicfeed-ai-robot-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Sanctions API from Dynamic Feed — 1 operation(s) for sanctions.
  name: Dynamic Feed Sanctions API
  phrasing_intents:
  - id: sanctions_screen_sanctions_get
    intent: Screen a name against sanctions lists
    question: Is this company on the US or UK sanctions list?
  phrasing_ops: 1
  slug: dynamicfeed-ai-sanctions-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Satellite API from Dynamic Feed — 1 operation(s) for satellite.
  name: Dynamic Feed Satellite API
  phrasing_intents:
  - id: satellite_satellite_get
    intent: Locate a satellite by NORAD id
    question: Where is the Hubble telescope right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-satellite-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Satellites API from Dynamic Feed — 1 operation(s) for satellites.
  name: Dynamic Feed Satellites API
  phrasing_intents:
  - id: satellites_satellites_get
    intent: Browse satellite constellations
    question: How many Starlink satellites are in the catalog and at what altitude?
  phrasing_ops: 1
  slug: dynamicfeed-ai-satellites-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Sec Filings API from Dynamic Feed — 1 operation(s) for sec filings.
  name: Dynamic Feed Sec Filings API
  phrasing_intents:
  - id: sec_filings_sec_filings_get
    intent: List recent SEC filings for a company
    question: What has Nvidia filed with the SEC recently?
  phrasing_ops: 1
  slug: dynamicfeed-ai-sec-filings-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The security API from Dynamic Feed — 1 operation(s) for security.
  name: Dynamic Feed Security API
  phrasing_intents:
  - id: package_health_ep_package_health_get
    intent: Check a package's health and security posture
    question: Should I depend on this npm package given its Scorecard and advisories?
  phrasing_ops: 1
  slug: dynamicfeed-ai-security-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Servers API from Dynamic Feed — 1 operation(s) for servers.
  name: Dynamic Feed Servers API
  phrasing_intents:
  - id: servers_servers_get
    intent: Search the MCP server registry
    question: Which MCP servers can I use for database access?
  phrasing_ops: 1
  slug: dynamicfeed-ai-servers-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Shipping API from Dynamic Feed — 1 operation(s) for shipping.
  name: Dynamic Feed Shipping API
  phrasing_intents:
  - id: shipping_ep_shipping_get
    intent: Track shipping chokepoints, ports and vessels
    question: How many ships transited the Suez Canal yesterday?
  phrasing_ops: 1
  slug: dynamicfeed-ai-shipping-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Signals API from Dynamic Feed — 1 operation(s) for signals.
  name: Dynamic Feed Signals API
  phrasing_intents:
  - id: signals_signals_get
    intent: Get derived volatility signals for a symbol
    question: How volatile has ETH been over the last day?
  phrasing_ops: 1
  slug: dynamicfeed-ai-signals-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Signup API from Dynamic Feed — 1 operation(s) for signup.
  name: Dynamic Feed Signup API
  phrasing_intents:
  - id: signup_signup_post
    intent: Get a free API key
    question: Can I get a free API key instantly?
  phrasing_ops: 1
  slug: dynamicfeed-ai-signup-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Space Weather API from Dynamic Feed — 1 operation(s) for space weather.
  name: Dynamic Feed Space Weather API
  phrasing_intents:
  - id: space_weather_space_weather_get
    intent: Get the current space weather
    question: Is there a geomagnetic storm right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-space-weather-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Sports API from Dynamic Feed — 2 operation(s) for sports.
  name: Dynamic Feed Sports API
  phrasing_intents:
  - id: sports_sports_get
    intent: Measure global attention for a sporting event
    question: How much global attention is the World Cup getting by language?
  - id: worldcup_route_worldcup_get
    intent: Get 2026 World Cup fixtures and results
    question: What are the 2026 World Cup fixtures and final scores so far?
  phrasing_ops: 2
  slug: dynamicfeed-ai-sports-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Status API from Dynamic Feed — 1 operation(s) for status.
  name: Dynamic Feed Status API
  phrasing_intents:
  - id: status_status_get
    intent: Check live status of AI and dev services
    question: Are any AI services down right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-status-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Tides API from Dynamic Feed — 1 operation(s) for tides.
  name: Dynamic Feed Tides API
  phrasing_intents:
  - id: tides_ep_tides_get
    intent: Get tides for a US coastal station
    question: When is the next high tide in San Francisco?
  phrasing_ops: 1
  slug: dynamicfeed-ai-tides-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Time API from Dynamic Feed — 1 operation(s) for time.
  name: Dynamic Feed Time API
  phrasing_intents:
  - id: time_ep_time_get
    intent: Get the current time in a timezone
    question: What time is it in New York right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-time-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Treasury Yields API from Dynamic Feed — 1 operation(s) for treasury yields.
  name: Dynamic Feed Treasury Yields API
  phrasing_intents:
  - id: treasury_yields_treasury_yields_get
    intent: Get the US Treasury yield curve
    question: What is the 10-year Treasury yield today?
  phrasing_ops: 1
  slug: dynamicfeed-ai-treasury-yields-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The verified facts API from Dynamic Feed — 4 operation(s) for verified facts.
  name: Dynamic Feed verified facts API
  phrasing_intents:
  - id: v1_state_of_mcp_v1_state_of_mcp_get
    intent: Get the signed State of MCP census
    question: How many MCP servers exist right now, and how many are remote or keyless?
  - id: v1_state_of_mcp_trend_v1_state_of_mcp_trend_get
    intent: Get State of MCP growth over time
    question: How has the number of MCP servers grown over recent weeks?
  - id: v1_facts_v1_facts_get
    intent: Get a verified fact via GET
    question: Can I get any tool's value as a canonical fact with an honest verification block?
  - id: postV1Facts
    intent: Request a verified fact via POST
    question: Can I post a JSON request to the verified-fact layer instead of using GET?
  - id: v1_answer_v1_answer_get
    intent: Get a signed answer with receipts via GET
    question: Can I ask a factual question and get a signed answer with its full evidence chain?
  - id: postV1Answer
    intent: Submit premises for a signed answer via POST
    question: Can I post structured premises and get per-premise verdicts in one signed answer?
  phrasing_ops: 6
  slug: dynamicfeed-ai-verified-facts-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Versions API from Dynamic Feed — 1 operation(s) for versions.
  name: Dynamic Feed Versions API
  phrasing_intents:
  - id: versions_versions_get
    intent: Look up latest versions and end-of-life dates
    question: What is the latest version of Python?
  phrasing_ops: 1
  slug: dynamicfeed-ai-versions-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Volcanoes API from Dynamic Feed — 1 operation(s) for volcanoes.
  name: Dynamic Feed Volcanoes API
  phrasing_intents:
  - id: volcanoes_ep_volcanoes_get
    intent: Check US volcano alert levels
    question: Are any US volcanoes at an elevated alert level right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-volcanoes-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Water Levels API from Dynamic Feed — 1 operation(s) for water levels.
  name: Dynamic Feed Water Levels API
  phrasing_intents:
  - id: water_levels_water_levels_get
    intent: Get real-time US river levels
    question: Are rivers in Texas rising right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-water-levels-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Weather Alerts API from Dynamic Feed — 1 operation(s) for weather alerts.
  name: Dynamic Feed Weather Alerts API
  phrasing_intents:
  - id: weather_alerts_weather_alerts_get
    intent: List active US weather alerts
    question: Are there any tornado warnings right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-weather-alerts-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Weather API from Dynamic Feed — 3 operation(s) for weather.
  name: Dynamic Feed Weather API
  phrasing_intents:
  - id: weather_weather_get
    intent: Get current weather for a place
    question: What is the weather like in Tokyo right now?
  - id: v1_openweather_current_v1_openweather_current_get
    intent: Get current weather via the legacy alias
    question: Does the old openweather current-conditions path still work for existing integrations?
  - id: v1_openweather_forecast_v1_openweather_forecast_get
    intent: Get a forecast via the legacy alias
    question: Does the old openweather forecast path still return a forecast?
  phrasing_ops: 3
  slug: dynamicfeed-ai-weather-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Whats New API from Dynamic Feed — 1 operation(s) for whats new.
  name: Dynamic Feed Whats New API
  phrasing_intents:
  - id: whats_new_ep_whats_new_get
    intent: Catch up on what changed since a cutoff
    question: What has changed in the world since my training cutoff?
  phrasing_ops: 1
  slug: dynamicfeed-ai-whats-new-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The Wildfires API from Dynamic Feed — 1 operation(s) for wildfires.
  name: Dynamic Feed Wildfires API
  phrasing_intents:
  - id: wildfires_wildfires_get
    intent: List active US wildfires
    question: What are the largest active wildfires in California?
  phrasing_ops: 1
  slug: dynamicfeed-ai-wildfires-api
- baseURL: https://dynamicfeed.ai/mcp
  baseurl_source: declared
  description: The World Pulse API from Dynamic Feed — 1 operation(s) for world pulse.
  name: Dynamic Feed World Pulse API
  phrasing_intents:
  - id: world_pulse_ep_world_pulse_get
    intent: Get a live cross-domain world digest
    question: What is happening on Earth right now?
  phrasing_ops: 1
  slug: dynamicfeed-ai-world-pulse-api
artifact_total: 101
asyncapis:
- description: ''
  name: Dynamicfeed Ai Webhooks
  slug: dynamicfeed-ai-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/dynamicfeed-ai/rate-limits/dynamicfeed-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dynamicfeed-ai-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/dynamicfeed-ai/overlays/dynamicfeed-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dynamicfeed-ai-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/dynamicfeed-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/security/dynamicfeed-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dynamicfeed-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/security/dynamicfeed-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dynamicfeed-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/security/dynamicfeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dynamicfeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dynamicfeed.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://dynamicfeed.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dynamicfeed.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dynamicfeed.ai/connect
- group: start
  title: ''
  type: GettingStarted
  url: https://dynamicfeed.ai/connect
- group: other
  title: ''
  type: Playground
  url: https://dynamicfeed.ai/playground
- group: start
  title: ''
  type: Console
  url: https://dynamicfeed.ai/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://dynamicfeed.ai/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://dynamicfeed.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dynamicfeed.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dynamicfeed.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://dynamicfeed.ai/uptime
- group: operate
  title: ''
  type: StatusPage
  url: https://dynamicfeed.ai/status.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fluxdyne
- group: auth
  title: ''
  type: TrustCenter
  url: https://dynamicfeed.ai/trust
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://dynamicfeed.ai/security/advisories
- group: other
  title: ''
  type: ParentCompany
  url: https://fluxdyne.com
- group: agent
  href: https://artifacts.apis.io/dynamicfeed-ai/llms/dynamicfeed-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dynamicfeed-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://dynamicfeed.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/dynamicfeed-ai/well-known/dynamicfeed-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dynamicfeed-ai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/well-known/dynamicfeed-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dynamicfeed-ai-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: https://dynamicfeed.ai/.well-known/security.txt
- group: other
  href: https://artifacts.apis.io/dynamicfeed-ai/well-known/dynamicfeed-ai-ai-catalog.json
  title: ''
  type: AICatalog
  url: well-known/dynamicfeed-ai-ai-catalog.json
- group: build
  href: https://artifacts.apis.io/dynamicfeed-ai/well-known/dynamicfeed-ai-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/dynamicfeed-ai-ai-plugin.json
- group: build
  href: https://artifacts.apis.io/dynamicfeed-ai/packages/dynamicfeed-ai-packages.yml
  title: ''
  type: Packages
  url: packages/dynamicfeed-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/dynamicfeed-ai/packages/dynamicfeed-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/dynamicfeed-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/dynamicfeed-ai/cli/dynamicfeed-ai-cli.yml
  title: ''
  type: CLI
  url: cli/dynamicfeed-ai-cli.yml
- group: design
  href: https://artifacts.apis.io/dynamicfeed-ai/conformance/dynamicfeed-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dynamicfeed-ai-conformance.yml
- group: design
  href: https://artifacts.apis.io/dynamicfeed-ai/lifecycle/dynamicfeed-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dynamicfeed-ai-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/dynamicfeed-ai/plans/dynamicfeed-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dynamicfeed-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dynamicfeed-ai/components/dynamicfeed-ai-components.yml
  title: ''
  type: Components
  url: components/dynamicfeed-ai-components.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://dynamicfeed.ai/privacy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://dynamicfeed.ai/privacy
- group: other
  href: https://artifacts.apis.io/dynamicfeed-ai/regulatory/dynamicfeed-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/dynamicfeed-ai-regulatory-posture.yml
- group: other
  title: ''
  type: OpenDataset
  url: https://dynamicfeed.ai/dataset
- group: other
  title: ''
  type: X402
  url: https://dynamicfeed.ai/v1/pro/catalog
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/authentication/dynamicfeed-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dynamicfeed-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dynamicfeed-ai/security/dynamicfeed-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dynamicfeed-ai-vulnerability-disclosure.yml
created: '2026-09-19'
description: 'Dynamic Feed, a product of Fluxdyne Pty Ltd (Australia), is a live-data and machine-evidence layer for AI agents and robots: 94 read-only tools across 20 domains (weather and air quality, natural hazards, space weather and satellite positions, CVEs and actively-exploited vulnerabilities, software versions and EOL, sanctions and Federal Register, shipping, macro and rates, AI-model pricing and provider latency) drawn from named public sources such as NASA, NOAA, USGS, CISA, OFAC and the World Bank plus its own measurements. Every response carries a provenance and freshness envelope and a detached Ed25519 signature (DF-VERIFY/1) verifiable offline against published keys. The same tool registry is served three ways from one host: a keyless MCP server at /mcp (Streamable HTTP, protocol 2025-06-18), an A2A 1.0 agent at /a2a with a conformant signed agent card, and a REST API published as OpenAPI 3.1 with a keyless 20-call batch endpoint. A /v1 surface adds robot go/caution/no-go
  awareness verdicts, RFC 3161 anchoring, signed transaction/inference/robot/eval receipts on an append-only notary log with daily checkpoints, per-key watchlists, HMAC-signed change webhooks and an SSE stream. Paid access is machine-native via x402 (HTTP 402, USDC on Base, 0.001 USDC per call).'
finops:
- has_sources: true
  method: derived
  name: Dynamicfeed Ai Finops
  primary_unit: ''
  service_category: ''
  slug: dynamicfeed-ai-finops
  template: true
image: https://dynamicfeed.ai/df-logo.png
json_schemas:
- name: DF-VERIFY/1 — attestation/v1 profile (parametric trigger)
  property_count: 8
  slug: dynamicfeed-ai-attestation-v1
- name: DF-VERIFY/1 — awareness/v1 profile
  property_count: 13
  slug: dynamicfeed-ai-awareness-v1
- name: DF-VERIFY/1 — delivery-receipt/v1 (proof of delivery for agent commerce)
  property_count: 15
  slug: dynamicfeed-ai-delivery-receipt-v1
- name: Dynamic Feed eval-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-eval-receipt-v1
- name: DF-VERIFY/1 — GroundTruthReceipt Verifiable Credential profile
  property_count: 7
  slug: dynamicfeed-ai-ground-truth-vc-v1
- name: Dynamic Feed — inference-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-inference-receipt-v1
- name: DF-VERIFY/1 — intensity/v1 profile (parametric intensity-at-location)
  property_count: 14
  slug: dynamicfeed-ai-intensity-v1
- name: OKF reliability object (v1 draft)
  property_count: 12
  slug: dynamicfeed-ai-okf-reliability-v1
- name: DF-VERIFY/1 — proxy-witness/v1 profile (receipts for any API)
  property_count: 8
  slug: dynamicfeed-ai-proxy-witness-v1
- name: DF-VERIFY/1 — receipt/v1 profile
  property_count: 6
  slug: dynamicfeed-ai-receipt-v1
- name: Dynamic Feed — robot-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-robot-receipt-v1
- name: Dynamicfeed Ai Schemas Index
  property_count: 0
  slug: dynamicfeed-ai-schemas-index
- name: DF-VERIFY/1 — station-receipt/v1 profile (We Sign Your Station)
  property_count: 9
  slug: dynamicfeed-ai-station-receipt-v1
- name: DF-VERIFY/1 — trigger-receipt/v1 profile (parametric catastrophe settlement)
  property_count: 11
  slug: dynamicfeed-ai-trigger-receipt-v1
- name: Dynamic Feed Trust Receipt v1 envelope
  property_count: 3
  slug: dynamicfeed-ai-trust-receipt-v1
- name: Dynamic Feed txn-receipt/v1
  property_count: 6
  slug: dynamicfeed-ai-txn-receipt-v1
layout: provider
mcp_servers:
- description: Dynamic Feed runs ONE hosted, keyless MCP server at https://dynamicfeed.ai/mcp (Streamable HTTP, with legacy HTTP+SSE auto-detected on the same URL and explicit at /sse) exposing 94 read-only live-dat
  name: Dynamic Feed MCP Server
  slug: dynamicfeed-ai-mcp-yml
modified: '2026-09-19'
name: Dynamic Feed
nav: Providers
network: true
overview: 'Dynamic Feed publishes 71 API contracts indexed on the [APIs.io](https://apis.io/) network, including Advisories API, Agent API, Agent Stats API, and 68 more. Tagged areas include Live Data, AI Agents, MCP, A2A, and Agent-Native.


  The Dynamic Feed catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dynamic Feed''s developer surface includes documentation, API reference, getting-started guide, developer console, signup flow, pricing, CLI, and 37 more developer resources.'
plans:
- name: Dynamicfeed Ai Plans Pricing
  plan_count: 4
  slug: dynamicfeed-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Dynamicfeed Ai Rate Limits
  slug: dynamicfeed-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Dynamic Feed API Rules
  rule_count: 51
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 11
  slug: dynamicfeed-ai-rules
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 72.5
    catalog_earned_first_party: 24.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.1
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 60.1
    developer_ergonomics: 50.6
    discoverability: 81.7
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 71.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 68
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dynamicfeed-ai/dynamicfeed-ai-2026-10-11T184819.png
security:
- kind: authentication
  name: Dynamicfeed Ai Authentication
  slug: dynamicfeed-ai-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Dynamicfeed Ai Domain Security
  slug: dynamicfeed-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dynamicfeed Ai Vulnerability Disclosure
  slug: dynamicfeed-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Dynamicfeed Ai Trust Center
  slug: dynamicfeed-ai-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: dynamicfeed-ai-robot-awareness
  slug: dynamicfeed-ai-robot-awareness
- name: dynamicfeed-ai-signed-receipts
  slug: dynamicfeed-ai-signed-receipts
- name: dynamicfeed-ai-verify-before-answer
  slug: dynamicfeed-ai-verify-before-answer
- name: dynamicfeed-ai-watch-and-notify
  slug: dynamicfeed-ai-watch-and-notify
slug: dynamicfeed-ai
tags:
- Live Data
- AI Agents
- MCP
- A2A
- Agent-Native
- Provenance
- Weather
- Natural Hazards
- Vulnerabilities
- Sanctions
- Space
- Robotics
- x402
- Receipts
- Notary
- Australia
website: https://dynamicfeed.ai/
---
