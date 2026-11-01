---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Itau Unibanco Agentic Access
  operation_count: 17
  slug: itau-unibanco-agentic-access
  summary_line: 17 operations
api_count: 16
apis:
- description: 'Itaú''s corporate API catalog on Itaú for Developers: Pix receipts and payments, payment initiation, payroll-deductible credit (consignado), credit recovery, collateral lookup, treasury bank cash suppl'
  name: Itaú for Developers Corporate APIs
  slug: corporate-apis
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem de contas.
  name: Itaú Unibanco Accounts API
  slug: itau-unibanco-accounts-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem de canais de atendimento
  name: Itaú Unibanco Channels API
  slug: itau-unibanco-channels-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem de cartões de crédito.
  name: Itaú Unibanco Credit Cards API
  slug: itau-unibanco-credit-cards-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: The Discovery API from Itaú Unibanco — 2 operation(s) for discovery.
  name: Itaú Unibanco Discovery API
  slug: itau-unibanco-discovery-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem financiamentos
  name: Itaú Unibanco Financings API
  slug: itau-unibanco-financings-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem de Direitos Creditórios Descontados.
  name: Itaú Unibanco Invoice Financings API
  slug: itau-unibanco-invoice-financings-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: Operações para listagem empréstimos
  name: Itaú Unibanco Loans API
  slug: itau-unibanco-loans-api
- baseURL: https://api.itau/open-banking/channels/v2
  baseurl_source: declared
  description: The Unarranged Account Overdraft API from Itaú Unibanco — 2 operation(s) for unarranged account overdraft.
  name: Itaú Unibanco Unarranged Account Overdraft API
  slug: itau-unibanco-unarranged-account-overdraft-api
artifact_total: 38
common:
- group: agent
  href: https://artifacts.apis.io/itau-unibanco/agentic-access/itau-unibanco-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/itau-unibanco-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/rules/itau-unibanco-rules.yml
  title: ''
  type: Spectral
  url: rules/itau-unibanco-rules.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/json-ld/itau-unibanco-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/itau-unibanco-context.jsonld
- group: design
  href: https://artifacts.apis.io/itau-unibanco/vocabulary/itau-unibanco-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/itau-unibanco-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/itau-unibanco/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/data-model/itau-unibanco-data-model.yml
  title: ''
  type: DataModel
  url: data-model/itau-unibanco-data-model.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/conventions/itau-unibanco-conventions.yml
  title: ''
  type: Conventions
  url: conventions/itau-unibanco-conventions.yml
- group: start
  href: https://artifacts.apis.io/itau-unibanco/sandbox/itau-unibanco-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/itau-unibanco-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/itau-unibanco/lifecycle/itau-unibanco-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/itau-unibanco-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://devportal.itau.com.br/nossas-apis/openfinance
- group: design
  href: https://artifacts.apis.io/itau-unibanco/lifecycle/itau-unibanco-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/itau-unibanco-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/errors/itau-unibanco-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/itau-unibanco-problem-types.yml
- group: design
  href: https://artifacts.apis.io/itau-unibanco/conformance/itau-unibanco-conformance.yml
  title: ''
  type: Conformance
  url: conformance/itau-unibanco-conformance.yml
- group: other
  href: https://artifacts.apis.io/itau-unibanco/overlays/itau-unibanco-open-finance-channels-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/itau-unibanco-open-finance-channels-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/itau-unibanco/llms/itau-unibanco-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/itau-unibanco-llms.txt
- group: other
  href: https://artifacts.apis.io/itau-unibanco/hosts/itau-unibanco-hosts.yml
  title: ''
  type: Hosts
  url: hosts/itau-unibanco-hosts.yml
- group: other
  href: https://artifacts.apis.io/itau-unibanco/vendors/itau-unibanco-vendors.yml
  title: ''
  type: Vendors
  url: vendors/itau-unibanco-vendors.yml
- group: auth
  href: https://artifacts.apis.io/itau-unibanco/authentication/itau-unibanco-authentication.yml
  title: ''
  type: Authentication
  url: authentication/itau-unibanco-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.itau.com.br
- group: auth
  href: https://artifacts.apis.io/itau-unibanco/security/itau-unibanco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/itau-unibanco-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.itau.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://devportal.itau.com.br/conheca-o-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://devportal.itau.com.br/como-se-conectar-as-apis-itau
- group: operate
  title: ''
  type: Support
  url: https://devportal.itau.com.br/suportefaq
- group: start
  title: ''
  type: SignUp
  url: https://devportal.itau.com.br/baas/#/create-account/personal-information
