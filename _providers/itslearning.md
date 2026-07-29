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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: SOAP web services (DataService, ReadDataService, FileService, FileStreamService, InstanceService) to automate workflows by managing courses, content, files and assessments on an itslearning site. Used
  name: itslearning Organisation API
  slug: itslearning-organisation-api
- description: OData-based reporting and analytics API over a star-schema data warehouse refreshed by a daily overnight ETL, compatible with common BI and reporting tools. Access is granted via the customer's accoun
  name: itslearning Data Warehouse API
  slug: itslearning-data-warehouse-api
- description: Standardized IMS Enterprise web services and SFTP XML imports to manage users, groups and courses (persons, memberships and groups) for provisioning and roster synchronization.
  name: itslearning IMS Enterprise Services
  slug: itslearning-ims-enterprise-services
- description: Learning Tools Interoperability integration supporting LTI 1.3 Core and LTI Advantage (itslearning holds LTI Advantage Complete certification) to securely embed third-party tools and contribute conten
  name: itslearning LTI Integration
  slug: itslearning-lti-integration
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/itslearning-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://itslearning.com/privacy-commitment/responsible-disclosure/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itslearning-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/itslearning-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/itslearning-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itslearning-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/itslearning-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://itslearning.com/privacy-commitment/gdpr
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/itslearning-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.itslearning.com/Content-and-tool-integrations.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/itslearning-llms.txt
- group: company
  title: ''
  type: Website
  url: https://itslearning.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.itslearning.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.itslearning.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.itslearning.com/Content-and-tool-integrations.html
- group: operate
  title: ''
  type: Support
  url: https://itslearning.com/support
- group: company
  title: ''
  type: Blog
  url: https://itslearning.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://itslearning.com/learn/pricing
- group: start
  title: ''
  type: SignUp
  url: https://itslearning.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://eu1.itslearning.com/welcome.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://itslearning.com/privacy-commitment
- group: commercial
  title: ''
  type: TermsOfService
  url: https://itslearning.com/privacy-commitment/gdpr
- group: operate
  title: ''
  type: Roadmap
  url: https://itslearning.com/roadmap
- group: operate
  title: ''
  type: StatusPage
  url: https://status.itslearning.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://itslearning.com/product-updates
created: '2026-07-17'
description: itslearning is a Norwegian learning management system (LMS) founded in 1999 and headquartered in Bergen, Norway, now part of the Sanoma Learning group. Its cloud platform serves primary, secondary, vocational, higher education, lifelong-learning and international schools across Europe and beyond, giving teachers lesson planning ("Plans"), assessment and quizzing, communication, an AI Toolkit, administration and reporting in one place. For integrators itslearning exposes an Organisation API (SOAP web services for courses, content, files and assessments), a Data Warehouse OData reporting API, IMS Enterprise Services and SFTP imports for user/course provisioning, and standards-based Learning Tools Interoperability (LTI 1.3 Core and LTI Advantage, with LTI 1.0/1.1 deprecated since June 2022) for third-party tool and content integration into the itslearning Library.
image: https://itslearning.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: itslearning
nav: Providers
network: true
overview: 'itslearning publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, Education, EdTech, and Learning Management System.


  itslearning''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 50
score:
  band: thin
  composite: 36.7
  delta: 0.7
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 36.0
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itslearning/refs/heads/main/screenshots/itslearning-2026-07-25T223009.png
security:
- kind: authentication
  name: Itslearning Authentication
  slug: itslearning-authentication
  summary_line: oauth2/http/ims-enterprise · 3 schemes
- kind: domain-security
  name: Itslearning Domain Security
  slug: itslearning-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Itslearning Vulnerability Disclosure
  slug: itslearning-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: itslearning
tags:
- Company
- Saas
- Education
- EdTech
- Learning Management System
- LMS
- LTI
- Norway
website: https://itslearning.com/
---
