---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-08-11'
api_count: 9
apis:
- description: 'Public register of the federally regulated financial institutions OSFI supervises, including every federally regulated insurer with its Authorized Insurance Classes, FI industry group, trade name and '
  name: OSFI Who We Regulate Register
  slug: osfi-who-we-regulate-register
- description: Publicly disclosable regulatory returns filed by federally regulated life insurance companies — LCA/LCQ (LICAT capital), LF1 Life Core Financial Statement Return, LF2 Life Supervisory Quarterly Return
  name: OSFI Life Insurance Companies Financial Data
  slug: osfi-life-insurance-financial-data
- description: Publicly disclosable regulatory returns filed by federally regulated property and casualty insurers and mortgage insurers — PC1 P&C Core Financial Statement Return, PC2/PC3 supervisory returns, PC4 Mi
  name: OSFI Property and Casualty Companies Financial Data
  slug: osfi-property-casualty-financial-data
- description: 'Publicly disclosable regulatory returns filed by federally regulated fraternal benefit societies — the LICAT (LCA/LCQ) and LF1/LF2/LF3 life-return series applied to Canada''s mutual-aid insurers, plus '
  name: OSFI Fraternal Benefit Societies Financial Data
  slug: osfi-fraternal-benefit-societies-financial-data
- description: 'Publicly disclosable regulatory returns filed by federally regulated banks — M4 Consolidated Balance Sheet, BA BASEL III Capital Adequacy Reporting (BCAR), E3 Return of Allowances for Expected Credit '
  name: OSFI Banks Financial Data
  slug: osfi-banks-financial-data
- description: 'Publicly disclosable regulatory returns filed by foreign bank branches operating in Canada — M4 Consolidated Balance Sheet, E3 Return of Allowances for Expected Credit Losses, K3 Supplementary Return '
  name: OSFI Foreign Bank Branches Financial Data
  slug: osfi-foreign-bank-branches-financial-data
- description: Publicly disclosable regulatory returns filed by federally regulated trust companies — M4 Consolidated Balance Sheet, BA BASEL III Capital Adequacy Reporting (BCAR), E3 Return of Allowances for Expect
  name: OSFI Trust Companies Financial Data
  slug: osfi-trust-companies-financial-data
- description: Publicly disclosable regulatory returns filed by federally regulated loan companies — M4 Consolidated Balance Sheet, BA BASEL III Capital Adequacy Reporting (BCAR), E3 Return of Allowances for Expecte
  name: OSFI Loan Companies Financial Data
  slug: osfi-loan-companies-financial-data
- description: Publicly disclosable regulatory returns filed by federally regulated cooperative retail associations — M4 Consolidated Balance Sheet, BA BASEL III Capital Adequacy Reporting (BCAR), E3 Return of Allow
  name: OSFI Retail Associations Financial Data
  slug: osfi-retail-associations-financial-data
artifact_total: 33
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/osfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.osfi-bsif.gc.ca/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.osfi-bsif.gc.ca/en/data-forms
- group: docs
  title: ''
  type: Documentation
  url: https://www.osfi-bsif.gc.ca/en/guidance/guidance-library
- group: docs
  title: ''
  type: Documentation
  url: https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/financial-reporting-instructions
- group: docs
  title: ''
  type: Documentation
  url: https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns
- group: docs
  title: ''
  type: Documentation
  url: https://www.osfi-bsif.gc.ca/en/about-osfi/progress-our-initiatives/modernizing-we-collect-data-institutions
- group: start
  title: ''
  type: Portal
  url: https://connect-connexion.bank-banque-canada.ca/igw/apps/ami/portal/login
- group: other
  title: ''
  type: OpenData
  url: https://search.open.canada.ca/opendata/?owner_org=osfi-bsif
- group: company
  title: ''
  type: News
  url: https://www.osfi-bsif.gc.ca/en/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/office-of-the-superintendent-of-financial-institutions-of-canada
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OSFICanada
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/OSFIBSIF
- group: start
  title: ''
  type: GettingStarted
  url: https://www.osfi-bsif.gc.ca/en/data-forms/open-government-osfi-financial-data/working-open-government-data
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ckan.org/en/2.10/api/index.html
- group: operate
  title: ''
  type: Support
  url: https://www.osfi-bsif.gc.ca/en/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.osfi-bsif.gc.ca/en/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.osfi-bsif.gc.ca/en/transparency/access-information-privacy
- group: commercial
  title: ''
  type: License
  url: https://open.canada.ca/en/open-government-licence-canada
- group: operate
  title: ''
  type: Roadmap
  url: https://www.osfi-bsif.gc.ca/en/about-osfi/progress-our-initiatives/modernizing-we-collect-data-institutions
- group: other
  title: ''
  type: Glossary
  url: https://www.osfi-bsif.gc.ca/en/data-forms/reporting-returns/filing-financial-returns/glossary-terms
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/osfi-vocabulary.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/osfi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/osfi-problem-types.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/osfi-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/osfi-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/osfi-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/osfi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/osfi-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/osfi-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/osfi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/osfi-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/osfi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/osfi-plans-pricing.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-banks.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-foreign-bank-branches.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-fraternal-benefit-societies.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-life-insurance.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-loan-companies.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-property-casualty.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-retail-associations.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-trust-companies.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/osfi-who-we-regulate.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osfi-financial-return-datapoint-monthly.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osfi-financial-return-datapoint.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osfi-who-we-regulate-financial-institutions.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/osfi-who-we-regulate-private-pension-plans.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-datastore-search-banks-bcar-example.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-datastore-search-life-lf1-example.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-datastore-search-not-found-example.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-datastore-search-pc1-example.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-datastore-search-who-we-regulate-example.json
- group: build
  title: ''
  type: Examples
  url: examples/osfi-package-search-example.json
