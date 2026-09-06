---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://91squarefeet.com/wp-json
  baseurl_source: declared
  description: The read-only WordPress REST API (`wp/v2` namespace) that 91squarefeet.com serves by default, including the custom content types the company registered for its own business content — portfolio (delive
  name: 91Squarefeet Content API
  slug: 91squarefeet-content-api
- description: A Model Context Protocol endpoint present on the 91squarefeet.com host at the WordPress `mcp` REST namespace, route `mcp/mcp-adapter-default-server`, declared by the site's own /wp-json route index. I
  name: 91Squarefeet MCP Adapter Endpoint
  slug: 91squarefeet-mcp-adapter
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
  title: ''
  type: LLMsTxt
  url: llms/91squarefeet-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/91squarefeet-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/91squarefeet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/91squarefeet-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/91squarefeet-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/91squarefeet-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
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
overview: '91Squarefeet publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Company, Construction, Retail, Interior Design, and Real Estate.


  91Squarefeet''s developer surface includes engineering blog, support, YouTube channel, and 13 more developer resources.'
plans:
- name: 91Squarefeet Plans Pricing
  plan_count: 0
  slug: 91squarefeet-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 91Squarefeet Rate Limits
  slug: 91squarefeet-rate-limits
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 57.1
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Content
- WordPress
website: https://91squarefeet.com/
---
