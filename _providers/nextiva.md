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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
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
  score: 29.4
  scored_at: '2026-11-06'
api_count: 5
apis:
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: User login and token management operations.
  name: Nextiva Authentication API
  slug: nextiva-authentication-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: Actions specific to managing calls within workitems
  name: Nextiva Call Management API
  slug: nextiva-call-management-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: The Campaigns API from Nextiva — 1 operation(s) for campaigns.
  name: Nextiva Campaigns API
  slug: nextiva-campaigns-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: Operations related to conversations
  name: Nextiva Conversations API
  slug: nextiva-conversations-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: DTMF tone sending for calls
  name: Nextiva DTMF API
  slug: nextiva-dtmf-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: Email-related workitem operations
  name: Nextiva Email API
  slug: nextiva-email-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: Operations for sending and managing SMS messages.
  name: Nextiva SMS Messaging API
  slug: nextiva-sms-messaging-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: The Tickets API from Nextiva — 1 operation(s) for tickets.
  name: Nextiva Tickets API
  slug: nextiva-tickets-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: Operations for transferring workitems
  name: Nextiva Transfers API
  slug: nextiva-transfers-api
- baseURL: https://api.nextiva.com
  baseurl_source: declared
  description: The Work Items API from Nextiva — 4 operation(s) for work items.
  name: Nextiva Work Items API
  slug: nextiva-work-items-api
artifact_total: 27
asyncapis:
- description: ''
  name: Nextiva Events
  slug: nextiva-events
collections:
- collection_type: open
  name: Provider Authentication API
  slug: open-nextiva-authentication
- collection_type: open
  name: Conversation API
  slug: open-nextiva-conversation
- collection_type: open
  name: Provider Authentication API
  slug: open-nextiva-provider-authentication
- collection_type: open
  name: SMS Messaging API
  slug: open-nextiva-sms-messaging
- collection_type: open
  name: Workitem Service API
  slug: open-nextiva-workitem-service
common:
- group: commercial
  href: https://artifacts.apis.io/nextiva/plans/nextiva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nextiva-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.nextiva.com/blog/feed
- group: other
  href: https://artifacts.apis.io/nextiva/capabilities/nextiva-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nextiva-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/nextiva/overlays/nextiva-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextiva-authentication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nextiva/overlays/nextiva-provider-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextiva-provider-authentication-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nextiva/overlays/nextiva-workitem-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextiva-workitem-service-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nextiva/overlays/nextiva-conversation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextiva-conversation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nextiva/overlays/nextiva-sms-messaging-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nextiva-sms-messaging-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.nextiva.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.nextiva.com/nextiva/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nextiva.com/nextiva/docs/overview-of-sdks
- group: docs
  title: ''
  type: APIReference
  url: https://developer.nextiva.com/nextiva/reference/generatetokenwithauthorities
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.nextiva.com/nextiva/docs/sdk-installation
- group: operate
  title: ''
  type: Support
  url: https://help.nextiva.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nextiva.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nextiva
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nextiva.com/nextivapricing
- group: start
  title: ''
  type: Login
  url: https://login.nextiva.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nextiva.com/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nextiva.com/privacy-policy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nextiva.com/
- group: auth
  title: ''
  type: Security
  url: https://www.nextiva.com/security-policy.html
- group: auth
  title: ''
  type: Compliance
  url: https://www.nextiva.com/resources/learn/security-certification-overview
- group: build
  href: https://artifacts.apis.io/nextiva/packages/nextiva-packages.yml
  title: ''
  type: Packages
  url: packages/nextiva-packages.yml
- group: build
  href: https://artifacts.apis.io/nextiva/packages/nextiva-packages.yml
  title: ''
  type: SDKs
  url: packages/nextiva-packages.yml
- group: auth
  href: https://artifacts.apis.io/nextiva/authentication/nextiva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nextiva-authentication.yml
- group: design
  href: https://artifacts.apis.io/nextiva/conventions/nextiva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nextiva-conventions.yml
- group: design
  href: https://artifacts.apis.io/nextiva/errors/nextiva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nextiva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nextiva/conformance/nextiva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nextiva-conformance.yml
- group: design
  href: https://artifacts.apis.io/nextiva/lifecycle/nextiva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nextiva-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/nextiva/security/nextiva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nextiva-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nextiva/security/nextiva-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nextiva-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/nextiva/asyncapi/nextiva-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/nextiva-events.yml
- group: design
  href: https://artifacts.apis.io/nextiva/data-model/nextiva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nextiva-data-model.yml
- group: agent
  href: https://artifacts.apis.io/nextiva/mcp/nextiva-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nextiva-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nextiva/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/nextiva/llms/nextiva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nextiva-llms.txt
created: '2026-07-31'
description: 'Nextiva is a Scottsdale, Arizona based cloud communications and customer experience company whose NextOS / NEXT platform combines UCaaS business phone service, contact center (NCX), SMS and team messaging, voice AI agents, and conversation analytics for small business through enterprise. Its developer surface is the Nextiva Contact Center platform: a ReadMe-hosted developer portal at developer.nextiva.com publishing five REST OpenAPI 3.0 contracts (Provider Authentication, Provider Token Service, Workitem Service, Conversation, SMS Messaging) served from api.nextiva.com, alongside four frontend SDKs (Core, Web, React, React Native) that wrap the same backend over HTTP plus two WebSocket channels — an events socket for real-time workitem, offer, phone-state and live-transcription notifications, and an analytics socket for supervisory data.'
finops:
- has_sources: true
  method: derived
  name: Nextiva Finops
  primary_unit: user
  service_category: ''
  slug: nextiva-finops
  template: false
image: https://files.readme.io/c57cfd17e3ed303431732141b3a42eaff618f7682e4cd2c42e12470ba7ce8878-nextiva_logo_rgb_dark.svg
layout: provider
modified: '2026-10-06'
name: Nextiva
nav: Providers
network: true
overview: 'Nextiva publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Call Management API, Campaigns API, and 7 more. Tagged areas include Company, Communications, Voice, Contact Center, and Customer Experience.


  The Nextiva catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Nextiva''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 30 more developer resources.'
plans:
- name: Nextiva Plans Pricing
  plan_count: 6
  slug: nextiva-plans-pricing
- name: Nextiva Price Estimates
  plan_count: 0
  slug: nextiva-price-estimates
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Nextiva API Rules
  rule_count: 60
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 10
  slug: nextiva-rules
score:
  band: strong
  composite: 58.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 59.5
    catalog_earned_first_party: 12.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 61.3
    discoverability: 78.6
    operational_transparency: 36.8
  previous_composite: 55.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nextiva/nextiva-2026-08-07T185215.png
security:
- kind: authentication
  name: Nextiva Authentication
  slug: nextiva-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Nextiva Domain Security
  slug: nextiva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nextiva Vulnerability Disclosure
  slug: nextiva-vulnerability-disclosure
  summary_line: Hackerone · contact published
skill_count: 4
skills:
- name: Authenticate and control a live Nextiva call
  slug: nextiva-authenticate-and-call-control
- name: Read Nextiva conversation history, transcripts and recordings
  slug: nextiva-conversation-history-and-transcripts
- name: Send an SMS from Nextiva
  slug: nextiva-send-sms
- name: Transfer a Nextiva workitem or send an email response
  slug: nextiva-transfer-and-respond
slug: nextiva
tags:
- Company
- Communications
- Voice
- Contact Center
- Customer Experience
- SMS
- Messaging
- Unified Communications
- VoIP
- Telephony
- Conversational AI
- Call Center
website: https://www.nextiva.com/
---
