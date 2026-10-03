---
access_model:
  confidence: high
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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Official open-source Model Context Protocol server (Java) exposing 14 WhoisFreaks domain-intelligence tools to MCP-compatible AI clients. Distributed as source and as the whoisfreaks/mcp-server Docker
  name: WhoisFreaks MCP Server
  slug: whoisfreaks-mcp-server
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Account, API key, and usage utilities
  name: WhoisFreaks Account API
  phrasing_intents:
  - id: rotateApiKey
    intent: Rotate my API key
    question: How do I replace my WhoisFreaks API key with a new one?
  - id: accountUsage
    intent: Check my account credit usage
    question: How many API credits have I used so far?
  - id: databaseFileStatus
    intent: Check freshness of downloadable database files
    question: When were the downloadable database files last updated?
  phrasing_ops: 3
  slug: whoisfreaks-account-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Autonomous System Number WHOIS
  name: WhoisFreaks ASN WHOIS API
  phrasing_intents:
  - id: asnWhois
    intent: Look up WHOIS for an ASN
    question: Who owns a given autonomous system number?
  phrasing_ops: 1
  slug: whoisfreaks-asn-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: ASN WHOIS database snapshots
  name: WhoisFreaks Databases - ASN WHOIS API
  phrasing_intents:
  - id: dbAsnWhois
    intent: Download the ASN WHOIS snapshot
    question: Can I download the full ASN WHOIS database as a file?
  - id: dbAsnWhoisStatus
    intent: Check ASN WHOIS snapshot status
    question: Which ASN WHOIS snapshot dates are available to download?
  phrasing_ops: 2
  slug: whoisfreaks-databases-asn-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: DNS database snapshots
  name: WhoisFreaks Databases - DNS API
  phrasing_intents:
  - id: dbDnsDaily
    intent: Download the daily DNS database update
    question: Where can I download yesterday's changes to the DNS database?
  - id: dbDnsWeekly
    intent: Download the weekly DNS database update
    question: Is there a weekly roll-up of DNS record changes I can pull?
  - id: dbDnsMonthly
    intent: Download the monthly DNS database update
    question: Can I download a full month of DNS record changes in one file?
  phrasing_ops: 3
  slug: whoisfreaks-databases-dns-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Expiring and dropped domain downloads
  name: WhoisFreaks Databases - Expiring & Dropped API
  phrasing_intents:
  - id: dbExpired
    intent: Download the expiring domains file
    question: Where can I get a list of domains that are about to expire?
  - id: dbExpiredCleaned
    intent: Download cleaned WHOIS for expiring domains
    question: Is there a cleaned, normalized WHOIS file for expiring domains?
  - id: dbDropped
    intent: Download the dropped domains file
    question: Where do I download the list of domains that just dropped?
  - id: dbDroppedJson
    intent: List dropped domains as JSON
    question: Can I get dropped domains as a JSON response instead of a file download?
  - id: dbDroppedBacklinks
    intent: Download dropped domains that have backlinks
    question: Which recently dropped domains still have backlinks pointing at them?
  phrasing_ops: 5
  slug: whoisfreaks-databases-expiring-dropped-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP geolocation database snapshots
  name: WhoisFreaks Databases - IP Geolocation API
  phrasing_intents:
  - id: dbIpCountryStatus
    intent: Check IP-to-country snapshot status
    question: Is a new IP to country snapshot available yet?
  - id: dbIpCountry
    intent: Download the IP-to-country snapshot
    question: Can I download a full IP to country mapping database?
  - id: dbIpCityStatus
    intent: Check IP-to-city snapshot status
    question: Has the IP to city database been refreshed recently?
  - id: dbIpCity
    intent: Download the IP-to-city snapshot
    question: Can I download a city-level IP geolocation database for offline use?
  phrasing_ops: 4
  slug: whoisfreaks-databases-ip-geolocation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP security database snapshots
  name: WhoisFreaks Databases - IP Security API
  phrasing_intents:
  - id: dbIpSecurity
    intent: Download the IP security snapshot
    question: Can I download a bulk database of IP security and threat flags?
  - id: dbIpSecurityStatus
    intent: Check IP security snapshot status
    question: Is the latest IP security snapshot available?
  phrasing_ops: 2
  slug: whoisfreaks-databases-ip-security-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP WHOIS database snapshots
  name: WhoisFreaks Databases - IP WHOIS API
  phrasing_intents:
  - id: dbIpWhois
    intent: Download the IP WHOIS snapshot
    question: Can I download WHOIS data for all IP ranges as a file?
  - id: dbIpWhoisStatus
    intent: Check IP WHOIS snapshot status
    question: Is a new IP WHOIS snapshot ready to download?
  phrasing_ops: 2
  slug: whoisfreaks-databases-ip-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Newly registered domain downloads
  name: WhoisFreaks Databases - Newly Registered API
  phrasing_intents:
  - id: dbNewlyGtld
    intent: Download newly registered gTLD domains (CSV)
    question: Where can I download newly registered .com and other gTLD domains?
  - id: dbNewlyCctld
    intent: Download newly registered ccTLD domains (CSV)
    question: Can I download newly registered country-code domains like .de or .uk?
  - id: dbNewlyGtldCleaned
    intent: Download cleaned WHOIS for new gTLD domains
    question: Is there a cleaned WHOIS CSV for newly registered gTLD domains?
  - id: dbNewlyCctldCleaned
    intent: Download cleaned WHOIS for new ccTLD domains
    question: Is there a cleaned WHOIS CSV for newly registered country-code domains?
  - id: dbNewlyGtldJson
    intent: List newly registered gTLD domains as JSON
    question: Can I get new gTLD registrations as JSON instead of a CSV download?
  - id: dbNewlyCctldJson
    intent: List newly registered ccTLD domains as JSON
    question: Can I pull new country-code domain registrations as JSON?
  - id: dbNewlyDns
    intent: Download newly registered domains with DNS
    question: Can I get newly registered domains together with their DNS records?
  phrasing_ops: 7
  slug: whoisfreaks-databases-newly-registered-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Subdomain database snapshots
  name: WhoisFreaks Databases - Subdomains API
  phrasing_intents:
  - id: dbSubdomainsDaily
    intent: Download the daily subdomains database update
    question: Where can I get a daily file of newly discovered subdomains?
  - id: dbSubdomainsWeekly
    intent: Download the weekly subdomains database update
    question: Is there a weekly subdomains database I can sync from?
  - id: dbSubdomainsMonthly
    intent: Download the monthly subdomains database update
    question: Can I pull a monthly bulk file of subdomains?
  phrasing_ops: 3
  slug: whoisfreaks-databases-subdomains-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: The Databases - Threat Feed API from WhoisFreaks — 6 operation(s) for databases - threat feed.
  name: WhoisFreaks Databases - Threat Feed API
  phrasing_intents:
  - id: downloadThreatFeedPhishing
    intent: Download the daily phishing threat feed
    question: Where can I download a daily list of phishing domains?
  - id: downloadThreatFeedPhishingSample
    intent: Download a sample of the phishing threat feed
    question: Is there a free phishing feed sample I can evaluate first?
  - id: downloadThreatFeedMalware
    intent: Download the daily malware threat feed
    question: Where do I get a daily feed of malware-hosting domains?
  - id: downloadThreatFeedMalwareSample
    intent: Download a sample of the malware threat feed
    question: Can I preview the malware feed before subscribing?
  - id: downloadThreatFeedSpam
    intent: Download the daily spam threat feed
    question: Where can I download a daily list of spam domains for blocklisting?
  - id: downloadThreatFeedSpamSample
    intent: Download a sample of the spam threat feed
    question: Is a sample of the spam domain feed available to test with?
  phrasing_ops: 6
  slug: whoisfreaks-databases-threat-feed-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: WHOIS database snapshots
  name: WhoisFreaks Databases - WHOIS API
  phrasing_intents:
  - id: dbWhoisDaily
    intent: Download the daily domain WHOIS database update
    question: Where can I download each day's changed domain WHOIS records?
  - id: dbWhoisWeekly
    intent: Download the weekly domain WHOIS database update
    question: Is there a weekly domain WHOIS database file to keep my copy in sync?
  - id: dbWhoisMonthly
    intent: Download the monthly domain WHOIS database update
    question: Can I download a monthly bulk dump of domain WHOIS records?
  phrasing_ops: 3
  slug: whoisfreaks-databases-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: DNS lookup APIs (live, historical, reverse, bulk)
  name: WhoisFreaks DNS API
  phrasing_intents:
  - id: dnsLive
    intent: Look up current DNS records
    question: What are the current MX and TXT records for a domain?
  - id: dnsHistorical
    intent: Get historical DNS records for a domain
    question: How can I see what DNS records a domain used to have?
  - id: dnsReverse
    intent: Find domains by IP or DNS record value
    question: Which domains point to a given IP address?
  - id: dnsBulk
    intent: Look up DNS for many domains and IPs at once
    question: Can I check DNS records for a hundred domains in one request?
  phrasing_ops: 4
  slug: whoisfreaks-dns-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Check domain availability
  name: WhoisFreaks Domain Availability API
  phrasing_intents:
  - id: domainAvailabilityV2
    intent: Check if a domain is available to register
    question: Is a particular domain name still available to register?
  - id: bulkDomainAvailabilityV2
    intent: Check availability for a batch of domains
    question: Can I check availability for up to 100 domain names in one call?
  phrasing_ops: 2
  slug: whoisfreaks-domain-availability-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Real-time domain threat assessment and trust scoring
  name: WhoisFreaks Domain Reputation API
  phrasing_intents:
  - id: domainReputation
    intent: Assess a domain's threat reputation
    question: Is this domain malicious or safe to trust?
  phrasing_ops: 1
  slug: whoisfreaks-domain-reputation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP geolocation lookup
  name: WhoisFreaks Geolocation API
  phrasing_intents:
  - id: geolocation
    intent: Geolocate an IP address
    question: Where is a given IP address located?
  - id: bulkGeolocation
    intent: Geolocate a batch of IP addresses
    question: Can I geolocate up to 100 IPs in a single request?
  phrasing_ops: 2
  slug: whoisfreaks-geolocation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP threat intelligence
  name: WhoisFreaks IP Reputation API
  phrasing_intents:
  - id: ipReputation
    intent: Check an IP for VPN, proxy, Tor or bot activity
    question: Is this IP address a VPN, proxy or Tor exit node?
  - id: bulkIpReputation
    intent: Check reputation for a batch of IPs
    question: Can I screen up to 100 IP addresses for threats in one request?
  phrasing_ops: 2
  slug: whoisfreaks-ip-reputation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP address WHOIS
  name: WhoisFreaks IP WHOIS API
  phrasing_intents:
  - id: ipWhois
    intent: Look up WHOIS for an IP address
    question: Who is the registered owner of an IP address?
  phrasing_ops: 1
  slug: whoisfreaks-ip-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: SSL certificate lookup
  name: WhoisFreaks SSL API
  phrasing_intents:
  - id: sslLookup
    intent: Inspect a domain's live SSL certificate
    question: When does a website's SSL certificate expire?
  phrasing_ops: 1
  slug: whoisfreaks-ssl-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Subdomain enumeration
  name: WhoisFreaks Subdomains API
  phrasing_intents:
  - id: subdomains
    intent: Find all subdomains of a domain
    question: What subdomains exist under a domain, including nested ones?
  phrasing_ops: 1
  slug: whoisfreaks-subdomains-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Detect typo variants of brand domains
  name: WhoisFreaks Typosquatting API
  phrasing_intents:
  - id: typosquatting
    intent: Find typo variants of a brand domain
    question: Which lookalike domains are typosquatting my brand?
  phrasing_ops: 1
  slug: whoisfreaks-typosquatting-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: WHOIS lookup APIs (live, historical, reverse, bulk)
  name: WhoisFreaks WHOIS API
  phrasing_intents:
  - id: whoisLive
    intent: Look up current WHOIS for a domain
    question: Who currently owns a domain and when does it expire?
  - id: bulkWhois
    intent: Look up WHOIS for many domains at once
    question: Can I run WHOIS on up to 100 domains in one request?
  - id: whoisHistory
    intent: Get a domain's historical WHOIS records
    question: How has a domain's ownership changed over the years?
  - id: whoisReverse
    intent: Find domains by a keyword in WHOIS records
    question: Which domains are registered by a given company or email?
  phrasing_ops: 4
  slug: whoisfreaks-whois-api
