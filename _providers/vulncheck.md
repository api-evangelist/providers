---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.vulncheck.com/v3
  baseurl_source: declared
  description: The endpoints API from VulnCheck — 13 operation(s) for endpoints.
  name: VulnCheck Endpoints API
  slug: vulncheck-endpoints-api
- baseURL: https://api.vulncheck.com/v3
  baseurl_source: declared
  description: The indices API from VulnCheck — 508 operation(s) for indices.
  name: VulnCheck Indices API
  slug: vulncheck-indices-api
artifact_total: 14
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vulncheck.com/feed/blog/atom.xml
- group: other
  href: https://artifacts.apis.io/vulncheck/capabilities/vulncheck-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vulncheck-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/vulncheck/overlays/vulncheck-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vulncheck-api-overlay.yaml
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
  href: https://artifacts.apis.io/vulncheck/well-known/vulncheck-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vulncheck-security.txt
- group: agent
  href: https://artifacts.apis.io/vulncheck/well-known/vulncheck-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vulncheck-well-known.yml
- group: auth
  href: https://artifacts.apis.io/vulncheck/security/vulncheck-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vulncheck-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vulncheck/security/vulncheck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vulncheck-domain-security.yml
- group: build
  href: https://artifacts.apis.io/vulncheck/packages/vulncheck-packages.yml
  title: ''
  type: Packages
  url: packages/vulncheck-packages.yml
- group: build
  href: https://artifacts.apis.io/vulncheck/packages/vulncheck-packages.yml
  title: ''
  type: SDKs
  url: packages/vulncheck-packages.yml
- group: build
  href: https://artifacts.apis.io/vulncheck/cli/vulncheck-cli.yml
  title: ''
  type: CLI
  url: cli/vulncheck-cli.yml
- group: agent
  href: https://artifacts.apis.io/vulncheck/mcp/vulncheck-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vulncheck-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vulncheck/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/vulncheck/llms/vulncheck-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vulncheck-llms.txt
- group: design
  href: https://artifacts.apis.io/vulncheck/lifecycle/vulncheck-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vulncheck-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vulncheck/conformance/vulncheck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vulncheck-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/vulncheck/plans/vulncheck-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vulncheck-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vulncheck/rate-limits/vulncheck-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vulncheck-rate-limits.yml
created: '2026-09-04'
description: VulnCheck is an exploit and vulnerability intelligence company that supplies machine-readable data on known exploited vulnerabilities, exploit maturity, threat-actor activity, initial-access exploitation, IP and target intelligence, CPE/PURL identity and vendor advisories. Its Exploit & Vulnerability Intelligence platform enriches CVE records ahead of NIST NVD, publishes the VulnCheck KEV catalog, and exposes everything through a 521-operation REST API at api.vulncheck.com/v3 covering 490+ named indices, alongside a Go SDK, Python SDK, a scripting/agent-oriented CLI, an MCP server and a published Claude Code agent skill. A free Community tier provides VulnCheck KEV and NVD++ data.
finops:
- has_sources: true
  method: derived
  name: Vulncheck Finops
  primary_unit: ''
  service_category: ''
  slug: vulncheck-finops
  template: true
image: https://www.vulncheck.com/logo.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 24 tools listed.
  name: VulnCheck MCP Server
  slug: vulncheck-mcp-server
modified: '2026-10-06'
name: VulnCheck
nav: Providers
network: true
overview: 'VulnCheck publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Endpoints API and Indices API. Tagged areas include Company, Security, Vulnerability Intelligence, Exploit Intelligence, and Threat Intelligence.


  The VulnCheck catalog on APIs.io includes 1 Spectral governance ruleset.


  VulnCheck''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, changelog, and 25 more developer resources.'
plans:
- name: Vulncheck Plans Pricing
  plan_count: 1
  slug: vulncheck-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Vulncheck Rate Limits
  slug: vulncheck-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: VulnCheck API Rules
  rule_count: 63
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 8
  slug: vulncheck-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 78.6
    discoverability: 71.7
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 57.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vulncheck/vulncheck-2026-10-11T133225.png
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
skill_count: 4
skills:
- name: vulncheck-c2-blocklist
  slug: vulncheck-c2-blocklist
- name: vulncheck-cli
  slug: vulncheck-cli
- name: vulncheck-cve-triage
  slug: vulncheck-cve-triage
- name: vulncheck-dependency-vulnerabilities
  slug: vulncheck-dependency-vulnerabilities
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
