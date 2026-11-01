---
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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: LawPay provides payment processing APIs for legal professionals. Documentation is available at the LLM Info page.
  name: LawPay API
  slug: lawpay-api-2
- baseURL: https://api.8am.com
  baseurl_source: declared
  description: 'LawPay API as documented publicly: 74 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: LawPay API
  slug: lawpay-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/lawpay/plans/lawpay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lawpay-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/lawpay/rules/lawpay-rules.yml
  title: ''
  type: Spectral
  url: rules/lawpay-rules.yml
- group: design
  href: https://artifacts.apis.io/lawpay/json-ld/lawpay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lawpay-context.jsonld
- group: design
  href: https://artifacts.apis.io/lawpay/vocabulary/lawpay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lawpay-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lawpay/data-model/lawpay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lawpay-data-model.yml
- group: design
  href: https://artifacts.apis.io/lawpay/conformance/lawpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lawpay-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lawpay/llms/lawpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lawpay-llms.txt
- group: auth
  href: https://artifacts.apis.io/lawpay/well-known/lawpay-supportcenter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lawpay-supportcenter-security.txt
- group: auth
  href: https://artifacts.apis.io/lawpay/well-known/lawpay-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/lawpay-help-security.txt
- group: agent
  href: https://artifacts.apis.io/lawpay/well-known/lawpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lawpay-well-known.yml
- group: other
  href: https://artifacts.apis.io/lawpay/hosts/lawpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lawpay-hosts.yml
- group: other
  href: https://artifacts.apis.io/lawpay/vendors/lawpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lawpay-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.lawpay.com/about/blog/category/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.lawpay.com/about/news/
- group: start
  title: ''
  type: Login
  url: https://www.lawpay.com/login/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.lawpay.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.lawpay.com/en/articles/10080776-8am-lawpay-quick-start-guide
- group: auth
  href: https://artifacts.apis.io/lawpay/security/lawpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lawpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lawpay.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lawpay.com/about/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lawpay.com/llm-info/
- group: operate
  title: ''
  type: Support
  url: https://www.lawpay.com/support/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lawpay.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.8am.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.8am.com/privacy-policy/
coverage:
  checked: '2026-10-26'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://www.lawpay.com/llm-info/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: LawPay provides payment processing solutions tailored for legal professionals, offering secure, compliant, and IOLTA‑ready credit card, debit, and eCheck transactions. Founded in 2005, LawPay serves over 50,000 law firms, integrating with practice management software and supporting online billing, recurring payments, and mobile apps. The platform emphasizes data security, fraud protection, and seamless client experiences, helping attorneys focus on their practice rather than payment logistics.
image: https://www.lawpay.com/asset-og-lawpay-default.webp
json_schemas:
- name: DeleteInvoicesInvoiceidAttachmentsAttachmentidResponse
  property_count: 21
  slug: lawpay-delete-invoices-invoiceid-attachments-attachmentid-response
- name: GetBankAccountsBankaccountidSurchargeResponse
  property_count: 6
  slug: lawpay-get-bank-accounts-bankaccountid-surcharge-response
- name: GetInvoicesInvoiceidResponse
  property_count: 21
  slug: lawpay-get-invoices-invoiceid-response
- name: PatchInvoicesInvoiceidResponse
  property_count: 22
  slug: lawpay-patch-invoices-invoiceid-response
- name: PostContactsContactidMakePaymentResponse
  property_count: 24
  slug: lawpay-post-contacts-contactid-make-payment-response
- name: PostMerchantApplicationsSignUpRequest
  property_count: 35
  slug: lawpay-post-merchant-applications-sign-up-request
jsonld:
- class_count: 99
  name: Lawpay Context
  property_count: 173
  slug: lawpay-context
layout: provider
modified: '2026-10-26'
name: LawPay
nav: Providers
network: true
overview: 'LawPay is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, LegalTech, FinTech, and SaaS.


  The LawPay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LawPay''s developer surface includes getting-started guide, engineering blog, documentation, support, pricing, and 20 more developer resources.'
plans:
- name: Lawpay Plans Pricing
  plan_count: 1
  slug: lawpay-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: LawPay API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: lawpay-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 21
      marker_coverage: 100.0
      total: 21
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lawpay Domain Security
  slug: lawpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lawpay
tags:
- Company
- Payments
- LegalTech
- FinTech
- SaaS
website: https://www.lawpay.com/
---
