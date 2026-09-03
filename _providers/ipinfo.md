---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ipinfo Agentic Access
  operation_count: 53
  slug: ipinfo-agentic-access
  summary_line: 53 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Abuse Contact API.
  name: IPinfo abuse API
  slug: ipinfo-abuse-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: ASN API.
  name: IPinfo asn API
  slug: ipinfo-asn-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IP to Phone Carrier Detection API.
  name: IPinfo carrier API
  slug: ipinfo-carrier-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IP to Company API.
  name: IPinfo company API
  slug: ipinfo-company-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Hosted Domains API.
  name: IPinfo domains API
  slug: ipinfo-domains-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: General API.
  name: IPinfo general API
  slug: ipinfo-general-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IPinfo Core API - Core IP information service.
  name: IPinfo ipinfo core API
  slug: ipinfo-ipinfo-core-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IPinfo Lite API - IPinfo's free API service for country and ASN information.
  name: IPinfo ipinfo lite API
  slug: ipinfo-ipinfo-lite-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IPinfo Max API - Most comprehensive IP intelligence with residential proxy detection.
  name: IPinfo ipinfo max API
  slug: ipinfo-ipinfo-max-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IPinfo Plus API - Enhanced IP information service with mobile and anonymity detection.
  name: IPinfo ipinfo plus API
  slug: ipinfo-ipinfo-plus-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IPinfo Places API - Building-level IP intelligence for physical locations.
  name: IPinfo places API
  slug: ipinfo-places-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Privacy Detection Standard API.
  name: IPinfo privacy detection API
  slug: ipinfo-privacy-detection-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Privacy Detection Extended API with detailed methodologies.
  name: IPinfo privacy detection extended API
  slug: ipinfo-privacy-detection-extended-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IP Ranges API.
  name: IPinfo ranges API
  slug: ipinfo-ranges-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Residential Proxy Detection API.
  name: IPinfo residential proxy detection API
  slug: ipinfo-residential-proxy-detection-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: Single info API.
  name: IPinfo single API
  slug: ipinfo-single-api
- baseURL: https://api.ipinfo.io
  baseurl_source: declared
  description: IP WHOIS API
  name: IPinfo whois API
  slug: ipinfo-whois-api
arazzos:
- description: Resolve an IP to its abuse contact and the domains hosted on it.
  name: IPinfo Abuse Contact and Hosted Domains
  slug: ipinfo-abuse-reporting-workflow
- description: Verify token access, then pull ASN detail and the domain ranges behind it.
  name: IPinfo ASN Prefix Reconnaissance
  slug: ipinfo-asn-prefix-recon-workflow
- description: Bulk-enrich a list of IPs, then pull the full record for one focus IP.
  name: IPinfo Batch Enrich then Detail
  slug: ipinfo-batch-then-detail-workflow
- description: Resolve an IP address to its full record and then to the company operating it.
  name: IPinfo IP to Operating Company
  slug: ipinfo-ip-to-company-workflow
- description: Discover the caller's own public IP and then pull full IP intelligence for it.
  name: IPinfo Enrich My Current IP
  slug: ipinfo-my-ip-enrichment-workflow
- description: Generate a summary report for a list of IPs, then a map visualization for them.
  name: IPinfo Summarize and Map IP Addresses
  slug: ipinfo-summarize-and-map-workflow
- description: Screen an IP for privacy/anonymizer signals and confirm residential proxy use.
  name: IPinfo IP Threat Screening
  slug: ipinfo-threat-screening-workflow
artifact_total: 181
collections:
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse API
  slug: postman-ipinfo-abuse-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse asn API
  slug: postman-ipinfo-asn-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse carrier API
  slug: postman-ipinfo-carrier-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse company API
  slug: postman-ipinfo-company-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse domains API
  slug: postman-ipinfo-domains-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse general API
  slug: postman-ipinfo-general-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse ipinfo core API
  slug: postman-ipinfo-ipinfo-core-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse ipinfo lite API
  slug: postman-ipinfo-ipinfo-lite-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse ipinfo max API
  slug: postman-ipinfo-ipinfo-max-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse ipinfo plus API
  slug: postman-ipinfo-ipinfo-plus-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse places API
  slug: postman-ipinfo-places-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse privacy detection API
  slug: postman-ipinfo-privacy-detection-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse privacy detection extended API
  slug: postman-ipinfo-privacy-detection-extended-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse ranges API
  slug: postman-ipinfo-ranges-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse residential proxy detection API
  slug: postman-ipinfo-residential-proxy-detection-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse single API
  slug: postman-ipinfo-single-api
