---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-brandtech-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thebrandtechgroup.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://trypencil.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.trypencil.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.trypencil.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.trypencil.com/en/
- group: company
  title: ''
  type: Blog
  url: https://trypencil.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thebrandtechgroup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trypencil.com/legals/pencil-pro-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thebrandtechgroup.com/privacy-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.trypencil.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trypencil.com/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/the-brandtech-group-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-brandtech-group-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/the-brandtech-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-brandtech-group-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/the-brandtech-group-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/the-brandtech-group-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-brandtech-group-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/the-brandtech-group-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/the-brandtech-group-packages.yml
coverage:
  checked: '2026-08-30'
  detail: The Brandtech Group sells agency services and one end-user SaaS product (Pencil) and runs no developer program at all — trypencil.com/openapi.json 404s, app.trypencil.com, pro.trypencil.com and cn.trypencil.com answer every spec, GraphQL and /.well-known path with the same 3,480-byte React shell, and the one production API host in the group, api.acorn-i.com, is an AWS API Gateway that returns "Missing Authentication Token" on its root with no documentation, sign-up or key issuance published anywhere.
  evidence:
  - status: 404
    url: https://trypencil.com/openapi.json
  - status: 200
    url: https://app.trypencil.com/openapi.json
  - status: 403
    url: https://api.acorn-i.com/openapi.json
  - status: 404
    url: https://trypencil.com/.well-known/agent-card.json
  - status: 200
    url: https://trypencil.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-30'
description: 'The Brandtech Group is a privately held marketing and marketing-technology holding group founded in 2015 by former Havas CEO David Jones as You & Mr Jones and renamed in 2022. It positions itself as a generative-AI marketing group and operates a portfolio of wholly owned brands rather than a single product: Oliver (in-house agency), Jellyfish (digital and performance marketing), Pencil (a generative-AI creative platform for ad copy, image and video), Acorn-i (Amazon and ecommerce retail-media analytics), fifty-five and DP6 (data and marketing science), Collectively (creator and influencer marketing), Mobkoi, Gravity Road, Mofilm and Brandtech Consulting. Its customer-facing software surface is Pencil, a SaaS platform that orchestrates third-party generative-AI models (OpenAI, Google, Adobe, Runway, Bria) and pushes creative into Meta, TikTok, YouTube, Google Display, DV360 and LinkedIn. The group publishes no developer portal, no OpenAPI or other machine-readable contract,
  and no public API keys or SDKs; integration is delivered through the products themselves and through partner connectors.'
image: https://thebrandtechgroup.com/apple-touch-icon.png
layout: provider
modified: '2026-08-30'
name: The Brandtech Group
nav: Providers
network: true
overview: 'The Brandtech Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Advertising, Generative AI, and Creative.


  The Brandtech Group''s developer surface includes pricing, signup flow, support, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: The Brandtech Group Plans Pricing
  plan_count: 3
  slug: the-brandtech-group-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: The Brandtech Group Rate Limits
  slug: the-brandtech-group-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 11
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 34.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
security:
- kind: domain-security
  name: The Brandtech Group Domain Security
  slug: the-brandtech-group-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: The Brandtech Group Trust Center
  slug: the-brandtech-group-trust-center
  summary_line: SOC 2 Type II
slug: the-brandtech-group
tags:
- Company
- Marketing
- Advertising
- Generative AI
- Creative
- Marketing Technology
- Retail Media
- Analytics
- Agency
website: https://thebrandtechgroup.com/
---