artifact_total: 52
asyncapis:
- description: ''
  name: Whoisfreaks Monitoring Webhooks
  slug: whoisfreaks-monitoring-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WhoisFreaks Account API
  slug: open-whoisfreaks-account-api
- collection_type: open
  name: WhoisFreaks ASN WHOIS API
  slug: open-whoisfreaks-asn-whois-api
- collection_type: open
  name: WhoisFreaks Databases - ASN WHOIS API
  slug: open-whoisfreaks-databases-asn-whois-api
- collection_type: open
  name: WhoisFreaks Databases - DNS API
  slug: open-whoisfreaks-databases-dns-api
- collection_type: open
  name: WhoisFreaks Databases - Expiring & Dropped API
  slug: open-whoisfreaks-databases-expiring-dropped-api
- collection_type: open
  name: WhoisFreaks Databases - IP Geolocation API
  slug: open-whoisfreaks-databases-ip-geolocation-api
- collection_type: open
  name: WhoisFreaks Databases - IP Security API
  slug: open-whoisfreaks-databases-ip-security-api
- collection_type: open
  name: WhoisFreaks Databases - IP WHOIS API
  slug: open-whoisfreaks-databases-ip-whois-api
- collection_type: open
  name: WhoisFreaks Databases - Newly Registered API
  slug: open-whoisfreaks-databases-newly-registered-api
