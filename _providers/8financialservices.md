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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/8financialservices/
coverage:
  checked: '2026-09-05'
  detail: 8 Financial Intelligence has no discoverable first-party web presence at all — the only public page about the company is its EquityZen secondary-market listing, which carries a description and funding figure but no outbound company link, no logo link and no domain, while the brand-obvious domains are all parked or brokered (8fi.com 403s to a Sedo sales lander, 8fi.ai serves a parity.domains parking page, eightfi.com redirects to a namebamboo.com for-sale page) and sixteen other candidate domains plus every snyamic.* variant of the company's former name do not resolve in DNS, so there was no company-controlled host against which to probe for an OpenAPI, GraphQL, MCP, agent card, well-known document or llms.txt.
  evidence:
  - status: 200
    url: https://equityzen.com/company/8financialservices/
  - status: 403
    url: https://www.crunchbase.com/organization/8-financial-services
  - status: 403
    url: http://8fi.com/
  - status: 200
    url: http://8fi.ai/
  - status: 200
    url: https://eightfi.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '8 Financial Intelligence (8FI) is a privately held artificial-intelligence research and deployment company focused on financial engineering, established in 2016 under the name Snyamic Technology Limited (動力科創有限公司) and headquartered in Hong Kong SAR, with stated operations and partnerships in Cyprus, Estonia, Israel, Singapore and the United States. Its publicly stated positioning is autonomous AI and financial-engineering systems rather than a packaged product, and its only reported financing is HKD 2.3 billion (roughly USD 300 million) from Parallel Strategy, an alternative asset manager investing in large-scale AI technology and infrastructure. Every one of these facts is drawn from a single public source — the EquityZen secondary-market listing recorded below — because API Evangelist could not locate a company-controlled website, developer portal, documentation host, GitHub organisation or any other first-party property for 8 Financial Intelligence. The company therefore
  has no observable API surface: no public API, SDK, webhook catalogue, MCP server, agent card or machine-readable specification of any kind was found, and none could be probed, because no host attributable to the company was discoverable to probe. This profile is a factual record of what is publicly observable, not an assessment of the company''s technology.'
layout: provider
modified: '2026-09-05'
name: 8 Financial Intelligence
nav: Providers
network: true
overview: 8 Financial Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Financial Engineering, Financial Services, and Fintech.
random_paper: 9
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  schema_version: 0.18.3
  scored_at: '2026-09-05'
slug: 8financialservices
tags:
- Company
- Artificial Intelligence
- Financial Engineering
- Financial Services
- Fintech
- Data and Analytics
- Machine Learning
- Hong Kong
- Private Company
---
