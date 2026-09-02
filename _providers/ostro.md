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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ostro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ostro.veeva.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ostro-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://ostro.veeva.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ostro.veeva.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ostro.veeva.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ostrohealth
- group: commercial
  title: ''
  type: Plans
  url: plans/ostro-plans-pricing.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://www.veeva.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veeva-ostro
- group: company
  title: ''
  type: Careers
  url: https://ostro.veeva.com/careers
- group: company
  title: ''
  type: About
  url: https://ostro.veeva.com/company
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/ostro_stock/
coverage:
  checked: '2026-08-26'
  detail: Ostro sells a managed AI brand-engagement platform to pharma marketing teams and ships nothing to developers — ostro.veeva.com has no /developers, /docs, /pricing or API reference, no api./developer./docs. subdomain resolves on ostrohealth.com, and the ostrohealth GitHub org holds only a Webflow export and a job-descriptions repo.
  evidence:
  - status: 404
    url: https://ostro.veeva.com/openapi.json
  - status: 404
    url: https://ostro.veeva.com/.well-known/api-catalog
  - status: 404
    url: https://ostro.veeva.com/pricing
  - status: 0
    url: https://api.ostrohealth.com/
  - status: 200
    url: https://api.github.com/orgs/ostrohealth/repos
  - status: 200
    url: https://ostro.veeva.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Ostro (Veeva Ostro) is an AI-powered brand engagement platform for life sciences. Founded in 2019 as RxDefine and legally incorporated as Rise Healthcare Tech, Inc., the Miami-based, remote-first company turns a pharmaceutical brand''s existing PRC/MLR-approved content into compliant, two-way conversational AI across web, email and SMS. Its products are Navigate (web engagement), Airmark (conversational email for HCPs), Prompt (SMS) and Tailor (brand-website intelligence), unified in September 2025 into a single digital experience. The platform is grounded exclusively in approved content and is designed not to generate novel responses, which is how it clears promotional-review requirements. Veeva Systems (NYSE: VEEV) acquired Ostro on 2026-03-10 for approximately $100M and runs it as an independent unit whose capabilities are being folded into Veeva Commercial Cloud. Ostro publishes no public developer program, API reference or machine-readable contract; its only machine-readable
  surface is an llms.txt served at its own website root.'
image: https://cdn.prod.website-files.com/634f008d7831c61867845aad/69dd6a20fe40f5dff2a56a40_Veeva-Ostro-Open-Graph.png
layout: provider
modified: '2026-08-26'
name: Ostro
nav: Providers
network: true
overview: 'Ostro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Pharmaceuticals, Healthcare, and Artificial Intelligence.


  Ostro''s developer surface includes engineering blog and 12 more developer resources.'
plans:
- name: Ostro Plans Pricing
  plan_count: 0
  slug: ostro-plans-pricing
random_paper: 0
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Ostro Domain Security
  slug: ostro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ostro
tags:
- Company
- Life Sciences
- Pharmaceuticals
- Healthcare
- Artificial Intelligence
- Conversational AI
- Patient Engagement
- Marketing
- Software-as-a-Service
website: https://ostro.veeva.com/
---
