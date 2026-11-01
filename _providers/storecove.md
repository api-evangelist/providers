---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Storecove Agentic Access
  operation_count: 40
  slug: storecove-agentic-access
  summary_line: 40 operations · 27 acting
api_count: 3
apis:
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The AdditionalTaxIdentifiers API from Storecove — 2 operation(s) for additionaltaxidentifiers.
  name: Storecove Additional Tax Identifiers API
  slug: storecove-additionaltaxidentifiers-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The Administrations API from Storecove — 2 operation(s) for administrations.
  name: Storecove Administrations API
  slug: storecove-administrations-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The C5Activation API from Storecove — 8 operation(s) for c5activation.
  name: Storecove C5Activation API
  slug: storecove-c5activation-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The Discovery API from Storecove — 3 operation(s) for discovery.
  name: Storecove Discovery API
  slug: storecove-discovery-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The InvoiceSubmissions API from Storecove — 3 operation(s) for invoicesubmissions.
  name: Storecove Invoice Submissions API
  slug: storecove-invoicesubmissions-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The LegalEntities API from Storecove — 2 operation(s) for legalentities.
  name: Storecove Legal Entities API
  slug: storecove-legalentities-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The PeppolIdentifiers API from Storecove — 2 operation(s) for peppolidentifiers.
  name: Storecove Peppol Identifiers API
  slug: storecove-peppolidentifiers-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The PurchaseInvoices API from Storecove — 3 operation(s) for purchaseinvoices.
  name: Storecove Purchase Invoices API
  slug: storecove-purchaseinvoices-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The ReceivedDocuments API from Storecove — 3 operation(s) for receiveddocuments.
  name: Storecove Received Documents API
  slug: storecove-receiveddocuments-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The WebhookInstances API from Storecove — 2 operation(s) for webhookinstances.
  name: Storecove Webhook Instances API
  slug: storecove-webhookinstances-api
- baseURL: https://api.storecove.com/api/v2
  baseurl_source: declared
  description: The document submissions API from Storecove — 3 operation(s) for document submissions.
  name: Storecove document submissions API
  slug: storecove-document-submissions-api
artifact_total: 31
common:
- group: agent
  href: https://artifacts.apis.io/storecove/agentic-access/storecove-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/storecove-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/storecove/rules/storecove-rules.yml
  title: ''
  type: Spectral
  url: rules/storecove-rules.yml
- group: design
  href: https://artifacts.apis.io/storecove/json-ld/storecove-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/storecove-context.jsonld
- group: design
  href: https://artifacts.apis.io/storecove/vocabulary/storecove-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/storecove-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/storecove/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/storecove/data-model/storecove-data-model.yml
  title: ''
  type: DataModel
  url: data-model/storecove-data-model.yml
- group: operate
  href: https://artifacts.apis.io/storecove/changelog/storecove-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/storecove-changelog.yml
- group: design
  href: https://artifacts.apis.io/storecove/conventions/storecove-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/storecove-conventions.yml
- group: design
  href: https://artifacts.apis.io/storecove/conventions/storecove-conventions.yml
  title: ''
  type: Conventions
  url: conventions/storecove-conventions.yml
- group: start
  href: https://artifacts.apis.io/storecove/sandbox/storecove-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/storecove-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/storecove/lifecycle/storecove-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/storecove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/storecove/lifecycle/storecove-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/storecove-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/storecove/errors/storecove-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/storecove-problem-types.yml
- group: design
  href: https://artifacts.apis.io/storecove/conformance/storecove-conformance.yml
  title: ''
  type: Conformance
  url: conformance/storecove-conformance.yml
- group: other
  href: https://artifacts.apis.io/storecove/overlays/storecove-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/storecove-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/storecove/llms/storecove-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/storecove-llms.txt
- group: auth
  href: https://artifacts.apis.io/storecove/well-known/storecove-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storecove-ws-security.txt
- group: auth
  href: https://artifacts.apis.io/storecove/well-known/storecove-webservices-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storecove-webservices-security.txt
- group: auth
  href: https://artifacts.apis.io/storecove/well-known/storecove-storecove-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storecove-storecove-security.txt
- group: auth
  href: https://artifacts.apis.io/storecove/well-known/storecove-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storecove-help-security.txt
- group: auth
  href: https://artifacts.apis.io/storecove/well-known/storecove-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/storecove-api-security.txt
- group: agent
  href: https://artifacts.apis.io/storecove/well-known/storecove-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/storecove-well-known.yml
