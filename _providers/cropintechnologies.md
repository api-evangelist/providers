---
access_model:
  confidence: low
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: true
  source:
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/cropintechnologies/llms/cropintechnologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cropintechnologies-llms.txt
- group: build
  href: https://artifacts.apis.io/cropintechnologies/integrations/cropintechnologies-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cropintechnologies-integration-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.cropin.com
- group: company
  title: ''
  type: Blog
  url: https://www.cropin.com/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.cropin.com/contact/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cropin.com/newsroom/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.cropin.com/trust/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cropin.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cropin.com/privacy-policy/
- group: other
  href: https://artifacts.apis.io/cropintechnologies/hosts/cropintechnologies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cropintechnologies-hosts.yml
- group: other
  href: https://artifacts.apis.io/cropintechnologies/vendors/cropintechnologies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cropintechnologies-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cropintechnologies/security/cropintechnologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cropintechnologies-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: Cropin runs a real API surface behind an Apigee gateway (api.cropin.com 403, api.cropin.in Apigee 'Unable to route' 500) and the Cropin Cloud platform page advertises 'APIs and MCP' as a feature, but docs.cropin.in serves a JS redirect to /CropInMVC/ (customer login) and cloud.cropin.in / smartfarm.cropin.com are login shells. No public developer portal, API reference, OpenAPI/AsyncAPI/GraphQL/MCP/gRPC/WSDL/Postman artifact, SDK or pricing page found; /robots.txt disallows /api/.
  evidence:
  - status: 403
    url: https://api.cropin.com/
  - status: 403
    url: https://api.cropin.com/openapi.json
  - status: 403
    url: https://api.cropin.com/graphql
  - status: 403
    url: https://api.cropin.com/mcp
  - status: 500
    url: https://api.cropin.in/
  - status: 200
    url: https://docs.cropin.in/
  - status: 200
    url: https://www.cropin.com/platform/
  - status: 200
    url: https://www.cropin.com/llms.txt
  - status: 404
    url: https://www.cropin.com/openapi.json
  - status: 404
    url: https://www.cropin.com/.well-known/mcp.json
  - status: 404
    url: https://www.cropin.com/api-reference/
  reason: customer-only-docs
  state: gated
created: '2026-10-11'
description: Cropin is an agricultural and physical-world intelligence company (founded 2010, headquartered in Bengaluru, India) that turns field records, satellite observation, weather and climate data into decisions on crops, supply, water, forests, energy and land risk. Its Cropin Cloud platform combines field apps and workflows, the OrbitAI agentic intelligence assistant, domain-specific models and a data foundry, and is used by food, retail, seed, government, utilities, banking and insurance enterprises in 103 countries.
image: https://www.cropin.com/og/home.png
layout: provider
modified: '2026-11-04'
name: Cropin
nav: Providers
network: true
overview: 'Cropin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Satellite Intelligence, Climate Data, and Crop Intelligence.


  Cropin''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Cropintechnologies Plans Pricing
  plan_count: 0
  slug: cropintechnologies-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Cropintechnologies Rate Limits
  slug: cropintechnologies-rate-limits
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.8
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cropintechnologies Authentication
  slug: cropintechnologies-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cropintechnologies Domain Security
  slug: cropintechnologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cropintechnologies
tags:
- Company
- Agriculture
- Satellite Intelligence
- Climate Data
- Crop Intelligence
- Supply Chain
- Sustainability
- AI Agents
- EUDR Compliance
website: https://www.cropin.com
---
