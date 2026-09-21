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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/security/takeda-pharmaceutical-company-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/takeda-pharmaceutical-company-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.takeda.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.takeda.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.takeda.com/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.takeda.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://www.takeda.com/newsroom/press-releases/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/llms/takeda-pharmaceutical-company-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/takeda-pharmaceutical-company-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/conformance/takeda-pharmaceutical-company-conformance.yml
  title: ''
  type: Conformance
  url: conformance/takeda-pharmaceutical-company-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/packages/takeda-pharmaceutical-company-packages.yml
  title: ''
  type: Packages
  url: packages/takeda-pharmaceutical-company-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/plans/takeda-pharmaceutical-company-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/takeda-pharmaceutical-company-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/takeda-pharmaceutical-company/refs/heads/main/rate-limits/takeda-pharmaceutical-company-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/takeda-pharmaceutical-company-rate-limits.yml
coverage:
  checked: '2026-09-13'
  detail: 'Takeda runs large internal API platforms - AWS AppSync GraphQL for its data scientists, a PingFederate workforce IdP that robots.txt disallows - but exposes none of it outward: developer.takeda.com and api.takeda.com do not resolve at all, the corporate site 404s every well-known path, and the only supplier integration Takeda names is a third-party Apex Analytix payments portal, so there is no developer programme to gate or to read.'
  evidence:
  - status: 0
    url: https://developer.takeda.com/
  - status: 0
    url: https://api.takeda.com/
  - status: 404
    url: https://www.takeda.com/openapi.json
  - status: 404
    url: https://www.takeda.com/.well-known/api-catalog
  - status: 404
    url: https://www.takeda.com/.well-known/security.txt
  - status: 200
    url: https://www.takeda.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-13'
description: 'Takeda Pharmaceutical Company Limited is a Japanese multinational biopharmaceutical company headquartered in Tokyo, founded in 1781 and listed on the Tokyo Stock Exchange (4502) and the New York Stock Exchange (TAK). It is the largest pharmaceutical company in Japan and Asia, and operates globally across oncology, rare genetic and hematologic diseases, neuroscience, gastroenterology, plasma-derived therapies and vaccines, a portfolio substantially expanded by its 2019 acquisition of Shire. Takeda is a software consumer rather than a software vendor: it runs large internal API and data platforms, but publishes no public developer program, API reference or machine-readable contract. The one machine-readable document it does serve to automated clients is an llms.txt at its corporate root, which indexes its verified country websites and states an explicit LLM usage and attribution policy.'
layout: provider
modified: '2026-09-13'
name: Takeda Pharmaceutical Company
nav: Providers
network: true
overview: 'Takeda Pharmaceutical Company is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Healthcare, Life Sciences, and Biotechnology.


  Takeda Pharmaceutical Company''s developer surface includes support, engineering blog, and 9 more developer resources.'
plans:
- name: Takeda Pharmaceutical Company Plans Pricing
  plan_count: 0
  slug: takeda-pharmaceutical-company-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Takeda Pharmaceutical Company Rate Limits
  slug: takeda-pharmaceutical-company-rate-limits
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 14.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Takeda Pharmaceutical Company Domain Security
  slug: takeda-pharmaceutical-company-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: takeda-pharmaceutical-company
tags:
- Company
- Pharmaceuticals
- Healthcare
- Life Sciences
- Biotechnology
- Clinical Trials
- Japan
website: https://www.takeda.com/
---
