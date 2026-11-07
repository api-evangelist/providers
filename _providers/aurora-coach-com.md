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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation is provided but no machine-readable contract was found.
  name: Aurora Coach API
  slug: aurora-coach-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/aurora-coach-com/conformance/aurora-coach-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aurora-coach-com-conformance.yml
- group: auth
  href: https://artifacts.apis.io/aurora-coach-com/well-known/aurora-coach-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aurora-coach-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aurora-coach-com/well-known/aurora-coach-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aurora-coach-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aurora-coach-com/hosts/aurora-coach-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurora-coach-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aurora-coach-com/vendors/aurora-coach-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurora-coach-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aurora-coach.com/terms
- group: auth
  title: ''
  type: Security
  url: https://aurora-coach.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aurora-coach.com/privacy
- group: auth
  href: https://artifacts.apis.io/aurora-coach-com/security/aurora-coach-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurora-coach-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aurora-coach.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aurora-coach.com/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://aurora-coach.com/overview
- group: company
  title: ''
  type: Blog
  url: https://aurora-coach.com/blog
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI/AsyncAPI/GraphQL spec is available.
  evidence:
  - status: 200
    url: https://aurora-coach.com/docs/connector
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Aurora Coach provides a continuous improvement platform for software teams. It uses AI to score teams across six domains, offers actionable next steps, and tracks commitments. Teams can see results, decide on changes, and Aurora Coach follows up to ensure progress, fostering a culture of ongoing improvement and high performance.
image: https://aurora-coach.com/og-image.png
layout: provider
modified: '2026-11-02'
name: Aurora Coach
nav: Providers
network: true
overview: 'Aurora Coach is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Software, Artificial Intelligence, Continuous Improvement, Team Performance, and Coaching.


  Aurora Coach''s developer surface includes documentation, getting-started guide, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
  previous_composite: 19.4
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aurora Coach Com Domain Security
  slug: aurora-coach-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aurora-coach-com
tags:
- Software
- Artificial Intelligence
- Continuous Improvement
- Team Performance
- Coaching
website: https://aurora-coach.com/
---
