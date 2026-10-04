---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - finops
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 174
  human_in_the_loop: 1
  name: Amtrust Financial Services Agentic Access
  operation_count: 371
  slug: amtrust-financial-services-agentic-access
  summary_line: 371 operations · 174 acting · 1 human-in-the-loop
api_count: 9
apis:
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Admin API from AmTrust Financial Services — 31 operation(s) for admin.
  name: AmTrust Financial Services Admin API
  slug: amtrust-financial-services-admin-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Agent Contacts API from AmTrust Financial Services — 1 operation(s) for agent contacts.
  name: AmTrust Financial Services Agent Contacts API
  slug: amtrust-financial-services-agent-contacts-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: Coverage appetite and eligibility checks
  name: AmTrust Financial Services Appetite API
  slug: amtrust-financial-services-appetite-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: OAuth 2.0 token management
  name: AmTrust Financial Services Authentication API
  slug: amtrust-financial-services-authentication-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Bind API from AmTrust Financial Services — 1 operation(s) for bind.
  name: AmTrust Financial Services Bind API
  slug: amtrust-financial-services-bind-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Callconsent API from AmTrust Financial Services — 1 operation(s) for callconsent.
  name: AmTrust Financial Services Callconsent API
  slug: amtrust-financial-services-callconsent-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Contract API from AmTrust Financial Services — 23 operation(s) for contract.
  name: AmTrust Financial Services Contract API
  slug: amtrust-financial-services-contract-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The DmsDocument API from AmTrust Financial Services — 4 operation(s) for dmsdocument.
  name: AmTrust Financial Services Dms Document API
  slug: amtrust-financial-services-dmsdocument-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Document API from AmTrust Financial Services — 1 operation(s) for document.
  name: AmTrust Financial Services Document API
  slug: amtrust-financial-services-document-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The DownloadInfo API from AmTrust Financial Services — 1 operation(s) for downloadinfo.
  name: AmTrust Financial Services Download Info API
  slug: amtrust-financial-services-downloadinfo-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The HardStops API from AmTrust Financial Services — 2 operation(s) for hardstops.
  name: AmTrust Financial Services Hard Stops API
  slug: amtrust-financial-services-hardstops-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Health API from AmTrust Financial Services — 1 operation(s) for health.
  name: AmTrust Financial Services Health API
  slug: amtrust-financial-services-health-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Insured Clearance API from AmTrust Financial Services — 1 operation(s) for insured clearance.
  name: AmTrust Financial Services Insured Clearance API
  slug: amtrust-financial-services-insured-clearance-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Layer API from AmTrust Financial Services — 9 operation(s) for layer.
  name: AmTrust Financial Services Layer API
  slug: amtrust-financial-services-layer-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Liability Limits API from AmTrust Financial Services — 1 operation(s) for liability limits.
  name: AmTrust Financial Services Liability Limits API
  slug: amtrust-financial-services-liability-limits-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Location API from AmTrust Financial Services — 11 operation(s) for location.
  name: AmTrust Financial Services Location API
  slug: amtrust-financial-services-location-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Loss History API from AmTrust Financial Services — 1 operation(s) for loss history.
  name: AmTrust Financial Services Loss History API
  slug: amtrust-financial-services-loss-history-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Mcm API from AmTrust Financial Services — 3 operation(s) for mcm.
  name: AmTrust Financial Services Mcm API
  slug: amtrust-financial-services-mcm-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Payment Plans API from AmTrust Financial Services — 4 operation(s) for payment plans.
  name: AmTrust Financial Services Payment Plans API
  slug: amtrust-financial-services-payment-plans-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Payments API from AmTrust Financial Services — 2 operation(s) for payments.
  name: AmTrust Financial Services Payments API
  slug: amtrust-financial-services-payments-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: Policy binding and management
  name: AmTrust Financial Services Policies API
  slug: amtrust-financial-services-policies-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Policy API from AmTrust Financial Services — 3 operation(s) for policy.
  name: AmTrust Financial Services Policy API
  slug: amtrust-financial-services-policy-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Quote API from AmTrust Financial Services — 6 operation(s) for quote.
  name: AmTrust Financial Services Quote API
  slug: amtrust-financial-services-quote-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Quotes API from AmTrust Financial Services — 18 operation(s) for quotes.
  name: AmTrust Financial Services Quotes API
  slug: amtrust-financial-services-quotes-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Reference Resources API from AmTrust Financial Services — 15 operation(s) for reference resources.
  name: AmTrust Financial Services Reference Resources API
  slug: amtrust-financial-services-reference-resources-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Shared API from AmTrust Financial Services — 15 operation(s) for shared.
  name: AmTrust Financial Services Shared API
  slug: amtrust-financial-services-shared-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The SyncLog API from AmTrust Financial Services — 2 operation(s) for synclog.
  name: AmTrust Financial Services Sync Log API
  slug: amtrust-financial-services-synclog-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Terms of Agreement API from AmTrust Financial Services — 3 operation(s) for terms of agreement.
  name: AmTrust Financial Services Terms of Agreement API
  slug: amtrust-financial-services-terms-of-agreement-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Underwriting API from AmTrust Financial Services — 1 operation(s) for underwriting.
  name: AmTrust Financial Services Underwriting API
  slug: amtrust-financial-services-underwriting-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Underwriting Questions API from AmTrust Financial Services — 2 operation(s) for underwriting questions.
  name: AmTrust Financial Services Underwriting Questions API
  slug: amtrust-financial-services-underwriting-questions-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Workers Comp API from AmTrust Financial Services — 72 operation(s) for workers comp.
  name: AmTrust Financial Services Workers Comp API
  slug: amtrust-financial-services-workers-comp-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Workers Comp-Specialty Programs API from AmTrust Financial Services — 77 operation(s) for workers comp-specialty programs.
  name: AmTrust Financial Services Workers Comp-Specialty Programs API
  slug: amtrust-financial-services-workers-comp-specialty-programs-api
