---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arundo-analytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arundo.com/
- group: operate
  title: ''
  type: Support
  url: https://support.arundo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.arundo.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arundo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arundo-analytics-inc-
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arundo.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arundo.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.arundo.com
- group: start
  title: ''
  type: Login
  url: https://carbonpath.arundo.com/
- group: other
  title: ''
  type: SecondaryMarketProfile
  url: https://forgeglobal.com/arundo-analytics_stock/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arundo-analytics-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arundo-analytics-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arundo-analytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arundo-analytics-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arundo-analytics-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/arundo-analytics-packages.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/arundo-analytics-foundation-compute.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arundo-analytics-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Arundo markets "Arundo Foundation APIs" on its technology page but publishes no developer portal or reference anywhere — the only routes in are the CarbonPath and Marathon apps, which bounce to an Auth0 tenant login, and a Jira Service Management customer portal, while the old api.arundo.com host is a 2017 static S3 bucket that 404s every path.
  evidence:
  - status: 400
    url: https://carbonpath.arundo.com/
  - status: 404
    url: https://api.arundo.com/openapi.json
  - status: 404
    url: https://www.arundo.com/docs
  - status: 200
    url: https://arundo.eu.auth0.com/.well-known/openid-configuration
  reason: customer-only-docs
  state: gated
created: '2026-08-06'
description: Arundo Analytics is an industrial AI company with offices in Oslo, Stockholm, Heidelberg and Houston, building software for asset-heavy industries such as oil and gas, maritime and shipping, chemicals and manufacturing. Its Arundo AI Foundation platform combines a knowledge graph of asset hierarchies and sensor metadata, industrial time-series storage built for high-velocity sensor data, parallelised machine-learning model orchestration, and specialised AI agents, surfaced through the AI Foundation Studio and what the company calls the Arundo Foundation APIs. Packaged applications include Marathon (continuous equipment condition monitoring), ArundoEdge and Edge Manager (secure streaming of IoT sensor data from control systems to the cloud), Energy Optimizer, CarbonPath (Scope 3 emissions management for shipping) and AI Companion. Arundo also maintains the open-source Python packages ADTK (unsupervised time-series anomaly detection) and tsaug (time-series augmentation), and publishes
  a public Foundation compute plug-in contract on GitHub. The Foundation APIs themselves are marketed on the public site but are not publicly documented; there is no developer portal, no public API reference and no machine-readable specification, and the applications sit behind an Auth0 customer login.
image: https://cdn.prod.website-files.com/628b26907521666ea45674fa/62ab23ffdc11279ec1b336a5_Favicin_Square_256x256.png
json_schemas:
- name: Arundo Foundation compute plug-in contract
  property_count: 0
  slug: arundo-analytics-foundation-compute
layout: provider
modified: '2026-08-06'
name: Arundo Analytics
nav: Providers
network: true
overview: 'Arundo Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial AI, Industrial IoT, Analytics, and Machine-Learning.


  Arundo Analytics'' developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 3
scopes:
- name: Arundo Analytics Scopes
  scope_count: 14
  slug: arundo-analytics-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 23.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arundo-analytics/refs/heads/main/screenshots/arundo-analytics-2026-08-07T161747.png
security:
- kind: authentication
  name: Arundo Analytics Authentication
  slug: arundo-analytics-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Arundo Analytics Domain Security
  slug: arundo-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arundo-analytics
tags:
- Company
- Industrial AI
- Industrial IoT
- Analytics
- Machine-Learning
- Time Series
- Asset Performance Management
- Anomaly Detection
- Energy
- Maritime
- Oil and Gas
- Manufacturing
website: https://www.arundo.com/
---
