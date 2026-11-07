---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 45
  human_in_the_loop: 1
  name: Idenfy Agentic Access
  operation_count: 73
  slug: idenfy-agentic-access
  summary_line: 73 operations · 45 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: AI risk scoring, proxy/VPN/Tor detection, phone validation, SMS phone verification, fraud probability estimation, address verification and AI proof of address, plus configurable risk assessment profil
  name: iDenfy Fraud Prevention and Risk API
  slug: idenfy-fraud-api
- description: 'A hosted, unauthenticated remote Model Context Protocol server over the whole public documentation site, including the seven OpenAPI specs. Three live tools: documentation search, a read-only virtual '
  name: iDenfy Documentation MCP Server
  slug: idenfy-docs-mcp
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Age estimation session endpoints.
  name: iDenfy Age Estimation API
  slug: idenfy-age-estimation-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Anti-money laundering check endpoints.
  name: iDenfy AML Checks API
  slug: idenfy-aml-checks-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Anti-money laundering monitoring endpoints.
  name: iDenfy AML Monitorings API
  slug: idenfy-aml-monitorings-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Bank verification endpoints.
  name: iDenfy Bank API
  slug: idenfy-bank-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Bank card verification endpoints.
  name: iDenfy Bank Card Verification API
  slug: idenfy-bank-card-verification-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Beneficiaries CRUD endpoints for the KYB form.
  name: iDenfy Beneficiaries API
  slug: idenfy-beneficiaries-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for actions with companies.
  name: iDenfy Companies API
  slug: idenfy-companies-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Face authentication session endpoints.
  name: iDenfy Face Auth Sessions API
  slug: idenfy-face-auth-sessions-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for actions with GOV ordered documents.
  name: iDenfy GOV Orders API
  slug: idenfy-gov-orders-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: KYB documents CRUD endpoints for the KYB form.
  name: iDenfy KYB Documents API
  slug: idenfy-kyb-documents-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for KYB form actions.
  name: iDenfy KYB Forms API
  slug: idenfy-kyb-forms-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: KYB questionnaires endpoints.
  name: iDenfy KYB Questionnaires API
  slug: idenfy-kyb-questionnaires-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: KYB token endpoints to begin KYB flow.
  name: iDenfy KYB Token API
  slug: idenfy-kyb-token-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for managing face, document-face and document-info blocklist entries.
  name: iDenfy KYC Blocklist API
  slug: idenfy-kyc-blocklist-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for creating KYC verification session tokens.
  name: iDenfy KYC Token API
  slug: idenfy-kyc-token-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for actions with KYC verifications.
  name: iDenfy KYC Verifications API
  slug: idenfy-kyc-verifications-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for standalone proof of address (POA) checks.
  name: iDenfy POA API
  slug: idenfy-poa-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Registry center check endpoints.
  name: iDenfy Registry Center Checks API
  slug: idenfy-registry-center-checks-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Endpoints for actions with SOS filing documents.
  name: iDenfy SOS Reports API
  slug: idenfy-sos-reports-api
- baseURL: https://ivs.idenfy.com
  baseurl_source: declared
  description: Webhooks.
  name: iDenfy Webhooks API
  slug: idenfy-webhooks-api
artifact_total: 100
asyncapis:
- description: ''
  name: Idenfy Webhooks
  slug: idenfy-webhooks
common:
- group: auth
  title: ''
  type: Security
  url: https://idenfy.com/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/idenfy/rules/idenfy-rules.yml
  title: ''
  type: Spectral
  url: rules/idenfy-rules.yml
- group: design
  href: https://artifacts.apis.io/idenfy/json-ld/idenfy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/idenfy-context.jsonld
- group: design
  href: https://artifacts.apis.io/idenfy/vocabulary/idenfy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/idenfy-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/idenfy/security/idenfy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/idenfy-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/idenfy/lifecycle/idenfy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/idenfy-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/idenfy/llms/idenfy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idenfy-llms.txt
- group: other
  href: https://artifacts.apis.io/idenfy/hosts/idenfy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idenfy-hosts.yml
- group: build
  href: https://artifacts.apis.io/idenfy/integrations/idenfy-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/idenfy-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/idenfy/vendors/idenfy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idenfy-vendors.yml
