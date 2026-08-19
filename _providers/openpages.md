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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Data-centric GRC REST API for IBM OpenPages, specified in terms of resources, their URIs, and the actions that can be performed on those URIs. Available as v1 and v2. The API is hosted per service ins
  name: IBM OpenPages GRC REST API
  slug: ibm-openpages-grc-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Openpages Events Webhooks
  slug: openpages-events-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openpages-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.ibm.com/trust/security-psirt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.ibm.com/docs/openpages
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.ibm.com/docs/openpages
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.ibm.com/apidocs/openpages
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.ibm.com/docs/openpages?topic=openpages-gettingstartedtutorial
- group: company
  title: ''
  type: Website
  url: https://www.ibm.com/products/openpages
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.ibm.com/docs/openpages?topic=openpages-openpages-choose-plan
- group: start
  title: ''
  type: SignUp
  url: https://cloud.ibm.com/registration
- group: start
  title: ''
  type: Login
  url: https://cloud.ibm.com/login
- group: operate
  title: ''
  type: Support
  url: https://cloud.ibm.com/docs/openpages?topic=openpages-help-and-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.ibm.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.ibm.com/docs/openpages?topic=openpages-openpages-relnotes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openpages-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/openpages-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openpages-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/openpages-events-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openpages-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openpages-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openpages-domain-security.yml
created: '2026-07-17'
description: IBM OpenPages is an AI-driven, unified governance, risk, and compliance (GRC) platform delivered as a managed service on IBM Cloud. Originally founded as OpenPages Inc. (a Matrix Partners portfolio company) and acquired by IBM in 2010, it consolidates operational risk, regulatory compliance, financial controls, policy, IT governance, third-party risk, and model/AI governance (watsonx.governance) into one system of record. OpenPages exposes a data-centric GRC REST API (v1 and v2), an ObjectManager CLI (ibmcloud openpages), IBM Cloud IAM authentication, and event notifications (CloudEvents v1.0) so teams can automate configuration, integrate risk data, and drive event-driven workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openpages.png
layout: provider
modified: '2026-07-20'
name: OpenPages
nav: Providers
network: true
overview: 'OpenPages publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, B2B, Governance, Risk, and Compliance.


  The OpenPages catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenPages'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, changelog, and 15 more developer resources.'
random_paper: 68
score:
  band: developing
  composite: 47.2
  delta: 0.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 61.9
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 47.1
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openpages/refs/heads/main/screenshots/openpages-2026-08-07T190623.png
security:
- kind: authentication
  name: Openpages Authentication
  slug: openpages-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Openpages Domain Security
  slug: openpages-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openpages Vulnerability Disclosure
  slug: openpages-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: openpages
tags:
- Company
- B2B
- Governance
- Risk
- Compliance
- GRC
- Regulatory Compliance
- Risk Management
- Enterprise Software
- watsonx
- Audit
website: https://www.ibm.com/products/openpages
---
