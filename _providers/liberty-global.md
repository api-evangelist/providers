---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Liberty Global Agentic Access
  operation_count: 14
  slug: liberty-global-agentic-access
  summary_line: 14 operations · 6 acting
api_count: 3
apis:
- description: The Applications API from Liberty Global — 2 operation(s) for applications.
  name: Liberty Global Applications API
  slug: liberty-global-applications-api
- description: The Maintainer API from Liberty Global — 4 operation(s) for maintainer.
  name: Liberty Global Maintainer API
  slug: liberty-global-maintainer-api
- description: The STB API from Liberty Global — 2 operation(s) for stb.
  name: Liberty Global STB API
  slug: liberty-global-stb-api
artifact_total: 10
collections:
- collection_type: open
  name: AppStore Bundle Service API
  slug: open-liberty-global-appstore-bundle-service
- collection_type: open
  name: AppStore Caching Service API
  slug: open-liberty-global-appstore-caching-service
- collection_type: open
  name: ASMS API
  slug: open-liberty-global-appstore-metadata-service
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/liberty-global-appstore-metadata-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/liberty-global-appstore-bundle-service-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/liberty-global-appstore-caching-service-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/liberty-global-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/LibertyGlobal/appstore-metadata-service/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/LibertyGlobal/appstore-metadata-service/blob/master/LICENSE
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
overview: 'Liberty Global publishes 3 APIs on the [APIs.io](https://apis.io/) network: Applications API, Maintainer API, and STB API. Tagged areas include Telecommunications, United Kingdom, Broadband, Fixed Broadband, and Mobile Network Operator.


  Liberty Global''s developer surface includes engineering blog, authentication, changelog, sandbox, and 25 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 43.1
    developer_ergonomics: 39.9
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 40.7
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/liberty-global/refs/heads/main/screenshots/liberty-global-2026-08-07T171613.png
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
