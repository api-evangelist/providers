---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 99
  human_in_the_loop: 4
  name: Lynx Agentic Access
  operation_count: 180
  slug: lynx-agentic-access
  summary_line: 180 operations · 99 acting · 4 human-in-the-loop
api_count: 18
apis:
- description: 'Lynx FinHealth API for embedded health accounts, enrollment, contributions, payments and distributions, transactions, and card issuance/management. Reference is gated behind developer login; a hosted '
  name: Lynx API
  slug: lynx-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Investments API from Lynx — 20 operation(s) for investments.
  name: Lynx Investments API
  slug: lynx-investments-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Tags API from Lynx — 2 operation(s) for tags.
  name: Lynx Tags API
  slug: lynx-tags-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Accounts API from Lynx — 9 operation(s) for accounts.
  name: Lynx Accounts API
  slug: lynx-accounts-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Cards API from Lynx — 14 operation(s) for cards.
  name: Lynx Cards API
  slug: lynx-cards-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Claims API from Lynx — 3 operation(s) for claims.
  name: Lynx Claims API
  slug: lynx-claims-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The client-org-application-token-controller API from Lynx — 1 operation(s) for client-org-application-token-controller.
  name: Lynx Client Org Application Token Controller API
  slug: lynx-client-org-application-token-controller-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Clients API from Lynx — 5 operation(s) for clients.
  name: Lynx Clients API
  slug: lynx-clients-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Commerce API from Lynx — 23 operation(s) for commerce.
  name: Lynx Commerce API
  slug: lynx-commerce-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Copay API from Lynx — 2 operation(s) for copay.
  name: Lynx Copay API
  slug: lynx-copay-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Enrollments API from Lynx — 3 operation(s) for enrollments.
  name: Lynx Enrollments API
  slug: lynx-enrollments-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Expense API from Lynx — 1 operation(s) for expense.
  name: Lynx Expense API
  slug: lynx-expense-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Externalaccounts API from Lynx — 6 operation(s) for externalaccounts.
  name: Lynx Externalaccounts API
  slug: lynx-externalaccounts-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Externalnotifications API from Lynx — 7 operation(s) for externalnotifications.
  name: Lynx Externalnotifications API
  slug: lynx-externalnotifications-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The member-expense-controller API from Lynx — 4 operation(s) for member-expense-controller.
  name: Lynx Member Expense Controller API
  slug: lynx-member-expense-controller-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Members API from Lynx — 8 operation(s) for members.
  name: Lynx Members API
  slug: lynx-members-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Payments API from Lynx — 11 operation(s) for payments.
  name: Lynx Payments API
  slug: lynx-payments-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Relatedpersons API from Lynx — 7 operation(s) for relatedpersons.
  name: Lynx Relatedpersons API
  slug: lynx-relatedpersons-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Substantiation API from Lynx — 5 operation(s) for substantiation.
  name: Lynx Substantiation API
  slug: lynx-substantiation-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Transactions API from Lynx — 13 operation(s) for transactions.
  name: Lynx Transactions API
  slug: lynx-transactions-api
- baseURL: https://sandbox.lynx-fh.co
  baseurl_source: declared
  description: The Uploads API from Lynx — 2 operation(s) for uploads.
  name: Lynx Uploads API
  slug: lynx-uploads-api
artifact_total: 86
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/agentic-access/lynx-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lynx-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/rules/lynx-rules.yml
  title: ''
  type: Spectral
  url: rules/lynx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/json-ld/lynx-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lynx-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/vocabulary/lynx-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lynx-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/data-model/lynx-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lynx-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/lifecycle/lynx-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/lynx-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/errors/lynx-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lynx-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/hosts/lynx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lynx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/vendors/lynx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lynx-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.lynx-fh.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/authentication/lynx-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lynx-authentication.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lynx-fh.com/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://lynx-fh.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lynx-fh.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lynx-fh.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lynx-fh.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lynx-fh.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lynx-fh.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lynx-fh.com/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.lynx-fh.co/client-ui/
- group: start
  title: ''
  type: SignUp
  url: https://www.lynx-fh.com/request-lynx-api-access
- group: operate
  title: ''
  type: Support
  url: https://www.lynx-fh.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.lynx-fh.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lynx-fh.com/website-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lynx-fh.com/website-terms-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://www.lynx-fh.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/conformance/lynx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lynx-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/lifecycle/lynx-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lynx-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/changelog/lynx-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lynx-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/sandbox/lynx-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lynx-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/security/lynx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lynx-domain-security.yml
