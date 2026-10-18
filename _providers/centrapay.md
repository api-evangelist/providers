---
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Centrapay Agentic Access
  operation_count: 16
  slug: centrapay-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://service.centrapay.com
  baseurl_source: declared
  description: The payment-requests API from Centrapay — 16 operation(s) for payment-requests.
  name: Centrapay Payment Requests API
  slug: centrapay-payment-requests-api
artifact_total: 11
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/agentic-access/centrapay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/centrapay-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/rate-limits/centrapay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/centrapay-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/rules/centrapay-rules.yml
  title: ''
  type: Spectral
  url: rules/centrapay-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/rules/centrapay-centrapay-docs-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/centrapay-centrapay-docs-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/json-ld/centrapay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centrapay-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/vocabulary/centrapay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centrapay-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/data-model/centrapay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centrapay-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/components/centrapay-components.yml
  title: ''
  type: Components
  url: components/centrapay-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/conventions/centrapay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/centrapay-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/conventions/centrapay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/centrapay-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/sandbox/centrapay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/centrapay-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/scopes/centrapay-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/centrapay-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/lifecycle/centrapay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/centrapay-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/errors/centrapay-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/centrapay-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/errors/centrapay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/centrapay-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/conformance/centrapay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centrapay-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/overlays/centrapay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/centrapay-openapi-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/hosts/centrapay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centrapay-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/vendors/centrapay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centrapay-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/packages/centrapay-packages.yml
  title: ''
  type: SDKs
  url: packages/centrapay-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/packages/centrapay-packages.yml
  title: ''
  type: Packages
  url: packages/centrapay-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/authentication/centrapay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/centrapay-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/security/centrapay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centrapay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.centrapay.com/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/centrapay/centrapay-docs/blob/636b5947eae1c8b9a6ce2f827bb32daba981b1b3/.spectral.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.centrapay.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.centrapay.com/api/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.centrapay.com/guides/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/centrapay
- group: operate
  title: ''
  type: Support
  url: https://www.centrapay.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.centrapay.com/
- group: company
  title: ''
  type: Blog
  url: https://www.centrapay.com/blog/nz-tech-expo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.centrapay.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.centrapay.com/legal/privacy-policy
created: '2026-10-09'
description: Centrapay is a payments network that connects existing commerce systems (point-of-sale terminals and checkouts) to digital wallets, tokens and low-cost alternative payments. Its API-first infrastructure lets merchants accept Payap, bank transfers via Open Banking and QR-code rails, brand loyalty points and digital gift cards, bypassing traditional card-network fees. Developers integrate through the Centrapay REST API documented at docs.centrapay.com.
image: https://framerusercontent.com/images/KVxxaI7Lvpyui2d4eS31RH11vZQ.png
jsonld:
- class_count: 1
  name: Centrapay Context
  property_count: 1
  slug: centrapay-context
layout: provider
modified: '2026-10-09'
name: Centrapay
nav: Providers
network: true
overview: 'Centrapay publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Payment Requests API. Tagged areas include Company, Payments, Digital Wallet, Open Banking, and QR Code Payments.


  The Centrapay catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Centrapay''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Centrapay Plans Pricing
  plan_count: 0
  slug: centrapay-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Centrapay Rate Limits
  slug: centrapay-rate-limits
rules:
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: Centrapay — centrapay docs rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: centrapay-centrapay-docs-spectral-rules
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Centrapay API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: centrapay-rules
scopes:
- name: Centrapay Scopes
  scope_count: 4
  slug: centrapay-scopes
  summary_line: 4 scopes
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 51.8
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 53.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/centrapay/refs/heads/main/screenshots/centrapay-2026-10-11T103022.png
security:
- kind: authentication
  name: Centrapay Authentication
  slug: centrapay-authentication
  summary_line: apiKey/openIdConnect · 2 schemes
- kind: domain-security
  name: Centrapay Domain Security
  slug: centrapay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: centrapay-e-commerce-integration
  slug: centrapay-e-commerce-integration
slug: centrapay
tags:
- Company
- Payments
- Digital Wallet
- Open Banking
- QR Code Payments
- Loyalty
- Gift Cards
- Fintech
website: https://www.centrapay.com/
---
