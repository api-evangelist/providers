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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Morf's REST API and webhook surface for building healthcare automation workflows. Webhooks from source applications are ingested at api.morf.healthcare/webhooks/ and processed into events that trigger
  name: Morf API
  slug: morf-api
artifact_total: 6
asyncapis:
- description: ''
  name: Morf Webhooks
  slug: morf-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/morf-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://morf.health/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.morf.health/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.morf.health/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.morf.health/libraries/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.morf.health/morf_dashboard/overview
- group: other
  title: ''
  type: HowItWorks
  url: https://www.morf.health/how-it-works
- group: company
  title: ''
  type: Blog
  url: https://www.morf.health/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.morf.health/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.morf.health/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.morf.health/
- group: operate
  title: ''
  type: Support
  url: https://www.morf.health/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.morf.health/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.morf.health/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/morfhealth
- group: auth
  title: ''
  type: Compliance
  url: https://trust.morf.health/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morf-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/morf-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/morf-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/morf-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/morf-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/morf-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/morf-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/morf-lifecycle.yml
created: '2026-07-17'
description: Morf is a HIPAA-compliant healthcare automation and integration platform that connects EHRs, CRMs, payment systems, and communication tools so digital health teams can eliminate manual work and put patient outreach on autopilot. Workflows are triggered by inbound webhooks from source applications (Healthie, Elation, Medplum, Feathery, athenahealth, Cerbo, DrChrono, Hint Health, and dozens more), which Morf processes into events that fan out to actions across 30+ connected applications. The platform exposes a REST API at api.morf.healthcare secured with API keys and OAuth 2.0 / OpenID Connect (auth.morf.health), a webhook ingestion surface, an integration/action catalog of 170+ pre-built actions, and Flo AI, a no-code workflow co-pilot.
image: https://cdn.sanity.io/images/teurbt0n/production/9e3de2ea4057cbaef5c3b8c011b87232520081e0-1200x630.jpg?w=1200
layout: provider
modified: '2026-07-20'
name: Morf
nav: Providers
network: true
overview: 'Morf publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Automation, and Integration.


  The Morf catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Morf''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 18 more developer resources.'
random_paper: 36
scopes:
- name: Morf Scopes
  scope_count: 6
  slug: morf-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 49.1
  delta: 2.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 46.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Morf Authentication
  slug: morf-authentication
  summary_line: apiKey/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Morf Domain Security
  slug: morf-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Morf Trust Center
  slug: morf-trust-center
  summary_line: SOC 2, HIPAA
slug: morf
tags:
- Company
- Healthcare
- Health IT
- Automation
- Integration
- iPaaS
- Webhooks
- EHR
- Patient Communication
- HIPAA
- Workflow
- Digital Health
website: https://morf.health/
---
