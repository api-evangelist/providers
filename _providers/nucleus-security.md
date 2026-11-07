---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: The Nucleus platform API. Every platform capability is exposed over REST, documented with Swagger inside the authenticated customer console, and authenticated with a static API key in an x-apikey head
  name: Nucleus Security Platform REST API
  slug: nucleus-security-platform-rest-api
- description: Hosted remote Model Context Protocol server included with the Nucleus platform, reachable at a per-tenant URL. Exposes project, asset, finding/vulnerability and Nucleus Query Language tools to AI clie
  name: Nucleus MCP Server
  slug: nucleus-mcp-server
- description: 'The public WordPress REST API (wp-json) of the Nucleus Security website at nucleussec.com: the route index of the site''s content management system, catalogued as one site surface rather than as separa'
  name: Nucleus Security Website (WordPress REST)
  slug: nucleussec-com-website-wordpress-rest
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://nucleussec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.nucleussec.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.nucleussec.com/docs/api-access
- group: start
  title: ''
  type: GettingStarted
  url: https://help.nucleussec.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://nucleussec.atlassian.net/servicedesk/customer/portal/3
- group: company
  title: ''
  type: Blog
  url: https://nucleussec.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nucleus-security
- group: commercial
  title: ''
  type: Pricing
  url: https://nucleussec.com/get-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nucleussec.com/legal/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nucleussec.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nucleussec.com/
- group: auth
  href: https://artifacts.apis.io/nucleus-security/security/nucleus-security-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/nucleus-security-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/security/nucleus-security-trust-center.yml
  title: ''
  type: Compliance
  url: security/nucleus-security-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/security/nucleus-security-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/nucleus-security-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/security/nucleus-security-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nucleus-security-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/well-known/nucleus-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/nucleus-security-security.txt
- group: auth
  href: https://artifacts.apis.io/nucleus-security/security/nucleus-security-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nucleus-security-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/nucleus-security/well-known/nucleus-security-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nucleus-security-well-known.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/scopes/nucleus-security-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nucleus-security-scopes.yml
- group: auth
  href: https://artifacts.apis.io/nucleus-security/authentication/nucleus-security-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nucleus-security-authentication.yml
- group: design
  href: https://artifacts.apis.io/nucleus-security/conventions/nucleus-security-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nucleus-security-conventions.yml
- group: design
  href: https://artifacts.apis.io/nucleus-security/conformance/nucleus-security-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nucleus-security-conformance.yml
- group: design
  href: https://artifacts.apis.io/nucleus-security/errors/nucleus-security-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nucleus-security-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nucleus-security/lifecycle/nucleus-security-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nucleus-security-lifecycle.yml
- group: commercial
  href: https://artifacts.apis.io/nucleus-security/plans/nucleus-security-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nucleus-security-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nucleus-security/rate-limits/nucleus-security-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nucleus-security-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/nucleus-security/packages/nucleus-security-packages.yml
  title: ''
  type: Packages
  url: packages/nucleus-security-packages.yml
- group: design
  href: https://artifacts.apis.io/nucleus-security/data-model/nucleus-security-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nucleus-security-data-model.yml
- group: agent
  href: https://artifacts.apis.io/nucleus-security/mcp/nucleus-security-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nucleus-security-mcp.yml
- group: build
  href: https://artifacts.apis.io/nucleus-security/mcp/nucleus-security-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nucleus-security-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/nucleus-security/llms/nucleus-security-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nucleus-security-llms.txt
- group: agent
  href: https://artifacts.apis.io/nucleus-security/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Nucleus Security is a risk-based vulnerability and exposure management platform that unifies findings from across an organization''s scanning estate - network, application, cloud, container and penetration-test tooling - into a single normalized view, then prioritizes and automates remediation against it. The platform ingests from roughly thirty first-party connectors (Tenable, Qualys, Rapid7, Snyk, Checkmarx, Crowdstrike, Orca, Prisma and others), enriches findings with threat intelligence including CISA KEV, EPSS, CVSS v3/v4 and Nucleus Insights exploitation signals, and drives remediation through ServiceNow, Jira and other ticketing systems. Programmatic access is a first-class deployment model: every platform capability is exposed through an API-key-authenticated REST API documented in-console with Swagger, and Nucleus ships a hosted Model Context Protocol server so AI clients can query Nucleus data under the same RBAC and Asset Group Access Control enforced in the UI.
  Nucleus also publishes an open, unauthenticated vulnerability intelligence API on its corporate domain, and a FedRAMP Moderate government offering, NucleusGov.'
image: https://nucleussec.com/wp-content/uploads/2024/12/cropped-Nucleus-Full-Color-Logo-270x270.png
layout: provider
mcp_servers:
- description: Nucleus Security operates TWO distinct, real, remote Model Context Protocol servers. The product server is a documented per-tenant endpoint on the customer's own Nucleus instance; the website server i
  name: Nucleus Security MCP Servers
  slug: nucleus-security-mcp-servers
modified: '2026-08-26'
name: Nucleus Security
nav: Providers
network: true
overview: 'Nucleus Security publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Cybersecurity, Vulnerability Management, and Exposure Management.


  Nucleus Security''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 25 more developer resources.'
plans:
- name: Nucleus Security Plans Pricing
  plan_count: 0
  slug: nucleus-security-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Nucleus Security Rate Limits
  slug: nucleus-security-rate-limits
scopes:
- name: Nucleus Security Scopes
  scope_count: 1
  slug: nucleus-security-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 49.4
    discoverability: 60.0
    operational_transparency: 28.9
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nucleus-security/nucleus-security-2026-09-02T150811.png
security:
- kind: authentication
  name: Nucleus Security Authentication
  slug: nucleus-security-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nucleus Security Domain Security
  slug: nucleus-security-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nucleus Security Vulnerability Disclosure
  slug: nucleus-security-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Nucleus Security Trust Center
  slug: nucleus-security-trust-center
  summary_line: SOC 2 Type II, FedRAMP Moderate, NIST CSF, CISA Secure by Design Pledge
skill_count: 2
skills:
- name: nucleus-security-monitor-platform-status
  slug: nucleus-security-monitor-platform-status
- name: nucleus-security-triage-exploited-cves
  slug: nucleus-security-triage-exploited-cves
slug: nucleus-security
tags:
- Company
- Security
- Cybersecurity
- Vulnerability Management
- Exposure Management
- Risk Management
- Threat Intelligence
- Compliance
- DevSecOps
- MCP
website: https://nucleussec.com/
---
