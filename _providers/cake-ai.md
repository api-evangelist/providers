---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Cake Ai Webhooks
  slug: cake-ai-webhooks
common:
- group: design
  href: https://artifacts.apis.io/cake-ai/asyncapi/cake-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cake-ai-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/cake-ai/authentication/cake-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cake-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/cake-ai/llms/cake-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cake-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/cake-ai/a2a/cake-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cake-ai-a2a.yml
- group: auth
  href: https://artifacts.apis.io/cake-ai/well-known/cake-ai-linear-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cake-ai-linear-security.txt
- group: agent
  href: https://artifacts.apis.io/cake-ai/well-known/cake-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cake-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/cake-ai/hosts/cake-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cake-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/cake-ai/vendors/cake-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cake-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cake.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cake.ai/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://console.cake.ai/signin
- group: company
  title: ''
  type: Blog
  url: https://www.cake.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cake.ai/admin/getting-started-console
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cake.ai/
- group: auth
  href: https://artifacts.apis.io/cake-ai/security/cake-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cake-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cake.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://docs.cake.ai/mcp
  - status: 403
    url: https://www.cake.ai/mcp
  - status: 403
    url: https://agents.cake.ai/mcp
  - status: 200
    url: https://www.cake.ai/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Cake provides an AI management platform that lets enterprise engineering teams build, run, and govern AI workloads, including self‑hosted coding agents, data extraction, and generative AI applications. The platform is designed for regulated industries such as insurance, financial services, healthcare, and eCommerce, offering control over code, data, model choices, cost, security, and compliance within a customer’s own cloud environment.
image: https://www.cake.ai/hubfs/Screenshot%202026-05-08%20at%204.16.11%20PM.png
layout: provider
modified: '2026-10-24'
name: Cake
nav: Providers
network: true
overview: 'Cake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI platform, Regulated industries, Coding agents, Data extraction, and Enterprise AI.


  The Cake catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cake''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 18.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cake Ai Authentication
  slug: cake-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cake Ai Domain Security
  slug: cake-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cake-ai
tags:
- AI platform
- Regulated industries
- Coding agents
- Data extraction
- Enterprise AI
- Governance
- Security
website: https://www.cake.ai/
---
