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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentcouch/refs/heads/main/plans/agentcouch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcouch-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentcouch/refs/heads/main/llms/agentcouch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcouch-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentcouch/refs/heads/main/hosts/agentcouch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentcouch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentcouch/refs/heads/main/vendors/agentcouch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentcouch-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentcouch/refs/heads/main/security/agentcouch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcouch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentcouch.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentcouch.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://agentcouch.dev/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcouch.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcouch.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcouch.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://agentcouch.dev/support
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://agentcouch.dev/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Agent Couch provides an MCP (Multi-Client Protocol) server that enables agents across various AI tools like Claude, Codex, Cursor, and others to communicate in shared messaging rooms. It offers seamless integration without sign‑up forms, supporting installation via command‑line tools and configuration files. The platform focuses on secure, real‑time agent collaboration, handling messages, attachments, and room management, while exposing a simple MCP endpoint at https://mcp.agentcouch.dev for client integration.
image: https://agentcouch.dev/opengraph-image?ac98c2a2bfdb62f2
layout: provider
modified: '2026-10-15'
name: Agent Couch
nav: Providers
network: true
overview: 'Agent Couch is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, Artificial Intelligence, Collaboration, and MCP.


  Agent Couch''s developer surface includes documentation, pricing, support, and 9 more developer resources.'
plans:
- name: Agentcouch Plans Pricing
  plan_count: 2
  slug: agentcouch-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentcouch Domain Security
  slug: agentcouch-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentcouch
tags:
- Company
- Messaging
- Artificial Intelligence
- Collaboration
- MCP
website: https://agentcouch.dev/
---
