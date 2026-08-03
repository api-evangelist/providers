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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The signed-request platform API behind the UrbanLogiq community intelligence platform — data catalog objects, aggregate queries, and streams served in Apache Arrow, Parquet, CSV, XLSX, JSON, text, and
  name: UrbanLogiq Platform API
  slug: urbanlogiq-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/urbanlogiq-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://urbanlogiq.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urbanlogiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://urbanlogiq.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/urbanlogiq/ulsdk#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/urbanlogiq
- group: company
  title: ''
  type: Blog
  url: https://urbanlogiq.com/resources/blog
- group: operate
  title: ''
  type: Support
  url: https://urbanlogiq.com/resources/faqs
- group: company
  title: ''
  type: Careers
  url: https://urbanlogiq.com/resources/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://urbanlogiq.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://urbanlogiq.com/terms-and-conditions
- group: auth
  title: ''
  type: TrustCenter
  url: security/urbanlogiq-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://urbanlogiq.com/trust-center
- group: build
  title: ''
  type: Packages
  url: packages/urbanlogiq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/urbanlogiq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/urbanlogiq-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urbanlogiq-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/urbanlogiq-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urbanlogiq-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urbanlogiq-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urbanlogiq-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urbanlogiq-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/urbanlogiq-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/urbanlogiq-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/urbanlogiq-lifecycle.yml
created: '2026-07-17'
description: UrbanLogiq (CommunityLogiq Software, Inc.) is a community intelligence platform that helps government leaders make faster, data-driven decisions by unifying siloed departmental data across transportation, planning, public safety, and economic development. The platform spans data integration, predictive modeling, cross-domain analytics, and governed generative AI (Ethica), and is served by a signed-request platform API with an official open source multi-language SDK (C++, Go, Java, Python, Rust, TypeScript) and CLI. Customers include the City of Toronto, Chicago DOT, the State of Hawaii, and Texas DOT; the service runs in separate US and Canada environments for data residency and is ISO/IEC 27001, 27701, 27017, and 27018 certified.
image: https://storage.googleapis.com/gpt-engineer-file-uploads/iMsRxc6pmShB43YLqbITcQTBj7L2/social-images/social-1774310251571-colored_ul_logo.webp
layout: provider
mcp_servers:
- description: ''
  name: urbanlogiq-mcp.yml
  slug: urbanlogiq-mcpyml
modified: '2026-07-21'
name: UrbanLogiq
nav: Providers
network: true
overview: 'UrbanLogiq publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, GovTech, Data, and Analytics.


  UrbanLogiq''s developer surface includes documentation, engineering blog, support, CLI, authentication, sandbox, and 19 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 34.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 66.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Urbanlogiq Authentication
  slug: urbanlogiq-authentication
  summary_line: signedRequest/bearer · 2 schemes
- kind: domain-security
  name: Urbanlogiq Domain Security
  slug: urbanlogiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Urbanlogiq Vulnerability Disclosure
  slug: urbanlogiq-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Urbanlogiq Trust Center
  slug: urbanlogiq-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO/IEC 27017:2015, ISO/IEC 27018:2019
slug: urbanlogiq
tags:
- Company
- Government
- GovTech
- Data
- Analytics
- Transportation
- Urban Planning
- Public Safety
- Economic Development
- Artificial Intelligence
website: https://urbanlogiq.com
---
