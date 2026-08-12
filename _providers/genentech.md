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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: FHIR R4 (v4.3.0) Universal API for Genentech Patient Support Services, documented in the Universal API Implementation Guide. Supports Access Solutions patient enrollment, Copay enrollment, Patient Fou
  name: Genentech Universal API (UAPI)
  slug: genentech-universal-api-uapi
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.gene.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.gene.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.gene.com/s/api-library
- group: docs
  title: ''
  type: APIReference
  url: https://fhir.developer.gene.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.gene.com/s/how-will-this-help-me-or-my-customers
- group: operate
  title: ''
  type: Support
  url: https://developer.gene.com/s/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.gene.com/s/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Genentech
- group: agent
  title: ''
  type: WellKnown
  url: well-known/genentech-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/genentech-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/genentech-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/genentech-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/genentech-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/genentech-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/genentech-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/genentech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gene.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genentech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/genentech-llms.txt
created: '2026-07-17'
description: Genentech is a biotechnology company founded in 1976 and headquartered in South San Francisco, California, and a member of the Roche Group since 2009. It discovers, develops, manufactures, and commercializes medicines across oncology, immunology, ophthalmology, neuroscience, infectious disease, and rare disease. For developers and health-system integration partners, Genentech operates a public Developer Portal (developer.gene.com) and an Integration Marketplace that exposes FHIR R4 "Universal API" (UAPI) services for Patient Support Services — including Access Solutions patient enrollment, Copay program enrollment, Patient Foundation enrollment, and status query services. Access is registration-based with API keys and an OAuth2 / OpenID Connect authorization surface. Genentech also maintains a large open-source GitHub organization (github.com/Genentech, 150+ repositories) focused on computational biology, genomics, and AI/ML for drug discovery.
image: https://www.gene.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Genentech
nav: Providers
network: true
overview: 'Genentech publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Healthcare, and Life Sciences.


  Genentech''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 14 more developer resources.'
random_paper: 17
scopes:
- name: Genentech Scopes
  scope_count: 36
  slug: genentech-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: thin
  composite: 29.0
  delta: -1.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 30.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 55.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genentech/refs/heads/main/screenshots/genentech-2026-07-25T215539.png
security:
- kind: authentication
  name: Genentech Authentication
  slug: genentech-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Genentech Domain Security
  slug: genentech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Genentech Vulnerability Disclosure
  slug: genentech-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: genentech
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Healthcare
- Life Sciences
- FHIR
- Patient Support Services
- Drug Discovery
- Genomics
website: https://www.gene.com/
---
