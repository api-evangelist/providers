---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Amie Webhooks
  slug: amie-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.amie.so/
- group: start
  title: ''
  type: SignUp
  url: https://calendar.amie.so/login
- group: start
  title: ''
  type: Login
  url: https://calendar.amie.so/login
- group: commercial
  title: ''
  type: Pricing
  url: https://amie.so/pricing
- group: company
  title: ''
  type: Blog
  url: https://amie.so/blog
- group: operate
  title: ''
  type: Support
  url: https://amie.so/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amie.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amie.so/privacy
- group: other
  title: ''
  type: Download
  url: https://amie.so/download
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amie-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amie-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amie-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amie-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amie-llms.txt
created: '2026-07-17'
description: 'Amie is an AI-powered calendar, task, and meeting-notes application for individuals and teams, positioned as an alternative to meeting recorders like Fireflies, Otter, and Fathom. It records calls across platforms without a bot participant, generates AI summaries and action items, intelligently schedules todos, and consolidates calendar and task management in one app. Amie connects to Google Calendar, Gmail, Slack, Notion, Linear, HubSpot, Pipedrive, Todoist, ClickUp, Craft, and Apple Reminders, and processes meetings in many languages with speaker labeling. In update #128 (2026-07-14) Amie shipped an official MCP server that lets AI assistants such as Claude and ChatGPT read a user''s calendar, contacts, tasks, and meeting notes and create todos, plus an in-app outbound webhook surface (Early Access). Amie is backed by Creandum. It does not publish a general-purpose public REST API, OpenAPI spec, SDK, or CLI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amie.png
layout: provider
mcp_servers:
- description: ''
  name: Amie MCP server
  slug: amie-mcp-server
modified: '2026-07-17'
name: Amie
nav: Providers
network: true
overview: 'Amie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Calendar, Productivity, and Meetings.


  The Amie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Amie''s developer surface includes signup flow, pricing, engineering blog, support, changelog, and 9 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 29.6
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amie/refs/heads/main/screenshots/amie-2026-07-25T200056.png
security:
- kind: domain-security
  name: Amie Domain Security
  slug: amie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amie
tags:
- Company
- Consumer
- Calendar
- Productivity
- Meetings
- AI Assistant
- Scheduling
- Task
- Notes
- MCP
website: https://www.amie.so/
---
