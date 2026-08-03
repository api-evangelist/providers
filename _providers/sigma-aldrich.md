---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sigma Aldrich Agentic Access
  operation_count: 6
  slug: sigma-aldrich-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 6
apis:
- description: The Sigma-Aldrich Chemical Structure Search API enables substructure, exact structure, and similarity searches against the Sigma-Aldrich chemical catalog using SMILES, InChI, or molecular formula nota
  name: Sigma-Aldrich Chemical Structure Search API
  slug: sigma-aldrich-structure-search-api
- description: The Safety Data Sheet (SDS) API provides programmatic access to GHS- compliant Safety Data Sheets for all Sigma-Aldrich chemical products. Enables EHS systems, LIMS platforms, and safety management so
  name: Sigma-Aldrich Safety Data Sheet API
  slug: sigma-aldrich-sds-api
- description: Real-time pricing and global stock availability for Sigma-Aldrich products.
  name: Sigma-Aldrich Pricing and Availability API
  slug: sigma-aldrich-pricing-and-availability-api
- description: Product catalog search and retrieval for research chemicals, biochemicals, and laboratory supplies.
  name: Sigma-Aldrich Products API
  slug: sigma-aldrich-products-api
- description: Retrieval of GHS-compliant Safety Data Sheets for regulatory compliance and laboratory safety management.
  name: Sigma-Aldrich Safety Data Sheets API
  slug: sigma-aldrich-safety-data-sheets-api
- description: Chemical structure search using SMILES, InChI, or molecular formula notation for cheminformatics workflows.
  name: Sigma-Aldrich Structures API
  slug: sigma-aldrich-structures-api
artifact_total: 19
collections:
- collection_type: open
  name: Sigma-Aldrich Product Search API
  slug: open-sigma-aldrich-product
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sigma-aldrich-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigma-aldrich-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sigma-aldrich-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sigma-aldrich
- group: company
  title: ''
  type: Website
  url: https://www.sigmaaldrich.com/
- group: other
  title: ''
  type: ProductCatalog
  url: https://www.sigmaaldrich.com/US/en/catalog
- group: start
  title: ''
  type: SDS Portal
  url: https://www.sigmaaldrich.com/US/en/support/sds-portal
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sigmaaldrich.com/US/en/technical-documents/technical-article/chemistry/labware/sigma-aldrich-developer-portal
- group: other
  title: ''
  type: Parent Company
  url: https://www.merckgroup.com/
created: '2025-01-01'
description: Sigma-Aldrich was a leading life science and high technology company whose biochemical and organic chemical products, kits, and services are used in scientific research, including genomics, proteomics, and drug discovery. Acquired by Merck KGaA in 2015, Sigma-Aldrich now operates as part of MilliporeSigma in North America and Merck in other regions, continuing to provide the world's largest catalog of research chemicals, biochemicals, laboratory equipment, and life science products to researchers globally.
examples:
- key_count: 2
  name: Sigma Aldrich Search Products Example
  slug: sigma-aldrich-search-products-example
finops:
- name: Sigma Aldrich Finops
  service_category: Life Science Procurement
  slug: sigma-aldrich-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sigma-aldrich.png
json_schemas:
- name: SigmaAldrichProduct
  property_count: 15
  slug: sigma-aldrich-product
json_structures:
- name: Sigma Aldrich Product Structure
  property_count: 0
  slug: sigma-aldrich-product-structure
jsonld:
- class_count: 15
  name: Sigma Aldrich Context
  property_count: 8
  slug: sigma-aldrich-context
layout: provider
modified: '2026-05-19'
name: Sigma-Aldrich
nav: Providers
network: true
overview: 'Sigma-Aldrich publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pricing and Availability API, Products API, Safety Data Sheets API, and 1 more. Tagged areas include Life Science, Chemistry, Biochemistry, Laboratory, and Research.


  The Sigma-Aldrich catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sigma-Aldrich''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Sigma Aldrich Plans Pricing
  plan_count: 1
  slug: sigma-aldrich-plans-pricing
press:
- date: '2026-05-25'
  title: Sigma-Aldrich Stockholders Approve Acquisition By Merck ...
  url: https://www.prnewswire.com/news-releases/sigma-aldrich-stockholders-approve-acquisition-by-merck-kgaa-300005544.html
- date: '2026-05-25'
  title: 'AIDDISON™: Using AI-Powered Software to Accelerate ...'
  url: https://www.sigmaaldrich.com/deepweb/assets/sigmaaldrich/marketing/global/documents/337/293/aiddison-wp11667en-ms.pdf?srsltid=AfmBOorzcyht-cJN5uA5Ja97HzfX965AcgyqtWRQLv_cgMtvNL4LfhrA
- date: '2026-05-25'
  title: Fast-Tracking Drug Discovery with an AI Boost
  url: https://www.sigmaaldrich.com/US/en/life-science/about-us/stories/drug-discovery-with-an-ai-boost?srsltid=AfmBOoqP93uCOX0sPhIuG8A6P1Vn8EtwfjrTbuqoD8ssLGK4nCo2hQwU
- date: '2026-05-25'
  title: MilliporeSigma Launches First Ever AI Solution to Integrate ...
  url: https://www.sigmaaldrich.com/US/en/collections/press/first-ever-ai-solution-to-integrate-drug-discovery-and-synthesis?srsltid=AfmBOorXdiiwAD3PAloTM009VNX8lrmFD2gsiFCy6Fww9dZyfr6Za1OH
- date: '2026-05-25'
  title: Sigma-Aldrich® and The Scripps Research Institute ...
  url: https://www.fiercebiotech.com/research/sigma-aldrich%C2%AE-and-scripps-research-institute-partner-to-accelerate-commercialization-of
random_paper: 66
rate_limits:
- limit_count: 1
  name: Sigma Aldrich Rate Limits
  slug: sigma-aldrich-rate-limits
rules:
- name: Sigma-Aldrich API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sigma-aldrich-jsonschema-spectral-rules
- name: Sigma-Aldrich API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: sigma-aldrich-rules
score:
  band: developing
  composite: 44.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 76.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sigma-aldrich/refs/heads/main/screenshots/sigma-aldrich-2026-06-20T193909.png
security:
- kind: authentication
  name: Sigma Aldrich Authentication
  slug: sigma-aldrich-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sigma Aldrich Domain Security
  slug: sigma-aldrich-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sigma-aldrich
tags:
- Life Science
- Chemistry
- Biochemistry
- Laboratory
- Research
- Chemical Catalog
website: https://www.sigmaaldrich.com/
---