- collection_type: postman
  name: IPinfo.io OpenAPI Specification abuse whois API
  slug: postman-ipinfo-whois-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse API
  slug: open-ipinfo-abuse-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse asn API
  slug: open-ipinfo-asn-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse carrier API
  slug: open-ipinfo-carrier-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse company API
  slug: open-ipinfo-company-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse domains API
  slug: open-ipinfo-domains-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse general API
  slug: open-ipinfo-general-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse ipinfo core API
  slug: open-ipinfo-ipinfo-core-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse ipinfo lite API
  slug: open-ipinfo-ipinfo-lite-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse ipinfo max API
  slug: open-ipinfo-ipinfo-max-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse ipinfo plus API
  slug: open-ipinfo-ipinfo-plus-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse places API
  slug: open-ipinfo-places-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse privacy detection API
  slug: open-ipinfo-privacy-detection-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse privacy detection extended API
  slug: open-ipinfo-privacy-detection-extended-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse ranges API
  slug: open-ipinfo-ranges-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse residential proxy detection API
  slug: open-ipinfo-residential-proxy-detection-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse single API
  slug: open-ipinfo-single-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification abuse whois API
  slug: open-ipinfo-whois-api
- collection_type: open
  name: IPinfo.io OpenAPI Specification
  slug: open-ipinfo
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ipinfo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ipinfo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipinfo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ipinfo-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-abuse-reporting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-asn-prefix-recon-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-batch-then-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-ip-to-company-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-my-ip-enrichment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-summarize-and-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ipinfo-threat-screening-workflow.yml
- group: build
  title: ''
  type: Packages
  url: packages/ipinfo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ipinfo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ipinfo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ipinfo-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ipinfo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/ipinfo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ipinfo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ipinfo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ipinfo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ipinfo-data-model.yml
- group: build
  title: IPinfo CLI command surface
  type: CLI
  url: cli/ipinfo-cli.yml
- group: company
  title: ''
  type: Website
  url: https://ipinfo.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ipinfo.io/developers
- group: start
  title: ''
  type: Signup
  url: https://ipinfo.io/signup
- group: start
  title: ''
  type: Login
  url: https://ipinfo.io/login
- group: commercial
  title: ''
  type: Pricing
  url: https://ipinfo.io/pricing
- group: start
  title: Dashboard
  type: Console
  url: https://ipinfo.io/account
- group: company
  title: ''
  type: Blog
  url: https://ipinfo.io/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ipinfo.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ipinfo.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://ipinfo.io/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ipinfo.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ipinfo.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://ipinfo.io/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ipinfo
- group: build
  title: IPinfo CLI
  type: CLI
  url: https://github.com/ipinfo/cli
- group: build
  title: mmdbctl (MMDB File Management CLI)
  type: CLI
  url: https://github.com/ipinfo/mmdbctl
- group: build
  title: Summarize IPs Tool
  type: Tools
  url: https://ipinfo.io/tools/summarize-ips
- group: build
  title: Map IPs Tool
  type: Tools
  url: https://ipinfo.io/tools/map
- group: build
  title: Sample Database Repository
  type: CodeExamples
  url: https://github.com/ipinfo/sample-database
- group: build
  title: Rails Example App
  type: CodeExamples
  url: https://github.com/ipinfo/rails-example
- group: build
  title: Docker Image
  type: CodeExamples
  url: https://github.com/ipinfo/docker
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/ipinfo/main/rules/ipinfo-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ipinfo/main/vocabulary/ipinfo-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ipinfo/main/json-ld/ipinfo-context.jsonld
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: IPinfo is an IP address data and intelligence platform that provides geolocation (country, region, city, coordinates, postal, timezone), ASN data, company association, mobile carrier identification, hosted domains lookup, privacy detection (VPN, proxy, Tor, relay, hosting), residential proxy detection, WHOIS, IP ranges, abuse contacts, and an IP-to-Places product. Data is available via a unified REST API (Lite, Core, Plus, Max, Enterprise tiers), a Batch Enrichment endpoint, and downloadable databases (CSV, MMDB, JSON, Parquet). Authentication uses access tokens via Basic Auth, Bearer Token, or query parameter; dual-stack IPv4/IPv6 endpoints are available.
examples:
- key_count: 6
  name: Ipinfo Abuse Response Example
  slug: ipinfo-abuse-response-example
- key_count: 14
  name: Ipinfo Asn Response Example
  slug: ipinfo-asn-response-example
