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
    event_surface_described: unknown
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Justcall Agentic Access
  operation_count: 3
  slug: justcall-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: REST API for placing calls, sending SMS and MMS messages, managing contacts, phone numbers, users, and call dispositions in JustCall. Authentication uses an API key and API secret passed in the Author
  name: JustCall REST API
  slug: rest-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: Manage and query voice calls handled through JustCall.
  name: JustCall Calls API
  slug: justcall-calls-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: Create and manage contacts in the JustCall directory.
  name: JustCall Contacts API
  slug: justcall-contacts-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: Send and manage SMS/MMS messages.
  name: JustCall SMS API
  slug: justcall-sms-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The AI Voice Agents API from JustCall — 2 operation(s) for ai voice agents.
  name: JustCall AI Voice Agents API
  slug: justcall-ai-voice-agents-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Appointments API from JustCall — 3 operation(s) for appointments.
  name: JustCall Appointments API
  slug: justcall-appointments-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The JustCall AI API from JustCall — 13 operation(s) for justcall ai.
  name: JustCall JustCall AI API
  slug: justcall-justcall-ai-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Oauth API from JustCall — 5 operation(s) for oauth.
  name: JustCall OAuth API
  slug: justcall-oauth-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Phone Numbers API from JustCall — 3 operation(s) for phone numbers.
  name: JustCall Phone Numbers API
  slug: justcall-phone-numbers-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The RCS API from JustCall — 9 operation(s) for rcs.
  name: JustCall RCS API
  slug: justcall-rcs-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Sales Dialer API from JustCall — 21 operation(s) for sales dialer.
  name: JustCall Sales Dialer API
  slug: justcall-sales-dialer-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Sales Dialer - Phone Numbers API from JustCall — 2 operation(s) for sales dialer - phone numbers.
  name: JustCall Sales Dialer - Phone Numbers API
  slug: justcall-sales-dialer-phone-numbers-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Special Dates API from JustCall — 2 operation(s) for special dates.
  name: JustCall Special Dates API
  slug: justcall-special-dates-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Unified Analytics API from JustCall — 62 operation(s) for unified analytics.
  name: JustCall Unified Analytics API
  slug: justcall-unified-analytics-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The User Groups API from JustCall — 3 operation(s) for user groups.
  name: JustCall User Groups API
  slug: justcall-user-groups-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Users API from JustCall — 3 operation(s) for users.
  name: JustCall Users API
  slug: justcall-users-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Webhooks API from JustCall — 10 operation(s) for webhooks.
  name: JustCall Webhooks API
  slug: justcall-webhooks-api
- baseURL: https://api.justcall.io/v2.1
  baseurl_source: declared
  description: The Whats App API from JustCall — 5 operation(s) for whats app.
  name: JustCall Whats App API
  slug: justcall-whats-app-api
artifact_total: 28
collections:
- collection_type: open
  name: JustCall REST Calls API
  slug: open-justcall-calls-api
- collection_type: open
  name: JustCall REST Calls Contacts API
  slug: open-justcall-contacts-api
- collection_type: open
  name: JustCall REST Calls SMS API
  slug: open-justcall-sms-api
- collection_type: open
  name: JustCall REST API
  slug: open-justcall
common:
- group: other
  href: https://artifacts.apis.io/justcall/capabilities/justcall-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/justcall-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/justcall/agentic-access/justcall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/justcall-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/justcall/security/justcall-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/justcall-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/justcall/security/justcall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/justcall-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/justcall/authentication/justcall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/justcall-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/justcall-io
- group: company
  title: ''
  type: Website
  url: https://justcall.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.justcall.io/docs/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://justcall.io/developer-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://justcall.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://justcall.io/signup
- group: operate
  title: ''
  type: Support
  url: https://help.justcall.io
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.justcall.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://justcall.io/blog/
created: '2026-05-11'
description: JustCall is a cloud-based phone system and contact center platform that provides voice calling, SMS/MMS messaging, IVR, call analytics, and contact management for small and mid-sized businesses. The platform integrates with CRMs, helpdesks, and automation tools. JustCall exposes REST APIs and webhooks for programmatically managing calls, SMS, contacts, phone numbers, and call dispositions, authenticated via API key plus API secret in headers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/justcall.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.justcall.io over HTTP; 4 tools listed.
  name: JustCall MCP Server
  slug: justcall
modified: '2026-05-11'
name: JustCall
nav: Providers
network: true
overview: 'JustCall publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calls API, Contacts API, SMS API, and 15 more. Tagged areas include Voice, SMS, Cloud Phone, Contact Center, and Telephony.


  The JustCall catalog on APIs.io includes 1 Spectral governance ruleset.


  JustCall''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: JustCall API Rules
  rule_count: 50
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 5
  slug: justcall-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 51.8
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 7.9
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 81.0
      total: 21
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/justcall/justcall-2026-06-20T183845.png
security:
- kind: authentication
  name: Justcall Authentication
  slug: justcall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Justcall Domain Security
  slug: justcall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justcall Trust Center
  slug: justcall-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, CSA STAR
slug: justcall
tags:
- Voice
- SMS
- Cloud Phone
- Contact Center
- Telephony
- Communications
website: https://justcall.io
---
