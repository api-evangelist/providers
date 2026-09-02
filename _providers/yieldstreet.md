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
  url: security/yieldstreet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.willowwealth.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/yieldstreet_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yieldstreet
- group: company
  title: ''
  type: Blog
  url: https://www.willowwealth.com/blog
- group: auth
  title: ''
  type: Security
  url: https://www.willowwealth.com/vulnerability-disclosure-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/yieldstreet-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yieldstreet-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yieldstreet-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-05'
  detail: Every developer host is NXDOMAIN on both willowwealth.com and the legacy yieldstreet.com (api., developer., docs., dev.), the yieldstreet GitHub org's 14 public repos are internal Scala/Akka and React Native forks with no client library, and no package exists on npm, PyPI or RubyGems - the private-markets platform is sold as an end-user web and mobile product only.
  evidence:
  - status: 0
    url: https://api.willowwealth.com/
  - status: 0
    url: https://developer.willowwealth.com/
  - status: 404
    url: https://www.willowwealth.com/.well-known/api-catalog
  - status: 404
    url: https://www.willowwealth.com/.well-known/agent-card.json
  - status: 404
    url: https://registry.npmjs.org/yieldstreet
  - status: 200
    url: https://api.github.com/orgs/yieldstreet/repos
  - status: 200
    url: https://www.willowwealth.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: Willow Wealth Inc. - formerly Yieldstreet - is a New York City financial technology company that operates an online private-markets investing platform, giving accredited and retail investors access to alternative asset classes including real estate, private credit, private equity, art, legal finance, and third-party evergreen funds from institutional managers. Founded in 2015 by Milind Mehere and Michael Weisz, the platform reports more than 500,000 members and over $6 billion in cumulative investments, and renamed itself Willow Wealth in late 2025. Investors reach it through a web portal and iOS/Android apps; the company publishes no public developer program, API reference, or machine-readable specification.
image: https://www.willowwealth.com/favicon.ico
layout: provider
modified: '2026-08-05'
name: Willow Wealth
nav: Providers
network: true
overview: 'Willow Wealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alternative Investments, Private Markets, Investing, and Wealth Management.


  Willow Wealth''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 7.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Yieldstreet Domain Security
  slug: yieldstreet-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Yieldstreet Vulnerability Disclosure
  slug: yieldstreet-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: yieldstreet
tags:
- Company
- Alternative Investments
- Private Markets
- Investing
- Wealth Management
- Financial-Services
- Fintech
- Real-Estate
- Private Credit
website: https://www.willowwealth.com/
---
