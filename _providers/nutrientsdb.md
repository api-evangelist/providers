---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nutrientsdb Agentic Access
  operation_count: 1
  slug: nutrientsdb-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The Foods API from NutrientsDB — 1 operation(s) for foods.
  name: NutrientsDB Foods API
  slug: nutrientsdb-foods-api
arazzos:
- description: 'Two-step flow over the free, keyless NutrientsDB Sample API: search the public 1,000-food sample by name fragment, then re-fetch the chosen record by its stable public_id. Both steps use the single pu'
  name: Resolve a food name to a NutrientsDB record and read its nutrient profile
  slug: nutrientsdb-search-then-lookup
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NutrientsDB Sample Foods API
  slug: open-nutrientsdb-foods-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nutrientsdb-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nutrientsdb-sample-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nutrientsdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutrientsdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nutrientsdb-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nutrientsdb-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nutrientsdb-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nutrientsdb-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nutrientsdb-nutrient-schema.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nutrientsdb-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.nutrientsdb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.nutrientsdb.com/api/docs
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/57076285/2sBY4TqJ5d
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/colinearstudio
- group: company
  title: ''
  type: Blog
  url: https://www.nutrientsdb.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.nutrientsdb.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nutrientsdb.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nutrientsdb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nutrientsdb.com/privacy
created: '2026-08-02'
description: A curated global food-composition dataset of roughly 2.9 million food entries across 86 normalized nutrient fields, deduplicated across 180+ countries and sold under a one-time license as a downloadable file for local use rather than as a hosted, metered API. Every nutrient value is expressed per 100 g of food, with the unit encoded as a suffix on the field name, and a null value means the source did not report that nutrient rather than that the value is zero. NutrientsDB fronts the licensed dataset with a free, keyless, read-only Sample API that exposes a public 1,000-food slice carrying the identical 86-field schema, so developers, researchers, and AI builders can inspect the shape and density of the data before licensing it. The same sample is mirrored as plain JSON on GitHub and Hugging Face.
examples:
- key_count: 2
  name: Nutrientsdb Error Missing Params
  slug: nutrientsdb-error-missing-params
- key_count: 2
  name: Nutrientsdb Error Not Found
  slug: nutrientsdb-error-not-found
- key_count: 2
  name: Nutrientsdb Error Short Q
  slug: nutrientsdb-error-short-q
- key_count: 2
  name: Nutrientsdb Lookup
  slug: nutrientsdb-lookup
- key_count: 6
  name: Nutrientsdb Search
  slug: nutrientsdb-search
image: https://nutrientsdb.com/og-image.png
json_schemas:
- name: NutrientsDB Food
  property_count: 3
  slug: nutrientsdb-food
layout: provider
mcp_servers:
- description: ''
  name: nutrientsdb-mcp.yml
  slug: nutrientsdb-mcpyml
modified: '2026-08-09'
name: NutrientsDB
nav: Providers
network: true
overview: 'NutrientsDB publishes 1 API on the [APIs.io](https://apis.io/) network: Foods API. Tagged areas include nutrition, food, nutrients, food-composition, and data.


  NutrientsDB''s developer surface includes authentication, documentation, API reference, engineering blog, support, pricing, and 14 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 34.7
  delta: -6.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 60.1
    developer_ergonomics: 35.1
    discoverability: 70.4
    governance: 31.8
    operational_transparency: 2.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Nutrientsdb Authentication
  slug: nutrientsdb-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nutrientsdb Domain Security
  slug: nutrientsdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nutrientsdb
tags:
- nutrition
- food
- nutrients
- food-composition
- data
- search
- sample-data
- dataset
- ai-builders
- reference-data
- open-data
- keyless-api
---
