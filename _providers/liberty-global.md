---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Liberty Global Agentic Access
  operation_count: 14
  slug: liberty-global-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 3
apis:
- description: The ASMS (AppStore Metadata Service) REST API from Liberty Global Technology Services BV — the MAS API in RDK. Manages application metadata and maintainer records for the RDK-based set-top box app sto
  name: AppStore Metadata Service API
  slug: appstore-metadata-service-api
- description: The AppStore Bundle Service API from Liberty Global Technology Services BV handles the application bundle generation process by interacting with the Bundle Generator and Bundle Cryptor services, expos
  name: AppStore Bundle Service API
  slug: appstore-bundle-service-api
- description: The AppStore Caching Service API from Liberty Global Technology Services BV acts as a caching proxy in front of the AppStore Bundle Service, serving generated application bundles addressed by applicat
  name: AppStore Caching Service API
  slug: appstore-caching-service-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/liberty-global-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liberty-global-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.libertyglobal.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LibertyGlobal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/liberty-global
- group: company
  title: ''
  type: Blog
  url: https://www.libertyglobal.com/news-insights/insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.libertyglobal.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://www.libertyglobal.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.libertyglobal.com/legal-notices/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.libertyglobal.com/privacy-and-security-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.libertyglobal.com/about/corporate-governance/data-privacy-protection/
- group: design
  title: ''
  type: Conformance
  url: conformance/liberty-global-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/liberty-global-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liberty-global-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/liberty-global-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/liberty-global-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liberty-global-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/liberty-global-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/liberty-global-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/liberty-global-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liberty-global-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liberty-global-llms.txt
created: '2026-07-25'
description: 'Liberty Global is a London-headquartered converged connectivity group that owns and operates fixed-broadband and mobile networks across Europe, mostly through joint ventures rather than under its own brand — Virgin Media O2 in the United Kingdom (50/50 with Telefonica), VodafoneZiggo in the Netherlands (50/50 with Vodafone Group), Telenet in Belgium, and Virgin Media Ireland — serving roughly 80 million connections over fibre-rich broadband and 5G. It sits in the value chain as a network owner and holding company, not as a developer-facing platform. Liberty Global has been a GSMA Open Gateway participant since the initiative launched at MWC 2023 and announced a Network-as-a-Service framework with AWS in February 2024 built on CAMARA standard APIs, but its API posture toward developers is partner-gated and indirect: there is no first-party developer portal on libertyglobal.com — the developer.libertyglobal.com hostname advertised on its own GitHub organisation profile does not
  resolve — and every callable CAMARA network API reaches the market through the operating joint ventures (Virgin Media O2''s UK KYC Age Verify, KYC Tenure and SIM Swap APIs; VodafoneZiggo''s four Dutch network APIs) or through the operators'' shared channels, never from the parent. The only OpenAPI definitions Liberty Global itself publishes are the Apache-2.0 RDK App Store service specs in its public GitHub organisation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Liberty Global
nav: Providers
network: true
overview: 'Liberty Global publishes 3 APIs on the [APIs.io](https://apis.io/) network: AppStore Metadata Service API, AppStore Bundle Service API, and AppStore Caching Service API. Tagged areas include Telecommunications, United Kingdom, Broadband, Fixed Broadband, and Mobile Network Operator.


  Liberty Global''s developer surface includes engineering blog, authentication, changelog, sandbox, and 19 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 40.1
    developer_ergonomics: 21.2
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Liberty Global Authentication
  slug: liberty-global-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Liberty Global Domain Security
  slug: liberty-global-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Liberty Global Vulnerability Disclosure
  slug: liberty-global-vulnerability-disclosure
  summary_line: Hackerone
slug: liberty-global
tags:
- Telecommunications
- United Kingdom
- Broadband
- Fixed Broadband
- Mobile Network Operator
- Network APIs
- CAMARA
- Open Gateway
- 5G
- Europe
- Set-Top Box
- RDK
website: https://www.libertyglobal.com/
---
