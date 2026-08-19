---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Directus 10.10.7 headless CMS that serves carbonfarm.tech's news posts and image assets. It publishes a real OpenAPI 3.0.1 (14 operations) and a full GraphQL SDL anonymously at /server/specs/oas a
  name: CarbonFarm CMS Content API
  slug: carbonfarm-cms-content-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.carbonfarm.tech
- group: company
  title: ''
  type: Blog
  url: https://carbonfarm.tech/posts
- group: operate
  title: ''
  type: Support
  url: https://carbonfarm.tech/contact
- group: start
  title: ''
  type: Login
  url: https://app.carbonfarm.tech
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carbonfarm.tech/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbonfarmtech
- group: auth
  title: ''
  type: Authentication
  url: authentication/carbonfarm-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carbonfarm-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carbonfarm-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carbonfarm-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carbonfarm-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carbonfarm-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carbonfarm-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carbonfarm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carbonfarm-rate-limits.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/carbonfarm-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carbonfarm-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carbonfarm-domain-security.yml
created: '2026-08-17'
description: 'CarbonFarm Technology is a French climate-tech company (registered in Nanterre, SIREN 912160389) that uses satellite imagery and proprietary machine-learning models to monitor, measure and verify greenhouse-gas reductions in rice production. Rice accounts for roughly 12% of global methane emissions, and practices such as Alternate Wetting and Drying can cut paddy methane substantially — but conventional MRV depends on self-declared practices recorded in paper logbooks, which is expensive to collect from smallholders and open to fraud. CarbonFarm detects water-management and straw-management practices remotely at paddy level, estimates baseline and project emissions with validated models, and verifies additionality, at a fraction of the cost of ground-based MRV. Customers and partners named publicly include Mars Food, Tilda, Beneo, Amru Rice, Vida Energy, Fortune Rice, Ostrom Climate, Core Carbon X, the Sustainable Rice Platform, UNDP, Danone, Rikolto, Cornell University, IRRI
  and Regrow Ag. CarbonFarm operates no developer program: there is no developer portal, API reference, SDK or public API product, and the client platform sits behind an Auth0 organization login. The one machine-readable contract it publishes is the Directus headless CMS behind its marketing website.'
graphqls:
- description: 'generated: ''2026-08-17'''
  name: CarbonFarm CMS — GraphQL schema
  slug: carbonfarm-cms-graphql
image: https://carbonfarm.tech/opengraph-image.png?opengraph-image.d25adc5b.png
layout: provider
modified: '2026-08-17'
name: CarbonFarm
nav: Providers
network: true
overview: 'CarbonFarm publishes 1 API on the [APIs.io](https://apis.io/) network: CMS Content API. Tagged areas include Company, Climate Tech, Carbon Credits, Agriculture, and MRV.


  CarbonFarm''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
plans:
- name: Carbonfarm Plans Pricing
  plan_count: 0
  slug: carbonfarm-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Carbonfarm Rate Limits
  slug: carbonfarm-rate-limits
score:
  band: thin
  composite: 32.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 30.3
    contract_quality: 50.6
    developer_ergonomics: 20.8
    discoverability: 77.8
    governance: 30.3
    operational_transparency: 2.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Carbonfarm Authentication
  slug: carbonfarm-authentication
  summary_line: apiKey/openIdConnect · 3 schemes
- kind: domain-security
  name: Carbonfarm Domain Security
  slug: carbonfarm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: carbonfarm
tags:
- Company
- Climate Tech
- Carbon Credits
- Agriculture
- MRV
- Satellite Imagery
- Remote Sensing
- Machine Learning
- Sustainability
- Content Management
website: https://www.carbonfarm.tech
---
