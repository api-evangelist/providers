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
api_count: 1
apis:
- description: API documented on the website but no machine-readable contract found.
  name: BuildMyAgent API
  slug: buildmyagent-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/buildmyagent/refs/heads/main/plans/buildmyagent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildmyagent-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buildmyagent/refs/heads/main/hosts/buildmyagent-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildmyagent-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buildmyagent/refs/heads/main/vendors/buildmyagent-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildmyagent-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buildmyagent/refs/heads/main/security/buildmyagent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildmyagent-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildmyagent.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://buildmyagent.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildmyagent.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildmyagent.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://buildmyagent.io/#faq
coverage:
  checked: '2026-10-16'
  detail: The site returns only a JavaScript shell with no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://buildmyagent.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: BuildMyAgent is an AI automation platform that enables users to create, customize, and deploy intelligent agents that integrate with over 800 applications. The service offers a visual builder, pre‑built templates, and extensive integration options for tools like Gmail, Slack, Salesforce, and more. It targets businesses and developers seeking to automate workflows, enhance customer interactions, and streamline operations through AI‑driven bots. Pricing plans are transparent, and comprehensive documentation guides users from onboarding to advanced customization.
image: https://buildmyagent.io/mean-icon.svg
layout: provider
modified: '2026-10-16'
name: Testmyprompt
nav: Providers
network: true
overview: 'Testmyprompt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, Platform, and Integration.


  Testmyprompt''s developer surface includes pricing, support, and 7 more developer resources.'
plans:
- name: Buildmyagent Plans Pricing
  plan_count: 4
  slug: buildmyagent-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildmyagent Domain Security
  slug: buildmyagent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildmyagent
tags:
- Company
- Artificial Intelligence
- Automation
- Platform
- Integration
- Bots
website: https://buildmyagent.io/
---
