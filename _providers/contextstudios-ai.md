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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented on the Guides page, but no machine‑readable contract was found.
  name: Context Studios API
  slug: context-studios-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/contextstudios-ai/security/contextstudios-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/contextstudios-ai-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/contextstudios-ai/llms/contextstudios-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contextstudios-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/contextstudios-ai/well-known/contextstudios-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contextstudios-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/contextstudios-ai/well-known/contextstudios-ai-contextstudios-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/contextstudios-ai-contextstudios-security.txt
- group: agent
  href: https://artifacts.apis.io/contextstudios-ai/well-known/contextstudios-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contextstudios-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/contextstudios-ai/hosts/contextstudios-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contextstudios-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/contextstudios-ai/vendors/contextstudios-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contextstudios-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contextstudios.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contextstudios.ai/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.contextstudios.ai/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Context-Studios
- group: docs
  title: ''
  type: Documentation
  url: https://www.contextstudios.ai/guides
- group: company
  title: ''
  type: Blog
  url: https://www.contextstudios.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.contextstudios.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/contextstudios-ai/security/contextstudios-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/contextstudios-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/contextstudios-ai/security/contextstudios-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contextstudios-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.contextstudios.ai/
coverage:
  checked: '2026-11-04'
  detail: Guides page provides documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec could be located.
  evidence:
  - status: 200
    url: https://www.contextstudios.ai/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Context Studios is an AI-native development studio based in Berlin, offering AI agents on MCP, Claude, and GPT integrated into workflows. They deliver production‑ready MVPs within weeks, focusing on custom software, React, TypeScript, and AI integration services for enterprises.
image: https://www.contextstudios.ai/api/og?family=home&locale=en&v=20260920
layout: provider
modified: '2026-11-04'
name: Context Studios
nav: Providers
network: true
overview: 'Context Studios is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Development, Berlin, Studio, and Services.


  Context Studios'' developer surface includes documentation, engineering blog, API reference, and 14 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contextstudios Ai Domain Security
  slug: contextstudios-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contextstudios Ai Vulnerability Disclosure
  slug: contextstudios-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: contextstudios-ai
tags:
- Artificial Intelligence
- Development
- Berlin
- Studio
- Services
website: https://www.contextstudios.ai/
---
