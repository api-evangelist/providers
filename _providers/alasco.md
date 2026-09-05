---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 70
  human_in_the_loop: 0
  name: Alasco Agentic Access
  operation_count: 178
  slug: alasco-agentic-access
  summary_line: 178 operations · 70 acting
api_count: 3
apis:
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: '**Annual Consumption** is the system-computed consumption per meter and calendar year, including emission factors and tenant allocations. The figures are derived from readings rather than written dire'
  name: Alasco Annual Consumption API
  slug: alasco-annual-consumption-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: 'An **Asset** is a property you manage capital expenditure for, mirrored from your Alasco asset register. Assets are read-only through this API: capital work on an asset is organised into **Measures**,'
  name: Alasco Asset API
  slug: alasco-asset-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: 'The **Audit Log** is a read-only account-level trail of changes. A raw audit feed reports table-level inserts, updates and deletes, and a user audit feed reports user- and API-triggered changes; both '
  name: Alasco Audit Log API
  slug: alasco-audit-log-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Budget Shift** is a record of budget moved between **Contract Units** in a **Project** (or added from reserve), with a type, amount and reason. Budget shifts are read-only through this API.
  name: Alasco Budget Shift API
  slug: alasco-budget-shift-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Building** is a property in your Alasco asset register and the anchor for ESG data - its **Utility Meters**, **Tenants** and **Documents** all attach to it. Buildings are read-only here, identifie
  name: Alasco Buildings API
  slug: alasco-buildings-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view of actual cash outflows (paid invoices) allocated per **Cost Element**.
  name: Alasco Cash Outflow Cost Element View API
  slug: alasco-cash-outflow-cost-element-view-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Change Order** is a formal amendment to a **Contract** - a cost or scope change - carrying claimed, audited and approved amounts and an approval state. Change orders are read-only through this API
  name: Alasco Change Order API
  slug: alasco-change-order-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Change Order Document** is a file attached to a **Change Order** (for example the amendment offer or supporting evidence). You can upload and download them; a document left unlinked is removed aut
  name: Alasco Change Order Document API
  slug: alasco-change-order-document-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Consumption Interval** is a consumption total for a period (start to end date) for a meter. Intervals are created individually or in bulk - all-or-nothing (`/bulk/`) or per-item (`/bulk-partial/`)
  name: Alasco Consumption Intervals API
  slug: alasco-consumption-intervals-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Contact** is a person or organisation used in invoicing and correspondence, with name, address and contact details. Contacts can be created and updated through the API.
  name: Alasco Contact API
  slug: alasco-contact-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: 'A **Contract** is an agreement with a **Contractor** to deliver work, tracking the committed amount and reserve. In CapEx a contract belongs to a **Measure**; it accumulates **Invoices** and **Change '
  name: Alasco Contract API
  slug: alasco-contract-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Contract Document** is a file (such as the signed contract or its terms) attached to a **Contract**. You can upload and download them; a document left unlinked from a contract is removed automatic
  name: Alasco Contract Document API
  slug: alasco-contract-document-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view with one row per **Contract**, summarising its amount, invoiced, approved, paid and outstanding figures.
  name: Alasco Contract Financials API
  slug: alasco-contract-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Contract Unit** is a budget package within a **Project** (the FinCon counterpart of a CapEx Measure), carrying an initial budget and a lifecycle **state**. **Contracts** are assigned to a contract
  name: Alasco Contract Unit API
  slug: alasco-contract-unit-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view with one row per **Contract Unit**, summarising its budget against the spend of the contracts assigned to it.
  name: Alasco Contract Unit Financials API
  slug: alasco-contract-unit-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Contracting Entity** is the legal entity on your side that commissions contracts, holding company and commercial-register details. Names are unique per account, and entities can be created and upd
  name: Alasco Contracting Entity API
  slug: alasco-contracting-entity-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Contractor** is a supplier engaged to carry out contracted work, holding master data such as its identifier, VAT ID and bank details. A contractor can hold many **Contracts**, its tax-waiver docum
  name: Alasco Contractor API
  slug: alasco-contractor-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Cost Element** is a node in a hierarchical cost structure (a cost group) belonging to a **Cost Element Tree Template**. Cost elements classify a project's budget and costs and can be created and u
  name: Alasco Cost Element API
  slug: alasco-cost-element-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view breaking down each **Contract**'s costs across the **Cost Elements** they are allocated to.
  name: Alasco Cost Element Contract Financials API
  slug: alasco-cost-element-contract-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view breaking down **Contract Unit** budget and spend across **Cost Elements**.
  name: Alasco Cost Element Contract Unit Financials API
  slug: alasco-cost-element-contract-unit-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view of budget and cost aggregated per **Cost Element** within a project.
  name: Alasco Cost Element Financials API
  slug: alasco-cost-element-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Cost Element Tree Template** is a reusable hierarchy of **Cost Elements** that defines a project's cost structure. A template can back many **Projects**, can be created and updated through the API
  name: Alasco Cost Element Tree Template API
  slug: alasco-cost-element-tree-template-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Custom Field** holds your account's user-defined values on a **Contract** (the fields themselves are configured in Alasco). It is read-only here and retrieved per contract (`GET /contracts/{contra
  name: Alasco Custom Field API
  slug: alasco-custom-field-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Custom Field Definition** describes a custom field - its name, type and which object it applies to (contract or project). Definitions are configured in Alasco and are read-only through this API.
  name: Alasco Custom Field Definition API
  slug: alasco-custom-field-definition-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Document** is a file attached to one or more **Buildings** (certificates, leases and similar). Documents can be uploaded, downloaded, given an external id, have their metadata read and updated, an
  name: Alasco Documents API
  slug: alasco-documents-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: An **Invoice** is a contractor's request for payment that moves through states from `NEW` to `PAID`. Submitting an invoice against an **Asset** creates it in `NEW`, linked only to the asset's project;
  name: Alasco Invoice API
  slug: alasco-invoice-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: An **Invoice Document** is a file attached to an **Invoice**, such as the invoice PDF or supporting evidence. At least one document is required before an invoice can be checked; documents can be uploa
  name: Alasco Invoice Document API
  slug: alasco-invoice-document-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: 'An **Invoice Tag** is a coloured label (with a name unique per account) you assign to **Invoices** for organisation and filtering. Tags can be created, updated and deleted, and assigned to or removed '
  name: Alasco Invoice Tag API
  slug: alasco-invoice-tag-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Measure** is a planned package of capital work on an **Asset** (for example a renovation or a fit-out), carrying a status, category and priority. Measures are read-only here and group the **Contra
  name: Alasco Measure API
  slug: alasco-measure-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view for outright (whole-asset) sales, showing total planned revenues against recorded payments.
  name: Alasco Outright Sale API
  slug: alasco-outright-sale-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Project** is the top-level container for a construction or development engagement. It optionally references a **Property** and a **Cost Element Tree Template**, and organises spend through **Contr
  name: Alasco Project API
  slug: alasco-project-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: 'Read-only reporting view with one row per **Project**, summarising budget against cost: current budget, contracted amount, change orders, approved and paid amounts, forecast and budget deviation.'
  name: Alasco Project Financials API
  slug: alasco-project-financials-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Property** is the real-estate asset a **Project** is carried out on, holding its address and location. A project references one property, and the same property can back several projects. Propertie
  name: Alasco Property API
  slug: alasco-property-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view of rental units, showing each unit's rent status and projected totals.
  name: Alasco Rent Unit API
  slug: alasco-rent-unit-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: Read-only reporting view of sales units, showing listed and sold prices.
  name: Alasco Sales Unit API
  slug: alasco-sales-unit-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Tenant Consumption Link** attributes a year's **Annual Consumption** to a **Tenant**. Links are created and deleted through the API by tenant external id and annual-consumption id (both must belon
  name: Alasco Tenant Consumption Links API
  slug: alasco-tenant-consumption-links-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Tenant** is an occupant of a **Building**, identified by your `external_id` and linked to a building by `external_building_id`. Tenants are upserted through the API (created or updated by external
  name: Alasco Tenants API
  slug: alasco-tenants-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: '**Utility Data Batch Info** records the source and label of a batch of imported utility data. Create one and reference it (via `batch_info_uuid`) when writing meters, readings or consumption intervals'
  name: Alasco Utility Data Batch Info API
  slug: alasco-utility-data-batch-info-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Utility Meter Reading** is a timestamped meter value. Readings are written individually or in bulk (upsert), keyed by the meter's external id, and feed the derived consumption figures.
  name: Alasco Utility Meter Readings API
  slug: alasco-utility-meter-readings-api
- baseURL: https://api.alasco.de/fincon/v1
  baseurl_source: declared
  description: A **Utility Meter** measures consumption (electricity, gas, water, heating or cooling) for a **Building**. Meters are created and updated through the API, identified by your `external_id`, and own the
  name: Alasco Utility Meters API
  slug: alasco-utility-meters-api
artifact_total: 87
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CAPEX Annual Consumption API
  slug: open-alasco-annual-consumption-api
- collection_type: open
  name: CAPEX Annual Consumption Asset API
  slug: open-alasco-asset-api
- collection_type: open
  name: CAPEX Annual Consumption Audit Log API
  slug: open-alasco-audit-log-api
- collection_type: open
  name: CAPEX Annual Consumption Budget Shift API
  slug: open-alasco-budget-shift-api
- collection_type: open
  name: CAPEX Annual Consumption Buildings API
  slug: open-alasco-buildings-api
- collection_type: open
  name: CAPEX Annual Consumption Cash Outflow Cost Element View API
  slug: open-alasco-cash-outflow-cost-element-view-api
- collection_type: open
  name: CAPEX Annual Consumption Change Order API
  slug: open-alasco-change-order-api
- collection_type: open
  name: CAPEX Annual Consumption Change Order Document API
  slug: open-alasco-change-order-document-api
- collection_type: open
  name: CAPEX Annual Consumption Consumption Intervals API
  slug: open-alasco-consumption-intervals-api
- collection_type: open
  name: CAPEX Annual Consumption Contact API
  slug: open-alasco-contact-api
- collection_type: open
  name: CAPEX Annual Consumption Contract API
  slug: open-alasco-contract-api
- collection_type: open
  name: CAPEX Annual Consumption Contract Document API
  slug: open-alasco-contract-document-api
- collection_type: open
  name: CAPEX Annual Consumption Contract Financials API
  slug: open-alasco-contract-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Contract Unit API
  slug: open-alasco-contract-unit-api
- collection_type: open
  name: CAPEX Annual Consumption Contract Unit Financials API
  slug: open-alasco-contract-unit-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Contracting Entity API
  slug: open-alasco-contracting-entity-api
- collection_type: open
  name: CAPEX Annual Consumption Contractor API
  slug: open-alasco-contractor-api
- collection_type: open
  name: CAPEX Annual Consumption Cost Element API
  slug: open-alasco-cost-element-api
- collection_type: open
  name: CAPEX Annual Consumption Cost Element Contract Financials API
  slug: open-alasco-cost-element-contract-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Cost Element Contract Unit Financials API
  slug: open-alasco-cost-element-contract-unit-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Cost Element Financials API
  slug: open-alasco-cost-element-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Cost Element Tree Template API
  slug: open-alasco-cost-element-tree-template-api
- collection_type: open
  name: CAPEX Annual Consumption Custom Field API
  slug: open-alasco-custom-field-api
- collection_type: open
  name: CAPEX Annual Consumption Custom Field Definition API
  slug: open-alasco-custom-field-definition-api
- collection_type: open
  name: CAPEX Annual Consumption Documents API
  slug: open-alasco-documents-api
- collection_type: open
  name: CAPEX Annual Consumption Invoice API
  slug: open-alasco-invoice-api
- collection_type: open
  name: CAPEX Annual Consumption Invoice Document API
  slug: open-alasco-invoice-document-api
- collection_type: open
  name: CAPEX Annual Consumption Invoice Tag API
  slug: open-alasco-invoice-tag-api
- collection_type: open
  name: CAPEX Annual Consumption Measure API
  slug: open-alasco-measure-api
- collection_type: open
  name: CAPEX Annual Consumption Outright Sale API
  slug: open-alasco-outright-sale-api
- collection_type: open
  name: CAPEX Annual Consumption Project API
  slug: open-alasco-project-api
- collection_type: open
  name: CAPEX Annual Consumption Project Financials API
  slug: open-alasco-project-financials-api
- collection_type: open
  name: CAPEX Annual Consumption Property API
  slug: open-alasco-property-api
- collection_type: open
  name: CAPEX Annual Consumption Rent Unit API
  slug: open-alasco-rent-unit-api
- collection_type: open
  name: CAPEX Annual Consumption Sales Unit API
  slug: open-alasco-sales-unit-api
- collection_type: open
  name: CAPEX Annual Consumption Tenant Consumption Links API
  slug: open-alasco-tenant-consumption-links-api
- collection_type: open
  name: CAPEX Annual Consumption Tenants API
  slug: open-alasco-tenants-api
- collection_type: open
  name: CAPEX Annual Consumption Utility Data Batch Info API
  slug: open-alasco-utility-data-batch-info-api
- collection_type: open
  name: CAPEX Annual Consumption Utility Meter Readings API
  slug: open-alasco-utility-meter-readings-api
- collection_type: open
  name: CAPEX Annual Consumption Utility Meters API
  slug: open-alasco-utility-meters-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/alasco-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/alasco-capex-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.alasco.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alasco.de/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.alasco.de/getstarted.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.alasco.de/getstarted.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.alasco.de/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.alasco.de/changelog.html
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alasco-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alasco-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alasco-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alasco-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alasco-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alasco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alasco-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alasco-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.alasco.com/security-trust
- group: design
  title: ''
  type: DataModel
  url: data-model/alasco-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/alasco-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alasco-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alasco-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alasco-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.alasco.com/security-trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/alasco-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alasco-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.alasco.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alasco.com/pricing/financial-management
- group: start
  title: ''
  type: SignUp
  url: https://www.alasco.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://login.alasco.de/u/login/identifier
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alasco.com/legal/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alasco.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://support.alasco.de/hc/de
created: '2026-07-17'
description: 'Alasco is a Munich-based real-estate financial management platform for developers, asset managers, and construction teams, replacing spreadsheet-based cost control with integrated workflows across the development lifecycle. It spans three products - FinCon (financial controlling: projects, properties, contracts, invoices, change orders, cost elements, and financial reporting), CapEx (capital-expenditure planning and cost processing across assets and measures), and ESG (environmental data: buildings, utility meters, tenants, and consumption data). Alasco exposes a REST Public API that follows JSON:API principles, plus an official hosted MCP server for AI-agent integrations. It is ISO/IEC 27001 certified and serves institutional real-estate firms including Hines, JLL, and Ardian.'
image: https://cdn.prod.website-files.com/656ef2eb27ad41897248f866/6a50ff4e64f5c6a6cb6d2dd5_Alasco_Logo_Full_Blue%20(1).svg
layout: provider
mcp_servers:
- description: ''
  name: Alasco MCP Server
  slug: alasco-mcp-server
modified: '2026-07-17'
name: Alasco
nav: Providers
network: true
overview: 'Alasco publishes 40 APIs on the [APIs.io](https://apis.io/) network, including Annual Consumption API, Asset API, Audit Log API, and 37 more. Tagged areas include Company, Ai Enterprise Software, Real-Estate, Construction, and PropTech.


  Alasco''s developer surface includes documentation, getting-started guide, API reference, changelog, authentication, engineering blog, pricing, and 26 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 52.6
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alasco/refs/heads/main/screenshots/alasco-2026-07-25T195534.png
security:
- kind: authentication
  name: Alasco Authentication
  slug: alasco-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Alasco Domain Security
  slug: alasco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alasco Vulnerability Disclosure
  slug: alasco-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Alasco Trust Center
  slug: alasco-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: alasco
tags:
- Company
- Ai Enterprise Software
- Real-Estate
- Construction
- PropTech
- Financial Management
- Cost Management
- Capital Expenditure
- ESG
- Sustainability
website: https://www.alasco.com/en/
---