- baseURL: https://gateway.amtrustgroup.com/DigitalAPI
  baseurl_source: declared
  description: The Action Log API from AmTrust Financial Services — 2 operation(s) for action log.
  name: AmTrust Financial Services Action Log API
  slug: amtrust-financial-services-action-log-api
artifact_total: 85
collections:
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite API
  slug: postman-amtrust-financial-services-appetite-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Authentication API
  slug: postman-amtrust-financial-services-authentication-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Policies API
  slug: postman-amtrust-financial-services-policies-api
- collection_type: postman
  name: AmTrust Financial Services Commercial Lines Appetite Quotes API
  slug: postman-amtrust-financial-services-quotes-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AmTrust Financial Services Commercial Lines Appetite API
  slug: open-amtrust-financial-services-appetite-api
- collection_type: open
  name: AmTrust Financial Services Commercial Lines Appetite Authentication API
  slug: open-amtrust-financial-services-authentication-api
- collection_type: open
  name: AmTrust Financial Services Commercial Lines Appetite Policies API
  slug: open-amtrust-financial-services-policies-api
- collection_type: open
  name: AmTrust Financial Services Commercial Lines Appetite Quotes API
  slug: open-amtrust-financial-services-quotes-api
common:
- group: company
  title: ''
  type: Website
  url: https://amtrustfinancial.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amtrust-financial-services/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/agentic-access/amtrust-financial-services-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amtrust-financial-services-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/security/amtrust-financial-services-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amtrust-financial-services-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/security/amtrust-financial-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amtrust-financial-services-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/authentication/amtrust-financial-services-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amtrust-financial-services-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amtrust-financial-services-inc
- group: start
  title: ''
  type: Portal
  url: https://amtrustfinancial.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.amtrustgroup.com
- group: docs
  title: ''
  type: APIReference
  url: https://apiportal.amtrustgroup.com/apis
- group: docs
  title: ''
  type: Documentation
  url: https://amtrustfinancial.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://apiportal.amtrustgroup.com/authentication
- group: start
  title: ''
  type: SignUp
  url: https://amtrustfinancial.com/api
