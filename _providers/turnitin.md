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
api_count: 2
apis:
- description: RESTful API for integrating Turnitin's integrity services into third-party platforms — submit a document, generate a Similarity Report, and display it to users. Authenticates with an integration-insta
  name: Turnitin Core API (TCA)
  slug: turnitin-core-api-tca
- description: LTI integration path for embedding Turnitin into learning management systems, as an alternative to the TCA REST surface.
  name: Turnitin Learning Tools Interoperability (LTI)
  slug: turnitin-learning-tools-interoperability-lti
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.turnitin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.turnitin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.turnitin.com/turnitin-core-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.turnitin.com/turnitin-core-api
- group: start
  title: ''
  type: Login
  url: https://developers.turnitin.com/customer-login
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.turnitin.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.turnitin.com
- group: company
  title: ''
  type: Blog
  url: https://www.turnitin.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/turnitin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.turnitin.com/privacy-policy-website/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.turnitin.com/terms-of-use-website/
- group: operate
  title: ''
  type: StatusPage
  url: https://turnitin.statuspage.io
- group: auth
  title: ''
  type: Security
  url: security/turnitin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/turnitin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turnitin-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/turnitin-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/turnitin-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/turnitin-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/turnitin-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turnitin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/turnitin-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/turnitin-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/turnitin-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/turnitin-llms.txt
created: '2026-07-17'
description: Turnitin is an academic and research integrity company that for more than 20 years has provided plagiarism/similarity detection, AI-writing detection, online grading, and feedback tools for educators, researchers, and publishers. Its market-leading integrity services are exposed to third-party platforms through the RESTful Turnitin Core API (TCA), which lets an integrating product submit a document, generate a Similarity Report, and display it to users without leaving the host platform, plus a Learning Tools Interoperability (LTI) path for LMS integrations. TCA is SOC2 compliant and runs across international data centers. Turnitin was surfaced as a portfolio company of Norwest Venture Partners and enriched into the API Evangelist network from its public developer documentation.
image: https://www.turnitin.com/themes/turnitin/img/turnitin-icon-rgb.jpg
layout: provider
modified: '2026-07-21'
name: Turnitin
nav: Providers
network: true
overview: 'Turnitin publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Academic Integrity, and Plagiarism Detection.


  Turnitin''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 32.3
  delta: 1.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 31.3
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Turnitin Authentication
  slug: turnitin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Turnitin Domain Security
  slug: turnitin-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Turnitin Vulnerability Disclosure
  slug: turnitin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: turnitin
tags:
- Company
- Education
- EdTech
- Academic Integrity
- Plagiarism Detection
- Similarity
- AI Detection
- Assessment
- Research Integrity
- Publishing
- LTI
website: https://www.turnitin.com
---
