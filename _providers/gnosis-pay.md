---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Gnosis Pay Agentic Access
  operation_count: 44
  slug: gnosis-pay-agentic-access
  summary_line: 44 operations · 22 acting
api_count: 1
apis:
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Auth API from Gnosis Pay — 5 operation(s) for auth.
  name: Gnosis Pay Auth API
  slug: gnosis-pay-auth-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Cards API from Gnosis Pay — 6 operation(s) for cards.
  name: Gnosis Pay Cards API
  slug: gnosis-pay-cards-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Health API from Gnosis Pay — 1 operation(s) for health.
  name: Gnosis Pay Health API
  slug: gnosis-pay-health-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The KYC API from Gnosis Pay — 1 operation(s) for kyc.
  name: Gnosis Pay KYC API
  slug: gnosis-pay-kyc-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The PCI API from Gnosis Pay — 4 operation(s) for pci.
  name: Gnosis Pay PCI API
  slug: gnosis-pay-pci-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Phone API from Gnosis Pay — 2 operation(s) for phone.
  name: Gnosis Pay Phone API
  slug: gnosis-pay-phone-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Source of Funds API from Gnosis Pay — 1 operation(s) for source of funds.
  name: Gnosis Pay Source of Funds API
  slug: gnosis-pay-source-of-funds-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The Terms API from Gnosis Pay — 2 operation(s) for terms.
  name: Gnosis Pay Terms API
  slug: gnosis-pay-terms-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The User Account API from Gnosis Pay — 2 operation(s) for user account.
  name: Gnosis Pay User Account API
  slug: gnosis-pay-user-account-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The User API from Gnosis Pay — 2 operation(s) for user.
  name: Gnosis Pay User API
  slug: gnosis-pay-user-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The User Movements API from Gnosis Pay — 5 operation(s) for user movements.
  name: Gnosis Pay User Movements API
  slug: gnosis-pay-user-movements-api
- baseURL: https://core.prod.gnosispay.com/user-api
  baseurl_source: declared
  description: The 3 DS API from Gnosis Pay — 4 operation(s) for 3 ds.
  name: Gnosis Pay 3 DS API
  slug: gnosis-pay-3-ds-api
artifact_total: 28
asyncapis:
- description: ''
  name: Gnosis Pay Webhooks
  slug: gnosis-pay-webhooks
common:
- group: other
  href: https://artifacts.apis.io/gnosis-pay/vendors/gnosis-pay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gnosis-pay-vendors.yml
- group: agent
  href: https://artifacts.apis.io/gnosis-pay/agentic-access/gnosis-pay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gnosis-pay-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/rules/gnosis-pay-rules.yml
  title: ''
  type: Spectral
  url: rules/gnosis-pay-rules.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/json-ld/gnosis-pay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gnosis-pay-context.jsonld
- group: design
  href: https://artifacts.apis.io/gnosis-pay/vocabulary/gnosis-pay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gnosis-pay-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gnosis-pay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/asyncapi/gnosis-pay-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gnosis-pay-webhooks.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/data-model/gnosis-pay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gnosis-pay-data-model.yml
- group: start
  href: https://artifacts.apis.io/gnosis-pay/sandbox/gnosis-pay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gnosis-pay-sandbox.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/errors/gnosis-pay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gnosis-pay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gnosis-pay/conformance/gnosis-pay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gnosis-pay-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gnosis-pay/llms/gnosis-pay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gnosis-pay-llms.txt
- group: other
  href: https://artifacts.apis.io/gnosis-pay/a2a/gnosis-pay-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gnosis-pay-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gnosis-pay/well-known/gnosis-pay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gnosis-pay-well-known.yml
- group: other
  href: https://artifacts.apis.io/gnosis-pay/hosts/gnosis-pay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gnosis-pay-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://help.gnosispay.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gnosispay.com/
- group: company
  title: ''
  type: Newsroom
  url: https://gnosispay.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gnosispay.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gnosispay.com/guides/onboarding
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gnosispay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gnosispay.com/api-reference/auth/get-siwe-message
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gnosispay
- group: auth
  href: https://artifacts.apis.io/gnosis-pay/authentication/gnosis-pay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gnosis-pay-authentication.yml
- group: auth
  href: https://artifacts.apis.io/gnosis-pay/security/gnosis-pay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gnosis-pay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gnosispay.com/
- group: company
  title: ''
  type: Blog
  url: https://gnosispay.com/blog
created: '2026-10-27'
description: Gnosis Pay is a decentralized payments network that removes the barriers between traditional finance and decentralized finance. It enables stablecoin‑backed card programs, seamless on‑ramp and off‑ramp solutions, and provides APIs for merchants and developers to integrate crypto payments, manage wallets, and comply with regulatory standards across multiple jurisdictions.
image: https://framerusercontent.com/assets/fjGAFaeqps5ZhiChsXMozeemvc.png
json_schemas:
- name: AccountLimit
  property_count: 7
  slug: gnosis-pay-account-limit
- name: Account
  property_count: 14
  slug: gnosis-pay-account
- name: GetUserResponse
  property_count: 9
  slug: gnosis-pay-get-user-response
- name: OnboardingStatus
  property_count: 0
  slug: gnosis-pay-onboarding-status
- name: PciChallengeResponse
  property_count: 4
  slug: gnosis-pay-pci-challenge-response
- name: PciPublicKeyResponse
  property_count: 2
  slug: gnosis-pay-pci-public-key-response
jsonld:
- class_count: 120
  name: Gnosis Pay Context
  property_count: 93
  slug: gnosis-pay-context
layout: provider
modified: '2026-10-27'
name: Gnosis Pay
nav: Providers
network: true
overview: 'Gnosis Pay publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Cards API, Health API, and 9 more. Tagged areas include Company, Payments, Crypto, Stablecoin, and API.


  The Gnosis Pay catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Gnosis Pay''s developer surface includes sandbox, support, changelog, getting-started guide, documentation, API reference, authentication, and 20 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Gnosis Pay API Rules
  rule_count: 15
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 4
  slug: gnosis-pay-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 70.9
    developer_ergonomics: 56.5
    discoverability: 67.9
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gnosis Pay Authentication
  slug: gnosis-pay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gnosis Pay Domain Security
  slug: gnosis-pay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: gnosis-pay-create-virtual-card-and-list-cards
  slug: gnosis-pay-create-virtual-card-and-list-cards
- name: gnosis-pay-register-and-fetch-user
  slug: gnosis-pay-register-and-fetch-user
- name: gnosis-pay-source-of-funds
  slug: gnosis-pay-source-of-funds
- name: gnosis-pay-user-movements-overview
  slug: gnosis-pay-user-movements-overview
slug: gnosis-pay
tags:
- Company
- Payments
- Crypto
- Stablecoin
- API
website: https://gnosispay.com/
---
