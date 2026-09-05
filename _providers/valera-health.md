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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.valerahealth.com/
- group: company
  title: ''
  type: Blog
  url: https://www.valerahealth.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.valerahealth.com/help-center/
- group: operate
  title: ''
  type: Support
  url: https://www.valerahealth.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.valerahealth.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.valerahealth.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/valerahealth
- group: design
  title: ''
  type: Conformance
  url: conformance/valera-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/valera-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valera-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/valera-health-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Valera Health is a virtual behavioral-health care provider, not a software vendor — it runs on NextGen Healthcare for its clinical record and patient portal, publishes no developer portal, docs subdomain or reference of any kind, and its only externally addressable API host, api.valerahealth.com, is the private Node/Express backend for its own patient app, which answered 404 for every discovery path probed.
  evidence:
  - status: 404
    url: https://api.valerahealth.com/openapi.json
  - status: 404
    url: https://api.valerahealth.com/graphql
  - status: 404
    url: https://www.valerahealth.com/llms.txt
  - status: 404
    url: https://www.valerahealth.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'Valera Health is a Brooklyn, New York based virtual behavioral health provider delivering therapy, psychiatry, group therapy, comprehensive Dialectical Behavior Therapy (DBT), suicide care and youth support programs to adults and children through an in-house clinical team, a care-coordinator model and a patient mobile app. It is a care-delivery organization rather than a software vendor: revenue comes from commercial insurance, Medicaid and Medicare reimbursement, and the clinical record and patient portal run on third-party health IT (the patient portal is operated by NextGen Healthcare at pxpportal.nextgen.com). As of this profile Valera Health publishes no developer program, no public API reference, and no machine-readable contract of any kind; its only externally addressable API host, api.valerahealth.com, is the private backend for its own patient application.'
image: https://www.valerahealth.com/wp-content/uploads/2025/01/valera-home-main-1024x966.jpg
layout: provider
modified: '2026-09-02'
name: Valera Health
nav: Providers
network: true
overview: 'Valera Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Behavioral Health, and Mental Health.


  Valera Health''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Valera Health Domain Security
  slug: valera-health-domain-security
  summary_line: TLSv1.3
slug: valera-health
tags:
- Company
- Health
- Healthcare
- Behavioral Health
- Mental Health
- Telehealth
- Telemedicine
- Psychiatry
- Digital Health
website: https://www.valerahealth.com/
---
