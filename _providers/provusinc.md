---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://provus.ai/pricing/
  - https://provus.ai/cpq-express/
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.4
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://provus.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.provus.ai
- group: company
  title: ''
  type: Blog
  url: https://provus.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://provus.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://provus.ai/product-demo/
- group: operate
  title: ''
  type: Support
  url: https://provus.ai/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://provus.ai/terms-of-service/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/provusinc-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provusinc-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/provusinc-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/provusinc-lifecycle.yml
coverage:
  checked: '2026-08-13'
  detail: Provus publishes no developer portal or spec at all — the entire product reference is a Document360 knowledge base at docs.provus.ai that 302s every path to https://docs.provus.ai/login, and the product itself ships as a Salesforce AppExchange managed package whose integration surface is Salesforce's, not Provus'.
  evidence:
  - status: 302
    url: https://docs.provus.ai/
  - status: 404
    url: https://provus.ai/.well-known/agent-card.json
  - status: 404
    url: https://provus.ai/openapi.json
  - status: 404
    url: https://developer.provus.ai/
  - status: 200
    url: https://api.github.com/orgs/provusinc
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Provus (Provusinc) is an agentic AI Configure, Price, Quote (CPQ) platform built specifically for services organizations — professional services, consulting, and asset-based services firms. The platform turns unstructured inputs such as emails, RFPs, and call notes into structured, accurate services quotes, and runs a set of AI agents (Quote Optimizer, Deal Predictor, Proposal Response, Deal Rescue, and Provus Admin) that monitor deals, optimize pricing, assess risk, and protect margin. Provus ships two products — CPQ Express for growing teams and Enterprise Services CPQ for large organizations — with native connectors to Salesforce, HubSpot, Kantata, NetSuite, and DocuSign. It is backed by Norwest Venture Partners and reports managing over $5B in enterprise services revenue across customers including Thoughtworks, Trace3, and Prolifics. Provus does not currently publish a public developer API, OpenAPI specification, or developer portal; integration is delivered through native
  prebuilt connectors and a Salesforce AppExchange managed package, and product help documentation is hosted on a Document360 knowledge base at docs.provus.ai that 302s the entire site to a login. Provus names an internal "Profet API" in its published sub-processor list, but that service is not documented, versioned, or reachable publicly.
image: https://provus.ai/wp-content/uploads/2021/08/Provus-Blue-Logo.png
layout: provider
modified: '2026-08-13'
name: Provus
nav: Providers
network: true
overview: 'Provus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CPQ, Services Quoting, Professional Services, and Pricing.


  Provus'' developer surface includes documentation, engineering blog, pricing, signup flow, support, and 6 more developer resources.'
plans:
- name: Provusinc Plans Pricing
  plan_count: 2
  slug: provusinc-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Provusinc Rate Limits
  slug: provusinc-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Provusinc Domain Security
  slug: provusinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: provusinc
tags:
- Company
- CPQ
- Services Quoting
- Professional Services
- Pricing
- AI Agents
- Sales
- Software-as-a-Service
website: https://provus.ai
---
