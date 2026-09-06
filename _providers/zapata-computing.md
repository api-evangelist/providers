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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zapata-computing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zapataquantum.com/
- group: operate
  title: ''
  type: Support
  url: https://zapataquantum.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zapataquantum.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zapataquantum.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zapatacomputing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zapata-engineering
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/zapata-engineering/orquestra-sdk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zapata-quantum/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.zapataquantum.com/
- group: company
  title: ''
  type: Careers
  url: https://zapataquantum.com/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://zapataquantum.com/case-studies
- group: other
  title: ''
  type: x-ResearchPapers
  url: https://zapataquantum.com/papers
- group: other
  title: ''
  type: x-Patents
  url: https://zapataquantum.com/patents
- group: build
  title: ''
  type: Packages
  url: packages/zapata-computing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zapata-computing-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/zapata-computing-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zapata-computing-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zapata-computing-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zapata-computing-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/zapata-computing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zapata-computing-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: Zapata Quantum sells the Orquestra platform as a delivered enterprise engagement — every call to action on zapataquantum.com routes to /contact, there is no /docs, /developers or /pricing route, and the only documentation host the company ever named, docs.orquestra.io, is now NXDOMAIN; the Apache-2.0 Orquestra Python libraries on PyPI are research/workflow packages, not clients for any API the company publishes.
  evidence:
  - status: 404
    url: https://zapataquantum.com/docs
  - status: 404
    url: https://zapataquantum.com/openapi.json
  - status: 404
    url: https://zapataquantum.com/.well-known/api-catalog
  - status: 0
    url: https://docs.orquestra.io/
  - status: 200
    url: https://zapataquantum.com/solutions
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: Zapata Quantum, Inc. (formerly Zapata Computing, and briefly Zapata AI) is a Boston-based, hardware-agnostic quantum software company spun out of a Harvard quantum computing lab in 2017. It sells enterprise engagements — use-case discovery, hardware-readiness assessment and quantum application development across chemistry, optimization, simulation and machine learning — around its Orquestra platform, and publishes the Orquestra Workflow SDK stack as Apache-2.0 open source. The company ceased operations in October 2024 after a debt acceleration, restructured through 2025, and relaunched under the Zapata Quantum name in 2026. It publishes no public API, developer portal, API reference or self-serve signup; its only machine-readable developer surface is the Orquestra Python package stack on PyPI and the `orq` CLI, both frozen at their October 2024 releases.
image: https://cdn.prod.website-files.com/68f2930870a8ae51b3d5b41b/68f5648b504a85f46118b931_zapata-fav256.png
layout: provider
modified: '2026-09-05'
name: Zapata Quantum
nav: Providers
network: true
overview: 'Zapata Quantum is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Quantum Software, Artificial Intelligence, and Scientific Computing.


  Zapata Quantum''s developer surface includes support, CLI, changelog, and 19 more developer resources.'
plans:
- name: Zapata Computing Plans Pricing
  plan_count: 0
  slug: zapata-computing-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Zapata Computing Rate Limits
  slug: zapata-computing-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Zapata Computing Domain Security
  slug: zapata-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zapata-computing
tags:
- Company
- Quantum Computing
- Quantum Software
- Artificial Intelligence
- Scientific Computing
- Workflow Orchestration
- Enterprise Software
- Open Source
- Research
website: https://zapataquantum.com/
---
