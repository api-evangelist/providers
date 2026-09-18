---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: 'Rayonier''s self-managed ArcGIS Enterprise 11.5 server (portalDeploymentType ArcGISEnterprise, single tenant) on gis.rayonier.com. The Public folder (29 services) and Hosted folder (16 services) — 102 '
  name: Rayonier GIS Services (ArcGIS REST)
  slug: rayonier-gis-services
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.rayonier.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rayonier.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rayonier.com/legal#privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rayonier
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rayonier
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/security/rayonier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rayonier-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/packages/rayonier-packages.yml
  title: ''
  type: Packages
  url: packages/rayonier-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/lifecycle/rayonier-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rayonier-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/conformance/rayonier-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rayonier-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/llms/rayonier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rayonier-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/plans/rayonier-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rayonier-plans-pricing.yml
created: '2026-04-19'
description: 'Rayonier (NYSE: RYN) is a timberland real estate investment trust owning about 2 million acres in the US South and Pacific Northwest. It publishes no developer program, SDK or OpenAPI, but it runs a self-hosted ArcGIS Enterprise 11.5 instance at gis.rayonier.com whose Public and Hosted folders — 45 Feature and Map services, 102 layers covering fee ownership, hunting lease units, bee-lease sites, land-sale tracts, forest stand inventory and wildfire overlays — answer anonymously over the GeoServices REST API and a SOAP/WSDL contract. Rayonier''s own hunting, beekeeping and Raydient land-sales websites consume these services.'
finops:
- name: Rayonier Finops
  service_category: Forestry / Real Estate
  slug: rayonier-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rayonier.png
layout: provider
modified: '2026-09-17'
name: Rayonier
nav: Providers
network: true
overview: Rayonier publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Timber, Real-Estate, Forest Products, Geospatial, and ArcGIS REST.
plans:
- name: Rayonier Plans Pricing
  plan_count: 1
  slug: rayonier-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rayonier Rate Limits
  slug: rayonier-rate-limits
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.0
  facets:
    access_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 28.0
    discoverability: 68.5
    operational_transparency: 2.6
  previous_composite: 10.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/rayonier/refs/heads/main/screenshots/rayonier-2026-06-20T192619.png
security:
- kind: authentication
  name: Rayonier Authentication
  slug: rayonier-authentication
  summary_line: none/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Rayonier Domain Security
  slug: rayonier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rayonier
tags:
- Timber
- Real-Estate
- Forest Products
- Geospatial
- ArcGIS REST
- Land Management
- Hunting Leases
- Forestry
website: https://www.rayonier.com
---
