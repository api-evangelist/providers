---
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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allwork-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://allworknow.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allwork-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allworknow.com/
- group: docs
  title: ''
  type: Documentation
  url: https://allworknow.com/how-it-works/
- group: operate
  title: ''
  type: Support
  url: https://allworknow.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://allworknow.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://allworknow.com/feed/
- group: start
  title: ''
  type: Login
  url: https://app.allworknow.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://allworknow.com/terms-of-use-2/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://allworknow.com/privacy-policy-3/
- group: company
  title: ''
  type: Press
  url: https://allworknow.com/press/
- group: operate
  title: ''
  type: FAQ
  url: https://allworknow.com/frequently-asked-questions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/allwork
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AllWorkNow
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allwork-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/allwork-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/allwork-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/allwork-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allwork-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/allwork-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allwork-llms.txt
coverage:
  checked: '2026-08-06'
  detail: AllWork ships only an end-user SaaS application — api.allworknow.com, developers.allworknow.com and docs.allworknow.com do not resolve in DNS, and the only anonymously readable machine contracts on the domain are the Keycloak OIDC discovery document for the realm that logs users into app.allworknow.com and an RFC 9116 security.txt.
  evidence:
  - status: 404
    url: https://allworknow.com/openapi.json
  - status: 404
    url: https://app.allworknow.com/openapi.json
  - status: 404
    url: https://allworknow.com/.well-known/api-catalog
  - status: 200
    url: https://auth.allworknow.com/realms/AWN1/.well-known/openid-configuration
  - status: 200
    url: https://allworknow.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'AllWork is a New York-based flexible-workforce management and payments platform for contingent labor. It combines onboarding, scheduling, budgeting and planning, time and attendance with GPS-confirmed check-in, timesheet and expense approval, payroll, reporting and analytics, and a manager mobile app into one system, and acts as both Employer of Record (EOR) and Agent of Record (AOR) so a brand can compliantly engage and pay W-2 and 1099 talent across the United States, Canada and internationally. It sells into beauty and luxury, retail, food and beverage, oil and gas, technology and engineering, life sciences and healthcare, financial services, and self-direction programs, handling worker classification, labor-law adherence, and federal, state and local tax filings. AllWork publishes no public developer program: there is no API reference, no SDK, and no machine-readable specification on its site.'
image: https://allworknow.com/wp-content/uploads/2023/07/Favicon-2.png
layout: provider
modified: '2026-08-06'
name: AllWork
nav: Providers
network: true
overview: 'AllWork is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Human Resources, Staffing, and Payroll.


  AllWork''s developer surface includes documentation, support, engineering blog, FAQ, authentication, and 17 more developer resources.'
random_paper: 8
scopes:
- name: Allwork Scopes
  scope_count: 10
  slug: allwork-scopes
  summary_line: 10 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 19.3
  delta: -1.3
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 5.3
  previous_composite: 20.6
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allwork/refs/heads/main/screenshots/allwork-2026-08-07T161234.png
security:
- kind: authentication
  name: Allwork Authentication
  slug: allwork-authentication
  summary_line: openIdConnect/oauth2/mutualTLS · 3 schemes
- kind: domain-security
  name: Allwork Domain Security
  slug: allwork-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Allwork Vulnerability Disclosure
  slug: allwork-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: allwork
tags:
- Company
- Workforce Management
- Human Resources
- Staffing
- Payroll
- Employer of Record
- Contingent Workforce
- Gig Economy
- Scheduling
- Time and Attendance
- Compliance
website: https://allworknow.com/
---
