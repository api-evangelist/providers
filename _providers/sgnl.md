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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST/JSON access-evaluation API. Evaluate whether a principal may perform actions on assets in context, search accessible assets or authorized principals, query the directory, and route provider hooks
  name: SGNL Public API v2 (Access Service)
  slug: sgnl-public-api-v2-access-service
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://sgnl.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sgnl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sgnl.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sgnl.ai/
- group: operate
  title: ''
  type: Support
  url: https://help.sgnl.ai/
- group: company
  title: ''
  type: Blog
  url: https://sgnl.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SGNL-ai
- group: start
  title: ''
  type: SignUp
  url: https://sgnl.ai/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sgnl.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sgnl.ai/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/sgnl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sgnl-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sgnl-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sgnl-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sgnl-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/sgnl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sgnl-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sgnl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sgnl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sgnl-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sgnl-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sgnl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://sgnl.ai/responsible-disclosure/
created: '2026-07-17'
description: SGNL is a continuous identity and authorization platform that eliminates standing privilege and makes real-time, context-aware access decisions for both human users and AI agents. It sits at the center of an enterprise IAM architecture, dynamically adapting permissions as conditions change and revoking sessions in real time. SGNL is built on the OpenID Shared Signals Framework (SSF) and the Continuous Access Evaluation Profile (CAEP), ingesting context from identity providers, HR systems, and security tooling to enforce zero standing privilege across cloud and infrastructure. Its Public API v2 (Access Service) exposes REST/JSON access evaluation, asset and principal search, directory query, and provider-hook routing.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sgnl.png
layout: provider
mcp_servers:
- description: ''
  name: sgnl-mcp.yml
  slug: sgnl-mcpyml
modified: '2026-07-21'
name: SGNL
nav: Providers
network: true
overview: 'SGNL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Identity, Authorization, and Access Management.


  SGNL''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
random_paper: 31
score:
  band: thin
  composite: 29.1
  delta: -0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 29.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sgnl Authentication
  slug: sgnl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sgnl Domain Security
  slug: sgnl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sgnl Vulnerability Disclosure
  slug: sgnl-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: sgnl
tags:
- Company
- Security
- Identity
- Authorization
- Access Management
- CAEP
- Shared Signals
- Zero Standing Privilege
- IAM
website: https://sgnl.ai
---
