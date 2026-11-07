---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://security.psu.edu/
- group: agent
  href: https://artifacts.apis.io/penn-state-applied-research-lab/llms/penn-state-applied-research-lab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/penn-state-applied-research-lab-llms.txt
- group: other
  href: https://artifacts.apis.io/penn-state-applied-research-lab/hosts/penn-state-applied-research-lab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/penn-state-applied-research-lab-hosts.yml
- group: other
  href: https://artifacts.apis.io/penn-state-applied-research-lab/vendors/penn-state-applied-research-lab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/penn-state-applied-research-lab-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://sites.psu.edu/Support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://security.psu.edu/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.arl.psu.edu/news/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.psu.edu/
- group: auth
  href: https://artifacts.apis.io/penn-state-applied-research-lab/security/penn-state-applied-research-lab-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/penn-state-applied-research-lab-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/penn-state-applied-research-lab/security/penn-state-applied-research-lab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/penn-state-applied-research-lab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arl.psu.edu
coverage:
  detail: The Penn State Applied Research Lab does not expose a public API surface.
  evidence:
  - status: 404
    url: https://api.psu.edu/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: The Applied Research Laboratory (ARL) at Penn State University is a University Affiliated Research Center conducting essential research, development, and systems engineering across core competencies such as communications, information, navigation, fluid dynamics, acoustics, materials, manufacturing, and undersea systems. Founded in 1945, ARL partners with industry and government to advance technology and innovation.
layout: provider
modified: '2026-10-28'
name: Penn State Applied Research Lab
nav: Providers
network: true
overview: 'Penn State Applied Research Lab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Engineering, University, and Defense.


  Penn State Applied Research Lab''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 52.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 10.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/penn-state-applied-research-lab/penn-state-applied-research-lab-2026-11-03T141110.png
security:
- kind: domain-security
  name: Penn State Applied Research Lab Domain Security
  slug: penn-state-applied-research-lab-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Penn State Applied Research Lab Trust Center
  slug: penn-state-applied-research-lab-trust-center
  summary_line: PCI DSS, HIPAA, GDPR
slug: penn-state-applied-research-lab
tags:
- Company
- Research
- Engineering
- University
- Defense
- Technology
website: https://www.arl.psu.edu
---
