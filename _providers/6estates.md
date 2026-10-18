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
- description: Enterprise AI platform API providing access to LLM inference, model hub, and workflow automation.
  name: 6Estates API
  slug: 6estates-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/well-known/6estates-6estates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/6estates-6estates-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.6estates.com/security/policy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/well-known/6estates-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/6estates-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/well-known/6estates-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/6estates-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/hosts/6estates-hosts.yml
  title: ''
  type: Hosts
  url: hosts/6estates-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/packages/6estates-packages.yml
  title: ''
  type: SDKs
  url: packages/6estates-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/packages/6estates-packages.yml
  title: ''
  type: Packages
  url: packages/6estates-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/6estates
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/security/6estates-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/6estates-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/6estates/refs/heads/main/security/6estates-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/6estates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://6estates.com/
- group: docs
  title: ''
  type: Documentation
  url: https://llm-platform-sea.6estates.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://llm-platform-sea.6estates.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://6estates.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://6estates.com/termcondition.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://6estates.com/privacy.html
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://llm-platform-sea.6estates.com/api/mcp
  - status: 200
    url: https://6estates.com/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: 6Estates provides enterprise AI solutions, offering a suite of agentic AI applications such as Document Agent, Lending Agent, and Financial Statement Agent. Their platform includes a token‑metered LLM inference service, a model hub, and tools for end‑to‑end workflow automation for lenders. Based in Southeast Asia, 6Estates delivers full‑stack AI from model deployment to decision making, targeting industries like finance, insurance, and enterprise analytics.
layout: provider
modified: '2026-10-15'
name: 6Estates
nav: Providers
network: true
overview: '6Estates is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Automation, and Finance.


  6Estates'' developer surface includes documentation, API reference, pricing, and 13 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 6Estates Domain Security
  slug: 6estates-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 6Estates Vulnerability Disclosure
  slug: 6estates-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: 6estates
tags:
- Company
- Artificial Intelligence
- Enterprise
- Automation
- Finance
website: https://6estates.com/
---
