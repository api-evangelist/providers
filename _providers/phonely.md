---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Phonely Agentic Access
  operation_count: 3
  slug: phonely-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: Manage Phonely voice agents programmatically. Retrieve a single agent or list all agents for a user, and update agent configuration including voice, greeting message, name, conversation style (Casual,
  name: Phonely Agents API
  slug: phonely-agents-api
- description: Receive structured post-call event data from Phonely after each AI voice interaction completes. The Send Call Data post-call workflow action POSTs a JSON payload containing call metadata, full transcr
  name: Phonely Webhooks API
  slug: phonely-webhooks-api
artifact_total: 59
asyncapis:
- description: Phonely delivers post-call event data to any HTTPS endpoint configured via the "Send Call Data" post-call action in the workflow builder. The event is delivered as an HTTP POST with a JSON body contai
  name: Phonely Webhooks
  slug: phonely-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Phonely Agents API
  slug: open-phonely-agents-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phonely-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phonely-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/phonely-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.phonely.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phonely.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phonely.ai/get-started/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phonely.ai/get-started/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://www.phonely.ai/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.phonely.ai/dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.phonely.ai/blogs
- group: start
  title: ''
  type: Signup
  url: https://app.phonely.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phonely.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phonely.ai/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phonely-ai
- group: other
  title: ''
  type: Customers
  url: https://customers.twilio.com/en-us/phonely
- group: commercial
  title: ''
  type: Plans
  url: https://www.phonely.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/phonely-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phonely-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/phonely-finops.yml
created: '2026-05-24'
description: Phonely is an AI voice agent platform that answers business phone calls in real time with large-language-model-powered conversation, sub-400ms response latency, 1,000+ voices across 100+ languages, and fine-tuned industry models for healthcare, finance, real estate, and insurance. The platform exposes a REST API at app.phonely.ai/api for agent management and a post-call webhook that delivers structured JSON (transcript, summary, sentiment, action items, recording URL) to any HTTPS endpoint after each call. Prebuilt integrations cover Google Calendar, Salesforce, HubSpot, Five9, Zapier, Outlook, Slack, and Gmail; the visual workflow builder also supports importing arbitrary REST APIs from a curl command. Pricing is usage-based with Free, Starter ($50/mo), Pro ($150/mo), and Enterprise tiers — minutes-included plus per-minute overage rather than per-agent seats. The platform is SOC 2, HIPAA, GDPR, CCPA, and PCI compliant.
examples:
- key_count: 2
  name: Phonely Get Agent Example
  slug: phonely-get-agent-example
- key_count: 2
  name: Phonely Get Agents Example
  slug: phonely-get-agents-example
- key_count: 28
  name: Phonely Post Call Event Example
  slug: phonely-post-call-event-example
- key_count: 2
  name: Phonely Update Agent Example
  slug: phonely-update-agent-example
features:
- AI voice agents that answer business phone calls in real time with sub-400ms response latency on dedicated infrastructure
- 1,000+ voices across 100+ languages with voice cloning
- Fine-tuned industry models for healthcare, finance, real estate, insurance, and home services
- Visual workflow builder with API Request blocks for arbitrary REST integrations
- Prebuilt one-click integrations with Google Calendar, Salesforce, HubSpot, Five9, Zapier, Outlook, Slack, Gmail
- Outbound calling campaigns for lead capture, qualification, and follow-up
- SMS conversational AI (Pro plan and above)
- Real-time appointment booking and CRM updates
- Call transcription, AI summaries, sentiment analysis, key points, and action items
- Post-call webhooks delivering structured JSON to any HTTPS endpoint
- A/B testing across agent configurations
- Frontend REST API for agent management with X-Authorization API key auth
- Spam filtering on inbound calls
- SIP trunking on Enterprise plans
- HIPAA, SOC 2, GDPR, CCPA, and PCI compliance
- Usage-based pricing with no per-agent fees — pay only for active AI call time
- 10,000+ customers handling 100,000+ daily calls (per company claims)
- Positioned against Bland AI, Retell AI, Vapi, and Dialora as a contact-center alternative
finops:
- name: Phonely Finops
  service_category: AI and Machine Learning
  slug: phonely-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phonely.png
integrations:
- Google Calendar (one-click)
- Outlook (one-click)
- Gmail (one-click)
- Slack (one-click)
- Salesforce CRM (one-click)
- HubSpot CRM (one-click)
- Five9 contact center (one-click)
- Zapier (one-click)
- Twilio (SIP trunking and number provisioning, enterprise)
- Any REST API via the visual workflow builder "API Request" block (curl import)
json_schemas:
- name: Phonely Agent
  property_count: 0
  slug: phonely-agent
- name: Phonely Post-Call Event
  property_count: 28
  slug: phonely-post-call-event
jsonld:
- class_count: 0
  name: Phonely Context
  property_count: 3
  slug: phonely-context
layout: provider
modified: '2026-05-24'
name: Phonely
nav: Providers
network: true
overview: 'Phonely publishes 2 APIs on the [APIs.io](https://apis.io/) network: Agents API and Webhooks API. Tagged areas include AI, Artificial Intelligence, Voice AI, Voice Agents, and Conversational AI.


  The Phonely catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Phonely''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 12 more developer resources.'
plans:
- name: Phonely Plans Pricing
  plan_count: 4
  slug: phonely-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Phonely Rate Limits
  slug: phonely-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Phonely API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: phonely-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Phonely API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: phonely-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Phonely API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: phonely-rules
score:
  band: developing
  composite: 49.2
  delta: -5.1
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 13.6
    contract_quality: 75.3
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 31.6
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/phonely/refs/heads/main/screenshots/phonely-2026-06-20T191652.png
security:
- kind: authentication
  name: Phonely Authentication
  slug: phonely-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Phonely Domain Security
  slug: phonely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: phonely
tags:
- AI
- Artificial Intelligence
- Voice AI
- Voice Agents
- Conversational AI
- Telephony
- Phone
- Call Center
- Contact Center
- SMS
- Webhooks
- Workflow Automation
- Scheduling
- CRM
use_cases:
- Healthcare appointment scheduling and intake with HIPAA BAA
- Insurance claim intake and qualification
- Contact center / call center automation for SMBs
- Legal intake and lead qualification
- Real estate lead capture and showing scheduling
- Home services dispatch and quoting
- Payment collection and processing over the phone
- Outbound sales outreach and lead qualification campaigns
- After-hours phone answering and ticketing
- Multilingual customer support across 100+ languages
website: https://www.phonely.ai
---
