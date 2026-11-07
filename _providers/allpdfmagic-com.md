---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AllPDFMagic API as documented publicly: 57 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AllPDFMagic API
  slug: allpdfmagic-com-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/allpdfmagic-com/plans/allpdfmagic-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/allpdfmagic-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/allpdfmagic-com/rules/allpdfmagic-com-rules.yml
  title: ''
  type: Spectral
  url: rules/allpdfmagic-com-rules.yml
- group: design
  href: https://artifacts.apis.io/allpdfmagic-com/json-ld/allpdfmagic-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/allpdfmagic-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/allpdfmagic-com/vocabulary/allpdfmagic-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/allpdfmagic-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/allpdfmagic-com/data-model/allpdfmagic-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/allpdfmagic-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.allpdfmagic.com/security
- group: design
  href: https://artifacts.apis.io/allpdfmagic-com/conformance/allpdfmagic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/allpdfmagic-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/allpdfmagic-com/llms/allpdfmagic-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/allpdfmagic-com-llms.txt
- group: other
  href: https://artifacts.apis.io/allpdfmagic-com/hosts/allpdfmagic-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/allpdfmagic-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/allpdfmagic-com/vendors/allpdfmagic-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/allpdfmagic-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.allpdfmagic.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.allpdfmagic.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://www.allpdfmagic.com/status
- group: start
  title: ''
  type: SignUp
  url: https://www.allpdfmagic.com/signup
- group: auth
  title: ''
  type: Security
  url: https://www.allpdfmagic.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.allpdfmagic.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.allpdfmagic.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.allpdfmagic.com/docs/api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.allpdfmagic.com/blog/category/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.allpdfmagic.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.allpdfmagic.com/blog
- group: auth
  href: https://artifacts.apis.io/allpdfmagic-com/security/allpdfmagic-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/allpdfmagic-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/allpdfmagic-com/security/allpdfmagic-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/allpdfmagic-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/allpdfmagic-com/security/allpdfmagic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/allpdfmagic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://allpdfmagic.com/
coverage:
  checked: '2026-11-01'
  detail: API documentation is provided as HTML pages without a downloadable OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.allpdfmagic.com/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AllPDFMagic provides a suite of free online PDF tools powered by AI, enabling users to compress, merge, edit, convert, and extract data from PDFs quickly and securely. The platform emphasizes privacy with SSL encryption and automatic file deletion after processing. Targeted at individuals, businesses, and finance teams, it offers both free utilities and premium features for professional workflows, including invoice extraction, document comparison, and AI‑assisted summarization.
image: https://www.allpdfmagic.com/og-image.svg
json_schemas:
- name: PostApiV1PdfAddPageNumbersRequest
  property_count: 4
  slug: allpdfmagic-com-post-api-v1-pdf-add-page-numbers-request
- name: PostApiV1PipelinesContractIntelResponse
  property_count: 5
  slug: allpdfmagic-com-post-api-v1-pipelines-contract-intel-response
- name: PostApiV1PipelinesOnboardingResponse
  property_count: 4
  slug: allpdfmagic-com-post-api-v1-pipelines-onboarding-response
- name: PostApiV1PipelinesTrustedDataResponse
  property_count: 3
  slug: allpdfmagic-com-post-api-v1-pipelines-trusted-data-response
- name: PostApiV1SandboxAiExtractInvoiceRequest
  property_count: 3
  slug: allpdfmagic-com-post-api-v1-sandbox-ai-extract-invoice-request
- name: PostApiV1WorkflowsProcessBankStatementResponse
  property_count: 3
  slug: allpdfmagic-com-post-api-v1-workflows-process-bank-statement-response
jsonld:
- class_count: 46
  name: Allpdfmagic Com Context
  property_count: 52
  slug: allpdfmagic-com-context
layout: provider
modified: '2026-11-01'
name: AllPDFMagic
nav: Providers
network: true
overview: 'AllPDFMagic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include PDF, Artificial Intelligence, Tools, Online, and Free.


  The AllPDFMagic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AllPDFMagic''s developer surface includes support, signup flow, pricing, documentation, changelog, engineering blog, and 19 more developer resources.'
plans:
- name: Allpdfmagic Com Plans Pricing
  plan_count: 5
  slug: allpdfmagic-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AllPDFMagic API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: allpdfmagic-com-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 47.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Allpdfmagic Com Domain Security
  slug: allpdfmagic-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Allpdfmagic Com Vulnerability Disclosure
  slug: allpdfmagic-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Allpdfmagic Com Trust Center
  slug: allpdfmagic-com-trust-center
  summary_line: SOC 2, GDPR
slug: allpdfmagic-com
tags:
- PDF
- Artificial Intelligence
- Tools
- Online
- Free
website: https://allpdfmagic.com/
---
