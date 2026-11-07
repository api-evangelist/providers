---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 111
  human_in_the_loop: 2
  name: Sitegpt Ai Agentic Access
  operation_count: 175
  slug: sitegpt-ai-agentic-access
  summary_line: 175 operations · 111 acting · 2 human-in-the-loop
api_count: 2
apis:
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Account API from sitegpt-ai — 6 operation(s) for account.
  name: sitegpt-ai Account API
  slug: sitegpt-ai-account-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Billing API from sitegpt-ai — 2 operation(s) for billing.
  name: sitegpt-ai Billing API
  slug: sitegpt-ai-billing-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage different chatbots. APIs include `Fetching All Chatbots`, `Creating New Chatbot`, Fetching One Chatbot`, `Updating Chatbot Appearance` and `Deleting Chatbot`.
  name: sitegpt-ai Chatbot API
  slug: sitegpt-ai-chatbot-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to update appearance of the chatbot.
  name: sitegpt-ai Chatbot Appearance API
  slug: sitegpt-ai-chatbot-appearance-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage `Conversation Starters` of a particular chatbot. APIs include `Fetching All Conversation Starters`, `Adding New Conversation Starter`, `Fetching One Conversation Starter`, `Updating Con
  name: sitegpt-ai Chatbot Conversation Starters API
  slug: sitegpt-ai-chatbot-conversation-starters-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to modify custom content of the chatbot.
  name: sitegpt-ai Chatbot Custom Content API
  slug: sitegpt-ai-chatbot-custom-content-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage `Follow up Prompts` of a particular chatbot. APIs include `Fetching All Follow up Prompts`, `Adding New Follow up Prompt`, `Fetching One Follow up Prompt`, `Updating Follow up Prompt` a
  name: sitegpt-ai Chatbot Follow Up Prompts API
  slug: sitegpt-ai-chatbot-follow-up-prompts-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage (add/update/delete) icons related to a particular chatbot.
  name: sitegpt-ai Chatbot Icons API
  slug: sitegpt-ai-chatbot-icons-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to fetch internal links of any url and to add certain links to a particular chatbot.
  name: sitegpt-ai Chatbot Links API
  slug: sitegpt-ai-chatbot-links-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to send a message to a particular thread or start a new conversation with in a particular chatbot.
  name: sitegpt-ai Chatbot Messages API
  slug: sitegpt-ai-chatbot-messages-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage personas of the chatbot.
  name: sitegpt-ai Chatbot Personas API
  slug: sitegpt-ai-chatbot-personas-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage prompts of the chatbot.
  name: sitegpt-ai Chatbot Prompts API
  slug: sitegpt-ai-chatbot-prompts-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to update different settings of the chatbot. APIs include `General Settings`, `User Data Settings`, `Chat Mode Settings`, `Localization Settings` and `Advanced Settings`.
  name: sitegpt-ai Chatbot Settings API
  slug: sitegpt-ai-chatbot-settings-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage threads related to a particular chatbot. APIs include `Fetching All Threads`, `Fetching One Thread` and `Update Thread`.
  name: sitegpt-ai Chatbot Threads API
  slug: sitegpt-ai-chatbot-threads-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Chatbots API from sitegpt-ai — 7 operation(s) for chatbots.
  name: sitegpt-ai Chatbots API
  slug: sitegpt-ai-chatbots-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Conversation Followups API from sitegpt-ai — 3 operation(s) for conversation followups.
  name: sitegpt-ai Conversation Followups API
  slug: sitegpt-ai-conversation-followups-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Conversation Starters API from sitegpt-ai — 3 operation(s) for conversation starters.
  name: sitegpt-ai Conversation Starters API
  slug: sitegpt-ai-conversation-starters-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Conversations API from sitegpt-ai — 10 operation(s) for conversations.
  name: sitegpt-ai Conversations API
  slug: sitegpt-ai-conversations-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Custom Responses API from sitegpt-ai — 2 operation(s) for custom responses.
  name: sitegpt-ai Custom Responses API
  slug: sitegpt-ai-custom-responses-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Discovery API from sitegpt-ai — 3 operation(s) for discovery.
  name: sitegpt-ai Discovery API
  slug: sitegpt-ai-discovery-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Instructions API from sitegpt-ai — 3 operation(s) for instructions.
  name: sitegpt-ai Instructions API
  slug: sitegpt-ai-instructions-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Knowledge API from sitegpt-ai — 12 operation(s) for knowledge.
  name: sitegpt-ai Knowledge API
  slug: sitegpt-ai-knowledge-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Knowledge Sources API from sitegpt-ai — 9 operation(s) for knowledge sources.
  name: sitegpt-ai Knowledge Sources API
  slug: sitegpt-ai-knowledge-sources-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Knowledge Sync Jobs API from sitegpt-ai — 2 operation(s) for knowledge sync jobs.
  name: sitegpt-ai Knowledge Sync Jobs API
  slug: sitegpt-ai-knowledge-sync-jobs-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Leads API from sitegpt-ai — 3 operation(s) for leads.
  name: sitegpt-ai Leads API
  slug: sitegpt-ai-leads-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Members API from sitegpt-ai — 4 operation(s) for members.
  name: sitegpt-ai Members API
  slug: sitegpt-ai-members-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Messages API from sitegpt-ai — 3 operation(s) for messages.
  name: sitegpt-ai Messages API
  slug: sitegpt-ai-messages-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Onboarding API from sitegpt-ai — 3 operation(s) for onboarding.
  name: sitegpt-ai Onboarding API
  slug: sitegpt-ai-onboarding-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Personas API from sitegpt-ai — 3 operation(s) for personas.
  name: sitegpt-ai Personas API
  slug: sitegpt-ai-personas-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Settings API from sitegpt-ai — 2 operation(s) for settings.
  name: sitegpt-ai Settings API
  slug: sitegpt-ai-settings-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Tags API from sitegpt-ai — 2 operation(s) for tags.
  name: sitegpt-ai Tags API
  slug: sitegpt-ai-tags-api
