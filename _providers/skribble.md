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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 40
  human_in_the_loop: 0
  name: Skribble Agentic Access
  operation_count: 88
  slug: skribble-agentic-access
  summary_line: 88 operations · 40 acting
api_count: 3
apis:
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for authentication, authorization, and user access management.
  name: Skribble Access API
  slug: skribble-access-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints providing extra metadata or supplementary details for documents.
  name: Skribble Additional Information API
  slug: skribble-additional-information-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for managing account credits, billing information, and payment operations.
  name: Skribble Billing and Credits API
  slug: skribble-billing-and-credits-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for uploading and managing documents.
  name: Skribble Document API
  slug: skribble-document-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for retrieving, checking status, and downloading identification evidence collected during identification.
  name: Skribble Identification API
  slug: skribble-identification-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for monitoring system health.
  name: Skribble Monitoring API
  slug: skribble-monitoring-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for signature activity reporting.
  name: Skribble Report API
  slug: skribble-report-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for generating, retrieving, and managing reports related to document processing.
  name: Skribble Reports API
  slug: skribble-reports-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for applying electronic seals to documents.
  name: Skribble Seal API
  slug: skribble-seal-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for the Send-To signing flow.
  name: Skribble Send To API
  slug: skribble-sendto-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for creating and managing signature requests.
  name: Skribble Signature API
  slug: skribble-signature-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for managing attachments on a signature request.
  name: Skribble Signature Attachment API
  slug: skribble-signature-attachment-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for handling signature requests and callbacks.
  name: Skribble Signature Handling API
  slug: skribble-signature-handling-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for managing observers on a signature request.
  name: Skribble Signature Observer API
  slug: skribble-signature-observer-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for managing signers on a signature request.
  name: Skribble Signature Signer API
  slug: skribble-signature-signer-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints for user information and signature quality queries.
  name: Skribble User API
  slug: skribble-user-api
- baseURL: https://api.skribble.com/v2
  baseurl_source: declared
  description: Endpoints to validate documents, data formats, and signatures.
  name: Skribble Validation API
  slug: skribble-validation-api
artifact_total: 49
common:
- group: agent
  href: https://artifacts.apis.io/skribble/agentic-access/skribble-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/skribble-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/skribble/rate-limits/skribble-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/skribble-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/skribble/plans/skribble-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skribble-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/skribble/rules/skribble-rules.yml
  title: ''
  type: Spectral
  url: rules/skribble-rules.yml
- group: design
  href: https://artifacts.apis.io/skribble/json-ld/skribble-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/skribble-context.jsonld
- group: design
  href: https://artifacts.apis.io/skribble/vocabulary/skribble-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/skribble-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/skribble/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/skribble/data-model/skribble-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skribble-data-model.yml
- group: design
  href: https://artifacts.apis.io/skribble/conventions/skribble-conventions.yml
  title: ''
  type: Conventions
  url: conventions/skribble-conventions.yml
- group: start
  href: https://artifacts.apis.io/skribble/sandbox/skribble-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/skribble-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/skribble/lifecycle/skribble-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/skribble-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/skribble/lifecycle/skribble-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/skribble-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/skribble/errors/skribble-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skribble-problem-types.yml
- group: design
  href: https://artifacts.apis.io/skribble/conformance/skribble-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skribble-conformance.yml
- group: other
  href: https://artifacts.apis.io/skribble/overlays/skribble-sign-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/skribble-sign-v2-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/skribble/llms/skribble-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skribble-llms.txt
- group: auth
  href: https://artifacts.apis.io/skribble/well-known/skribble-skribble-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skribble-skribble-security.txt
- group: auth
  href: https://artifacts.apis.io/skribble/well-known/skribble-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skribble-security.txt
- group: agent
  href: https://artifacts.apis.io/skribble/well-known/skribble-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skribble-well-known.yml
- group: other
  href: https://artifacts.apis.io/skribble/hosts/skribble-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skribble-hosts.yml
- group: build
  href: https://artifacts.apis.io/skribble/integrations/skribble-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/skribble-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/skribble/vendors/skribble-vendors.yml
  title: ''
  type: Vendors
  url: vendors/skribble-vendors.yml
- group: build
  href: https://artifacts.apis.io/skribble/packages/skribble-packages.yml
  title: ''
  type: SDKs
  url: packages/skribble-packages.yml
- group: build
  href: https://artifacts.apis.io/skribble/packages/skribble-packages.yml
  title: ''
  type: Packages
  url: packages/skribble-packages.yml
- group: auth
  href: https://artifacts.apis.io/skribble/authentication/skribble-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skribble-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.skribble.com/en-eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.docs.skribble.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.docs.skribble.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api.docs.skribble.com/api/sign-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://api.docs.skribble.com/sign-api-quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skribble.com/business-admin/
