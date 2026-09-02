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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.recapped.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.recapped.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.recapped.io
- group: start
  title: ''
  type: Login
  url: https://app.recapped.io
- group: operate
  title: ''
  type: Support
  url: mailto:help@recapped.io
- group: company
  title: ''
  type: Blog
  url: https://www.recapped.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recapped.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recapped.io/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.recapped.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/recapped-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recapped-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recapped-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Recapped
- group: commercial
  title: ''
  type: Plans
  url: plans/recapped-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recapped-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recapped-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recapped-conformance.yml
coverage:
  checked: '2026-08-13'
  detail: RecappED shipped an end-user sales-room product with no developer program at all — api.recapped.io, docs.recapped.io and developer.recapped.io have no DNS record, /llms.txt and every /.well-known/ path 404 on www.recapped.io, and the company announced on 2026-07-31 that it is shutting down; the only machine-oriented document it publishes is the customer data-export schema in github.com/Recapped/customer-offboarding-docs.
  evidence:
  - status: 404
    url: https://www.recapped.io/llms.txt
  - status: 404
    url: https://www.recapped.io/openapi.json
  - status: 404
    url: https://www.recapped.io/.well-known/agent-card.json
  - status: 200
    url: https://raw.githubusercontent.com/Recapped/customer-offboarding-docs/main/README.md
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: RecappED (recapped.io) is an AI-powered digital sales room and customer onboarding platform for B2B revenue teams. It consolidates the buying and selling process into a single collaborative workspace with mutual action plans, deal management, buyer-engagement tracking, AI deal intelligence, an AI sales coach, and structured handoffs from sales to implementation. Integration with CRM and sales tooling is delivered through native connectors (Salesforce, HubSpot, Slack, Gong, Clari, Zoom) and Zapier rather than a public developer API; no OpenAPI, developer portal, or public REST reference is published. The platform announced it is shutting down on 2026-07-31 and is not accepting new customers; probed again on 2026-08-13 the site and application were still serving, with the shutdown banner on every page. The one machine-oriented document the company publishes is the schema of the customer offboarding data export, in the github.com/Recapped organization. Surfaced as a CRV portfolio
  company and enriched into the API Evangelist network.
image: https://cdn.prod.website-files.com/61af7c094ef4b24b1e3eda92/61dee2a765d386544289a873_Link%20preview%20image.jpg
layout: provider
modified: '2026-08-13'
name: RecappED
nav: Providers
network: true
overview: 'RecappED is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Sales Enablement, Digital Sales Room, and Customer Onboarding.


  RecappED''s developer surface includes pricing, signup flow, support, engineering blog, and 13 more developer resources.'
plans:
- name: Recapped Plans Pricing
  plan_count: 7
  slug: recapped-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Recapped Rate Limits
  slug: recapped-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.5
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Recapped Domain Security
  slug: recapped-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Recapped Trust Center
  slug: recapped-trust-center
  summary_line: SOC 2, GDPR
slug: recapped
tags:
- Company
- Sales
- Sales Enablement
- Digital Sales Room
- Customer Onboarding
- CRM
- Revenue Operations
website: https://www.recapped.io/
---