- key_count: 3
  name: Ipinfo Carrier Response Example
  slug: ipinfo-carrier-response-example
- key_count: 3
  name: Ipinfo Company Response Example
  slug: ipinfo-company-response-example
- key_count: 9
  name: Ipinfo Core Response Example
  slug: ipinfo-core-response-example
- key_count: 4
  name: Ipinfo Domains Response Example
  slug: ipinfo-domains-response-example
- key_count: 15
  name: Ipinfo Full Response Example
  slug: ipinfo-full-response-example
- key_count: 8
  name: Ipinfo Lite Response Example
  slug: ipinfo-lite-response-example
- key_count: 11
  name: Ipinfo Max Response Example
  slug: ipinfo-max-response-example
- key_count: 3
  name: Ipinfo Me Response Example
  slug: ipinfo-me-response-example
- key_count: 6
  name: Ipinfo Places Response Example
  slug: ipinfo-places-response-example
- key_count: 10
  name: Ipinfo Plus Response Example
  slug: ipinfo-plus-response-example
- key_count: 7
  name: Ipinfo Prefix Example
  slug: ipinfo-prefix-example
- key_count: 7
  name: Ipinfo Prefix6 Example
  slug: ipinfo-prefix6-example
- key_count: 16
  name: Ipinfo Privacy Extended Response Example
  slug: ipinfo-privacy-extended-response-example
- key_count: 6
  name: Ipinfo Privacy Response Example
  slug: ipinfo-privacy-response-example
- key_count: 4
  name: Ipinfo Ranges Response Example
  slug: ipinfo-ranges-response-example
- key_count: 4
  name: Ipinfo Residential Proxy Response Example
  slug: ipinfo-residential-proxy-response-example
- key_count: 4
  name: Ipinfo Whois Asn Response Example
  slug: ipinfo-whois-asn-response-example
- key_count: 4
  name: Ipinfo Whois Domain Response Example
  slug: ipinfo-whois-domain-response-example
- key_count: 4
  name: Ipinfo Whois Ip Response Example
  slug: ipinfo-whois-ip-response-example
- key_count: 4
  name: Ipinfo Whois Net Id Response Example
  slug: ipinfo-whois-net-id-response-example
- key_count: 4
  name: Ipinfo Whois Org Response Example
  slug: ipinfo-whois-org-response-example
- key_count: 4
  name: Ipinfo Whois Poc Response Example
  slug: ipinfo-whois-poc-response-example
features:
- description: City, region, country, postal code, coordinates, and timezone for any IP.
  name: IP Geolocation
- description: Autonomous System Number, organization, domain, type, peers, upstreams, downstreams, and prefixes.
  name: ASN Data
- description: Organization name, type, and domain associated with an IP block.
  name: Company Identification
- description: Carrier name, Mobile Country Code (MCC), and Mobile Network Code (MNC).
  name: Mobile Carrier Detection
- description: List of domains hosted on an IP address (up to 1,000 per request).
  name: Hosted Domains
- description: Identifies VPN, proxy, Tor, relay, and hosting provider anonymization services.
  name: Privacy Detection
- description: Detects residential, mobile, and datacenter proxies with last-seen recency.
  name: Residential Proxy Detection
- description: Network administrator address, email, and phone for reporting abuse.
  name: Abuse Contact
- description: WHOIS lookup by Net ID, IP, domain, ASN, organization, or point-of-contact.
  name: WHOIS
- description: Bulk lookup of up to thousands of IPs in a single request.
  name: Batch Enrichment
- description: Daily-refreshed CSV, MMDB, JSON, and Parquet database files.
  name: Database Downloads
- description: Dual-stack service with explicit v4.api.ipinfo.io and v6.api.ipinfo.io endpoints.
  name: IPv4 and IPv6 Support
- description: Request a single field (plaintext) or filtered object (JSON) per lookup.
  name: Field Filtering
- description: High-availability service with 50-200 ms typical response time.
  name: 99.999% Uptime
finops:
- name: Ipinfo Finops
  service_category: Identity + Network Intelligence
  slug: ipinfo-finops
image: https://ipinfo.io/static/images/logo.svg
integrations:
- description: IPinfo Splunk app and lookups for SIEM enrichment.
  name: Splunk
- description: Logstash filter plugin for IPinfo MMDB database enrichment.
  name: Elastic / Logstash
- description: Enrich edge requests with IPinfo data inside Workers.
  name: Cloudflare Workers
- description: Serverless enrichment using IPinfo SDKs and Lambda layers.
  name: AWS Lambda
- description: Bulk database loads of IPinfo data for analytical warehouses.
  name: Snowflake
