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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 41
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/cresta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cresta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cresta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cresta.com
- group: start
  title: ''
  type: Portal
  url: https://cresta.com/ai-platform
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cresta.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cresta.com
- group: other
  title: ''
  type: Product
  url: https://cresta.com/ai-agent
- group: other
  title: ''
  type: Product
  url: https://cresta.com/agent-assist
- group: other
  title: ''
  type: Product
  url: https://cresta.com/conversation-intelligence
- group: other
  title: ''
  type: Product
  url: https://cresta.com/knowledge-agent
- group: other
  title: ''
  type: Product
  url: https://cresta.com/quality-management
- group: other
  title: ''
  type: Company
  url: https://cresta.com/about
- group: company
  title: ''
  type: Careers
  url: https://cresta.com/careers
- group: company
  title: ''
  type: Blog
  url: https://cresta.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://cresta.com/news
- group: learn
  title: ''
  type: Webinars
  url: https://cresta.com/webinars
- group: other
  title: ''
  type: Customers
  url: https://cresta.com/customers
- group: auth
  title: ''
  type: TrustCenter
  url: https://cresta.com/trust
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cresta.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cresta.com/terms
- group: auth
  title: ''
  type: Security
  url: https://cresta.com/security
- group: operate
  title: ''
  type: Support
  url: https://cresta.com/support
- group: start
  title: ''
  type: Login
  url: https://cresta.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://cresta.com/status
- group: operate
  title: ''
  type: ContactSales
  url: https://cresta.com/demo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cresta
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cresta-inc
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Cresta
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CrestaAI
- group: company
  title: ''
  type: Investors
  url: ''
created: '2026-05-24'
description: Cresta is a Mountain View / Sunnyvale, California contact center AI company spun out of the Stanford AI Lab and founded in 2017 by Zayd Enam, Tim Shi, and Sebastian Thrun. The platform unifies human and AI agents for the enterprise contact center across voice, chat, and SMS, combining real-time agent assist, autonomous voice and digital AI agents, conversation intelligence, a knowledge agent, and automated quality management. Cresta runs a multi-model architecture composed of 20+ large and small language models, fine-tuned on customer-specific transcripts and synthetic data, with enterprise guardrails, supervisory models, and a no-code orchestration surface. The AI Agent supports API-based function calling and Model Context Protocol (MCP) for standardized tool access. Voice integrations span Five9, Genesys (Cloud CX and Engage), NICE CXone, Amazon Connect, Twilio Flex, Talkdesk, 8x8, Vonage, Gladly, TCN, RingCX, Avaya Infinity, Cisco UCCE/PCCE/UCCX, and SIPREC across Oracle,
  Ribbon, Avaya SBC, and Cisco CUBE via SIP, PSTN transfer, CCaaS native streaming, WebSocket, gRPC, and raw RTP. Cresta is privately held with $270M+ raised across rounds led by Greylock, Andreessen Horowitz, Sequoia, and Tiger Global, with strategic investors including Genesys, Five9, Accenture, Comcast, Qualcomm, JP Morgan, and Workday Ventures. The Cresta API and SDK are private and gated behind a customer / partner engagement; there is no public OpenAPI specification, no public SDK release, and no public developer self-service portal.
