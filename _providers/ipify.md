---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ipify Agentic Access
  operation_count: 5
  slug: ipify-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: Account balance and credit utilities.
  name: ipify Account API
  slug: ipify-account-api
- description: Resolve an IP, domain, or email to a country, region, city, and ISP.
  name: ipify Geolocation API
  slug: ipify-geolocation-api
- description: Operations that return the caller's public IP address.
  name: ipify IP Address API
  slug: ipify-ip-address-api
artifact_total: 42
collections:
- collection_type: open
  name: ipify IP Geolocation API
  slug: open-ipify-geolocation-api
- collection_type: open
  name: ipify Public IP Address API
  slug: open-ipify-ip-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ipify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ipify-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ipify.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ipify-api (server)
  type: GitHubRepository
  url: https://github.com/rdegges/ipify-api
- group: build
  title: python-ipify
  type: GitHubRepository
  url: https://github.com/rdegges/python-ipify
- group: build
  title: go-ipify
  type: GitHubRepository
  url: https://github.com/rdegges/go-ipify
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ipify-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/ipify-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ipify-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ipify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ipify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ipify-finops.yml
created: '2026-05-28'
description: ipify operates two complementary IP APIs. The free Public IP Address API (api.ipify.org, api6.ipify.org, api64.ipify.org) returns the caller's public IPv4, IPv6, or dual-stack address as plain text, JSON, or JSONP — with no authentication, no rate limit, and no logging. The paid IP Geolocation API (geo.ipify.org), operated by WhoisXML API, resolves an IP, domain, or email to a country/region/city, ISP, and Autonomous System (ASN) profile using credit-metered subscription plans.
examples:
- key_count: 1
  name: Geolocation Api Account Balance Example
  slug: geolocation-api-account-balance-example
- key_count: 5
  name: Geolocation Api Geolocation Response Example
  slug: geolocation-api-geolocation-response-example
- key_count: 1
  name: Ip Api Ip Response Example
  slug: ip-api-ip-response-example
features:
- description: Return the caller's public IPv4, IPv6, or dual-stack address with zero authentication.
  name: Public IP Lookup
- description: Plain text, JSON, or JSONP — pick what the client speaks natively.
  name: Multi-Format Response
- description: Resolve IP, domain, or email to country/region/city, ISP, and ASN.
  name: Credit-Metered Geolocation
- description: Optionally return up to five reverse-DNS associated domains for an IP.
  name: Reverse DNS Lookup
- description: Query remaining credits on the API key in real time.
  name: Account Balance Endpoint
- description: Hard 100 requests/second per API key on the Geolocation API.
  name: 100 req/s Rate Ceiling
- description: The free public IP server is MIT/Unlicense-licensed Go (github.com/rdegges/ipify-api).
  name: Open Source Server
finops:
- name: Ipify Finops
  service_category: IP Intelligence + Geolocation
  slug: ipify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipify.png
integrations:
- description: Geolocation product line is part of WhoisXML API's broader IP/DNS intelligence catalog.
  name: WhoisXML API
- description: Public IP API server (rdegges/ipify-api) is deployed on Heroku.
  name: Heroku
- description: Bash, C, Clojurescript, Crystal, Dart, Elixir, Go, Java, Kotlin, .NET, Node.js, Objective-C, PHP, Python, R, Rust, Swift, Xojo, and more.
  name: 20+ Community Client Libraries
json_schemas:
- name: AccountBalanceResponse
  property_count: 1
  slug: geolocation-api-account-balance
- name: GeolocationResponse
  property_count: 5
  slug: geolocation-api-geolocation-response
- name: IpResponse
  property_count: 1
  slug: ip-api-ip-response
json_structures:
- name: Geolocation Api Account Balance Structure
  property_count: 1
  slug: geolocation-api-account-balance-structure
- name: Geolocation Api Geolocation Response Structure
  property_count: 5
  slug: geolocation-api-geolocation-response-structure
- name: Ip Api Ip Response Structure
  property_count: 1
  slug: ip-api-ip-response-structure
jsonld:
- class_count: 6
  name: Ipify Context
  property_count: 18
  slug: ipify-context
layout: provider
modified: '2026-05-29'
name: ipify
nav: Providers
network: true
overview: 'ipify publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Geolocation API, and IP Address API. Tagged areas include Development, IP Address, Geolocation, IP Intelligence, and Public APIs.


  The ipify catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ipify''s developer surface includes authentication and 13 more developer resources.'
plans:
- name: Ipify Plans Pricing
  plan_count: 6
  slug: ipify-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Ipify Rate Limits
  slug: ipify-rate-limits
rules:
- name: ipify API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ipify-jsonschema-spectral-rules
- name: ipify API Rules
  rule_count: 37
  severity_counts:
    error: 15
    hint: 0
    info: 5
    warn: 17
  slug: ipify-rules
score:
  band: developing
  composite: 46.7
  delta: -7.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.4
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ipify/refs/heads/main/screenshots/ipify-2026-06-20T183551.png
security:
- kind: authentication
  name: Ipify Authentication
  slug: ipify-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ipify Domain Security
  slug: ipify-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ipify
solutions:
- description: Drop-in HTTP call to api.ipify.org with no signup. Best for client-side IP discovery.
  name: Free Public IP Lookup
- description: Credit-metered Geolocation API for backend enrichment of inbound traffic.
  name: Server-Side IP Geolocation
- description: Geolocation API with `reverseIp=1` for associating an IP with up to five domains.
  name: Reverse IP Enrichment
tags:
- Development
- IP Address
- Geolocation
- IP Intelligence
- Public APIs
use_cases:
- description: Bootstrapping cloud instances that need to know their own egress IP.
  name: Cloud Server Provisioning
- description: Configuring SSH/VPN tunnels that need the client's current public IP.
  name: Firewall Tunneling Setup
- description: Personalize banners, currency, or language based on visitor country/city.
  name: Geotargeted Content
- description: Flag suspicious traffic by ASN, ISP, or geographic mismatch.
  name: Fraud Detection
- description: Block or restrict access from disallowed regions or countries.
  name: Compliance Geofencing
- description: Cross-reference IP origin with AS classification (Hosting vs ISP) for traffic scoring.
  name: Bot and Scraping Defense
website: https://www.ipify.org/
---
