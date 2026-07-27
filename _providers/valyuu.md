---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Partner-facing trade-in API behind Valyuu's embedded recommerce platform. Version 1 exposes device catalog lookups (categories, brands, series, models, and model condition/attribute questions), FAQ co
  name: Valyuu Partner API
  slug: valyuu-partner-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valyuu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valyuu.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Valyuu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://15q6umhquujjvdoy.public.blob.vercel-storage.com/privacy-policy/(EN)%20Privacy%20policy-SCHnPlBo0ZIC7CyGhWHgpLjRIeEVLE.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://15q6umhquujjvdoy.public.blob.vercel-storage.com/selling-t%26c/(EN)%20Selling%20Terms%20and%20Conditions_Valyuu%20-LdMQiilaDa887YNj0BWw2XEGmYgLmK.pdf
- group: agent
  title: ''
  type: WellKnown
  url: well-known/valyuu-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/valyuu-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valyuu-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/valyuu-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/valyuu-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/valyuu-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/valyuu-sandbox.yml
created: '2026-07-17'
description: Valyuu is an Amsterdam-founded embedded recommerce service provider offering a plug-and-play trade-in platform that businesses integrate to buy back, resell, and recycle used consumer electronics such as smartphones, tablets, and smartwatches across Dutch, German, and English-language markets. Its partner-facing Trade-In API powers embedded trade-in flows covering device catalogs, condition questions, offers, payments, and shipping. Valyuu is a Techstars portfolio company; as of mid-2026 valyuu.com redirects to prioont.com, whose storefront is currently unreachable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valyuu.png
layout: provider
mcp_servers:
- description: ''
  name: valyuu-mcp.yml
  slug: valyuu-mcpyml
modified: '2026-07-21'
name: Valyuu
nav: Providers
network: true
overview: 'Valyuu publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recommerce, Trade-In, Circular Economy, and Consumer Electronics.


  Valyuu''s developer surface includes authentication, sandbox, and 10 more developer resources.'
random_paper: 66
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Valyuu Authentication
  slug: valyuu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valyuu Domain Security
  slug: valyuu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valyuu
tags:
- Company
- Recommerce
- Trade-In
- Circular Economy
- Consumer Electronics
- Sustainability
- eCommerce
website: https://valyuu.com/
---
