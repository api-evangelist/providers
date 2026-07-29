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
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Shodan Agentic Access
  operation_count: 51
  slug: shodan-agentic-access
  summary_line: 51 operations · 12 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: Account, profile, and API plan information.
  name: Shodan Account API
  slug: shodan-account-api
- description: Enterprise bulk data exports.
  name: Shodan Bulk Data API
  slug: shodan-bulk-data-api
- description: The CPE API from Shodan — 1 operation(s) for cpe.
  name: Shodan CPE API
  slug: shodan-cpe-api
- description: The CVE API from Shodan — 2 operation(s) for cve.
  name: Shodan CVE API
  slug: shodan-cve-api
- description: Browse and search saved Shodan queries.
  name: Shodan Directory API
  slug: shodan-directory-api
- description: Forward, reverse, and domain DNS lookups.
  name: Shodan DNS API
  slug: shodan-dns-api
- description: The InternetDB API from Shodan — 1 operation(s) for internetdb.
  name: Shodan InternetDB API
  slug: shodan-internetdb-api
- description: Create and manage alerts on monitored IP ranges.
  name: Shodan Network Alerts API
  slug: shodan-network-alerts-api
- description: Manage notification providers used by alerts.
  name: Shodan Notifiers API
  slug: shodan-notifiers-api
- description: Request crawls of specific IPs, netblocks, or the entire Internet.
  name: Shodan On-Demand Scanning API
  slug: shodan-on-demand-scanning-api
- description: Enterprise organization management.
  name: Shodan Organization API
  slug: shodan-organization-api
- description: Search and lookup endpoints for indexed devices.
  name: Shodan Search Methods API
  slug: shodan-search-methods-api
- description: The Streaming API from Shodan — 5 operation(s) for streaming.
  name: Shodan Streaming API
  slug: shodan-streaming-api
- description: The Trends API from Shodan — 1 operation(s) for trends.
  name: Shodan Trends API
  slug: shodan-trends-api
- description: Helper endpoints for HTTP headers and IP detection.
  name: Shodan Utility API
  slug: shodan-utility-api
arazzos:
- description: Pull the account profile, API plan limits, and the client's own IP.
  name: Shodan Account Overview
  slug: shodan-account-overview-workflow
- description: Create a notifier, attach it via an alert, and arm a trigger for delivery.
  name: Shodan Alert With Notifier
  slug: shodan-alert-with-notifier-workflow
- description: Resolve a product to a CPE, search its CVEs, then pull full CVE details.
  name: Shodan CVEDB Product Vulnerability Enrichment
  slug: shodan-cve-enrichment-workflow
- description: Enumerate a domain's DNS records, resolve a subdomain, and inspect the host.
  name: Shodan Domain Reconnaissance
  slug: shodan-domain-recon-workflow
- description: Pull an IP's free InternetDB record, then detail one of its known CVEs.
  name: Shodan InternetDB Vulnerability Triage
  slug: shodan-internetdb-vuln-triage-workflow
- description: Create a network alert, enable a trigger, verify it, then update the IP set.
  name: Shodan Network Alert Lifecycle
  slug: shodan-network-alert-lifecycle-workflow
- description: Create a notifier, read it back, update it, then delete it.
  name: Shodan Notifier Lifecycle
  slug: shodan-notifier-lifecycle-workflow
- description: Browse popular query tags, search the saved-query directory, then run a match.
  name: Shodan Query Directory Explorer
  slug: shodan-query-directory-workflow
- description: Resolve a hostname to an IP and pull the full Shodan host record for that IP.
  name: Shodan Resolve Hostname and Inspect Host
  slug: shodan-resolve-and-host-info-workflow
- description: Reverse-resolve an IP to its hostnames, then pull the full host record.
  name: Shodan Reverse DNS to Host Info
  slug: shodan-reverse-dns-to-host-info-workflow
- description: Submit a single-IP scan, poll until done, then pull the fresh host record.
  name: Shodan Scan Then Inspect Host
  slug: shodan-scan-then-inspect-host-workflow
- description: Discover available filters and facets, validate a query, then count its results.
  name: Shodan Search Builder
  slug: shodan-search-builder-workflow
- description: Estimate a search, run it, then drill into the first matching host.
  name: Shodan Search to Host Detail
  slug: shodan-search-to-host-detail-workflow
- description: Submit an on-demand scan and poll its status until the crawl completes.
  name: Shodan Submit On-Demand Scan and Poll
  slug: shodan-submit-scan-and-poll-workflow
- description: Pull historical monthly trends for a query, then compare to the live count.
  name: Shodan Historical Trends vs Live Exposure
  slug: shodan-trends-vs-live-workflow
