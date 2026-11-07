---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The AZION v4 REST API.
  name: Azion API
  slug: azion-api
- baseURL: https://api.azion.com/v4
  baseurl_source: declared
  description: The AZION v4 REST API.
  name: azion-api API
  slug: azion-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: Azion Webhooks
  slug: azion-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/azion/well-known/azion-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/azion-status-security.txt
- group: design
  href: https://artifacts.apis.io/azion/rules/azion-rules.yml
  title: ''
  type: Spectral
  url: rules/azion-rules.yml
- group: design
  href: https://artifacts.apis.io/azion/json-ld/azion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/azion-context.jsonld
- group: design
  href: https://artifacts.apis.io/azion/vocabulary/azion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/azion-vocabulary.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.azion.com/en/documentation/agreements/tos/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.azion.com/en/documentation/agent-setup/
- group: docs
  title: ''
  type: APIReference
  url: https://www.azion.com/llms.txt
- group: operate
  href: https://artifacts.apis.io/azion/rate-limits/azion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/azion-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/azion/plans/azion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/azion-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/azion/asyncapi/azion-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/azion-webhooks.yml
- group: design
  href: https://artifacts.apis.io/azion/data-model/azion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/azion-data-model.yml
- group: build
  href: https://artifacts.apis.io/azion/cli/azion-cli.yml
  title: ''
  type: CLI
  url: cli/azion-cli.yml
- group: operate
  href: https://artifacts.apis.io/azion/changelog/azion-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/azion-changelog.yml
- group: auth
  href: https://artifacts.apis.io/azion/authentication/azion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/azion-authentication.yml
- group: design
  href: https://artifacts.apis.io/azion/errors/azion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/azion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/azion/conformance/azion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/azion-conformance.yml
- group: agent
  href: https://artifacts.apis.io/azion/llms/azion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/azion-llms.txt
- group: agent
  href: https://artifacts.apis.io/azion/well-known/azion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/azion-well-known.yml
- group: other
  href: https://artifacts.apis.io/azion/hosts/azion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/azion-hosts.yml
- group: build
  href: https://artifacts.apis.io/azion/packages/azion-packages.yml
  title: ''
  type: SDKs
  url: packages/azion-packages.yml
- group: build
  href: https://artifacts.apis.io/azion/packages/azion-packages.yml
  title: ''
  type: Packages
  url: packages/azion-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azion.com/
- group: auth
  title: ''
  type: Security
  url: https://www.azion.com/en/solutions/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.azion.com/en/documentation/changelog/
- group: auth
  href: https://artifacts.apis.io/azion/security/azion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/azion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.azion.com/en/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.azion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.azion.com/en/documentation/
- group: operate
  title: ''
  type: Support
  url: https://www.azion.com/en/support/
- group: company
  title: ''
  type: Blog
  url: https://www.azion.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aziontech
- group: commercial
  title: ''
  type: Pricing
  url: https://www.azion.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.azion.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.azion.com/en/documentation/agreements/privacy-policy/
created: '2026-10-19'
description: Azion provides an edge computing platform that enables developers to deploy serverless functions, AI inference, and other compute workloads close to users worldwide. Their solutions include edge functions, durable objects, load balancer, AI gateway, object storage, and security services, all managed via a unified console. Azion serves enterprises across various industries, offering performance, scalability, and security at the edge.
image: https://anp9wamula0.map.azionedge.net/?title=Azion%20Web%20Platform&subtitle=Azion%20enables%20you%20to%20build%2C%20protect%2C%20and%20scale%20applications%20everywhere.&type=dotGrid
json_schemas:
- name: CertificateRequest
  property_count: 23
  slug: azion-certificate-request
- name: Certificate
  property_count: 20
  slug: azion-certificate
- name: CertificateSigningRequest
  property_count: 28
  slug: azion-certificate-signing-request
- name: PatchedCertificate
  property_count: 20
  slug: azion-patched-certificate
- name: PatchedWAFRuleRequest
  property_count: 6
  slug: azion-patched-wafrule-request
- name: WAFRuleRequest
  property_count: 6
  slug: azion-wafrule-request
jsonld:
- class_count: 120
  name: Azion Context
  property_count: 97
  slug: azion-context
layout: provider
modified: '2026-10-19'
name: Azion
nav: Providers
network: true
overview: 'Azion publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including azion-api API, and 1 more. Tagged areas include Edge Computing, Serverless, Artificial Intelligence, Cloud Infrastructure, and Platform.


  The Azion catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Azion''s developer surface includes getting-started guide, API reference, CLI, changelog, authentication, documentation, support, and 27 more developer resources.'
plans:
- name: Azion Plans Pricing
  plan_count: 4
  slug: azion-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Azion Rate Limits
  slug: azion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 111
  extends:
  - spectral:oas
  name: Azion API Rules
  rule_count: 70
  severity_counts:
    error: 51
    hint: 0
    info: 6
    warn: 13
  slug: azion-rules
score:
  band: strong
  composite: 56.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.1
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 71.4
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 70.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/azion/azion-2026-11-03T121519.png
security:
- kind: authentication
  name: Azion Authentication
  slug: azion-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Azion Domain Security
  slug: azion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azion
tags:
- Edge Computing
- Serverless
- Artificial Intelligence
- Cloud Infrastructure
- Platform
website: https://www.azion.com/en/
---
