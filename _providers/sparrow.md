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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparrow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparrow.com/
- group: company
  title: ''
  type: Blog
  url: https://sparrow.com/blog/
- group: operate
  title: ''
  type: FAQ
  url: https://sparrow.com/faq/
- group: start
  title: ''
  type: SignUp
  url: https://app.trysparrow.com/start/
- group: start
  title: ''
  type: Login
  url: https://app.sparrow.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparrow.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sparrow.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trysparrow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sparrowinc/
- group: company
  title: ''
  type: Careers
  url: https://sparrow.com/careers/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trysparrow.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sparrow-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/sparrow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sparrow-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sparrow-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/sparrow-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sparrow-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sparrow-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sparrow-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sparrow-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sparrow-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sparrow-conventions.yml
coverage:
  checked: '2026-08-28'
  detail: 'Sparrow ships leave management only as an end-user web application: its own FAQ answers the integration question with "Sparrow can integrate with your HRIS via file feed", there is no developer portal, and the backend its SPA calls (api.trysparrow.com, named in the app.trysparrow.com Content-Security-Policy) returns a bare 404 to every anonymous path including /openapi.json and every /.well-known/ location.'
  evidence:
  - status: 404
    url: https://api.trysparrow.com/openapi.json
  - status: 200
    url: https://sparrow.com/faq/
  - status: 404
    url: https://sparrow.com/openapi.json
  - status: 200
    url: https://github.com/trysparrow
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: Sparrow is an end-to-end employee leave management platform for employers in the United States and Canada, pairing software with a team of leave specialists to administer FMLA, CFRA, parental, medical and state paid-leave programs. The platform automates employee intake, files the associated insurance claims, coordinates with medical providers, delivers required notices, builds a personalized leave and financial plan for each employee, and reconciles leave pay back into payroll. Sparrow connects to customer HRIS and payroll systems — Workday, BambooHR, Gusto and ADP among them — by file feed rather than through a public developer API, and it publishes no developer portal, OpenAPI or SDK. The company was founded in 2018 in San Francisco by Deborah Hanus and Samarth Keshava, has raised roughly $64M across Series A and Series B rounds, and its shares are quoted on secondary marketplaces such as Forge Global.
image: https://images.ctfassets.net/xtppkev0deqn/wKGxeLeF2NiRU2VbwufDO/2b4373da7eb50e8252d6874221bbb2fe/Sparrow_Preview_Card_Static.png
layout: provider
modified: '2026-08-28'
name: Sparrow
nav: Providers
network: true
overview: 'Sparrow is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Leave Management, Human Resources, HR Tech, and Payroll.


  Sparrow''s developer surface includes engineering blog, FAQ, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Sparrow Plans Pricing
  plan_count: 0
  slug: sparrow-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Sparrow Rate Limits
  slug: sparrow-rate-limits
scopes:
- name: Sparrow Scopes
  scope_count: 0
  slug: sparrow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 22.5
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sparrow/refs/heads/main/screenshots/sparrow-2026-09-02T160337.png
security:
- kind: authentication
  name: Sparrow Authentication
  slug: sparrow-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sparrow Domain Security
  slug: sparrow-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sparrow Vulnerability Disclosure
  slug: sparrow-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Sparrow Trust Center
  slug: sparrow-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27001 Statement of Applicability, ISO/IEC 27701, ISO 22301, GDPR, CCPA, PIPEDA
slug: sparrow
tags:
- Company
- Leave Management
- Human Resources
- HR Tech
- Payroll
- Compliance
- Employee Benefits
- Absence Management
- Software-as-a-Service
website: https://sparrow.com/
---
