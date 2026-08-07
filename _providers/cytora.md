---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Cytora's production REST API for digital risk processing — the "preferred method" of submission intake described in its own Risk Flow Academy. The gateway is real (api.cytora.com resolves via gateway.
  name: Cytora Platform API
  slug: cytora-platform-api
- description: The OAuth 2.0 / OpenID Connect authorization server that fronts every Cytora integration, running on an Auth0 EU tenant (cytora-prod.eu.auth0.com). This is the only Cytora surface that answers anonymo
  name: Cytora Identity (Auth0 OIDC)
  slug: cytora-identity-auth0-oidc
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cytora-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cytora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cytora.com/
- group: company
  title: ''
  type: Blog
  url: https://cytora.com/risk-flow-center/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cytora.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cytora-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.cytora.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cytora-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cytora.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/cytora-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: https://auth.cytora.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/cytora-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cytora-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cytora-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cytora-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cytora-llms.txt
- group: start
  title: ''
  type: Login
  url: https://uwp.cytora.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cytora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cytora
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cytora
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cytora.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://cytora.com/cookie-policy
- group: operate
  title: ''
  type: Support
  url: https://cytora.com/about-us/contact-us
- group: other
  title: ''
  type: Customers
  url: https://cytora.com/customers
- group: company
  title: ''
  type: Partners
  url: https://cytora.com/digital-risk-processing/data-ecosystem
created: '2026-07-25'
description: 'Cytora is a London-headquartered insurtech, founded in 2012 as a University of Cambridge spinout, that sells a digital risk processing platform to commercial insurers, wholesale brokers, MGAs and reinsurers. Its software ingests inbound submissions arriving as email, PDF, spreadsheet and broker API payloads, digitises them against pre-built line-of-business schemas (property, commercial combined, construction, cyber, fleet, general liability, professional liability, D&O, E&O, management liability), augments them from a data ecosystem of roughly sixty third-party risk-data partners, evaluates them against appetite and priority rules, and routes them into downstream underwriting and claims systems. Use cases span new business, renewals, mid-term adjustments, claims FNOL and post-FNOL intake, and facultative and treaty reinsurance submissions. Named customers include Zurich, Chubb, Markel, Beazley, Travelers, Tokio Marine, Ecclesiastical, Arch, Everest and TransRe. Applied Systems
  acquired Cytora in September 2025. Its API posture is partner-gated and enterprise-only: Cytora runs a real production API gateway at api.cytora.com and a real ReadMe-hosted API reference at docs.cytora.com, but the documentation site is entirely password-protected (HTTP 302 to a password wall, robots.txt Disallow) and the gateway resets anonymous TLS connections. There is no self-serve developer signup, no public OpenAPI, no public Postman collection and no published webhook or event catalog. The only externally verifiable technical surface is the Auth0 OIDC discovery document at auth.cytora.com, which confirms OAuth 2.0 client-credentials and authorization-code flows for provisioned partner integrations. The United Kingdom home market has no open-insurance mandate, so nothing compels Cytora to expose any of this publicly.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Cytora
nav: Providers
network: true
overview: 'Cytora publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United Kingdom, Insurtech, Commercial Insurance, and Underwriting.


  Cytora''s developer surface includes documentation, engineering blog, authentication, support, and 21 more developer resources.'
random_paper: 93
scopes:
- name: Cytora Scopes
  scope_count: 14
  slug: cytora-scopes
  summary_line: 14 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 31.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 31.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 65.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cytora/refs/heads/main/screenshots/cytora-2026-07-25T211113.png
security:
- kind: authentication
  name: Cytora Authentication
  slug: cytora-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cytora Domain Security
  slug: cytora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cytora Trust Center
  slug: cytora-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27001:2013, ISO/IEC 42001:2023
slug: cytora
tags:
- Insurance
- United Kingdom
- Insurtech
- Commercial Insurance
- Underwriting
- Claims
- Risk Data
- Property and Casualty
- Reinsurance
- Broker
- Submission Intake
- Document AI
website: https://cytora.com/
---
