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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cryptopulse provides whale and smart money tracking services. Documentation is available at the public website.
  name: Cryptopulse API
  slug: cryptopulse-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/cryptopulse-uno/llms/cryptopulse-uno-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptopulse-uno-llms.txt
- group: other
  href: https://artifacts.apis.io/cryptopulse-uno/hosts/cryptopulse-uno-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptopulse-uno-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptopulse.uno/terms
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@cryptopulse/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptopulse.uno/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptopulse.uno/pricing
- group: start
  title: ''
  type: Login
  url: https://cryptopulse.uno/login
- group: company
  title: ''
  type: Blog
  url: https://cryptopulse.uno/blog
- group: auth
  href: https://artifacts.apis.io/cryptopulse-uno/security/cryptopulse-uno-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptopulse-uno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptopulse.uno/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite public documentation pages.
  evidence:
  - status: 200
    url: https://cryptopulse.uno/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: 'cryptopulse-uno is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://cryptopulse.uno/api/og
layout: provider
modified: '2026-11-04'
name: cryptopulse-uno
nav: Providers
network: true
overview: 'cryptopulse-uno is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include WhaleTracking, Smart Money, On-Chain Analytics, Alerts, and AI Wallet Roast.


  cryptopulse-uno''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptopulse Uno Domain Security
  slug: cryptopulse-uno-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cryptopulse-uno
tags:
- WhaleTracking
- Smart Money
- On-Chain Analytics
- Alerts
- AI Wallet Roast
website: https://cryptopulse.uno/
---
