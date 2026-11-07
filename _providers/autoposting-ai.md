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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 125
  human_in_the_loop: 10
  name: Autoposting Ai Agentic Access
  operation_count: 187
  slug: autoposting-ai-agentic-access
  summary_line: 187 operations · 125 acting · 10 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create and manage AI agents that autonomously generate and schedule content, trigger runs, inspect outputs, and track statistics.
  name: Autoposting.ai Agents API
  slug: autoposting-ai-agents-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create, list, update, and revoke API keys for programmatic access to the Autoposting.ai API.
  name: Autoposting.ai API Keys API
  slug: autoposting-ai-api-keys-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Signup, login, logout, social login, profile management, email change, and session management.
  name: Autoposting.ai Auth API
  slug: autoposting-ai-auth-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Manage subscriptions, credits, plan changes, billing history, and the customer portal.
  name: Autoposting.ai Billing API
  slug: autoposting-ai-billing-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create, list, update, delete, and reorder brands. Each brand maps to a set of social media accounts.
  name: Autoposting.ai Brands API
  slug: autoposting-ai-brands-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create, manage, and AI-generate carousel posts for LinkedIn and other platforms.
  name: Autoposting.ai Carousels API
  slug: autoposting-ai-carousels-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Upload, manage, render, and publish video clips, including multipart upload, AI candidate generation, and credit billing.
  name: Autoposting.ai Clips API
  slug: autoposting-ai-clips-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Knowledge bases, document ingestion, semantic search, and AI content idea generation.
  name: Autoposting.ai Knowledge Base API
  slug: autoposting-ai-knowledge-base-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: List, read, and manage in-app notifications and notification preferences.
  name: Autoposting.ai Notifications API
  slug: autoposting-ai-notifications-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create, list, update, and delete organizations (workspaces), including a safeguarded deletion flow with a grace period.
  name: Autoposting.ai Organizations API
  slug: autoposting-ai-organizations-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Connect social media accounts via OAuth and manage platform tokens for X, LinkedIn, Instagram, Threads, and YouTube.
  name: Autoposting.ai Platform OAuth API
  slug: autoposting-ai-platform-oauth-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Create, manage, schedule, publish, and AI-enhance posts across platforms.
  name: Autoposting.ai Posts API
  slug: autoposting-ai-posts-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Manage team members, invitations, invite links, permission groups, brand-level overrides, ownership transfers, and allowed email domains.
  name: Autoposting.ai Teams API
  slug: autoposting-ai-teams-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Usage summaries, token breakdowns, feature access, onboarding progress, and account management endpoints.
  name: Autoposting.ai Usage API
  slug: autoposting-ai-usage-api
- baseURL: https://app.autoposting.ai/api-proxy
  baseurl_source: declared
  description: Configure outbound webhook endpoints to receive real-time event notifications from Autoposting.ai.
  name: Autoposting.ai Webhooks API
  slug: autoposting-ai-webhooks-api
artifact_total: 33
asyncapis:
- description: ''
  name: Autoposting Ai Webhooks
  slug: autoposting-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/autoposting-ai/agentic-access/autoposting-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autoposting-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/autoposting-ai/plans/autoposting-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autoposting-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/rules/autoposting-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/autoposting-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/json-ld/autoposting-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autoposting-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/autoposting-ai/vocabulary/autoposting-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autoposting-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/autoposting-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/asyncapi/autoposting-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/autoposting-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/data-model/autoposting-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autoposting-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/autoposting-ai/cli/autoposting-ai-cli.yml
  title: ''
  type: CLI
  url: cli/autoposting-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/autoposting-ai/authentication/autoposting-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autoposting-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/errors/autoposting-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autoposting-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autoposting-ai/conformance/autoposting-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autoposting-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autoposting-ai/llms/autoposting-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autoposting-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/autoposting-ai/a2a/autoposting-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/autoposting-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/autoposting-ai/well-known/autoposting-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autoposting-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/autoposting-ai/hosts/autoposting-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autoposting-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/autoposting-ai/vendors/autoposting-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autoposting-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/autoposting-ai/packages/autoposting-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/autoposting-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/autoposting-ai/packages/autoposting-ai-packages.yml
  title: ''
  type: Packages
  url: packages/autoposting-ai-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.autoposting.ai/
- group: start
  title: ''
  type: SignUp
  url: https://app.autoposting.ai/signup
- group: auth
  title: ''
  type: Security
  url: https://autoposting.ai/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://autoposting.ai/solutions/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://autoposting.ai/changelog
- group: auth
  href: https://artifacts.apis.io/autoposting-ai/security/autoposting-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/autoposting-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/autoposting-ai/security/autoposting-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autoposting-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autoposting.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://autoposting.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://autoposting.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://autoposting.ai/tutorial
- group: commercial
  title: ''
  type: Pricing
  url: https://autoposting.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autoposting.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autoposting.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://autoposting.ai/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://autoposting.ai/status
created: '2026-11-02'
description: Autoposting.ai provides an AI‑powered social media automation platform that generates engaging content, schedules posts across multiple platforms, and offers smart reposting, carousel creation, video clipping, and self‑learning AI that adapts to your brand. It includes a developer‑focused CLI, MCP server integration, REST API and webhooks for programmatic access, as well as team collaboration tools, analytics, and a visual content calendar. The service targets creators, marketers, agencies, and developers seeking to streamline multi‑channel publishing with AI assistance.
image: https://autoposting.ai/og-image.webp
json_schemas:
- name: Agent
  property_count: 15
  slug: autoposting-ai-agent
- name: ApiKey
  property_count: 9
  slug: autoposting-ai-api-key
- name: Brand
  property_count: 9
  slug: autoposting-ai-brand
- name: Clip
  property_count: 9
  slug: autoposting-ai-clip
- name: Post
  property_count: 15
  slug: autoposting-ai-post
- name: UsageSummary
  property_count: 6
  slug: autoposting-ai-usage-summary
jsonld:
- class_count: 70
  name: Autoposting Ai Context
  property_count: 163
  slug: autoposting-ai-context
layout: provider
modified: '2026-11-02'
name: Autoposting.ai
nav: Providers
network: true
overview: 'Autoposting.ai publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, API Keys API, Auth API, and 12 more. Tagged areas include Artificial Intelligence, Social Media, Automation, Marketing, and Developer Tools.


  The Autoposting.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Autoposting.ai''s developer surface includes CLI, authentication, support, signup flow, changelog, documentation, API reference, and 28 more developer resources.'
plans:
- name: Autoposting Ai Plans Pricing
  plan_count: 3
  slug: autoposting-ai-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Autoposting.ai API Rules
  rule_count: 56
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 9
  slug: autoposting-ai-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 50.6
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 65.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autoposting Ai Authentication
  slug: autoposting-ai-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Autoposting Ai Domain Security
  slug: autoposting-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Autoposting Ai Vulnerability Disclosure
  slug: autoposting-ai-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: autoposting-ai-create-and-retrieve-brand
  slug: autoposting-ai-create-and-retrieve-brand
- name: autoposting-ai-create-and-test-webhook
  slug: autoposting-ai-create-and-test-webhook
- name: autoposting-ai-create-and-verify-billing-checkout
  slug: autoposting-ai-create-and-verify-billing-checkout
- name: autoposting-ai-delete-organization
  slug: autoposting-ai-delete-organization
slug: autoposting-ai
tags:
- Artificial Intelligence
- Social Media
- Automation
- Marketing
- Developer Tools
- Company
website: https://autoposting.ai/
---
