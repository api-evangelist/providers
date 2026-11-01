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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/axiommath-ai/hosts/axiommath-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/axiommath-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/axiommath-ai/vendors/axiommath-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/axiommath-ai-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://axiommath.ai/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AxiomMath
- group: company
  title: ''
  type: Blog
  url: https://axiommath.ai/research/blog/
- group: auth
  href: https://artifacts.apis.io/axiommath-ai/security/axiommath-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axiommath-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axiommath.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://axiommath.ai
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Axiom builds formal foundations and tooling that enable machines and mathematicians to verify proofs and reason about logic. Their platform includes AXLE, an interactive proof environment, and supports research projects such as the Bounded Gaps Project. The company focuses on advancing mathematical reasoning through software, offering APIs for proof verification, research data, and educational tools.
layout: provider
modified: '2026-10-22'
name: Axiom
nav: Providers
network: true
overview: 'Axiom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mathematics, FormalVerification, Research, and AI.


  Axiom''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Axiommath Ai Domain Security
  slug: axiommath-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: axiommath-ai
tags:
- Company
- Mathematics
- FormalVerification
- Research
- AI
website: https://axiommath.ai
---
