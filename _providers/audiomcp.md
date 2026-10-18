---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The MCP layer that lets any AI agent build, configure, and deploy production voice agents. Describe one and call it in 30 seconds.
  name: audioMCP API
  slug: audiomcp-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/audiomcp/refs/heads/main/llms/audiomcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/audiomcp-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/audiomcp/refs/heads/main/hosts/audiomcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiomcp-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/audiomcp/refs/heads/main/security/audiomcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiomcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiomcp.ai/
coverage:
  checked: '2026-10-16'
  detail: The homepage renders a JavaScript shell and no machine‑readable API spec was found despite probing common spec locations.
  evidence:
  - status: 200
    url: https://audiomcp.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: audioMCP (op.ai) provides a Managed Conversational Platform (MCP) that enables AI agents to build, configure, and deploy production voice agents. Users can describe a voice agent and launch it within seconds, integrating with telephony, speech-to-text, and text-to-speech services. The platform offers tools for scaling, monitoring, and customizing voice interactions for enterprise AI deployments.
image: https://audiomcp.ai/og-image.png
layout: provider
modified: '2026-10-16'
name: op.ai
nav: Providers
network: true
overview: op.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Voice, Conversational AI, Platform, and MCP.
random_paper: 14
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Audiomcp Domain Security
  slug: audiomcp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: audiomcp
tags:
- Artificial Intelligence
- Voice
- Conversational AI
- Platform
- MCP
website: https://audiomcp.ai/
---
