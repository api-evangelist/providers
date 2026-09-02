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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Staffbase employee experience platform — manage users, groups, news, pages, media, notifications, spaces, campaigns, analytics, and audit logs. Authenticated with HTTP Basic auth carr
  name: Staffbase Platform API
  slug: staffbase-platform-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://staffbase.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.staffbase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.staffbase.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.staffbase.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.staffbase.com/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.staffbase.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://developers.staffbase.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.staffbase.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.staffbase.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Staffbase
- group: commercial
  title: ''
  type: Pricing
  url: https://staffbase.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.staffbase.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://staffbase.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://staffbase.com/legal/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://staffbase.com/en/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.staffbase.com/
- group: auth
  title: ''
  type: Security
  url: https://staffbase.com/security/bug-bounty
- group: auth
  title: ''
  type: Authentication
  url: authentication/staffbase-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/staffbase-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/staffbase-packages.yml
- group: design
  title: ''
  type: Components
  url: components/staffbase-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/staffbase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/staffbase-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/staffbase-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/staffbase-security.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/staffbase-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/staffbase-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/staffbase-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/staffbase-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/staffbase-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/staffbase-vulnerability-disclosure.yml
created: '2026-07-17'
description: Staffbase is an AI-native employee experience and internal-communications platform that connects workforce communications across an intranet, a branded employee mobile app, email and newsletters, and an AI-powered knowledge assistant. Used by more than 1,500 enterprises, it is built to reach hard-to-reach frontline, shift, and distributed employees on every channel. Staffbase exposes a Platform API (HTTP Basic auth with an API token, base https://app.staffbase.com/api) covering users, groups, news, pages, media, notifications, spaces, campaigns, analytics, and audit logs, plus first-party Plugins and Custom-Widget SDKs (JavaScript, Node.js, PHP, Java) for embedding apps and widgets inside the Staffbase experience. Backed by Insight Partners.
image: https://logo.clearbit.com/staffbase.com
layout: provider
mcp_servers:
- description: ''
  name: Staffbase MCP Server
  slug: staffbase-mcp-server
modified: '2026-07-21'
name: Staffbase
nav: Providers
network: true
overview: 'Staffbase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Communications, Internal Communications, Employee Experience, and Intranet.


  Staffbase''s developer surface includes documentation, API reference, getting-started guide, changelog, engineering blog, support, pricing, and 24 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 37.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Staffbase Authentication
  slug: staffbase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Staffbase Domain Security
  slug: staffbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Staffbase Vulnerability Disclosure
  slug: staffbase-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Staffbase Trust Center
  slug: staffbase-trust-center
  summary_line: ISO 27001, SOC 2, GDPR, HIPAA, CCPA
slug: staffbase
tags:
- Company
- Employee Communications
- Internal Communications
- Employee Experience
- Intranet
- Employee App
- Email
- HR Tech
- Enterprise
website: https://staffbase.com/en/
---
