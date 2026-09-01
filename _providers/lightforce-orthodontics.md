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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://lf.co/
- group: start
  title: ''
  type: Portal
  url: https://id.lightforceortho.com/
- group: operate
  title: ''
  type: Support
  url: https://kb.lightforceortho.com/en/
- group: company
  title: ''
  type: Blog
  url: https://lf.co/blog
- group: start
  title: ''
  type: SignUp
  url: https://lf.co/doctors/get-started
- group: start
  title: ''
  type: Login
  url: https://id.lightforceortho.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lf.co/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lf.co/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lightforceortho
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lightforce-orthodontics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightforce-orthodontics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightforce-orthodontics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lightforce-orthodontics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightforce-orthodontics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lightforce-orthodontics-llms.txt
created: '2026-07-17'
description: 'LightForce Orthodontics is a Burlington, Massachusetts medical device manufacturer that produces 3D-printed, patient-specific orthodontic brackets marketed as "generative braces". Its LightBracket, LightTray indirect-bonding and LightTray Turbo products are generated from each patient''s digital orthodontic treatment plan and printed in the United States, giving orthodontists micron-level control across six dimensions and letting them preview the projected outcome before treatment begins. LightForce sells to orthodontic practices rather than to developers: doctors work through a Doctor Portal and a hosted knowledge base, and the company publishes no public developer portal, API reference, SDKs or machine-readable API specification. The only publicly reachable programmable surface is its Auth0-hosted identity tenant at id.lightforceortho.com, which serves standard OpenID Connect and OAuth 2.0 authorization-server discovery documents. Backed by Kleiner Perkins.'
image: https://cdn.prod.website-files.com/69aec45d4fb611242f119860/69e9d73bdc029cbaa9bc1429_Logo%20Image%20Cover.png
layout: provider
modified: '2026-07-19'
name: LightForce Orthodontics
nav: Providers
network: true
overview: 'LightForce Orthodontics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Orthodontics, Medical Devices, and Dental.


  LightForce Orthodontics'' developer surface includes developer portal, support, engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 5
scopes:
- name: Lightforce Orthodontics Scopes
  scope_count: 14
  slug: lightforce-orthodontics-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 24.2
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightforce-orthodontics/refs/heads/main/screenshots/lightforce-orthodontics-2026-07-25T225117.png
security:
- kind: authentication
  name: Lightforce Orthodontics Authentication
  slug: lightforce-orthodontics-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Lightforce Orthodontics Domain Security
  slug: lightforce-orthodontics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lightforce-orthodontics
tags:
- Company
- Healthcare
- Orthodontics
- Medical Devices
- Dental
- 3D Printing
- Manufacturing
- Identity
website: https://lf.co/
---
