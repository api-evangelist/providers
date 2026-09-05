---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 8
apis:
- description: API for programmatic access to Microsoft Access databases through various interfaces including ODBC, OLE DB, and DAO.
  name: Microsoft Access Database Engine API
  slug: microsoft-access-database-engine-api
- description: API for accessing Microsoft Access databases stored in SharePoint or OneDrive through Microsoft Graph.
  name: Microsoft Graph API (for Access Online)
  slug: microsoft-graph-api-for-access-online
- description: 'The Access Visual Basic for Applications (VBA) object model provides programmatic access to all Access objects, properties, methods, and events for developing custom solutions and automating database '
  name: Microsoft Access VBA API
  slug: microsoft-access-vba-api
- description: 'Data Access Objects (DAO) provide a programmatic interface to create, query, and modify the structure and data of Access databases, with objects like Database, Recordset, TableDef, QueryDef, and more '
  name: Microsoft Data Access Objects (DAO) API
  slug: microsoft-data-access-objects-dao-api
- description: ActiveX Data Objects (ADO) enable client applications to access and manipulate data from Access databases through OLE DB providers, supporting features for building client/server and web-based applica
  name: Microsoft ActiveX Data Objects (ADO) API
  slug: microsoft-activex-data-objects-ado-api
- description: The Microsoft Access SQL reference provides documentation for the Access SQL dialect, including data definition language (DDL) for creating and modifying database structures and data manipulation lang
  name: Microsoft Access SQL API
  slug: microsoft-access-sql-api
- description: The Access macro actions interface provides a set of programmable actions for automating database tasks including data operations, form management, navigation, filtering, and system commands without w
  name: Microsoft Access Macro Actions API
  slug: microsoft-access-macro-actions-api
- description: Power Automate for desktop provides built-in actions for automating Microsoft Access databases, including launching Access instances, reading tables, running stored queries, executing macros, and clos
  name: Power Automate Access Actions API
  slug: power-automate-access-actions-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-access-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-access-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-access-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://www.microsoft.com/en-us/microsoft-365
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/access
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/access/compare-microsoft-access-plans-and-pricing
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/access-blog/bg-p/AccessBlog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/office/client-developer/access/access-home
- group: docs
  title: ''
  type: Desktop Database Reference
  url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/
- group: other
  title: ''
  type: Access Database Engine Download
  url: https://www.microsoft.com/en-us/download/details.aspx?id=54920
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: design
  title: ''
  type: JSONLD
  url: json-ld/microsoft-access-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-access-database-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-access-table-schema.json
created: '2024'
description: Microsoft Access is a database management system from Microsoft that combines the relational Microsoft Jet Database Engine with a graphical user interface and software development tools.
finops:
- name: Microsoft Access Finops
  service_category: API
  slug: microsoft-access-finops
image: https://www.microsoft.com/en-us/microsoft-365/access
json_schemas:
- name: Microsoft Access Database
  property_count: 14
  slug: microsoft-access-database
- name: Microsoft Access TableDef
  property_count: 14
  slug: microsoft-access-table
jsonld:
- class_count: 0
  name: Microsoft Access Context
  property_count: 9
  slug: microsoft-access-context
layout: provider
modified: '2026-04-28'
name: Microsoft Access
nav: Providers
network: true
overview: 'Microsoft Access publishes 1 API on the [APIs.io](https://apis.io/) network: Database Engine API. Tagged areas include Access Database, Database, Desktop Database, Microsoft, and Relational Database.


  The Microsoft Access catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Access'' developer surface includes developer portal, support, pricing, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Microsoft Access Plans Pricing
  plan_count: 3
  slug: microsoft-access-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Microsoft Access Rate Limits
  slug: microsoft-access-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Microsoft Access API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-access-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 42.3
    catalog_earned_first_party: 0.0
    catalog_gap: 72.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 33.3
    developer_ergonomics: 45.2
    discoverability: 53.7
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 35.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-access/refs/heads/main/screenshots/microsoft-access-2026-06-20T185353.png
security:
- kind: domain-security
  name: Microsoft Access Domain Security
  slug: microsoft-access-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Access Vulnerability Disclosure
  slug: microsoft-access-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Access Trust Center
  slug: microsoft-access-trust-center
  summary_line: GDPR
slug: microsoft-access
tags:
- Access Database
- Database
- Desktop Database
- Microsoft
- Relational Database
website: https://www.microsoft.com/en-us/microsoft-365
---
