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
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Official open-source Model Context Protocol server (Java) exposing 14 WhoisFreaks domain-intelligence tools to MCP-compatible AI clients. Distributed as source and as the whoisfreaks/mcp-server Docker
  name: WhoisFreaks MCP Server
  slug: whoisfreaks-mcp-server
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Account, API key, and usage utilities
  name: WhoisFreaks Account API
  slug: whoisfreaks-account-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Autonomous System Number WHOIS
  name: WhoisFreaks ASN WHOIS API
  slug: whoisfreaks-asn-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: ASN WHOIS database snapshots
  name: WhoisFreaks Databases - ASN WHOIS API
  slug: whoisfreaks-databases-asn-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: DNS database snapshots
  name: WhoisFreaks Databases - DNS API
  slug: whoisfreaks-databases-dns-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Expiring and dropped domain downloads
  name: WhoisFreaks Databases - Expiring & Dropped API
  slug: whoisfreaks-databases-expiring-dropped-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP geolocation database snapshots
  name: WhoisFreaks Databases - IP Geolocation API
  slug: whoisfreaks-databases-ip-geolocation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP security database snapshots
  name: WhoisFreaks Databases - IP Security API
  slug: whoisfreaks-databases-ip-security-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP WHOIS database snapshots
  name: WhoisFreaks Databases - IP WHOIS API
  slug: whoisfreaks-databases-ip-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Newly registered domain downloads
  name: WhoisFreaks Databases - Newly Registered API
  slug: whoisfreaks-databases-newly-registered-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Subdomain database snapshots
  name: WhoisFreaks Databases - Subdomains API
  slug: whoisfreaks-databases-subdomains-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: The Databases - Threat Feed API from WhoisFreaks — 6 operation(s) for databases - threat feed.
  name: WhoisFreaks Databases - Threat Feed API
  slug: whoisfreaks-databases-threat-feed-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: WHOIS database snapshots
  name: WhoisFreaks Databases - WHOIS API
  slug: whoisfreaks-databases-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: DNS lookup APIs (live, historical, reverse, bulk)
  name: WhoisFreaks DNS API
  slug: whoisfreaks-dns-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Check domain availability
  name: WhoisFreaks Domain Availability API
  slug: whoisfreaks-domain-availability-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Real-time domain threat assessment and trust scoring
  name: WhoisFreaks Domain Reputation API
  slug: whoisfreaks-domain-reputation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP geolocation lookup
  name: WhoisFreaks Geolocation API
  slug: whoisfreaks-geolocation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP threat intelligence
  name: WhoisFreaks IP Reputation API
  slug: whoisfreaks-ip-reputation-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: IP address WHOIS
  name: WhoisFreaks IP WHOIS API
  slug: whoisfreaks-ip-whois-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: SSL certificate lookup
  name: WhoisFreaks SSL API
  slug: whoisfreaks-ssl-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Subdomain enumeration
  name: WhoisFreaks Subdomains API
  slug: whoisfreaks-subdomains-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: Detect typo variants of brand domains
  name: WhoisFreaks Typosquatting API
  slug: whoisfreaks-typosquatting-api
- baseURL: https://api.whoisfreaks.com
  baseurl_source: declared
  description: WHOIS lookup APIs (live, historical, reverse, bulk)
  name: WhoisFreaks WHOIS API
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
- group: other
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
  title: ''
  type: Lifecycle
  url: lifecycle/whoisfreaks-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whoisfreaks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/whoisfreaks-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whoisfreaks-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/whoisfreaks-plans.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/whoisfreaks-problem-types.yml
- group: build
  title: ''
  type: Examples
  url: examples/whoisfreaks-code-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/whoisfreaks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/whoisfreaks-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/whoisfreaks-cli.yml
- group: start
  title: ''
  type: Console
  url: sandbox/whoisfreaks-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/whoisfreaks-monitoring-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/whoisfreaks-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/whoisfreaks-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/whoisfreaks-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/whoisfreaks-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whoisfreaks-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://whoisfreaks.com/privacy-policy
- group: operate
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
overview: 'WhoisFreaks publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, ASN WHOIS API, Databases - ASN WHOIS API, and 19 more. Tagged areas include WHOIS, DNS, Domain Intelligence, IP Intelligence / Geolocation, and Cybersecurity / Threat Intelligence.


  The WhoisFreaks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WhoisFreaks'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Whoisfreaks Plans
  plan_count: 5
  slug: whoisfreaks-plans
random_paper: 14
rate_limits:
- limit_count: 4
  name: Whoisfreaks Rate Limits
  slug: whoisfreaks-rate-limits
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 64.9
    developer_ergonomics: 82.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 73.7
  previous_composite: 66.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
website: https://whoisfreaks.com/documentation
---
