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
- description: Integrated financing for mobile growth API (documentation site)
  name: Braavo Capital API
  slug: braavo-capital-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braavocapital/refs/heads/main/llms/braavocapital-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/braavocapital-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braavocapital/refs/heads/main/well-known/braavocapital-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/braavocapital-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/braavocapital/refs/heads/main/well-known/braavocapital-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/braavocapital-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/braavocapital/refs/heads/main/hosts/braavocapital-hosts.yml
  title: ''
  type: Hosts
  url: hosts/braavocapital-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.getbraavo.com/sign-up?int_src=getbraavo.com&int_med=fund_me
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/braavocapital/refs/heads/main/security/braavocapital-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braavocapital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getbraavo.com
- group: company
  title: ''
  type: Blog
  url: https://www.getbraavo.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getbraavo.com/funding-pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getbraavo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getbraavo.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.getbraavo.com/en/collections/2257420-faq
coverage:
  checked: '2026-10-03'
  detail: The API documentation site renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://www.getbraavo.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Braavocapital, operating as Braavo Capital, provides on‑demand funding for mobile apps and games. It offers financing solutions such as app‑store payout advances, user‑acquisition financing, and financial analytics, enabling developers to scale growth without giving up equity. Since 2015, Braavo has funded over 10,000 apps with $2 billion invested, supporting a portfolio that includes popular consumer apps and games.
image: https://www-static.getbraavo.com/wp-content/uploads/2026/04/Braavo-Capital.png
layout: provider
modified: '2026-10-03'
name: Braavocapital
nav: Providers
network: true
overview: 'Braavocapital publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Funding, Mobile App, and Gaming.


  Braavocapital''s developer surface includes signup flow, engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Braavocapital Domain Security
  slug: braavocapital-domain-security
  summary_line: TLSv1.3 · DMARC
slug: braavocapital
tags:
- Company
- Fintech
- Funding
- Mobile App
- Gaming
website: https://www.getbraavo.com
---