features:
- Cresta AI Agent — autonomous voice, chat, and SMS agents resolving end-to-end across 30+ languages
- Agent Assist — real-time AI guidance, knowledge surfacing, and next-best-action for live human agents
- Conversation Intelligence — automated analysis of 100% of customer conversations for insight and revenue surfacing
- Knowledge Agent — proactive real-time answer retrieval from enterprise knowledge bases
- Quality Management — automated QA scoring across 100% of contact center conversations
- Multi-model architecture combining 20+ large and small language models tuned for contact center tasks
- Fine-tuning on customer-proprietary transcripts plus purpose-built synthetic datasets
- No-code Discover / Build / Test / Deploy / Optimize lifecycle for AI workflows
- Agent Operations Center for real-time monitoring, supervision, and intervention
- Enterprise guardrails, supervisory models, and continuous threat detection
- API-based function calling and Model Context Protocol (MCP) tool access from AI Agent
- Bidirectional metadata exchange (caller ID, IVR selections, routing data, conversation summaries) during transfers and handoffs
- Voice transport via SIP trunking, PSTN transfer, CCaaS native streaming, WebSocket, gRPC, and raw RTP
- Pull-mode audio retrieval from cloud storage (e.g., AWS KVS) or direct desktop capture
- Warm transfer, cold transfer, conference bridge, and multi-party call tracking
- Shared conversation memory across channels and human ↔ AI handoffs
- Configurable voice persona — tone, empathy, communication style, pacing, pronunciation
- SOC 2, ISO 27001, HIPAA, and GDPR compliance posture
- Private, gated API and SDK — no public OpenAPI, no public SDK release, no self-service developer signup
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cresta.png
integrations:
- description: Voice integration with Five9 Intelligent CX Platform via native streaming.
  name: Five9
- description: Native real-time voice and digital streaming integration with Genesys Cloud CX.
  name: Genesys Cloud CX
- description: On-premise / hybrid integration with Genesys Engage.
  name: Genesys Engage
- description: Real-time voice and digital integration with NICE CXone.
  name: NICE CXone
- description: Real-time voice integration with Amazon Connect via Kinesis Video Streams.
  name: Amazon Connect
- description: Real-time voice and digital integration with Twilio Flex via Media Streams.
  name: Twilio Flex
- description: Voice and digital channel integration with Talkdesk.
  name: Talkdesk
- description: Voice integration with 8x8 contact center.
  name: 8x8
- description: Voice integration with Vonage Contact Center.
  name: Vonage
- description: Digital channel integration with Gladly.
  name: Gladly
- description: Voice integration with TCN cloud contact center.
  name: TCN
- description: Voice integration with RingCentral RingCX.
  name: RingCX
- description: Voice integration with Avaya Infinity Experience Platform.
  name: Avaya Infinity
- description: On-premise Cisco contact center integration via desktop capture and SIP.
  name: Cisco UCCE / PCCE / UCCX
- description: On-premise Avaya integration.
  name: Avaya (on-prem)
- description: SIPREC recording integration across Oracle, Ribbon, Avaya SBC, and Cisco CUBE.
  name: SIPREC
- description: CRM integration for customer context and screen pop.
  name: Salesforce
- description: Standardized tool access for AI Agent function calling.
  name: Model Context Protocol (MCP)
jsonld:
- class_count: 20
  name: Cresta Context
  property_count: 9
  slug: cresta-context
layout: provider
modified: '2026-05-24'
name: Cresta
nav: Providers
network: true
overview: 'Cresta is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Artificial Intelligence, Contact Center, Contact Center AI, and CCaaS.


  The Cresta catalog on APIs.io includes 1 JSON-LD context.


  Cresta''s developer surface includes developer portal, documentation, engineering blog, support, YouTube channel, and 25 more developer resources.'
random_paper: 75
score:
  band: emerging
  composite: 25.5
  delta: -2.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 12.9
    developer_ergonomics: 23.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cresta/refs/heads/main/screenshots/cresta-2026-06-20T175228.png
security:
- kind: domain-security
  name: Cresta Domain Security
  slug: cresta-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Cresta Vulnerability Disclosure
  slug: cresta-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cresta Trust Center
  slug: cresta-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: cresta
tags:
- AI
- Artificial Intelligence
- Contact Center
- Contact Center AI
- CCaaS
- Customer Experience
- Conversational AI
- Voice AI
- Agent Assist
- Conversation Intelligence
- Knowledge Agent
- Quality Management
- Real-Time Coaching
- After-Call Automation
- Enterprise AI
- MCP
website: https://cresta.com
---
