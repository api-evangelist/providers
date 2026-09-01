---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'An OAuth 2.1-protected Model Context Protocol (MCP) server exposed on DispatchHealth''s own host by the WordPress MCP adapter running on www.dispatchhealth.com. Discovery is fully machine-readable: RFC'
  name: DispatchHealth MCP Server
  slug: dispatchhealth-mcp-server
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dispatchhealth-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dispatchhealth-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dispatchhealth-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dispatchhealth-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dispatchhealth-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dispatchhealth-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/dispatchhealth-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.dispatchhealth.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dispatchhealth-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.dispatchhealth.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/dispatchhealth_stock/
- group: company
  title: ''
  type: About
  url: https://www.dispatchhealth.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.dispatchhealth.com/blog/
- group: company
  title: ''
  type: Press
  url: https://www.dispatchhealth.com/press-room/
- group: operate
  title: ''
  type: Support
  url: https://www.dispatchhealth.com/get-in-touch/
- group: operate
  title: ''
  type: FAQ
  url: https://www.dispatchhealth.com/faq/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dispatchhealth.com/cost-insurance-coverage/
- group: start
  title: ''
  type: SignUp
  url: https://request.dispatchhealth.com/
- group: start
  title: ''
  type: Login
  url: https://express.dispatchhealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dispatchhealth.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dispatchhealth.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DispatchHealth
- group: company
  title: ''
  type: Partners
  url: https://www.dispatchhealth.com/partners/
- group: other
  title: ''
  type: Technology
  url: https://www.dispatchhealth.com/technology/
- group: company
  title: ''
  type: Careers
  url: https://www.dispatchhealth.com/careers/
- group: other
  title: ''
  type: Locations
  url: https://www.dispatchhealth.com/locations/
created: '2026-07-31'
description: DispatchHealth is a Denver, Colorado-based provider of complex medical care in the home, founded in 2013 and merged with Medically Home in June 2025 to create one of the largest hospital-at-home platforms in the United States. The combined company delivers same-day urgent care, hospital-alternative (hospital-at-home) care, transitional and recovery care across roughly 50 metropolitan areas in partnership with nearly 40 health systems and national payers. Its CESIA technology platform handles rules-based and AI-assisted care planning, dispatching, routing, scheduling, care-team status, real-time two-way patient communications and field equipment tracking, and is designed to integrate with a partner health system's existing EMR rather than replace it. DispatchHealth partners access the platform through the Dispatch Express portal and patients through an online request flow; the company publishes no public developer portal, API documentation, or machine-readable API contract as
  of this profiling pass.
image: https://www.dispatchhealth.com/wp-content/uploads/2025/07/dispatchhealth-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: DispatchHealth MCP Server
  slug: dispatchhealth-mcp-server
modified: '2026-07-31'
name: DispatchHealth
nav: Providers
network: true
overview: 'DispatchHealth publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Systems, Hospital at Home, and Home Health.


  DispatchHealth''s developer surface includes authentication, engineering blog, support, FAQ, pricing, signup flow, and 20 more developer resources.'
random_paper: 8
scopes:
- name: Dispatchhealth Scopes
  scope_count: 1
  slug: dispatchhealth-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 30.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dispatchhealth/refs/heads/main/screenshots/dispatchhealth-2026-08-07T164356.png
security:
- kind: authentication
  name: Dispatchhealth Authentication
  slug: dispatchhealth-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Dispatchhealth Domain Security
  slug: dispatchhealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Dispatchhealth Trust Center
  slug: dispatchhealth-trust-center
  summary_line: trust center published
slug: dispatchhealth
tags:
- Company
- Healthcare
- Health Systems
- Hospital at Home
- Home Health
- Urgent Care
- Care Delivery
- Medical Services
- Telehealth
- Digital Health
website: https://www.dispatchhealth.com/
---
