---
agent_readiness:
  band: human-only
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering chatbots, conversational agents, and bot frameworks across messaging, voice, and customer experience channels. Bots are scripted or model-augmented conversational interfaces deployed inside Slack, Discord, Microsoft Teams, Telegram, WhatsApp, web chat widgets, and voice channels. This collection brings together developer-oriented bot frameworks like Microsoft Bot Framework, Botpress, Rasa, Botkit, Hubot, and Errbot alongside SaaS conversational platforms like Intercom, Drift, ManyChat, Tidio, Landbot, Dialogflow, IBM watsonx Assistant, and Amazon Lex. Bots in this collection are distinct from autonomous AI agents — they are conversational, channel-bound interfaces driven by intents, dialog flows, and integration triggers.
examples:
- key_count: 9
  name: Bots Bot Definition Example
  slug: bots-bot-definition-example
- key_count: 10
  name: Bots Conversation Turn Example
  slug: bots-conversation-turn-example
features:
- description: Bot platforms expose adapters that connect a single bot implementation to multiple messaging channels — Slack, Microsoft Teams, Discord, Telegram, WhatsApp, web chat, and voice — without rewriting conversation logic for each surface.
  name: Channel Integration
- description: Conversational AI platforms like Dialogflow, Amazon Lex, IBM watsonx Assistant, and Rasa classify user utterances into intents and extract entities, mapping free-text input to structured actions.
  name: Intent Recognition and NLU
- description: Frameworks model multi-turn conversations as state machines, decision trees, or graph-based flows, tracking conversation context across turns and routing users through branching dialog paths.
  name: Dialog Flow Management
- description: Developer SDKs like Microsoft Bot Framework, Botkit, Botpress, and Hubot provide opinionated abstractions for handling events, sending messages, building cards, and deploying bots to a runtime.
  name: Bot SDKs and Builder Tooling
- description: SaaS platforms like ManyChat, Chatfuel, Tidio, and Landbot offer visual flow editors that let non-developers assemble bots through drag-and-drop nodes, templates, and conditional logic.
  name: Low-Code Bot Builders
- description: Customer support bots integrate with live agent platforms to escalate from automated flows to human agents when intents fall outside the bot's confidence threshold or scope.
  name: Human Handoff and Hybrid Conversations
- description: Bots emit channel-specific rich content — Slack blocks, Discord embeds, Teams adaptive cards, WhatsApp interactive lists — using a unified abstraction or channel-targeted payloads.
  name: Channel-Native Rich Messaging
- description: Voice-bot platforms like Amazon Lex, Amazon Connect, Voiceflow, and Retell AI wire conversational logic into PSTN telephony, IVRs, and voice assistants.
  name: Voice and Telephony Bots
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Workplace messaging platform with a rich bot and app ecosystem; the de facto channel for ChatOps and internal automation bots.
  name: Slack
- description: Microsoft's SDK and channel connector service for building bots that deploy across Teams, Web Chat, Direct Line, SMS, and other channels.
  name: Microsoft Bot Framework
- description: Google Cloud's conversational AI platform with intent classification, entity extraction, and Dialogflow CX visual flow builder.
  name: Google Dialogflow
- description: AWS conversational AI service for building text and voice bots, with native integration to Amazon Connect for contact-center voice flows.
  name: Amazon Lex
- description: Open-source conversational AI platform with a visual flow builder, NLU engine, and channel integrations for self-hosted bots.
  name: Botpress
- description: Customer messaging platform with the Fin AI agent and a long-standing chatbot product for support deflection and proactive messaging.
  name: Intercom
- description: Cloud communications platform exposing SMS, WhatsApp, voice, and chat channels that bot frameworks plug into for omnichannel deployment.
  name: Twilio
- description: Low-code chatbot builder focused on Messenger, Instagram, WhatsApp, and SMS for marketing and conversational commerce.
  name: ManyChat
json_schemas:
- name: BotDefinition
  property_count: 9
  slug: bots-bot-definition
- name: ConversationTurn
  property_count: 10
  slug: bots-conversation-turn
json_structures:
- name: Bots Bot Definition Structure
  property_count: 9
  slug: bots-bot-definition-structure
- name: Bots Conversation Turn Structure
  property_count: 10
  slug: bots-conversation-turn-structure
jsonld:
- class_count: 7
  name: Bots Context
  property_count: 20
  slug: bots-context
layout: provider
modified: '2026-05-19'
name: Bots
nav: Providers
network: true
overview: 'Bots is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Chatbots, Conversational AI, Bot Framework, Slack Bot, and Discord Bot.


  The Bots catalog on APIs.io includes 1 JSON-LD context.


  Bots'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: bots
tags:
- Chatbots
- Conversational AI
- Bot Framework
- Slack Bot
- Discord Bot
- Messaging
- Voicebot
- Customer Support Bot
use_cases:
- description: Conversational bots in platforms like Intercom Fin, Drift, Freshchat, and Zendesk deflect common support questions, qualify tickets, and hand off to human agents with full conversation history.
  name: Customer Support Automation
- description: Sales chatbots from Drift, ManyChat, and Landbot greet website visitors, qualify leads by asking screening questions, and route qualified prospects into CRM pipelines.
  name: Lead Qualification and Marketing
- description: Slack and Teams bots automate routine workflows — deploys, on-call alerts, polls, time tracking — bringing operations into the team's primary chat channel.
  name: Internal Productivity and ChatOps
- description: WhatsApp, Messenger, and Instagram bots powered by Sinch, MessageBird, WATI, and Twilio handle catalog browsing, order placement, payment collection, and shipping notifications.
  name: Conversational Commerce
- description: Recruiting bots like Paradox Olivia screen candidates, schedule interviews, and answer FAQ across SMS, WhatsApp, and career-site chat.
  name: HR and Recruiting Conversations
- description: Voice-bot frameworks from Amazon Lex, Google Dialogflow CX, and Voiceflow replace touch-tone IVRs with natural-language voice flows for contact centers.
  name: IVR Modernization and Voice Bots
- description: Discord and Slack community bots handle onboarding, role assignment, moderation, polls, and gamification for online communities.
  name: Community and Moderation Bots
- description: Bots integrate with knowledge bases and retrieval systems to answer policy, product, and how-to questions in chat using grounded responses.
  name: Knowledge Base Q and A
website: https://apievangelist.com
---
