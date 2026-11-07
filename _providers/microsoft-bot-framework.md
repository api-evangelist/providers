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
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Microsoft Bot Framework Agentic Access
  operation_count: 15
  slug: microsoft-bot-framework-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 2
apis:
- description: Custom applications communicate directly with bots through REST and WebSocket connections.
  name: Direct Line API
  slug: direct-line
- description: Libraries for building conversational AI bots in C#, JavaScript, Python, and Java.
  name: Bot Builder SDK
  slug: bot-builder-sdk
- baseURL: https://api.botframework.com/
  baseurl_source: declared
  description: The Activities API from Microsoft Bot Framework — 3 operation(s) for activities.
  name: Microsoft Bot Framework Activities API
  slug: microsoft-bot-framework-activities-api
- baseURL: https://api.botframework.com/
  baseurl_source: declared
  description: The Attachments API from Microsoft Bot Framework — 3 operation(s) for attachments.
  name: Microsoft Bot Framework Attachments API
  slug: microsoft-bot-framework-attachments-api
- baseURL: https://api.botframework.com/
  baseurl_source: declared
  description: The Conversations API from Microsoft Bot Framework — 1 operation(s) for conversations.
  name: Microsoft Bot Framework Conversations API
  slug: microsoft-bot-framework-conversations-api
- baseURL: https://api.botframework.com/
  baseurl_source: declared
  description: The Members API from Microsoft Bot Framework — 4 operation(s) for members.
  name: Microsoft Bot Framework Members API
  slug: microsoft-bot-framework-members-api
- baseURL: https://token.botframework.com
  baseurl_source: declared
  description: The BotSignIn API from Microsoft Bot Framework — 2 operation(s) for botsignin.
  name: Microsoft Bot Framework Bot Sign In API
  slug: microsoft-bot-framework-botsignin-api
- baseURL: https://token.botframework.com
  baseurl_source: declared
  description: The User Token API from Microsoft Bot Framework — 5 operation(s) for user token.
  name: Microsoft Bot Framework User Token API
  slug: microsoft-bot-framework-user-token-api
artifact_total: 24
collections:
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities API
  slug: open-microsoft-bot-framework-activities-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Attachments API
  slug: open-microsoft-bot-framework-attachments-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Conversations API
  slug: open-microsoft-bot-framework-conversations-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST Activities Members API
  slug: open-microsoft-bot-framework-members-api
- collection_type: open
  name: Microsoft Bot Framework Connector REST API
  slug: open-microsoft-bot-framework
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/rules/microsoft-bot-framework-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-bot-framework-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/vocabulary/microsoft-bot-framework-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-bot-framework-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/data-model/microsoft-bot-framework-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-bot-framework-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/conventions/microsoft-bot-framework-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-bot-framework-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/microsoft/botframework-sdk
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/lifecycle/microsoft-bot-framework-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-bot-framework-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/errors/microsoft-bot-framework-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-bot-framework-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-bot-framework/conformance/microsoft-bot-framework-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-bot-framework-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-bot-framework/llms/microsoft-bot-framework-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-bot-framework-llms.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-bot-framework/well-known/microsoft-bot-framework-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-bot-framework-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-bot-framework/well-known/microsoft-bot-framework-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-bot-framework-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bot-framework/hosts/microsoft-bot-framework-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-bot-framework-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-bot-framework/vendors/microsoft-bot-framework-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-bot-framework-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bot-framework/packages/microsoft-bot-framework-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-bot-framework-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-bot-framework/packages/microsoft-bot-framework-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-bot-framework-packages.yml
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
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.botframework.com/
- group: auth
  href: https://artifacts.apis.io/microsoft-bot-framework/security/microsoft-bot-framework-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-bot-framework-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bot-framework/security/microsoft-bot-framework-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-bot-framework-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bot-framework/plans/microsoft-bot-framework-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-bot-framework-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-bot-framework/rate-limits/microsoft-bot-framework-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-bot-framework-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bot-framework/finops/microsoft-bot-framework-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-bot-framework-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-bot-framework/agentic-access/microsoft-bot-framework-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bot-framework-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bot-framework/security/microsoft-bot-framework-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-bot-framework-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bot-framework/authentication/microsoft-bot-framework-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-bot-framework-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://dev.botframework.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/botframework-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/bot-services/
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
created: '2026-03-13'
description: Microsoft Bot Framework provides APIs and SDKs for building conversational AI bots that work across multiple channels including Teams, Slack, and custom applications. Its public REST surface is the Bot Connector API, the Bot Token service and the Direct Line API, hosted through Azure AI Bot Service, with first-party Bot Builder SDKs for C#, JavaScript, Python and Java.
finops:
- has_sources: false
  method: generated
  name: Microsoft Bot Framework Finops
  primary_unit: request
  service_category: API
  slug: microsoft-bot-framework-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bot-framework.png
json_schemas:
- name: GenericList
  property_count: 0
  slug: microsoft-bot-framework-generic-list
- name: GenericObject
  property_count: 0
  slug: microsoft-bot-framework-generic-object
layout: provider
modified: '2026-05-19'
name: Microsoft Bot Framework
nav: Providers
network: true
overview: 'Microsoft Bot Framework publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Attachments API, Conversations API, and 5 more. Tagged areas include Bots, Conversational AI, Messaging, Bot Framework, and Direct Line.


  The Microsoft Bot Framework catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Bot Framework''s developer surface includes changelog, engineering blog, getting-started guide, documentation, authentication, developer portal, pricing, and 31 more developer resources.'
plans:
- name: Microsoft Bot Framework Plans Pricing
  plan_count: 3
  slug: microsoft-bot-framework-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Microsoft Bot Framework Rate Limits
  slug: microsoft-bot-framework-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Microsoft Bot Framework API Rules
  rule_count: 55
  severity_counts:
    error: 43
    hint: 0
    info: 7
    warn: 5
  slug: microsoft-bot-framework-rules
score:
  band: developing
  composite: 53.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.6
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 45.6
    developer_ergonomics: 57.1
    discoverability: 73.2
    operational_transparency: 60.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-bot-framework/microsoft-bot-framework-2026-06-20T185445.png
security:
- kind: authentication
  name: Microsoft Bot Framework Authentication
  slug: microsoft-bot-framework-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Microsoft Bot Framework Domain Security
  slug: microsoft-bot-framework-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Bot Framework Vulnerability Disclosure
  slug: microsoft-bot-framework-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Bot Framework Trust Center
  slug: microsoft-bot-framework-trust-center
  summary_line: GDPR
slug: microsoft-bot-framework
tags:
- Bots
- Conversational AI
- Messaging
- Bot Framework
- Direct Line
website: https://www.microsoft.com/
---
