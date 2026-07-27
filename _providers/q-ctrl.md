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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Hosted GraphQL API behind the Q-CTRL Boulder Opal and Fire Opal Python clients. Not published as a public OpenAPI/REST spec; accessed via the official SDKs with an account-issued API key.
  name: Q-CTRL Cloud API
  slug: q-ctrl-cloud-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://q-ctrl.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.q-ctrl.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.q-ctrl.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.q-ctrl.com/boulder-opal/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qctrl
- group: start
  title: ''
  type: SignUp
  url: https://accounts.q-ctrl.com/signup
- group: company
  title: ''
  type: Blog
  url: https://q-ctrl.com/blog
- group: operate
  title: ''
  type: Support
  url: https://q-ctrl.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://q-ctrl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://q-ctrl.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.q-ctrl.com/
- group: auth
  title: ''
  type: Security
  url: https://q-ctrl.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://q-ctrl.com/security
- group: build
  title: ''
  type: Packages
  url: packages/q-ctrl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/q-ctrl-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/q-ctrl-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/q-ctrl-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/q-ctrl-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/q-ctrl-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/q-ctrl-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/q-ctrl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/q-ctrl-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/q-ctrl-well-known.yml
created: '2026-07-17'
description: Q-CTRL builds infrastructure software to power the quantum future, delivering AI-driven quantum control, error-suppression, and performance-management tools that span quantum computing and quantum sensing. Its products — Boulder Opal (hardware design and control), Fire Opal (quantum error suppression), Black Opal (education), and Ironstone Opal (GPS-free quantum navigation) — are consumed primarily through official Python client libraries that authenticate against the Q-CTRL account service and call a hosted cloud GraphQL API at api.q-ctrl.com. Q-CTRL serves enterprise, defense, aerospace, and research customers and is ISO/IEC 27001:2022 certified.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/q-ctrl.png
layout: provider
modified: '2026-07-20'
name: Q Ctrl
nav: Providers
network: true
overview: 'Q Ctrl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Quantum Control, Quantum Sensing, and Error Suppression.


  Q Ctrl''s developer surface includes documentation, getting-started guide, signup flow, engineering blog, support, authentication, changelog, and 16 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 35.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 35.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Q Ctrl Authentication
  slug: q-ctrl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Q Ctrl Domain Security
  slug: q-ctrl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Q Ctrl Vulnerability Disclosure
  slug: q-ctrl-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Q Ctrl Trust Center
  slug: q-ctrl-trust-center
  summary_line: ISO/IEC 27001:2022, Cyber Essentials, NIST SP 800-171 Rev 3, DISP (Defence Industry Security Program)
slug: q-ctrl
tags:
- Company
- Quantum Computing
- Quantum Control
- Quantum Sensing
- Error Suppression
- Developer Tools
- SDK
- GraphQL API
website: https://q-ctrl.com/
---
