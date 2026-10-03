---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Backbase Agentic Access
  operation_count: 26
  slug: backbase-agentic-access
  summary_line: 26 operations · 12 acting
api_count: 2
apis:
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: Payment approval API.
  name: BackBase Approve API
  slug: backbase-approve-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: The bbt API from BackBase — 1 operation(s) for bbt.
  name: BackBase Bbt API
  slug: backbase-bbt-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: The patch API from BackBase — 1 operation(s) for patch.
  name: BackBase Patch API
  slug: backbase-patch-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: Core payments API.
  name: BackBase Payment Orders API
  slug: backbase-payment-orders-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: The test API from BackBase — 4 operation(s) for test.
  name: BackBase Test API
  slug: backbase-test-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: Utility endpoints.
  name: BackBase Utility API
  slug: backbase-utility-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: Validation of a payment.
  name: BackBase Validate API
  slug: backbase-validate-api
- baseURL: https://api.backbase.com
  baseurl_source: declared
  description: The wallet API from BackBase — 2 operation(s) for wallet.
  name: BackBase Wallet API
  slug: backbase-wallet-api
artifact_total: 25
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/agentic-access/backbase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/backbase-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/rules/backbase-rules.yml
  title: ''
  type: Spectral
  url: rules/backbase-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/json-ld/backbase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/backbase-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/vocabulary/backbase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/backbase-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/data-model/backbase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/backbase-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/errors/backbase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/backbase-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/conformance/backbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/backbase-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/overlays/backbase-payment-order-client-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/backbase-payment-order-client-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/llms/backbase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/backbase-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/hosts/backbase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backbase-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/vendors/backbase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backbase-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/packages/backbase-packages.yml
  title: ''
  type: SDKs
  url: packages/backbase-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/packages/backbase-packages.yml
  title: ''
  type: Packages
  url: packages/backbase-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.backbase.com/about/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backbase.com/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.backbase.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://www.backbase.com/insight/guides
- group: company
  title: ''
  type: Blog
  url: https://www.backbase.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.backbase.com/blog/agentic-onboarding-commercial-banking
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Backbase
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/security/backbase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/backbase-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/backbase/refs/heads/main/security/backbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backbase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.backbase.com
created: '2026-09-27'
description: BackBase provides an AI-native Banking Operating System that enables banks to deliver digital experiences, integrate open banking, and accelerate product innovation. The platform offers modular components for customer engagement, core banking, risk management, and marketplace extensions, helping financial institutions modernize their services and improve operational efficiency.
image: https://cdn.prod.website-files.com/688b633d00cf5931b997219b/69e897c9dfa32eb11c5bb807_Open%20Graph.jpg
json_schemas:
- name: BbtBuild-infoGetGetResponseBody
  property_count: 1
  slug: backbase-bbt-build-info-get-get-response-body
- name: BulkPaymentOrdersApprovalPutResponse
  property_count: 5
  slug: backbase-bulk-payment-orders-approval-put-response
- name: DateQueryParamGetResponseBody
  property_count: 14
  slug: backbase-date-query-param-get-response-body
- name: PaymentCard
  property_count: 10
  slug: backbase-payment-card
- name: PaymentCardsPostResponseBody
  property_count: 1
  slug: backbase-payment-cards-post-response-body
- name: PaymentOrderGet
  property_count: 32
  slug: backbase-payment-order-get-response
- name: PaymentOrdersPostResponse
  property_count: 13
  slug: backbase-payment-orders-post-response
- name: InitiatePaymentOrder
  property_count: 10
  slug: backbase-payment-orders-post
- name: PaymentOrdersValidatePostResponse
  property_count: 17
  slug: backbase-payment-orders-validate-post-response
- name: InitiatePaymentOrder
  property_count: 10
  slug: backbase-payment-orders-validate-post
- name: TestHeadersResponseBody
  property_count: 1
  slug: backbase-test-headers-response-body
- name: TestValuesGetResponseBody
  property_count: 2
  slug: backbase-test-values-get-response-body
jsonld:
- class_count: 71
  name: Backbase Context
  property_count: 138
  slug: backbase-context
layout: provider
modified: '2026-09-27'
name: BackBase
nav: Providers
network: true
overview: 'BackBase publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Approve API, Bbt API, Patch API, and 5 more. Tagged areas include Banking, Fintech, Digital Banking, API Platform, and AI-Native.


  The BackBase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BackBase''s developer surface includes documentation, engineering blog, getting-started guide, and 21 more developer resources.'
random_paper: 20
rules:
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: BackBase API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: backbase-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.6
    developer_ergonomics: 32.7
    discoverability: 75.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 16.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Backbase Domain Security
  slug: backbase-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Backbase Vulnerability Disclosure
  slug: backbase-vulnerability-disclosure
  summary_line: security.txt
slug: backbase
tags:
- Banking
- Fintech
- Digital Banking
- API Platform
- AI-Native
website: https://www.backbase.com
---
