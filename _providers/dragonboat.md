---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
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
    dynamic_client_registration: false
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
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/dragonboat/plans/dragonboat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dragonboat-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dragonboat.io/security/
- group: agent
  href: https://artifacts.apis.io/dragonboat/llms/dragonboat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dragonboat-llms.txt
- group: agent
  href: https://artifacts.apis.io/dragonboat/well-known/dragonboat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dragonboat-well-known.yml
- group: other
  href: https://artifacts.apis.io/dragonboat/hosts/dragonboat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dragonboat-hosts.yml
- group: other
  href: https://artifacts.apis.io/dragonboat/vendors/dragonboat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dragonboat-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dragonboat.io/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://dragonboat.io/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dragonboat.io/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dragonboat.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://dragonboat.io/blog/
- group: auth
  href: https://artifacts.apis.io/dragonboat/security/dragonboat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dragonboat-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dragonboat/security/dragonboat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dragonboat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dragonboat.io/
coverage:
  checked: '2026-10-24'
  detail: OpenAPI endpoints returned HTML pages instead of a JSON/YAML spec
  evidence:
  - status: 200
    url: https://api.dragonboat.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Dragonboat provides an agentic product development lifecycle (PDLC) platform that uses an active ontology to orchestrate strategy, portfolio, and execution across product teams. It offers headless APIs, MCP integration, and tools for product managers, CPOs, and CTOs to automate workflows, gain real‑time insights, and adapt to changing market conditions. The platform integrates with Jira, Azure DevOps, Salesforce, Slack, and Teams, enabling AI agents to act on product data and drive outcomes at scale.
image: https://dragonboat.io/wp-content/uploads/2026/09/09-2026-Product-Portfolio-OS-for-Agentic-PDLC.png
layout: provider
modified: '2026-10-24'
name: Dragonboat
nav: Providers
network: true
overview: 'Dragonboat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Product Management, Portfolio Management, AI Integration, Enterprise Software, and Agile.


  Dragonboat''s developer surface includes pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Dragonboat Plans Pricing
  plan_count: 2
  slug: dragonboat-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 5.3
  previous_composite: 22.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dragonboat/dragonboat-2026-11-03T131019.png
security:
- kind: domain-security
  name: Dragonboat Domain Security
  slug: dragonboat-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Dragonboat Trust Center
  slug: dragonboat-trust-center
  summary_line: SOC 2, GDPR
slug: dragonboat
tags:
- Product Management
- Portfolio Management
- AI Integration
- Enterprise Software
- Agile
website: https://dragonboat.io/
---
