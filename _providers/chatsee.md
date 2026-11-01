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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/chatsee/llms/chatsee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatsee-llms.txt
- group: other
  href: https://artifacts.apis.io/chatsee/hosts/chatsee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatsee-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.chatsee.ai/newsroom
- group: auth
  href: https://artifacts.apis.io/chatsee/security/chatsee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatsee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatsee.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.chatsee.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.chatsee.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://www.chatsee.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.chatsee.ai/
- group: operate
  title: ''
  type: Support
  url: https://www.chatsee.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.chatsee.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chatsee.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chatsee.ai/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://dev.chatsee.ai/mcp
  - status: 200
    url: https://chatsee.ai
  reason: partner-login
  state: gated
created: '2026-10-24'
description: ChatSee provides an AI runtime feedback platform for enterprise AI systems, offering observability, governance, and reliability tools for autonomous agents. Their solution captures failure events, provides operational learning, and helps product, engineering, and security teams monitor and improve AI agent behavior in production environments.
image: https://framerusercontent.com/assets/oqi1CuzBuWUIP4Yhz2evMxD9k.jpeg
layout: provider
modified: '2026-10-24'
name: ChatSee
nav: Providers
network: true
overview: 'ChatSee is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Observability, Enterprise, and Governance.


  ChatSee''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.9
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
    developer_ergonomics: 45.2
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chatsee Domain Security
  slug: chatsee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chatsee
tags:
- Company
- AI
- Observability
- Enterprise
- Governance
- Monitoring
website: https://chatsee.ai
---
