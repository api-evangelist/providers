---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Abuseipdb Agentic Access
  operation_count: 7
  slug: abuseipdb-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: Endpoints for downloading the community blacklist.
  name: AbuseIPDB Blacklist API
  slug: abuseipdb-blacklist-api
- description: Endpoints for managing your own reports.
  name: AbuseIPDB Management API
  slug: abuseipdb-management-api
- description: Endpoints for submitting and retrieving abuse reports.
  name: AbuseIPDB Reports API
  slug: abuseipdb-reports-api
- description: Endpoints for looking up the abuse data of an IP or CIDR network.
  name: AbuseIPDB Reputation API
  slug: abuseipdb-reputation-api
arazzos:
- description: Download the community blacklist and enrich its top entry with a full single-IP check.
  name: AbuseIPDB Blacklist Triage
  slug: abuseipdb-blacklist-triage-workflow
- description: Scan a CIDR network block for reported addresses and deep-check the most abusive host.
  name: AbuseIPDB Block Scan And Check
  slug: abuseipdb-block-scan-and-check-workflow
- description: Upload a CSV of abuse reports in bulk, then spot-check one submitted IP to confirm it landed.
  name: AbuseIPDB Bulk Report Then Verify
  slug: abuseipdb-bulk-report-then-verify-workflow
- description: Check an IP's reputation and conditionally file an abuse report based on its confidence score.
  name: AbuseIPDB Check Then Report
  slug: abuseipdb-check-then-report-workflow
- description: Check an IP and clear your own reports against it when it turns out to be whitelisted or clean.
  name: AbuseIPDB Clear False Positive
  slug: abuseipdb-clear-false-positive-workflow
- description: Check an IP and, when it is abusive, pull its full paginated report history.
  name: AbuseIPDB Investigate IP
  slug: abuseipdb-investigate-ip-workflow
- description: Submit an abuse report for an IP and immediately re-check it to confirm the updated score.
  name: AbuseIPDB Report Then Verify
  slug: abuseipdb-report-then-verify-workflow
artifact_total: 63
collections:
- collection_type: postman
  name: AbuseIPDB APIv2
  slug: postman-abuseipdb-apiv2
- collection_type: open
  name: AbuseIPDB APIv2
  slug: open-abuseipdb-apiv2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abuseipdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abuseipdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abuseipdb-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/abuseipdb/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-blacklist-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-block-scan-and-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-bulk-report-then-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-check-then-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-clear-false-positive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-investigate-ip-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/abuseipdb-report-then-verify-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.abuseipdb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abuseipdb.com/
- group: start
  title: ''
  type: Signup
  url: https://www.abuseipdb.com/register
- group: start
  title: ''
  type: Login
  url: https://www.abuseipdb.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.abuseipdb.com/account/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.abuseipdb.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/abuseipdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abuseipdb-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/abuseipdb-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/abuseipdb-vocabulary.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/abuseipdb-finops.yml
- group: commercial
  title: ''
  type: Plans
  url: https://www.abuseipdb.com/account/plans
- group: company
  title: ''
  type: Blog
  url: https://www.abuseipdb.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://www.abuseipdb.com/faq.html
- group: operate
  title: ''
  type: Support
  url: https://www.abuseipdb.com/contact
- group: operate
  title: ''
  type: Contact
  url: https://www.abuseipdb.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.abuseipdb.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abuseipdb.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AbuseIPDB
- group: build
  title: ''
  type: SDKs
  url: https://github.com/AbuseIPDB/laravel
- group: build
  title: ''
  type: SDKs
  url: https://github.com/nickurt/laravel-abuseipdb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/falegk/abuseipdb-rb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/meatyite/python-abuseipdb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/streanger/abuseipdb-wrapper
- group: build
  title: ''
  type: CLI
  url: https://github.com/kristuff/abuseipdb-cli
