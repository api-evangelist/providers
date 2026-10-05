---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Contrast Security Agentic Access
  operation_count: 8
  slug: contrast-security-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: REST API for interacting with Contrast TeamServer to manage applications, libraries, vulnerabilities, traces, servers, agents, and organization settings. Requires an API key, Authorization header form
  name: Contrast TeamServer REST API
  slug: rest-api
- baseURL: https://app.contrastsecurity.com/Contrast/api/ng
  baseurl_source: declared
  description: An application represents an executable unit of code that can be instrumented at runtime by an agent in Contrast. This can be a web app, microservice, or other runnable code and any dependencies inclu
  name: Contrast Security Applications API
  slug: contrast-security-applications-api
- baseURL: https://app.contrastsecurity.com/Contrast/api/ng
  baseurl_source: declared
  description: An organization represents a grouping of user accounts in Contrast.
  name: Contrast Security Organizations API
  slug: contrast-security-organizations-api
- baseURL: https://app.contrastsecurity.com/Contrast/api/ng
  baseurl_source: declared
  description: A rule defines a data flow pattern used to categorize vulnerability and attack types. Some common rules are sql-injection, ssrf, and reflected-xss.
  name: Contrast Security Rules API
  slug: contrast-security-rules-api
- baseURL: https://app.contrastsecurity.com/Contrast/api/ng
  baseurl_source: declared
  description: Vulnerabilities detected in runtime by Contrast Assess are weaknesses in the application code that allow an attacker to cause harm.
  name: Contrast Security Vulnerabilities API
  slug: contrast-security-vulnerabilities-api
artifact_total: 26
asyncapis:
- description: ''
  name: Contrast Security Webhooks
  slug: contrast-security-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contrast Assess Applications API
  slug: open-contrast-security-applications-api
- collection_type: open
  name: Contrast Assess Applications Organizations API
  slug: open-contrast-security-organizations-api
- collection_type: open
  name: Contrast Assess Applications Rules API
  slug: open-contrast-security-rules-api
- collection_type: open
  name: Contrast Assess Applications Vulnerabilities API
  slug: open-contrast-security-vulnerabilities-api
- collection_type: open
  name: Contrast Assess API
  slug: open-contrast-security
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/well-known/contrast-security-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contrast-security-status-security.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contrastsecurity.com/pricing-and-packaging
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/plans/contrast-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contrast-security-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/rules/contrast-security-rules.yml
  title: ''
  type: Spectral
  url: rules/contrast-security-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/json-ld/contrast-security-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/contrast-security-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/vocabulary/contrast-security-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/contrast-security-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/asyncapi/contrast-security-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contrast-security-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/data-model/contrast-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/contrast-security-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/changelog/contrast-security-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/contrast-security-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.contrastsecurity.com/disclosure-policy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/errors/contrast-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contrast-security-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/conformance/contrast-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contrast-security-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/well-known/contrast-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contrast-security-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/well-known/contrast-security-contrastsecurity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contrast-security-contrastsecurity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/well-known/contrast-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contrast-security-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/hosts/contrast-security-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contrast-security-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/vendors/contrast-security-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contrast-security-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/packages/contrast-security-packages.yml
  title: ''
  type: SDKs
  url: packages/contrast-security-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/packages/contrast-security-packages.yml
  title: ''
  type: Packages
  url: packages/contrast-security-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.contrastsecurity.com/
- group: operate
  title: ''
  type: Support
  url: https://support.contrastsecurity.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contrastsecurity.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.contrastsecurity.com/press/new-contrast-security-report-finds
- group: start
  title: ''
  type: Login
  url: https://cs004.contrastsecurity.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.contrastsecurity.com/en/java-quick-start-guide.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.contrastsecurity.jp/index.html?lang=ja
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contrastsecurity
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/agentic-access/contrast-security-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contrast-security-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/security/contrast-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contrast-security-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/security/contrast-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contrast-security-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/authentication/contrast-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contrast-security-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contrast-security
- group: company
  title: ''
  type: Website
  url: https://www.contrastsecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.contrastsecurity.com
- group: docs
  title: ''
  type: API Docs
  url: https://api.contrastsecurity.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://api.contrastsecurity.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.contrastsecurity.com/security-influencers/rss.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://app.contrastsecurity.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Contrast-Security-OSS/mcp-contrast
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/capabilities/contrast-security-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/contrast-security-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contrastsecurity.com/contact-sales
- group: start
  title: ''
  type: Signup
  url: https://www.contrastsecurity.com/contrast-free-tools
coverage:
  checked: '2026-10-04'
  detail: No OpenAPI or other machine‑readable contract found on the API host despite probing common spec endpoints.
  evidence:
  - status: 200
    url: https://api.contrastsecurity.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-11'
description: Contrast Security is an application security platform that uses instrumentation-based agents to provide Interactive Application Security Testing (IAST), Runtime Application Self-Protection (RASP), and Software Composition Analysis (SCA) across Java, .NET, Node.js, Python, PHP, Go, and Ruby applications. The platform identifies, prioritizes, and defends against vulnerabilities and attacks in real time from inside running applications. Contrast's REST API enables programmatic access to TeamServer applications, libraries, vulnerabilities, and traces, authenticated via API key plus Authorization header (Base64 of username:service_key) and an Organization ID.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contrast-security.png
json_schemas:
- name: PageV4Application
  property_count: 11
  slug: contrast-security-page-v4-application
- name: V4Application
  property_count: 12
  slug: contrast-security-v4-application
- name: V4Organization
  property_count: 7
  slug: contrast-security-v4-organization
- name: V4Rule
  property_count: 10
  slug: contrast-security-v4-rule
- name: V4Vulnerability
  property_count: 17
  slug: contrast-security-v4-vulnerability
jsonld:
- class_count: 7
  name: Contrast Security Context
  property_count: 51
  slug: contrast-security-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: ''
  name: MCP Server Source
  slug: mcp-server-source
modified: '2026-07-12'
name: Contrast Security
nav: Providers
network: true
overview: 'Contrast Security publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Organizations API, Rules API, and 2 more. Tagged areas include Application Security, AppSec, IAST, RASP, and SCA.


  The Contrast Security catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Contrast Security''s developer surface includes pricing, changelog, support, getting-started guide, authentication, documentation, engineering blog, and 35 more developer resources.'
plans:
- name: Contrast Security Plans Pricing
  plan_count: 3
  slug: contrast-security-plans-pricing
random_paper: 7
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Contrast Security API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: contrast-security-rules
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.4
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 69.2
    developer_ergonomics: 57.1
    discoverability: 76.7
    operational_transparency: 55.3
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/contrast-security/refs/heads/main/screenshots/contrast-security-2026-06-20T174948.png
security:
- kind: authentication
  name: Contrast Security Authentication
  slug: contrast-security-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Contrast Security Domain Security
  slug: contrast-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Contrast Security Vulnerability Disclosure
  slug: contrast-security-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contrast-security
tags:
- Application Security
- AppSec
- IAST
- RASP
- SCA
- DevSecOps
- Runtime Protection
website: https://www.contrastsecurity.com
---
