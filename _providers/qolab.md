---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://qolab.ai
- group: company
  title: ''
  type: About
  url: https://qolab.ai/about
- group: other
  title: ''
  type: Product
  url: https://qolab.ai/product
- group: other
  title: ''
  type: Technology
  url: https://qolab.ai/technology
- group: other
  title: ''
  type: Research
  url: https://qolab.ai/research
- group: other
  title: ''
  type: Team
  url: https://qolab.ai/team
- group: company
  title: ''
  type: Partners
  url: https://qolab.ai/partners
- group: company
  title: ''
  type: Investors
  url: https://qolab.ai/investors
- group: company
  title: ''
  type: Careers
  url: https://qolab.ai/career
- group: operate
  title: ''
  type: Support
  url: https://qolab.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://qolab.ai/news-updates
- group: company
  title: ''
  type: Newsroom
  url: https://qolab.ai/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qolab-Ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qolabai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCiCuzvOPdeFspWJdRGZQSdA
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qolab.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qolab.ai/privacy
- group: auth
  title: ''
  type: Security
  url: https://qolab.ai/vulnerability-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qolab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qolab-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qolab-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/qolab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qolab-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/qolab-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Qolab's only product page names "API and control interface guides" as a deliverable of the Qolab Start QPU platform, but the sole route to them is the "Request access" form on that same page — there is no developer portal, no reference, and no api./docs./developer. subdomain (all three NXDOMAIN), so the contract is behind a sales conversation rather than published.
  evidence:
  - status: 200
    url: https://qolab.ai/product
  - status: 404
    url: https://qolab.ai/openapi.json
  - status: 404
    url: https://qolab.ai/.well-known/agent-card.json
  - status: 404
    url: https://qolab.ai/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: 'Qolab, Inc. is a superconducting quantum computing hardware company founded in 2022, with offices in Los Angeles, California and research laboratories in Madison, Wisconsin. Co-founded by 2025 Nobel laureate in physics John Martinis and Alan Ho — both of whom led hardware and product for Google''s 2019 quantum supremacy milestone — Qolab builds high-coherence superconducting qubits by applying advanced semiconductor manufacturing processes to qubit fabrication, targeting the yield and integration problems that stand between quantum research and utility-scale machines. Its first deployable offering is Qolab Start, a turn-key superconducting QPU platform for pulse-level and device-level hardware research, sold to university labs, national laboratories and semiconductor R&D teams and delivered either on-premise or through secure cloud connectivity. Qolab has raised roughly $70M across a $16M Series A and a $54.2M Series B led by UC Investments, with strategic investment from Applied
  Ventures and Western Digital, and leads hardware development for DARPA''s Quantum Benchmarking Initiative. Qolab publishes no public developer program: there is no developer portal, no machine-readable API contract and no self-serve sign-up, and the API and control interface guides that ship with Qolab Start are released to customers after a Request Access review.'
image: https://cdn.prod.website-files.com/6997406d670814baad5db361/69998f1154fc550d9c79d656_Webclip.png
layout: provider
modified: '2026-08-26'
name: Qolab
nav: Providers
network: true
overview: 'Qolab is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Superconducting Qubits, Quantum Hardware, and Semiconductors.


  Qolab''s developer surface includes support, engineering blog, YouTube channel, and 21 more developer resources.'
plans:
- name: Qolab Plans Pricing
  plan_count: 0
  slug: qolab-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Qolab Rate Limits
  slug: qolab-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qolab/refs/heads/main/screenshots/qolab-2026-09-02T152533.png
security:
- kind: domain-security
  name: Qolab Domain Security
  slug: qolab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qolab Vulnerability Disclosure
  slug: qolab-vulnerability-disclosure
  summary_line: Hackerone
slug: qolab
tags:
- Company
- Quantum Computing
- Superconducting Qubits
- Quantum Hardware
- Semiconductors
- Deep Tech
- Research Instrumentation
- QPU
website: https://qolab.ai
---
