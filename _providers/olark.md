---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Olark Agentic Access
  operation_count: 15
  slug: olark-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 1
apis:
- description: 'Browser-side JavaScript API for controlling the Olark chat widget, including chatbox appearance and behavior, chat conversations, visitor information, attention grabber, greeter and pre-chat surveys, '
  name: Olark JavaScript API
  slug: javascript-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Chatbox visibility and lifecycle
  name: Olark Box API
  slug: olark-box-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Chat conversation and operator control
  name: Olark Chat API
  slug: olark-chat-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Pre-load configuration
  name: Olark Configure API
  slug: olark-configure-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Targeted chat rules
  name: Olark Rules API
  slug: olark-rules-api
- baseURL: https://www.olark.com/api
  baseurl_source: declared
  description: Visitor profile updates
  name: Olark Visitor API
  slug: olark-visitor-api
artifact_total: 18
collections:
- collection_type: open
  name: Olark JavaScript Box API
  slug: open-olark-box-api
- collection_type: open
  name: Olark JavaScript Box Chat API
  slug: open-olark-chat-api
- collection_type: open
  name: Olark JavaScript Box Configure API
  slug: open-olark-configure-api
- collection_type: open
  name: Olark JavaScript Box Rules API
  slug: open-olark-rules-api
- collection_type: open
  name: Olark JavaScript Box Visitor API
  slug: open-olark-visitor-api
- collection_type: open
  name: Olark JavaScript API
  slug: open-olark
common:
- group: other
  href: https://artifacts.apis.io/olark/capabilities/olark-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/olark-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/olark/agentic-access/olark-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/olark-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/olark/security/olark-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/olark-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/olark/security/olark-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/olark-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/olark/authentication/olark-authentication.yml
  title: ''
  type: Authentication
  url: authentication/olark-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/olark
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/olark
- group: company
  title: ''
  type: Website
  url: https://www.olark.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.olark.com/help
- group: docs
  title: ''
  type: API Documentation
  url: https://www.olark.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.olark.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.olark.com/signup
- group: company
  title: ''
  type: Blog
  url: https://blog.olark.com/rss.xml
created: '2026-05-11'
description: Olark is a live chat and AI-powered customer communication platform that enables businesses to engage website visitors in real time through chat, chatbots, WhatsApp, and SMS. The platform combines human support with CoPilot automation for capturing leads, driving sales, and providing 24/7 customer service, and is WCAG 2.1 AA accessibility certified. Olark exposes a browser-side JavaScript API for embedding and customizing the chat widget, plus webhooks and integrations with 100+ external tools.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/olark.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.olark.com over HTTP.
  name: Olark MCP Server
  slug: olark
modified: '2026-05-11'
name: Olark
nav: Providers
network: true
overview: 'Olark publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Box API, Chat API, Configure API, and 3 more. Tagged areas include Live Chat, Customer Service, Chatbots, Customer Engagement, and Messaging.


  The Olark catalog on APIs.io includes 1 Spectral governance ruleset.


  Olark''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Olark API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: olark-rules
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 44.2
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 13.2
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/olark/olark-2026-06-20T190655.png
security:
- kind: authentication
  name: Olark Authentication
  slug: olark-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Olark Domain Security
  slug: olark-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Olark Vulnerability Disclosure
  slug: olark-vulnerability-disclosure
  summary_line: Hackerone
slug: olark
tags:
- Live Chat
- Customer Service
- Chatbots
- Customer Engagement
- Messaging
- Accessibility
website: https://www.olark.com
---
