---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The BSEE Well API provides multiregional offshore well information retrieval across Alaska, Atlantic, Gulf of America, and Pacific regions. Query by API well number, company name, well status, field n
  name: BSEE Well API Online Query
  slug: bsee-well-api
- description: The BSEE Data Center provides online query services and data downloads for offshore oil and gas operations. Data covers company information, leasing, pipelines, wells, production, platforms, and permi
  name: BSEE Data Center
  slug: bsee-data-center
- description: The Technical Information Management System (TIMS) / eWell system enables permit submissions and well activity reporting for offshore operations. Operators use this system to submit Applications for P
  name: BSEE eWell Permitting System (TIMS)
  slug: tims-eplanning
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bureau-of-safety-and-environmental-enforcement-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bureau-of-safety-and-environmental-enforcement-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-safety-and-environmental-enforcement
- group: company
  title: ''
  type: Website
  url: https://www.bsee.gov/
- group: start
  title: ''
  type: Portal
  url: https://www.data.bsee.gov/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bsee.gov/privacy-policy
- group: start
  title: ''
  type: Data Portal
  url: https://catalog.data.gov/dataset?organization=bsee-gov
- group: company
  title: ''
  type: Blog
  url: https://www.bsee.gov/rss.xml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bureau-of-safety-and-environmental-enforcement-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/bureau-of-safety-and-environmental-enforcement-security.txt
- group: auth
  title: ''
  type: Security
  url: security/bureau-of-safety-and-environmental-enforcement-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bureau-of-safety-and-environmental-enforcement-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/bureau-of-safety-and-environmental-enforcement-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bureau-of-safety-and-environmental-enforcement-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bureau-of-safety-and-environmental-enforcement-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bureau-of-safety-and-environmental-enforcement-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/bureau-of-safety-and-environmental-enforcement-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bureau-of-safety-and-environmental-enforcement-rate-limits.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.data.bsee.gov/Main/RawData.aspx
- group: start
  title: ''
  type: GettingStarted
  url: https://www.data.bsee.gov/Main/Tutorials/OnlineQuery.aspx
- group: operate
  title: ''
  type: Support
  url: https://www.data.bsee.gov/Main/HtmlPage.aspx?page=contactbsee
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DOI-BSEE
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bsee.gov/who-we-are/working-with-us/doing-business-with-bsee/fees-for-services
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bsee.gov/site-page/disclaimer
- group: start
  title: ''
  type: Login
  url: https://timsweb.bsee.gov/
coverage:
  checked: '2026-09-05'
  detail: BSEE's offshore data is fully public and free, but it is only reachable through ASP.NET online-query forms and zipped delimited-ASCII downloads on www.data.bsee.gov — no OpenAPI, GraphQL, AsyncAPI, WSDL or MCP contract exists on any bsee.gov host, and the host answers HTTP 200 with a "Data Center 404 Error" HTML shell for every path that does not exist, so even path discovery returns false positives.
  evidence:
  - status: 200
    url: https://www.data.bsee.gov/openapi.json
  - status: 200
    url: https://www.data.bsee.gov/zzzz-not-a-real-page.aspx
  - status: 404
    url: https://www.bsee.gov/llms.txt
  - status: 404
    url: https://www.bsee.gov/data.json
  - status: 200
    url: https://timsweb.bsee.gov/
  reason: no-machine-readable-spec
  state: unreadable
created: '2024-11-30'
description: The Bureau of Safety and Environmental Enforcement (BSEE) is the U.S. Department of the Interior bureau that promotes safety, protects the environment and conserves resources offshore through regulatory oversight and enforcement of oil, gas and mineral operations on the Outer Continental Shelf. BSEE publishes the authoritative public record of offshore wells, leases, pipelines, platforms, production, exploration and development plans and incidents of non-compliance through the BSEE Data Center, as HTML online-query applications and zipped delimited-ASCII bulk downloads, and operates the eWell/TIMS permitting system that offshore operators use to file permits and activity reports. BSEE publishes no OpenAPI, GraphQL, AsyncAPI, SOAP or MCP contract; note that "API" in BSEE's own vocabulary means the American Petroleum Institute well number, not an application programming interface.
finops:
- name: Bureau Of Safety And Environmental Enforcement Finops
  service_category: API
  slug: bureau-of-safety-and-environmental-enforcement-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bureau-of-safety-and-environmental-enforcement.png
layout: provider
modified: '2026-09-05'
name: Bureau of Safety and Environmental Enforcement
nav: Providers
network: true
overview: 'Bureau of Safety and Environmental Enforcement publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enforcement, Environment, Federal-Government, Safety, and Offshore.


  Bureau of Safety and Environmental Enforcement''s developer surface includes developer portal, engineering blog, documentation, getting-started guide, support, pricing, and 19 more developer resources.'
plans:
- name: Bureau Of Safety And Environmental Enforcement Plans Pricing
  plan_count: 0
  slug: bureau-of-safety-and-environmental-enforcement-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Bureau Of Safety And Environmental Enforcement Rate Limits
  slug: bureau-of-safety-and-environmental-enforcement-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.9
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 17.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/bureau-of-safety-and-environmental-enforcement/refs/heads/main/screenshots/bureau-of-safety-and-environmental-enforcement-2026-06-20T173818.png
security:
- kind: domain-security
  name: Bureau Of Safety And Environmental Enforcement Domain Security
  slug: bureau-of-safety-and-environmental-enforcement-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Bureau Of Safety And Environmental Enforcement Vulnerability Disclosure
  slug: bureau-of-safety-and-environmental-enforcement-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bureau-of-safety-and-environmental-enforcement
tags:
- Enforcement
- Environment
- Federal-Government
- Safety
- Offshore
- Oil and Gas
- Wells
website: https://www.bsee.gov/
---
