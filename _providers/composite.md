---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/composite/well-known/composite-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/composite-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.composite.com/
- group: other
  href: https://artifacts.apis.io/composite/hosts/composite-hosts.yml
  title: ''
  type: Hosts
  url: hosts/composite-hosts.yml
- group: other
  href: https://artifacts.apis.io/composite/vendors/composite-vendors.yml
  title: ''
  type: Vendors
  url: vendors/composite-vendors.yml
- group: auth
  href: https://artifacts.apis.io/composite/security/composite-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/composite-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/composite/security/composite-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/composite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://composite.com
- group: company
  title: ''
  type: Blog
  url: https://composite.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://composite.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://composite.com/terms
- group: operate
  title: ''
  type: Support
  url: https://composite.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://composite.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://composite.com
coverage:
  checked: '2026-10-29'
  detail: The provider's website renders only a JavaScript shell, preventing machine‑readable API documentation from being accessed.
  evidence:
  - status: 200
    url: https://composite.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Composite (Composite Sciences, Inc.) is an AI‑powered browser autopilot that runs locally in Chrome, Edge, or Arc to automate repetitive web tasks. The platform lets users describe a task in natural language and watches it get done, offering a free beta with no setup required. It targets professionals seeking to streamline data entry, research, CRM updates, and other browser‑based workflows, providing a downloadable product at zero cost. Founded in 2024 and based in San Francisco, Composite integrates AI to predict user actions, extract information, and interact with web applications without requiring custom API integrations.
image: https://imagedelivery.net/ihXHxFMfVWH7HR2jdEkB_A/08358984-b75b-4af6-af40-fa319c9ce000/optimal
layout: provider
modified: '2026-10-29'
name: Composite
nav: Providers
network: true
overview: 'Composite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Automation, Browser, SaaS, and Productivity.


  Composite''s developer surface includes engineering blog, support, pricing, signup flow, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Composite Domain Security
  slug: composite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Composite Trust Center
  slug: composite-trust-center
  summary_line: SOC 2
slug: composite
tags:
- AI
- Automation
- Browser
- SaaS
- Productivity
- Company
website: https://composite.com
---
