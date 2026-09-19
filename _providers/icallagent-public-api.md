---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-09-18'
api_count: 1
apis:
- baseURL: https://api.icallagent.com/api/public/v1/
  baseurl_source: declared
  description: The agents API from iCallAgent Public API — 1 operation(s) for agents.
  name: iCallAgent Public API Agents API
  slug: icallagent-public-api-agents-api
- baseURL: https://api.icallagent.com/api/public/v1/
  baseurl_source: declared
  description: The campaigns API from iCallAgent Public API — 1 operation(s) for campaigns.
  name: iCallAgent Public API Campaigns API
  slug: icallagent-public-api-campaigns-api
- baseURL: https://api.icallagent.com/api/public/v1/
  baseurl_source: declared
  description: The contacts API from iCallAgent Public API — 1 operation(s) for contacts.
  name: iCallAgent Public API Contacts API
  slug: icallagent-public-api-contacts-api
- baseURL: https://api.icallagent.com/api/public/v1/
  baseurl_source: declared
  description: The phone-numbers API from iCallAgent Public API — 1 operation(s) for phone-numbers.
  name: iCallAgent Public API Phone Numbers API
  slug: icallagent-public-api-phone-numbers-api
- baseURL: https://api.icallagent.com/api/public/v1/
  baseurl_source: declared
  description: The webhooks API from iCallAgent Public API — 2 operation(s) for webhooks.
  name: iCallAgent Public API Webhooks API
  slug: icallagent-public-api-webhooks-api
artifact_total: 12
asyncapis:
- description: ''
  name: Icallagent Public Api Webhooks
  slug: icallagent-public-api-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/mcp/icallagent-public-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/icallagent-public-api-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/overlays/icallagent-public-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/icallagent-public-api-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://icallagent.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/security/icallagent-public-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/icallagent-public-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/scopes/icallagent-public-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/icallagent-public-api-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/authentication/icallagent-public-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/icallagent-public-api-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/llms/icallagent-public-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/icallagent-public-api-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/icallagent-public-api/refs/heads/main/packages/icallagent-public-api-packages.yml
  title: ''
  type: Packages
  url: packages/icallagent-public-api-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.icallagent.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://icallagent.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://icallagent.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://icallagent.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://icallagent.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.icallagent.com
created: '2026-09-15'
description: 'Partner REST API for iCallAgent, a platform for building and operating AI voice agents that hold real-time phone/web conversations via an ASR-LLM-TTS pipeline. The API lets third-party apps act on a user''s workspace: managing agents, outbound campaigns, contacts, phone numbers, and webhooks.'
layout: provider
mcp_servers:
- description: ''
  name: iCallAgent Public API (candidate MCP)
  slug: icallagent-public-api-candidate-mcp
modified: '2026-09-15'
name: iCallAgent Public API
nav: Providers
network: true
overview: 'iCallAgent Public API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Campaigns API, Contacts API, and 2 more. Tagged areas include Voice AI, voice ai assistant, Conversational AI, Voice Agents, and telephony / CPaaS.


  The iCallAgent Public API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  iCallAgent Public API''s developer surface includes authentication, pricing, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Icallagent Public Api Plans Pricing
  plan_count: 2
  slug: icallagent-public-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Icallagent Public Api Rate Limits
  slug: icallagent-public-api-rate-limits
scopes:
- name: Icallagent Public Api Scopes
  scope_count: 3
  slug: icallagent-public-api-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 62.8
    developer_ergonomics: 42.3
    discoverability: 66.7
    operational_transparency: 7.9
  previous_composite: 53.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 38.9
security:
- kind: authentication
  name: Icallagent Public Api Authentication
  slug: icallagent-public-api-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Icallagent Public Api Domain Security
  slug: icallagent-public-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: icallagent-public-api
tags:
- Voice AI
- voice ai assistant
- Conversational AI
- Voice Agents
- telephony / CPaaS
- contact center / CCaaS
- Outbound Calling
- speech (ASR/TTS)
- agent tools / MCP
website: https://icallagent.com
---
