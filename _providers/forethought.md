---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Forethought Agentic Access
  operation_count: 4
  slug: forethought-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: Start and continue Solve conversations.
  name: Forethought Conversations API
  slug: forethought-conversations-api
- description: Inspect workspace-level Solve configuration.
  name: Forethought Metadata API
  slug: forethought-metadata-api
- description: Predict labels for customer-support tickets.
  name: Forethought Predictions API
  slug: forethought-predictions-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Forethought Solve Conversations API
  slug: open-forethought-conversations-api
- collection_type: open
  name: Forethought Solve Conversations Metadata API
  slug: open-forethought-metadata-api
- collection_type: open
  name: Forethought Solve Conversations Predictions API
  slug: open-forethought-predictions-api
- collection_type: open
  name: Forethought Solve API
  slug: open-forethought-solve-api
- collection_type: open
  name: Forethought Triage API
  slug: open-forethought-triage-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forethought-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/forethought-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forethought-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forethought-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://forethought.ai
- group: start
  title: ''
  type: Portal
  url: https://forethought.ai/platform
- group: docs
  title: ''
  type: Documentation
  url: https://support.forethought.ai/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.forethought.ai/hc/en-us/articles/31636750750227-Solve-API-Developer-Reference
- group: docs
  title: ''
  type: Documentation
  url: https://support.forethought.ai/hc/en-us/articles/26701042038419-Triage-API-Guide-for-Users
- group: commercial
  title: ''
  type: Pricing
  url: https://forethought.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/forethought-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forethought-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forethought-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://forethought.ai/resource-center
- group: company
  title: ''
  type: Blog
  url: https://engineering.forethought.ai/blog/
- group: company
  title: ''
  type: Careers
  url: https://forethought.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://forethought.ai/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forethought-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/forethought_ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Forethought-Technologies
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Forethought-Technologies/solve-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Forethought-Technologies/solve-android
- group: build
  title: ''
  type: Tools
  url: https://github.com/Forethought-Technologies/AutoChain
- group: docs
  title: ''
  type: Documentation
  url: https://autochain.forethought.ai
- group: other
  title: ''
  type: Channels
  url: ''
- group: other
  title: ''
  type: Customers
  url: ''
created: '2026-05-24'
description: 'Forethought is a San Francisco-based generative AI customer-support platform. Its multi-agent product suite — Solve (omnichannel resolution), Triage (ticket classification and routing), Discover (knowledge-gap detection and article generation), Assist (agentic copilot for human agents), and Agent QA (automated quality scoring) — is powered by SupportGPT, Forethought''s fine-tuned generative AI engine. The platform supports chat, email, voice, Slack, mobile, and a Headless API channel, and integrates with Zendesk, Salesforce, Intercom, Front, Gorgias, Genesys, Five9, LiveChat, and knowledge sources including Notion, Document360, and Stonly. Forethought exposes two public REST APIs on the Enterprise plan: the Solve API (https://app.forethought.ai/solve/api/v1) for starting and continuing AI conversations and inspecting workspace context variables, and the Triage API (https://api.forethought.ai/api/predict) for classifying tickets against customer-trained models. Public iOS and
  Android SDKs (Forethought- Technologies/solve-ios, solve-android) embed Solve into mobile apps. The Forethought engineering team also maintains AutoChain, an open-source lightweight framework for building and testing LLM agents. Forethought is now part of Zendesk.'
examples:
- key_count: 2
  name: Solve Continue Conversation Example
  slug: solve-continue-conversation-example
- key_count: 2
  name: Solve Metadata Example
  slug: solve-metadata-example
- key_count: 2
  name: Solve Start Conversation Example
  slug: solve-start-conversation-example
- key_count: 2
  name: Triage Predict Example
  slug: triage-predict-example
