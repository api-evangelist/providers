---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'fineconomy API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: fineconomy API
  slug: banksapi-api
artifact_total: 13
common:
- group: auth
  href: https://artifacts.apis.io/banksapi/well-known/banksapi-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/banksapi-status-security.txt
- group: design
  href: https://artifacts.apis.io/banksapi/rules/banksapi-rules.yml
  title: ''
  type: Spectral
  url: rules/banksapi-rules.yml
- group: design
  href: https://artifacts.apis.io/banksapi/json-ld/banksapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/banksapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/banksapi/vocabulary/banksapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/banksapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/banksapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/banksapi/data-model/banksapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/banksapi-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://banksapi.de/en/security/
- group: auth
  href: https://artifacts.apis.io/banksapi/authentication/banksapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/banksapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/banksapi/conformance/banksapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/banksapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/banksapi/llms/banksapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/banksapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/banksapi/well-known/banksapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/banksapi-well-known.yml
- group: other
  href: https://artifacts.apis.io/banksapi/hosts/banksapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/banksapi-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.banksapi.de/
- group: auth
  title: ''
  type: Security
  url: https://banksapi.de/en/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BANKSapi
- group: auth
  href: https://artifacts.apis.io/banksapi/scopes/banksapi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/banksapi-scopes.yml
- group: auth
  href: https://artifacts.apis.io/banksapi/security/banksapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/banksapi-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/banksapi/security/banksapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/banksapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://banksapi.de/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.banksapi.de/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.banksapi.de/guide/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.banksapi.de/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.banksapi.de/guide/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://banksapi.de/testzugang/
created: '2026-10-20'
description: 'BANKSapi verbindet Ihre Anwendung per API mit über 3.000 Banken: Kontodaten, SEPA-Zahlungen, Pay by Bank und Datenanalysen – PSD2-Lizenz inklusive. Das Unternehmen bietet umfassende Banking‑APIs für Kontoinformationen, Zahlungsinitiierung, Datenanalyse und Frontend‑Integration, unterstützt von einer PSD2‑Lizenz und richtet sich an Entwickler, FinTech‑Startups und etablierte Banken, die digitale Services skalieren wollen.'
image: https://banksapi.de/wp-content/themes/banksapi/img/social/og-default-de.jpg
json_schemas:
- name: GetCustomerV2AiAffinitiesHideResponse
  property_count: 2
  slug: banksapi-get-customer-v2-ai-affinities-hide-response
- name: GetCustomerV2AiDisposableMoneyReturnsResponse
  property_count: 12
  slug: banksapi-get-customer-v2-ai-disposable-money-returns-response
- name: GetCustomerV2AiSalesTriggersReturnsResponse
  property_count: 9
  slug: banksapi-get-customer-v2-ai-sales-triggers-returns-response
- name: GetCustomerV2AiTaggingRulesPlaygroundResponse
  property_count: 5
  slug: banksapi-get-customer-v2-ai-tagging-rules-playground-response
- name: PutCustomerV2BankzugaengeAccessidProductidKontoumsaetzeTrans
  property_count: 1
  slug: banksapi-put-customer-v2-bankzugaenge-accessid-productid-kontoumsaetze-trans
- name: PutCustomerV2BankzugaengeAccessidProductidKontoumsaetzeTrans2
  property_count: 1
  slug: banksapi-put-customer-v2-bankzugaenge-accessid-productid-kontoumsaetze-trans2
jsonld:
- class_count: 12
  name: Banksapi Context
  property_count: 31
  slug: banksapi-context
layout: provider
modified: '2026-10-20'
name: fineconomy
nav: Providers
network: true
overview: 'fineconomy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Banking, Fintech, Payments, and Data Analytics.


  The fineconomy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fineconomy''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: fineconomy API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: banksapi-rules
scopes:
- name: Banksapi Scopes
  scope_count: 5
  slug: banksapi-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 39.8
    discoverability: 55.4
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/banksapi/banksapi-2026-11-03T121624.png
security:
- kind: authentication
  name: Banksapi Authentication
  slug: banksapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Banksapi Domain Security
  slug: banksapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Banksapi Trust Center
  slug: banksapi-trust-center
  summary_line: ISO 27001, GDPR
slug: banksapi
tags:
- Banking
- Fintech
- Payments
- Data Analytics
website: https://banksapi.de/
---
