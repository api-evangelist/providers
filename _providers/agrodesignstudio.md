---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-09-23'
api_count: 2
apis:
- description: A live, unauthenticated remote Model Context Protocol endpoint served at the AgroBox structural-biology service site. The server is the Wix "Site Visitor Assistant" — a PLATFORM-AUTHORED MCP surface g
  name: AgroBox Site MCP
  slug: agrobox-site-mcp
- description: The second live, unauthenticated remote MCP endpoint, served at the AgroDesign.SHOP storefront where the company sells lab-automation robot arms (as a UFACTORY xArm authorized reseller), Arabidopsis c
  name: AgroDesign.SHOP Site MCP
  slug: agrodesignshop-site-mcp
artifact_total: 7
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/security/agrodesignstudio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrodesignstudio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agrodesign.co.jp/
- group: operate
  title: ''
  type: Support
  url: https://www.agrobox.jp/contact
- group: company
  title: ''
  type: Blog
  url: https://www.agrodesign.co.jp/pages/2231598/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agrobox.jp/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrobox.jp/tokusyohou
- group: company
  title: ''
  type: LinkedIn
  url: https://jp.linkedin.com/company/agrodesignstudios
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/mcp/agrodesignstudio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agrodesignstudio-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/llms/agrodesignstudio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrodesignstudio-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/authentication/agrodesignstudio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agrodesignstudio-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/conformance/agrodesignstudio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agrodesignstudio-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/conventions/agrodesignstudio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agrodesignstudio-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/rate-limits/agrodesignstudio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agrodesignstudio-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/plans/agrodesignstudio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrodesignstudio-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agrodesignstudio/refs/heads/main/packages/agrodesignstudio-packages.yml
  title: ''
  type: Packages
  url: packages/agrodesignstudio-packages.yml
created: '2026-09-13'
description: 'AgroDesign Studios (株式会社アグロデザイン・スタジオ) is a Japanese structural-biology startup founded 30 March 2018 by CEO Yuki Nishigaya, based in the University of Tokyo Kashiwa-II campus industry-academia building in Kashiwa, Chiba. It applies protein and nucleic-acid 3D structure information to the discovery of molecular-targeted, environmentally safer crop-protection chemicals. Its commercial surface is contract research rather than software: the AgroBox® service brand sells X-ray crystallography, cryo-EM, fragment screening and structure-based drug design (SBDD) engagements, and AgroDesign.SHOP sells lab-automation robots, cultivation kits and experimental materials. The company publishes no first-party API, SDK or developer program; its only machine-callable agent surface is the Wix platform Site MCP endpoint served on each of its two Wix-hosted sites.'
image: https://static.wixstatic.com/media/a7776e_4c1c9094741c45dd9391de482e580aeb~mv2.jpg/v1/fill/w_446,h_234,al_c/a7776e_4c1c9094741c45dd9391de482e580aeb~mv2.jpg
layout: provider
mcp_servers:
- description: 'Two live, unauthenticated remote MCP endpoints served from hosts AgroDesign Studios (株式会社アグロデザイン・スタジオ) controls: the AgroBox structural-biology service site and the AgroDesign.SHOP lab-equipment store'
  name: AgroDesign Studios — Site MCP servers
  slug: agrodesign-studios-site-mcp-servers
modified: '2026-09-13'
name: AgroDesign Studios
nav: Providers
network: true
overview: 'AgroDesign Studios publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Biotechnology, Life Sciences, and Structural Biology.


  AgroDesign Studios'' developer surface includes support, engineering blog, authentication, and 12 more developer resources.'
plans:
- name: Agrodesignstudio Plans Pricing
  plan_count: 0
  slug: agrodesignstudio-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Agrodesignstudio Rate Limits
  slug: agrodesignstudio-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 19.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agrodesignstudio Authentication
  slug: agrodesignstudio-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Agrodesignstudio Domain Security
  slug: agrodesignstudio-domain-security
  summary_line: TLSv1.2 · HSTS
slug: agrodesignstudio
tags:
- Agriculture
- AgTech
- Biotechnology
- Life Sciences
- Structural Biology
- Drug Discovery
- Crop Protection
- Contract Research
- Laboratory Automation
- Japan
- MCP
- Company
website: https://www.agrodesign.co.jp/
---
