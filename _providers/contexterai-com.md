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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/contexterai-com/well-known/contexterai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contexterai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/contexterai-com/hosts/contexterai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contexterai-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/contexterai-com/security/contexterai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contexterai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contexterai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://contexterai.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://contexterai.com/features
- group: auth
  title: ''
  type: Security
  url: https://contexterai.com/security
- group: operate
  title: ''
  type: Help
  url: https://contexterai.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contexterai.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contexterai.com/terms
coverage:
  checked: '2026-11-04'
  detail: The developer portal at https://contexterai.com/developers provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications were found.
  evidence:
  - status: 200
    url: https://contexterai.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Contexter enables users to share AI context across multiple large language model assistants such as ChatGPT, Claude, and Telegram. It provides a unified workspace where prompts, notes, and data can be persisted and accessed by different AI tools, facilitating seamless collaboration and continuity. The platform includes a Telegram bot, ChatGPT plugin, and Claude connector, allowing teams to maintain a single source of truth for AI-driven projects, improve productivity, and avoid redundant re‑prompting.
image: https://contexterai.com/assets/contexter-social-1200x630-v4.png
layout: provider
modified: '2026-11-04'
name: Contexter
nav: Providers
network: true
overview: 'Contexter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Productivity, ChatGPT, and Claude.


  Contexter''s developer surface includes documentation and 9 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contexterai Com Domain Security
  slug: contexterai-com-domain-security
  summary_line: TLSv1.3
slug: contexterai-com
tags:
- Artificial Intelligence
- Collaboration
- Productivity
- ChatGPT
- Claude
- Telegram
- Company
website: https://contexterai.com/
---
