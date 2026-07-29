---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 25
  name: Altruistiq Agentic Access
  operation_count: 44
  slug: altruistiq-agentic-access
  summary_line: 44 operations · 29 acting · 25 human-in-the-loop
api_count: 9
apis:
- description: '### Altruistiq’s datasource API enables you to: - Create new datasources - Manage existing datasources (read, update) - Upload data to a datasource A datasource is the place where you will share a sin'
  name: Altruistiq Datasource API
  slug: altruistiq-datasource-api
- description: '### Altruistiq’s Export API enables you to: - Export corporate data Exporting data is a key part of the Altruistiq platform. It allows you to take your data and use it in other systems, or to share it'
  name: Altruistiq Export API
  slug: altruistiq-export-api
- description: 'Altruistiq''s Facility API enables you to: - Create new facilities in bulk - Update existing facility persistent properties - Update facility version - Create new facility version - Delete facility ver'
  name: Altruistiq Facility API
  slug: altruistiq-facility-api
- description: 'Altruistiq''s Location API enables you to: - Get a list of countries with their alpha_2 codes and names - Get country subdivisions for a specific country by its alpha-2 code'
  name: Altruistiq Location API
  slug: altruistiq-location-api
- description: 'Altruistiq''s Organization API enables you to: - Get organization details and business units The organization API provides access to organizational structure data including the root organization and it'
  name: Altruistiq Organization API
  slug: altruistiq-organization-api
- description: '### Altruistiq’s Product API enables you to: - Create new products - Update existing products - Delete products - Get a list of products - All the above in bulk'
  name: Altruistiq Product API
  slug: altruistiq-product-api
- description: '### Altruistiq’s Product Structure API enables you to: - Create new product structures - Update existing product structures - Delete product structures - Get a list of all product structures - All the'
  name: Altruistiq Product structure API
  slug: altruistiq-product-structure-api
- description: '### Altruistiq’s Product Structure API enables you to: - Create new product structure inputs - Update existing product structure inputs - Delete product structure inputs - Get a list of all product st'
  name: Altruistiq Product structure inputs API
  slug: altruistiq-product-structure-inputs-api
- description: 'The Altruistiq API uses TLS and follows the OAuth 2.0 Client credentials flow as per [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4) ### Generating `client_id` and `client_secret'
  name: Altruistiq Security API
  slug: altruistiq-security-api
artifact_total: 47
collections:
- collection_type: open
  name: Altruistiq Datasource API
  slug: open-altruistiq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/altruistiq-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/altruistiq-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altruistiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/altruistiq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/altruistiq-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.altruistiq.com
- group: start
  title: ''
  type: Portal
  url: https://www.altruistiq.com/platform/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.altruistiq.com
- group: other
  title: ''
  type: Platform
  url: https://app.altruistiq.com
- group: start
  title: ''
  type: Signup
  url: https://www.altruistiq.com/get-in-touch
- group: other
  title: ''
  type: Company
  url: https://www.altruistiq.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.altruistiq.com/careers
- group: company
  title: ''
  type: Blog
  url: https://www.altruistiq.com/insights
- group: other
  title: ''
  type: Customers
  url: https://www.altruistiq.com/customers
- group: other
  title: ''
  type: Capabilities
  url: https://www.altruistiq.com/data-capabilities
- group: auth
  title: ''
  type: Security
  url: https://www.altruistiq.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.altruistiq.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.altruistiq.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.altruistiq.com/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/altruistiq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/altruistiq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/altruistiq
- group: other
  title: ''
  type: Standards
  url: https://www.carbon-transparency.org
- group: other
  title: ''
  type: Standards
  url: https://www.iso.org/standard/66453.html
- group: other
  title: ''
  type: Standards
  url: https://ghgprotocol.org
- group: other
  title: ''
  type: Standards
  url: https://sciencebasedtargets.org
- group: other
  title: ''
  type: Standards
  url: https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/company-reporting-and-auditing/company-reporting/corporate-sustainability-reporting_en
- group: commercial
  title: ''
  type: Plans
  url: plans/altruistiq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/altruistiq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/altruistiq-finops.yml
