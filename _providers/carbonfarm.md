---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: Image typed files can be dynamically resized and transformed to fit any need.
  name: CarbonFarm Assets API
  slug: carbonfarm-assets-api
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: All data within the platform is private by default. The public role can be configured to expose data without authentication, or you can pass an access token to the API to access private data.
  name: CarbonFarm Authentication API
  slug: carbonfarm-authentication-api
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: Files can be saved in any given location. Directus has a powerful assets endpoint that can be used to generate thumbnails for images on the fly.
  name: CarbonFarm Files API
  slug: carbonfarm-files-api
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: The Items API from CarbonFarm — 2 operation(s) for items.
  name: CarbonFarm Items API
  slug: carbonfarm-items-api
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: The ItemsPost API from CarbonFarm — 2 operation(s) for itemspost.
  name: CarbonFarm Items Post API
  slug: carbonfarm-itemspost-api
- baseURL: https://cms.int.carbonfarm.app
  baseurl_source: declared
  description: Access to where Directus runs. Allows you to make sure your server has everything needed to run the platform, and check what kind of latency we're dealing with.
  name: CarbonFarm Server API
  slug: carbonfarm-server-api
artifact_total: 11
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/carbonfarm-cms-overlay.yaml
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
overview: 'CarbonFarm publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Files API, and 3 more. Tagged areas include Company, Climate Tech, Carbon Credits, Agriculture, and MRV.


  CarbonFarm''s developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Carbonfarm Plans Pricing
  plan_count: 0
  slug: carbonfarm-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Carbonfarm Rate Limits
  slug: carbonfarm-rate-limits
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 53.1
    developer_ergonomics: 20.8
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbonfarm/refs/heads/main/screenshots/carbonfarm-2026-09-02T145013.png
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
- Machine-Learning
- Sustainability
- Content Management
website: https://www.carbonfarm.tech
---
