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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Voicegenie Agentic Access
  operation_count: 7
  slug: voicegenie-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://core-saas.voicegenie.ai
  baseurl_source: declared
  description: Place and track voice calls.
  name: VoiceGenie Calls API
  slug: voicegenie-calls-api
- baseURL: https://core-saas.voicegenie.ai
  baseurl_source: declared
  description: Manage outbound/inbound campaigns and their contacts.
  name: VoiceGenie Campaigns API
  slug: voicegenie-campaigns-api
artifact_total: 15
asyncapis:
- description: ''
  name: Voicegenie Webhooks
  slug: voicegenie-webhooks
collections:
- collection_type: open
  name: VoiceGenie Public REST Calls API
  slug: open-voicegenie-calls-api
- collection_type: open
  name: VoiceGenie Public REST Calls Campaigns API
  slug: open-voicegenie-campaigns-api
common:
- group: other
  href: https://artifacts.apis.io/voicegenie/overlays/voicegenie-calls-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/voicegenie-calls-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/voicegenie/overlays/voicegenie-campaigns-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/voicegenie-campaigns-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://voicegenie.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://voicegenie.gitbook.io/voicegenie-ai
- group: docs
  title: ''
  type: Documentation
  url: https://voicegenie.gitbook.io/voicegenie-ai/developer-documentation-1.0
- group: docs
  title: ''
  type: APIReference
  url: https://voicegenie.gitbook.io/voicegenie-ai/integrations/public-api-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://voicegenie.gitbook.io/voicegenie-ai/welcome-to-voicegenie-ai
- group: company
  title: ''
  type: Blog
  url: https://blogs.voicegenie.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://voicegenie.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.voicegenie.ai/
- group: start
  title: ''
  type: Login
  url: https://app.voicegenie.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voicegenie.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voicegenie.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@voicegenie.ai
- group: start
  title: ''
  type: Demo
  url: https://cal.com/voicegenie/demo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/voicegenie
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/voicegenie_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@VoiceGenieAI
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/voicegenie.ai/
- group: agent
  href: https://artifacts.apis.io/voicegenie/llms/voicegenie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voicegenie-llms.txt
- group: auth
  href: https://artifacts.apis.io/voicegenie/authentication/voicegenie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voicegenie-authentication.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/conventions/voicegenie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/voicegenie-conventions.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/errors/voicegenie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/voicegenie-problem-types.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/lifecycle/voicegenie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/voicegenie-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/conformance/voicegenie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voicegenie-conformance.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/data-model/voicegenie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/voicegenie-data-model.yml
- group: auth
  href: https://artifacts.apis.io/voicegenie/security/voicegenie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voicegenie-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/voicegenie/mcp/voicegenie-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/voicegenie-mcp.yml
- group: design
  href: https://artifacts.apis.io/voicegenie/asyncapi/voicegenie-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/voicegenie-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/voicegenie/agentic-access/voicegenie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/voicegenie-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/voicegenie/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/voicegenie/plans/voicegenie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voicegenie-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/voicegenie/rate-limits/voicegenie-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/voicegenie-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/voicegenie/packages/voicegenie-packages.yml
  title: ''
  type: Packages
  url: packages/voicegenie-packages.yml
- group: start
  href: https://artifacts.apis.io/voicegenie/sandbox/voicegenie-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/voicegenie-sandbox.yml
created: '2026-07-17'
description: VoiceGenie (Ori Labs Ltd.) is a conversational voice AI platform for sales automation that lets teams deploy AI voice agents to run outbound and inbound phone calls end to end. Businesses build assistants (voice bots) with a chosen voice, language, script and knowledge base, attach a phone number (via Twilio or Plivo), upload contact lists, and launch campaigns that qualify leads, book meetings, send SMS, run surveys, chase payment reminders, and hand off to human agents when needed. VoiceGenie exposes a Public REST API on core-saas.voicegenie.ai for placing calls, adding calls to recurring campaigns, pausing/resuming campaigns, fetching call analysis and status, retrieving inbound-call updates, checking transfer status, and removing customers from campaigns, plus a post-call analysis webhook, so voice workflows can be automated from n8n, Zapier, Zoho Flow, HubSpot, HighLevel, Cal.com and custom applications.
finops:
- has_sources: true
  method: derived
  name: Voicegenie Finops
  primary_unit: minutes
  service_category: ''
  slug: voicegenie-finops
  template: false
image: https://voicegenie.ai/images/vg_logo_name.svg
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP; 7 tools listed. A candidate, not confirmed as published by the provider.
  name: VoiceGenie MCP Server
  slug: voicegenie
modified: '2026-08-14'
name: VoiceGenie
nav: Providers
network: true
overview: 'VoiceGenie publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Calls API and Campaigns API. Tagged areas include Company, Voice AI, Conversational AI, Sales Automation, and Voice Agents.


  The VoiceGenie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VoiceGenie''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 28 more developer resources.'
plans:
- name: Voicegenie Plans Pricing
  plan_count: 5
  slug: voicegenie-plans-pricing
- name: Voicegenie Price Estimates
  plan_count: 0
  slug: voicegenie-price-estimates
random_paper: 22
rate_limits:
- limit_count: 0
  name: Voicegenie Rate Limits
  slug: voicegenie-rate-limits
score:
  band: developing
  composite: 53.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 57.6
    developer_ergonomics: 66.1
    discoverability: 65.0
    operational_transparency: 7.9
  previous_composite: 51.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/voicegenie/voicegenie-2026-08-17T082816.png
security:
- kind: authentication
  name: Voicegenie Authentication
  slug: voicegenie-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Voicegenie Domain Security
  slug: voicegenie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Place a VoiceGenie call and track its outcome
  slug: voicegenie-place-and-track-call
- name: Feed and control a VoiceGenie campaign
  slug: voicegenie-run-campaign
slug: voicegenie
tags:
- Company
- Voice AI
- Conversational AI
- Sales Automation
- Voice Agents
- Telephony
- Call Center
- Customer Service
- Lead Generation
- Webhook
website: https://voicegenie.ai
---
