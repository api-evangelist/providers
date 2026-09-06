---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Remote Model Context Protocol server operated by HackNotice, speaking JSON-RPC 2.0 over Streamable HTTP at https://mcp.hacknotice.com:13330/mcp. It publishes 80 tools across third-party, first-party, '
  name: HackNotice MCP Server
  slug: hacknotice-mcp
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: Cross-service alert retrieval.
  name: HackNotice Alerts API
  slug: hacknotice-alerts-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: Authentication, leak/leakfile search, customer records, metrics, habits, downloads, utilities and item notes shared by every business account.
  name: HackNotice All Business Accounts API
  slug: hacknotice-all-business-accounts-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: Aggregate/rollup calculation endpoints for breaches, threat actors and per-service alerts.
  name: HackNotice Calc endpoints API
  slug: hacknotice-calc-endpoints-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: Endpoints HackNotice groups as deprecated in its published collection (dark hash alerts, Teams accounts).
  name: HackNotice Deprecated API
  slug: hacknotice-deprecated-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: 'First-party domain monitoring: domain watchlists, domain leaks, domain alerts and downloads.'
  name: HackNotice Domain Business Accounts API
  slug: hacknotice-domain-business-accounts-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: 'End-user monitoring: end-user watchlists, end-user leaks and end-user alerts.'
  name: HackNotice Enduser Business Accounts API
  slug: hacknotice-enduser-business-accounts-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: Threat-research search over terms, filenames and word pools, plus saved searches.
  name: HackNotice Research Service Accounts API
  slug: hacknotice-research-service-accounts-api
- baseURL: https://extensionapi.hacknotice.com
  baseurl_source: declared
  description: 'Third-party vendor monitoring: hacks, hack updates, watchlists, alerts and vendor security assessments.'
  name: HackNotice Third Party Accounts API
  slug: hacknotice-third-party-accounts-api
artifact_total: 15
asyncapis:
- description: ''
  name: Hacknotice Webhooks
  slug: hacknotice-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/HackNotice/n8n-nodes-hacknotice-mcp/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hacknotice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hacknotice.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.hacknotice.com
- group: docs
  title: ''
  type: Documentation
  url: https://hacknotice.zendesk.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.hacknotice.com
- group: start
  title: ''
  type: GettingStarted
  url: https://hacknotice.zendesk.com/hc/en-us/articles/13771563959828-Overview-Getting-Started-for-Sec-Teams
- group: operate
  title: ''
  type: Support
  url: https://hacknotice.zendesk.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://hacknotice.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://hacknotice.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://hacknotice.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HackNotice
- group: commercial
  title: ''
  type: Pricing
  url: https://hacknotice.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://hacknotice.com/free-account/
- group: start
  title: ''
  type: Login
  url: https://app.hacknotice.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hacknotice.com/businesstandc/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hacknotice.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://api-docs.hacknotice.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hacknotice-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hacknotice-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hacknotice-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/hacknotice-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hacknotice-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hacknotice-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hacknotice-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hacknotice-plans-pricing.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hacknotice-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hacknotice-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hacknotice-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hacknotice-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hacknotice-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/hacknotice-openapi-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hacknotice-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hacknotice-llms.txt
created: '2026-08-22'
description: HackNotice is an external threat-intelligence and cyber-risk platform founded in 2018 and headquartered in Austin, Texas. It continuously collects intelligence from ransomware groups, infostealer malware logs, data breaches, dark-web marketplaces, hacker forums and public disclosures, then matches that intelligence against the domains, employees, customers and vendors an organization asks it to watch. The product is organized around four monitoring services — first-party domain monitoring, third-party vendor risk monitoring, end-user credential monitoring, and threat research and investigations — plus AI-assisted vendor security assessments. HackNotice exposes this surface programmatically through a REST API documented as a public Postman collection at api-docs.hacknotice.com, a remote Model Context Protocol server at mcp.hacknotice.com whose tool catalogue answers anonymously, first-party n8n automation nodes on npm, and webhook, Splunk HEC and SIEM/SOAR alert delivery.
image: https://hacknotice.com/wp-content/uploads/2022/12/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: HackNotice MCP Server
  slug: hacknotice-mcp-server
modified: '2026-08-22'
name: HackNotice
nav: Providers
network: true
overview: 'HackNotice publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, All Business Accounts API, Calc endpoints API, and 5 more. Tagged areas include Company, Security, Threat Intelligence, Cybersecurity, and Dark Web Monitoring.


  The HackNotice catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HackNotice''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Hacknotice Plans Pricing
  plan_count: 4
  slug: hacknotice-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Hacknotice Rate Limits
  slug: hacknotice-rate-limits
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 65.6
    developer_ergonomics: 49.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 52.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hacknotice/refs/heads/main/screenshots/hacknotice-2026-09-02T145647.png
security:
- kind: authentication
  name: Hacknotice Authentication
  slug: hacknotice-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Hacknotice Domain Security
  slug: hacknotice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hacknotice
tags:
- Company
- Security
- Threat Intelligence
- Cybersecurity
- Dark Web Monitoring
- Data Breaches
- Credential Monitoring
- Third-Party Risk
- Vendor Risk Management
- Vulnerability Management
- Ransomware
- Security Assessments
- Alerts
- Monitoring
website: https://hacknotice.com/
---
