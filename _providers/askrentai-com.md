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
    mcp_server: documented
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
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/askrentai-com/llms/askrentai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askrentai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/askrentai-com/well-known/askrentai-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askrentai-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askrentai-com/hosts/askrentai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askrentai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askrentai-com/vendors/askrentai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askrentai-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/askrentai-com/security/askrentai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askrentai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askrentai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://askrentai.com/rent-manager-api-access
- group: start
  title: ''
  type: GettingStarted
  url: https://askrentai.com/connect
- group: start
  title: ''
  type: SignUp
  url: https://askrentai.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askrentai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askrentai.com/privacy
coverage:
  checked: '2026-11-02'
  detail: OpenAPI spec endpoints returned 401, indicating no public machine‑readable contract.
  evidence:
  - status: 401
    url: https://api.askrentai.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskRentAI provides an AI-powered interface for Rent Manager, enabling Claude, ChatGPT, Gemini, Grok, and custom AI agents to query live rental property data. Users can ask questions about portfolios, receive instant answers, and integrate AI-driven insights into their workflows. The service connects to Rent Manager MCP server, offering natural language access to property management information.
image: https://askrentai.com/og-image.png
layout: provider
modified: '2026-11-01'
name: AskRentAI
nav: Providers
network: true
overview: 'AskRentAI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Real Estate, Property Management, and RentManager.


  AskRentAI''s developer surface includes documentation, getting-started guide, signup flow, and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    mcp: unknown
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
- kind: domain-security
  name: Askrentai Com Domain Security
  slug: askrentai-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: askrentai-com
tags:
- Company
- Artificial Intelligence
- Real Estate
- Property Management
- RentManager
website: https://askrentai.com/
---
