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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ciro.io/
- group: start
  title: ''
  type: Login
  url: https://app.ciro.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ciro.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ciro.io/terms-of-service
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ciro.io
- group: auth
  title: ''
  type: Compliance
  url: security/ciro-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ciro-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ciro-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ciro-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ciro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ciro-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/ciro-packages.yml
coverage:
  checked: '2026-08-14'
  detail: Ciro ships its AI prospecting agent only as a Slack app and a hosted web application — api.ciro.io, docs.ciro.io, developer.ciro.io and developers.ciro.io are all NXDOMAIN, and the 15-URL sitemap contains no developer, docs or API page at all.
  evidence:
  - status: 404
    url: https://ciro.io/openapi.json
  - status: 404
    url: https://www.ciro.io/docs
  - status: 404
    url: https://app.ciro.io/mcp
  - status: 404
    url: https://app.ciro.io/graphql
  - status: 404
    url: https://ciro.io/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ciro-io
  - status: 200
    url: https://www.ciro.io/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Ciro (Ciro Technologies Inc.) is an AI sales platform that finds a revenue team's best accounts, deeply qualifies each contact, runs a contact data waterfall for verified emails and phone numbers, and writes signal-based outbound that is pushed directly into existing sales tools. Reps command Ciro in plain English from Slack, where it runs prospect searches, enriches contacts, queries the CRM, analyzes CSVs, drafts multi-step personalized email sequences, and recommends the highest-ROI campaigns. It integrates with Salesforce and HubSpot (CRM); Salesloft, Outreach, Gong Engage, and Instantly (sales engagement); Slack; and webhook-based export to Clay and Zapier. Ciro is sold through a sales-led motion with no published pricing, is SOC 2 Type II certified, and was backed by Y Combinator and CRV. On 2026-07-08 Reevo announced it had acquired Ciro and is folding the prospecting agent into its revenue operating system; ciro.io remains live and still sells, and every page now carries
  an "acquired by Reevo" banner. Ciro was surfaced as a portfolio company of CRV and enriched into the API Evangelist network. It publishes no public developer API, no developer documentation, no OpenAPI, GraphQL, MCP or AsyncAPI contract, no SDK in any package registry, and no /.well-known/ document — every one of those was probed on 2026-08-14 and missed.
image: https://ciro.io/og-image.png
layout: provider
modified: '2026-08-14'
name: Ciro
nav: Providers
network: true
overview: Ciro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sales, Sales Intelligence, Sales Engagement, and Prospecting.
plans:
- name: Ciro Plans Pricing
  plan_count: 0
  slug: ciro-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ciro Rate Limits
  slug: ciro-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ciro/refs/heads/main/screenshots/ciro-2026-07-25T205418.png
security:
- kind: domain-security
  name: Ciro Domain Security
  slug: ciro-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Ciro Trust Center
  slug: ciro-trust-center
  summary_line: SOC 2 Type II
slug: ciro
tags:
- Company
- Sales
- Sales Intelligence
- Sales Engagement
- Prospecting
- Contact Enrichment
- Lead Generation
- Go-To-Market
- Artificial Intelligence
- CRM
- Slack
- B2B
website: https://www.ciro.io/
---
