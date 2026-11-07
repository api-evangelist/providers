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
    agent_card: conformant
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for Double AIgents private AI platform
  name: Double AIgents API
  slug: double-aigents-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/doubleaigents-com/llms/doubleaigents-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doubleaigents-com-llms.txt
- group: other
  href: https://artifacts.apis.io/doubleaigents-com/a2a/doubleaigents-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/doubleaigents-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/doubleaigents-com/well-known/doubleaigents-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doubleaigents-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/doubleaigents-com/hosts/doubleaigents-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doubleaigents-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/doubleaigents-com/vendors/doubleaigents-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doubleaigents-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doubleaigents.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doubleaigents.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://blog.doubleaigents.com/
- group: auth
  href: https://artifacts.apis.io/doubleaigents-com/security/doubleaigents-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doubleaigents-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doubleaigents.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doubleaigents.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.doubleaigents.com/#about
coverage:
  checked: '2026-11-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.doubleaigents.com/openapi.json
  - status: 404
    url: https://www.doubleaigents.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Double AIgents provides private, on‑premise AI solutions for law firms, wealth managers and regulated professionals. Their platform runs on isolated hardware, offering control, accountability and provability across three pillars. The company focuses on secure, compliant AI deployment for the financial and legal sectors, emphasizing data sovereignty and regulatory adherence.
image: https://www.doubleaigents.com/og-image-v2.png
layout: provider
modified: '2026-11-05'
name: Double AIgents
nav: Providers
network: true
overview: 'Double AIgents is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Private AI, Legal Tech, and Fintech.


  Double AIgents'' developer surface includes engineering blog, pricing, and 10 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Doubleaigents Com Domain Security
  slug: doubleaigents-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: doubleaigents-com
tags:
- Company
- Artificial Intelligence
- Private AI
- Legal Tech
- Fintech
website: https://www.doubleaigents.com/
---
