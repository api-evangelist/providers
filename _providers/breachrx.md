---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API documentation for BreachRx platform
  name: BreachRx API
  slug: breachrx-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/breachrx/refs/heads/main/llms/breachrx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breachrx-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/breachrx/refs/heads/main/plans/breachrx-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breachrx-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breachrx/refs/heads/main/hosts/breachrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breachrx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/breachrx/refs/heads/main/vendors/breachrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breachrx-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.breachrx.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.breachrx.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.breachrx.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.breachrx.com/leadership/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.breachrx.com/get-started/
- group: company
  title: ''
  type: Blog
  url: https://www.breachrx.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/breachrx/refs/heads/main/security/breachrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breachrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.breachrx.com/
coverage:
  checked: '2026-10-03'
  detail: OpenAPI endpoint returned HTML instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://trust.breachrx.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: BreachRx provides a comprehensive cyber incident response management platform, offering tools such as the Rex Platform™, AI-driven tabletop simulations, out‑of‑band communications, and regulatory intelligence. Their solutions help organizations prepare for, detect, and respond to security incidents, integrating with existing security stacks and providing real‑time guidance and automation to mitigate breach impacts.
image: https://www.breachrx.com/wp-content/uploads/BreachRx-Featured-Image-1200x628px.jpg
layout: provider
modified: '2026-10-03'
name: BreachRx
nav: Providers
network: true
overview: 'BreachRx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Incident Response, Platform, Artificial Intelligence, and Regulatory Intelligence.


  BreachRx''s developer surface includes getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Breachrx Plans Pricing
  plan_count: 0
  slug: breachrx-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Breachrx Domain Security
  slug: breachrx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: breachrx
tags:
- Cybersecurity
- Incident Response
- Platform
- Artificial Intelligence
- Regulatory Intelligence
website: https://www.breachrx.com/
---
