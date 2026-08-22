---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.7
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/credit-karma-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.creditkarma.com
- group: operate
  title: ''
  type: Support
  url: https://support.creditkarma.com/s
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.creditkarma.com/s
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.creditkarma.com/about/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.intuit.com/privacy/statement/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/creditkarma
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/credit-karma-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/credit-karma-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/credit-karma-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/credit-karma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.creditkarma.com/about/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/credit-karma-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.creditkarma.com/about/security
- group: company
  title: ''
  type: Blog
  url: https://www.creditkarma.com/insights
- group: build
  title: ''
  type: Packages
  url: packages/credit-karma-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/credit-karma-llms.txt
created: '2026-07-17'
description: Credit Karma is an AI-powered personal finance platform founded in 2007 and owned by Intuit since 2020, serving more than 140 million members in the US, UK and Canada. It began as a free credit-score and credit-monitoring destination and has grown into a broad consumer finance marketplace spanning credit cards, personal and auto loans, mortgages, auto and home insurance, banking (checking, savings and credit-builder accounts), tax filing, and identity monitoring. Credit Karma monetizes through personalized recommendations and lead generation rather than a public developer or partner API; it maintains no external consumer-facing API program. It does run an active engineering culture with 29 public open-source repositories on GitHub (Thrift and GraphQL tooling), a coordinated vulnerability disclosure program via HackerOne, and SOC 2 / ISO 27001 security certifications.
image: https://logo.clearbit.com/creditkarma.com
layout: provider
mcp_servers:
- description: ''
  name: credit-karma-mcp.yml
  slug: credit-karma-mcpyml
modified: '2026-08-08'
name: Credit Karma
nav: Providers
network: true
overview: 'Credit Karma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Personal Finance, Credit Scores, and Credit Monitoring.


  Credit Karma''s developer surface includes support, engineering blog, and 15 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.8
  delta: -11.3
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 21.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/credit-karma/refs/heads/main/screenshots/credit-karma-2026-07-25T210719.png
security:
- kind: domain-security
  name: Credit Karma Domain Security
  slug: credit-karma-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Credit Karma Vulnerability Disclosure
  slug: credit-karma-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Credit Karma Trust Center
  slug: credit-karma-trust-center
  summary_line: SOC 2, ISO 27001
slug: credit-karma
tags:
- Company
- Fintech
- Personal Finance
- Credit Scores
- Credit Monitoring
- Lending
- Consumer Finance
- Insurance
- Banking
website: https://www.creditkarma.com
---