features:
- Solve — omnichannel AI agent with end-to-end resolution across chat, email, voice, Slack, mobile, and headless API
- Triage — customer-trained ticket classification with ranked predictions and confidence scores
- Discover — automatic knowledge-gap detection and AI-drafted knowledge-base articles and Autoflows
- Assist — agentic AI copilot for human agents (ticket summaries, resolution guidance, AI-generated replies)
- Agent QA — automated quality reviews against customizable rubrics with performance dashboards
- SupportGPT — fine-tuned generative AI engine grounded in customer conversation history
- Autoflows — generative AI workflows that fully resolve customer issues end-to-end
- Context Variables — typed values (string, number, boolean, list, object) passed into Solve conversations
- Multilingual support across Solve and Triage
- Multi-brand support (2 brands Professional, 20 brands Enterprise)
- Browser Agent — operates inside the browser to interact with legacy applications without backend APIs
- Headless API channel for embedding into custom applications
- Outbound Call API for voice automation (provisioned by Customer Success)
- Public Solve iOS and Android SDKs (Apache-2.0)
- AutoChain — open-source lightweight framework for building and testing LLM agents (1.8k+ GitHub stars)
- Bearer-token authentication on both Solve API and Triage API
- Forethought API access available on the Enterprise plan
- Now part of Zendesk (acquired)
finops:
- name: Forethought Finops
  service_category: AI and Machine Learning
  slug: forethought-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forethought.png
integrations:
- category: Helpdesk
  name: Zendesk
- category: CRM
  name: Salesforce
- category: Helpdesk
  name: Intercom
- category: Contact Center
  name: Genesys
- category: Contact Center
  name: Five9
- category: Helpdesk
  name: Gorgias
- category: Chat
  name: LiveChat
- category: Helpdesk
  name: Front
- category: Knowledge
  name: Notion
- category: Knowledge
  name: Document360
- category: Knowledge
  name: Stonly
- category: API Connector
  name: Airtable
- category: API Connector
  name: Snowflake
- category: Contact Center
  name: 8x8
- category: Channel
  name: Slack
json_schemas:
- name: Forethought Solve Context Variable
  property_count: 4
  slug: forethought-context-variable
- name: Forethought Solve Conversation
  property_count: 12
  slug: forethought-conversation
- name: Forethought Triage Prediction
  property_count: 4
  slug: forethought-triage-prediction
json_structures:
- name: Forethought Conversation Structure
  property_count: 0
  slug: forethought-conversation-structure
- name: Forethought Triage Prediction Structure
  property_count: 0
  slug: forethought-triage-prediction-structure
jsonld:
- class_count: 0
  name: Forethought Context
  property_count: 3
  slug: forethought-context
layout: provider
modified: '2026-05-24'
name: Forethought
nav: Providers
network: true
overview: 'Forethought publishes 3 APIs on the [APIs.io](https://apis.io/) network: Conversations API, Metadata API, and Predictions API. Tagged areas include Artificial Intelligence, Customer-Support, Customer Service, Generative AI, and SupportGPT.


  The Forethought catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Forethought''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, tooling, and 18 more developer resources.'
plans:
- name: Forethought Plans Pricing
  plan_count: 6
  slug: forethought-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Forethought Rate Limits
  slug: forethought-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Forethought API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: forethought-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Forethought API Rules
  rule_count: 5
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 1
  slug: forethought-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 70.7
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 2.6
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forethought/refs/heads/main/screenshots/forethought-2026-06-20T181426.png
security:
- kind: authentication
  name: Forethought Authentication
  slug: forethought-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forethought Domain Security
  slug: forethought-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Forethought Trust Center
  slug: forethought-trust-center
  summary_line: SOC 2, GDPR
slug: forethought
tags:
- Artificial Intelligence
- Customer-Support
- Customer Service
- Generative AI
- SupportGPT
- Conversational AI
- Ticket Triage
- Agentic AI
- Voice AI
- Help Desk
- Multi-Agent
website: https://forethought.ai
---
