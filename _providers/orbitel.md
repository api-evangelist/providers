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
  href: https://raw.githubusercontent.com/api-evangelist/orbitel/refs/heads/main/plans/orbitel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orbitel-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orbitel/refs/heads/main/hosts/orbitel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orbitel-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orbitel/refs/heads/main/security/orbitel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orbitel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orbitel.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://orbitel.in/pricing.html
- group: company
  title: ''
  type: Blog
  url: https://orbitel.in/blogs.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orbitel.in/terms&condition.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orbitel.in/privacypolicy.html
- group: company
  title: ''
  type: AboutUs
  url: https://orbitel.in/aboutus.html
- group: operate
  title: ''
  type: Contact
  url: https://orbitel.in/contactus.html
coverage:
  checked: '2026-10-15'
  detail: The homepage redirects to a JavaScript parking page with no developer documentation.
  evidence:
  - status: 200
    url: https://www.orbitel.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Orbitel is an Indian Communications Platform as a Service (CPaaS) provider offering SMS, WhatsApp, Voice, Email, and RCS solutions. The company markets enterprise‑grade messaging infrastructure with regulatory compliance, high delivery uptime, and multi‑channel support. While Orbitel promotes its services on its website, it does not publicly expose API documentation or specifications, focusing instead on reseller and enterprise sales channels.
layout: provider
modified: '2026-10-15'
name: Orbitel
nav: Providers
network: true
overview: 'Orbitel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CPaaS, Messaging, SMS, and WhatsApp.


  Orbitel''s developer surface includes pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Orbitel Plans Pricing
  plan_count: 16
  slug: orbitel-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orbitel Domain Security
  slug: orbitel-domain-security
  summary_line: TLSv1.2 · DMARC
slug: orbitel
tags:
- Company
- CPaaS
- Messaging
- SMS
- WhatsApp
- Voice
- Email
- RCS
website: https://orbitel.in/
---