- collection_type: open
  name: WhoisFreaks Databases - Subdomains API
  slug: open-whoisfreaks-databases-subdomains-api
- collection_type: open
  name: WhoisFreaks Databases - Threat Feed API
  slug: open-whoisfreaks-databases-threat-feed-api
- collection_type: open
  name: WhoisFreaks Databases - WHOIS API
  slug: open-whoisfreaks-databases-whois-api
- collection_type: open
  name: WhoisFreaks DNS API
  slug: open-whoisfreaks-dns-api
- collection_type: open
  name: WhoisFreaks Domain Availability API
  slug: open-whoisfreaks-domain-availability-api
- collection_type: open
  name: WhoisFreaks Domain Reputation API
  slug: open-whoisfreaks-domain-reputation-api
- collection_type: open
  name: WhoisFreaks Geolocation API
  slug: open-whoisfreaks-geolocation-api
- collection_type: open
  name: WhoisFreaks IP Reputation API
  slug: open-whoisfreaks-ip-reputation-api
- collection_type: open
  name: WhoisFreaks IP WHOIS API
  slug: open-whoisfreaks-ip-whois-api
- collection_type: open
  name: WhoisFreaks SSL API
  slug: open-whoisfreaks-ssl-api
- collection_type: open
  name: WhoisFreaks Subdomains API
  slug: open-whoisfreaks-subdomains-api
