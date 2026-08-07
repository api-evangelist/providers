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
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: The account-based marketing platform API behind Terminus (now the DemandScience ABM Platform). The API host api.terminusplatform.com is live and answers every anonymous request with HTTP 401 "Authenti
  name: Terminus ABM Platform API
  slug: terminus-abm-platform-api
- description: A dedicated service that streamlines management of users and employee signature data inside an Email Experiences (Signature Ads, formerly Sigstr) account. Employee data delivered to the API endpoint c
  name: Employee Automation API
  slug: employee-automation-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://demandscience.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.terminus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.demandscience.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://support.demandscience.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://app.demandscienceplatform.com/
- group: company
  title: ''
  type: Blog
  url: https://demandscience.com/resources/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demandscience.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demandscience.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/demandscience
- group: auth
  title: ''
  type: Authentication
  url: authentication/terminus-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/terminus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://support.demandscience.com/hc/en-us/articles/46047614705811-Chat-Experiences-Deprecation-December-31-2025
- group: design
  title: ''
  type: Conformance
  url: conformance/terminus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terminus-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/terminus-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terminus-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Every path on the Terminus developer portal at developer.terminus.com — including /openapi.yaml, /llms.txt and /.well-known/agent-card.json — 302-redirects to a Redocly account login, and the live API host api.terminusplatform.com answers every path with HTTP 401 "Authentication Invalid"; the help center states that Platform API access is issued only by submitting a DemandScience support ticket.
  evidence:
  - status: 302
    url: https://developer.terminus.com/openapi.yaml
  - status: 401
    url: https://api.terminusplatform.com/openapi.json
  - status: 200
    url: https://developer.terminus.com/redocly-login
  - status: 200
    url: https://support.demandscience.com/api/v2/help_center/en-us/articles/360051822454.json
  reason: partner-login
  state: gated
created: '2026-08-05'
description: Terminus is an account-based marketing (ABM) platform covering account-based advertising, web personalization, email-signature marketing (Sigstr), conversational chat (Ramble) and revenue measurement (BrightFunnel). Terminus merged into DemandScience on 2024-11-12; terminus.com now 301-redirects to demandscience.com and the product runs as the DemandScience ABM Platform at app.demandscienceplatform.com. Terminus-branded infrastructure is still in production — api.terminusplatform.com, email.terminusplatform.com (Email Experiences / Signature Ads), terminus.bound360.com (Web Experiences) and *.terminus.services — and the API reference is published on a Redocly developer portal at developer.terminus.com. Platform API access is issued through a support ticket, and every path on the developer portal and the API host requires credentials.
layout: provider
modified: '2026-08-05'
name: Terminus
nav: Providers
network: true
overview: 'Terminus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Account Based Marketing, Marketing, Advertising, and Sales.


  Terminus'' developer surface includes documentation, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 96
score:
  band: emerging
  composite: 26.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 83.3
    governance: 12.5
    operational_transparency: 13.2
  provenance:
    conformance: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Terminus Authentication
  slug: terminus-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Terminus Domain Security
  slug: terminus-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Terminus Trust Center
  slug: terminus-trust-center
  summary_line: trust center published
slug: terminus
tags:
- Company
- Account Based Marketing
- Marketing
- Advertising
- Sales
- B2B
- Analytics
- Email
website: https://demandscience.com/
---
