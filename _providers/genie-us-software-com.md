---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: flavored
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'Six static, anonymous, read-only JSON documents the provider publishes for agents under /machine/ and /.well-known/, mapped by its commerce manifest: products (SKU, price, delivery), capabilities (wit'
  name: Genie-us Software Machine Commerce Discovery
  slug: machine-commerce-discovery
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.genie-us-software.com/
- group: company
  title: ''
  type: About
  url: https://www.genie-us-software.com/about/
- group: other
  title: ''
  type: HowItWorks
  url: https://www.genie-us-software.com/how-it-works/
- group: operate
  title: ''
  type: FAQ
  url: https://www.genie-us-software.com/faq/
- group: auth
  title: ''
  type: Trust
  url: https://www.genie-us-software.com/trust/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.genie-us-software.com/coreos/
- group: start
  title: ''
  type: SignUp
  url: https://www.genie-us-software.com/discoverypass/
- group: operate
  title: ''
  type: Support
  url: https://www.genie-us-software.com/support/
- group: operate
  title: ''
  type: Contact
  url: https://www.genie-us-software.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.genie-us-software.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.genie-us-software.com/privacy/
- group: other
  title: ''
  type: AcceptableUse
  url: https://www.genie-us-software.com/acceptable-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genie-us-software-inc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genie-us-software
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/a2a/genie-us-software-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/genie-us-software-com-a2a.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/plans/genie-us-software-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/genie-us-software-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/rate-limits/genie-us-software-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/genie-us-software-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/llms/genie-us-software-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/genie-us-software-com-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/conventions/genie-us-software-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/genie-us-software-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/lifecycle/genie-us-software-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/genie-us-software-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/conformance/genie-us-software-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/genie-us-software-com-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/regulatory/genie-us-software-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/genie-us-software-com-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/regulatory/genie-us-software-com-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/genie-us-software-com-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/genie-us-software-com/refs/heads/main/security/genie-us-software-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/genie-us-software-com-domain-security.yml
created: '2026-09-19'
description: 'Genie-us Software, Inc. sells CoreOS v1.0, a governance-first set of custom skills, operating instructions and boundaries installed into the AI environment a person already uses (ChatGPT as a Markdown install package, Claude Code as a skills ZIP) — no hosted runtime, one $499 one-time license per person, with DiscoveryPass as the free seven-day evaluation. Rather than an API, the company publishes a small machine-readable commercial discovery surface for agents: an A2A agent card at /.well-known/agent-card.json (discovery-only — no A2A endpoint is deployed), a commerce manifest, and static JSON documents for products, capabilities, evidence, health and a JSON Schema qualification request.'
json_schemas:
- name: Genie-us Software Commercial Qualification Request
  property_count: 6
  slug: genie-us-software-com-qualification
layout: provider
modified: '2026-09-19'
name: Genie-us Software
nav: Providers
network: true
overview: 'Genie-us Software publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Governance, AI Agents, Agent Skills, and A2A.


  Genie-us Software''s developer surface includes FAQ, pricing, signup flow, support, and 20 more developer resources.'
plans:
- name: Genie Us Software Com Plans Pricing
  plan_count: 2
  slug: genie-us-software-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Genie Us Software Com Rate Limits
  slug: genie-us-software-com-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.4
    catalog_earned_first_party: 8.0
    catalog_gap: 66.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 7.2
    developer_ergonomics: 14.3
    discoverability: 62.5
    operational_transparency: 2.6
  previous_composite: 28.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Genie Us Software Com Domain Security
  slug: genie-us-software-com-domain-security
  summary_line: TLSv1.3
slug: genie-us-software-com
tags:
- Company
- AI Governance
- AI Agents
- Agent Skills
- A2A
- Machine Commerce
- Software Licensing
website: https://www.genie-us-software.com/
---
