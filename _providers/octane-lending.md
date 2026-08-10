---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octane-lending-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octane.co/o/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/octane-lending_stock/
- group: company
  title: ''
  type: Blog
  url: https://octane.co/o/blog/
- group: company
  title: ''
  type: Press
  url: https://octane.co/o/press/
- group: operate
  title: ''
  type: Support
  url: https://octane.co/o/who-we-are/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://octane.co/o/who-we-are/help-faq/
- group: start
  title: ''
  type: SignUp
  url: https://octane.co/o/dealer-signup/
- group: start
  title: ''
  type: Login
  url: https://dealer.octane.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octane.co/o/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octane.co/o/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctaneLending
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/octane-lending-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Octane markets DMS integrations (AppOne, Ekho) but publishes no developer host at all — developer/docs/api.octane.co do not resolve — and the only reachable API host, los.octane.co (the Dealer Portal's API_BASE_URL, read from https://dealer.octane.co/config.js), 302s straight to the authenticated dealer portal, with partner API credentials coordinated one-to-one by an Octane account manager.
  evidence:
  - status: 302
    url: https://los.octane.co/
  - status: 404
    url: https://los.octane.co/openapi.json
  - status: 403
    url: https://dealer.octane.co/openapi.json
  - status: 404
    url: https://octane.co/.well-known/agent-card.json
  - status: 200
    url: https://ekho.com/integration/octane-lending/
  reason: partner-login
  state: gated
created: '2026-08-04'
description: Octane (Octane Lending, Inc.) is a New York City fintech founded in 2014 that makes powersports, outdoor power equipment and recreational-vehicle financing as simple as paying cash. It runs an end-to-end digital lending platform — instant soft-pull prequalification for consumers, real-time credit decisioning and eContracting through its in-house lender Roadrunner Financial, Inc., and loan servicing — connecting more than 4,000 dealer partners and 30-plus OEMs with prime through non-prime buyers. Its Dealer Portal 2.0 and dealer-management-system integrations (AppOne, Ekho and similar DMS platforms) submit credit applications and return decisions over a partner API whose credentials are coordinated privately by Octane account managers; Octane publishes no public developer portal, API documentation or machine-readable specification.
image: https://octane.co/o/wp-content/uploads/2019/11/octane-sq-blue.png
layout: provider
modified: '2026-08-04'
name: Octane Lending
nav: Providers
network: true
overview: 'Octane Lending is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, Consumer Finance, and Powersports.


  Octane Lending''s developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 15.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octane-lending/refs/heads/main/screenshots/octane-lending-2026-08-07T185931.png
security:
- kind: domain-security
  name: Octane Lending Domain Security
  slug: octane-lending-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: octane-lending
tags:
- Company
- Financial Services
- Lending
- Consumer Finance
- Powersports
- Fintech
- Loan Origination
- Dealer Software
website: https://octane.co/o/
---
