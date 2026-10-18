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
- description: API for ConnectIt Software services as described in the portal documentation.
  name: ConnectIt Software API
  slug: connectit-software-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/connectit-software/refs/heads/main/plans/connectit-software-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/connectit-software-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/connectit-software/refs/heads/main/hosts/connectit-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/connectit-software-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/connectit-software/refs/heads/main/security/connectit-software-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/connectit-software-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://connectit-software.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://connectit-software.co.uk/support/index.aspx
- group: operate
  title: ''
  type: Roadmap
  url: https://connectit-software.co.uk/support/development-roadmap.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://connectit-software.co.uk/products/pricing.aspx?curr=GBP
- group: start
  title: ''
  type: SignUp
  url: https://connectit-software.co.uk/registration/index.aspx
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://connectit-software.co.uk/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Hilltops IT, operating as ConnectIt Software Development, provides integration and add‑on solutions for business software systems such as QuoteWerks, Sage, Microsoft Dynamics, and Monday.com. Based in the UK, they deliver bespoke development, migration, and support services to improve efficiency and profitability for their clients.
layout: provider
modified: '2026-10-16'
name: Hilltops IT
nav: Providers
network: true
overview: 'Hilltops IT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software Integration, Add‑On Solutions, Sage, QuoteWerks, and Microsoft Business Central.


  Hilltops IT''s developer surface includes support, pricing, signup flow, and 5 more developer resources.'
plans:
- name: Connectit Software Plans Pricing
  plan_count: 3
  slug: connectit-software-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Connectit Software Domain Security
  slug: connectit-software-domain-security
  summary_line: TLSv1.3
slug: connectit-software
tags:
- Software Integration
- Add‑On Solutions
- Sage
- QuoteWerks
- Microsoft Business Central
- Monday.com
- Salesforce
website: https://connectit-software.co.uk/
---
