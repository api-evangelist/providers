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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 21.2
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.scienceexchange.com
- group: docs
  title: ''
  type: APIReference
  url: https://demo.scienceexchange.com/api-docs/providers
- group: company
  title: ''
  type: Blog
  url: https://www.scienceexchange.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scienceexchange
- group: start
  title: ''
  type: Login
  url: https://app.scienceexchange.com
- group: operate
  title: ''
  type: Support
  url: mailto:info@scienceexchange.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.scienceexchange.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.scienceexchange.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.scienceexchange.com/platform/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/scienceexchange-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scienceexchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scienceexchange-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/scienceexchange-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/scienceexchange-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/scienceexchange-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/scienceexchange-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/scienceexchange-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/scienceexchange-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/scienceexchange-llms.txt
created: '2026-07-17'
description: Science Exchange is an R&D supplier onboarding and orchestration platform for life-sciences organizations. It connects pharmaceutical, biotech, and research companies with a network of thousands of pre-vetted external research suppliers and centralizes sourcing, contracting, compliance, payment, and spend analytics into a single system that layers on top of existing ERP, procure-to-pay, and identity infrastructure. The platform automates supplier qualification and onboarding (from 50+ hours to roughly 6), executes contracts, processes payments, and reports on R&D spend. Science Exchange exposes a Providers API (with a first-party Ruby client) and a Developer Portal offering RESTful APIs for custom integrations, data export, and workflow automation, alongside SAML SSO and OAuth2/OIDC login. The company is backed by Norwest Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scienceexchange.png
layout: provider
modified: '2026-07-21'
name: Science Exchange
nav: Providers
network: true
overview: 'Science Exchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Research and Development, Procurement, and Supplier Management.


  Science Exchange''s developer surface includes API reference, engineering blog, support, authentication, and 15 more developer resources.'
random_paper: 35
score:
  band: emerging
  composite: 28.1
  delta: 4.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.5
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Scienceexchange Authentication
  slug: scienceexchange-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Scienceexchange Domain Security
  slug: scienceexchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Scienceexchange Trust Center
  slug: scienceexchange-trust-center
  summary_line: SOC 2 Type II, HIPAA-ready, GDPR
slug: scienceexchange
tags:
- Company
- Life Sciences
- Research and Development
- Procurement
- Supplier Management
- Marketplace
- Biotech
- Pharmaceutical
- Scientific Research
website: https://www.scienceexchange.com
---