- baseURL: https://sitegpt.ai
  baseurl_source: declared
  description: The Tokens API from sitegpt-ai — 3 operation(s) for tokens.
  name: sitegpt-ai Tokens API
  slug: sitegpt-ai-tokens-api
- baseURL: https://sitegpt.ai/api
  baseurl_source: declared
  description: APIs to manage whitelabel users. APIs include `Create Whitelabel User` and `Update Whitelabel User Quota`.
  name: sitegpt-ai Whitelabel API
  slug: sitegpt-ai-whitelabel-api
artifact_total: 49
common:
- group: agent
  href: https://artifacts.apis.io/sitegpt-ai/agentic-access/sitegpt-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sitegpt-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sitegpt-ai/plans/sitegpt-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sitegpt-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/rules/sitegpt-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/sitegpt-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/json-ld/sitegpt-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sitegpt-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/vocabulary/sitegpt-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sitegpt-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sitegpt-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/data-model/sitegpt-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sitegpt-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/sitegpt-ai/cli/sitegpt-ai-cli.yml
  title: ''
  type: CLI
  url: cli/sitegpt-ai-cli.yml
- group: operate
  href: https://artifacts.apis.io/sitegpt-ai/changelog/sitegpt-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sitegpt-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/conventions/sitegpt-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sitegpt-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.sitegpt.ai/
- group: auth
  href: https://artifacts.apis.io/sitegpt-ai/authentication/sitegpt-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sitegpt-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sitegpt-ai/scopes/sitegpt-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sitegpt-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/errors/sitegpt-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sitegpt-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sitegpt-ai/conformance/sitegpt-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sitegpt-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sitegpt-ai/llms/sitegpt-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sitegpt-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/sitegpt-ai/a2a/sitegpt-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sitegpt-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/sitegpt-ai/well-known/sitegpt-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sitegpt-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/sitegpt-ai/hosts/sitegpt-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sitegpt-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/sitegpt-ai/vendors/sitegpt-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sitegpt-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/sitegpt-ai/packages/sitegpt-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/sitegpt-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/sitegpt-ai/packages/sitegpt-ai-packages.yml
  title: ''
  type: Packages
  url: packages/sitegpt-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://sitegpt.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://sitegpt.ai/docs/changelog/overview
- group: auth
  href: https://artifacts.apis.io/sitegpt-ai/security/sitegpt-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sitegpt-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sitegpt-ai/security/sitegpt-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sitegpt-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sitegpt.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://sitegpt.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://sitegpt.ai/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://sitegpt.ai/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://sitegpt.ai/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://sitegpt.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sitegpt
- group: commercial
  title: ''
  type: Pricing
  url: https://sitegpt.ai/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://sitegpt.ai/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sitegpt.ai/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sitegpt.ai/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/sitegpt/
created: '2026-10-30'
description: SiteGPT is an AI-powered customer support chatbot platform founded in 2023. It enables businesses to turn website content, help docs, and files into a personalized chatbot that answers visitor questions instantly. The service offers customizable plans, automatic content syncing, and integrates with popular channels, helping reduce support workload and improve user experience.
image: https://b-cdn.sitegpt.ai/images/og-image-new.jpg
json_schemas:
- name: BillingSubscription
  property_count: 16
  slug: sitegpt-ai-billing-subscription
- name: Chatbot
  property_count: 10
  slug: sitegpt-ai-chatbot
- name: Conversation
  property_count: 29
  slug: sitegpt-ai-conversation
- name: Invoice
  property_count: 20
  slug: sitegpt-ai-invoice
- name: KnowledgeDocument
  property_count: 18
  slug: sitegpt-ai-knowledge-document
- name: Message
  property_count: 13
  slug: sitegpt-ai-message
jsonld:
- class_count: 65
  name: Sitegpt Ai Context
  property_count: 310
  slug: sitegpt-ai-context
layout: provider
modified: '2026-10-30'
name: sitegpt-ai
nav: Providers
network: true
overview: 'sitegpt-ai publishes 33 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Billing API, Chatbot API, and 30 more. Tagged areas include Company, Artificial Intelligence, Customer Service, Chatbots, and Software-as-a-Service.


  The sitegpt-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sitegpt-ai''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, support, and 31 more developer resources.'
plans:
- name: Sitegpt Ai Plans Pricing
  plan_count: 4
  slug: sitegpt-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Sitegpt Ai Rate Limits
  slug: sitegpt-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: sitegpt-ai API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: sitegpt-ai-rules
scopes:
- name: Sitegpt Ai Scopes
  scope_count: 37
  slug: sitegpt-ai-scopes
  summary_line: 37 scopes
score:
  band: strong
  composite: 56.2
  coverage:
    artifact_dirs: 35
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 70.6
    developer_ergonomics: 52.9
    discoverability: 73.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sitegpt-ai/sitegpt-ai-2026-11-03T143243.png
security:
- kind: authentication
  name: Sitegpt Ai Authentication
  slug: sitegpt-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sitegpt Ai Domain Security
  slug: sitegpt-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Sitegpt Ai Trust Center
  slug: sitegpt-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
skill_count: 1
skills:
- name: create-chatbot
  slug: sitegpt-ai-create-chatbot
slug: sitegpt-ai
tags:
- Company
- Artificial Intelligence
- Customer Service
- Chatbots
- Software-as-a-Service
- Automation
website: https://sitegpt.ai/
---
