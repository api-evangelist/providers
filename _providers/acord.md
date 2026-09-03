---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Acord Agentic Access
  operation_count: 10
  slug: acord-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 6
apis:
- description: ACORD XML Standards define data exchange formats for property & casualty, life, annuity, and reinsurance using SOAP/XML protocols. APIs enable claims inquiry, policy administration, and regulatory rep
  name: ACORD XML Standards API
  slug: acord-xml-standards-api
- description: ACORD Global Reinsurance & Large Commercial Data Standards define XML data exchange formats for reinsurance and large commercial lines. APIs support facultative and treaty reinsurance transactions, pl
  name: ACORD Reinsurance & Large Commercial Data Standards API
  slug: acord-reinsurance-standards-api
- baseURL: https://api.insurer-internal.example.com/ngds
  baseurl_source: spec
  description: Claims inquiry, submission, and management
  name: ACORD Claims API
  slug: acord-claims-api
- baseURL: https://api.insurer-internal.example.com/ngds
  baseurl_source: spec
  description: Insured party and contact management
  name: ACORD Party API
  slug: acord-party-api
- baseURL: https://api.insurer-internal.example.com/ngds
  baseurl_source: spec
  description: Policy administration and management
  name: ACORD Policy API
  slug: acord-policy-api
- baseURL: https://api.insurer-internal.example.com/ngds
  baseurl_source: spec
  description: Underwriting and risk assessment
  name: ACORD Underwriting API
  slug: acord-underwriting-api
artifact_total: 85
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) Claims API
  slug: open-acord-claims-api
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) API
  slug: open-acord-ngds
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) Claims Party API
  slug: open-acord-party-api
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) Claims Policy API
  slug: open-acord-policy-api
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) Claims Underwriting API
  slug: open-acord-underwriting-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/acord-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acord-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acord-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acord-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acord-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acord
- group: company
  title: ''
  type: Website
  url: https://www.acord.org
- group: start
  title: ''
  type: Portal
  url: https://www.acord.org/standards-architecture/acord-data-standards
- group: docs
  title: ''
  type: Documentation
  url: https://www.acord.org/standards-architecture/acord-data-standards
- group: start
  title: ''
  type: GettingStarted
  url: https://www.acord.org/standards-architecture/acord-data-standards/next-generation-digital-standards
- group: docs
  title: ''
  type: Documentation
  url: https://www.acord.org/standards-architecture/reference-architecture
- group: operate
  title: ''
  type: Support
  url: https://www.acord.org/standards-architecture/get-involved/standards-project-advisory-groups
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-policy-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-schema/acord-claim-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/json-ld/acord-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/vocabulary/acord-vocabulary.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acord-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/acord-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/acord-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acord-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/acord-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acordsolutions.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acord-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acord-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/acord-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acord-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acord-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acord.org/membership-participation/programs-offerings
- group: start
  title: ''
  type: Login
  url: https://www.acord.org/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acord.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acord.org/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://acord.atlassian.net/servicedesk/customer/portal/35
- group: company
  title: ''
  type: Blog
  url: https://www.acord.org/ACORD-about/acord-news
coverage:
  checked: '2026-08-30'
  detail: Every ACORD standards artifact — the NGDS schemas, Master Object List, Master Resource Definitions and Master Deprecation List — is published only as a /file-download/<uuid> link that 302s an anonymous request into Microsoft Entra member sign-in, and ACORD's own downloads page states you must first join a membership or participation program before an acord.org account will grant access; the one real REST API in the estate, ACORD Solutions Group's ADEPT, releases its specifications to GRLC members and licensed integrators at ASG's discretion.
  evidence:
  - status: 302
    url: https://www.acord.org/file-download/04dcef0d-6222-46a2-911f-5c905db8e086
  - status: 200
    url: https://www.acord.org/standards-architecture/acord-data-standards/standards-downloads
  - status: 404
    url: https://www.acord.org/openapi.json
  - status: 403
    url: https://standards.acord.org/openapi.json
  - status: 404
    url: https://www.acordsolutions.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-04-19'
