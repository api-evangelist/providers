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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.earnin.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/activehours
coverage:
  checked: '2026-09-06'
  detail: Activehours is the pre-2017 name of EarnIn, whose earned-wage-access products ship only as a consumer mobile app — openapi.json, swagger.json, api-docs, llms.txt and the agent-card/api-catalog well-known paths all 404 on www.earnin.com, api.earnin.com is a Cloudflare 403/nginx 404 with nothing behind it, and the activehours GitHub org's 15 public repositories are every one of them a fork of somebody else's project.
  evidence:
  - status: 404
    url: https://www.earnin.com/openapi.json
  - status: 404
    url: https://www.earnin.com/llms.txt
  - status: 404
    url: https://www.earnin.com/.well-known/api-catalog
  - status: 403
    url: https://api.earnin.com/openapi.json
  - status: 404
    url: https://api.earnin.com/
  - status: 301
    url: https://www.activehours.com/
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Activehours, Inc. is the legal entity behind EarnIn, the consumer earned-wage-access fintech founded by Ram Palaniappan. The company launched as Activehours in 2014 and rebranded to EarnIn in 2017; it still files and licenses under the Activehours name (Activehours, Inc. NMLS #2535570) and still ships its Android application under the package identifier com.activehours, and EarnIn''s own AI-information page names the company outright as Activehours, Inc. (d/b/a EarnIn). The former corporate domain www.activehours.com now returns an HTTP 301 to www.earnin.com. This record is the pre-2017 name of a company the API Evangelist network already carries in full at all/earnin, and it is retained only as a name pointer — see x-duplicate-of. Products (Live Pay, Cash Out, Early Pay, Balance Shield, Credit Monitoring, Savings Jars and EarnIn Payroll) are delivered as a consumer mobile application; no public API, developer portal, or machine-readable contract is published under either name.'
image: https://www.earnin.com/assets/img/share.png
layout: provider
modified: '2026-09-06'
name: Activehours
nav: Providers
network: true
overview: Activehours is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Earned Wage Access, Consumer Finance, and Payments.
random_paper: 0
score:
  band: minimal
  composite: 0.8
  coverage:
    artifact_dirs: 0
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 0.0
  schema_version: 0.19.0
  scored_at: '2026-09-06'
slug: activehours
tags:
- Company
- Fintech
- Earned Wage Access
- Consumer Finance
- Payments
- Payroll
- Mobile App
website: https://www.earnin.com
---
