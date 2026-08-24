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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.1
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.brightfunds.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hello.brightfunds.org/
- group: start
  title: ''
  type: Login
  url: https://www.brightfunds.org/login/
- group: operate
  title: ''
  type: Support
  url: https://www.brightfunds.org/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.brightfunds.org/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brightfunds.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brightfunds.org/privacy_policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/bright-funds-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bright-funds-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bright-funds-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bright-funds-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/bright-funds-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-funds-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bright-funds-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/bright-funds-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bright-funds-llms.txt
created: '2026-07-17'
description: Bright Funds is a workplace-giving, corporate grants, and employee volunteering platform (now part of Submittable) that lets employers run donation, matching-gift, and volunteering programs for their employees and route funds to vetted nonprofits. The platform operates a live OpenID Connect / OAuth 2.0 authorization server at www.brightfunds.org for single sign-on and API integrations (authorization_code, client_credentials, and refresh_token grants; RS256 id_tokens; openid/profile/email/write/update scopes). It publishes a PGP-signed security.txt but no standalone developer portal or OpenAPI specification. Surfaced as a portfolio company of Bloomberg Beta and enriched into the API Evangelist network from its public identity and well-known discovery surface.
image: https://cdn.prod.website-files.com/64c3f11f46b35cb5f865c514/66994cfea9422c379d8041d9_BrightFunds_Icon_Webflow-256.png
layout: provider
modified: '2026-07-18'
name: Bright Funds
nav: Providers
network: true
overview: 'Bright Funds is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workplace Giving, Corporate Social Responsibility, Employee Engagement, and Non-Profit.


  Bright Funds'' developer surface includes support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 11
scopes:
- name: Bright Funds Scopes
  scope_count: 7
  slug: bright-funds-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 21.6
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 21.6
  provenance:
    conformance: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bright-funds/refs/heads/main/screenshots/bright-funds-2026-07-25T203821.png
security:
- kind: authentication
  name: Bright Funds Authentication
  slug: bright-funds-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Bright Funds Domain Security
  slug: bright-funds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bright Funds Vulnerability Disclosure
  slug: bright-funds-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bright-funds
tags:
- Company
- Workplace Giving
- Corporate Social Responsibility
- Employee Engagement
- Non-Profit
- Grants Management
- Donations
- Volunteering
- Authentication
- OpenID Connect
website: https://www.brightfunds.org/
---
