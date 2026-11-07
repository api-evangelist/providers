---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dmparrot-com/plans/dmparrot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dmparrot-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dmparrot-com/llms/dmparrot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dmparrot-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dmparrot-com/well-known/dmparrot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dmparrot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dmparrot-com/hosts/dmparrot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dmparrot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dmparrot-com/vendors/dmparrot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dmparrot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dmparrot.com/terms
- group: operate
  title: ''
  type: Support
  url: https://dmparrot.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dmparrot.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dmparrot.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://dmparrot.com/blog
- group: auth
  href: https://artifacts.apis.io/dmparrot-com/security/dmparrot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dmparrot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dmparrot.com/
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.dmparrot.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DMParrot provides Instagram comment-to-DM automation, offering a ManyChat‑like experience for agents. Built on the MCP deterministic engine, it lets AI‑driven tools create comment keyword flows that automatically send private‑reply DMs. The platform supports free and starter pricing, integrates with Meta OAuth, and targets business‑oriented Instagram accounts. It emphasizes reproducible, cost‑free messaging without a visual canvas, focusing on AI‑controlled funnel automation.
image: https://og-image-api.merchantai.workers.dev/?title=DMParrot&subtitle=ManyChat%20for%20agents%20%E2%80%94%20Instagram%20DM%20automation%20via%20MCP&template=tech&type=og
layout: provider
modified: '2026-11-05'
name: DMParrot
nav: Providers
network: true
overview: 'DMParrot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Instagram, Automation, MCP, and Messaging.


  DMParrot''s developer surface includes support, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Dmparrot Com Plans Pricing
  plan_count: 4
  slug: dmparrot-com-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Dmparrot Com Domain Security
  slug: dmparrot-com-domain-security
  summary_line: TLSv1.3
slug: dmparrot-com
tags:
- Artificial Intelligence
- Instagram
- Automation
- MCP
- Messaging
- Company
website: https://dmparrot.com/
---
