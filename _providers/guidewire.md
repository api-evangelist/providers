---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Guidewire Agentic Access
  operation_count: 15
  slug: guidewire-agentic-access
  summary_line: 15 operations · 5 acting
api_count: 2
apis:
- description: The Guidewire BillingCenter API provides REST endpoints for payment orchestration, invoice generation, payment plans, disbursements, and collections management for insurance billing operations.
  name: Guidewire BillingCenter API
  slug: guidewire-billingcenter-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: The Guidewire Integration Gateway provides a managed API layer for connecting Guidewire Cloud applications to third-party systems, enabling event-driven integrations and REST API extensions for the Gu
  name: Guidewire Integration Gateway API
  slug: guidewire-integration-gateway-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Customer account management
  name: Guidewire Accounts API
  slug: guidewire-accounts-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Claims lifecycle management
  name: Guidewire Claims API
  slug: guidewire-claims-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Claim exposure management
  name: Guidewire Exposures API
  slug: guidewire-exposures-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: First Notice of Loss intake
  name: Guidewire FNOL API
  slug: guidewire-fnol-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Claim payment and reserves
  name: Guidewire Payments API
  slug: guidewire-payments-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Policy lifecycle management
  name: Guidewire Policies API
  slug: guidewire-policies-api
- baseURL: https://{applicationURL}/rest
  baseurl_source: declared
  description: Policy quoting and rating
  name: Guidewire Quotes API
  slug: guidewire-quotes-api
artifact_total: 34
asyncapis:
- description: Guidewire Integration Gateway AsyncAPI specification for event-driven integrations. The gateway publishes webhook events when key policy, claim, and billing lifecycle events occur in Guidewire Cloud a
  name: Guidewire Integration Gateway Events
  slug: guidewire-integration-gateway-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Guidewire ClaimCenter Accounts API
  slug: open-guidewire-accounts-api
- collection_type: open
  name: Guidewire ClaimCenter API
  slug: open-guidewire-claimcenter
- collection_type: open
  name: Guidewire ClaimCenter Accounts Claims API
  slug: open-guidewire-claims-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Exposures API
  slug: open-guidewire-exposures-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts FNOL API
  slug: open-guidewire-fnol-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Payments API
  slug: open-guidewire-payments-api
- collection_type: open
  name: Guidewire ClaimCenter Accounts Policies API
  slug: open-guidewire-policies-api
- collection_type: open
  name: Guidewire PolicyCenter API
  slug: open-guidewire-policycenter
- collection_type: open
  name: Guidewire ClaimCenter Accounts Quotes API
  slug: open-guidewire-quotes-api
common:
- group: start
  title: ''
  type: SignUp
  url: https://www.guidewire.com/sign-in
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.guidewire.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/agentic-access/guidewire-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/guidewire-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/security/guidewire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guidewire-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/authentication/guidewire-authentication.yml
  title: ''
  type: Authentication
  url: authentication/guidewire-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/conventions/guidewire-conventions.yml
  title: ''
  type: Conventions
  url: conventions/guidewire-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/conventions/guidewire-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/guidewire-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/lifecycle/guidewire-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/guidewire-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/changelog/guidewire-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/guidewire-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/conformance/guidewire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/guidewire-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/conformance/guidewire-conformance.yml
  title: ''
  type: Compliance
  url: conformance/guidewire-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/security/guidewire-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/guidewire-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/security/guidewire-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/guidewire-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/security/guidewire-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/guidewire-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/errors/guidewire-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/guidewire-error-codes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/packages/guidewire-packages.yml
  title: ''
  type: Packages
  url: packages/guidewire-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/well-known/guidewire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/guidewire-well-known.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/rate-limits/guidewire-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/guidewire-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/plans/guidewire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/guidewire-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/finops/guidewire-finops.yml
  title: ''
  type: FinOps
  url: finops/guidewire-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Portal
  url: https://www.guidewire.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.guidewire.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.guidewire.com/developers
- group: operate
  title: ''
  type: StatusPage
  url: https://status.guidewire.com/
- group: operate
  title: ''
  type: Support
  url: https://community.guidewire.com/
- group: company
  title: ''
  type: Blog
  url: https://www.guidewire.com/resources/blog
- group: company
  title: ''
  type: Website
  url: https://www.guidewire.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.guidewire.com/cloud/cc/202607/apiref/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.guidewire.com/developers/apis
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.guidewire.com/legal-notices
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.guidewire.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.guidewire.com/sign-in
- group: build
  title: ''
  type: Developer Tools
  url: https://marketplace.guidewire.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guidewire-oss
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/openapi/_original/guidewire-policycenter-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/guidewire-policycenter-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/openapi/_original/guidewire-claimcenter-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/guidewire-claimcenter-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/json-schema/guidewire-policy-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/guidewire-policy-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/json-ld/guidewire-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/guidewire-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/asyncapi/guidewire-integration-gateway-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/guidewire-integration-gateway-asyncapi.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guidewire-software
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/llms/guidewire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/guidewire-llms.txt
created: '2026-05-01'
description: Guidewire provides the insurance industry's leading platform including PolicyCenter, ClaimCenter, and BillingCenter. REST APIs enable policy lifecycle management, claims processing, payment orchestration, and underwriting workflows for P&C insurance carriers on the Guidewire Cloud platform.
finops:
- name: Guidewire Finops
  service_category: Insurance Platform / SaaS
  slug: guidewire-finops
graphqls:
- description: Guidewire is a cloud platform for property and casualty insurance covering policy administration, billing, and claims management. The API covers policies, quotes, billing accounts, claims, payments, a
  name: Guidewire GraphQL API
  slug: guidewire-graphql
image: screenshots/guidewire-2026-06-20T182433.png
json_schemas:
- name: Guidewire Policy
  property_count: 14
  slug: guidewire-policy
jsonld:
- class_count: 11
  name: Guidewire Context
  property_count: 17
  slug: guidewire-context
layout: provider
modified: '2026-09-12'
name: Guidewire
nav: Providers
network: true
overview: 'Guidewire publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Integration Gateway API, Accounts API, Claims API, and 5 more. Tagged areas include Insurance, Policy, Claims, Billing, and P&C.


  The Guidewire catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Guidewire''s developer surface includes signup flow, authentication, changelog, developer portal, documentation, getting-started guide, support, and 35 more developer resources.'
plans:
- name: Guidewire Plans Pricing
  plan_count: 1
  slug: guidewire-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Guidewire Rate Limits
  slug: guidewire-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Guidewire API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: guidewire-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Guidewire API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: guidewire-jsonschema-spectral-rules
scopes:
- name: Guidewire Scopes
  scope_count: 0
  slug: guidewire-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 70.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 71.5
    catalog_earned_first_party: 16.0
    catalog_gap: 43.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 70.2
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 65.8
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/guidewire/refs/heads/main/screenshots/guidewire-2026-06-20T182433.png
security:
- kind: authentication
  name: Guidewire Authentication
  slug: guidewire-authentication
  summary_line: http-basic/bearer-jwt · 2 schemes
- kind: domain-security
  name: Guidewire Domain Security
  slug: guidewire-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Guidewire Vulnerability Disclosure
  slug: guidewire-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Guidewire Trust Center
  slug: guidewire-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, PCI DSS
slug: guidewire
tags:
- Insurance
- Policy
- Claims
- Billing
- P&C
website: https://www.guidewire.com/
---
