---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/magic-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/magic-dev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/magicproduct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/magicailabs
- group: company
  title: ''
  type: Website
  url: https://magic.dev
- group: company
  title: ''
  type: Blog
  url: https://magic.dev/blog
- group: company
  title: ''
  type: Careers
  url: https://magic.dev/careers
- group: other
  title: ''
  type: Safety
  url: https://magic.dev/safety
created: '2026-07-02'
description: Magic (magic.dev) is a San Francisco frontier AI research lab building frontier-scale code models - an "AI coworker" for software engineering, and ultimately a path to safe AGI - rather than a shipping developer product. It has raised roughly $515M from Nat Friedman, Daniel Gross, CapitalG, Elad Gil, Sequoia, Jane Street, and Eric Schmidt, and has published research on ultra-long-context models (LTM-1 at a 5M token context window, and the unreleased LTM-2-mini research prototype claimed to handle up to 100M tokens). As of this review Magic does not publish a public, self-serve developer API, API reference, SDK, or waitlist; its website and careers pages describe mission, research, and open roles only, with no product access model, pricing, or documented endpoints. Its GitHub organization (magicproduct) hosts research tooling (e.g. hash-hop, a long-context evaluation harness) and infrastructure forks, not an API client or SDK.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/magic-dev.png
layout: provider
modified: '2026-07-02'
name: Magic
nav: Providers
network: true
overview: 'Magic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, AGI Research, Coding Agents, Long Context, and LLM.


  Magic''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/magic-dev/refs/heads/main/screenshots/magic-dev-2026-07-25T225842.png
security:
- kind: domain-security
  name: Magic Dev Domain Security
  slug: magic-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Magic Dev Vulnerability Disclosure
  slug: magic-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: magic-dev
tags:
- Artificial Intelligence
- AGI Research
- Coding Agents
- Long Context
- LLM
- Frontier Lab
- No Public API
website: https://magic.dev
---