- description: Use IPinfo enrichment in Datadog dashboards and detection rules.
  name: Datadog
- description: Use IPinfo SDKs (Rails, Node, Python, etc.) in Heroku apps.
  name: Heroku
- description: Official Docker image and Compose files for self-hosted enrichment.
  name: Docker
- description: Install the IPinfo CLI and mmdbctl via Homebrew tap.
  name: Homebrew
json_schemas:
- name: AbuseResponse
  property_count: 6
  slug: ipinfo-abuse-response
- name: AsnResponse
  property_count: 14
  slug: ipinfo-asn-response
- name: CarrierResponse
  property_count: 3
  slug: ipinfo-carrier-response
- name: CompanyResponse
  property_count: 3
  slug: ipinfo-company-response
- name: CoreResponse
  property_count: 9
  slug: ipinfo-core-response
- name: DomainsResponse
  property_count: 4
  slug: ipinfo-domains-response
- name: FullResponse
  property_count: 15
  slug: ipinfo-full-response
- name: LiteResponse
  property_count: 8
  slug: ipinfo-lite-response
- name: MaxResponse
  property_count: 11
  slug: ipinfo-max-response
- name: MeResponse
  property_count: 3
  slug: ipinfo-me-response
- name: PlacesResponse
  property_count: 6
  slug: ipinfo-places-response
- name: PlusResponse
  property_count: 10
  slug: ipinfo-plus-response
- name: Prefix
  property_count: 7
  slug: ipinfo-prefix
- name: Prefix6
  property_count: 7
  slug: ipinfo-prefix6
- name: PrivacyExtendedResponse
  property_count: 16
  slug: ipinfo-privacy-extended-response
- name: PrivacyResponse
  property_count: 6
  slug: ipinfo-privacy-response
- name: RangesResponse
  property_count: 4
  slug: ipinfo-ranges-response
- name: ResidentialProxyResponse
  property_count: 4
  slug: ipinfo-residential-proxy-response
- name: WhoisAsnResponse
  property_count: 4
  slug: ipinfo-whois-asn-response
- name: WhoisDomainResponse
  property_count: 4
  slug: ipinfo-whois-domain-response
- name: WhoisIpResponse
  property_count: 4
  slug: ipinfo-whois-ip-response
- name: WhoisNetIdResponse
  property_count: 4
  slug: ipinfo-whois-net-id-response
- name: WhoisOrgResponse
  property_count: 4
  slug: ipinfo-whois-org-response
- name: WhoisPocResponse
  property_count: 4
  slug: ipinfo-whois-poc-response
json_structures:
- name: Ipinfo Abuse Response Structure
  property_count: 6
  slug: ipinfo-abuse-response-structure
- name: Ipinfo Asn Response Structure
  property_count: 14
  slug: ipinfo-asn-response-structure
- name: Ipinfo Carrier Response Structure
  property_count: 3
  slug: ipinfo-carrier-response-structure
- name: Ipinfo Company Response Structure
  property_count: 3
  slug: ipinfo-company-response-structure
- name: Ipinfo Core Response Structure
  property_count: 9
  slug: ipinfo-core-response-structure
- name: Ipinfo Domains Response Structure
  property_count: 4
  slug: ipinfo-domains-response-structure
- name: Ipinfo Full Response Structure
  property_count: 15
  slug: ipinfo-full-response-structure
- name: Ipinfo Lite Response Structure
  property_count: 8
  slug: ipinfo-lite-response-structure
- name: Ipinfo Max Response Structure
  property_count: 11
  slug: ipinfo-max-response-structure
- name: Ipinfo Me Response Structure
  property_count: 3
  slug: ipinfo-me-response-structure
- name: Ipinfo Places Response Structure
  property_count: 6
  slug: ipinfo-places-response-structure
- name: Ipinfo Plus Response Structure
  property_count: 10
  slug: ipinfo-plus-response-structure
- name: Ipinfo Prefix Structure
  property_count: 7
  slug: ipinfo-prefix-structure
- name: Ipinfo Prefix6 Structure
  property_count: 7
  slug: ipinfo-prefix6-structure
- name: Ipinfo Privacy Extended Response Structure
  property_count: 16
  slug: ipinfo-privacy-extended-response-structure
- name: Ipinfo Privacy Response Structure
  property_count: 6
  slug: ipinfo-privacy-response-structure
- name: Ipinfo Ranges Response Structure
  property_count: 4
  slug: ipinfo-ranges-response-structure
