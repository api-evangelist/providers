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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thoughtly Agentic Access
  operation_count: 12
  slug: thoughtly-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.thoughtly.com
  baseurl_source: declared
  description: Voice and chat agent operations. Agents are referenced as "interviews" in URLs.
  name: Thoughtly agent API
  slug: thoughtly-agent-api
- baseURL: https://api.thoughtly.com
  baseurl_source: declared
  description: Contact management — create, retrieve, update, and call contacts.
  name: Thoughtly contact API
  slug: thoughtly-contact-api
- baseURL: https://api.thoughtly.com
  baseurl_source: declared
  description: Authenticated user details.
  name: Thoughtly user API
  slug: thoughtly-user-api
- baseURL: https://api.thoughtly.com
  baseurl_source: declared
  description: Webhook subscription, unsubscription, and automation triggers.
  name: Thoughtly webhooks API
  slug: thoughtly-webhooks-api
artifact_total: 50
collections:
- collection_type: postman
  name: Thoughtly agent API
  slug: postman-thoughtly-agent-api
- collection_type: postman
  name: Thoughtly agent contact API
  slug: postman-thoughtly-contact-api
- collection_type: postman
  name: Thoughtly agent user API
  slug: postman-thoughtly-user-api
- collection_type: postman
  name: Thoughtly agent webhooks API
  slug: postman-thoughtly-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Thoughtly agent API
  slug: open-thoughtly-agent-api
- collection_type: open
  name: Thoughtly API
  slug: open-thoughtly-api
- collection_type: open
  name: Thoughtly agent contact API
  slug: open-thoughtly-contact-api
- collection_type: open
  name: Thoughtly agent user API
  slug: open-thoughtly-user-api
- collection_type: open
  name: Thoughtly agent webhooks API
  slug: open-thoughtly-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thoughtly/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thoughtly-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/thoughtly-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thoughtly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thoughtly-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://thoughtly.com
- group: start
  title: ''
  type: Portal
  url: https://docs.thoughtly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thoughtly.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thoughtly.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thoughtly.com/getting-started/quick-start
- group: start
  title: ''
  type: Signup
  url: https://app.thoughtly.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.thoughtly.com/login
- group: auth
  title: ''
  type: Authentication
  url: https://app.thoughtly.com/settings/developer
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.thoughtly.com/platform/billing
- group: commercial
  title: ''
  type: Plans
  url: plans/thoughtly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thoughtly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thoughtly-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.thoughtly.com/support/changelog
- group: operate
  title: ''
  type: Support
  url: https://docs.thoughtly.com/support/getting-help
- group: operate
  title: ''
  type: FAQ
  url: https://docs.thoughtly.com/resources/faq
- group: other
  title: ''
  type: Glossary
  url: https://docs.thoughtly.com/resources/glossary/overview
- group: other
  title: ''
  type: Whitepapers
  url: https://docs.thoughtly.com/resources/whitepapers/overview
- group: build
  title: ''
  type: VideoLibrary
  url: https://docs.thoughtly.com/resources/video-library
- group: design
  title: ''
  type: Webhooks
  url: https://docs.thoughtly.com/integrations/webhooks
- group: other
  title: ''
  type: Automations
  url: https://docs.thoughtly.com/automations/getting-started
- group: other
  title: ''
  type: KnowledgeBase
  url: https://docs.thoughtly.com/genius/getting-started
- group: other
  title: ''
  type: AgentBuilder
  url: https://docs.thoughtly.com/build/agent-builder/overview
- group: other
  title: ''
  type: PhoneNumbers
  url: https://docs.thoughtly.com/phone-number/getting-started
- group: other
  title: ''
  type: Voices
  url: https://docs.thoughtly.com/agents/voices
- group: company
  title: ''
  type: BlogPost
  url: https://thoughtly.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thoughtly-ai/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/thoughtlyai
- group: other
  title: ''
  type: AffiliateProgram
  url: https://docs.thoughtly.com/promptbooks/joining-the-thoughtly-affiliate-program
- group: other
  title: ''
  type: ReferralProgram
  url: https://docs.thoughtly.com/support/referral-program
