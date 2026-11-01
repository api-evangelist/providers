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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bonfire/plans/bonfire-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bonfire-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bonfire/conformance/bonfire-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bonfire-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bonfire/llms/bonfire-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bonfire-llms.txt
- group: auth
  href: https://artifacts.apis.io/bonfire/well-known/bonfire-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bonfire-help-security.txt
- group: agent
  href: https://artifacts.apis.io/bonfire/well-known/bonfire-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonfire-well-known.yml
- group: other
  href: https://artifacts.apis.io/bonfire/hosts/bonfire-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonfire-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonfire/vendors/bonfire-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonfire-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.bonfire.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.bonfire.com/registered-nurse-most-old-men-would-have-give/
- group: company
  title: ''
  type: Blog
  url: https://www.bonfire.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.bonfire.com/en/articles/15935998-complete-your-setup-checklist
- group: docs
  title: ''
  type: Documentation
  url: https://help.bonfire.com/
- group: auth
  href: https://artifacts.apis.io/bonfire/security/bonfire-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonfire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonfire.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonfire.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonfire.com/terms-and-conditions/
coverage:
  checked: '2026-10-27'
  detail: The provider's OpenAPI endpoint returns HTML shell and docs site shows a JavaScript‑rendered placeholder page.
  evidence:
  - status: 200
    url: https://www.bonfire.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Bonfire is an online platform that enables individuals, creators, and organizations to design, sell, and fundraise through custom merchandise. Users can create custom t‑shirts, hoodies, accessories, and more, with Bonfire handling printing, shipping, and customer support. The service supports both personal storefronts and nonprofit fundraising campaigns, offering tools for product design, order management, and integrated payment processing.
image: https://framerusercontent.com/assets/RaxEkb5dvkpqufJjmenxatjZbfY.png
layout: provider
modified: '2026-10-27'
name: Bonfire
nav: Providers
network: true
overview: 'Bonfire is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E‑commerce, Merchandising, Fundraising, and Custom Design.


  Bonfire''s developer surface includes support, signup flow, engineering blog, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Bonfire Plans Pricing
  plan_count: 2
  slug: bonfire-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonfire Domain Security
  slug: bonfire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonfire
tags:
- Company
- E‑commerce
- Merchandising
- Fundraising
- Custom Design
website: https://bonfire.com/
---
