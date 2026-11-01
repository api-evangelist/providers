---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: REST API for Banking as a Service (digital and escrow accounts, Pix, TED, boletos, cards, DDA) and Lending as a Service (debt issuance, simulation, formalization), served from the shared BaaS/LaaS hos
  name: QI Tech Banking and Lending as a Service API
  slug: banking-and-lending-api
- description: 'REST API for Risk Solutions: onboarding, OCR, face recognition, device scan and Pix limits. Production and sandbox hosts are stated in the host table at https://docs.qitech.com.br/documentation/introd'
  name: QI Tech Risk Solutions (CaaS) API
  slug: risk-solutions-api
- description: REST API for CertifiQI, the QI Tech platform for signing documents with ICP-Brasil certificates (CAdES p7s and PAdES PDF signatures) at high volume. Production and sandbox hosts are stated in the host
  name: QI Tech CertifiQI API
  slug: certifiqi-api
- description: 'REST API for Insurance as a Service products. Production and sandbox hosts are stated in the host table at https://docs.qitech.com.br/documentation/introducao_api_reference (sandbox: https://api.sandb'
  name: QI Tech Insurance as a Service API
  slug: insurance-api
- baseURL: https://api.caas.qitech.app
  baseurl_source: declared
  description: 'QI Tech API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: QI Tech API
  slug: qi-tech-api
artifact_total: 18
common:
- group: commercial
  href: https://artifacts.apis.io/qi-tech/plans/qi-tech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qi-tech-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/rules/qi-tech-rules.yml
  title: ''
  type: Spectral
  url: rules/qi-tech-rules.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/json-ld/qi-tech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qi-tech-context.jsonld
- group: design
  href: https://artifacts.apis.io/qi-tech/vocabulary/qi-tech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qi-tech-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/data-model/qi-tech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qi-tech-data-model.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/conventions/qi-tech-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qi-tech-conventions.yml
- group: auth
  href: https://artifacts.apis.io/qi-tech/authentication/qi-tech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qi-tech-authentication.yml
- group: operate
  href: https://artifacts.apis.io/qi-tech/lifecycle/qi-tech-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/qi-tech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/lifecycle/qi-tech-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qi-tech-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/errors/qi-tech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qi-tech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qi-tech/conformance/qi-tech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qi-tech-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qi-tech/llms/qi-tech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qi-tech-llms.txt
- group: other
  href: https://artifacts.apis.io/qi-tech/hosts/qi-tech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qi-tech-hosts.yml
- group: build
  href: https://artifacts.apis.io/qi-tech/integrations/qi-tech-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/qi-tech-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/qi-tech/vendors/qi-tech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qi-tech-vendors.yml
- group: auth
  href: https://artifacts.apis.io/qi-tech/security/qi-tech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qi-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://qitech.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qitech.com.br/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qitech.com.br/documentation/introducao_api_reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qitech.com.br/documentation/primeiros_passos/inicio
- group: other
  title: ''
  type: Playground
  url: https://docs.qitech.com.br/playground
- group: operate
  title: ''
  type: Support
  url: https://qitech.com.br/central-de-ajuda/
- group: operate
  title: ''
  type: Contact
  url: https://qitech.com.br/contato/
- group: company
  title: ''
  type: Blog
  url: https://qitech.blog/
- group: company
  title: ''
  type: Newsroom
  url: https://qitech.com.br/newsroom/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qitech.com.br/politica-de-privacidade/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qi-tech/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@qitechoficial/videos
created: '2026-10-18'
description: 'QI Tech (legal entity on its docs: QI Sociedade de Crédito Direto S.A.) is a Brazilian financial-infrastructure company offering regulated APIs to build financial products: Lending as a Service (debt issuance, simulation, formalization, payroll-deductible credit), Banking as a Service (digital accounts, Pix, TED, boletos, escrow accounts), Risk Solutions (KYC, onboarding, antifraud, credit analysis, SCR) and investment fund administration and custody (FIDC, DTVM). Its developer documentation at docs.qitech.com.br covers API key exchange, authentication, webhooks and an API playground.'
image: https://qitech.com.br/covers/qi-tech-infraestrutura-financeira-baas-laas-fidc.png
json_schemas:
- name: PostLimitsPixAccountAccountidLimitUpdateRequestRequest
  property_count: 4
  slug: qi-tech-post-limits-pix-account-accountid-limit-update-request-request
- name: PostLimitsPixAccountAccountidLimitUpdateRequestResponse
  property_count: 7
  slug: qi-tech-post-limits-pix-account-accountid-limit-update-request-response
- name: PostLimitsPixAccountAccountidRecipientListRecipientResponse
  property_count: 5
  slug: qi-tech-post-limits-pix-account-accountid-recipient-list-recipient-response
- name: PostLimitsPixAccountRequest
  property_count: 3
  slug: qi-tech-post-limits-pix-account-request
- name: PostOnboardingLegalPersonRequest
  property_count: 7
  slug: qi-tech-post-onboarding-legal-person-request
- name: PostOnboardingNaturalPersonRequest
  property_count: 7
  slug: qi-tech-post-onboarding-natural-person-request
jsonld:
- class_count: 20
  name: Qi Tech Context
  property_count: 36
  slug: qi-tech-context
layout: provider
modified: '2026-10-18'
name: QI Tech
nav: Providers
network: true
overview: 'QI Tech is listed with 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Banking as a Service, Lending, and Payments.


  The QI Tech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  QI Tech''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, YouTube channel, and 21 more developer resources.'
plans:
- name: Qi Tech Plans Pricing
  plan_count: 1
  slug: qi-tech-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Qi Tech Rate Limits
  slug: qi-tech-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: QI Tech API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: qi-tech-rules
scopes:
- name: Qi Tech Scopes
  scope_count: 0
  slug: qi-tech-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 73.0
    catalog_earned_first_party: 8.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 33.3
    contract_quality: 26.0
    developer_ergonomics: 54.8
    discoverability: 73.2
    operational_transparency: 7.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 27.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Qi Tech Authentication
  slug: qi-tech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Qi Tech Domain Security
  slug: qi-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: qi-tech
tags:
- Company
- Fintech
- Banking as a Service
- Lending
- Payments
- Pix
- KYC
- Fraud Prevention
- Fund Administration
- Brazil
website: https://qitech.com.br
---
