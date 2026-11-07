---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/evertrue/well-known/evertrue-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/evertrue-status-security.txt
- group: agent
  href: https://artifacts.apis.io/evertrue/well-known/evertrue-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evertrue-well-known.yml
- group: other
  href: https://artifacts.apis.io/evertrue/hosts/evertrue-hosts.yml
  title: ''
  type: Hosts
  url: hosts/evertrue-hosts.yml
- group: build
  href: https://artifacts.apis.io/evertrue/integrations/evertrue-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/evertrue-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/evertrue/vendors/evertrue-vendors.yml
  title: ''
  type: Vendors
  url: vendors/evertrue-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.evertrue.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.evertrue.com/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.evertrue.com/t/p8hc02b/lesson-1-getting-started
- group: company
  title: ''
  type: Website
  url: https://www.evertrue.com/
- group: start
  title: ''
  type: Login
  url: https://accounts.evertrue.com/
- group: operate
  title: ''
  type: Support
  url: https://www.evertrue.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.evertrue.com/
- group: company
  title: ''
  type: Blog
  url: https://www.evertrue.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/evertrue
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.evertrue.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.evertrue.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://help.evertrue.com/category/guides
- group: agent
  href: https://artifacts.apis.io/evertrue/llms/evertrue-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evertrue-llms.txt
- group: auth
  href: https://artifacts.apis.io/evertrue/security/evertrue-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evertrue-domain-security.yml
coverage:
  checked: '2026-10-20'
  detail: EverTrue's api.evertrue.com answers its GraphQL endpoint with 401 and its root and /openapi.json with a 504, and neither help.evertrue.com nor the github.com/evertrue org publishes a contract, SDK or developer reference.
  evidence:
  - status: 401
    url: https://api.evertrue.com/graphql
  - status: 504
    url: https://api.evertrue.com/openapi.json
  - status: 200
    url: https://help.evertrue.com/
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: 'EverTrue is a donor experience and fundraising platform for nonprofit, higher-education, and healthcare advancement teams, serving more than 13,000 teams. Its product suite spans AI-driven prospect identification and research (Signal, DonorSearch), donor outreach and stewardship (ThankView personalized video, Pledgemine direct mail), and endowment reporting (Balance, Impact, ODDER). EverTrue integrates with advancement CRMs such as Blackbaud Raiser''s Edge NXT via an automated data sync. EverTrue operates as a closed B2B SaaS: it runs internal REST APIs behind its iOS, Android, and single-page web applications but does not publish a public developer portal, OpenAPI specification, or self-serve API program. Backed by Bain Capital Ventures and Techstars.'
image: https://www.evertrue.com/wp-content/uploads/2026/01/New-Evertrue-logoHomepage-A.png
layout: provider
modified: '2026-07-19'
name: EverTrue
nav: Providers
network: true
overview: 'EverTrue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Fundraising, Non-Profit, and Donor Management.


  EverTrue''s developer surface includes getting-started guide, support, engineering blog, documentation, and 15 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 56.3
    operational_transparency: 21.1
  previous_composite: 20.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/evertrue/evertrue-2026-08-07T165040.png
security:
- kind: domain-security
  name: Evertrue Domain Security
  slug: evertrue-domain-security
  summary_line: TLSv1.3 · DMARC
slug: evertrue
tags:
- Company
- Ai Apps
- Fundraising
- Non-Profit
- Donor Management
- Higher Education
- Advancement
- Prospect Research
- Stewardship
website: https://www.evertrue.com/
---