- name: Ipinfo Residential Proxy Response Structure
  property_count: 4
  slug: ipinfo-residential-proxy-response-structure
- name: Ipinfo Whois Asn Response Structure
  property_count: 4
  slug: ipinfo-whois-asn-response-structure
- name: Ipinfo Whois Domain Response Structure
  property_count: 4
  slug: ipinfo-whois-domain-response-structure
- name: Ipinfo Whois Ip Response Structure
  property_count: 4
  slug: ipinfo-whois-ip-response-structure
- name: Ipinfo Whois Net Id Response Structure
  property_count: 4
  slug: ipinfo-whois-net-id-response-structure
- name: Ipinfo Whois Org Response Structure
  property_count: 4
  slug: ipinfo-whois-org-response-structure
- name: Ipinfo Whois Poc Response Structure
  property_count: 4
  slug: ipinfo-whois-poc-response-structure
jsonld:
- class_count: 31
  name: Ipinfo Context
  property_count: 104
  slug: ipinfo-context
layout: provider
mcp_servers:
- description: ''
  name: IPinfo MCP Server
  slug: ipinfo-mcp-server
modified: '2026-06-20'
name: IPinfo
nav: Providers
network: true
overview: 'IPinfo publishes 17 APIs on the [APIs.io](https://apis.io/) network, including abuse API, asn API, carrier API, and 14 more. Tagged areas include IP Intelligence, IP Geolocation, ASN, Privacy Detection, and VPN Detection.


  The IPinfo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IPinfo''s developer surface includes authentication, CLI, signup flow, pricing, developer console, engineering blog, support, and 40 more developer resources.'
plans:
- name: Ipinfo Plans Pricing
  plan_count: 6
  slug: ipinfo-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 9
  name: Ipinfo Rate Limits
  slug: ipinfo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: IPinfo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ipinfo-jsonschema-spectral-rules
- effective_rule_count: 71
  extends:
  - spectral:oas
  name: IPinfo API Rules
  rule_count: 30
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 24
  slug: ipinfo-spectral-rules
score:
  band: exemplar
  composite: 68.9
  coverage:
    artifact_dirs: 29
    catalog_gap: 27.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 33.3
    contract_quality: 70.1
    developer_ergonomics: 92.9
    discoverability: 70.4
    governance: 33.3
    operational_transparency: 42.1
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipinfo/refs/heads/main/screenshots/ipinfo-2026-06-20T183555.png
security:
- kind: authentication
  name: Ipinfo Authentication
  slug: ipinfo-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Ipinfo Domain Security
  slug: ipinfo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ipinfo
solutions:
- description: Free, unlimited tier with country, continent, and ASN attributes.
  name: IPinfo Lite
- description: Paid tier with 16 attributes including city-level geolocation and basic privacy detection.
  name: IPinfo Core
- description: Paid tier with 32 attributes including carrier data and named privacy services.
  name: IPinfo Plus
- description: Paid tier with 35 attributes including residential proxy detection.
  name: IPinfo Max
- description: Custom tier with 40+ attributes, full WHOIS, IP ranges, dedicated account manager.
  name: IPinfo Enterprise
- description: Downloadable IP database in CSV, MMDB, JSON, and Parquet for offline lookups.
  name: IPinfo Database
tags:
- IP Intelligence
- IP Geolocation
- ASN
- Privacy Detection
- VPN Detection
- Threat Intelligence
- Network Data
- Mobile Carrier
- WHOIS
- Public APIs
- Development
use_cases:
- description: Block or flag traffic from VPNs, proxies, Tor, and known abuse sources.
  name: Fraud Prevention
- description: Personalize content, pricing, and language based on visitor country and city.
  name: Geo-Targeted Content
- description: Enforce geographic licensing or regulatory restrictions on content access.
  name: Compliance and Geofencing
- description: Enrich SIEM, SOAR, and EDR events with IP context for faster triage.
  name: Cybersecurity and Threat Intelligence
- description: Attribute conversions, dedupe sessions, and segment by carrier or ASN.
  name: Ad Tech and Marketing Analytics
- description: Add geolocation, ASN, and privacy flags to web, application, and network logs.
  name: Log Enrichment
- description: Identify datacenter and hosting-provider IPs that are likely bots.
  name: Bot Detection
- description: Detect anomalous logins from unusual countries or proxy networks.
  name: Account Takeover Prevention
- description: Surface visitor location and ISP to support agents in real time.
  name: Customer Support Triage
- description: Look up ASN peering, prefixes, and abuse contacts during incident response.
  name: Network Engineering
website: https://ipinfo.io
---