- group: start
  title: ''
  type: Login
  url: https://devportal.itau.com.br/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devportal.itau.com.br/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devportal.itau.com.br/politicas
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/itau
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/itau
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/itau
created: '2026-10-18'
description: Itaú Unibanco Holding S.A. (CNPJ 60.872.504/0001-23, São Paulo, Brazil) is Brazil's largest private bank, describing itself as the largest bank in Latin America. Through its developer portal, Itaú for Developers (devportal.itau.com.br), it offers companies APIs for Pix receipts and payments, payment initiation, payroll-deductible credit (consignado), credit recovery, collateral lookup, treasury bank cash supply, third-party fund custody, foreign exchange and trade, plus Open Finance and managed file transfer, with a sandbox environment, self-registration and getting-started guides covering credentials and dynamic certificates.
image: https://avatars.githubusercontent.com/u/74078611?v=4
json_schemas:
- name: BusinessCreditCardResponse
  property_count: 3
  slug: itau-unibanco-business-credit-card-response
- name: PersonalCreditCardResponse
  property_count: 3
  slug: itau-unibanco-personal-credit-card-response
- name: ResponseBankingAgentsList
  property_count: 3
  slug: itau-unibanco-response-banking-agents-list
- name: ResponseBranchesList
  property_count: 3
  slug: itau-unibanco-response-branches-list
- name: ResponseBusinessAccounts
  property_count: 3
  slug: itau-unibanco-response-business-accounts
- name: ResponseBusinessFinancings
  property_count: 3
  slug: itau-unibanco-response-business-financings
- name: ResponseBusinessInvoiceFinancings
  property_count: 3
  slug: itau-unibanco-response-business-invoice-financings
- name: ResponseBusinessLoans
  property_count: 3
  slug: itau-unibanco-response-business-loans
- name: ResponseBusinessUnarrangedAccountOverdraft
  property_count: 3
  slug: itau-unibanco-response-business-unarranged-account-overdraft
- name: ResponseDiscoveryOutageList
  property_count: 3
  slug: itau-unibanco-response-discovery-outage-list
- name: ResponseDiscoveryStatusList
  property_count: 3
  slug: itau-unibanco-response-discovery-status-list
- name: ResponseElectronicChannelsList
  property_count: 3
  slug: itau-unibanco-response-electronic-channels-list
- name: ResponsePersonalAccounts
  property_count: 3
  slug: itau-unibanco-response-personal-accounts
- name: ResponsePersonalFinancings
  property_count: 3
  slug: itau-unibanco-response-personal-financings
- name: ResponsePersonalLoans
  property_count: 3
  slug: itau-unibanco-response-personal-loans
- name: ResponsePersonalUnarrangedAccountOverdraft
  property_count: 3
  slug: itau-unibanco-response-personal-unarranged-account-overdraft
- name: ResponsePhoneChannelsList
  property_count: 3
  slug: itau-unibanco-response-phone-channels-list
jsonld:
- class_count: 119
  name: Itau Unibanco Context
  property_count: 101
  slug: itau-unibanco-context
layout: provider
modified: '2026-10-18'
name: Itaú Unibanco
nav: Providers
network: true
overview: 'Itaú Unibanco publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Channels API, Credit Cards API, and 6 more. Tagged areas include Company, Banking, Financial Services, Payments, and Pix.


  The Itaú Unibanco catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Itaú Unibanco''s developer surface includes sandbox, authentication, documentation, getting-started guide, support, signup flow, YouTube channel, and 24 more developer resources.'
plans:
- name: Itau Unibanco Plans Pricing
  plan_count: 0
  slug: itau-unibanco-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Itau Unibanco Rate Limits
  slug: itau-unibanco-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Itaú Unibanco API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: itau-unibanco-rules
scopes:
- name: Itau Unibanco Scopes
  scope_count: 0
  slug: itau-unibanco-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 56.5
    discoverability: 71.4
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
    score: 33.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Itau Unibanco Authentication
  slug: itau-unibanco-authentication
  summary_line: apiKey/oauth2/mtls · 2 schemes
- kind: domain-security
  name: Itau Unibanco Domain Security
  slug: itau-unibanco-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: itau-unibanco-check-api-status
  slug: itau-unibanco-check-api-status
- name: itau-unibanco-compare-account-products
  slug: itau-unibanco-compare-account-products
- name: itau-unibanco-compare-credit-products
  slug: itau-unibanco-compare-credit-products
- name: itau-unibanco-find-service-channels
  slug: itau-unibanco-find-service-channels
slug: itau-unibanco
tags:
- Company
- Banking
- Financial Services
- Payments
- Pix
- Open Finance
- Brazil
- Foreign Exchange
- Credit
website: https://www.itau.com.br
---
