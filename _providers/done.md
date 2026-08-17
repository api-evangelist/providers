---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Done Agentic Access
  operation_count: 27
  slug: done-agentic-access
  summary_line: 27 operations · 27 acting · 1 human-in-the-loop
api_count: 27
apis:
- description: Single-page agent-native catalog of the 26 _done pay-per-call utility APIs. Publishes a real llms.txt, a robots.txt, a sitemap.xml and an x402 resource manifest at /.well-known/x402.json listing every
  name: _done Catalog
  slug: done-catalog
- description: Look up the network operator, country, and address block behind any IP address or ASN number. Given an internet address (IP) or a network identification number (ASN), this tool returns who operates th
  name: ASN Lookup
  slug: asn-lookup
- description: 'Checks whether a website''s email branding setup is correct so its logo shows up in inboxes. Checks one or more website addresses to see if they are properly set up to show a brand logo next to emails '
  name: BIMI Checker
  slug: bimi-checker
- description: Send a URL and origin, get back exactly which cross-origin permissions that server grants. Sends a real request to any URL you provide, attaches an Origin header, and reads back all six standard cross
  name: CORS Header Checker
  slug: cors-header-checker
- description: Returns the latest, a specific month's, or a historical range of official US inflation (CPI) figures from BLS . Gives you official United States inflation numbers from the government's BLS Consumer Pr
  name: US CPI Data & Inflation Report
  slug: us-cpi-data-inflation-report
- description: Make a real HTTP request from the cloud and get back the status code, headers, and body instantly. Send an HTTP request to any URL from our servers and receive the full response — including the status
  name: Curl HTTP Request
  slug: curl-http-request
- description: Places an order to have a website submitted to twenty directories, returning a confirmation number to track it. Places an order to have a website submitted to twenty directories that publish a link ba
  name: Directory Submission Lite
  slug: directory-submission-lite
- description: 'Check email security (DMARC) configuration for one or many domains in a single request. Give this tool a list of domain names and it will instantly check each one''s DMARC email security record. DMARC '
  name: Bulk DMARC Record Lookup
  slug: bulk-dmarc-record-lookup
