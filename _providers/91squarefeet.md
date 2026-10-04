---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.8
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: A Model Context Protocol endpoint present on the 91squarefeet.com host at the WordPress `mcp` REST namespace, route `mcp/mcp-adapter-default-server`, declared by the site's own /wp-json route index. I
  name: 91Squarefeet MCP Adapter Endpoint
  slug: 91squarefeet-mcp-adapter
- description: 'The public WordPress REST API (wp-json) of the 91Squarefeet website at 91squarefeet.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate'
  name: 91Squarefeet Website (WordPress REST)
  slug: 91squarefeet-com-website-wordpress-rest
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://91squarefeet.com/
- group: company
  title: ''
  type: Blog
  url: https://91squarefeet.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://91squarefeet.com/blog/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://91squarefeet.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://91squarefeet.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/91sqft
- group: company
  title: ''
  type: Twitter
  url: https://x.com/91sqft
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@91squarefeet
- group: company
  title: ''
  type: Careers
  url: https://91squarefeet.com/careers/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/llms/91squarefeet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/91squarefeet-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/security/91squarefeet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/91squarefeet-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/conformance/91squarefeet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/91squarefeet-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/lifecycle/91squarefeet-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/91squarefeet-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/plans/91squarefeet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/91squarefeet-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/packages/91squarefeet-packages.yml
  title: ''
  type: Packages
  url: packages/91squarefeet-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/authentication/91squarefeet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/91squarefeet-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/conventions/91squarefeet-conventions.yml
  title: ''
  type: Conventions
  url: conventions/91squarefeet-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/errors/91squarefeet-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/91squarefeet-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/data-model/91squarefeet-data-model.yml
  title: ''
  type: DataModel
  url: data-model/91squarefeet-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/91squarefeet/refs/heads/main/rate-limits/91squarefeet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/91squarefeet-rate-limits.yml
created: '2026-09-05'
description: 91Squarefeet is a Gurugram, India based design-and-build company delivering turnkey retail and office fit-outs for brands expanding their physical footprint across India. Founded 2018-2019 and backed by Y Combinator, Stellaris Venture Partners and Stride Ventures, it runs a full-stack, non-subcontracted model — in-house project management, a digitized supply chain spanning fixture factories, material OEMs, engineering consultants and labour contractors, and an internal AI-assisted project platform with a field mobile app — and reports 1,100+ delivered projects for brands including TATA, DLF, Godrej, Asian Paints, Kotak and Bluestone. It publishes no developer program, no API documentation and no OpenAPI. The only machine-readable surfaces on its host are the WordPress REST API its public website exposes (serving the company's own portfolio, client, case-study, property, testimonial and press-release content anonymously), a Rank Math llms.txt, and a gated WordPress MCP adapter
  endpoint.
image: https://91squarefeet.com/wp-content/uploads/2024/02/91_400x400.webp
layout: provider
mcp_servers:
- description: 91squarefeet.com serves a Model Context Protocol endpoint at the WordPress `mcp` REST namespace. It was not found in any MCP registry, in 91Squarefeet marketing material, or in any documentation — the
  name: 91Squarefeet MCP Server
  slug: 91squarefeet-mcp-server
modified: '2026-09-05'
name: 91Squarefeet
nav: Providers
network: true
overview: '91Squarefeet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Retail, Interior Design, and Real Estate.


  91Squarefeet''s developer surface includes engineering blog, support, YouTube channel, authentication, and 17 more developer resources.'
plans:
- name: 91Squarefeet Plans Pricing
  plan_count: 0
  slug: 91squarefeet-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: 91Squarefeet Rate Limits
  slug: 91squarefeet-rate-limits
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 16.1
  provenance:
    conformance: derived
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: 91Squarefeet Authentication
  slug: 91squarefeet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 91Squarefeet Domain Security
  slug: 91squarefeet-domain-security
  summary_line: TLSv1.3
slug: 91squarefeet
tags:
- Company
- Construction
- Retail
- Interior Design
- Real Estate
- Project Management
- Supply Chain
- India
- WordPress
website: https://91squarefeet.com/
---
