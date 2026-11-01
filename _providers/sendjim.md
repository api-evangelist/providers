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
api_count: 1
apis:
- description: SendJim provides a direct mail marketing platform with an API (not publicly documented).
  name: SendJim API
  slug: sendjim-api
artifact_total: 3
common:
- group: operate
  title: ''
  type: Support
  url: https://support.sendjim.com/sendjim-support
- group: commercial
  href: https://artifacts.apis.io/sendjim/plans/sendjim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sendjim-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/sendjim/hosts/sendjim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sendjim-hosts.yml
- group: other
  href: https://artifacts.apis.io/sendjim/vendors/sendjim-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sendjim-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://members.sendjim.com/Account/Login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SendJim
- group: auth
  href: https://artifacts.apis.io/sendjim/security/sendjim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sendjim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendjim.com/
- group: company
  title: ''
  type: Blog
  url: https://sendjim.com/growth-hub/
- group: commercial
  title: ''
  type: Pricing
  url: https://members.sendjim.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendjim.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendjim.com/privacy-policy/
coverage:
  checked: '2026-10-28'
  detail: SendJim's developer portal pages return JavaScript challenges, preventing access to machine-readable specs.
  evidence:
  - status: 429
    url: https://sendjim.com/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: SendJim provides a direct mail marketing platform that helps home service businesses automate their outreach. It offers features like campaign playbooks, predictive targeting, and integrations with popular tools such as Jobber, ServiceMinder, and Housecall Pro. Users can schedule webinars, access case studies, and explore pricing options, all aimed at simplifying marketing and increasing revenue for service‑based companies.
image: https://sendjim.com/wp-content/uploads/2025/09/Grey_Blue_SendJim_VerticalLogo_2024-scaled.png
layout: provider
modified: '2026-10-28'
name: SendJim
nav: Providers
network: true
overview: 'SendJim is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketing, DirectMail, HomeServices, Automation, and SaaS.


  SendJim''s developer surface includes support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Sendjim Plans Pricing
  plan_count: 3
  slug: sendjim-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 22.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sendjim Domain Security
  slug: sendjim-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sendjim
tags:
- Marketing
- DirectMail
- HomeServices
- Automation
- SaaS
website: https://sendjim.com/
---
