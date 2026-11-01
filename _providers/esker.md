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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-31'
api_count: 3
apis:
- description: 'Entry point of the Esker on Demand Web Service: retrieves the service bindings (GetBindings) and opens or closes an authenticated session (Login, Logout, GetSessionInformation). SOAP 1.1 service (urn:'
  name: Esker on Demand Session Service
  slug: esker-on-demand-session-service
- description: Manages documents and submits them to Esker on Demand for processing and delivery (fax, mail, email and other transports). SOAP 1.1 service (urn:SubmissionService2); the docs require calling SessionSe
  name: Esker on Demand Submission Service
  slug: esker-on-demand-submission-service
- description: 'Queries and manages documents already submitted to Esker on Demand: query transports, attachments and statistics, download files, approve, cancel and resubmit. SOAP 1.1 service (urn:QueryService2); th'
  name: Esker on Demand Query Service
  slug: esker-on-demand-query-service
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/esker/conventions/esker-conventions.yml
  title: ''
  type: Conventions
  url: conventions/esker-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.esker.com/capabilities/security-certifications/
- group: auth
  href: https://artifacts.apis.io/esker/authentication/esker-authentication.yml
  title: ''
  type: Authentication
  url: authentication/esker-authentication.yml
- group: operate
  href: https://artifacts.apis.io/esker/lifecycle/esker-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/esker-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/esker/lifecycle/esker-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/esker-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/esker/conformance/esker-conformance.yml
  title: ''
  type: Conformance
  url: conformance/esker-conformance.yml
- group: agent
  href: https://artifacts.apis.io/esker/llms/esker-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/esker-llms.txt
- group: agent
  href: https://artifacts.apis.io/esker/well-known/esker-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/esker-well-known.yml
- group: other
  href: https://artifacts.apis.io/esker/hosts/esker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esker-hosts.yml
- group: other
  href: https://artifacts.apis.io/esker/vendors/esker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esker-vendors.yml
- group: build
  href: https://artifacts.apis.io/esker/packages/esker-packages.yml
  title: ''
  type: SDKs
  url: packages/esker-packages.yml
- group: build
  href: https://artifacts.apis.io/esker/packages/esker-packages.yml
  title: ''
  type: Packages
  url: packages/esker-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.esker.com/company/press
- group: other
  title: ''
  type: Leadership
  url: https://www.esker.com/company/leadership/
- group: auth
  href: https://artifacts.apis.io/esker/security/esker-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esker-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/esker/security/esker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.esker.com/index.asp
- group: docs
  title: ''
  type: APIReference
  url: https://doc.esker.com/eskerondemand/cv_ly/en/webservices/Content/Introduction_v2.html
- group: company
  title: ''
  type: Blog
  url: https://www.esker.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.esker.com/customer-enablement/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://esker.my.site.com/
- group: auth
  title: ''
  type: Security
  url: https://www.esker.com/capabilities/security-certifications/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.esker.com/terms-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.esker.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/esker/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/eskersa
created: '2026-10-18'
description: Esker is a software company that automates document-driven business processes for the Office of the CFO, with cloud solutions spanning Source-to-Pay (accounts payable, procurement) and Order-to-Cash (order management, credit, collections, e-invoicing), plus document delivery, fax (VSI-Fax) and terminal emulation products. Its site describes them as document automation and order management software that helps businesses cut costs and increase efficiencies. Developers integrate through the Esker on Demand Web Services API (SOAP/WSDL session, submission and query services), documented at doc.esker.com.
image: https://www.esker.com/sites/default/files/screenshot_home_us.jpg
layout: provider
modified: '2026-10-18'
name: Esker
nav: Providers
network: true
overview: 'Esker is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounts Payable, Order-to-Cash, Source-to-Pay, and Document Automation.


  Esker''s developer surface includes authentication, documentation, API reference, engineering blog, support, YouTube channel, and 21 more developer resources.'
plans:
- name: Esker Plans Pricing
  plan_count: 0
  slug: esker-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Esker Rate Limits
  slug: esker-rate-limits
scopes:
- name: Esker Scopes
  scope_count: 0
  slug: esker-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 75.0
    operational_transparency: 18.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Esker Authentication
  slug: esker-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Esker Domain Security
  slug: esker-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Esker Trust Center
  slug: esker-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: esker
tags:
- Company
- Accounts Payable
- Order-to-Cash
- Source-to-Pay
- Document Automation
- E-Invoicing
- Procurement
- SOAP
website: https://www.esker.com/
---
