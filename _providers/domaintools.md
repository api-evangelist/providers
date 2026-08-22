---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Domaintools Agentic Access
  operation_count: 53
  slug: domaintools-agentic-access
  summary_line: 53 operations · 11 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: The Flex search API from DomainTools — 2 operation(s) for flex search.
  name: DomainTools Flex search API
  slug: domaintools-flex-search-api
- description: Access the latest information about your account, including service limits.
  name: DomainTools Information API
  slug: domaintools-information-api
- description: 'Iris Detect is an Internet infrastructure detection, monitoring, and enforcement tool. It rapidly discovers malicious domains that are engaged in brand impersonation, risk-scores them within minutes, '
  name: DomainTools Iris Detect API
  slug: domaintools-iris-detect-api
- description: Designed to support high query volumes with batch processing and fast response times, the Iris Enrich API provides actionable insights-at-scale with enterprise-scale ingestion of DomainTools data
  name: DomainTools Iris Enrich API
  slug: domaintools-iris-enrich-api
- description: The Iris Investigate API is ideally suited for investigate and orchestrate use cases at human scale. Identify threats, map adversary infrastructure, and streamline investigations.
  name: DomainTools Iris Investigate API
  slug: domaintools-iris-investigate-api
- description: Endpoints for retrieving detailed information about domains and IPs, and for finding connections between domains and infrastructure.
  name: DomainTools Lookups API
  slug: domaintools-lookups-api
- description: Endpoints for monitoring new domain registrations, changes to IP ranges, and other key infrastructure events based on specific terms.
  name: DomainTools Monitors API
  slug: domaintools-monitors-api
- description: The Ping API from DomainTools — 1 operation(s) for ping.
  name: DomainTools Ping API
  slug: domaintools-ping-api
- description: The Rate Limit API from DomainTools — 1 operation(s) for rate limit.
  name: DomainTools Rate Limit API
  slug: domaintools-rate-limit-api
- description: The rdata Lookups API from DomainTools — 4 operation(s) for rdata lookups.
  name: DomainTools rdata Lookups API
  slug: domaintools-rdata-lookups-api
- description: The rrset Lookups API from DomainTools — 6 operation(s) for rrset lookups.
  name: DomainTools rrset Lookups API
  slug: domaintools-rrset-lookups-api
- description: The Siebatchd API from DomainTools — 4 operation(s) for siebatchd.
  name: DomainTools Siebatchd API
  slug: domaintools-siebatchd-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dnsdb Flex search API
  slug: open-domaintools-flex-search-api
- collection_type: open
  name: dnsdb Flex search Information API
  slug: open-domaintools-information-api
- collection_type: open
  name: dnsdb Flex search Iris Detect API
  slug: open-domaintools-iris-detect-api
- collection_type: open
  name: dnsdb Flex search Iris Enrich API
  slug: open-domaintools-iris-enrich-api
- collection_type: open
  name: dnsdb Flex search Iris Investigate API
  slug: open-domaintools-iris-investigate-api
- collection_type: open
  name: dnsdb Flex search Lookups API
  slug: open-domaintools-lookups-api
- collection_type: open
  name: dnsdb Flex search Monitors API
  slug: open-domaintools-monitors-api
- collection_type: open
  name: dnsdb Flex search Ping API
  slug: open-domaintools-ping-api
- collection_type: open
  name: dnsdb Flex search Rate Limit API
  slug: open-domaintools-rate-limit-api
- collection_type: open
  name: dnsdb Flex search rdata Lookups API
  slug: open-domaintools-rdata-lookups-api
- collection_type: open
  name: dnsdb Flex search rrset Lookups API
  slug: open-domaintools-rrset-lookups-api
- collection_type: open
  name: dnsdb Flex search Siebatchd API
  slug: open-domaintools-siebatchd-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/domaintools-dnsdb-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.domaintools.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.domaintools.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.domaintools.com/api/iris/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.domaintools.com/api/iris/
- group: auth
  title: ''
  type: Authentication
  url: authentication/domaintools-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.domaintools.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.domaintools.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DomainTools
- group: start
  title: ''
  type: SignUp
  url: https://www.domaintools.com/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.domaintools.com/company/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.domaintools.com/company/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/domaintools-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://domaintools.statuspage.io
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/domaintools-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/domaintools-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/domaintools-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/domaintools-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/domaintools-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/domaintools-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/domaintools-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/domaintools-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/domaintools-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/domaintools-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/domaintools-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/domaintools-well-known.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/domaintools-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/domaintools-domain-security.yml
created: '2026-07-17'
description: DomainTools is a domain and DNS intelligence company whose APIs power threat investigation, hunting, and monitoring for security teams. Its product surface spans Iris Investigate (pivot-based domain investigation), Iris Enrich (bulk domain enrichment), and Iris Detect (brand-infringement monitoring); the Farsight DNSDB passive DNS history API (300+ billion records); Lookups & Monitors (WHOIS, RDAP, hosting history, reverse IP/WHOIS, reputation, risk score, and change monitors); Threat Feeds (predictive risk and discovery feeds with RPZ integration); and Farsight SIE real-time DNS event streaming. DomainTools publishes OpenAPI specifications, an official Python SDK with a bundled CLI, and a remotely hosted MCP server for AI agents. A Battery Ventures portfolio company, enriched into the API Evangelist network.
image: https://www.domaintools.com/wp-content/uploads/dt-logo.png
layout: provider
mcp_servers:
- description: ''
  name: domaintools-mcp.yml
  slug: domaintools-mcpyml
modified: '2026-07-18'
name: DomainTools
nav: Providers
network: true
overview: 'DomainTools publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Flex search API, Information API, Iris Detect API, and 9 more. Tagged areas include Company, Threat Intelligence, Domain Intelligence, DNS, and WHOIS.


  DomainTools'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 22 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 50.8
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 54.9
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 42.1
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/domaintools/refs/heads/main/screenshots/domaintools-2026-07-25T212242.png
security:
- kind: authentication
  name: Domaintools Authentication
  slug: domaintools-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Domaintools Domain Security
  slug: domaintools-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: domaintools
tags:
- Company
- Threat Intelligence
- Domain Intelligence
- DNS
- WHOIS
- Passive DNS
- Cybersecurity
- Domain Monitoring
- Risk Scoring
- Security
website: https://docs.domaintools.com/
---
