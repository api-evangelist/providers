---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: API for Foxit eSign documented at the Foxit Developer portal.
  name: Foxit eSign API
  slug: foxit-esign-api
- baseURL: https://na1.fusion.foxit.com
  baseurl_source: declared
  description: The Document Generation API from Foxit eSign — 1 operation(s) for document generation.
  name: Foxit eSign Document Generation API
  slug: foxit-document-generation-api
- baseURL: https://na1.fusion.foxit.com
  baseurl_source: declared
  description: The Documents API from Foxit eSign — 1 operation(s) for documents.
  name: Foxit eSign Documents API
  slug: foxit-documents-api
- baseURL: https://na1.fusion.foxit.com
  baseurl_source: declared
  description: The Foxit ESign API API from Foxit eSign — 1 operation(s) for foxit esign api.
  name: Foxit eSign Foxit ESign API
  slug: foxit-foxit-esign-api-api
- baseURL: https://na1.fusion.foxit.com
  baseurl_source: declared
  description: The Pdf Services API from Foxit eSign — 3 operation(s) for pdf services.
  name: Foxit eSign Pdf Services API
  slug: foxit-pdf-services-api
artifact_total: 15
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/well-known/foxit-foxit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/foxit-foxit-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/plans/foxit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/foxit-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/rules/foxit-rules.yml
  title: ''
  type: Spectral
  url: rules/foxit-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/json-ld/foxit-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/foxit-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/vocabulary/foxit-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/foxit-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/data-model/foxit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/foxit-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/conformance/foxit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/foxit-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/llms/foxit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/foxit-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/well-known/foxit-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/foxit-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/well-known/foxit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/foxit-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/hosts/foxit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/foxit-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/vendors/foxit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/foxit-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.foxit.com/trust-center/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.foxit.com/product/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://www.foxit.com/support/refund-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.foxit.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.foxit.com/company/register-partner-deal/
- group: auth
  title: ''
  type: Security
  url: https://www.foxit.com/support/security/
- group: build
  title: ''
  type: SDKs
  url: https://www.foxit.com/sdk/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.foxit.com/company/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.foxit.com/ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.foxit.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.foxit.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/security/foxit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/foxit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/foxit/refs/heads/main/security/foxit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/foxit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://foxit.com/
coverage:
  checked: '2026-10-16'
  detail: Developer portal pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://developers.foxit.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Foxit Software provides Foxit eSign, a solution that enables organizations to send, sign, and manage agreements through secure electronic signature workflows. The service is offered to businesses that need to handle legally binding signatures, integrate signing into document processes, and manage signed documents at scale. It is part of Foxit’s broader portfolio of PDF and document productivity tools.
image: https://www.foxit.com/assets/images/og-images/thumb.webp
json_schemas:
- name: GetDocumentGenerationApiApiidResponse
  property_count: 2
  slug: foxit-get-document-generation-api-apiid-response
- name: GetPdfServicesApiDocumentsUploadResponse
  property_count: 4
  slug: foxit-get-pdf-services-api-documents-upload-response
- name: GetPdfServicesApiTasksTaskIdResponse
  property_count: 4
  slug: foxit-get-pdf-services-api-tasks-task-id-response
- name: PostDocumentGenerationApiApiidRequest
  property_count: 1
  slug: foxit-post-document-generation-api-apiid-request
- name: PostPdfServicesApiDocumentsUploadResponse
  property_count: 1
  slug: foxit-post-pdf-services-api-documents-upload-response
jsonld:
- class_count: 5
  name: Foxit Context
  property_count: 8
  slug: foxit-context
layout: provider
modified: '2026-10-16'
name: Foxit eSign
nav: Providers
network: true
overview: 'Foxit eSign is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Document Generation API, Documents API, Foxit ESign API, and 2 more. Tagged areas include E-Signature, Document Management, PDF, Cloud APIs, and Enterprise Software.


  The Foxit eSign catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Foxit eSign''s developer surface includes support, signup flow, pricing, engineering blog, documentation, and 21 more developer resources.'
plans:
- name: Foxit Plans Pricing
  plan_count: 1
  slug: foxit-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Foxit eSign API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: foxit-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 35.6
    contract_quality: 23.5
    developer_ergonomics: 23.8
    discoverability: 69.6
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Foxit Domain Security
  slug: foxit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Foxit Vulnerability Disclosure
  slug: foxit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: foxit
tags:
- E-Signature
- Document Management
- PDF
- Cloud APIs
- Enterprise Software
- Workflow Automation
website: https://foxit.com/
---