- group: operate
  title: ''
  type: Support
  url: https://amtrustfinancial.com/about-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amtrustfinancial.com/about-us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amtrustfinancial.com/about-us/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/well-known/amtrust-financial-services-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amtrust-financial-services-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/well-known/amtrust-financial-services-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/amtrust-financial-services-openid-configuration.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/llms/amtrust-financial-services-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amtrust-financial-services-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/scopes/amtrust-financial-services-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/amtrust-financial-services-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/conventions/amtrust-financial-services-conventions.yml
  title: ''
  type: Conventions
  url: conventions/amtrust-financial-services-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/errors/amtrust-financial-services-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/amtrust-financial-services-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/lifecycle/amtrust-financial-services-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/amtrust-financial-services-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/conformance/amtrust-financial-services-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amtrust-financial-services-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/data-model/amtrust-financial-services-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amtrust-financial-services-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/sandbox/amtrust-financial-services-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/amtrust-financial-services-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/packages/amtrust-financial-services-packages.yml
  title: ''
  type: Packages
  url: packages/amtrust-financial-services-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/mcp/amtrust-financial-services-mcp.yml
  title: ''
  type: MCP
  url: mcp/amtrust-financial-services-mcp.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/plans/amtrust-financial-services-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amtrust-financial-services-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/rate-limits/amtrust-financial-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amtrust-financial-services-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/finops/amtrust-financial-services-finops.yml
  title: ''
  type: FinOps
  url: finops/amtrust-financial-services-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-digital-wc-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-digital-wc-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-digital-bop-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-digital-bop-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-digital-cyber-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-digital-cyber-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-digital-es-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-digital-es-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-digital-pac-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-digital-pac-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-reinsurance-contract-entry-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-reinsurance-contract-entry-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-experience-claims-medical-case-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-experience-claims-medical-case-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-experience-next-gen-bond-pro-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-experience-next-gen-bond-pro-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/overlays/amtrust-financial-services-conversa-engine-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/amtrust-financial-services-conversa-engine-api-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/rules/amtrust-financial-services-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/amtrust-financial-services-spectral-rules.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/json-schema/amtrust-financial-services-quote-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-request-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/json-schema/amtrust-financial-services-quote-response-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/amtrust-financial-services-quote-response-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/json-ld/amtrust-financial-services-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amtrust-financial-services-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/vocabulary/amtrust-financial-services-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/amtrust-financial-services-vocabulary.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/json-structure/amtrust-financial-services-quote-request-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/amtrust-financial-services-quote-request-structure.json
- group: company
  title: ''
  type: Blog
  url: https://amtrustfinancial.com/blog
description: AmTrust Financial Services is a multinational specialty property and casualty insurer focused on small to mid-sized businesses, with more than 7,000 employees, 500,000+ small commercial policies in force and an AM Best rating of A- (Excellent). AmTrust runs a real, production API program on Azure API Management — nine externally exposed APIs at gateway.amtrustgroup.com spanning 387 operations, covering workers' compensation, Businessowners Policy, cyber, Excess & Surplus and commercial package quote-rate-bind, plus medical case management claims, surety bond documents and reinsurance contract entry. Authentication is two-factor at the edge — an Azure API Management subscription key (subscriber_id) alongside a four-hour OpenID Connect bearer token from AmTrust's own IdentityServer at auth.amtrustgroup.com. Access is partner-gated; there is no self-serve signup and no published pricing, and credentials follow a Digital Partner Vetting Questionnaire.
examples:
- key_count: 4
  name: Amtrust Financial Services Appetite Request Example
  slug: amtrust-financial-services-appetite-request-example
- key_count: 7
  name: Amtrust Financial Services Policy Example
  slug: amtrust-financial-services-policy-example
- key_count: 6
  name: Amtrust Financial Services Quote Request Example
  slug: amtrust-financial-services-quote-request-example
- key_count: 9
  name: Amtrust Financial Services Quote Response Example
  slug: amtrust-financial-services-quote-response-example
features:
- description: Review coverage eligibility for specific business classes and risk profiles.
  name: Appetite Check
- description: Generate commercial lines quotes in real time via API.
  name: Instant Quoting
- description: Bind policies programmatically for eligible class codes.
  name: Online Binding
- description: Access over 300 bind-online eligible class codes.
  name: 300+ Class Codes
- description: Token-based authentication with 4-hour access tokens.
  name: OAuth 2.0 Authentication
- description: 12 million daily API calls with 99.68% uptime SLA.
  name: High Availability
finops:
- name: Amtrust Financial Services Finops
  service_category: API
  slug: amtrust-financial-services-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amtrust-financial-services.png
integrations:
- description: Workers' compensation digital submission integration.
  name: Appulate
- description: Commercial lines quoting platform integration.
  name: Semsee
- description: Commercial lines quoting marketplace integration.
  name: Tarmika
- description: Commercial lines rating platform integration.
  name: IBQ Systems
json_schemas:
- name: AppetiteRequest
  property_count: 4
  slug: amtrust-financial-services-appetite-request
- name: AppetiteResponse
  property_count: 4
  slug: amtrust-financial-services-appetite-response
- name: BindRequest
  property_count: 3
  slug: amtrust-financial-services-bind-request
- name: Insured
  property_count: 7
  slug: amtrust-financial-services-insured
- name: PolicyResponse
  property_count: 8
  slug: amtrust-financial-services-policy-response
- name: QuoteRequest
  property_count: 7
  slug: amtrust-financial-services-quote-request
- name: QuoteResponse
  property_count: 10
  slug: amtrust-financial-services-quote-response
json_structures:
- name: Amtrust Financial Services Appetite Request Structure
  property_count: 4
  slug: amtrust-financial-services-appetite-request-structure
- name: Amtrust Financial Services Appetite Response Structure
  property_count: 4
  slug: amtrust-financial-services-appetite-response-structure