description: 'ACORD is the global standards-setting body for the insurance industry, publishing the data standards that insurers, reinsurers, brokers, MGAs and software vendors use to exchange policy, claims, party, underwriting, accounting and settlement data: ACORD XML and AL3 for property & casualty, Life & Annuity XML and DTCC EDI, the Global Reinsurance & Large Commercial (GRLC) standards behind EBOT, ECOT, GPM and CRP, and the JSON/YAML Next-Generation Digital Standards (NGDS) aimed at REST APIs and microservices. ACORD operates no public API of its own; standards and schemas are delivered to members under licence, and its commercial subsidiary ACORD Solutions Group runs the ADEPT data exchange platform under separate agreement.'
examples:
- key_count: 18
  name: Acord Claim Example
  slug: acord-claim-example
- key_count: 13
  name: Acord Policy Example
  slug: acord-policy-example
- key_count: 6
  name: Ngds Address Example
  slug: ngds-address-example
- key_count: 2
  name: Ngds Claim List Example
  slug: ngds-claim-list-example
- key_count: 6
  name: Ngds Claim Request Example
  slug: ngds-claim-request-example
- key_count: 2
  name: Ngds Contact Example
  slug: ngds-contact-example
- key_count: 6
  name: Ngds Coverage Example
  slug: ngds-coverage-example
- key_count: 5
  name: Ngds Coverage Request Example
  slug: ngds-coverage-request-example
- key_count: 8
  name: Ngds Party Example
  slug: ngds-party-example
- key_count: 2
  name: Ngds Party List Example
  slug: ngds-party-list-example
- key_count: 7
  name: Ngds Party Request Example
  slug: ngds-party-request-example
- key_count: 2
  name: Ngds Policy List Example
  slug: ngds-policy-list-example
- key_count: 7
  name: Ngds Policy Request Example
  slug: ngds-policy-request-example
- key_count: 4
  name: Ngds Policy Update Example
  slug: ngds-policy-update-example
- key_count: 5
  name: Ngds Underwriting Submission Example
  slug: ngds-underwriting-submission-example
- key_count: 4
  name: Ngds Underwriting Submission Response Example
  slug: ngds-underwriting-submission-response-example
features:
- description: ACORD XML standards for property & casualty, life, annuity, and reinsurance SOAP/XML data exchange.
  name: XML Data Standards
- description: JSON/YAML-based NGDS for RESTful APIs, microservices, and IoT insurance data exchange.
  name: Next-Generation Digital Standards
- description: Global reinsurance and large commercial data standards for facultative and treaty transactions.
  name: Reinsurance Standards
- description: Electronic data standards for life insurance and annuity products covering underwriting and policy management.
  name: Life and Annuity Standards
- description: ACORD reference architecture providing structural frameworks for insurance technology implementations.
  name: Reference Architecture
finops:
- name: Acord Finops
  service_category: Insurance Standards / Data Exchange
  slug: acord-finops
image: /assets/icons/acord.png
integrations:
- description: Integration with policy administration systems (PAS) and claims management systems (CMS).
  name: Insurance Core Systems
- description: Integration with reinsurance management platforms supporting ACORD AL3 and RIBO formats.
  name: Reinsurance Platforms
- description: Modern insurtech API platforms consuming ACORD NGDS JSON standards.
  name: Insurtech Solutions
- description: Integration with state and national insurance regulatory reporting systems.
  name: Regulatory Systems
json_schemas:
- name: ACORD Claim
  property_count: 18
  slug: acord-claim
- name: ACORD Policy
  property_count: 13
  slug: acord-policy
- name: Address
  property_count: 6
  slug: ngds-address
- name: ClaimList
  property_count: 2
  slug: ngds-claim-list
- name: ClaimRequest
  property_count: 6
  slug: ngds-claim-request
- name: Contact
  property_count: 2
  slug: ngds-contact
- name: CoverageRequest
  property_count: 5
  slug: ngds-coverage-request
- name: Coverage
  property_count: 6
  slug: ngds-coverage
- name: PartyList
  property_count: 2
  slug: ngds-party-list
- name: PartyRequest
  property_count: 7
  slug: ngds-party-request
- name: Party
  property_count: 8
  slug: ngds-party
- name: PolicyList
  property_count: 2
  slug: ngds-policy-list