created: '2026-07-17'
description: Lynx (Lynx FinHealth) is a healthcare fintech platform that provides embedded banking, payments, benefits, and e-commerce infrastructure for health plans, providers, and digital health companies. Its API-first and white-label platform powers consumer-directed health accounts (HSA/FSA), ICHRA administration, directed and filtered spend accounts, instant physical and virtual card issuance with merchant and SKU-level controls, supplemental benefits, pharmacy access, rewards and incentive programs, and a qualified medical expense (QME) e-commerce marketplace with end-to-end fulfillment. Lynx is SOC 2 and HITRUST certified and exposes a developer hub, dated changelog, hosted sandbox, and Atlassian status page. Surfaced as a portfolio company of Obvious Ventures and enriched from the public Lynx surface (the full API reference, authentication model, and test data are gated behind developer login).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lynx.png
json_schemas:
- name: AdHocNotificationRequest
  property_count: 2
  slug: lynx-ad-hoc-notification-request
- name: BaseMemberResponse
  property_count: 2
  slug: lynx-base-member-response
- name: CalculateSalesTaxResponse
  property_count: 5
  slug: lynx-calculate-sales-tax-response
- name: CardStatusChangeRequest
  property_count: 2
  slug: lynx-card-status-change-request
- name: ClientOrgApplicationTokenRequestDoc
  property_count: 2
  slug: lynx-client-org-application-token-request-doc
- name: ClientOrgApplicationTokenResponse
  property_count: 4
  slug: lynx-client-org-application-token-response
- name: ClientOrgExclusionListRequest
  property_count: 2
  slug: lynx-client-org-exclusion-list-request
- name: ClientOrgNotificationConfigurationData
  property_count: 16
  slug: lynx-client-org-notification-configuration-data
- name: ClientOrgNotificationConfigurationResponse
  property_count: 2
  slug: lynx-client-org-notification-configuration-response
- name: ClientOrgRequest
  property_count: 2
  slug: lynx-client-org-request
- name: ClientOrgSubscribedEventsRequest
  property_count: 2
  slug: lynx-client-org-subscribed-events-request
- name: ClientOrgSubstantiationModelDto
  property_count: 11
  slug: lynx-client-org-substantiation-model-dto
- name: ClientOrgSubstantiationModelRequest
  property_count: 2
  slug: lynx-client-org-substantiation-model-request
- name: CommerceCatalogFacetsResponse
  property_count: 2
  slug: lynx-commerce-catalog-facets-response
- name: CommerceCommodityListDocModelResponse
  property_count: 3
  slug: lynx-commerce-commodity-list-doc-model-response
- name: CopayCreateResponse
  property_count: 2
  slug: lynx-copay-create-response
- name: CopayGroupGetDetail
  property_count: 2
  slug: lynx-copay-group-get-detail
- name: DocClientOrgCopayGroupCreateRequest
  property_count: 2
  slug: lynx-doc-client-org-copay-group-create-request
- name: DocClientOrgCopayGroupEditRequest
  property_count: 2
  slug: lynx-doc-client-org-copay-group-edit-request
- name: DocCopayGroupGetRequest
  property_count: 2
  slug: lynx-doc-copay-group-get-request
- name: DocCreateClientOrgExternalBankAccountRequest
  property_count: 2
  slug: lynx-doc-create-client-org-external-bank-account-request
- name: DocLinkAccountRequest
  property_count: 2
  slug: lynx-doc-link-account-request
- name: DocMemberBankAccountRequest
  property_count: 2
  slug: lynx-doc-member-bank-account-request
- name: DocMemberBankAccountRequestVerified
  property_count: 2
  slug: lynx-doc-member-bank-account-request-verified
- name: DocPostDependentCardRequest
  property_count: 2
  slug: lynx-doc-post-dependent-card-request
- name: DocUpdateBankAccountRequest
  property_count: 2
  slug: lynx-doc-update-bank-account-request
- name: GetAccountPerformanceResponse
  property_count: 6
  slug: lynx-get-account-performance-response
- name: GetAccountPositionsResponse
  property_count: 6
  slug: lynx-get-account-positions-response
- name: GetClaimDetailResponse
  property_count: 1
  slug: lynx-get-claim-detail-response
- name: GetClaimsResponse
  property_count: 2
  slug: lynx-get-claims-response
- name: GetClientOrgBankAccountBalanceResponse
  property_count: 2
  slug: lynx-get-client-org-bank-account-balance-response