- name: Amtrust Financial Services Bind Request Structure
  property_count: 3
  slug: amtrust-financial-services-bind-request-structure
- name: Amtrust Financial Services Insured Structure
  property_count: 7
  slug: amtrust-financial-services-insured-structure
- name: Amtrust Financial Services Policy Response Structure
  property_count: 8
  slug: amtrust-financial-services-policy-response-structure
- name: Amtrust Financial Services Quote Request Structure
  property_count: 7
  slug: amtrust-financial-services-quote-request-structure
- name: Amtrust Financial Services Quote Response Structure
  property_count: 10
  slug: amtrust-financial-services-quote-response-structure
jsonld:
- class_count: 6
  name: Amtrust Financial Services Context
  property_count: 13
  slug: amtrust-financial-services-context
layout: provider
modified: '2026-09-02'
name: AmTrust Financial Services
nav: Providers
network: true
overview: 'AmTrust Financial Services publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agent Contacts API, Appetite API, and 30 more. Tagged areas include Commercial Insurance, Insurance, Property and Casualty, Small Business, and Workers Compensation.


  The AmTrust Financial Services catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AmTrust Financial Services'' developer surface includes authentication, developer portal, API reference, documentation, signup flow, support, sandbox, and 41 more developer resources.'
plans:
- name: Amtrust Financial Services Plans Pricing
  plan_count: 0
  slug: amtrust-financial-services-plans-pricing
press:
- date: ''
  title: AmTrust Improves Outcomes for Injured Employees with ...
  url: https://claraanalytics.com/news/amtrust-scores-a-win-win-with-small-businesses-ensuring-quality-care-for-injured-employees/
- date: ''
  title: AmTrust partners with TCS to transform E&S clearance ...
  url: https://www.tcs.com/what-we-do/industries/insurance/case-study/amtrust-financial-services-transformation
- date: ''
  title: Hagens Berman Alerts Investors in AmTrust Financial ...
  url: https://www.prnewswire.com/news-releases/afsi-investor-alert-hagens-berman-alerts-investors-in-amtrust-financial-services-to-investigation-into-possible-securities-law-violations-related-to-admitted-material-weaknesses-in-internal-controls-over-financial-reporting-300414199.html
- date: ''
  title: AmTrust Financial Services and Blackstone Credit & ...
  url: https://www.sttinfo.fi/tiedote/71449628/amtrust-financial-services-and-blackstone-credit-and-insurance-enter-into-strategic-transaction-for-amtrusts-global-mga-and-fee-businesses?publisherId=58763726&lang=en
- date: ''
  title: 'AmTrust partners with Blackstone: Insurance news'
  url: https://www.dig-in.com/news/amtrust-partners-with-blackstone-insurance-news
random_paper: 13
rate_limits:
- limit_count: 0
  name: Amtrust Financial Services Rate Limits
  slug: amtrust-financial-services-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AmTrust Financial Services API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amtrust-financial-services-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: AmTrust Financial Services API Rules
  rule_count: 17
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 10
  slug: amtrust-financial-services-spectral-rules
scopes:
- name: Amtrust Financial Services Scopes
  scope_count: 0
  slug: amtrust-financial-services-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 33
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 31.8
    contract_quality: 46.9
    developer_ergonomics: 55.4
    discoverability: 78.6
    operational_transparency: 0.0
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 78.9
      derived: 8
      marker_coverage: 21.1
      total: 38
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 42.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/amtrust-financial-services/refs/heads/main/screenshots/amtrust-financial-services-2026-06-20T171943.png
security:
- kind: authentication
  name: Amtrust Financial Services Authentication
  slug: amtrust-financial-services-authentication
  summary_line: apiKey/openIdConnect · 4 schemes
- kind: domain-security
  name: Amtrust Financial Services Domain Security
  slug: amtrust-financial-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amtrust Financial Services Vulnerability Disclosure
  slug: amtrust-financial-services-vulnerability-disclosure
  summary_line: Hackerone
slug: amtrust-financial-services
tags:
- Commercial Insurance
- Insurance
- Property and Casualty
- Small Business
- Workers Compensation
- Fortune 1000
- Underwriting
- Claims
- Policy
- Reinsurance
- Cyber Insurance
- Surety
use_cases:
- description: Embed AmTrust quoting and binding in agent management systems.
  name: Agent Platform Integration
- description: Automate workers' compensation submissions from wholesale platforms.
  name: Wholesale Brokerage Automation
- description: Connect agency management software to AmTrust for policy lifecycle management.
  name: AMS Software Integration
- description: Streamline small business workers' compensation from quote to bind.
  name: Workers Compensation Automation
website: https://amtrustfinancial.com/
---
