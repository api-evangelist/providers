---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: RESTful API marketed to lenders for integrating loan portfolios with Clerkie's recovery platform — payment arrangement recommendations, multi-currency payment processing, delinquency intervention, and
  name: Clerkie API
  slug: clerkie-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.clerkie.io/
- group: start
  title: ''
  type: Portal
  url: https://www.getfiber.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.getfiber.ai/resources
- group: start
  title: ''
  type: SignUp
  url: https://app.clerkie.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s3-us-west-2.amazonaws.com/clerkie-legal/Henry+Labs+-+Terms+of+Use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s3-us-west-2.amazonaws.com/clerkie-legal/Henry+Labs+-+Privacy+Policy.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clerkie-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/clerkie-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clerkie-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: Clerkie markets a RESTful API to lenders on www.clerkie.io/lenders ("For developers, by developers") but ships no developer portal at all — docs.clerkie.io and developers.clerkie.io have no DNS, api.clerkie.io answers its root with a health payload and returns HTTP 500 on every documentation and discovery path, api.getfiber.ai returns 403 Forbidden on every path behind an AWS load balancer, and the only route to the API is a HubSpot "Contact Sales" form.
  evidence:
  - status: 200
    url: https://www.clerkie.io/lenders
  - status: 500
    url: https://api.clerkie.io/openapi.json
  - status: 403
    url: https://api.getfiber.ai/openapi.json
  - status: 404
    url: https://www.getfiber.ai/docs
  - status: 200
    url: https://share.hsforms.com/1EslFlOk3Q6Gc5rFLq26n1w5n2wx
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: Clerkie, operated by Henry Labs Inc. and founded in San Francisco in 2016, is an AI-powered debt management and loan-recovery platform serving both consumers and institutional lenders. The consumer side offers a conversational financial assistant for budgeting, debt negotiation, and personalized repayment planning, while the B2B side — marketed as Fiber, launched in 2021 and now sold on its own domain getfiber.ai — gives lenders, banks, credit unions, and collection agencies an AI-driven recovery suite spanning CRM, an inventory management system (IMS), an AI agent, omnichannel communications, borrower scoring, a self-service payment portal, and workflow automation. Clerkie markets a RESTful API and multi-currency payment processing for lenders to integrate loan portfolios, real-time reporting, and automated repayment arrangements, but publishes no public developer documentation, machine-readable API contract, or self-serve developer portal — integration is arranged through
  a sales conversation. The company has raised over $41M from Left Lane Capital, Flourish Ventures, Vestigo Ventures, and Citibank.
image: https://www.clerkie.io/static/clerkie-logo-white-bc35b467de9da2a6e9ab4dfe5fc98170.png
layout: provider
modified: '2026-08-09'
name: Clerkie
nav: Providers
network: true
overview: 'Clerkie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Debt Management, Lending, and Loan Servicing.


  Clerkie''s developer surface includes developer portal, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.0
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Clerkie Domain Security
  slug: clerkie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clerkie
tags:
- Company
- Fintech
- Debt Management
- Lending
- Loan Servicing
- Debt Collection
- Payments
- Credit
- Financial-Services
- Personal Finance
- AI Agent
- Consumer Finance
website: https://www.clerkie.io/
---