- group: other
  href: https://artifacts.apis.io/idenfy/capabilities/idenfy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/idenfy-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-kyc-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-kyc-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-kyb-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-kyb-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-aml-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-aml-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-bank-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-bank-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-bank-card-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-bank-card-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-face-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-face-authentication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/idenfy/overlays/idenfy-age-estimation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/idenfy-age-estimation-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.idenfy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.idenfy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.idenfy.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.idenfy.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.idenfy.com/quickstart
- group: auth
  href: https://artifacts.apis.io/idenfy/authentication/idenfy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/idenfy-authentication.yml
- group: design
  href: https://artifacts.apis.io/idenfy/conventions/idenfy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/idenfy-conventions.yml
- group: design
  href: https://artifacts.apis.io/idenfy/data-model/idenfy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/idenfy-data-model.yml
- group: design
  href: https://artifacts.apis.io/idenfy/errors/idenfy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/idenfy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/idenfy/lifecycle/idenfy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/idenfy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.idenfy.com/
- group: operate
  href: https://artifacts.apis.io/idenfy/changelog/idenfy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/idenfy-changelog.yml
- group: design
  href: https://artifacts.apis.io/idenfy/conformance/idenfy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/idenfy-conformance.yml
- group: auth
  href: https://artifacts.apis.io/idenfy/security/idenfy-trust-center.yml
  title: ''
  type: Compliance
  url: security/idenfy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/idenfy/security/idenfy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/idenfy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/idenfy/security/idenfy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idenfy-domain-security.yml
- group: design
  href: https://artifacts.apis.io/idenfy/asyncapi/idenfy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/idenfy-webhooks.yml
- group: start
  href: https://artifacts.apis.io/idenfy/sandbox/idenfy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/idenfy-sandbox.yml
- group: design
  href: https://artifacts.apis.io/idenfy/components/idenfy-components.yml
  title: ''
  type: Components
  url: components/idenfy-components.yml
- group: build
  href: https://artifacts.apis.io/idenfy/packages/idenfy-packages.yml
  title: ''
  type: Packages
  url: packages/idenfy-packages.yml
- group: build
  href: https://artifacts.apis.io/idenfy/packages/idenfy-packages.yml
  title: ''
  type: SDKs
  url: packages/idenfy-packages.yml
- group: commercial
  href: https://artifacts.apis.io/idenfy/plans/idenfy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/idenfy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/idenfy/rate-limits/idenfy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/idenfy-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/idenfy/a2a/idenfy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/idenfy-a2a.yml
- group: agent
  href: https://artifacts.apis.io/idenfy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/idenfy/well-known/idenfy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/idenfy-well-known.yml
- group: agent
  href: https://artifacts.apis.io/idenfy/agentic-access/idenfy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/idenfy-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/idenfy/finops/idenfy-finops.yml
  title: ''
  type: FinOps
  url: finops/idenfy-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://idenfy.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/idenfy/llms/idenfy-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idenfy-docs-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://idenfy.com/pricing-plans-v4/
- group: start
  title: ''
  type: SignUp
  url: https://idenfy.com/pricing-plans-v4/
- group: start
  title: ''
  type: Login
  url: https://admin.idenfy.com
- group: operate
  title: ''
  type: Support
  url: https://idenfy-ivs.atlassian.net/servicedesk/customer/portal/1
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.idenfy.com/contact/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/idenfy-developers/idenfy-public-api/collection/gwjcqp9/idenfy-api-requests
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/idenfy
- group: company
  title: ''
  type: Blog
  url: https://idenfy.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/idenfy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://idenfy.com/privacy-policy/
created: '2024-11-13'
description: iDenfy is an identity verification platform providing KYC, KYB, and AML compliance solutions. The iDenfy API enables businesses to verify identities, check for fraud, and comply with regulatory requirements through automated document verification, facial recognition, AML screening, business verification, and bank verification services.
finops:
- has_sources: true
  method: derived
  name: Idenfy Finops
  primary_unit: subscription
  service_category: ''
  slug: idenfy-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idenfy.png
json_schemas:
- name: AgeEstimationTokenRequest
  property_count: 12
  slug: idenfy-age-estimation-token-request
- name: AgeEstimationToken
  property_count: 11
  slug: idenfy-age-estimation-token
- name: AmlCheckPdfRequest
  property_count: 1
  slug: idenfy-aml-check-pdf-request
