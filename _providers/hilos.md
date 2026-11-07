---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Hilos Agentic Access
  operation_count: 19
  slug: hilos-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 1
apis:
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The Contact API from Hilos — 2 operation(s) for contact.
  name: Hilos Contact API
  slug: hilos-contact-api
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The Conversation API from Hilos — 2 operation(s) for conversation.
  name: Hilos Conversation API
  slug: hilos-conversation-api
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The Flow Execution API from Hilos — 3 operation(s) for flow execution.
  name: Hilos Flow Execution API
  slug: hilos-flow-execution-api
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The Flow Execution Contact API from Hilos — 2 operation(s) for flow execution contact.
  name: Hilos Flow Execution Contact API
  slug: hilos-flow-execution-contact-api
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The User API from Hilos — 1 operation(s) for user.
  name: Hilos User API
  slug: hilos-user-api
- baseURL: https://api.hilos.io/api/
  baseurl_source: declared
  description: The Whats App API from Hilos — 3 operation(s) for whats app.
  name: Hilos Whats App API
  slug: hilos-whats-app-api
artifact_total: 23
asyncapis:
- description: ''
  name: Hilos Events
  slug: hilos-events
collections:
- collection_type: open
  name: Hilos Contact API
  slug: open-hilos-contact-api
- collection_type: open
  name: Hilos Contact Conversation API
  slug: open-hilos-conversation-api
- collection_type: open
  name: Hilos Contact Flow Execution API
  slug: open-hilos-flow-execution-api
- collection_type: open
  name: Hilos Contact Flow Execution Contact API
  slug: open-hilos-flow-execution-contact-api
- collection_type: open
  name: Hilos Contact User API
  slug: open-hilos-user-api
- collection_type: open
  name: Hilos Contact WhatsApp API
  slug: open-hilos-whatsapp-api
common:
- group: other
  href: https://artifacts.apis.io/hilos/capabilities/hilos-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hilos-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/hilos/overlays/hilos-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hilos-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/hilos/security/hilos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hilos-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/hilos/agentic-access/hilos-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hilos-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://hilos.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hilos.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://hilos.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hilos.io/docs/developer/apidocs/contact/get-apicontact
- group: start
  title: ''
  type: GettingStarted
  url: https://hilos.io/docs/developer/getting-started/test-request
- group: auth
  href: https://artifacts.apis.io/hilos/authentication/hilos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hilos-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://hilos.io/blog
- group: commercial
  href: https://artifacts.apis.io/hilos/plans/hilos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hilos-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://hilos.io/signup-ac
- group: start
  title: ''
  type: Login
  url: https://app.hilos.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hilos.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hilos.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:hey@hilos.io
- group: agent
  href: https://artifacts.apis.io/hilos/llms/hilos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hilos-llms.txt
- group: design
  href: https://artifacts.apis.io/hilos/conventions/hilos-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hilos-conventions.yml
- group: design
  href: https://artifacts.apis.io/hilos/errors/hilos-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hilos-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hilos/conformance/hilos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hilos-conformance.yml
- group: design
  href: https://artifacts.apis.io/hilos/lifecycle/hilos-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hilos-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hilos/data-model/hilos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hilos-data-model.yml
- group: agent
  href: https://artifacts.apis.io/hilos/mcp/hilos-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/hilos-mcp.yml
- group: build
  href: https://artifacts.apis.io/hilos/mcp/hilos-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hilos-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/hilos/a2a/hilos-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hilos-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hilos/well-known/hilos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hilos-well-known.yml
- group: build
  href: https://artifacts.apis.io/hilos/packages/hilos-packages.yml
  title: ''
  type: Packages
  url: packages/hilos-packages.yml
- group: operate
  href: https://artifacts.apis.io/hilos/rate-limits/hilos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hilos-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/hilos/asyncapi/hilos-events.yml
  title: ''
  type: Events
  url: asyncapi/hilos-events.yml
- group: agent
  href: https://artifacts.apis.io/hilos/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Hilos is a WhatsApp Business Platform automation company (backed by 500 Global and Techstars, now part of ActiveCampaign) that helps businesses capture leads, qualify prospects, and automate follow-ups over WhatsApp''s Cloud API. Its REST API exposes contacts, inbox conversations, WhatsApp message templates, and no-code flow executions, authenticated with an `Authorization: Token` API key against https://api.hilos.io/api/ and paginated with `page` / `page_size` query parameters.'
finops:
- has_sources: true
  method: derived
  name: Hilos Finops
  primary_unit: ''
  service_category: ''
  slug: hilos-finops
  template: true
image: https://app.hilos.io/logo512.png
layout: provider
modified: '2026-08-13'
name: Hilos
nav: Providers
network: true
overview: 'Hilos publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Contact API, Conversation API, Flow Execution API, and 3 more. Tagged areas include Company, WhatsApp, Messaging, Automation, and CRM.


  The Hilos catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hilos'' developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, signup flow, support, and 24 more developer resources.'
plans:
- name: Hilos Plans Pricing
  plan_count: 0
  slug: hilos-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Hilos Rate Limits
  slug: hilos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Hilos API Rules
  rule_count: 57
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 4
  slug: hilos-rules
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 59.4
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/hilos/hilos-2026-07-25T221229.png
security:
- kind: authentication
  name: Hilos Authentication
  slug: hilos-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hilos Domain Security
  slug: hilos-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: Manage inbox conversations
  slug: hilos-manage-inbox-conversations
- name: Send a WhatsApp template message
  slug: hilos-send-whatsapp-template
- name: Sync a contact and run a flow
  slug: hilos-sync-contact-and-run-flow
slug: hilos
tags:
- Company
- WhatsApp
- Messaging
- Automation
- CRM
- Conversational Commerce
- Chatbots
- Customer Engagement
- Marketing
- A2A
website: https://hilos.io
---
