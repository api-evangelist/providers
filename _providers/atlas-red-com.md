---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/atlas-red-com/plans/atlas-red-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlas-red-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/atlas-red-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/atlas-red-com/llms/atlas-red-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlas-red-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/atlas-red-com/well-known/atlas-red-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlas-red-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/atlas-red-com/hosts/atlas-red-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-red-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlas-red-com/vendors/atlas-red-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-red-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlas-red
- group: auth
  href: https://artifacts.apis.io/atlas-red-com/security/atlas-red-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-red-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlas-red.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.atlas-red.com/
- group: operate
  title: ''
  type: Support
  url: https://atlas-red.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.atlas-red.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.atlas-red.com/privacy
coverage:
  checked: '2026-11-02'
  detail: All attempted contract URLs returned HTML pages or 404, with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL found.
  evidence:
  - status: 200
    url: https://app.atlas-red.com/openapi.json
  - status: 404
    url: https://atlas-red.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atlas Red is a mind‑mapping SaaS that offers a pay‑once, subscription‑free product. Users can create unlimited maps, export them to Markdown, OPML, XMindMark and other formats, and keep their data forever. A free tier provides up to 10 maps with full export capabilities, while paid plans unlock additional features. The service emphasizes untangling ideas without recurring fees.
image: https://atlas-red.com/og-image.png
layout: provider
modified: '2026-11-01'
name: Atlas Red
nav: Providers
network: true
overview: 'Atlas Red is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include MindMapping, Productivity, Software-as-a-Service, no-subscription, and Export.


  Atlas Red''s developer surface includes support and 12 more developer resources.'
plans:
- name: Atlas Red Com Plans Pricing
  plan_count: 2
  slug: atlas-red-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Atlas Red Com Rate Limits
  slug: atlas-red-com-rate-limits
scopes:
- name: Atlas Red Com Scopes
  scope_count: 0
  slug: atlas-red-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.6
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 20.2
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlas Red Com Authentication
  slug: atlas-red-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlas Red Com Domain Security
  slug: atlas-red-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atlas-red-com
tags:
- MindMapping
- Productivity
- Software-as-a-Service
- no-subscription
- Export
website: https://atlas-red.com/
---
