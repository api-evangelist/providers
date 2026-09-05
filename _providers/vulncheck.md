---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://api.vulncheck.com/v3
  baseurl_source: declared
  description: 'Version 3 of the VulnCheck API. A read-only REST API exposing VulnCheck''s exploit and vulnerability intelligence: 490+ named indices browsable at /index/{name}, CVE and CPE search, PURL vulnerability '
  name: VulnCheck API
  slug: vulncheck-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.vulncheck.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vulncheck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vulncheck.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vulncheck.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vulncheck.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://console.vulncheck.com/register
- group: start
  title: ''
  type: Login
  url: https://console.vulncheck.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.vulncheck.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.vulncheck.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vulncheck-oss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vulncheck.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vulncheck.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vulncheck.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vulncheck.com/changelog
- group: auth
  title: ''
  type: Security
  url: https://www.vulncheck.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/vulncheck-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vulncheck-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vulncheck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vulncheck-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/vulncheck-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vulncheck-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/vulncheck-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vulncheck-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vulncheck-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vulncheck-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vulncheck-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vulncheck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vulncheck-rate-limits.yml
created: '2026-09-04'
description: VulnCheck is an exploit and vulnerability intelligence company that supplies machine-readable data on known exploited vulnerabilities, exploit maturity, threat-actor activity, initial-access exploitation, IP and target intelligence, CPE/PURL identity and vendor advisories. Its Exploit & Vulnerability Intelligence platform enriches CVE records ahead of NIST NVD, publishes the VulnCheck KEV catalog, and exposes everything through a 521-operation REST API at api.vulncheck.com/v3 covering 490+ named indices, alongside a Go SDK, Python SDK, a scripting/agent-oriented CLI, an MCP server and a published Claude Code agent skill. A free Community tier provides VulnCheck KEV and NVD++ data.
image: https://www.vulncheck.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: VulnCheck MCP Server
  slug: vulncheck-mcp-server
modified: '2026-09-04'
name: VulnCheck
nav: Providers
network: true
overview: 'VulnCheck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Vulnerability Intelligence, Exploit Intelligence, and Threat Intelligence.


  VulnCheck''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 22 more developer resources.'
plans:
- name: Vulncheck Plans Pricing
  plan_count: 1
  slug: vulncheck-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Vulncheck Rate Limits
  slug: vulncheck-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 78.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 68.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Vulncheck Authentication
  slug: vulncheck-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Vulncheck Domain Security
  slug: vulncheck-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vulncheck Vulnerability Disclosure
  slug: vulncheck-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: vulncheck
tags:
- Company
- Security
- Vulnerability Intelligence
- Exploit Intelligence
- Threat Intelligence
- Cybersecurity
- CVE
- Vulnerability Management
- Data
website: https://www.vulncheck.com/
---
