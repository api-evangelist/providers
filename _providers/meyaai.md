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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Meya Grid HTTP gateway that receives inbound integration and API/webhook events for a Meya app. Webhook URLs follow the format https://grid.meya.ai/gateway/v2/{integration}/{app_id}/{dot_path}.
  name: Meya Grid Gateway
  slug: meya-grid-gateway
artifact_total: 3
asyncapis:
- description: ''
  name: Meyaai Webhooks
  slug: meyaai-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://meya.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meya.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meya.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meya.ai/reference
- group: company
  title: ''
  type: Blog
  url: https://www.meya.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meya-customers
- group: start
  title: ''
  type: SignUp
  url: https://www.meya.ai/article/sign-up
- group: operate
  title: ''
  type: StatusPage
  url: https://meya-v2.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.meya.ai/docs/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meyaai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/meyaai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/meyaai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/meyaai-cli.yml
- group: design
  title: ''
  type: Components
  url: components/meyaai-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/meyaai-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meyaai-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meyaai-domain-security.yml
created: '2026-07-17'
description: Meya is a chatbot and CX-automation platform for building, coding, and launching customer-support conversational apps, digital assistants, and workflow automation. Developers use the Grid platform and Console to script flows in BFML (a YAML syntax with Jinja2 templating) and Python 3 with async I/O, embed the Meya Orb chat UI on web and mobile, and connect messaging, support, NLU, and analytics integrations (WhatsApp, Facebook Messenger, Twilio, Zendesk, Front, Salesforce, Dialogflow, Wit.ai, Segment). The platform exposes an HTTP gateway for inbound integration/API webhooks, a first-party Meya CLI for local development with live push, and the Orb SDKs for web, Flutter, and iOS.
image: https://files.readme.io/0187488-small-meya-wordmark.png
layout: provider
modified: '2026-07-20'
name: Meya.ai
nav: Providers
network: true
overview: 'Meya.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chatbots, Conversational AI, Customer-Support, and CX Automation.


  The Meya.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Meya.ai''s developer surface includes documentation, API reference, engineering blog, signup flow, changelog, CLI, and 11 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 29.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 31.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meyaai/refs/heads/main/screenshots/meyaai-2026-08-07T172812.png
security:
- kind: domain-security
  name: Meyaai Domain Security
  slug: meyaai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meyaai
tags:
- Company
- Chatbots
- Conversational AI
- Customer-Support
- CX Automation
- Messaging
- Webhook
- Developer Platform
website: https://meya.ai
---