created: '2026-05-25'
description: Altruistiq is a London-based climate intelligence platform for food and beverage and other FMCG enterprises managing complex supply chains. The platform unifies corporate carbon footprint reporting, product carbon footprint (PCF) calculation, and supplier engagement on a single ISO 14064-1 assured calculation engine, drawing raw operational data from finance, procurement, and supply chain systems to produce activity-based Scope 1, 2, and 3 emissions measurements. Altruistiq exposes a public Datasource API and a PACT-conformant Product Carbon Footprint data exchange API (OAuth 2.0 client credentials) for uploading activity data, managing products, bills of materials, facilities, and exporting calculated emissions. Customers include Starbucks, Kraft Heinz, Huel, Nando's, Octopus Energy, and other FMCG and food and beverage brands.
examples:
- key_count: 3
  name: Altruistiq Create Export Example
  slug: altruistiq-create-export-example
- key_count: 3
  name: Altruistiq Create Product Example
  slug: altruistiq-create-product-example
- key_count: 3
  name: Altruistiq Get Export Example
  slug: altruistiq-get-export-example
- key_count: 3
  name: Altruistiq Oauth Token Example
  slug: altruistiq-oauth-token-example
features:
- Unified platform for corporate carbon footprint, product carbon footprint, and supplier decarbonisation programs
- ISO 14064-1 assured calculation engine across Scope 1, 2, and 3 emissions
- Public Datasource API for multipart upload of activity data into named datasources
- Public PACT API for PACT/Pathfinder-conformant Product Carbon Footprint data exchange
- OAuth 2.0 Client Credentials authentication against /api/public/v1/oauth2/token
- Corporate emissions Export API with filterable downloads and a documented 40-plus field data dictionary
- Bulk and single-record CRUD for Products, Product Structures (BOMs), and Product Structure Inputs
- Facility management with versioning (versioned facility records, persistent properties, facility types)
- Location reference endpoints for ISO countries and country subdivisions
- Organization endpoint exposing business units for multi-entity reporting
- 220,000+ curated emissions factors database for food and beverage, refreshed quarterly
- Ingredient-level Product Carbon Footprint calculation at scale
- Evie AI agent for climate data automation, analysis, and advisory
- Spreadsheet-style analytics workspace for modelling and dashboarding
- Supplier engagement and primary data collection workflows for Scope 3 accuracy
- Designed for CSRD, SBTi/CDP, eco-design, on-pack claims, and B2B PCF reporting use cases
- SOC 2 and ISO 27001 certified
- Customers include Starbucks, Kraft Heinz, Huel, Nando's, Urban Outfitters, Octopus Energy
finops:
- name: Altruistiq Finops
  service_category: Sustainability and ESG
  slug: altruistiq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/altruistiq.png
json_schemas:
- name: Altruistiq Emission Record
  property_count: 13
  slug: altruistiq-emission-record
- name: Altruistiq Facility
  property_count: 8
  slug: altruistiq-facility
- name: Altruistiq Product
  property_count: 9
  slug: altruistiq-product
json_structures:
- name: Altruistiq Product Structure
  property_count: 0
  slug: altruistiq-product-structure
jsonld:
- class_count: 0
  name: Altruistiq Context
  property_count: 14
  slug: altruistiq-context
layout: provider
modified: '2026-05-25'
name: Altruistiq
nav: Providers
network: true
overview: 'Altruistiq publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Datasource API, Export API, Facility API, and 6 more. Tagged areas include Sustainability, Climate, Carbon Accounting, Emissions, and Greenhouse Gas.


  The Altruistiq catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Altruistiq''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, and 25 more developer resources.'
plans:
- name: Altruistiq Plans Pricing
  plan_count: 4
  slug: altruistiq-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 0
  name: Altruistiq Rate Limits
  slug: altruistiq-rate-limits
rules:
- name: Altruistiq API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: altruistiq-jsonschema-spectral-rules
- name: Altruistiq API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: altruistiq-rules
scopes:
- name: Altruistiq Scopes
  scope_count: 0
  slug: altruistiq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.4
  delta: -4.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 75.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 15.8
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altruistiq/refs/heads/main/screenshots/altruistiq-2026-06-20T171616.png
security:
- kind: authentication
  name: Altruistiq Authentication
  slug: altruistiq-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Altruistiq Domain Security
  slug: altruistiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Altruistiq Trust Center
  slug: altruistiq-trust-center
  summary_line: SOC 2, ISO 27001
slug: altruistiq
tags:
- Sustainability
- Climate
- Carbon Accounting
- Emissions
- Greenhouse Gas
- Scope 3
- Product Carbon Footprint
- Corporate Carbon Footprint
- Supply Chain
- FMCG
- Food and Beverage
- ESG
- CSRD
- SBTi
- PACT
- Sustainability Intelligence
website: https://www.altruistiq.com
---