- group: other
  href: https://artifacts.apis.io/storecove/hosts/storecove-hosts.yml
  title: ''
  type: Hosts
  url: hosts/storecove-hosts.yml
- group: build
  href: https://artifacts.apis.io/storecove/integrations/storecove-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/storecove-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/storecove/vendors/storecove-vendors.yml
  title: ''
  type: Vendors
  url: vendors/storecove-vendors.yml
- group: build
  href: https://artifacts.apis.io/storecove/packages/storecove-packages.yml
  title: ''
  type: SDKs
  url: packages/storecove-packages.yml
- group: build
  href: https://artifacts.apis.io/storecove/packages/storecove-packages.yml
  title: ''
  type: Packages
  url: packages/storecove-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/downloads/
- group: auth
  href: https://artifacts.apis.io/storecove/authentication/storecove-authentication.yml
  title: ''
  type: Authentication
  url: authentication/storecove-authentication.yml
- group: auth
  href: https://artifacts.apis.io/storecove/security/storecove-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/storecove-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.storecove.com/us/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.storecove.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.storecove.com/us/en/start-now
- group: operate
  title: ''
  type: Support
  url: https://help.storecove.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.storecove.com/blog/en/
- group: start
  title: ''
  type: Login
  url: https://app.storecove.com/users/sign_in
- group: operate
  title: ''
  type: Contact
  url: https://www.storecove.com/us/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storecove.com/fileadmin/editors-filemount/documents/Data_Privacy_Policy_Storecove_final_website.pdf
- group: auth
  title: ''
  type: Security
  url: https://www.storecove.com/fileadmin/editors-filemount/documents/Security_Principals_2023.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://storecove.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/storecove/
created: '2026-10-18'
description: Storecove provides e-invoicing software and a global compliance API. A single API connection gives businesses and ERP providers access to the Peppol network and to other e-invoicing networks such as DBNAlliance (USA), FACeB2B and Finvoice, along with e-invoicing and reporting compliance in markets including Belgium, France, Germany, India, Italy, Malaysia, Poland, Singapore and the UAE. Storecove handles invoice compliance, format conversion and delivery, and offers a free 30-day test account.
image: https://www.storecove.com/typo3temp/assets/_processed_/3/a/csm_logo-storecove_af3bf9d4b5.webp
json_schemas:
- name: Document submission
  property_count: 9
  slug: storecove-document-submission
- name: Invoice submission
  property_count: 13
  slug: storecove-invoice-submission
- name: LegalEntityCreate
  property_count: 19
  slug: storecove-legal-entity-create
- name: LegalEntityUpdate
  property_count: 22
  slug: storecove-legal-entity-update
- name: PurchaseInvoice
  property_count: 41
  slug: storecove-purchase-invoice
- name: PurchaseInvoiceUbl
  property_count: 7
  slug: storecove-purchase-invoice-ubl
jsonld:
- class_count: 120
  name: Storecove Context
  property_count: 391
  slug: storecove-context
layout: provider
modified: '2026-10-18'
name: Storecove
nav: Providers
network: true
overview: 'Storecove publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Additional Tax Identifiers API, Administrations API, C5Activation API, and 8 more. Tagged areas include Company, E-Invoicing, PEPPOL, Tax Compliance, and Invoicing.


  The Storecove catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Storecove''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, support, engineering blog, and 34 more developer resources.'
plans:
- name: Storecove Plans Pricing
  plan_count: 0
  slug: storecove-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Storecove Rate Limits
  slug: storecove-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Storecove API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: storecove-rules
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 65.1
    developer_ergonomics: 61.3
    discoverability: 71.4
    operational_transparency: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Storecove Authentication
  slug: storecove-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Storecove Domain Security
  slug: storecove-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 7
skills:
- name: storecove-create-and-manage-legal-entity
  slug: storecove-create-and-manage-legal-entity
- name: storecove-manage-administration
  slug: storecove-manage-administration
- name: onboard-legal-entity
  slug: storecove-onboard-legal-entity
- name: storecove-receive-and-retrieve-document
  slug: storecove-receive-and-retrieve-document
- name: receive-documents
  slug: storecove-receive-documents
- name: send-document
  slug: storecove-send-document
- name: storecove-submit-document-and-retrieve-evidence
  slug: storecove-submit-document-and-retrieve-evidence
slug: storecove
tags:
- Company
- E-Invoicing
- PEPPOL
- Tax Compliance
- Invoicing
- Accounting
- ERP Integration
- Fintech
website: https://www.storecove.com/us/en/
---
