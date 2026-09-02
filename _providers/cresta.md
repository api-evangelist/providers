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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Cresta's production API host. https://api.cresta.com resolves and answers anonymously with a gRPC-JSON transcoding gateway error envelope ({"code":2,"httpStatus":500,"message":"the requested gRPC meth
  name: Cresta Platform API
  slug: cresta-platform-api
artifact_total: 51
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
- group: auth
  title: ''
  type: Security
  url: https://cresta.com/trust
- group: auth
  title: ''
  type: Compliance
  url: conformance/cresta-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cresta-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cresta-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cresta.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cresta-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cresta-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cresta-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/cresta-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://cresta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cresta.com
- group: start
  title: ''
  type: Portal
  url: https://cresta.com/platform-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cresta.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.cresta.com
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
  url: https://cresta.com/about-us
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
  url: https://cresta.com/press
- group: other
  title: ''
  type: Resources
  url: https://cresta.com/resources
- group: other
  title: ''
  type: Customers
  url: https://cresta.com/customer-stories
- group: auth
  title: ''
  type: TrustCenter
  url: https://cresta.com/trust
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cresta.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cresta.com/legal/terms-of-service
- group: operate
  title: ''
  type: SLA
  url: https://cresta.com/legal/service-level-agreement
- group: commercial
  title: ''
  type: Legal
  url: https://cresta.com/legal
- group: operate
  title: ''
  type: Support
  url: https://cresta.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://login.cresta.com
- group: company
  title: ''
  type: Partners
  url: https://cresta.com/partner
- group: other
  title: ''
  type: ResponsibleAI
  url: https://cresta.com/responsible-ai
- group: operate
  title: ''
  type: ContactSales
  url: https://cresta.com/request-a-demo
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
description: 'Cresta (legally Cresta Intelligence, Inc.) is a Palo Alto, California enterprise Customer Experience AI company spun out of the Stanford AI Lab and founded in 2017 by Zayd Enam, Tim Shi, and Sebastian Thrun, and led since 2023 by CEO Ping Wu, the former co-founder of Google Contact Center AI. The platform unifies human and AI agents for the enterprise contact center across voice, chat, email, and SMS, combining real-time agent assist, autonomous omnichannel AI agents, conversation intelligence, an AI analyst, a knowledge agent, coaching, a training simulator, and automated quality management, all orchestrated through Cresta Opera, a no-code AI orchestration layer, with Cresta Conductor as the developer facing agentic engine for building and optimizing AI agents. Cresta runs a multi-model architecture composed of 20+ large and small language models, fine-tuned on customer-specific transcripts and synthetic data, with enterprise guardrails, supervisory models, and automated pre-release
  AI agent testing. The AI Agent consumes external tools through API-based function calling and the Model Context Protocol; Cresta itself does not publish an MCP server. Voice integrations span Five9, Genesys (Cloud CX and Engage), NICE CXone, Amazon Connect, Twilio Flex, Talkdesk, 8x8, Vonage, Gladly, TCN, RingCX, Avaya Infinity, Cisco UCCE/PCCE/UCCX, and SIPREC across Oracle, Ribbon, Avaya SBC, and Cisco CUBE via SIP, PSTN transfer, CCaaS native streaming, WebSocket, gRPC, and raw RTP. Cresta is privately held at Series D with $280M+ raised from Greylock, Andreessen Horowitz, Sequoia, Tiger Global, Coatue, Greenoaks, Lightspeed, Porsche Ventures, World Innovation Lab, and the Qatar Investment Authority, plus strategic investors including Genesys, Five9, Accenture, Comcast, Qualcomm, JP Morgan, and Workday Ventures. It is the first Customer Experience AI provider to hold ISO/IEC 42001 certification, alongside SOC 2 Type II, ISO 27001, HIPAA, GDPR, TISAX, CCPA, and PCI DSS posture. A production
  API host is live at api.cresta.com — a gRPC-JSON transcoding gateway that answers anonymously with a google.rpc.Status error envelope — but the Cresta API and SDK are gated behind a customer / partner engagement: there is no public OpenAPI specification, no published API reference or base-path documentation, no public SDK release on any package registry, no public pricing, and no developer self-service signup.'
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
- Cresta Opera — no-code AI orchestration layer underneath every product
- Cresta Conductor — developer-facing agentic engine for building, testing, and optimizing AI agents
- AI Agent consumes external tools via API function calling and MCP (Cresta is an MCP client, not an MCP server)
- Bidirectional metadata exchange (caller ID, IVR selections, routing data, conversation summaries) during transfers and handoffs
- Voice transport via SIP trunking, PSTN transfer, CCaaS native streaming, WebSocket, gRPC, and raw RTP
- Pull-mode audio retrieval from cloud storage (e.g., AWS KVS) or direct desktop capture
- Warm transfer, cold transfer, conference bridge, and multi-party call tracking
- Shared conversation memory across channels and human ↔ AI handoffs
- Configurable voice persona — tone, empathy, communication style, pacing, pronunciation
- ISO/IEC 42001, SOC 2 Type II, ISO 27001, HIPAA, GDPR, TISAX, and CCPA compliance posture
- Live production API host at api.cresta.com — a gRPC-JSON transcoding gateway, confirmed by anonymous probe
- Public Atlassian Statuspage with a machine-readable v2 JSON API and RSS incident history
- RFC 9116 security.txt with HackerOne submission form and PGP key
- First-party page written for AI assistants at cresta.com/llm-info ("Hey AI, learn about us")
- Private, gated API and SDK — no public OpenAPI, no public SDK release, no self-service developer signup
- Help center at docs.cresta.com is robots-disallowed with Content-Signal ai-train=no, search=no, ai-input=no
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
modified: '2026-08-14'
name: Cresta
nav: Providers
network: true
overview: 'Cresta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Contact Center, Contact Center AI, CCaaS, and Customer Experience.


  The Cresta catalog on APIs.io includes 1 JSON-LD context.


  Cresta''s developer surface includes developer portal, documentation, engineering blog, legal docs, support, YouTube channel, and 36 more developer resources.'
plans:
- name: Cresta Plans Pricing
  plan_count: 0
  slug: cresta-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cresta Rate Limits
  slug: cresta-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 30.1
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cresta/refs/heads/main/screenshots/cresta-2026-06-20T175228.png
security:
- kind: domain-security
  name: Cresta Domain Security
  slug: cresta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cresta Vulnerability Disclosure
  slug: cresta-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Cresta Trust Center
  slug: cresta-trust-center
  summary_line: ISO/IEC 42001, SOC 2 Type II, ISO 27001, PCI DSS, HIPAA, GDPR, TISAX, CCPA
slug: cresta
tags:
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
- Customer Experience AI
- AI Agents
- gRPC
- Speech Analytics
- Enterprise Software
website: https://cresta.com
---
