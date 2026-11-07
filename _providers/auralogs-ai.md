---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only logging API for AI agents, documented at the developer portal.
  name: Auralogs API
  slug: auralogs-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/auralogs-ai/plans/auralogs-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auralogs-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/auralogs-ai/authentication/auralogs-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auralogs-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/auralogs-ai/llms/auralogs-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auralogs-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/auralogs-ai/hosts/auralogs-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auralogs-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/auralogs-ai/vendors/auralogs-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auralogs-ai-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auralogs-ai
- group: auth
  href: https://artifacts.apis.io/auralogs-ai/security/auralogs-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auralogs-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auralogs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.auralogs.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.auralogs.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://auralogs.ai/use-cases/ai-agent-log-debugging/
- group: company
  title: ''
  type: Blog
  url: https://auralogs.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://auralogs.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auralogs.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auralogs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auralogs.ai/privacy
created: '2026-11-02'
description: Auralogs provides production logging for AI agents, offering read‑only access to structured logs via its MCP API. Teams can query logs, search metadata, and integrate with AI tools like Claude, Cursor, and Codex. The platform includes SDKs for multiple languages, optional GitHub integration, and features for error investigation, incident analysis, and automated PR generation. Auralogs aims to streamline AI‑assisted debugging and improve incident response with searchable, contextual log data.
image: https://auralogs.ai/og-image.png
layout: provider
modified: '2026-11-02'
name: Auralogs
nav: Providers
network: true
overview: 'Auralogs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logging, Artificial Intelligence, Monitoring, SDK, and Production.


  Auralogs'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Auralogs Ai Plans Pricing
  plan_count: 3
  slug: auralogs-ai-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 2.6
  previous_composite: 30.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auralogs Ai Authentication
  slug: auralogs-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Auralogs Ai Domain Security
  slug: auralogs-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auralogs-ai
tags:
- Logging
- Artificial Intelligence
- Monitoring
- SDK
- Production
website: https://auralogs.ai/
---
