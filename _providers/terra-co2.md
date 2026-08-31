---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/terra-co2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://terraco2.com/
- group: company
  title: ''
  type: About
  url: https://terraco2.com/about/
- group: operate
  title: ''
  type: Support
  url: https://terraco2.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terraco2.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terraco2.com/terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/terra-co2-technology
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/terra-co2_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/terra-co2-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Terra CO2 Technology manufactures and sells a physical product - OPUS SCM and OPUS ZERO cement replacements shipped by the ton into concrete plants - so there is no software product to expose; terraco2.com is a WordPress marketing site with no developer portal, no api/developer/docs subdomain resolving in DNS, and no published OpenAPI, GraphQL, MCP or agent card.
  evidence:
  - status: 404
    url: https://terraco2.com/openapi.json
  - status: 404
    url: https://terraco2.com/.well-known/agent-card.json
  - status: 200
    url: https://terraco2.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Terra CO2 Technology is a Golden, Colorado climate-technology and building-materials manufacturer that produces low-carbon replacements for Portland cement. Its commercial product, OPUS SCM, is a supplementary cementitious material that replaces up to 50% of the Portland cement in a concrete mix as a drop-in substitute for legacy SCMs such as fly ash, cutting CO2 by roughly 70% and NOx by roughly 90% per ton replaced, and it is produced from abundant silicate feedstocks rather than coal-plant by-products. A second product, OPUS ZERO, targets a full zero-carbon cement replacement and is in concrete trials. The company runs a pilot and materials R&D facility in Golden and is building a 240,000-ton-per-year commercial plant in Cleburne, Texas, backed by more than $250M raised from climate and construction investors including Cemex Ventures. Terra CO2 sells physical material into the construction supply chain; it publishes no developer program, no public API, and no machine-readable
  API contract.
image: https://terraco2.com/wp-content/uploads/2026/05/logo-header.svg
layout: provider
modified: '2026-08-30'
name: Terra CO2
nav: Providers
network: true
overview: 'Terra CO2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Building Materials, Construction, Cement, and Concrete.


  Terra CO2''s developer surface includes support and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
security:
- kind: domain-security
  name: Terra Co2 Domain Security
  slug: terra-co2-domain-security
  summary_line: TLSv1.3 · DMARC
slug: terra-co2
tags:
- Company
- Building Materials
- Construction
- Cement
- Concrete
- Climate Tech
- Carbon Reduction
- Sustainability
- Manufacturing
- Materials Science
website: https://terraco2.com/
---