- group: other
  title: ''
  type: Promptbooks
  url: https://docs.thoughtly.com/promptbooks/browse
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thoughtly-vocabulary.yml
created: '2026-05-24'
description: Thoughtly is an AI voice and chat agent platform that helps revenue and support teams contact every lead across every channel — voice, SMS, email, WhatsApp, and iMessage. The product combines a no-code agent designer (decision-tree builder, Vibes AI assistant, Genius knowledge base), a managed telephony layer (purchased numbers, branded calling, BYOC, voice cloning), and a public REST API for programmatically creating contacts, triggering outbound calls, and subscribing to call-completion webhooks. Thoughtly integrates natively with Salesforce, HubSpot, Zoho, GoHighLevel, Keap, Pipedrive, Attio, Calendly, Acuity, Cal.com, Mindbody, Gmail, Slack, Zendesk, Shopify, Zapier, and Make.
examples:
- key_count: 2
  name: Thoughtly Call Contact Example
  slug: thoughtly-call-contact-example
- key_count: 2
  name: Thoughtly Create Contact Example
  slug: thoughtly-create-contact-example
- key_count: 3
  name: Thoughtly New Response Webhook Example
  slug: thoughtly-new-response-webhook-example
- key_count: 2
  name: Thoughtly Subscribe Webhook Example
  slug: thoughtly-subscribe-webhook-example
features:
- No-code Agent Builder with decision-tree nodes, variables, outcomes, and branching logic
- Vibes AI assistant for generating and editing agent workflows from natural language
- Genius knowledge base (RAG) for grounding agents in customer documents and data
- Voice library plus voice cloning and Bring Your Own Key (BYOK) TTS
- Branded calling, Bring Your Own Carrier (BYOC), and phone number purchase/management
- Public REST API for agents, contacts, calls, webhooks, and automations
- Webhook events NEW_RESPONSE, PHONE_TRANSFER, FOLDER_NEW_RESPONSE, FOLDER_PHONE_TRANSFER, ACTION_FAILED
- Webhook-triggered Automations for chaining Agent calls with HTTP, CRM, SMS, and email steps
- Omnichannel agents — voice → SMS → email → WhatsApp follow-up cadence
- Bulk upload + bulk call workflows with Audiences segmentation
- Multilingual agents and call screening bypass
- Mid-call SMS and mid-call website lookup actions
- Analytics dashboard, audit log, and call history with outcome classification
- Workspaces with role-based access and team invites
- Native integrations with 25+ tools including Salesforce, HubSpot, Zapier, Make, and Shopify
- 100 requests per minute API rate limit; subscriber 429s retried once with Retry-After
finops:
- name: Thoughtly Finops
  service_category: ''
  slug: thoughtly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thoughtly.png
json_schemas:
- name: Thoughtly Agent
  property_count: 11
  slug: thoughtly-agent
- name: Thoughtly Call
  property_count: 14
  slug: thoughtly-call
- name: Thoughtly Contact
  property_count: 9
  slug: thoughtly-contact
- name: Thoughtly Webhook
  property_count: 0
  slug: thoughtly-webhook
json_structures:
- name: Thoughtly Call Structure
  property_count: 0
  slug: thoughtly-call-structure
- name: Thoughtly Contact Structure
  property_count: 0
  slug: thoughtly-contact-structure
jsonld:
- class_count: 0
  name: Thoughtly Context
  property_count: 4
  slug: thoughtly-context
layout: provider
modified: '2026-05-24'
name: Thoughtly
nav: Providers
network: true
overview: 'Thoughtly publishes 4 APIs on the [APIs.io](https://apis.io/) network, including agent API, contact API, user API, and 1 more. Tagged areas include Voice AI, Chat AI, Conversational AI, AI Agents, and Outbound Calling.


  The Thoughtly catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thoughtly''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, changelog, and 29 more developer resources.'
plans:
- name: Thoughtly Plans Pricing
  plan_count: 4
  slug: thoughtly-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Thoughtly Rate Limits
  slug: thoughtly-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Thoughtly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thoughtly-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Thoughtly API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 4
  slug: thoughtly-rules
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 84.5
    catalog_earned_first_party: 0.0
    catalog_gap: 30.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 64.5
    commercial_clarity: 64.5
    contract_governance: 28.8
    contract_quality: 65.8
    developer_ergonomics: 48.8
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 44.7
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thoughtly/refs/heads/main/screenshots/thoughtly-2026-06-20T195315.png
security:
- kind: authentication
  name: Thoughtly Authentication
  slug: thoughtly-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Thoughtly Domain Security
  slug: thoughtly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Thoughtly Trust Center
  slug: thoughtly-trust-center
  summary_line: trust center published
slug: thoughtly
tags:
- Voice AI
- Chat AI
- Conversational AI
- AI Agents
- Outbound Calling
- Inbound Calling
- Lead Conversion
- SMS
- WhatsApp
- CRM
- Telephony
website: https://thoughtly.com
---
