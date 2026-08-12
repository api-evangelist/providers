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
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The OAuth 2.0 authorization server and OpenID Connect provider that fronts the Everlywell member account. It is not a documented developer product — Everly Health publishes no API reference for it — b
  name: Everly Health Identity (OAuth 2.0 / OpenID Connect)
  slug: identity
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.everlywell.com/
- group: company
  title: ''
  type: Blog
  url: https://www.everlywell.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.everlywell.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.everlywell.com/
- group: start
  title: ''
  type: SignUp
  url: https://results.everlywell.com/register
- group: start
  title: ''
  type: Login
  url: https://secure.everlywell.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.everlywell.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.everlywell.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EverlyWell
- group: company
  title: ''
  type: Careers
  url: https://www.everlywell.com/careers/
- group: other
  title: ''
  type: Enterprise
  url: https://www.everlyhealthsolutions.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/everly-health-stock
- group: agent
  title: ''
  type: WellKnown
  url: well-known/everly-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everly-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/everly-health-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/everly-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everly-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/everly-health-llms.txt
created: '2026-08-04'
description: Everly Health (legal name Everly Well, Inc.) is an Austin, Texas digital health company that operates the Everlywell consumer brand for at-home lab collection and testing, Everly Health Solutions (the former PWNHealth / Home Access Health businesses) for enterprise lab connectivity, clinician-network oversight and results delivery, and the Natalist fertility and pregnancy brand. Its catalog spans daily health, digestive, sexual, hormone and cancer-screening panels, paired with an affiliated telehealth provider network and the Eva AI platform for member engagement, care coordination and support. Everly Health publishes no public developer portal, API reference, SDKs or OpenAPI; the only machine-readable contract it serves anonymously is the OAuth 2.0 / OpenID Connect discovery surface behind its member login host.
image: https://www.everlywell.com/icons/icon-512x512.png
layout: provider
modified: '2026-08-04'
name: Everly Health
nav: Providers
network: true
overview: 'Everly Health publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Diagnostics.


  Everly Health''s developer surface includes engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 62
scopes:
- name: Everly Health Scopes
  scope_count: 2
  slug: everly-health-scopes
  summary_line: 2 scopes · authorizationCode/password
score:
  band: emerging
  composite: 25.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 25.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everly-health/refs/heads/main/screenshots/everly-health-2026-08-07T165035.png
security:
- kind: authentication
  name: Everly Health Authentication
  slug: everly-health-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Everly Health Domain Security
  slug: everly-health-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: everly-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Diagnostics
- Lab Testing
- Telehealth
- Consumer Health
- Identity
website: https://www.everlywell.com/
---
