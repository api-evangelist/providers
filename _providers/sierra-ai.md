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
artifact_total: 36
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sierra-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sierra-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sierra-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sierra.ai
- group: start
  title: ''
  type: Portal
  url: https://sierra.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sierra.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://sierra.ai/pricing
- group: other
  title: ''
  type: Customers
  url: https://sierra.ai/customers
- group: company
  title: ''
  type: Blog
  url: https://sierra.ai/blog
- group: other
  title: ''
  type: Resources
  url: https://sierra.ai/resources
- group: company
  title: ''
  type: Careers
  url: https://sierra.ai/careers
- group: operate
  title: ''
  type: Contact
  url: https://sierra.ai/contact
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.sierra.ai
- group: other
  title: ''
  type: Events
  url: https://sierra.ai/summit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sierra-ai
- group: other
  title: ''
  type: X
  url: https://twitter.com/sierraplatform
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-24'
description: Sierra is a conversational AI platform for customer experience, founded in 2023 by Bret Taylor (former co-CEO of Salesforce, CTO of Facebook, co-creator of Google Maps, and current chair of OpenAI's board) and Clay Bavor (former Google VP who led Labs, Project Starline, Google Lens, and Google Workspace). Headquartered in New York with offices in San Francisco, Atlanta, London, Paris, Madrid, Toronto, Singapore, and Tokyo, Sierra builds branded AI agents that handle customer service, sales, and operational interactions across chat, voice, SMS, WhatsApp, email, and ChatGPT for enterprises including SiriusXM, WeightWatchers, Sonos, ADT, Chime, Sutter Health, Rocket Mortgage, Ramp, Brex, SoFi, Casper, CLEAR, Vivid Seats, Wayfair, AOL, and approximately 40% of the Fortune 50. The platform is anchored by Agent OS 2.0, with Agent Studio (no-code builder for CX teams), Agent SDK (a developer-facing programmatic layer that lets engineering teams write customer journeys as code), Agent
  Data Platform (persistent cross-session memory unifying structured CRM data and unstructured conversation history), Insights (analytics — Explorer, Monitors, Experiments, Observability), Live Assist (human-in-the-loop), Voice (real-time voice agents), and Ghostwriter (an agent-building agent that generates production-ready multilingual agents from SOPs, transcripts, audio recordings, whiteboard photos, or plain English in 30+ languages). Sierra runs an outcome-based pricing model — customers pay per resolved case, not per seat or per token — and operates a gated developer documentation portal at docs.sierra.ai available only to contracted customers. There is no public REST API, no public Agent SDK package, no public GitHub org, and no self-serve sign-up; access is via enterprise sales. Sierra raised $950M at a $15.8B valuation in May 2026 (after a $350M round at $10B earlier in the year) and reported $150M ARR within roughly two years of public launch. Sierra also acquired the French agent-evaluation
  startup Fragment in April 2026 and publishes the public τ-bench, τ-voice, and τ-knowledge benchmarks for evaluating agentic systems.
features:
- description: Multi-channel agent operating system spanning chat, voice, email, SMS, WhatsApp, ChatGPT, and contact-center integrations with shared memory, learning, and live human assist.
  name: Agent OS 2.0
- description: No-code builder for CX teams to design agents using natural-language instructions and a collaborative workspace with simulations and guardrails.
  name: Agent Studio
- description: Developer-facing programmatic layer that lets engineering teams write customer journeys as code, version them in their existing source control, and orchestrate composable skills and multi-step workflows.
  name: Agent SDK
- description: Persistent agent memory unifying structured customer data (CRM, billing) with unstructured conversation history to enable personalized, relationship-aware responses across sessions.
  name: Agent Data Platform
- description: Analytics suite — Explorer (deep-research style conversation analysis), Monitors, Experiments, and Observability — for measuring and improving agent performance.
  name: Insights
- description: Human-in-the-loop interface that surfaces real-time answers and captures conversation details to augment human agents.
  name: Live Assist
- description: Real-time voice agents benchmarked publicly via Sierra's τ-voice benchmark; deployable into contact centers and IVR replacements.
  name: Voice
- description: Agent-building agent that ingests SOPs, support transcripts, whiteboard photos, audio recordings, and plain-English descriptions to generate production-ready agents across voice, chat, and email in 30+ languages.
  name: Ghostwriter
- description: Built-in guardrails, evaluations, simulations, and observability targeted at regulated industries (financial services, healthcare, telecom).
  name: Trust and Reliability
- description: Customers pay per resolved case (outcome) rather than per seat or per token, aligning Sierra's revenue with measurable customer outcomes.
  name: Outcome-Based Pricing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sierra-ai.png
integrations:
- description: One-click publish of a Sierra agent into the ChatGPT app directory, extending brand reach inside OpenAI's consumer surface.
  name: ChatGPT
- description: Native deployment of Sierra agents on the WhatsApp Business channel.
  name: WhatsApp
- description: Outbound and inbound SMS agent channels.
  name: SMS
- description: Email-as-a-channel for ticket-grade asynchronous interactions.
  name: Email
- description: Integrations into existing CCaaS deployments for live-assist and voice handoff.
  name: Contact Center Platforms
- description: Agent Data Platform ingests structured customer records from existing CRMs and billing engines.
  name: CRM and Billing Systems
- description: Agent SDK lets teams call any internal or external system from within an agent workflow.
  name: Custom Backends
layout: provider
modified: '2026-05-24'
name: Sierra
nav: Providers
network: true
overview: 'Sierra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Artificial Intelligence, Conversational AI, Customer Experience, and Customer Service.


  Sierra''s developer surface includes developer portal, documentation, pricing, engineering blog, and 12 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 15.6
  delta: -0.3
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sierra-ai/refs/heads/main/screenshots/sierra-ai-2026-06-20T193901.png
security:
- kind: domain-security
  name: Sierra Ai Domain Security
  slug: sierra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sierra Ai Vulnerability Disclosure
  slug: sierra-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Sierra Ai Trust Center
  slug: sierra-ai-trust-center
  summary_line: PCI DSS, HIPAA
slug: sierra-ai
solutions:
- description: Vertical solution for banks, fintechs, and lenders with compliance tooling and case templates.
  name: Financial Services
- description: HIPAA-aligned deployments for payers, providers, and digital health.
  name: Healthcare
- description: Carrier-grade agents for plan changes, troubleshooting, and retention.
  name: Telecommunications
- description: Subscription lifecycle and content support.
  name: Media and Subscriptions
- description: Booking, itinerary changes, and concierge experiences (Woodside Collection).
  name: Travel and Hospitality
- description: Pre-purchase, post-purchase, and loyalty agents.
  name: Retail
- description: Developer tools and SaaS support workflows.
  name: Technology
tags:
- AI
- Artificial Intelligence
- Conversational AI
- Customer Experience
- Customer Service
- Agents
- AI Agents
- Voice
- Contact Center
- Enterprise
- Outcome-Based Pricing
- Agent OS
- Agent SDK
- Ghostwriter
- Bret Taylor
use_cases:
- description: Branded AI agents handle Tier-1 support across chat, voice, SMS, and email — Chime, Ramp, Wilson, and Pendulum report case resolution rates of 70–90%.
  name: Customer Service Automation
- description: Real-time voice agents replace traditional IVR menus for providers such as R1 RCM, Singtel, and ADT, which handles ~2M monthly inquiries.
  name: Voice / IVR Replacement
- description: Conversational agents drive product discovery and conversion (Rocket Mortgage 4× conversion, Sun & Ski 3× conversion, Redfin 2× listing views).
  name: Sales and Conversion
- description: HIPAA-compliant agents for chronic care management, member enrollment, and patient navigation (Sutter Health, Cigna, WeightWatchers).
  name: Healthcare Member Support
- description: Agents for fintech onboarding, account servicing, and dispute resolution (SoFi +33 NPS, Chime 70%+ resolution, Brex 90% faster).
  name: Financial Services
- description: Order tracking, returns, sizing, and personalization across brands like Casper, Minted, ThirdLove, BARK, Chubbies, and Sonos.
  name: Retail and E-Commerce
- description: Subscriber retention and support for SiriusXM (34M subscribers), AOL, Tubi, and WeightWatchers.
  name: Subscription and Media
- description: Plan changes, troubleshooting, and billing for Singtel and Next.
  name: Telecom
- description: Single agent runtime serving multiple brands under one customer (e.g., Imprint).
  name: Multi-Brand Agent Hosting
website: https://sierra.ai
---