- description: Look up all 13 DNS record types plus full WHOIS registration data for up to 10 domains in one call. Send up to 10 domain names and get back every DNS record type (A, AAAA, MX, CNAME, TXT, NS, PTR, SOA
  name: DNS & WHOIS Lookup
  slug: dns-whois-lookup
- description: Give it a list of domains and get back registration date, expiration date, age, and time remaining — instantly. Send a list of domain names and this tool tells you exactly how old each one is, when it
  name: Domain Age Checker
  slug: domain-age-checker
- description: Check whether 1–10 domain names have an active registration record using the official RDAP protocol. Give this API up to 10 domain names and it will tell you whether each one has a registration record
  name: Domain Availability Checker
  slug: domain-availability-checker
- description: Resolve an ENS name to an Ethereum address, or an address back to its ENS name. Look up an ENS name or an Ethereum address and get back the matching one, automatically figuring out which direction you
  name: ENS Resolver
  slug: ens-resolver
- description: Fetch Hacker News stories by category, or scan all stories/jobs/polls from a specific date, with optional nested comments. This tool reads live information from Hacker News, a popular website where pe
  name: Hacker News Data
  slug: hacker-news-data
- description: Compute cryptographic hashes, HMAC signatures, and checksums — and verify webhook signatures with constant-time comparison. Give this API any text or binary data and it instantly returns its fingerpri
  name: Hashing, HMAC & Checksum Suite
  slug: hashing-hmac-checksum-suite
- description: 'Fetches any web address and returns its response headers, status code, and redirect path. Sends a request to a web address you provide and reports back everything the server said in response: the stat'
  name: HTTP Header Checker
  slug: http-header-checker
- description: Check the live status of up to 10 URLs at once and detect redirects instantly. Give this API a list of up to 10 web addresses and it will visit each one to tell you whether it is working, broken, or r
  name: HTTP Status Code Checker
  slug: http-status-code-checker
- description: One endpoint to validate, repair, format, query, diff, convert, and canonicalize JSON — the most common operation in every agent workflow. Every AI agent and developer runs into broken or confusing JS
  name: JSON Validate, Repair, Convert, Query & Diff
  slug: json-validate-repair-convert-query-diff
- description: 'Converts regular text into leetspeak or decodes leetspeak back into normal readable text. Takes a piece of text and either turns it into leetspeak (swapping some letters for numbers and symbols, like '
  name: Leetspeak Translator
  slug: leetspeak-translator
- description: Get the exact monthly payment and full period-by-period breakdown for any fixed-rate loan — results an AI model cannot reliably compute on its own. Give this API a loan amount, an interest rate, and a
  name: Mortgage & Loan Amortization Calculator
  slug: mortgage-loan-amortization-calculator
- description: Extract text from any image using Tesseract OCR. Send a picture, either as a public web address or as base64-encoded image data, and get back the plain text found inside it. Pay-per-call at $0.01 USDC
  name: OCR Text Extractor
  slug: ocr-text-extractor
- description: 'Send a host and port range, get back a clean list of which ports are open and what services are running on them. Give this API a hostname or IP address and it will try connecting to each port in your '
  name: TCP Port Scanner
  slug: tcp-port-scanner
- description: Turn a list of text, URLs, or any strings into QR code images instantly — one call, many codes. Send a list of texts — website addresses, phone numbers, plain words, WiFi details, anything — and get b
  name: Bulk QR Code Generator
  slug: bulk-qr-code-generator
- description: Capture a screenshot of a fully rendered webpage, including JavaScript-heavy pages. Renders a webpage exactly as a real browser would, including all its scripts and dynamic content, then takes a pictu
  name: Screenshots
  slug: screenshots
- description: 'Fetch a webpage and instantly extract all key SEO fields: title, meta tags, headings, canonical URL, and more. Give this API a web address and it will visit that page, then hand back everything an SEO'
  name: SEO Data Extractor
  slug: seo-data-extractor
- description: Check exactly where your Shopify product ranks when AI shopping assistants like ChatGPT and Gemini search for it. Checks how well a Shopify store's products show up when AI shopping assistants such as
  name: Shopify AI Rank Checker
  slug: shopify-ai-rank-checker
- description: Give it a sitemap.xml link and get back every URL listed in it — including nested sub-sitemaps — with metadata like last modified date and change frequency. Give this API a link to any website's sitem
  name: Sitemap URL Extractor
  slug: sitemap-url-extractor
- description: Checks whether a website or web address is currently reachable and reports how fast it responded. Pay-per-call at $0.01 USDC over x402 on Base or Solana — no account, no API key. OpenAPI 3.1.0; 1 oper
  name: URL Uptime Checker
  slug: url-uptime-checker
artifact_total: 59
collections:
- collection_type: open
  name: ASN Lookup
  slug: open-done-asn-lookup
- collection_type: open
  name: BIMI Checker
  slug: open-done-bimi-checker
- collection_type: open
  name: CORS Header Checker
  slug: open-done-cors-header-checker
- collection_type: open
  name: US CPI Data & Inflation Report
  slug: open-done-cpi-report-us
- collection_type: open
  name: Curl HTTP Request
  slug: open-done-curl-http-request
- collection_type: open
  name: Directory Submission Lite
  slug: open-done-directory-submission-lite
- collection_type: open
  name: Bulk DMARC Record Lookup
  slug: open-done-dmarc-lookup
- collection_type: open
  name: DNS & WHOIS Lookup
  slug: open-done-dns-whois-lookup
- collection_type: open
  name: Domain Age Checker
  slug: open-done-domain-age-checker
- collection_type: open
  name: Domain Availability Checker
  slug: open-done-domain-availability-checker
- collection_type: open
  name: ENS Resolver
  slug: open-done-ens-resolver
- collection_type: open
  name: Hacker News Data
  slug: open-done-hackernews-data
- collection_type: open
  name: Hashing, HMAC & Checksum Suite
  slug: open-done-hash-hmac
- collection_type: open
  name: HTTP Header Checker
  slug: open-done-http-header-checker
- collection_type: open
  name: HTTP Status Code Checker
  slug: open-done-http-status-checker
- collection_type: open
  name: JSON Validate, Repair, Convert, Query & Diff
  slug: open-done-json-suite
- collection_type: open
  name: Leetspeak Translator
  slug: open-done-leetspeak-translator
- collection_type: open
  name: Mortgage & Loan Amortization Calculator
  slug: open-done-mortgage-amortization
- collection_type: open
  name: OCR Text Extractor
  slug: open-done-ocr
- collection_type: open
  name: TCP Port Scanner
  slug: open-done-port-scanner
- collection_type: open
  name: Bulk QR Code Generator
  slug: open-done-qr-code-generator
- collection_type: open
  name: Screenshots
  slug: open-done-screenshots
- collection_type: open
  name: SEO Data Extractor
  slug: open-done-seo-data-extractor
- collection_type: open
  name: Shopify AI Rank Checker
  slug: open-done-shopify-ai-rank-checker
- collection_type: open
  name: Sitemap URL Extractor
  slug: open-done-sitemap-url-extractor
- collection_type: open
  name: URL Uptime Checker
  slug: open-done-url-uptime-checker
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/done-mcp.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://underscoredone.com
- group: docs
  title: ''
  type: Documentation
  url: https://underscoredone.com
- group: docs
  title: ''
  type: APIReference
  url: https://underscoredone.com/#apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/underscoredone
- group: operate
  title: ''
  type: Support
  url: https://forms.gle/5KzuSFH7p8hHtDmz7
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/done-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/done-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/done-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/done-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/done-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/done-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/done-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/done-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/done-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/done-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/done-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/done-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://underscoredone.com/#apis
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/done-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/done-packages.yml
created: '2026-08-10'
description: '_done is an agent-native catalog of 26 single-purpose utility REST APIs — network and DNS lookups, domain intelligence, email-authentication checks, HTTP and SEO inspection, OCR, screenshots, hashing, JSON tooling, web3 resolution and finance calculators. There are no accounts, no signups and no API keys: every call is metered individually at $0.01 in USDC over the x402 protocol, settled on Base Mainnet or Solana Mainnet through the Coinbase CDP facilitator. Each service runs on its own subdomain, exposes a single POST operation, and publishes its own OpenAPI 3.1.0 spec annotated for AI agents with x-ai-instructions, x-guidance, x-pricing and x-402 payment metadata. Discovery is served from /.well-known/x402.json, /llms.txt, robots.txt and sitemap.xml. There is no MCP server, no A2A agent card, no SDK, no changelog, no status page and no published terms of service.'
image: https://underscoredone.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: done-mcp.yml
  slug: done-mcpyml
modified: '2026-08-11'
name: _done
nav: Providers
network: true
overview: '_done publishes 26 APIs on the [APIs.io](https://apis.io/) network, including ASN Lookup, BIMI Checker, CORS Header Checker, and 23 more. Tagged areas include developer-tools, utility-apis, ai-agents, agent-native, and x402.


  _done''s developer surface includes documentation, API reference, support, authentication, code examples, pricing, and 16 more developer resources.'
plans:
- name: Done Plans Pricing
  plan_count: 1
  slug: done-plans-pricing
random_paper: 124
rate_limits:
- limit_count: 0
  name: Done Rate Limits
  slug: done-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 59.7
    developer_ergonomics: 54.3
    discoverability: 57.4
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 38.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Done Authentication
  slug: done-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Done Domain Security
  slug: done-domain-security
  summary_line: TLSv1.3 · DMARC
slug: done
tags:
- developer-tools
- utility-apis
- ai-agents
- agent-native
- x402
- pay-per-call
- web3
- crypto-payments
- dns
- domains
- email-security
- network-security
- seo
- ocr
- data
- fintech-calculators
website: https://underscoredone.com
---
