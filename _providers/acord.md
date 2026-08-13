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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-12'
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
- description: Claims inquiry, submission, and management
  name: ACORD Claims API
  slug: acord-claims-api
- description: Insured party and contact management
  name: ACORD Party API
  slug: acord-party-api
- description: Policy administration and management
  name: ACORD Policy API
  slug: acord-policy-api
- description: Underwriting and risk assessment
  name: ACORD Underwriting API
  slug: acord-underwriting-api
artifact_total: 80
collections:
- collection_type: open
  name: ACORD Next-Generation Digital Standards (NGDS) API
  slug: open-acord-ngds
common:
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
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/openapi/acord-ngds-openapi.yml
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist/acord
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/rules/acord-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/acord/refs/heads/main/vocabulary/acord-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.acord.org/ACORD-about/acord-news
description: ACORD is a global standards-setting body for the insurance industry, providing data standards, reference architecture, and digital tools that enable insurers, brokers, and software providers to exchange information.
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
modified: '2026-04-19'
name: ACORD
nav: Providers
network: true
overview: 'ACORD publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Claims API, Party API, Policy API, and 1 more. Tagged areas include Claims, Insurance, Policy, Standards, and Underwriting.


  The ACORD catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  ACORD''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 13 more developer resources.'
plans:
- name: Acord Plans Pricing
  plan_count: 1
  slug: acord-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 0
  name: Acord Rate Limits
  slug: acord-rate-limits
rules:
- name: ACORD API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: acord-jsonschema-spectral-rules
- name: ACORD API Rules
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
  band: developing
  composite: 47.8
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 76.1
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 51.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
- Insurance
- Policy
- Standards
- Underwriting
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
