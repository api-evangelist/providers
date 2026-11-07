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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 4
  name: Digio Agentic Access
  operation_count: 10
  slug: digio-agentic-access
  summary_line: 10 operations · 6 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: Fetch government-issued documents (Aadhaar, PAN, driving licence and others) directly from India's DigiLocker with citizen consent for KYC.
  name: Digio DigiLocker API
  slug: digio-digilocker-api
- description: DigiShield - Anti-Money-Laundering and Counter-Financing-of-Terrorism screening and ongoing monitoring against sanctions and watchlists.
  name: Digio AML/CFT API
  slug: digio-aml-cft-api
- baseURL: https://api.digio.in
  baseurl_source: declared
  description: DigiDocs - template-based document and agreement creation with eStamp.
  name: Digio Documents API
  slug: digio-documents-api
- baseURL: https://api.digio.in
  baseurl_source: declared
  description: DigiCollect - eNACH / NACH electronic mandates for recurring debit.
  name: Digio eMandate API
  slug: digio-emandate-api
- baseURL: https://api.digio.in
  baseurl_source: declared
  description: DigiKYC - identity verification via CKYC, KRA, DigiLocker, and offline Aadhaar.
  name: Digio KYC API
  slug: digio-kyc-api
- baseURL: https://api.digio.in
  baseurl_source: declared
  description: DigiSign - Aadhaar and OTP based legally-valid electronic signatures.
  name: Digio e Sign API
  slug: digio-e-sign-api
artifact_total: 28
asyncapis:
- description: ''
  name: Digio Webhooks
  slug: digio-webhooks
collections:
- collection_type: postman
  name: Digio Documents API
  slug: postman-digio-documents-api
- collection_type: postman
  name: Digio Documents eMandate API
  slug: postman-digio-emandate-api
- collection_type: postman
  name: Digio Documents eSign API
  slug: postman-digio-esign-api
- collection_type: postman
  name: Digio Documents KYC API
  slug: postman-digio-kyc-api
- collection_type: open
  name: Digio Documents API
  slug: open-digio-documents-api
- collection_type: open
  name: Digio Documents eMandate API
  slug: open-digio-emandate-api
- collection_type: open
  name: Digio Documents eSign API
  slug: open-digio-esign-api
- collection_type: open
  name: Digio Documents KYC API
  slug: open-digio-kyc-api
common:
- group: other
  href: https://artifacts.apis.io/digio/capabilities/digio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/digio-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/digio/overview
- group: agent
  href: https://artifacts.apis.io/digio/agentic-access/digio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/digio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/digio/security/digio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/digio-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/digio/security/digio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/digio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/digio/security/digio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/digio-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/digio/authentication/digio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/digio-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/digio-tech
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/digio.in
- group: company
  title: ''
  type: Website
  url: https://www.digio.in/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.digio.in/
- group: commercial
  href: https://artifacts.apis.io/digio/plans/digio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/digio-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/digio/rate-limits/digio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/digio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/digio/finops/digio-finops.yml
  title: ''
  type: FinOps
  url: finops/digio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.digio.in/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.digio.in/
- group: operate
  title: ''
  type: Support
  url: https://www.digio.in/contact-us/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.digio.in/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.digio.in/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.digio.in/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.digio.in/privacy-policy/
- group: build
  href: https://artifacts.apis.io/digio/collections/digio.postman_collection.json
  title: ''
  type: Postman
  url: collections/digio.postman_collection.json
- group: agent
  href: https://artifacts.apis.io/digio/llms/digio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/digio-llms.txt
- group: build
  href: https://artifacts.apis.io/digio/packages/digio-packages.yml
  title: ''
  type: Packages
  url: packages/digio-packages.yml
- group: build
  href: https://artifacts.apis.io/digio/packages/digio-packages.yml
  title: ''
  type: SDKs
  url: packages/digio-packages.yml
- group: agent
  href: https://artifacts.apis.io/digio/mcp/digio-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/digio-mcp.yml
- group: other
  href: https://artifacts.apis.io/digio/overlays/digio-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/digio-overlay.yaml
- group: design
  href: https://artifacts.apis.io/digio/conformance/digio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/digio-conformance.yml
- group: auth
  href: https://artifacts.apis.io/digio/security/digio-trust-center.yml
  title: ''
  type: Compliance
  url: security/digio-trust-center.yml
- group: design
  href: https://artifacts.apis.io/digio/errors/digio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/digio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/digio/lifecycle/digio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/digio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/digio/conventions/digio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/digio-conventions.yml
- group: design
  href: https://artifacts.apis.io/digio/data-model/digio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/digio-data-model.yml
- group: design
  href: https://artifacts.apis.io/digio/asyncapi/digio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/digio-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/digio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/digio/sandbox/digio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/digio-sandbox.yml
created: '2026-07-17'
description: Digio is an India-based digital trust and paperwork automation platform. Its REST APIs deliver legally-valid Aadhaar and OTP eSign, eStamping, KYC (CKYC, KRA, DigiLocker, offline Aadhaar, and Video KYC), eNACH/NACH eMandates and UPI Autopay recurring payments, AML/CFT screening, and template-based document and agreement management. All endpoints use HTTPS with HTTP Basic authentication.
finops:
- has_sources: true
  method: generated
  name: Digio Finops
  primary_unit: ''
  service_category: Identity and Digital Trust
  slug: digio-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/digio.png
layout: provider
modified: '2026-06-20'
name: Digio
nav: Providers
network: true
overview: 'Digio publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Documents API, eMandate API, KYC API, and 3 more. Tagged areas include E-Signature, KYC, eNACH, eMandate, and Digital Signature.


  The Digio catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Digio''s developer surface includes authentication, documentation, engineering blog, support, pricing, signup flow, sandbox, and 29 more developer resources.'
plans:
- name: Digio Plans Pricing
  plan_count: 1
  slug: digio-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Digio Rate Limits
  slug: digio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Digio API Rules
  rule_count: 56
  severity_counts:
    error: 39
    hint: 0
    info: 6
    warn: 11
  slug: digio-rules
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 59.3
    developer_ergonomics: 48.2
    discoverability: 73.2
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 30.8
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/digio/digio-2026-07-25T212007.png
security:
- kind: authentication
  name: Digio Authentication
  slug: digio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Digio Domain Security
  slug: digio-domain-security
  summary_line: no transport/DNS hardening detected
- kind: vulnerability-disclosure
  name: Digio Vulnerability Disclosure
  slug: digio-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Digio Trust Center
  slug: digio-trust-center
  summary_line: ISO 27001, SOC 2
skill_count: 4
skills:
- name: Register an eNACH / UPI Autopay recurring-debit mandate
  slug: digio-create-emandate
- name: Collect a legally-valid eSignature on a document
  slug: digio-esign-document
- name: Run a DigiKYC identity-verification workflow
  slug: digio-run-kyc
- name: Generate a document from a template and collect eSign
  slug: digio-template-sign
slug: digio
tags:
- E-Signature
- KYC
- eNACH
- eMandate
- Digital Signature
- India
- Fintech
- Identity Verification
website: https://www.digio.in/
---
