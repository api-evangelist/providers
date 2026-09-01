---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The SimSpace Portal Suite platform API. SimSpace describes the cyber range platform as built API-first, giving partners and customers programmatic access for custom integrations, automation, advanced '
  name: SimSpace Platform API
  slug: simspace-platform
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://simspace.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.simspace.com/
- group: docs
  title: ''
  type: Documentation
  url: https://simspace.com/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://simspace.com/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.simspace.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://simspace.com/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Simspace
- group: start
  title: ''
  type: SignUp
  url: https://simspace.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://simspace.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simspace.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.simspace.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.simspace.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.simspace.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simspace-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/simspace-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/simspace-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simspace-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/simspace-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/simspace-packages.yml
- group: design
  title: ''
  type: Components
  url: components/simspace-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/simspace-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/simspace-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/simspace-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/simspace-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/simspace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simspace-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/simspace-llms.txt
created: '2026-08-27'
description: SimSpace Corporation builds a realistic, high-fidelity cyber range and simulation platform used by security teams to train people, test technology, and now to train, validate and operationalize AI agents alongside human defenders. The product line spans the AI Proving Grounds, Range Workbench (visual and YAML-as-code range design and versioning), and Team Trainer, delivered through the SimSpace Portal Suite at portal.simspace.com with a European instance at portal-eu.simspace.com. SimSpace serves critical infrastructure, financial services, healthcare, insurance, higher education, US federal and military, state and local, and international government customers. The platform is described by the company as API-first, exposing programmatic access for custom integrations, automation and data extensibility; the platform REST API is served from portal.simspace.com/api/v1 but its reference documentation is published only inside the authenticated portal and the customer-only Freshdesk
  support site, so no public machine-readable contract is available. SimSpace is headquartered in Orlando, Florida.
image: https://simspace.com/wp-content/uploads/2025/10/square_logo_linkedin-x-4x-1.jpg
layout: provider
mcp_servers:
- description: ''
  name: SimSpace MCP Server
  slug: simspace-mcp-server
modified: '2026-08-27'
name: SimSpace
nav: Providers
network: true
overview: 'SimSpace publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Cyber Range, Security Training, and Simulation.


  SimSpace''s developer surface includes documentation, support, engineering blog, signup flow, authentication, changelog, and 21 more developer resources.'
plans:
- name: Simspace Plans Pricing
  plan_count: 0
  slug: simspace-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Simspace Rate Limits
  slug: simspace-rate-limits
scopes:
- name: Simspace Scopes
  scope_count: 0
  slug: simspace-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 39.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 74.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Simspace Authentication
  slug: simspace-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Simspace Domain Security
  slug: simspace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Simspace Trust Center
  slug: simspace-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, CMMC Level 2, CSA STAR Level 1, NIST SP 800-171, GDPR, CCPA, HECVAT Lite
slug: simspace
tags:
- Company
- Cybersecurity
- Cyber Range
- Security Training
- Simulation
- AI Agents
- Security Operations
- Critical Infrastructure
- Government
- Compliance
website: https://simspace.com/
---