- group: operate
  title: ''
  type: Support
  url: https://help.skribble.com/de
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skribble.com/
- group: company
  title: ''
  type: Blog
  url: https://www.skribble.com/en-eu/blog/category/all/page/1/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skribble.com/en-eu/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://my.skribble.com/business/signup/?lang=en
- group: start
  title: ''
  type: Login
  url: https://my.skribble.com/login/
- group: auth
  title: ''
  type: Security
  url: https://www.skribble.com/en-eu/security/
- group: other
  title: ''
  type: Leadership
  url: https://www.skribble.com/en-eu/team/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skribble.com/en-eu/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skribble.com/en-eu/privacy/
- group: auth
  href: https://artifacts.apis.io/skribble/security/skribble-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/skribble-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/skribble/security/skribble-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skribble-domain-security.yml
created: '2026-10-18'
description: Skribble (Skribble AG) is a Swiss electronic signature provider offering simple (SES/EES), advanced (AES/FES) and qualified (QES) electronic signatures that are legally valid under Swiss ZertES and EU eIDAS law, hosted in Switzerland and GDPR-compliant. Beyond its web app, Skribble publishes a developer portal at api.docs.skribble.com documenting the Sign API v2 (stable), Sign API v3 (preview, with draft workflows and multi-document requests) and the Validation API v1 for verifying signed PDFs and certificates.
image: https://images.prismic.io/covebe/aUkWynNYClf9okDs_ThumbnailHomeEN.webp?auto=format,compress&rect=0,0,2400,1260&w=1200&h=630
json_schemas:
- name: BillingCreditInfos
  property_count: 2
  slug: skribble-billing-credit-infos
- name: BillingCreditUsage
  property_count: 4
  slug: skribble-billing-credit-usage
- name: Create Signature Request
  property_count: 0
  slug: skribble-create-signature-request
- name: Document Response
  property_count: 14
  slug: skribble-document-response
- name: DocumentValidationResponse
  property_count: 10
  slug: skribble-document-validation-response
- name: Identification Evidence Status Response
  property_count: 11
  slug: skribble-identification-evidence-status-response
- name: LoginRequest
  property_count: 2
  slug: skribble-login-request
- name: SignatureRecipient
  property_count: 0
  slug: skribble-signature-recipient
- name: Signature Report
  property_count: 3
  slug: skribble-signature-report
- name: SignatureResponse
  property_count: 27
  slug: skribble-signature-response
- name: SignatureResponse_v3
  property_count: 29
  slug: skribble-signature-response-v3
- name: SignatureValidationResponse
  property_count: 8
  slug: skribble-signature-validation-response
- name: Update Signature Request
  property_count: 15
  slug: skribble-update-signature-request
- name: ValidationInfosResponse
  property_count: 3
  slug: skribble-validation-infos-response
jsonld:
- class_count: 63
  name: Skribble Context
  property_count: 156
  slug: skribble-context
layout: provider
modified: '2026-10-18'
name: Skribble
nav: Providers
network: true
overview: 'Skribble publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access API, Additional Information API, Billing and Credits API, and 14 more. Tagged areas include Company, E-Signature, Digital Signature, Qualified Electronic Signature, and Signature Validation.


  The Skribble catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Skribble''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 36 more developer resources.'
plans:
- name: Skribble Plans Pricing
  plan_count: 4
  slug: skribble-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Skribble Rate Limits
  slug: skribble-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Skribble API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: skribble-rules
scopes:
- name: Skribble Scopes
  scope_count: 0
  slug: skribble-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 67.4
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 65.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: eidas
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Skribble Authentication
  slug: skribble-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Skribble Domain Security
  slug: skribble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skribble Vulnerability Disclosure
  slug: skribble-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 9
skills:
- name: skribble-add-and-manage-signature-attachments
  slug: skribble-add-and-manage-signature-attachments
- name: skribble-create-and-manage-signature-request
  slug: skribble-create-and-manage-signature-request
- name: skribble-create-and-track-a-signature-request
  slug: skribble-create-and-track-a-signature-request
- name: skribble-draft-and-initiate-a-multi-document-request
  slug: skribble-draft-and-initiate-a-multi-document-request
- name: skribble-manage-signature-signer
  slug: skribble-manage-signature-signer
- name: skribble-seal-a-document
  slug: skribble-seal-a-document
- name: skribble-send-to-request-workflow
  slug: skribble-send-to-request-workflow
- name: skribble-upload-and-retrieve-document
  slug: skribble-upload-and-retrieve-document
- name: skribble-validate-a-signed-pdf
  slug: skribble-validate-a-signed-pdf
slug: skribble
tags:
- Company
- E-Signature
- Digital Signature
- Qualified Electronic Signature
- Signature Validation
- eIDAS
- Switzerland
website: https://www.skribble.com/en-eu/
---
