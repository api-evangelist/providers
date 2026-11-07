---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Advisor Agentic Access
  operation_count: 7
  slug: microsoft-azure-advisor-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: Microsoft Azure Advisor Operations API
  slug: microsoft-azure-advisor-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Recommendations operations
  name: Microsoft Azure Advisor Recommendations API
  slug: microsoft-azure-advisor-recommendations-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The AdvisorScoreEntities API from Microsoft Azure Advisor — 2 operation(s) for advisorscoreentities.
  name: Microsoft Azure Advisor Advisor Score Entities API
  slug: microsoft-azure-advisor-advisorscoreentities-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The MetadataEntities API from Microsoft Azure Advisor — 2 operation(s) for metadataentities.
  name: Microsoft Azure Advisor Metadata Entities API
  slug: microsoft-azure-advisor-metadataentities-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ResiliencyReviews API from Microsoft Azure Advisor — 2 operation(s) for resiliencyreviews.
  name: Microsoft Azure Advisor Resiliency Reviews API
  slug: microsoft-azure-advisor-resiliencyreviews-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The ResourceRecommendationBases API from Microsoft Azure Advisor — 3 operation(s) for resourcerecommendationbases.
  name: Microsoft Azure Advisor Resource Recommendation Bases API
  slug: microsoft-azure-advisor-resourcerecommendationbases-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Advisor — 8 operation(s) for subscriptions.
  name: Microsoft Azure Advisor Subscriptions API
  slug: microsoft-azure-advisor-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The SuppressionContracts API from Microsoft Azure Advisor — 1 operation(s) for suppressioncontracts.
  name: Microsoft Azure Advisor Suppression Contracts API
  slug: microsoft-azure-advisor-suppressioncontracts-api
artifact_total: 25
collections:
- collection_type: open
  name: Azure Advisor REST Operations API
  slug: open-microsoft-azure-advisor-operations-api
- collection_type: open
  name: Azure Advisor REST Operations Recommendations API
  slug: open-microsoft-azure-advisor-recommendations-api
- collection_type: open
  name: Azure Advisor REST API
  slug: open-microsoft-azure-advisor
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/rules/microsoft-azure-advisor-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-advisor-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/json-ld/microsoft-azure-advisor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-advisor-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/vocabulary/microsoft-azure-advisor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-advisor-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/data-model/microsoft-azure-advisor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-advisor-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-advisor/cli/microsoft-azure-advisor-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-advisor-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/conventions/microsoft-azure-advisor-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-advisor-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/errors/microsoft-azure-advisor-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-advisor-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-advisor/conformance/microsoft-azure-advisor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-advisor-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-advisor/llms/microsoft-azure-advisor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-advisor-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/well-known/microsoft-azure-advisor-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-advisor-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-advisor/well-known/microsoft-azure-advisor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-advisor-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-advisor/hosts/microsoft-azure-advisor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-advisor-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-advisor/vendors/microsoft-azure-advisor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-advisor-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-advisor/packages/microsoft-azure-advisor-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-advisor-packages.yml
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
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/azuredevcommunityblog
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/security/microsoft-azure-advisor-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-advisor-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/security/microsoft-azure-advisor-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-advisor-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-advisor/plans/microsoft-azure-advisor-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-advisor-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-advisor/rate-limits/microsoft-azure-advisor-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-advisor-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-advisor/finops/microsoft-azure-advisor-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-advisor-finops.yml
- group: company
  title: ''
  type: Website
  url: https://microsoft.com
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-advisor/agentic-access/microsoft-azure-advisor-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-advisor-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/security/microsoft-azure-advisor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-advisor-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/authentication/microsoft-azure-advisor-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-advisor-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-advisor/scopes/microsoft-azure-advisor-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-advisor-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/advisor/
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
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
created: '2026-03-13'
description: Microsoft Azure Advisor is a personalized cloud consultant that helps you follow best practices to optimize your Azure deployments. It analyzes your resource configuration and usage telemetry, then recommends solutions to improve the cost effectiveness, performance, reliability, security, and operational excellence of your Azure resources.
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Advisor Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-advisor-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-advisor.png
json_schemas:
- name: OperationList
  property_count: 2
  slug: microsoft-azure-advisor-operation-list
- name: ResourceList
  property_count: 2
  slug: microsoft-azure-advisor-resource-list
- name: Resource
  property_count: 6
  slug: microsoft-azure-advisor-resource
jsonld:
- class_count: 5
  name: Microsoft Azure Advisor Context
  property_count: 11
  slug: microsoft-azure-advisor-context
layout: provider
modified: '2026-09-16'
name: Microsoft Azure Advisor
nav: Providers
network: true
overview: 'Microsoft Azure Advisor publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Operations API, Recommendations API, Advisor Score Entities API, and 5 more. Tagged areas include Advisor, Best Practices, Cost Optimization, Microsoft Azure, and Optimization.


  The Microsoft Azure Advisor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Advisor''s developer surface includes getting-started guide, CLI, changelog, engineering blog, authentication, developer portal, documentation, and 32 more developer resources.'
plans:
- name: Microsoft Azure Advisor Plans Pricing
  plan_count: 0
  slug: microsoft-azure-advisor-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 6
  name: Microsoft Azure Advisor Rate Limits
  slug: microsoft-azure-advisor-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Microsoft Azure Advisor API Rules
  rule_count: 43
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 2
  slug: microsoft-azure-advisor-rules
scopes:
- name: Microsoft Azure Advisor Scopes
  scope_count: 1
  slug: microsoft-azure-advisor-scopes
  summary_line: 1 scope · implicit
score:
  band: strong
  composite: 64.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 20.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 71.4
    discoverability: 82.1
    operational_transparency: 76.3
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
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
screenshot: https://apis.io/screenshots/microsoft-azure-advisor/microsoft-azure-advisor-2026-06-20T185354.png
security:
- kind: authentication
  name: Microsoft Azure Advisor Authentication
  slug: microsoft-azure-advisor-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Advisor Domain Security
  slug: microsoft-azure-advisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Advisor Vulnerability Disclosure
  slug: microsoft-azure-advisor-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Advisor Trust Center
  slug: microsoft-azure-advisor-trust-center
  summary_line: GDPR
slug: microsoft-azure-advisor
tags:
- Advisor
- Best Practices
- Cost Optimization
- Microsoft Azure
- Optimization
- Recommendations
website: https://microsoft.com
---
