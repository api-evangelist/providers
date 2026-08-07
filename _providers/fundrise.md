---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Fundrise Agentic Access
  operation_count: 17
  slug: fundrise-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 1
apis:
- description: Fundrise Connect is Fundrise's external partner API for Client onboarding and investment into its alternative-asset offerings. It is organized around REST with resource-oriented URLs, JSON responses a
  name: Fundrise Connect API
  slug: fundrise-connect
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'The primary Fundrise Connect flow, modelled from the sequence Fundrise publishes under the "Workflow Example" tag of its own OpenAPI: create a Client, exchange the issued refresh token for a Client ac'
  name: Fundrise Connect — onboard a Client and place an Investment
  slug: fundrise-onboard-client-and-invest
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://fundrise.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fundrise.com/connect-api
- group: docs
  title: ''
  type: Documentation
  url: https://connect.fundrise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://connect.fundrise.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://connect.fundrise.com/#tag/Authentication
- group: start
  title: ''
  type: SignUp
  url: https://fundrise.com/checkout-start
- group: start
  title: ''
  type: Login
  url: https://fundrise.com/login
- group: operate
  title: ''
  type: Support
  url: https://fundrise.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://fundrise.com/help
- group: company
  title: ''
  type: Blog
  url: https://fundrise.com/education
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fundrise
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fundrise.com/website-documents/Terms%20of%20Service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fundrise.com/privacy-policy.html
- group: auth
  title: ''
  type: Security
  url: https://fundrise.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fundrise-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fundrise-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fundrise-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fundrise-domain-security.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/fundrise-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fundrise-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: 'Fundrise is a Washington, DC based financial technology company that gives individual investors direct access to private-market alternative assets — private real estate, private credit, and venture capital — through a family of non-traded funds it sponsors and manages. Founded in 2012 and an early user of the SEC''s Regulation A+ exemption, Fundrise packages institutional-grade private investments into low-minimum vehicles bought and held entirely online. Its developer-facing surface is Fundrise Connect, a REST API that lets banks, brokerages, investment apps and other financial platforms natively onboard their own end users (\"Clients\") into Fundrise offerings: create and update Clients, retrieve open Offerings and their historical daily NAV, fetch the offering documents and acknowledgments a Client must sign, place and cancel investments, request and cancel share liquidations, and read back holdings, transactions and tax forms. Access is gated — partners request credentials
  from the Fundrise Connect team — and the API is documented publicly with an OpenAPI 3.1 definition.'
image: https://fundrise.com/favicon.ico
layout: provider
modified: '2026-08-04'
name: Fundrise
nav: Providers
network: true
overview: 'Fundrise publishes 1 API on the [APIs.io](https://apis.io/) network: Connect API. Tagged areas include Company, Financial Services, Investing, Real Estate, and Private Credit.


  Fundrise''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, and 15 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 0
  name: Fundrise Rate Limits
  slug: fundrise-rate-limits
scopes:
- name: Fundrise Scopes
  scope_count: 2
  slug: fundrise-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 68.2
    developer_ergonomics: 42.9
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Fundrise Authentication
  slug: fundrise-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Fundrise Domain Security
  slug: fundrise-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Fundrise Vulnerability Disclosure
  slug: fundrise-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fundrise
tags:
- Company
- Financial Services
- Investing
- Real Estate
- Private Credit
- Venture Capital
- Alternative Assets
- Wealth Management
- Fintech
- Embedded Investing
website: https://fundrise.com/
---
