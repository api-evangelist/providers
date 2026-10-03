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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: MCP server providing health tools such as find_symptom_words, build_health_timeline, prepare_appointment_brief, reflect_on_flare, render_appointment_brief.
  name: Juno Open Health Tools MCP Server
  slug: juno-open-health-tools-mcp-server
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/llms/juno-chat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/juno-chat-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/mcp/juno-chat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/juno-chat-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/mcp/juno-chat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/juno-chat-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/well-known/juno-chat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/juno-chat-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/hosts/juno-chat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/juno-chat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/vendors/juno-chat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/juno-chat-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://junocompanion.com/media
- group: docs
  title: ''
  type: Documentation
  url: https://developers.instagram.com/
- group: company
  title: ''
  type: Website
  url: https://junocompanion.com/
- group: company
  title: ''
  type: Blog
  url: https://junocompanion.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://junocompanion.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://junocompanion.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://apps.apple.com/app/juno-chronic-illness-support/id6749455368
- group: other
  title: ''
  type: X
  url: https://x.com/junocompanion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/junochat/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/junocompanion/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/security/juno-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/juno-chat-domain-security.yml
coverage:
  checked: '2026-09-28'
  detail: The MCP server provides tool listings via JSON/event-stream but no OpenAPI or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://juno-health-tools.vercel.app/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Juno (junocompanion.com), operated by SharedGenes, Inc., is a Y Combinator-backed (P26) consumer digital-health startup building an AI personal health assistant for the 1B+ people living with chronic illness. The Juno mobile app (iOS and Android) builds a longitudinal health profile through conversation, biometrics, and medical history to deliver personalized symptom guidance, automated symptom tracking by text or voice, trigger-pattern identification, and appointment-ready reports for clinicians. It supports conditions including fibromyalgia, long COVID, POTS, ME/CFS, EDS, endometriosis, lupus, and MS, and is informed by research from Oxford and UCL plus 1,000+ patient interviews. Founded in 2025 by Marshall Gould (CEO) and Isaac Tolley (CTO); HIPAA-aligned infrastructure with no health data sold. Juno is a consumer app and does not currently publish a public developer API, SDKs, or API documentation.
image: https://junocompanion.com/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Juno Chat MCP Server
  slug: juno-chat-mcp-server
modified: '2026-07-19'
name: Juno Chat
nav: Providers
network: true
overview: 'Juno Chat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Chronic Illness, AI Health Assistant, and Symptom Tracking.


  Juno Chat''s developer surface includes documentation, engineering blog, signup flow, and 14 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.6
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.3
    operational_transparency: 0.0
  previous_composite: 10.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/juno-chat/refs/heads/main/screenshots/juno-chat-2026-07-25T223327.png
security:
- kind: domain-security
  name: Juno Chat Domain Security
  slug: juno-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: juno-chat
tags:
- Company
- Digital Health
- Chronic Illness
- AI Health Assistant
- Symptom Tracking
- Consumer Health
- Mobile App
- Y Combinator
website: https://junocompanion.com/
---
