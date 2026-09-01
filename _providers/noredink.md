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
    dynamic_client_registration: false
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: NoRedInk's OAuth 2.0 authorization server with OpenID Connect on top, used for single sign-on and partner/classroom-rostering integrations. Advertises the authorization-code + refresh-token grants, an
  name: NoRedInk OAuth & OpenID Connect
  slug: noredink-oauth-openid-connect
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://noredink.com
- group: operate
  title: ''
  type: Support
  url: https://noredink.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.noredink.com/insights/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NoRedInk
- group: start
  title: ''
  type: SignUp
  url: https://www.noredink.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.noredink.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.noredink.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.noredink.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/noredink-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/noredink-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/noredink-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/noredink-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/noredink-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/noredink-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://noredinkstatus.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noredink-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/noredink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/noredink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/noredink-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noredink-llms.txt
created: '2026-07-17'
description: NoRedInk is a K-12 English Language Arts platform used by millions of students and teachers to build stronger writers and critical thinkers. It combines adaptive grammar and writing practice, personalized high-interest content, authentic assessments, guided essays with self and peer review, actionable teacher data, and an AI-powered Grading Assistant. NoRedInk's public developer surface is a standards-based OAuth 2.0 / OpenID Connect authorization server (issuer https://www.noredink.com) that powers single sign-on and classroom rostering integrations with Clever, ClassLink, Canvas, and Google Classroom.
image: https://noredink.com/wp-content/uploads/2025/09/GA-Essays-grayBG.gif
layout: provider
modified: '2026-07-20'
name: NoRedInk
nav: Providers
network: true
overview: 'NoRedInk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, English Language Arts, and Grammar.


  NoRedInk''s developer surface includes support, engineering blog, signup flow, authentication, and 16 more developer resources.'
random_paper: 18
scopes:
- name: Noredink Scopes
  scope_count: 1
  slug: noredink-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 32.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noredink/refs/heads/main/screenshots/noredink-2026-08-07T185517.png
security:
- kind: authentication
  name: Noredink Authentication
  slug: noredink-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Noredink Domain Security
  slug: noredink-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Noredink Vulnerability Disclosure
  slug: noredink-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Noredink Trust Center
  slug: noredink-trust-center
  summary_line: trust center published
slug: noredink
tags:
- Company
- Education
- EdTech
- English Language Arts
- Grammar
- Writing
- Literacy
- K-12
- Authentication
- OpenID Connect
- Single Sign-On
- Rostering
- Identity
website: https://noredink.com
---
