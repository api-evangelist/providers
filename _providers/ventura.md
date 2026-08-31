---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ventura-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ventura-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/ventura-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ventura-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ventura-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ventura.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ventura.ai/privacy-policy
- group: operate
  title: ''
  type: ContactPage
  url: https://ventura.ai/#contact
- group: operate
  title: ''
  type: Contact
  url: mailto:support@ventura.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getventura
- group: company
  title: ''
  type: Investors
  url: https://www.ycombinator.com/companies/ventura
coverage:
  checked: '2026-08-14'
  detail: 'Ventura sells a hosted AI application that its own team wires into a customer''s ERP during onboarding, not a developer product: api.ventura.ai, docs.ventura.ai and developer.ventura.ai do not resolve in DNS, the marketing site''s sitemap lists only the homepage and the privacy policy, and the customer app at app.ventura.ai 307-redirects every path - including every /.well-known/* path - to /authenticate.'
  evidence:
  - status: 404
    url: https://ventura.ai/openapi.json
  - status: 404
    url: https://ventura.ai/.well-known/agent-card.json
  - status: 404
    url: https://ventura.ai/llms.txt
  - status: 200
    url: https://ventura.ai/sitemap.xml
  - status: 307
    url: https://app.ventura.ai/openapi.json
  - status: 404
    url: https://ventura.ai/pricing
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Ventura builds the AI workforce for distributors and manufacturers, starting with quoting and order entry. It reads inbound requests in any format - emails, PDFs, images, and phone calls - matches products against the customer''s catalog, drafts a quote or order for a sales rep to review and approve, and pushes the approved result into the customer''s ERP, with sales intelligence and a phone agent that transcribes rep calls and creates the resulting quote or order. Ventura plugs into the ERP and CRM a distributor already runs, follows the team''s documented procedures, and learns from every correction. Ventura (formerly Autola) is operated by Gradient Ascent Labs, Inc., a Y Combinator Winter 2026 company based in San Francisco founded by Swen Koller and Jack Collins. As of 2026-08-14 the company publishes a marketing website and a privacy policy only: no public API, developer portal, documentation, SDK, OpenAPI, MCP server, or agent card was found on any Ventura host, and the
  customer application at app.ventura.ai redirects every path to a login.'
image: https://bookface-images.s3.amazonaws.com/small_logos/da34d67bc7bfb583fad0d2c587e602fbe787b210.png
layout: provider
modified: '2026-08-14'
name: Ventura
nav: Providers
network: true
overview: Ventura is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Distributors, and Manufacturers.
plans:
- name: Ventura Plans Pricing
  plan_count: 0
  slug: ventura-plans-pricing
random_paper: 17
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 10.9
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Ventura Domain Security
  slug: ventura-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ventura
tags:
- Company
- Artificial Intelligence
- AI Agents
- Distributors
- Manufacturers
- Quoting
- Order Entry
- ERP
- Industrials
- Sales Automation
- Y Combinator
website: https://www.ventura.ai
---
