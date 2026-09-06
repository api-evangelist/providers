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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 44
  human_in_the_loop: 10
  name: Plansource Agentic Access
  operation_count: 80
  slug: plansource-agentic-access
  summary_line: 80 operations · 44 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Affordable Care Act data.
  name: PlanSource ACA API
  slug: plansource-aca-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Administrator Management
  name: PlanSource Administrators API
  slug: plansource-administrators-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Collections of objects.
  name: PlanSource Collections API
  slug: plansource-collections-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Coverages, coverage lines, and dependent coverages.
  name: PlanSource Coverage API
  slug: plansource-coverage-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Subscribers, their dependents and beneficiaries.
  name: PlanSource Demographic API
  slug: plansource-demographic-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Evidence of Insurability Processing.
  name: PlanSource EOI API
  slug: plansource-eoi-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Organization page content data.
  name: PlanSource Page Content API
  slug: plansource-page-content-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Payroll coverages data.
  name: PlanSource Payroll API
  slug: plansource-payroll-api
- baseURL: https://api.plansource.com/admin/v2
  baseurl_source: declared
  description: Security Functions
  name: PlanSource Security API
  slug: plansource-security-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plansource Admin ACA API
  slug: open-plansource-aca-api
- collection_type: open
  name: Plansource Admin Administrators API
  slug: open-plansource-administrators-api
- collection_type: open
  name: Plansource Admin All API
  slug: open-plansource-all-api
- collection_type: open
  name: Plansource Admin Collections API
  slug: open-plansource-collections-api
- collection_type: open
  name: Plansource Admin Composites API
  slug: open-plansource-composites-api
- collection_type: open
  name: Plansource Admin Coverage API
  slug: open-plansource-coverage-api
- collection_type: open
  name: Plansource Admin Demographic API
  slug: open-plansource-demographic-api
- collection_type: open
  name: Plansource Admin EOI API
  slug: open-plansource-eoi-api
- collection_type: open
  name: Plansource Admin Page Content API
  slug: open-plansource-page-content-api
- collection_type: open
  name: Plansource Admin Payroll API
  slug: open-plansource-payroll-api
- collection_type: open
  name: Plansource Admin Processing API
  slug: open-plansource-processing-api
- collection_type: open
  name: Plansource Admin Resources API
  slug: open-plansource-resources-api
- collection_type: open
  name: Plansource Admin Security API
  slug: open-plansource-security-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/plansource-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/plansource-admin-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://plansource.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.plansource.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.plansource.com/docs/plansource-administrative-api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.plansource.com/v2.0/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.plansource.com/docs/utilize-postman
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/93f063e64815e4122102
- group: operate
  title: ''
  type: Support
  url: https://developer.plansource.com/docs/contact-support
- group: company
  title: ''
  type: Blog
  url: https://plansource.com/blog/
- group: start
  title: ''
  type: Login
  url: https://benefits.plansource.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plansource.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plansource.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: security/plansource-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.plansource.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plansource-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plansource-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plansource-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plansource-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plansource-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plansource-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plansource-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plansource-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plansource-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plansource-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plansource-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plansource-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/plansource-examples.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plansource-agentic-access.yml
created: '2026-08-06'
description: PlanSource is a benefits administration and employee-benefits engagement platform used by employers, brokers, carriers and HR/payroll partners to run enrollment, eligibility, billing and benefits communication. Its public developer surface is the PlanSource Benefits Administration API (Admin API v2), a RESTful HTTPS API of 80 operations across 62 paths covering employee (subscriber) demographics, dependents, beneficiaries, coverages and stacked coverage lines, payroll deductions with lookup codes and pre-tax/post-tax/employer/imputed amounts, Evidence of Insurability decisions and form completions, ACA offer and enrollee reporting data, administrator accounts, and organization portal page content. It is designed to replace fixed-schedule EDI files with near real-time sync between an HCM/payroll system of record and PlanSource. Authentication is OAuth 2.0 client credentials (scope admin_api_v2) or a legacy AuthenticationString + Signature header pair, with OpenID Connect and
  SAML 2.0 available for end-user single sign-on. The API is documented on a ReadMe developer portal that publishes llms.txt, an agent-skills manifest and an OAuth-gated MCP server, and PlanSource maintains a SafeBase trust center listing SOC 2 Type 2, ISO/IEC 27001:2022, HIPAA, CCPA and 23 NYCRR 500.
image: https://plansource.com/wp-content/uploads/2026/01/ps_social-share-img.webp
layout: provider
mcp_servers:
- description: ''
  name: PlanSource MCP Server
  slug: plansource-mcp-server
modified: '2026-08-06'
name: PlanSource
nav: Providers
network: true
overview: 'PlanSource publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ACA API, Administrators API, Collections API, and 6 more. Tagged areas include Employee Benefits, Benefits Administration, Insurance, Human Resources, and Payroll.


  PlanSource''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 23 more developer resources.'
random_paper: 13
scopes:
- name: Plansource Scopes
  scope_count: 8
  slug: plansource-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plansource/refs/heads/main/screenshots/plansource-2026-08-17T081304.png
security:
- kind: authentication
  name: Plansource Authentication
  slug: plansource-authentication
  summary_line: oauth2/apiKey/openIdConnect/saml2 · 5 schemes
- kind: domain-security
  name: Plansource Domain Security
  slug: plansource-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plansource Trust Center
  slug: plansource-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, HIPAA, CCPA, 23 NYCRR 500
slug: plansource
tags:
- Employee Benefits
- Benefits Administration
- Insurance
- Human Resources
- Payroll
- Health Insurance
- Enrollment
- HR Technology
- Evidence of Insurability
- ACA Reporting
- Eligibility
- Single Sign-On
website: https://plansource.com/
---
