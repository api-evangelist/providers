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
  score: 25.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: BankID Relying Party API for authentication and signing
  name: Relying Party API
  slug: relying-party-api
- description: Verify ID card from BankID
  name: ID Card Verification API
  slug: id-card-verification-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Auth API from BankID — 1 operation(s) for auth.
  name: BankID Auth API
  slug: bankid-auth-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Cancel API from BankID — 1 operation(s) for cancel.
  name: BankID Cancel API
  slug: bankid-cancel-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Collect API from BankID — 1 operation(s) for collect.
  name: BankID Collect API
  slug: bankid-collect-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Other API from BankID — 1 operation(s) for other.
  name: BankID Other API
  slug: bankid-other-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Payment API from BankID — 2 operation(s) for payment.
  name: BankID Payment API
  slug: bankid-payment-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Phone API from BankID — 4 operation(s) for phone.
  name: BankID Phone API
  slug: bankid-phone-api
- baseURL: https://appapi2.bankid.com/rp/v6.0
  baseurl_source: declared
  description: The Sign API from BankID — 1 operation(s) for sign.
  name: BankID Sign API
  slug: bankid-sign-api
artifact_total: 18
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/rules/bankid-rules.yml
  title: ''
  type: Spectral
  url: rules/bankid-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/json-ld/bankid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bankid-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/vocabulary/bankid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bankid-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/conformance/bankid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bankid-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/data-model/bankid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bankid-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/errors/bankid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bankid-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/llms/bankid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bankid-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankid-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankid-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankid-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankid-developers-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bankid-app-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/well-known/bankid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bankid-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/hosts/bankid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bankid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/vendors/bankid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bankid-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/packages/bankid-packages.yml
  title: ''
  type: SDKs
  url: packages/bankid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/packages/bankid-packages.yml
  title: ''
  type: Packages
  url: packages/bankid-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bankid.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bankid.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bankid.com/getting-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bankid.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BankID
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bankid/refs/heads/main/security/bankid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bankid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bankid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bankid.com/om-oss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankid.com/juridik/integritetspolicy-bankid
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankid.com/juridik/integritetspolicy-finansiell-id-teknik
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://status.bankid.com/mcp
  - status: 200
    url: https://bankid.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: BankID provides a digital identification and signing solution used widely across Sweden for secure online authentication and electronic signatures. It enables banks, government services, and private enterprises to verify user identities and authorize transactions through a mobile app and web integrations, supporting strong customer authentication and compliance with eIDAS standards. The platform offers APIs for developers to integrate BankID verification, signing, and user flow management into their applications, facilitating seamless and secure digital interactions.
image: https://www.bankid.com/assets/stock/press-material/bankid_start02-lo.jpg
json_schemas:
- name: auth_request
  property_count: 9
  slug: bankid-auth-request
- name: collect_response
  property_count: 4
  slug: bankid-collect-response
- name: otherPayment_request
  property_count: 11
  slug: bankid-other-payment-request
- name: paymentBulk_request
  property_count: 9
  slug: bankid-payment-bulk-request
- name: payment_request
  property_count: 11
  slug: bankid-payment-request
- name: sign_request
  property_count: 9
  slug: bankid-sign-request
jsonld:
- class_count: 38
  name: Bankid Context
  property_count: 51
  slug: bankid-context
layout: provider
modified: '2026-10-15'
name: BankID
nav: Providers
network: true
overview: 'BankID publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Cancel API, Collect API, and 6 more. Tagged areas include Company, Authentication, eIDAS, Digital Identity, and Sweden.


  The BankID catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BankID''s developer surface includes getting-started guide, API reference, documentation, and 24 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: BankID API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: bankid-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 61.1
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bankid Domain Security
  slug: bankid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bankid
tags:
- Company
- Authentication
- eIDAS
- Digital Identity
- Sweden
website: https://www.bankid.com/
---