- collection_type: open
  name: WhoisFreaks Typosquatting API
  slug: open-whoisfreaks-typosquatting-api
- collection_type: open
  name: WhoisFreaks WHOIS API
  slug: open-whoisfreaks-whois-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.whoisfreaks.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/capabilities/whoisfreaks-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/whoisfreaks-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/WhoisFreaks/whoisfreaks-mcp-server/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/WhoisFreaks/whoisfreaks-mcp-server/releases
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/overlays/whoisfreaks-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/whoisfreaks-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://whoisfreaks.com/documentation
- group: docs
  title: ''
  type: Documentation
  url: https://whoisfreaks.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://whoisfreaks.com/documentation/whois-api
- group: start
  title: ''
  type: GettingStarted
  url: https://whoisfreaks.com/integrations/sdk/python
- group: operate
  title: ''
  type: Support
  url: https://whoisfreaks.com/contact
- group: company
  title: ''
  type: Blog
  url: https://whoisfreaks.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WhoisFreaks
- group: commercial
  title: ''
  type: Pricing
  url: https://whoisfreaks.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://whoisfreaks.com/signup
- group: start
  title: ''
  type: Login
  url: https://whoisfreaks.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://whoisfreaks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://whoisfreaks.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/wf-official/api
- group: operate
  title: ''
  type: StatusPage
  url: https://whoisfreaks.com/uptime-status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/lifecycle/whoisfreaks-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/whoisfreaks-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/authentication/whoisfreaks-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whoisfreaks-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/conventions/whoisfreaks-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whoisfreaks-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/rate-limits/whoisfreaks-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whoisfreaks-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/plans/whoisfreaks-plans.yml
  title: ''
  type: Plans
  url: plans/whoisfreaks-plans.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/errors/whoisfreaks-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whoisfreaks-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/examples/whoisfreaks-code-examples.yml
  title: ''
  type: Examples
  url: examples/whoisfreaks-code-examples.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/packages/whoisfreaks-packages.yml
  title: ''
  type: Packages
  url: packages/whoisfreaks-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/packages/whoisfreaks-packages.yml
  title: ''
  type: SDKs
  url: packages/whoisfreaks-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/cli/whoisfreaks-cli.yml
  title: ''
  type: CLI
  url: cli/whoisfreaks-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/sandbox/whoisfreaks-sandbox.yml
  title: ''
  type: Console
  url: sandbox/whoisfreaks-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/asyncapi/whoisfreaks-monitoring-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/whoisfreaks-monitoring-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/llms/whoisfreaks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whoisfreaks-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/well-known/whoisfreaks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whoisfreaks-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/conformance/whoisfreaks-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whoisfreaks-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/data-model/whoisfreaks-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whoisfreaks-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/security/whoisfreaks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whoisfreaks-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://whoisfreaks.com/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/changelog/whoisfreaks-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/whoisfreaks-changelog.yml