- name: AmlCheckProfileDetail
  property_count: 0
  slug: idenfy-aml-check-profile-detail
- name: AmlCheckRequest
  property_count: 0
  slug: idenfy-aml-check-request
- name: AmlCheck
  property_count: 0
  slug: idenfy-aml-check
- name: AmlMonitoringPdfRequest
  property_count: 1
  slug: idenfy-aml-monitoring-pdf-request
- name: AmlMonitoringRequest
  property_count: 3
  slug: idenfy-aml-monitoring-request
- name: AmlMonitoring
  property_count: 7
  slug: idenfy-aml-monitoring
- name: AmlMonitoringStartStopRequest
  property_count: 1
  slug: idenfy-aml-monitoring-start-stop-request
- name: BankCardTokenRequest
  property_count: 8
  slug: idenfy-bank-card-token-request
- name: BankCardToken
  property_count: 5
  slug: idenfy-bank-card-token
- name: BankTokenRequest
  property_count: 4
  slug: idenfy-bank-token-request
- name: BankToken
  property_count: 6
  slug: idenfy-bank-token
- name: BeneficiaryCreateRequest
  property_count: 7
  slug: idenfy-beneficiary-create-request
- name: BeneficiaryCreate
  property_count: 8
  slug: idenfy-beneficiary-create
- name: BeneficiaryRequest
  property_count: 6
  slug: idenfy-beneficiary-request
- name: Beneficiary
  property_count: 8
  slug: idenfy-beneficiary
- name: CompanyDetail
  property_count: 18
  slug: idenfy-company-detail
- name: CompanyStatusRequest
  property_count: 0
  slug: idenfy-company-status-request
- name: CompanyStatus
  property_count: 0
  slug: idenfy-company-status
- name: FacialAuthenticationSession
  property_count: 7
  slug: idenfy-facial-authentication-session
- name: GovPartnerOrderDocumentRequest
  property_count: 5
  slug: idenfy-gov-partner-order-document-request
- name: GovPartnerOrderedDocument
  property_count: 9
  slug: idenfy-gov-partner-ordered-document
- name: GovRegistersAvailableDocuments
  property_count: 1
  slug: idenfy-gov-registers-available-documents
- name: IdentificationBlacklistEntry
  property_count: 0
  slug: idenfy-identification-blacklist-entry
- name: IdentificationBlacklistRequest
  property_count: 1
  slug: idenfy-identification-blacklist-request
- name: IdentificationRequestInformationRequest
  property_count: 6
  slug: idenfy-identification-request-information-request
- name: IdentificationRequestInformation
  property_count: 2
  slug: idenfy-identification-request-information
- name: KybAnswersDisplay
  property_count: 4
  slug: idenfy-kyb-answers-display
- name: KybFormAnswersRequest
  property_count: 1
  slug: idenfy-kyb-form-answers-request
- name: KybFormAnswers
  property_count: 1
  slug: idenfy-kyb-form-answers
- name: KybFormCreateRequest
  property_count: 4
  slug: idenfy-kyb-form-create-request
- name: KybFormCreate
  property_count: 6
  slug: idenfy-kyb-form-create
- name: KybFormDocumentCreateRequest
  property_count: 3
  slug: idenfy-kyb-form-document-create-request
- name: KybFormDocumentCreate
  property_count: 4
  slug: idenfy-kyb-form-document-create
- name: KybFormDocumentRequest
  property_count: 2
  slug: idenfy-kyb-form-document-request
- name: KybFormDocument
  property_count: 4
  slug: idenfy-kyb-form-document
- name: KybFormList
  property_count: 3
  slug: idenfy-kyb-form-list
- name: KybForm
  property_count: 6
  slug: idenfy-kyb-form
- name: KybFormUpdateRequest
  property_count: 2
  slug: idenfy-kyb-form-update-request
- name: KybFormUpdate
  property_count: 2
  slug: idenfy-kyb-form-update
- name: KybInfo
  property_count: 3
  slug: idenfy-kyb-info
- name: KybPdfRequest
  property_count: 2
  slug: idenfy-kyb-pdf-request
- name: KybTokenRequest
  property_count: 0
  slug: idenfy-kyb-token-request
- name: KybToken
  property_count: 0
  slug: idenfy-kyb-token
