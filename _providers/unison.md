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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unison-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unison.com/
- group: company
  title: ''
  type: Blog
  url: https://www.unison.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.unison.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.unison.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unison.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unison.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/firstrex
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unison-llms.txt
coverage:
  checked: '2026-09-02'
  detail: 'Unison is a consumer home-equity investment manager whose only software products are the www.unison.com Webflow marketing site and the MyUnison agreement portal: its 308-URL sitemap contains no developer, API or docs page, /developers, /developer, /api and /docs all 404, api.unison.com, developer.unison.com and docs.unison.com do not resolve, the /partnership page is a business-development contact form with no technical integration surface, and the company GitHub org (github.com/firstrex, Unison''s pre-rebrand name) holds only hiring mini-projects and forked style guides — so there is no developer program to profile, only a provider-published llms.txt.'
  evidence:
  - status: 200
    url: https://www.unison.com/llms.txt
  - status: 200
    url: https://www.unison.com/sitemap.xml
  - status: 404
    url: https://www.unison.com/developers
  - status: 404
    url: https://www.unison.com/api
  - status: 404
    url: https://www.unison.com/openapi.json
  - status: 404
    url: https://www.unison.com/.well-known/agent-card.json
  - status: 404
    url: https://www.unison.com/.well-known/agent.json
  - status: 404
    url: https://www.unison.com/.well-known/security.txt
  - status: 200
    url: https://www.unison.com/partnership
  - status: 200
    url: https://github.com/firstrex
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Unison (Unison Home Ownership Investors, headquartered in San Francisco with a second office in Omaha, and formerly FirstREX) is a residential home-equity investment manager that pioneered the equity sharing agreement and institutionalized the Home Equity Investment (HEI) asset class. Its consumer products are the Equity Sharing Agreement — up to roughly $500,000 in cash with no monthly payments and no interest, in exchange for a share of the home's future change in value over a 30-year term — and the Equity Sharing Home Loan, a fixed below-market-rate, interest-only mortgage. Unison securitizes its agreements and sells them to institutional investors, including a $300 million equity sharing home loan purchase partnership with Carlyle. It reaches homeowners through www.unison.com and services existing agreements through the MyUnison portal at my.unison.com. Unison publishes no public developer program, no API reference, no SDKs and no machine-readable contract of any kind; the
  only agent-facing artifact it serves is an llms.txt at the site root.
image: https://cdn.prod.website-files.com/688b907742517387194e886d/688bcf59a60dac663e6ab4c4_Unison%20symbol%20square%20brand.png
layout: provider
modified: '2026-09-02'
name: Unison
nav: Providers
network: true
overview: 'Unison is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Fintech, Real Estate, and Home Equity.


  Unison''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Unison Domain Security
  slug: unison-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unison
tags:
- Company
- Financial Services
- Fintech
- Real Estate
- Home Equity
- Mortgage
- Consumer Finance
- Investment Management
website: https://www.unison.com/
---