created: '2026-07-25'
description: The Office of the Superintendent of Financial Institutions (OSFI / BSIF) is Canada's federal prudential regulator, supervising more than 400 federally regulated financial institutions and over 1,200 private pension plans. On the insurance side OSFI supervises federally regulated life insurance companies, property and casualty insurers, mortgage insurers and fraternal benefit societies for solvency and capital adequacy — issuing the LICAT, MCT and BAAT capital guidelines and collecting the LF1/LF2/LF3, PC1-PC4 and MI1-MI5 regulatory returns. It does NOT regulate market conduct; that sits with the provinces (FSRA in Ontario, AMF in Quebec), and Canada has no open-insurance mandate — Consumer-Driven Banking excludes insurance entirely. OSFI publishes no first-party developer portal and no OpenAPI — developer.osfi-bsif.gc.ca, api.osfi-bsif.gc.ca and docs.osfi-bsif.gc.ca do not resolve, and /developers, /api and /developer all return 404. Its real machine-readable surface is its
  insurance and banking regulatory data (FINDAT) plus the "Who we regulate" register, published as datastore-active datasets on Canada's Open Government portal and readable anonymously through the CKAN 3 Action API (datastore_search; the SQL passthrough datastore_search_sql is disabled on the portal) — OSFI ships a step-by-step API usage guide PDF with each dataset. The filing side (the Regulatory Reporting System) is institution-gated behind a Bank of Canada Connect login. Everything else is a documentation-and-rulebook corpus of 313 guidance-library pages and 142 financial reporting instruction pages.
examples:
- key_count: 5
  name: Osfi Datastore Search Banks Bcar Example
  slug: osfi-datastore-search-banks-bcar-example
- key_count: 5
  name: Osfi Datastore Search Life Lf1 Example
  slug: osfi-datastore-search-life-lf1-example
- key_count: 5
  name: Osfi Datastore Search Not Found Example
  slug: osfi-datastore-search-not-found-example
- key_count: 5
  name: Osfi Datastore Search Pc1 Example
  slug: osfi-datastore-search-pc1-example
- key_count: 5
  name: Osfi Datastore Search Who We Regulate Example
  slug: osfi-datastore-search-who-we-regulate-example
- key_count: 5
  name: Osfi Package Search Example
  slug: osfi-package-search-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: OSFI FINDAT regulatory-return data point (calendar-month return series)
  property_count: 16
  slug: osfi-financial-return-datapoint-monthly
- name: OSFI FINDAT regulatory-return data point (fiscal-quarter return series)
  property_count: 17
  slug: osfi-financial-return-datapoint
- name: OSFI Who We Regulate — federally regulated financial institution record
  property_count: 14
  slug: osfi-who-we-regulate-financial-institutions
- name: OSFI Who We Regulate — federally regulated private pension plan record
  property_count: 8
  slug: osfi-who-we-regulate-private-pension-plans
jsonld:
- class_count: 0
  name: Osfi Banks Context
  property_count: 0
  slug: osfi-banks
- class_count: 0
  name: Osfi Foreign Bank Branches Context
  property_count: 0
  slug: osfi-foreign-bank-branches
- class_count: 0
  name: Osfi Fraternal Benefit Societies Context
  property_count: 0
  slug: osfi-fraternal-benefit-societies
- class_count: 0
  name: Osfi Life Insurance Context
  property_count: 0
  slug: osfi-life-insurance
- class_count: 0
  name: Osfi Loan Companies Context
  property_count: 0
  slug: osfi-loan-companies
- class_count: 0
  name: Osfi Property Casualty Context
  property_count: 0
  slug: osfi-property-casualty
- class_count: 0
  name: Osfi Retail Associations Context
  property_count: 0
  slug: osfi-retail-associations
- class_count: 0
  name: Osfi Trust Companies Context
  property_count: 0
  slug: osfi-trust-companies
- class_count: 0
  name: Osfi Who We Regulate Context
  property_count: 0
  slug: osfi-who-we-regulate
layout: provider
mcp_servers:
- description: ''
  name: osfi-mcp.yml
  slug: osfi-mcpyml
modified: '2026-07-25'
name: OSFI
nav: Providers
network: true
overview: 'OSFI publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Regulator, Life Insurance, and Property and Casualty.


  The OSFI catalog on APIs.io includes 9 JSON-LD contexts.


  OSFI''s developer surface includes documentation, developer portal, product news, YouTube channel, getting-started guide, API reference, support, and 47 more developer resources.'
plans:
- name: Osfi Plans Pricing
  plan_count: 1
  slug: osfi-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 3
  name: Osfi Rate Limits
  slug: osfi-rate-limits
score:
  band: developing
  composite: 42.2
  delta: -0.9
  facets:
    commercial_clarity: 42.1
    contract_quality: 24.2
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 22.9
    operational_transparency: 52.6
  previous_composite: 43.1
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/osfi/refs/heads/main/screenshots/osfi-2026-08-07T191000.png
security:
- kind: authentication
  name: Osfi Authentication
  slug: osfi-authentication
  summary_line: none/portal-login · 2 schemes
- kind: domain-security
  name: Osfi Domain Security
  slug: osfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: osfi
tags:
- Insurance
- Canada
- Regulator
- Life Insurance
- Property and Casualty
- Financial Regulation
- Prudential Supervision
- Open Data
- Risk Data
- Market Infrastructure
- Banking
- Basel III
- Capital Adequacy
- Regulatory Reporting
- Pensions
website: https://www.osfi-bsif.gc.ca/en
---
