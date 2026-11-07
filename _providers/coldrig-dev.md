---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 41
  human_in_the_loop: 3
  name: Coldrig Dev Agentic Access
  operation_count: 64
  slug: coldrig-dev-agentic-access
  summary_line: 64 operations · 41 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The account API from Coldrig — 8 operation(s) for account.
  name: Coldrig Account API
  slug: coldrig-dev-account-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The bootstrap API from Coldrig — 1 operation(s) for bootstrap.
  name: Coldrig Bootstrap API
  slug: coldrig-dev-bootstrap-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The byo-domains API from Coldrig — 6 operation(s) for byo-domains.
  name: Coldrig Byo Domains API
  slug: coldrig-dev-byo-domains-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The campaigns API from Coldrig — 13 operation(s) for campaigns.
  name: Coldrig Campaigns API
  slug: coldrig-dev-campaigns-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The compliance API from Coldrig — 1 operation(s) for compliance.
  name: Coldrig Compliance API
  slug: coldrig-dev-compliance-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The dashboard API from Coldrig — 5 operation(s) for dashboard.
  name: Coldrig Dashboard API
  slug: coldrig-dev-dashboard-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The inbox API from Coldrig — 6 operation(s) for inbox.
  name: Coldrig Inbox API
  slug: coldrig-dev-inbox-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The infrastructure API from Coldrig — 3 operation(s) for infrastructure.
  name: Coldrig Infrastructure API
  slug: coldrig-dev-infrastructure-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The leads API from Coldrig — 3 operation(s) for leads.
  name: Coldrig Leads API
  slug: coldrig-dev-leads-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The messages API from Coldrig — 4 operation(s) for messages.
  name: Coldrig Messages API
  slug: coldrig-dev-messages-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The sandbox API from Coldrig — 1 operation(s) for sandbox.
  name: Coldrig Sandbox API
  slug: coldrig-dev-sandbox-api
- baseURL: https://api.coldrig.dev
  baseurl_source: declared
  description: The webhooks API from Coldrig — 2 operation(s) for webhooks.
  name: Coldrig Webhooks API
  slug: coldrig-dev-webhooks-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/coldrig-dev/agentic-access/coldrig-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coldrig-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/coldrig-dev/plans/coldrig-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coldrig-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/rules/coldrig-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/coldrig-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/json-ld/coldrig-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coldrig-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/coldrig-dev/vocabulary/coldrig-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coldrig-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coldrig-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/data-model/coldrig-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coldrig-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/conventions/coldrig-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coldrig-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/conventions/coldrig-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coldrig-dev-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coldrig.dev/security
- group: auth
  href: https://artifacts.apis.io/coldrig-dev/authentication/coldrig-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coldrig-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/errors/coldrig-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coldrig-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coldrig-dev/conformance/coldrig-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coldrig-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coldrig-dev/llms/coldrig-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coldrig-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/coldrig-dev/well-known/coldrig-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coldrig-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/coldrig-dev/hosts/coldrig-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coldrig-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/coldrig-dev/vendors/coldrig-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coldrig-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coldrig.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://coldrig.dev/support
- group: operate
  title: ''
  type: StatusPage
  url: https://coldrig.dev/status
- group: start
  title: ''
  type: SignUp
  url: https://coldrig.dev/signup
- group: auth
  title: ''
  type: Security
  url: https://coldrig.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coldrig.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://coldrig.dev/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://coldrig.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coldrig.dev/connect
- group: docs
  title: ''
  type: APIReference
  url: https://coldrig.dev/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/coldrig-dev/security/coldrig-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coldrig-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coldrig-dev/security/coldrig-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coldrig-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coldrig-dev/security/coldrig-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coldrig-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coldrig.dev/
created: '2026-11-04'
description: Coldrig provides AI-powered cold email infrastructure, enabling agents to manage domains, mailboxes, warmup, campaigns, and automated replies. The platform integrates with AI models like Codex, Claude Code, and Cursor, offering a unified system for outreach automation and response handling. It aims to simplify cold outreach for developers and marketers by leveraging advanced language models to generate personalized email content and manage campaign workflows.
image: https://coldrig.dev/assets/og-image.png
json_schemas:
- name: CampaignPreview
  property_count: 10
  slug: coldrig-dev-campaign-preview
- name: LaunchCampaignInput
  property_count: 12
  slug: coldrig-dev-launch-campaign-input
- name: LaunchedCampaign
  property_count: 11
  slug: coldrig-dev-launched-campaign
- name: LeadInput
  property_count: 5
  slug: coldrig-dev-lead-input
- name: MailboxBilling
  property_count: 5
  slug: coldrig-dev-mailbox-billing
- name: SetupInfrastructureInput
  property_count: 13
  slug: coldrig-dev-setup-infrastructure-input
jsonld:
- class_count: 76
  name: Coldrig Dev Context
  property_count: 253
  slug: coldrig-dev-context
layout: provider
modified: '2026-11-04'
name: Coldrig
nav: Providers
network: true
overview: 'Coldrig publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bootstrap API, Byo Domains API, and 9 more. Tagged areas include Cold Email, Outreach, AI Agents, and Email Infrastructure.


  The Coldrig catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coldrig''s developer surface includes authentication, support, signup flow, pricing, documentation, getting-started guide, API reference, and 24 more developer resources.'
plans:
- name: Coldrig Dev Plans Pricing
  plan_count: 4
  slug: coldrig-dev-plans-pricing
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Coldrig API Rules
  rule_count: 59
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 11
  slug: coldrig-dev-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 47.0
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coldrig Dev Authentication
  slug: coldrig-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Coldrig Dev Domain Security
  slug: coldrig-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Coldrig Dev Vulnerability Disclosure
  slug: coldrig-dev-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Coldrig Dev Trust Center
  slug: coldrig-dev-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: coldrig-dev-handle-messages
  slug: coldrig-dev-handle-messages
- name: coldrig-dev-manage-webhook-subscription
  slug: coldrig-dev-manage-webhook-subscription
- name: coldrig-dev-reply-to-thread
  slug: coldrig-dev-reply-to-thread
- name: coldrig-dev-view-billing
  slug: coldrig-dev-view-billing
slug: coldrig-dev
tags:
- Cold Email
- Outreach
- AI Agents
- Email Infrastructure
website: https://coldrig.dev/
---