- name: PolicyRequest
  property_count: 7
  slug: ngds-policy-request
- name: PolicyUpdate
  property_count: 4
  slug: ngds-policy-update
- name: UnderwritingSubmissionResponse
  property_count: 4
  slug: ngds-underwriting-submission-response
- name: UnderwritingSubmission
  property_count: 5
  slug: ngds-underwriting-submission
json_structures:
- name: Acord Claim Structure
  property_count: 18
  slug: acord-claim-structure
- name: Acord Policy Structure
  property_count: 13
  slug: acord-policy-structure
- name: Ngds Address Structure
  property_count: 6
  slug: ngds-address-structure
- name: Ngds Claim List Structure
  property_count: 2
  slug: ngds-claim-list-structure
- name: Ngds Claim Request Structure
  property_count: 6
  slug: ngds-claim-request-structure
- name: Ngds Contact Structure
  property_count: 2
  slug: ngds-contact-structure
- name: Ngds Coverage Request Structure
  property_count: 5
  slug: ngds-coverage-request-structure
- name: Ngds Coverage Structure
  property_count: 6
  slug: ngds-coverage-structure
- name: Ngds Party List Structure
  property_count: 2
  slug: ngds-party-list-structure
- name: Ngds Party Request Structure
  property_count: 7
  slug: ngds-party-request-structure
- name: Ngds Party Structure
  property_count: 8
  slug: ngds-party-structure
- name: Ngds Policy List Structure
  property_count: 2
  slug: ngds-policy-list-structure
- name: Ngds Policy Request Structure
  property_count: 7
  slug: ngds-policy-request-structure
- name: Ngds Policy Update Structure
  property_count: 4
  slug: ngds-policy-update-structure
- name: Ngds Underwriting Submission Response Structure
  property_count: 4
  slug: ngds-underwriting-submission-response-structure
- name: Ngds Underwriting Submission Structure
  property_count: 5
  slug: ngds-underwriting-submission-structure
jsonld:
- class_count: 0
  name: Acord Context
  property_count: 5
  slug: acord-context
- class_count: 19
  name: Acord Ngds Context
  property_count: 55
  slug: acord-ngds-context
layout: provider
modified: '2026-08-30'
name: ACORD
nav: Providers
network: true
overview: 'ACORD publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Party API, Policy API, and 1 more. Tagged areas include Claims, Data Standards, Insurance, Policy, and Property Casualty.


  The ACORD catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  ACORD''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, changelog, pricing, and 27 more developer resources.'
plans:
- name: Acord Plans Pricing
  plan_count: 1
  slug: acord-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Acord Rate Limits
  slug: acord-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ACORD API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: acord-jsonschema-spectral-rules
- effective_rule_count: 80
  extends:
  - spectral:oas
  name: ACORD API Rules
  rule_count: 39
  severity_counts:
    error: 13
    hint: 0
    info: 3
    warn: 23
  slug: acord-spectral-rules
scopes:
- name: Acord Scopes
  scope_count: 4
  slug: acord-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 26
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 75.0
    commercial_clarity: 75.0
    contract_governance: 28.8
    contract_quality: 28.6
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 56.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/screenshots/acord-2026-08-17T121359.png
security:
- kind: authentication
  name: Acord Authentication
  slug: acord-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Acord Domain Security
  slug: acord-domain-security
  summary_line: TLSv1.3 · DMARC
slug: acord
tags:
- Claims
- Data Standards
- Insurance
- Policy
- Property Casualty
- Reinsurance
- Standards
- Underwriting
- XML
use_cases:
- description: Standardized ACORD XML or NGDS JSON claims transaction exchange between carriers, adjusters, and reinsurers.
  name: Claims Data Exchange
- description: Automated policy issuance, endorsement, and renewal using ACORD NGDS microservices architecture.
  name: Policy Administration
- description: Straight-through processing of insurance applications using ACORD standardized data elements.
  name: Underwriting Automation
- description: Facultative and treaty reinsurance data exchange using ACORD Global Reinsurance Data Standards.
  name: Reinsurance Settlement
- description: Compliance reporting using ACORD-standardized data formats for regulatory submissions.
  name: Regulatory Reporting
website: https://www.acord.org
---
