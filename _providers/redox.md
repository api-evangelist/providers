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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Redox's modern FHIR API for exchanging clinical and administrative healthcare data across the Redox network using HL7 FHIR resources and notifications, authenticated with OAuth2.
  name: Redox FHIR API
  slug: redox-fhir-api
- description: Redox's legacy event-based Data Model API (Redox Messages) for exchanging structured healthcare data across the network via JSON message payloads.
  name: Redox Data Model API
  slug: redox-data-model-api
- description: The Redox Platform API for managing organizations, sources, destinations, and platform settings via user-level API keys.
  name: Redox Platform API
  slug: redox-platform-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/redox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redox-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.redoxengine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.redoxengine.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.redoxengine.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.redoxengine.com/basics/
- group: company
  title: ''
  type: Blog
  url: https://redoxengine.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RedoxEngine
- group: commercial
  title: ''
  type: Pricing
  url: https://redoxengine.com/forms/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.redoxengine.com/#/signup/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redoxengine.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://redoxengine.com/platform-security/
- group: auth
  title: ''
  type: Security
  url: https://docs.redoxengine.com/security/responsible-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://redoxengine.com/platform-security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/redox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/redox-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/redox-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/redox-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/redox-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/redox-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/redox-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/redox-llms.txt
created: '2026-07-17'
description: Redox is a healthcare data interoperability platform, founded in 2014 and headquartered in Madison, Wisconsin, that enables secure, real-time exchange of clinical and administrative data across the healthcare ecosystem. Through a single API and a network of 100+ EHR connections and 12,000+ connected healthcare organizations, Redox lets digital health vendors, providers, payers, EHRs, and life-sciences companies integrate once and reach the entire network. The platform offers a modern FHIR API, the legacy Redox Data Model (Redox Messages) event-based API, and a Platform API for managing organizations, sources, and destinations. Redox is HITRUST r2 and SOC 2 Type 2 certified and HIPAA, GDPR, and CCPA aligned, processing tens of billions of healthcare transactions annually.
image: https://redoxengine.com/wp-content/uploads/2023/01/redox-logo.png
layout: provider
modified: '2026-07-21'
name: Redox
nav: Providers
network: true
overview: 'Redox publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Interoperability, FHIR, and EHR.


  Redox''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 15 more developer resources.'
random_paper: 54
scopes:
- name: Redox Scopes
  scope_count: 3
  slug: redox-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 37.4
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 39.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Redox Authentication
  slug: redox-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Redox Domain Security
  slug: redox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redox Vulnerability Disclosure
  slug: redox-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Redox Trust Center
  slug: redox-trust-center
  summary_line: HITRUST r2, SOC 2 Type 2
slug: redox
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- EHR
- Health Data
- Integration
- HL7
- Digital Health
- Healthcare API
website: https://docs.redoxengine.com/
---
