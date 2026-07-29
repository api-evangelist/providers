---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Cloudtalk Agentic Access
  operation_count: 56
  slug: cloudtalk-agentic-access
  summary_line: 56 operations · 33 acting
api_count: 13
apis:
- description: All data you can get about your agents.
  name: CloudTalk Agents API
  slug: cloudtalk-agents-api
- description: Bulk actions.
  name: CloudTalk Bulks API
  slug: cloudtalk-bulks-api
- description: All data you can get about your calls.
  name: CloudTalk Calls API
  slug: cloudtalk-calls-api
- description: All data you can get about your campaigns.
  name: CloudTalk Campaigns API
  slug: cloudtalk-campaigns-api
- description: All data you can get about your contacts.
  name: CloudTalk Contacts API
  slug: cloudtalk-contacts-api
- description: Conversation Intelligence data about your calls.
  name: CloudTalk Conversation Intelligence API
  slug: cloudtalk-conversation-intelligence-api
- description: CueCards API ver. 1.0.2
  name: CloudTalk CueCard API
  slug: cloudtalk-cuecard-api
- description: The Groups API from CloudTalk — 3 operation(s) for groups.
  name: CloudTalk Groups API
  slug: cloudtalk-groups-api
- description: All data you can get about your numbers.
  name: CloudTalk Numbers API
  slug: cloudtalk-numbers-api
- description: All other helper endpoints.
  name: CloudTalk Other API
  slug: cloudtalk-other-api
- description: Sms handling.
  name: CloudTalk Sms API
  slug: cloudtalk-sms-api
- description: All data you can get about your tags.
  name: CloudTalk Tags API
  slug: cloudtalk-tags-api
- description: VoiceAgent API ver. 1.0.0
  name: CloudTalk VoiceAgent API
  slug: cloudtalk-voiceagent-api
artifact_total: 20
asyncapis:
- description: ''
  name: Cloudtalk Webhooks
  slug: cloudtalk-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cloudtalk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudtalk.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudtalk.io/
- group: operate
  title: ''
  type: Support
  url: https://help.cloudtalk.io/en/
- group: company
  title: ''
  type: Blog
  url: https://www.cloudtalk.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CloudTalk-io
- group: operate
  title: ''
  type: Roadmap
  url: https://releases.cloudtalk.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudtalk.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudtalk.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.cloudtalk.io/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudtalk.io/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudtalk.io/privacy-notice/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudtalk-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudtalk-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/cloudtalk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudtalk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudtalk-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudtalk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cloudtalk.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cloudtalk-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.cloudtalk.io/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudtalk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudtalk-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudtalk-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudtalk-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudtalk-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudtalk-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudtalk-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudtalk-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudtalk.io
created: '2026-07-17'
description: CloudTalk is an AI-powered cloud call center and business phone system (CCaaS) for sales and customer support teams, backed by Point Nine. Its public REST API (served at https://my.cloudtalk.io/api, published as OpenAPI 3.0.1 version 1.7) lets developers automate calls, contacts, agents, groups, phone numbers, campaigns, tags, SMS, blacklists and notes, and read Conversation Intelligence data — transcription, sentiment, topics, talk-listen ratio and smart notes — plus initiate VoiceAgent calls. Authentication is HTTPS-only HTTP Basic Auth using an API Access Key ID and Secret; responses are JSON, paginated with a Collections Envelope, and rate limited to 60 requests per minute per company. Events are delivered through Workflow Automation triggers (native and virtual webhooks) rather than the REST API.
image: https://www.cloudtalk.sk/files/social/1/Share-Img.png
layout: provider
mcp_servers:
- description: ''
  name: cloudtalk-mcp.yml
  slug: cloudtalk-mcpyml
modified: '2026-07-18'
name: CloudTalk
nav: Providers
network: true
overview: 'CloudTalk publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Bulks API, Calls API, and 10 more. Tagged areas include Company, Communications, Voice, VoIP, and Call Center.


  The CloudTalk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudTalk''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 24 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 51.5
  delta: -2.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 61.0
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 54.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 50.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudtalk/refs/heads/main/screenshots/cloudtalk-2026-07-25T205712.png
security:
- kind: authentication
  name: Cloudtalk Authentication
  slug: cloudtalk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudtalk Domain Security
  slug: cloudtalk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudtalk Vulnerability Disclosure
  slug: cloudtalk-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Cloudtalk Trust Center
  slug: cloudtalk-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II, PCI DSS, HIPAA, GDPR, CCPA, CSA STAR, EU-US Data Privacy Framework, UK-US Data Privacy Framework
slug: cloudtalk
tags:
- Company
- Communications
- Voice
- VoIP
- Call Center
- Contact Center
- CCaaS
- Telephony
- SMS
- Conversation Intelligence
website: https://www.cloudtalk.io
---
