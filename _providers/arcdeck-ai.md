---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Arcdeck provides an MCP endpoint for integration with AI tools and custom connectors.
  name: Arcdeck MCP
  slug: arcdeck-mcp
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/arcdeck-ai/llms/arcdeck-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arcdeck-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/arcdeck-ai/well-known/arcdeck-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arcdeck-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/arcdeck-ai/hosts/arcdeck-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arcdeck-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arcdeck-ai/vendors/arcdeck-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arcdeck-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://arcdeck.ai/signin
- group: docs
  title: ''
  type: Documentation
  url: https://arcdeck.ai/guides
- group: auth
  href: https://artifacts.apis.io/arcdeck-ai/security/arcdeck-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arcdeck-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arcdeck.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://arcdeck.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcdeck.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcdeck.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: The MCP endpoint at https://arcdeck.ai/mcp requires authentication (401 Unauthorized).
  evidence:
  - status: 401
    url: https://arcdeck.ai/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Arcdeck is an AI-powered presentation creation platform that transforms user-provided topics, notes, or documents into fully designed slide decks. Leveraging large language models, it generates slide content, designs layouts, and exports editable PowerPoint files in multiple formats such as PDF, DOCX, and PPTX. The service supports 12 languages, offers 48 templates, and provides both free trial decks and premium subscription plans for unlimited use. Arcdeck operates from Sharjah, United Arab Emirates, and emphasizes data privacy, not selling user data or displaying ads.
image: https://arcdeck.ai/opengraph-image
layout: provider
modified: '2026-11-01'
name: Arcdeck
nav: Providers
network: true
overview: 'Arcdeck is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Presentation, Automation, Software-as-a-Service, and Productivity.


  Arcdeck''s developer surface includes documentation, pricing, and 9 more developer resources.'
random_paper: 4
scopes:
- name: Arcdeck Ai Scopes
  scope_count: 0
  slug: arcdeck-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 19.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arcdeck Ai Authentication
  slug: arcdeck-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arcdeck Ai Domain Security
  slug: arcdeck-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arcdeck-ai
tags:
- Artificial Intelligence
- Presentation
- Automation
- Software-as-a-Service
- Productivity
website: https://arcdeck.ai/
---
