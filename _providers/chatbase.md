---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Chatbase Agentic Access
  operation_count: 16
  slug: chatbase-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 1
apis:
- baseURL: https://www.chatbase.co/api/v1
  baseurl_source: declared
  description: Message an agent and receive a response, with optional streaming.
  name: Chatbase Chat API
  slug: chatbase-chat-api
- baseURL: https://www.chatbase.co/api/v1
  baseurl_source: declared
  description: Create, retrain, configure, list, and delete chatbots/agents.
  name: Chatbase Chatbots API
  slug: chatbase-chatbots-api
- baseURL: https://www.chatbase.co/api/v1
  baseurl_source: declared
  description: Manage contacts and custom attributes for a chatbot.
  name: Chatbase Contacts API
  slug: chatbase-contacts-api
- baseURL: https://www.chatbase.co/api/v1
  baseurl_source: declared
  description: Retrieve conversation history for a chatbot.
  name: Chatbase Conversations API
  slug: chatbase-conversations-api
- baseURL: https://www.chatbase.co/api/v1
  baseurl_source: declared
  description: Retrieve leads captured by a chatbot.
  name: Chatbase Leads API
  slug: chatbase-leads-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chatbase Chat API
  slug: open-chatbase-chat-api
- collection_type: open
  name: Chatbase Chat Chatbots API
  slug: open-chatbase-chatbots-api
- collection_type: open
  name: Chatbase Chat Contacts API
  slug: open-chatbase-contacts-api
- collection_type: open
  name: Chatbase Chat Conversations API
  slug: open-chatbase-conversations-api
- collection_type: open
  name: Chatbase Chat Leads API
  slug: open-chatbase-leads-api
- collection_type: open
  name: Chatbase API
  slug: open-chatbase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chatbase-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chatbase-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chatbase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chatbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatbase
- group: company
  title: ''
  type: Website
  url: https://www.chatbase.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.chatbase.co/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/chatbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chatbase-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.chatbase.co/blog
created: '2026-06-20'
description: Chatbase is a custom AI chatbot and AI agent platform for customer support. Teams train an agent on their own content (websites, files, Q&A), embed it on their site, and connect it to channels and tools. The Chatbase REST API lets developers message agents (with streaming), create and update chatbots/agents, retrieve conversations and leads, and manage contacts.
finops:
- name: Chatbase Finops
  service_category: AI and Machine Learning
  slug: chatbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatbase.png
layout: provider
modified: '2026-06-20'
name: Chatbase
nav: Providers
network: true
overview: 'Chatbase publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Chatbots API, Contacts API, and 2 more. Tagged areas include Artificial Intelligence, Chatbots, AI Agent, Customer-Support, and Conversational AI.


  Chatbase''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Chatbase Plans Pricing
  plan_count: 6
  slug: chatbase-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Chatbase Rate Limits
  slug: chatbase-rate-limits
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatbase/refs/heads/main/screenshots/chatbase-2026-06-20T174234.png
security:
- kind: authentication
  name: Chatbase Authentication
  slug: chatbase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chatbase Domain Security
  slug: chatbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chatbase Vulnerability Disclosure
  slug: chatbase-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Chatbase Trust Center
  slug: chatbase-trust-center
  summary_line: SOC 2, GDPR
slug: chatbase
tags:
- Artificial Intelligence
- Chatbots
- AI Agent
- Customer-Support
- Conversational AI
website: https://www.chatbase.co
---
