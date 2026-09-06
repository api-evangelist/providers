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
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: JSON over HTTPS REST API for the M-Files information management platform. Served per M-Files Server / Cloud vault under a /REST/ base path; supports objects, files, vaults, views, value lists, and sea
  name: M-Files Web Service (MFWS) REST API
  slug: m-files-web-service-mfws-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.m-files.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.m-files.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.m-files.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.m-files.com/APIs/REST-API/Reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.m-files.com/Getting-Started/
- group: operate
  title: ''
  type: Support
  url: https://support.m-files.com/
- group: company
  title: ''
  type: Blog
  url: https://www.m-files.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/m-files
- group: commercial
  title: ''
  type: Pricing
  url: https://www.m-files.com/editions/
- group: start
  title: ''
  type: SignUp
  url: https://www.m-files.com/try-m-files/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.m-files.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.m-files.com/about/trust-center/
- group: auth
  title: ''
  type: Compliance
  url: https://www.m-files.com/about/trust-center/
- group: build
  title: ''
  type: Packages
  url: packages/m-files-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/m-files-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/m-files-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/m-files-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/m-files-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/m-files-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/m-files-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/m-files-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.m-files.com/about/trust-center/
- group: auth
  title: ''
  type: TrustCenter
  url: security/m-files-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/m-files-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/m-files-well-known.yml
created: '2026-07-17'
description: M-Files is a metadata-driven document and information management platform that connects documents to their business context, turning disconnected files into connected, trusted information. It provides AI-powered document management with built-in governance, workflow and document automation, and compliance, and integrates deeply with Microsoft 365. Trusted by 6,000+ organizations, M-Files exposes developer access through the M-Files Web Service (MFWS) REST API, a COM/.NET API, and the UIX and Vault Application Framework (VAF) extensibility frameworks. It was surfaced as a portfolio company of Partech.
image: https://www.m-files.com/favicon.ico
layout: provider
modified: '2026-07-20'
name: M-Files
nav: Providers
network: true
overview: 'M-Files publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure Saas, Document-Management, Information Management, and Content Services.


  M-Files'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 33.4
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/m-files/refs/heads/main/screenshots/m-files-2026-07-25T225802.png
security:
- kind: authentication
  name: M Files Authentication
  slug: m-files-authentication
  summary_line: oauth2/apiKey/http · 6 schemes
- kind: domain-security
  name: M Files Domain Security
  slug: m-files-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: M Files Vulnerability Disclosure
  slug: m-files-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: M Files Trust Center
  slug: m-files-trust-center
  summary_line: ISO/IEC 27001, SOC 2, GDPR
slug: m-files
tags:
- Company
- Infrastructure Saas
- Document-Management
- Information Management
- Content Services
- Workflow-Automation
- Compliance
- Enterprise Content Management
website: https://www.m-files.com/
---
