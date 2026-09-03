---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: documented
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
  score: 23.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The ALEX Partner Integration API lets a Jellyvision partner — typically a benefits administration or enrollment platform — streamline and personalize the ALEX experience for its end users. Partners PO
  name: ALEX Partner Integration API
  slug: alex-partner-integration-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/jellyvision-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.jellyvision.com/
- group: docs
  title: ''
  type: Documentation
  url: https://partner-api-docs.myalex.com/
- group: docs
  title: ''
  type: APIReference
  url: https://partner-api-docs.myalex.com/
- group: company
  title: ''
  type: Blog
  url: https://www.jellyvision.com/resources/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.jellyvision.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://www.jellyvision.com/get-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jellyvision.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jellyvision.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jellyvision
- group: auth
  title: ''
  type: Compliance
  url: https://www.jellyvision.com/security/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jellyvision-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jellyvision-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jellyvision-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/jellyvision-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jellyvision-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jellyvision-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jellyvision-plans-pricing.yml
created: '2026-08-23'
description: Jellyvision (The Jellyvision Lab, Inc.) is a Chicago-based employee benefits engagement company and the maker of ALEX, a benefits decision-support, communication and administration platform used by employers, brokers and carriers to guide employees through medical, dental, vision, retirement, HSA/FSA and voluntary benefit choices. Its developer surface is the ALEX Partner Integration API — a partner-facing REST API documented publicly at partner-api-docs.myalex.com that lets benefits administration and enrollment platforms pre-populate end-user demographic and eligibility data, push per-plan premium and employer healthfund contribution tiers into an ALEX Session, and read back the medical, dental, vision, HSA and FSA selections a user made inside the ALEX experience. Authentication is OAuth 2.0 client credentials against an Auth0 tenant plus SAML 2.0 IdP-initiated single sign-on for the end-user experience.
image: https://www.jellyvision.com/wp-content/uploads/2023/12/Jellyvision_Generic.jpg
layout: provider
mcp_servers:
- description: ''
  name: Jellyvision MCP Server
  slug: jellyvision-mcp-server
modified: '2026-08-23'
name: Jellyvision
nav: Providers
network: true
overview: 'Jellyvision publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employee Benefits, Human Resources, Benefits Administration, and Benefits Enrollment.


  Jellyvision''s developer surface includes documentation, API reference, engineering blog, support, signup flow, and 13 more developer resources.'
plans:
- name: Jellyvision Plans Pricing
  plan_count: 0
  slug: jellyvision-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Jellyvision Rate Limits
  slug: jellyvision-rate-limits
scopes:
- name: Jellyvision Scopes
  scope_count: 0
  slug: jellyvision-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jellyvision/refs/heads/main/screenshots/jellyvision-2026-09-02T145934.png
security:
- kind: authentication
  name: Jellyvision Authentication
  slug: jellyvision-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Jellyvision Domain Security
  slug: jellyvision-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Jellyvision Trust Center
  slug: jellyvision-trust-center
  summary_line: SOC 2, HIPAA
slug: jellyvision
tags:
- Company
- Employee Benefits
- Human Resources
- Benefits Administration
- Benefits Enrollment
- Health Insurance
- Decision Support
- HR Technology
- Insurance
- Employee Engagement
website: https://www.jellyvision.com/
---