artifact_total: 109
asyncapis:
- description: Real-time streaming firehose of banner data collected by Shodan, delivered as newline-separated JSON or Server-Sent Events. Subscribers can consume the full firehose or filter by ASN, country, port, o
  name: Shodan Streaming API
  slug: shodan-stream-asyncapi
collections:
- collection_type: postman
  name: Shodan CVEDB API
  slug: postman-shodan-cvedb
- collection_type: postman
  name: Shodan InternetDB API
  slug: postman-shodan-internetdb
- collection_type: postman
  name: Shodan REST API
  slug: postman-shodan-rest
- collection_type: postman
  name: Shodan Streaming API
  slug: postman-shodan-stream
- collection_type: postman
  name: Shodan Trends API
  slug: postman-shodan-trends
- collection_type: open
  name: Shodan CVEDB API
  slug: open-shodan-cvedb
- collection_type: open
  name: Shodan InternetDB API
  slug: open-shodan-internetdb
- collection_type: open
  name: Shodan REST API
  slug: open-shodan-rest
- collection_type: open
  name: Shodan Streaming API
  slug: open-shodan-stream
- collection_type: open
  name: Shodan Trends API
  slug: open-shodan-trends
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shodan-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shodan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shodan-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/shodan/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-account-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-alert-with-notifier-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-cve-enrichment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-domain-recon-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-internetdb-vuln-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-network-alert-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-notifier-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-query-directory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-resolve-and-host-info-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-reverse-dns-to-host-info-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-scan-then-inspect-host-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-search-builder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-search-to-host-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-submit-scan-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/shodan-trends-vs-live-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.shodan.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.shodan.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shodan.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.shodan.io/api
- group: commercial
  title: ''
  type: Pricing
  url: https://account.shodan.io/billing
- group: commercial
  title: ''
  type: Plans
  url: plans/shodan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shodan-rate-limits.yml
- group: start
  title: ''
  type: Signup
  url: https://account.shodan.io/register
- group: start
  title: ''
  type: Login
  url: https://account.shodan.io/login
- group: start
  title: ''
  type: Console
  url: https://www.shodan.io/dashboard
- group: auth
  title: ''
  type: Authentication
  url: https://developer.shodan.io/api/requirements
- group: start
  title: ''
  type: GettingStarted
  url: https://help.shodan.io/the-basics/what-is-shodan
- group: start
  title: ''
  type: GettingStarted
  url: https://help.shodan.io/the-basics/search-query-fundamentals
- group: learn
  title: ''
  type: Tutorials
  url: https://help.shodan.io/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://help.shodan.io/
- group: other
  title: ''
  type: Glossary
  url: https://datapedia.shodan.io/
- group: operate
  title: ''
  type: Support
  url: mailto:support@shodan.io
- group: company
  title: ''
  type: Blog
  url: https://blog.shodan.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shodan.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shodan.io/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shodan.io/legal/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.shodan.io/legal
- group: other
  title: ''
  type: X
  url: https://x.com/shodanhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shodan
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@shodanhq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/achillean
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/shodan-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/shodan-developer-docs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/shodan-ruby
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/shodan-perl
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/Shodan.NET
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/achillean/steampipe-plugin-shodan
- group: build
  title: ''
  type: CLI
  url: https://help.shodan.io/command-line-interface/0-installation
- group: build
  title: ''
  type: SDKs
  url: https://github.com/achillean/shodan-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/picatz/shodanz
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ScadaExposure/Shodan-PHP-REST-API
- group: build
  title: ''
  type: SDKs
  url: https://github.com/prophetl33t/ShodanCPP
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Shodan/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tparnell8/Shodan.Net
- group: build
  title: ''
  type: SDKs
  url: https://github.com/shadowscatcher/shodan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ns3777k/go-shodan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/iomonad/shodan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fooock/jshodan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jesusprubio/shodan-client.js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Dudley5000/WWW-Shodan-API
- group: build
  title: ''
  type: SDKs
  url: https://github.com/darkoperator/Posh-Shodan
- group: build
  title: ''
  type: SDKs
  url: https://github.com/femiagbabiaka/shodan-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/PercussiveElbow/Shodan
- group: build
  title: ''
  type: Tools
  url: https://github.com/achillean/steampipe-plugin-shodan
- group: build
  title: ''
  type: Tools
  url: https://monitor.shodan.io
- group: build
  title: ''
  type: Tools
  url: https://maps.shodan.io
- group: build
  title: ''
  type: Tools
  url: https://images.shodan.io
- group: build
  title: ''
  type: Tools
  url: https://enterprise.shodan.io
- group: build
  title: ''
  type: Tools
  url: https://snippets.shodan.io
- group: build
  title: ''
  type: Tools
  url: https://github.com/BurtTheCoder/mcp-shodan
- group: build
  title: ''
  type: Tools
  url: https://github.com/ADEOSec/mcp-shodan
