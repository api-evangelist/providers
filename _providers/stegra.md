---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stegra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stegra.com/en
- group: company
  title: ''
  type: Blog
  url: https://stegra.com/en/news-and-stories
- group: operate
  title: ''
  type: Support
  url: https://stegra.com/en/get-in-touch
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stegra.com/en/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stegraab
- group: build
  title: ''
  type: Packages
  url: packages/stegra-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stegra-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Stegra sells physical green steel, green iron and green hydrogen from its Boden plant under negotiated offtake agreements, and its Next.js site carries no developer, API or portal route at all — /openapi.json and /llms.txt answer 200 with the application's HTML shell because a catch-all route swallows unknown paths, while every /.well-known/ path returns a real 404.
  evidence:
  - status: 200
    url: https://stegra.com/openapi.json
  - status: 404
    url: https://stegra.com/.well-known/api-catalog
  - status: 404
    url: https://stegra.com/.well-known/agent-card.json
  - status: 200
    url: https://stegra.com/en/supplier-info
  reason: not-a-software-company
  state: none
created: '2026-08-29'
description: 'Stegra (formerly H2 Green Steel) is a Stockholm-headquartered industrial company, founded in 2020 and backed by Vargas Holding, building what it describes as Europe''s first large-scale near-zero-emission steel plant in Boden, northern Sweden. The 270-hectare Boden site integrates a giga-scale electrolyzer producing green hydrogen from renewable Nordic electricity, a direct-reduction plant making green iron without coking coal, and a downstream steel mill — a combination Stegra says cuts steelmaking emissions by roughly 95 percent versus the blast-furnace route. Its commercial products are green steel, green iron and green hydrogen, sold to automotive, construction and appliance customers. Stegra is a heavy-industry manufacturer rather than a software vendor: it operates no public developer portal, publishes no API documentation, and serves no machine-readable API contract. Its only public engineering surface is the stegraab GitHub organization, which maintains community Terraform
  providers and a tflint ruleset used for its own internal infrastructure.'
image: https://avatars.githubusercontent.com/u/133014282?v=4
layout: provider
modified: '2026-08-29'
name: Stegra
nav: Providers
network: true
overview: 'Stegra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Steel, Manufacturing, Green Hydrogen, and Energy.


  Stegra''s developer surface includes engineering blog, support, and 6 more developer resources.'
plans:
- name: Stegra Plans Pricing
  plan_count: 0
  slug: stegra-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Stegra Rate Limits
  slug: stegra-rate-limits
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stegra/refs/heads/main/screenshots/stegra-2026-09-02T160834.png
security:
- kind: domain-security
  name: Stegra Domain Security
  slug: stegra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stegra
tags:
- Company
- Steel
- Manufacturing
- Green Hydrogen
- Energy
- Sustainability
- Decarbonization
- Industrial
- Materials
- Sweden
website: https://stegra.com/en
---
