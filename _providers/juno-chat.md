---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote streamable-HTTP MCP server (serverInfo Juno Health Tools 1.1.0) with five read-only, consent-gated tools (find_symptom_words, build_health_timeline, prepare_appointment_brief, reflect_on_flare,
  name: Juno Open Health Tools MCP Server
  slug: juno-open-health-tools-mcp-server
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/juno-chat/integrations/juno-chat-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/juno-chat-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/juno-chat/llms/juno-chat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/juno-chat-llms.txt
- group: build
  href: https://artifacts.apis.io/juno-chat/mcp/juno-chat-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/juno-chat-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/juno-chat/mcp/juno-chat-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/juno-chat-mcp.yml
- group: agent
  href: https://artifacts.apis.io/juno-chat/well-known/juno-chat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/juno-chat-well-known.yml
- group: other
  href: https://artifacts.apis.io/juno-chat/hosts/juno-chat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/juno-chat-hosts.yml
- group: other
  href: https://artifacts.apis.io/juno-chat/vendors/juno-chat-vendors.yml
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
  url: https://github.com/MarshallBear1/juno-open-health-tools/blob/main/app/README.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/MarshallBear1/juno-open-health-tools
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/MarshallBear1/juno-open-health-tools
- group: other
  title: ''
  type: DOI
  url: https://doi.org/10.5281/zenodo.21730086
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
- group: start
  title: ''
  type: SignUp
  url: https://play.google.com/store/apps/details?id=com.junochat.app
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
  href: https://artifacts.apis.io/juno-chat/security/juno-chat-domain-security.yml
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
description: Juno (junocompanion.com), operated by SharedGenes, Inc., is a Y Combinator-backed (P26) consumer digital-health startup building an AI personal health assistant for the 1B+ people living with chronic illness. The Juno mobile app (iOS and Android) builds a longitudinal health profile through conversation, biometrics, and medical history to deliver personalized symptom guidance, automated symptom tracking by text or voice, trigger-pattern identification, and appointment-ready reports for clinicians. It supports conditions including fibromyalgia, long COVID, POTS, ME/CFS, EDS, endometriosis, lupus, and MS, and is informed by research from Oxford and UCL plus 1,000+ patient interviews. Founded in 2025 by Marshall Gould (CEO) and Isaac Tolley (CTO); HIPAA-aligned infrastructure with no health data sold. Juno also publishes Juno Open Health Tools, an MIT-licensed remote MCP server at https://juno-health-tools.vercel.app/api/mcp with five read-only, consent-gated tools that turn a
  user's non-identifying health notes into non-diagnostic appointment-preparation material; it is listed in the official MCP Registry and archived on Zenodo (DOI 10.5281/zenodo.21730086). Juno publishes no REST API or SDK.
image: https://junocompanion.com/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at juno-health-tools.vercel.app over streamable HTTP; 5 tools listed.
  name: io.github.MarshallBear1/juno-open-health-tools
  slug: io-github-marshallbear1-juno-open-health-tools
modified: '2026-07-19'
name: Juno Chat
nav: Providers
network: true
overview: 'Juno Chat is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Health, Chronic Illness, AI Health Assistant, and Symptom Tracking.


  Juno Chat''s developer surface includes documentation, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 75.8
    operational_transparency: 5.3
  previous_composite: 16.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/juno-chat/juno-chat-2026-07-25T223327.png
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
