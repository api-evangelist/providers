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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/certainly/refs/heads/main/plans/certainly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/certainly-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certainly/refs/heads/main/hosts/certainly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/certainly-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/certainly/refs/heads/main/vendors/certainly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/certainly-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/certainly/refs/heads/main/security/certainly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/certainly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.certainlycx.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.certainlycx.com/getting-started-pricing
- group: operate
  title: ''
  type: Support
  url: https://www.certainlycx.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.certainlycx.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/certainlycx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.certainlycx.com/getting-started-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.certainlycx.com/begin-today
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certainlycx.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certainlycx.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/certainlycx/workspace
coverage:
  checked: '2026-10-08'
  detail: Documentation page returns 404, no machine‑readable OpenAPI or other contract found.
  evidence:
  - status: 404
    url: https://www.certainlycx.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Certainly provides AI‑enabled customer experience and support solutions, combining intelligent automation with human oversight to handle routine requests instantly while routing complex interactions to experts. Their platform supports multiple channels, offering speed, consistency, and care across customer support, sales support, and operational workflows. Founded to modernize service operations, Certainly serves enterprises seeking scalable, human‑in‑the‑loop AI for improved service quality and efficiency.
image: https://www.certainlycx.com/logo.png
layout: provider
modified: '2026-10-07'
name: Certainly
nav: Providers
network: true
overview: 'Certainly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Customer Experience, Support, Automation, and Enterprise.


  Certainly''s developer surface includes getting-started guide, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Certainly Plans Pricing
  plan_count: 3
  slug: certainly-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Certainly Domain Security
  slug: certainly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: certainly
tags:
- Artificial Intelligence
- Customer Experience
- Support
- Automation
- Enterprise
website: https://www.certainlycx.com/
---
