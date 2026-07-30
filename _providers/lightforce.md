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
api_count: 1
apis:
- description: The public OpenID Connect / OAuth 2.0 identity surface that fronts the LightForce Doctor Portal. Published as a live OIDC discovery document at id.lightforceortho.com/.well-known/openid-configuration,
  name: LightForce Identity (OpenID Connect)
  slug: identity
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://lf.co
- group: operate
  title: ''
  type: Support
  url: https://kb.lightforceortho.com/en/
- group: company
  title: ''
  type: Blog
  url: https://lf.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightforceortho
- group: start
  title: ''
  type: SignUp
  url: https://lf.co/doctors/get-started
- group: start
  title: ''
  type: Login
  url: https://id.lightforceortho.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lf.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lf.co/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://lf.co/legal/hipaa
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightforce-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightforce-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightforce-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightforce-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightforce-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lightforce-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightforce-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/lightforce-packages.yml
created: '2026-07-17'
description: 'LightForce Orthodontics, Inc. is a Boston-area medical device and digital manufacturing company that produces "generative braces" — fully customized, 3D-printed orthodontic brackets and indirect bonding trays generated from each patient''s own tooth anatomy and the treating orthodontist''s digital treatment plan. Doctors submit intraoral scans and treatment plans through the LightForce Doctor Portal, LightForce designs and 3D-prints patient-specific LightBracket ceramic and metal appliances, and ships custom IDB trays back to the practice. The company operates as a HIPAA-covered digital workflow: no public developer API or developer portal is published, but the Doctor Portal is fronted by a public OpenID Connect identity surface at id.lightforceortho.com. Backed by Matrix Partners, Kleiner Perkins, and others.'
image: https://cdn.prod.website-files.com/69aec45d4fb611242f119860/69e28a19a4f73f9aaab7e1f9_fav-lightforce%20256.png
layout: provider
modified: '2026-07-19'
name: Lightforce
nav: Providers
network: true
overview: 'Lightforce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Orthodontics, Dentistry, and Medical Devices.


  Lightforce''s developer surface includes support, engineering blog, signup flow, authentication, and 13 more developer resources.'
random_paper: 79
scopes:
- name: Lightforce Scopes
  scope_count: 14
  slug: lightforce-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 22.8
  delta: 1.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 21.8
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightforce/refs/heads/main/screenshots/lightforce-2026-07-25T225116.png
security:
- kind: authentication
  name: Lightforce Authentication
  slug: lightforce-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Lightforce Domain Security
  slug: lightforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightforce
tags:
- Company
- Healthtech
- Orthodontics
- Dentistry
- Medical Devices
- 3D Printing
- Digital Manufacturing
- Identity
website: https://lf.co
---
