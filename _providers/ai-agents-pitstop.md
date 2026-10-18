---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: AI Jungle's Pitstop platform API providing access to AI‑agent workspace features.
  name: Pitstop API
  slug: pitstop-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/plans/ai-agents-pitstop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ai-agents-pitstop-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/llms/ai-agents-pitstop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ai-agents-pitstop-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/well-known/ai-agents-pitstop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ai-agents-pitstop-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/hosts/ai-agents-pitstop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ai-agents-pitstop-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/vendors/ai-agents-pitstop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ai-agents-pitstop-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ai-agents-pitstop/refs/heads/main/security/ai-agents-pitstop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ai-agents-pitstop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ai-agents-pitstop.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://ai-agents-pitstop.com/pricing.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ai-agents-pitstop.com/privacy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://api.ai-agents-pitstop.com/getting-started
- group: company
  title: ''
  type: Blog
  url: https://ai-agents-pitstop.com/blog/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://api.ai-agents-pitstop.com/mcp/v1
  - status: 401
    url: https://app.ai-agents-pitstop.com/mcp/v1
  - status: 200
    url: https://ai-agents-pitstop.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: AI Jungle provides a modern AI‑powered workspace tailored for professional services firms, enabling executive‑search, advisory, and consulting teams to automate research, drafting, follow‑ups, meeting notes, and CRM updates. The platform combines AI agents with collaborative tools, offering a recurring‑task model, human‑in‑the‑loop approvals, and seamless integration with existing workflows, aiming to boost efficiency and reduce manual effort across the firm.
image: https://ai-agents-pitstop.com/og-image.png
layout: provider
modified: '2026-10-15'
name: AI Jungle
nav: Providers
network: true
overview: 'AI Jungle is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Workspace, Professional-Services, and Automation.


  AI Jungle''s developer surface includes pricing, getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: Ai Agents Pitstop Plans Pricing
  plan_count: 7
  slug: ai-agents-pitstop-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ai Agents Pitstop Domain Security
  slug: ai-agents-pitstop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ai-agents-pitstop
tags:
- Company
- Artificial Intelligence
- Workspace
- Professional-Services
- Automation
website: https://ai-agents-pitstop.com/
---