created: '2026-07-29'
description: WhoisFreaks is a domain and IP intelligence provider whose REST API suite covers live WHOIS, historical WHOIS, bulk and reverse WHOIS, IP and ASN WHOIS, live/historical/reverse DNS, domain availability with suggestions, typosquatting discovery, SSL certificate lookup, subdomain enumeration, IP geolocation, IP reputation and domain reputation. Alongside the live lookup APIs it ships bulk downloadable databases (WHOIS, DNS, subdomains, IP geolocation, IP security, ASN, newly registered domains, expiring and dropped domains, and daily phishing/malware/spam threat feeds), brand/domain/registrant monitoring services with email, Telegram and webhook alerts, ten officially maintained OpenAPI-generated SDKs, a Go CLI, an n8n community node, and an open-source MCP server exposing fourteen domain-intelligence tools to AI assistants. Authentication is a single apiKey query parameter across every endpoint.
image: https://whoisfreaks.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: WhoisFreaks MCP Server
  slug: whoisfreaks-mcp-server
modified: '2026-08-09'
name: WhoisFreaks
nav: Providers
network: true
overview: 'WhoisFreaks publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account API, ASN WHOIS API, Databases - ASN WHOIS API, and 20 more. Tagged areas include WHOIS, DNS, Domain Intelligence, IP Intelligence / Geolocation, and Cybersecurity / Threat Intelligence.


  The WhoisFreaks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WhoisFreaks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Whoisfreaks Plans
  plan_count: 5
  slug: whoisfreaks-plans
random_paper: 2
rate_limits:
- limit_count: 4
  name: Whoisfreaks Rate Limits
  slug: whoisfreaks-rate-limits
score:
  band: exemplar
  composite: 67.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 59.4
    developer_ergonomics: 82.7
    discoverability: 73.2
    operational_transparency: 73.7
  previous_composite: 67.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/whoisfreaks/refs/heads/main/screenshots/whoisfreaks-2026-08-17T080443.png
security:
- kind: authentication
  name: Whoisfreaks Authentication
  slug: whoisfreaks-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Whoisfreaks Domain Security
  slug: whoisfreaks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: whoisfreaks
tags:
- WHOIS
- DNS
- Domain Intelligence
- IP Intelligence / Geolocation
- Cybersecurity / Threat Intelligence
- OSINT
- Reverse Lookup
- SSL/Certificate
- Domain Monitoring
- Brand Protection
- Threat Feeds
- Domain Availability
website: https://www.whoisfreaks.com/
---
