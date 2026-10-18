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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fpl-com/refs/heads/main/hosts/fpl-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fpl-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fpl-com/refs/heads/main/vendors/fpl-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fpl-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.fpl.com/help/mesp.html
- group: start
  title: ''
  type: SignUp
  url: https://www.fpl.com/northwest/business/save/programs/commercial-surge-protection/sign-up.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.fpl.com/news/energy-news.html
- group: company
  title: ''
  type: Blog
  url: https://www.fpl.com/blog/ask-the-expert.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fpl-com/refs/heads/main/security/fpl-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fpl-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fpl.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fpl.com/support/contact/using-fpl-com/view-privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fpl.com/account/bill/pay-online-terms.html
- group: start
  title: ''
  type: Portal
  url: https://partner.fpl.com/
coverage:
  checked: '2026-10-13'
  detail: No API, developer portal, OpenAPI/AsyncAPI/GraphQL/MCP surface, or Green Button (Connect My Data or Download My Data) program found. api.fpl.com does not resolve; partner.fpl.com is a login-gated partner portal with no published interface; sitemap (www.fpl.com/sitemap.xml) lists no developer, data-access, or Green Button pages.
  evidence:
  - status: 200
    url: https://www.fpl.com/sitemap.xml
  - status: 200
    url: https://partner.fpl.com/
  - status: unresolved
    url: https://api.fpl.com/
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Florida Power & Light (FPL) is the largest electric utility in Florida and a subsidiary of NextEra Energy. As of 2026-10-13 it publishes no public API, developer portal, or Green Button Connect My Data program; customer usage data is available only inside the myFPL account dashboard.
layout: provider
modified: '2026-10-13'
name: Florida Power & Light
nav: Providers
network: true
overview: 'Florida Power & Light is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Utility, Energy, Florida, and Utilities.


  Florida Power & Light''s developer surface includes support, signup flow, engineering blog, developer portal, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 11.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fpl Com Domain Security
  slug: fpl-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fpl-com
tags:
- Company
- Electric Utility
- Energy
- Florida
- Utilities
website: https://www.fpl.com
---
