---
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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cybrary Agentic Access
  operation_count: 3
  slug: cybrary-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Daily completion-event exports as xAPI statements.
  name: Cybrary Completions API
  slug: cybrary-completions-api
artifact_total: 8
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cybrary-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.cybrary.it/
- group: docs
  title: ''
  type: Documentation
  url: https://help.cybrary.it/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://help.cybrary.it/completions-export-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cybrary.it/cybrary-for-teams
- group: operate
  title: ''
  type: Support
  url: https://help.cybrary.it/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.cybrary.it/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cybrary.it/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cybrary
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cybrary.it/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cybrary.it/register
- group: start
  title: ''
  type: Login
  url: https://app.cybrary.it/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cybrary.it/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cybrary.it/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.cybrary.it/responsible-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cybrary-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cybrary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cybrary-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cybrary-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cybrary-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cybrary-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cybrary-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cybrary-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cybrary-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cybrary-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cybrary-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/cybrary-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cybrary-agentic-access.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cybrary-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cybrary-completions-export-overlay.yaml
created: '2026-08-04'
description: Cybrary is a cybersecurity and IT skills-development platform used by individuals and enterprise teams for hands-on training, certification preparation and workforce upskilling. The catalog spans certification prep paths (Security+, CISSP, CISA, CISM, CCSP, CCNA, AWS security tracks), role-based career paths (SOC analyst, penetration tester, security engineer, incident handler, network engineer), skill paths, virtual labs, assessments and security awareness training. Cybrary for Teams adds administrative surfaces for enterprise customers — SAML 2.0 single sign-on with Okta, OneLogin and Microsoft Entra ID, SCIM 2.0 automated user provisioning with a per-tenant base URL and bearer token, bulk user upload, goals and custom career paths. Its one publicly documented API is the Completions Export Integration, an OAuth 2.0 client-credentials REST API that returns daily course, lab, assessment and career-path completion events as xAPI (Experience API) statements for ingestion into
  a customer LMS, HRIS or reporting warehouse.
image: https://cdn.prod.website-files.com/63eef15e3ff8fd318e9a6888/645ef224f84b330beefae1e7_Cybrary%20Opengraph%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: cybrary-mcp.yml
  slug: cybrary-mcpyml
modified: '2026-08-04'
name: Cybrary
nav: Providers
network: true
overview: 'Cybrary publishes 1 API on the [APIs.io](https://apis.io/) network: Completions API. Tagged areas include Company, Cybersecurity, Training, Education, and Learning Management.


  Cybrary''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 44
rate_limits:
- limit_count: 2
  name: Cybrary Rate Limits
  slug: cybrary-rate-limits
scopes:
- name: Cybrary Scopes
  scope_count: 1
  slug: cybrary-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 16.4
    developer_ergonomics: 47.3
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cybrary/refs/heads/main/screenshots/cybrary-2026-08-07T164005.png
security:
- kind: authentication
  name: Cybrary Authentication
  slug: cybrary-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cybrary Domain Security
  slug: cybrary-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cybrary Vulnerability Disclosure
  slug: cybrary-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cybrary
tags:
- Company
- Cybersecurity
- Training
- Education
- Learning Management
- Certification
- Workforce Development
- xAPI
- SCIM
- Security Awareness
website: https://www.cybrary.it/
---
