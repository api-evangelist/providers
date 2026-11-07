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
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Signalr Agentic Access
  operation_count: 7
  slug: microsoft-azure-signalr-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure SignalR Service Operations API
  slug: microsoft-azure-signalr-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: SignalR operations
  name: Azure SignalR Service SignalR API
  slug: microsoft-azure-signalr-signalr-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The general API from Azure SignalR Service — 1 operation(s) for general.
  name: Azure SignalR Service General API
  slug: microsoft-azure-signalr-general-api
artifact_total: 20
collections:
- collection_type: open
  name: Azure SignalR Service REST Operations API
  slug: open-microsoft-azure-signalr-operations-api
- collection_type: open
  name: Azure Service REST Operations SignalR API
  slug: open-microsoft-azure-signalr-signalr-api
- collection_type: open
  name: Azure SignalR Service REST API
  slug: open-microsoft-azure-signalr
common:
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/windows/blog/windows-itpro-blog
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/rules/microsoft-azure-signalr-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-signalr-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/json-ld/microsoft-azure-signalr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-signalr-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/vocabulary/microsoft-azure-signalr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-signalr-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-signalr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/data-model/microsoft-azure-signalr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-signalr-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-signalr/cli/microsoft-azure-signalr-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-signalr-cli.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-signalr/changelog/microsoft-azure-signalr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-signalr-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/conventions/microsoft-azure-signalr-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-signalr-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/conventions/microsoft-azure-signalr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-signalr-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-reference-data-plane-rest-api
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/lifecycle/microsoft-azure-signalr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-signalr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/errors/microsoft-azure-signalr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-signalr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-signalr/conformance/microsoft-azure-signalr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-signalr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-signalr/llms/microsoft-azure-signalr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-signalr-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/well-known/microsoft-azure-signalr-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-signalr-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-signalr/well-known/microsoft-azure-signalr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-signalr-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-signalr/hosts/microsoft-azure-signalr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-signalr-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-signalr/vendors/microsoft-azure-signalr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-signalr-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-signalr/packages/microsoft-azure-signalr-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-signalr-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-signalr/packages/microsoft-azure-signalr-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-signalr-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://techcommunity.microsoft.com/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/security/microsoft-azure-signalr-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-signalr-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/security/microsoft-azure-signalr-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-signalr-vulnerability-disclosure.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-signalr/rate-limits/microsoft-azure-signalr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-signalr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-signalr/finops/microsoft-azure-signalr-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-signalr-finops.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-signalr/plans/microsoft-azure-signalr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-signalr-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: other
  href: https://artifacts.apis.io/microsoft-azure-signalr/capabilities/microsoft-azure-signalr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-signalr-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-signalr/agentic-access/microsoft-azure-signalr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-signalr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/security/microsoft-azure-signalr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-signalr-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/authentication/microsoft-azure-signalr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-signalr-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-signalr/scopes/microsoft-azure-signalr-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-signalr-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/signalr-service/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-signalr/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-signalr/signalr-quickstart-azure-signalr-service-arm-template
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/azure-signalr
created: '2026-03-13'
description: Azure SignalR Service REST API enables management of real-time web communication services. It supports creating SignalR instances, managing connections, sending messages to clients and groups, and configuring upstream endpoints for serverless real-time messaging.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Signalr Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-signalr-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-signalr.png
json_schemas:
- name: OperationList
  property_count: 2
  slug: microsoft-azure-signalr-operation-list
jsonld:
- class_count: 3
  name: Microsoft Azure Signalr Context
  property_count: 6
  slug: microsoft-azure-signalr-context
layout: provider
modified: '2026-09-16'
name: Azure SignalR Service
nav: Providers
network: true
overview: 'Azure SignalR Service publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Operations API, SignalR API, and General API. Tagged areas include Real-Time, WebSocket, SignalR, Messaging, and Push.


  The Azure SignalR Service catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure SignalR Service''s developer surface includes engineering blog, CLI, changelog, authentication, developer portal, pricing, documentation, and 39 more developer resources.'
plans:
- name: Microsoft Azure Signalr Plans Pricing
  plan_count: 3
  slug: microsoft-azure-signalr-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 8
  name: Microsoft Azure Signalr Rate Limits
  slug: microsoft-azure-signalr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Azure SignalR Service API Rules
  rule_count: 39
  severity_counts:
    error: 34
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-signalr-rules
scopes:
- name: Microsoft Azure Signalr Scopes
  scope_count: 1
  slug: microsoft-azure-signalr-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 67.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 77.2
    catalog_earned_first_party: 24.0
    catalog_gap: 37.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 17.4
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 44.3
    developer_ergonomics: 64.9
    discoverability: 82.1
    operational_transparency: 84.2
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-signalr/microsoft-azure-signalr-2026-06-20T185437.png
security:
- kind: authentication
  name: Microsoft Azure Signalr Authentication
  slug: microsoft-azure-signalr-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Signalr Domain Security
  slug: microsoft-azure-signalr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Signalr Vulnerability Disclosure
  slug: microsoft-azure-signalr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Signalr Trust Center
  slug: microsoft-azure-signalr-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: provision-signalr-instance
  slug: microsoft-azure-signalr-provision-instance
- name: send-signalr-messages
  slug: microsoft-azure-signalr-send-messages
slug: microsoft-azure-signalr
tags:
- Real-Time
- WebSocket
- SignalR
- Messaging
- Push
website: https://microsoft.com
---
