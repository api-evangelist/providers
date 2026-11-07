---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Bastion Agentic Access
  operation_count: 7
  slug: microsoft-azure-bastion-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Bastion Hosts operations
  name: Azure Bastion Hosts API
  slug: microsoft-azure-bastion-bastion-hosts-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Azure Bastion Operations API
  slug: microsoft-azure-bastion-operations-api
artifact_total: 19
collections:
- collection_type: open
  name: Azure Bastion REST Bastion Hosts API
  slug: open-microsoft-azure-bastion-bastion-hosts-api
- collection_type: open
  name: Azure Bastion REST Bastion Hosts Operations API
  slug: open-microsoft-azure-bastion-operations-api
- collection_type: open
  name: Azure Bastion REST API
  slug: open-microsoft-azure-bastion
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/rules/microsoft-azure-bastion-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-bastion-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/json-ld/microsoft-azure-bastion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-bastion-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/vocabulary/microsoft-azure-bastion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-bastion-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/data-model/microsoft-azure-bastion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-bastion-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-bastion/cli/microsoft-azure-bastion-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-bastion-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/errors/microsoft-azure-bastion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-bastion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-bastion/conformance/microsoft-azure-bastion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-bastion-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-bastion/llms/microsoft-azure-bastion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-bastion-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/well-known/microsoft-azure-bastion-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-bastion-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-bastion/well-known/microsoft-azure-bastion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-bastion-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-bastion/hosts/microsoft-azure-bastion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-bastion-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-bastion/vendors/microsoft-azure-bastion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-bastion-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-bastion/packages/microsoft-azure-bastion-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-bastion-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-bastion/packages/microsoft-azure-bastion-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-bastion-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/security/microsoft-azure-bastion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-bastion-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/security/microsoft-azure-bastion-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-bastion-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-bastion/plans/microsoft-azure-bastion-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-bastion-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-bastion/rate-limits/microsoft-azure-bastion-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-bastion-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-bastion/finops/microsoft-azure-bastion-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-bastion-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-bastion/agentic-access/microsoft-azure-bastion-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-bastion-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/security/microsoft-azure-bastion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-bastion-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/authentication/microsoft-azure-bastion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-bastion-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-bastion/scopes/microsoft-azure-bastion-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-bastion-scopes.yml
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
  url: https://azure.microsoft.com/en-us/pricing/
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
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/bastion/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/azure-bastion/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/bastion-hosts
created: '2026-03-13'
description: Learn more about [Virtual Networks Bastion Hosts Operations]. How to [Create Or Update,Delete,Get,List,List By Resource Group,Update Tags].
finops:
- has_sources: false
  method: generated
  name: Microsoft Azure Bastion Finops
  primary_unit: request
  service_category: API
  slug: microsoft-azure-bastion-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-bastion.png
json_schemas:
- name: OperationList
  property_count: 2
  slug: microsoft-azure-bastion-operation-list
- name: ResourceList
  property_count: 2
  slug: microsoft-azure-bastion-resource-list
- name: Resource
  property_count: 6
  slug: microsoft-azure-bastion-resource
jsonld:
- class_count: 5
  name: Microsoft Azure Bastion Context
  property_count: 11
  slug: microsoft-azure-bastion-context
layout: provider
modified: '2026-09-16'
name: Azure Bastion
nav: Providers
network: true
overview: 'Azure Bastion is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Hosts API and Operations API. Tagged areas include Bastion, RDP, Remote Access, Secure Access, and SSH.


  The Azure Bastion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Azure Bastion''s developer surface includes CLI, changelog, getting-started guide, authentication, developer portal, pricing, support, and 33 more developer resources.'
plans:
- name: Microsoft Azure Bastion Plans Pricing
  plan_count: 3
  slug: microsoft-azure-bastion-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Microsoft Azure Bastion Rate Limits
  slug: microsoft-azure-bastion-rate-limits
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Azure Bastion API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-azure-bastion-rules
scopes:
- name: Microsoft Azure Bastion Scopes
  scope_count: 1
  slug: microsoft-azure-bastion-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.2
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 71.4
    discoverability: 66.1
    operational_transparency: 36.8
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
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
screenshot: https://apis.io/screenshots/microsoft-azure-bastion/microsoft-azure-bastion-2026-06-20T185400.png
security:
- kind: authentication
  name: Microsoft Azure Bastion Authentication
  slug: microsoft-azure-bastion-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Bastion Domain Security
  slug: microsoft-azure-bastion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Bastion Vulnerability Disclosure
  slug: microsoft-azure-bastion-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Bastion Trust Center
  slug: microsoft-azure-bastion-trust-center
  summary_line: GDPR
slug: microsoft-azure-bastion
tags:
- Bastion
- RDP
- Remote Access
- Secure Access
- SSH
website: https://www.microsoft.com/
---
