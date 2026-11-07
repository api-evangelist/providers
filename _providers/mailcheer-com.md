---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Mailcheer Com Agentic Access
  operation_count: 37
  slug: mailcheer-com-agentic-access
  summary_line: 37 operations · 22 acting
api_count: 1
apis:
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: Drafts, sending and statistics.
  name: mailcheer-com Campaigns API
  slug: mailcheer-com-campaigns-api
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: Individual sends and their status.
  name: mailcheer-com Emails API
  slug: mailcheer-com-emails-api
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: The people signed up to your lists.
  name: mailcheer-com Subscribers API
  slug: mailcheer-com-subscribers-api
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: Addresses that will receive nothing further.
  name: mailcheer-com Suppression API
  slug: mailcheer-com-suppression-api
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: Mailcheer calls YOUR service when something happens.
  name: mailcheer-com Webhooks API
  slug: mailcheer-com-webhooks-api
- baseURL: https://mailcheer.com
  baseurl_source: declared
  description: Who the key belongs to.
  name: mailcheer-com Workspace API
  slug: mailcheer-com-workspace-api
artifact_total: 22
asyncapis:
- description: ''
  name: Mailcheer Com Webhooks
  slug: mailcheer-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/mailcheer-com/agentic-access/mailcheer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mailcheer-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/mailcheer-com/plans/mailcheer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mailcheer-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/rules/mailcheer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/mailcheer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/json-ld/mailcheer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mailcheer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/mailcheer-com/vocabulary/mailcheer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mailcheer-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mailcheer-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/asyncapi/mailcheer-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mailcheer-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/data-model/mailcheer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mailcheer-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/conventions/mailcheer-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/mailcheer-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/conventions/mailcheer-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mailcheer-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/mailcheer-com/authentication/mailcheer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mailcheer-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/errors/mailcheer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mailcheer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mailcheer-com/conformance/mailcheer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mailcheer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mailcheer-com/llms/mailcheer-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mailcheer-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/mailcheer-com/well-known/mailcheer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mailcheer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/mailcheer-com/hosts/mailcheer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mailcheer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/mailcheer-com/vendors/mailcheer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mailcheer-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://mailcheer.com/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://mailcheer.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://mailcheer.com/docs/api
- group: auth
  href: https://artifacts.apis.io/mailcheer-com/security/mailcheer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mailcheer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mailcheer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://mailcheer.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://mailcheer.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mailcheer.com/signup
- group: operate
  title: ''
  type: Support
  url: https://mailcheer.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mailcheer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mailcheer.com/privacy
created: '2026-10-30'
description: Mailcheer provides free newsletter software with a robust API and MCP server, enabling developers and marketers to create, manage, and send AI‑enhanced newsletters. The platform offers campaign editors, templates, deliverability analytics, subscriber segmentation, and integrations for e‑commerce, real‑estate, and SaaS businesses. With AI writing assistance and a comprehensive developer portal, Mailcheer supports automated newsletter workflows and custom applications via its RESTful API.
image: https://mailcheer.com/og-en.png
json_schemas:
- name: Account
  property_count: 10
  slug: mailcheer-com-account
- name: CampaignRequest
  property_count: 8
  slug: mailcheer-com-campaign-request
- name: CampaignStats
  property_count: 8
  slug: mailcheer-com-campaign-stats
- name: CampaignUpdate
  property_count: 8
  slug: mailcheer-com-campaign-update
- name: EmailDetail
  property_count: 20
  slug: mailcheer-com-email-detail
- name: EmailRequest
  property_count: 16
  slug: mailcheer-com-email-request
jsonld:
- class_count: 29
  name: Mailcheer Com Context
  property_count: 109
  slug: mailcheer-com-context
layout: provider
modified: '2026-10-30'
name: mailcheer-com
nav: Providers
network: true
overview: 'mailcheer-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Campaigns API, Emails API, Subscribers API, and 3 more. Tagged areas include Company, Newsletters, Marketing, and Artificial Intelligence.


  The mailcheer-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  mailcheer-com''s developer surface includes authentication, changelog, API reference, documentation, pricing, signup flow, support, and 21 more developer resources.'
plans:
- name: Mailcheer Com Plans Pricing
  plan_count: 4
  slug: mailcheer-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: mailcheer-com API Rules
  rule_count: 17
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 3
  slug: mailcheer-com-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 73.8
    developer_ergonomics: 24.4
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    skills: derived
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mailcheer-com/mailcheer-com-2026-11-03T135239.png
security:
- kind: authentication
  name: Mailcheer Com Authentication
  slug: mailcheer-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mailcheer Com Domain Security
  slug: mailcheer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: mailcheer-com-create-and-send-campaign
  slug: mailcheer-com-create-and-send-campaign
- name: mailcheer-com-create-test-webhook
  slug: mailcheer-com-create-test-webhook
- name: mailcheer-com-upsert-and-tag-subscriber
  slug: mailcheer-com-upsert-and-tag-subscriber
slug: mailcheer-com
tags:
- Company
- Newsletters
- Marketing
- Artificial Intelligence
website: https://mailcheer.com/
---