- name: GetClientOrgExclusionList
  property_count: 2
  slug: lynx-get-client-org-exclusion-list
- name: GetCommodityDetailDocModelResponse
  property_count: 2
  slug: lynx-get-commodity-detail-doc-model-response
- name: GetMemberAccountBalanceResponse
  property_count: 3
  slug: lynx-get-member-account-balance-response
- name: GetMemberAccountTransferResponse
  property_count: 3
  slug: lynx-get-member-account-transfer-response
- name: GetMemberCardsResponse
  property_count: 3
  slug: lynx-get-member-cards-response
- name: GetMemberEnrollmentsByClientResponse
  property_count: 2
  slug: lynx-get-member-enrollments-by-client-response
- name: GetMemberExternalAccountsResponse
  property_count: 3
  slug: lynx-get-member-external-accounts-response
- name: MemberAccountStatusRequest
  property_count: 2
  slug: lynx-member-account-status-request
- name: MemberCardRequest
  property_count: 2
  slug: lynx-member-card-request
- name: MemberRequest
  property_count: 2
  slug: lynx-member-request
- name: MemberViewCommerceClassificationDto
  property_count: 9
  slug: lynx-member-view-commerce-classification-dto
- name: PatchClientOrgNotificationConfigurationRequest
  property_count: 2
  slug: lynx-patch-client-org-notification-configuration-request
- name: PatchClientOrgSubstantiationModelResponse
  property_count: 2
  slug: lynx-patch-client-org-substantiation-model-response
- name: PatchMemberAccountRequestDoc
  property_count: 2
  slug: lynx-patch-member-account-request-doc
- name: PatchMemberEnrollmentRequestDoc
  property_count: 2
  slug: lynx-patch-member-enrollment-request-doc
- name: PatchMemberEnrollmentResponseDoc
  property_count: 2
  slug: lynx-patch-member-enrollment-response-doc
- name: PatchMemberNotificationStatusRequest
  property_count: 2
  slug: lynx-patch-member-notification-status-request
- name: PersistClaimsResponse
  property_count: 2
  slug: lynx-persist-claims-response
- name: PostClientOrgNotificationConfigurationRequest
  property_count: 2
  slug: lynx-post-client-org-notification-configuration-request
- name: PostEcommerceRefundRequest
  property_count: 2
  slug: lynx-post-ecommerce-refund-request
- name: PostMemberAccountTransferRequest
  property_count: 2
  slug: lynx-post-member-account-transfer-request
- name: PostMemberClaimRequest
  property_count: 2
  slug: lynx-post-member-claim-request
- name: PostMemberEcommerceOrderRequestDoc
  property_count: 2
  slug: lynx-post-member-ecommerce-order-request-doc
- name: PostReplaceEcommerceOrderRequest
  property_count: 2
  slug: lynx-post-replace-ecommerce-order-request
- name: PutCommerceSalesTaxRequest
  property_count: 2
  slug: lynx-put-commerce-sales-tax-request
- name: PutMemberClaimRequest
  property_count: 2
  slug: lynx-put-member-claim-request
- name: ReissueCardRequestDoc
  property_count: 2
  slug: lynx-reissue-card-request-doc
- name: ReplaceCardRequestDoc
  property_count: 2
  slug: lynx-replace-card-request-doc
- name: ValidateCouponRequest
  property_count: 2
  slug: lynx-validate-coupon-request
jsonld:
- class_count: 120
  name: Lynx Context
  property_count: 223
  slug: lynx-context
layout: provider
modified: '2026-10-06'
name: Lynx
nav: Providers
network: true
overview: 'Lynx publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Investments API, Tags API, Accounts API, and 18 more. Tagged areas include Company, Healthcare, Fintech, Payments, and Benefits.


  The Lynx catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Lynx''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, sandbox, signup flow, and 24 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: Lynx API Rules
  rule_count: 18
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 7
  slug: lynx-rules
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.8
  facets:
    access_clarity: 42.1
    contract_governance: 35.6
    contract_quality: 66.0
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 31.6
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/lynx/refs/heads/main/screenshots/lynx-2026-07-25T225752.png
security:
- kind: authentication
  name: Lynx Authentication
  slug: lynx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lynx Domain Security
  slug: lynx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lynx
tags:
- Company
- Healthcare
- Fintech
- Payments
- Benefits
- Health Savings Accounts
- Embedded Finance
- Card Issuing
- Insurance
website: https://lynx-fh.com
---
