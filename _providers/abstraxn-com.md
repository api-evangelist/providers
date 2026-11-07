---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Abstraxn provides AI‑driven Web3 infrastructure with wallet integration, account abstraction, and agent tools. Documentation is at docs.abstraxn.com.
  name: Abstraxn API
  slug: abstraxn-api
- baseURL: https://agent-kit.abstraxn.com
  baseurl_source: declared
  description: 'Abstraxn ai API as documented publicly: 27 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Abstraxn ai API
  slug: ai-api
- baseURL: https://agent-kit.abstraxn.com
  baseurl_source: declared
  description: 'Abstraxn kyi API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Abstraxn kyi API
  slug: kyi-api
- baseURL: https://agent-kit.abstraxn.com
  baseurl_source: declared
  description: 'Abstraxn wallets API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Abstraxn wallets API
  slug: wallets-api
artifact_total: 25
common:
- group: commercial
  href: https://artifacts.apis.io/abstraxn-com/plans/abstraxn-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/abstraxn-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/abstraxn-com/rules/abstraxn-com-rules.yml
  title: ''
  type: Spectral
  url: rules/abstraxn-com-rules.yml
- group: design
  href: https://artifacts.apis.io/abstraxn-com/json-ld/abstraxn-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/abstraxn-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/abstraxn-com/vocabulary/abstraxn-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abstraxn-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/abstraxn-com/data-model/abstraxn-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/abstraxn-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/abstraxn-com/cli/abstraxn-com-cli.yml
  title: ''
  type: CLI
  url: cli/abstraxn-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/abstraxn-com/authentication/abstraxn-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abstraxn-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/abstraxn-com/conformance/abstraxn-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abstraxn-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abstraxn-com/llms/abstraxn-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abstraxn-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/abstraxn-com/well-known/abstraxn-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abstraxn-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/abstraxn-com/hosts/abstraxn-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abstraxn-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/abstraxn-com/vendors/abstraxn-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abstraxn-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/abstraxn-com/packages/abstraxn-com-packages.yml
  title: ''
  type: SDKs
  url: packages/abstraxn-com-packages.yml
- group: build
  href: https://artifacts.apis.io/abstraxn-com/packages/abstraxn-com-packages.yml
  title: ''
  type: Packages
  url: packages/abstraxn-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abstraxn.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abstraxn.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Abstraxn-Labs
- group: auth
  href: https://artifacts.apis.io/abstraxn-com/security/abstraxn-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abstraxn-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abstraxn.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.abstraxn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abstraxn.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.abstraxn.com/guides/getting-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://abstraxn.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://abstraxn.com/blogs
coverage:
  checked: '2026-10-31'
  detail: Documentation is publicly available but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found on any discovered host.
  evidence:
  - status: 200
    url: https://dashboard.abstraxn.com/openapi.json
  - status: 200
    url: https://dashboard.abstraxn.com/asyncapi.yaml
  - status: 200
    url: https://dashboard.abstraxn.com/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Abstraxn provides AI agent infrastructure, offering identity verification, embedded wallets, payment processing, and KYI policy controls that enable businesses to let autonomous agents act and spend safely. The platform combines account abstraction, ERC-4337 smart accounts, and developer tools to deliver secure, programmable agentic commerce solutions for the Web3 ecosystem.
image: https://obs-cdn.abstraxn.com/abstraxn/og-image.png
json_schemas:
- name: GetAgentIdRegistrationResponse
  property_count: 7
  slug: abstraxn-com-get-agent-id-registration-response
- name: GetAgentsAgentidPoliciesResponse
  property_count: 2
  slug: abstraxn-com-get-agents-agentid-policies-response
- name: GetKeysReceiptResponse
  property_count: 1
  slug: abstraxn-com-get-keys-receipt-response
- name: GetReceiptsReceiptidResponse
  property_count: 1
  slug: abstraxn-com-get-receipts-receiptid-response
- name: PatchAgentsAgentidPoliciesPolicyidRequest
  property_count: 3
  slug: abstraxn-com-patch-agents-agentid-policies-policyid-request
- name: PatchAgentsIdRequest
  property_count: 2
  slug: abstraxn-com-patch-agents-id-request
- name: PostAgentsAgentidPoliciesRequest
  property_count: 4
  slug: abstraxn-com-post-agents-agentid-policies-request
- name: PostAgentsIdRegisterIdentityResponse
  property_count: 2
  slug: abstraxn-com-post-agents-id-register-identity-response
- name: PostAuthCreateRequest
  property_count: 4
  slug: abstraxn-com-post-auth-create-request
- name: PostAuthCreateResponse
  property_count: 6
  slug: abstraxn-com-post-auth-create-response
- name: PostAuthExchangeRequest
  property_count: 4
  slug: abstraxn-com-post-auth-exchange-request
- name: PostAuthExchangeResponse
  property_count: 6
  slug: abstraxn-com-post-auth-exchange-response
- name: PostDecisionsRequest
  property_count: 4
  slug: abstraxn-com-post-decisions-request
- name: PostDecisionsResponse
  property_count: 5
  slug: abstraxn-com-post-decisions-response
- name: PostMandatesRequest
  property_count: 4
  slug: abstraxn-com-post-mandates-request
- name: PostMandatesResponse
  property_count: 3
  slug: abstraxn-com-post-mandates-response
jsonld:
- class_count: 21
  name: Abstraxn Com Context
  property_count: 40
  slug: abstraxn-com-context
layout: provider
modified: '2026-10-31'
name: Abstraxn
nav: Providers
network: true
overview: 'Abstraxn is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including ai API, kyi API, wallets API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Payments, Identity, and Wallets.


  The Abstraxn catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Abstraxn''s developer surface includes CLI, authentication, documentation, getting-started guide, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Abstraxn Com Plans Pricing
  plan_count: 4
  slug: abstraxn-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Abstraxn API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 1
  slug: abstraxn-com-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 42.9
    discoverability: 62.5
    operational_transparency: 2.6
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Abstraxn Com Authentication
  slug: abstraxn-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Abstraxn Com Domain Security
  slug: abstraxn-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abstraxn-com
tags:
- Artificial Intelligence
- Agents
- Payments
- Identity
- Wallets
- Web3
- Technology
website: https://abstraxn.com/
---