- group: build
  title: ''
  type: Tools
  url: https://github.com/Cyreslab-AI/shodan-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/Vorota-ai/shodan-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/mohdhaji87/Shodan-MCP
- group: design
  title: ''
  type: SpectralRules
  url: rules/shodan-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shodan-vocabulary.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shodan-finops.yml
created: '2026-05-28'
description: Shodan is the world's first search engine for Internet-connected devices. It continuously crawls the public Internet to build a searchable database of servers, IoT devices, industrial control systems, routers, webcams, databases, and any other host that exposes a service. Shodan provides REST, Streaming, and Trends APIs along with on-demand scanning, network alerts, notifiers, DNS lookups, the InternetDB API, and the CVEDB vulnerability database. It is widely used for attack-surface management, security research, threat intelligence, vulnerability discovery, market research, and academic study of the Internet itself.
examples:
- key_count: 2
  name: Shodan Cvedb Cve Lookup Example
  slug: shodan-cvedb-cve-lookup-example
- key_count: 2
  name: Shodan Internetdb Host Example
  slug: shodan-internetdb-host-example
- key_count: 2
  name: Shodan Rest Alert Create Example
  slug: shodan-rest-alert-create-example
- key_count: 2
  name: Shodan Rest Host Lookup Example
  slug: shodan-rest-host-lookup-example
- key_count: 2
  name: Shodan Rest Scan Create Example
  slug: shodan-rest-scan-create-example
- key_count: 2
  name: Shodan Rest Search Example
  slug: shodan-rest-search-example
- key_count: 2
  name: Shodan Stream Banner Example
  slug: shodan-stream-banner-example
- key_count: 2
  name: Shodan Trends Search Example
  slug: shodan-trends-search-example
features:
- description: Search billions of indexed banners from servers, routers, webcams, industrial control systems, and IoT devices using a powerful query language with facets and filters.
  name: Internet-Wide Device Search
- description: Retrieve all known information for an IP including open ports, service banners, geolocation, ASN/ISP, hostnames, vulnerabilities, SSL/TLS certificates, and detected technologies.
  name: Host Information Lookup
- description: Submit IPs, CIDR ranges, or netblocks for an on-demand crawl using scan credits. Enterprise plans can request Internet-wide scans for a specific port or protocol.
  name: On-Demand Scanning
- description: Create alerts on monitored IP ranges that fire when new services, changes, vulnerabilities, or expirations are detected, with delivery via Slack, email, webhook, and other notifier providers.
  name: Network Alerts and Notifiers
- description: Forward, reverse, and full-domain DNS lookups including subdomain enumeration backed by Shodan's passive DNS database.
  name: DNS Lookup Suite
- description: Subscribe to real-time banner data filtered by ASN, country, port, or CVE for SIEMs, data lakes, and bespoke analytics pipelines.
  name: Streaming Firehose
- description: Run faceted queries against the full historical scan database to analyze product adoption, regional exposure, and changes over time.
  name: Trends Analytics
- description: Open, key-free lookup that returns the open ports, CPEs, tags, and CVEs for any IPv4 address; refreshed weekly.
  name: InternetDB Free Lookup
- description: Open vulnerability lookup with CPE search, KEV filter, EPSS sorting, and date-range queries.
  name: CVEDB Vulnerability Database
- description: Enterprise-tier daily and on-demand bulk exports of Shodan's underlying datasets for offline analysis and warehousing.
  name: Bulk Data Exports
- description: Enterprise organization support for sharing credits and managing members through the API.
  name: Organization Management
- description: Browse, search, and tag community-contributed Shodan queries covering common technologies, exposures, and devices.
  name: Saved Query Directory
- description: Built-in notification provider integrations for Slack, email, Discord, Telegram, webhook, and more.
  name: Notifier Providers
finops:
- name: Shodan Finops
  service_category: API
  slug: shodan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shodan.png
integrations:
- description: Shodan data is widely ingested into Splunk for security analytics via the streaming API and the Splunk add-on ecosystem.
  name: Splunk
- description: Shodan transforms for Maltego enable graph-based pivoting on banners, certificates, and IPs.
  name: Maltego
- description: Notifier integration delivers alert events to Slack channels.
  name: Slack
- description: Notifier integration delivers alert events to mailboxes.
  name: Email
- description: Notifier integration posts alert events to arbitrary HTTPS endpoints.
  name: Webhook
- description: Notifier integration delivers alert events to Discord servers.
  name: Discord
- description: Notifier integration delivers alert events to Telegram chats.
  name: Telegram
- description: Official Steampipe plugin lets you query Shodan host, DNS, and exploit data using standard SQL.
  name: Steampipe
- description: Multiple community MCP servers expose Shodan tools to AI assistants including Claude, Cursor, and VS Code.
  name: Model Context Protocol