- name: KybTokenUpdateRequest
  property_count: 2
  slug: idenfy-kyb-token-update-request
- name: KybTokenUpdate
  property_count: 2
  slug: idenfy-kyb-token-update
- name: PaginatedAmlMonitoringListList
  property_count: 4
  slug: idenfy-paginated-aml-monitoring-list-list
- name: PaginatedBankTransactionList
  property_count: 4
  slug: idenfy-paginated-bank-transaction-list
- name: PaginatedCompanyListList
  property_count: 4
  slug: idenfy-paginated-company-list-list
- name: PaginatedPartnerIdentificationListList
  property_count: 4
  slug: idenfy-paginated-partner-identification-list-list
- name: PatchedAmlMonitoringUpdateRequest
  property_count: 2
  slug: idenfy-patched-aml-monitoring-update-request
- name: PatchedBeneficiaryDocumentRequest
  property_count: 0
  slug: idenfy-patched-beneficiary-document-request
- name: PatchedBeneficiaryRequest
  property_count: 6
  slug: idenfy-patched-beneficiary-request
- name: PatchedKybFormDocumentRequest
  property_count: 2
  slug: idenfy-patched-kyb-form-document-request
- name: PatchedKybTokenUpdateRequest
  property_count: 2
  slug: idenfy-patched-kyb-token-update-request
- name: PoaCheckDetailRequest
  property_count: 3
  slug: idenfy-poa-check-detail-request
- name: PoaCheckDetail
  property_count: 20
  slug: idenfy-poa-check-detail
- name: Questionnaire
  property_count: 7
  slug: idenfy-questionnaire
- name: RegistryCenterCheckRequest
  property_count: 0
  slug: idenfy-registry-center-check-request
- name: RegistryCenterCheck
  property_count: 0
  slug: idenfy-registry-center-check
- name: SosReportDocument
  property_count: 9
  slug: idenfy-sos-report-document
- name: SosReportParameterRequest
  property_count: 5
  slug: idenfy-sos-report-parameter-request
jsonld:
- class_count: 120
  name: Idenfy Context
  property_count: 219
  slug: idenfy-context
layout: provider
mcp_servers:
- description: iDenfy runs a hosted, remote Model Context Protocol server over the full public documentation site. It is read-only and unauthenticated — it serves published documentation pages and the OpenAPI specs,
  name: iDenfy Documentation MCP Server
  slug: idenfy-documentation-mcp-server
modified: '2026-09-13'
name: iDenfy
nav: Providers
network: true
overview: 'iDenfy publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Age Estimation API, AML Checks API, AML Monitorings API, and 19 more. Tagged areas include AML, Age Verification, Bank Verification, Biometrics, and Compliance.


  The iDenfy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  iDenfy''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, pricing, and 51 more developer resources.'
plans:
- name: Idenfy Plans Pricing
  plan_count: 3
  slug: idenfy-plans-pricing
- name: Idenfy Price Estimates
  plan_count: 0
  slug: idenfy-price-estimates
random_paper: 15
rate_limits:
- limit_count: 0
  name: Idenfy Rate Limits
  slug: idenfy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: iDenfy API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: idenfy-rules
score:
  band: exemplar
  composite: 68.2
  coverage:
    artifact_dirs: 37
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 89.5
    contract_governance: 22.0
    contract_quality: 69.7
    developer_ergonomics: 81.0
    discoverability: 80.0
    operational_transparency: 47.4
  previous_composite: 68.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 67.9
      total: 28
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/idenfy/idenfy-2026-06-20T183205.png
security:
- kind: authentication
  name: Idenfy Authentication
  slug: idenfy-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Idenfy Domain Security
  slug: idenfy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Idenfy Vulnerability Disclosure
  slug: idenfy-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Idenfy Trust Center
  slug: idenfy-trust-center
  summary_line: ISO/IEC 27001:2022, SOC 2 Type II, eIDAS, iBeta / ISO 30107-3
skill_count: 1
skills:
- name: idenfy
  slug: idenfy-verification-skill
slug: idenfy
tags:
- AML
- Age Verification
- Bank Verification
- Biometrics
- Compliance
- Fraud Prevention
- Identity Verification
- KYB
- KYC
- MCP
- Open Banking
- RegTech
- Sanctions Screening
- Webhook
- A2A
website: https://www.idenfy.com/
---