created: '2026-05-28'
description: AbuseIPDB is a community-driven project to help system administrators, webmasters, and security analysts check the reputation of IP addresses and report malicious activity. The free APIv2 surface lets developers query a single IP, check a CIDR block, retrieve paginated reports, download a curated blacklist, submit single or bulk abuse reports, and clear their own past reports for an address. AbuseIPDB underpins fail2ban, UFW, Cloudflare WAF, Wazuh, Splunk SOAR, and dozens of other firewall and SIEM integrations across the security community.
examples:
- key_count: 2
  name: Abuseipdb Blacklist Example
  slug: abuseipdb-blacklist-example
- key_count: 2
  name: Abuseipdb Bulk Report Example
  slug: abuseipdb-bulk-report-example
- key_count: 2
  name: Abuseipdb Check Block Example
  slug: abuseipdb-check-block-example
- key_count: 2
  name: Abuseipdb Check Example
  slug: abuseipdb-check-example
- key_count: 2
  name: Abuseipdb Report Example
  slug: abuseipdb-report-example
- key_count: 2
  name: Abuseipdb Reports Example
  slug: abuseipdb-reports-example
features:
- description: Query any IPv4 or IPv6 address for its abuse confidence score, total reports, distinct reporters, and country/ISP metadata.
  name: IP Reputation Lookups
- description: Downloadable daily blacklist of high-confidence abusive IPs, with configurable confidence threshold, country filters, IP version, and result limit.
  name: Community-Sourced Blacklist
- description: Submit single or bulk abuse reports tagged with one or more standard category IDs (e.g. SSH Brute-Force, DDoS, Web App Attack).
  name: Abuse Reporting
- description: Score whole subnets in one call via the CHECK-BLOCK endpoint, with subscriber tiers supporting up to /16 networks.
  name: CIDR Block Checking
- description: 23 standard report categories (DNS Compromise, Open Proxy, Brute-Force, Phishing, etc.) for consistent classification.
  name: Categorised Abuse Taxonomy
- description: Remove your own reports for a given IP via the CLEAR-ADDRESS endpoint if a report was made in error.
  name: Self-Service Report Clearing
- description: Every response carries X-RateLimit-Limit / Remaining / Reset and Retry-After, simplifying back-off in clients.
  name: Standard Rate-Limit Headers
- description: Responses include an `isWhitelisted` flag so consumers can avoid blocking known-good infrastructure.
  name: Whitelist Awareness
finops:
- name: Abuseipdb Finops
  service_category: Security & Identity
  slug: abuseipdb-finops
image: https://www.abuseipdb.com/img/abuseipdb-logo.svg
integrations:
- description: Pre-packaged AbuseIPDB action ships with fail2ban; reports banned offenders directly to AbuseIPDB.
  name: Fail2Ban
- description: Multiple community projects (sefinek/UFW-AbuseIPDB-Reporter, jseutens/ufw-abuseipdb) ingest UFW logs and report or ingest the AbuseIPDB blacklist.
  name: UFW (Uncomplicated Firewall)
- description: sefinek/Cloudflare-WAF-To-AbuseIPDB streams Cloudflare WAF events into AbuseIPDB reports.
  name: Cloudflare WAF
- description: Official splunk-soar-connectors/abuseipdb connector enriches Splunk SOAR playbooks with AbuseIPDB reputation.
  name: Splunk SOAR
- description: marciuscosta/abuseipdb-wazuh-integration wires AbuseIPDB enrichment into Wazuh with a local cache and multi-key support.
  name: Wazuh
- description: goremykin/crowdsec-abuseipdb-blocklist converts CrowdSec data into AbuseIPDB blocklists.
  name: CrowdSec
- description: elhenro/endlessh-auto-report-abuseipdb auto-reports SSH tarpit visitors to AbuseIPDB.
  name: Endlessh
- description: tmiland/abuseipdb-php-nginx-blacklist-create generates an Nginx-ready blocklist file from AbuseIPDB.
  name: Nginx
- description: CcMarc/AbuseIPDB plugs AbuseIPDB into the Zen Cart e-commerce platform.
  name: Zen Cart
