---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: Backend API for the TrueTracts appraiser console — the subscription platform that performs market definition, comparable selection, time and feature adjustments, heat mapping and 1004MC generation for
  name: TrueTracts API
  slug: truetracts-api
- description: A second production True Footage platform API, discovered through Certificate Transparency (api.trueengine.truefootage.tech) with its own Auth0 custom identity domain at auth.trueengine.truefootage.te
  name: TrueEngine API
  slug: trueengine-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-footage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truefootage.tech/
- group: company
  title: ''
  type: About
  url: https://www.truefootage.tech/about
- group: company
  title: ''
  type: Blog
  url: https://www.truefootage.tech/articles
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truefootage.tech/tools
- group: start
  title: ''
  type: SignUp
  url: https://truetracts.truefootage.tech/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truefootage.tech/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truefootage.tech/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.truefootage.tech/tools/truetracts/ttresourcecenter
- group: company
  title: ''
  type: Careers
  url: https://www.truefootage.tech/join-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/true-footage
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@truefootagetech
- group: agent
  title: ''
  type: WellKnown
  url: well-known/true-footage-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-footage-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/true-footage-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-footage-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Both production API hosts answer 401 {"detail":"authorization header is expected"} on /openapi.json and /docs exactly as they do on every business path, so the FastAPI-shaped contract is served but only to a paid TrueTracts tenant token — there is no public reference, portal, or spec anywhere to read instead.
  evidence:
  - status: 401
    url: https://api.truetracts.truefootage.tech/openapi.json
  - status: 401
    url: https://api.trueengine.truefootage.tech/docs
  - status: 404
    url: https://www.truefootage.tech/llms.txt
  - status: 200
    url: https://auth.truetracts.truefootage.tech/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-05'
description: 'True Footage is a US residential real estate valuation company that pairs staff appraisers with proprietary analytics software, founded in 2021 and operating as a distributed team across appraisal markets nationwide. It runs two connected businesses: an appraisal services arm producing purchase, refinance, HELOC, FHA/VA, PMI-removal, tax-appeal, divorce and date-of-death valuations for lenders, AMCs, investors and homeowners; and an appraiser software arm selling TrueTracts, Spark and Synapse — a subscription console that automates market definition, comparable selection, time and feature adjustments using generalized additive models, heat-mapped location similarity and 1004MC form completion, and exports a PDF workfile. TrueTracts is sold at $49 and $99 per month and integrates with the TOTAL, ACI and ClickFORMS form fillers. The company has raised roughly $119M. There is no public developer program: the platform APIs are real and reachable but reject every unauthenticated
  request, and no OpenAPI, developer portal or API reference is published.'
image: https://cdn.prod.website-files.com/673cdf161331913bdbf34fa9/684127ba41eae9cf49e4fe40_graph_image.png
layout: provider
modified: '2026-08-05'
name: True Footage
nav: Providers
network: true
overview: 'True Footage publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Appraisal, Valuation, and PropTech.


  True Footage''s developer surface includes engineering blog, pricing, signup flow, YouTube channel, authentication, and 11 more developer resources.'
random_paper: 74
score:
  band: emerging
  composite: 20.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 77.8
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 20.6
  provenance:
    conformance: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: True Footage Authentication
  slug: true-footage-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: True Footage Domain Security
  slug: true-footage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: true-footage
tags:
- Company
- Real Estate
- Appraisal
- Valuation
- PropTech
- Mortgage
- Property Data
- Analytics
- Machine Learning
website: https://www.truefootage.tech/
---
