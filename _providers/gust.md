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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Gust provides a developer portal and documentation at gust.helpscoutdocs.com, but no machine‑readable contract was found.
  name: Gust API
  slug: gust-api-2
- baseURL: https://api.inspectall.com
  baseurl_source: declared
  description: The Accounts API from Gust — 1 operation(s) for accounts.
  name: Gust Accounts API
  slug: gust-accounts-api
artifact_total: 6
asyncapis:
- description: ''
  name: Gust Webhooks
  slug: gust-webhooks
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/plans/gust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gust-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/rules/gust-rules.yml
  title: ''
  type: Spectral
  url: rules/gust-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/asyncapi/gust-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gust-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/conformance/gust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gust-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/hosts/gust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gust-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/vendors/gust-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gust-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gust/refs/heads/main/security/gust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gust.com
- group: docs
  title: ''
  type: Documentation
  url: https://gust.helpscoutdocs.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://gust.com/start-your-journey/
- group: operate
  title: ''
  type: Support
  url: https://gust.helpscoutdocs.com/
- group: company
  title: ''
  type: Blog
  url: https://gust.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gust
- group: commercial
  title: ''
  type: Pricing
  url: https://gust.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://gust.com/launch/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gust.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gust.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/gust/workspace
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://gust.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Gust is a comprehensive platform that empowers entrepreneurs to start, grow, and fund their ventures. It offers tools for company formation, fundraising, investor relations, and access to a vast network of accelerators and angel groups. With over 800,000 founders, Gust provides educational resources, benchmarking, and a marketplace for startup services, making it a central hub for the startup ecosystem.
layout: provider
modified: '2026-10-14'
name: Gust
nav: Providers
network: true
overview: 'Gust is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, and 1 more. Tagged areas include Incorporation, Equity Management, Fundraising, Startup Tools, and Investor Tools.


  The Gust catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Gust''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Gust Plans Pricing
  plan_count: 3
  slug: gust-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Gust API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: gust-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 18.6
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 13.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Gust Domain Security
  slug: gust-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gust
tags:
- Incorporation
- Equity Management
- Fundraising
- Startup Tools
- Investor Tools
- Accelerator Management
website: https://gust.com
---