- description: AbuseIPDB enrichment is used by SOAR/IR pipelines like malwarekid/SOAR-Flow alongside Wazuh and TheHive.
  name: TheHive
- description: AbuseIPDB sources its IP geolocation, ISP, usage type, and domain data from IPinfo.
  name: IPinfo
json_schemas:
- name: AbuseIPDB Blacklist Entry
  property_count: 4
  slug: abuseipdb-blacklist-entry
- name: AbuseIPDB Check Response
  property_count: 1
  slug: abuseipdb-check-response
- name: AbuseIPDB Report
  property_count: 7
  slug: abuseipdb-report
json_structures:
- name: Abuseipdb Blacklist Entry Structure
  property_count: 4
  slug: abuseipdb-blacklist-entry-structure
- name: Abuseipdb Check Response Structure
  property_count: 15
  slug: abuseipdb-check-response-structure
- name: Abuseipdb Report Structure
  property_count: 7
  slug: abuseipdb-report-structure
jsonld:
- class_count: 0
  name: Abuseipdb Context
  property_count: 34
  slug: abuseipdb-context
layout: provider
modified: '2026-05-30'
name: AbuseIPDB
nav: Providers
network: true
overview: 'AbuseIPDB publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Blacklist API, Management API, Reports API, and 1 more. Tagged areas include Anti Malware, Blacklist, Cyber Security, IP Reputation, and Network Security.


  The AbuseIPDB catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AbuseIPDB''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, FAQ, support, and 29 more developer resources.'
plans:
- name: Abuseipdb Plans Pricing
  plan_count: 4
  slug: abuseipdb-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 25
  name: Abuseipdb Rate Limits
  slug: abuseipdb-rate-limits
rules:
- name: AbuseIPDB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: abuseipdb-jsonschema-spectral-rules
- name: AbuseIPDB API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 14
  slug: abuseipdb-rules
score:
  band: exemplar
  composite: 69.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 77.5
    developer_ergonomics: 60.9
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 69.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abuseipdb/refs/heads/main/screenshots/abuseipdb-2026-06-20T163451.png
security:
- kind: authentication
  name: Abuseipdb Authentication
  slug: abuseipdb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Abuseipdb Domain Security
  slug: abuseipdb-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: abuseipdb
solutions:
- description: 1,000 checks/day, 100 block checks, 5 blacklist downloads. Aimed at hobby admins and home labs.
  name: Individual (Free)
- description: $25/mo. 10,000 checks/day, 1,000 block checks, 100 bulk reports, customisable blacklist up to 100,000 IPs.
  name: Basic
- description: $99/mo. 50,000 checks/day, 5,000 block checks, 500 bulk reports, customisable blacklist up to 500,000 IPs.
  name: Premium
- description: Custom-priced direct data access for ISPs and large security organisations.
  name: Enterprise
tags:
- Anti Malware
- Blacklist
- Cyber Security
- IP Reputation
- Network Security
- Public APIs
- Threat Intelligence
use_cases:
- description: Auto-block and report SSH/RDP brute-force sources via fail2ban, UFW, or endlessh integrations.
  name: SSH / RDP Brute-Force Defence
- description: Enrich Cloudflare / Nginx / custom WAF rulesets with the AbuseIPDB blacklist for IP-based pre-filtering.
  name: WAF Augmentation
- description: Add AbuseIPDB context to Splunk SOAR, Wazuh, and TheHive alerts for analyst triage.
  name: SIEM / SOC Enrichment
- description: Score request source IPs before serving e-commerce or login pages to block known-abusive infrastructure.
  name: Bot and Crawler Filtering
- description: Combine AbuseIPDB with VirusTotal, Shodan, GreyNoise and similar feeds (e.g. malwoverview) during incident response.
  name: Threat Hunting and OSINT
- description: Convert nightly access logs into CSV bulk reports to feed the AbuseIPDB community blacklist.
  name: Bulk Reporting from Edge Logs
website: https://www.abuseipdb.com/
---