- description: Shodan's CLI ships helpers to enrich Nmap scan output with Shodan-derived banner context.
  name: Nmap
json_schemas:
- name: Shodan CVEDB CPE
  property_count: 4
  slug: shodan-cvedb-cpe
- name: Shodan CVEDB CVE
  property_count: 14
  slug: shodan-cvedb-cve
- name: Shodan InternetDB Host
  property_count: 6
  slug: shodan-internetdb-host
- name: Shodan Network Alert
  property_count: 8
  slug: shodan-rest-alert
- name: Shodan Banner
  property_count: 19
  slug: shodan-rest-banner
- name: Shodan Host
  property_count: 20
  slug: shodan-rest-host
- name: Shodan Notifier
  property_count: 4
  slug: shodan-rest-notifier
- name: Shodan On-Demand Scan
  property_count: 5
  slug: shodan-rest-scan
- name: Shodan Search Result
  property_count: 3
  slug: shodan-rest-search-result
- name: Shodan Streaming Banner
  property_count: 19
  slug: shodan-stream-banner
- name: Shodan Trends Result
  property_count: 3
  slug: shodan-trends-result
json_structures:
- name: Shodan Rest Alert Structure
  property_count: 0
  slug: shodan-rest-alert-structure
- name: Shodan Rest Host Structure
  property_count: 0
  slug: shodan-rest-host-structure
- name: Shodan Stream Banner Structure
  property_count: 0
  slug: shodan-stream-banner-structure
jsonld:
- class_count: 8
  name: Shodan Context
  property_count: 46
  slug: shodan-context
layout: provider
modified: '2026-05-30'
name: Shodan
nav: Providers
network: true
overview: 'Shodan publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account API, Bulk Data API, CPE API, and 12 more. Tagged areas include Security, Search, Internet, Devices, and IoT.


  The Shodan catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shodan''s developer surface includes authentication, documentation, API reference, pricing, signup flow, developer console, getting-started guide, and 74 more developer resources.'
plans:
- name: Shodan Plans Pricing
  plan_count: 6
  slug: shodan-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 17
  name: Shodan Rate Limits
  slug: shodan-rate-limits
rules:
- name: Shodan API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: shodan-asyncapi-spectral-rules
- name: Shodan API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: shodan-jsonschema-spectral-rules
- name: Shodan API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 5
  slug: shodan-rules
score:
  band: exemplar
  composite: 72.9
  delta: -2.4
  facets:
    commercial_clarity: 84.2
    contract_quality: 81.0
    developer_ergonomics: 84.8
    discoverability: 57.4
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 75.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shodan/refs/heads/main/screenshots/shodan-2026-06-20T193830.png
security:
- kind: authentication
  name: Shodan Authentication
  slug: shodan-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shodan Domain Security
  slug: shodan-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: shodan
solutions:
- description: Hosted attack-surface monitoring product built on the network alerts and notifiers APIs.
  name: Shodan Monitor
- description: Real-time firehose and daily bulk data exports for SOCs, threat intelligence platforms, and academic researchers.
  name: Enterprise Data Feed
- description: Free, unauthenticated host lookup designed for embedding into security tools and dashboards.
  name: InternetDB
- description: Free vulnerability database with KEV and EPSS metadata for prioritization workflows.
  name: CVEDB
- description: Enterprise-only capability to request a scan of the entire Internet for a specific port or protocol.
  name: Internet-Wide Scanning
tags:
- Security
- Search
- Internet
- Devices
- IoT
- Vulnerabilities
- CVE
- Attack Surface
- Threat Intelligence
- Reconnaissance
- Network
- DNS
- Scanning
- Public APIs
use_cases:
- description: Continuously monitor an organization's external attack surface for new services, configuration drift, and vulnerable software.
  name: Attack Surface Management
- description: Quantify exposure to specific CVEs across the Internet or a defined customer footprint using CVEDB and the search/trends APIs.
  name: Vulnerability Intelligence
- description: Pivot from IPs, certificates, banners, and ASNs to map adversary infrastructure and discover related hosts.
  name: Threat Hunting and OSINT
- description: Study the distribution of misconfigured services, exposed databases, and emerging IoT ecosystems across the public Internet.
  name: Security Research
- description: Track adoption of products, web servers, cloud providers, and frameworks across regions and industries using Trends.
  name: Competitive and Market Research
- description: Demonstrate visibility into externally exposed assets for frameworks that require attack-surface inventories.
  name: Regulatory and Compliance Reporting
- description: Inform cyber-insurance scoring with externally observable evidence of exposed services, vulnerabilities, and hygiene.
  name: Insurance Underwriting
- description: Triage IPs observed in alerts against Shodan history to determine who they are and what services they expose.
  name: Incident Response
website: https://www.shodan.io/
---
