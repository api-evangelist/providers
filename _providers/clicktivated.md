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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://clicktivated.com/
- group: company
  title: ''
  type: Blog
  url: https://clicktivated.com/blog
- group: operate
  title: ''
  type: Support
  url: https://clicktivated.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clicktivated.com/legal/terms-conditions
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clicktivated-domain-security.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/clicktivated-graphql.yml
- group: design
  title: ''
  type: Components
  url: components/clicktivated-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clicktivated-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clicktivated-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clicktivated-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/clicktivated-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clicktivated-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clicktivated-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clicktivated-llms.txt
coverage:
  checked: '2026-08-12'
  detail: Clicktivated sells a managed shoppable-video service, not a developer product — its own how-it-works page promises "no complex API setups" — and the only machine surface that exists anywhere is a private Apollo GraphQL endpoint at api.clicktivatedstudio.com/graphql behind the Studio dashboard, which has introspection disabled and no portal, spec, SDK, reference, or key issuance of any kind published for it.
  evidence:
  - status: 404
    url: https://clicktivated.com/api
  - status: 200
    url: https://clicktivated.com/sitemap.xml
  - status: 400
    url: https://api.clicktivatedstudio.com/graphql
  - status: 403
    url: https://api.clicktivatedstudio.com/openapi.json
  - status: 404
    url: https://clicktivated.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Clicktivated is a video technology platform that turns existing video content into interactive, shoppable experiences without re-shooting or re-editing. Its "Activate, Distribute, Optimize" workflow makes any video clickable the same day, deploys it programmatically across DSPs, SSPs, publishers, and direct site embeds, and captures first-party intent signals - item-level and place-level - to improve targeting, measure lift, and drive better performance. The company serves retail brands closing the gap between inspiration and purchase, and tourism brands converting inspiration into itineraries. Founded as Clicktivated Video, Inc. and backed by Techstars, with offices in Detroit, New York, Dubai, and Sydney.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clicktivated.png
layout: provider
modified: '2026-08-12'
name: Clicktivated
nav: Providers
network: true
overview: 'Clicktivated is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video, Interactive Video, Shoppable Video, and Advertising Technology.


  Clicktivated''s developer surface includes engineering blog, support, and 12 more developer resources.'
plans:
- name: Clicktivated Plans Pricing
  plan_count: 0
  slug: clicktivated-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Clicktivated Rate Limits
  slug: clicktivated-rate-limits
score:
  band: minimal
  composite: 9.8
  coverage:
    artifact_dirs: 15
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 9.8
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clicktivated/refs/heads/main/screenshots/clicktivated-2026-07-25T205616.png
security:
- kind: authentication
  name: Clicktivated Authentication
  slug: clicktivated-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Clicktivated Domain Security
  slug: clicktivated-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clicktivated
tags:
- Company
- Video
- Interactive Video
- Shoppable Video
- Advertising Technology
- First-Party Data
- Retail
- Tourism
website: https://clicktivated.com/
---
