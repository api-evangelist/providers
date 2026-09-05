---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lenovo Agentic Access
  operation_count: 8
  slug: lenovo-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: The Lenovo XClarity Administrator REST API provides programmatic access to XClarity Administrator data and services from applications running outside of the XClarity Administrator framework. It suppor
  name: Lenovo XClarity Administrator REST API
  slug: lenovo-xclarity-administrator-rest-api
- baseURL_template: https://{xclarityHost}
  baseurl_source: spec_template
  description: Query inventory of managed devices.
  name: Lenovo Inventory API
  slug: lenovo-inventory-api
- baseURL_template: https://{xclarityHost}
  baseurl_source: spec_template
  description: Authenticate and manage XClarity Administrator sessions.
  name: Lenovo Sessions API
  slug: lenovo-sessions-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lenovo XClarity Administrator REST Inventory API
  slug: open-lenovo-inventory-api
- collection_type: open
  name: Lenovo XClarity Administrator REST Inventory Sessions API
  slug: open-lenovo-sessions-api
- collection_type: open
  name: Lenovo XClarity Administrator REST API
  slug: open-lenovo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lenovo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lenovo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lenovo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lenovo
- group: company
  title: ''
  type: Website
  url: https://www.lenovo.com/
- group: company
  title: ''
  type: AboutUs
  url: https://www.lenovo.com/us/en/about/
- group: other
  title: ''
  type: Products
  url: https://www.lenovo.com/us/en/d/sale/all-products/
- group: operate
  title: ''
  type: DataCenterSupport
  url: https://datacentersupport.lenovo.com/
- group: company
  title: ''
  type: PartnerHub
  url: https://www.lenovopartnerhub.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lenovo
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.lenovo.com/
- group: company
  title: ''
  type: News
  url: https://news.lenovo.com/
- group: company
  title: ''
  type: Careers
  url: https://www.lenovo.com/us/en/about/careers/
- group: company
  title: ''
  type: Blog
  url: https://news.lenovo.com/feed/
created: '2026-05-05'
description: Lenovo Group is a Chinese multinational technology company and one of the world's largest personal computer vendors by unit sales. Lenovo designs, manufactures, and sells PCs, tablets, smartphones, workstations, servers, storage, and data center infrastructure solutions globally. Lenovo exposes a REST API for its XClarity Administrator data center management platform and publishes open-source projects through its GitHub organization, but does not operate a general-purpose consumer or partner developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lenovo.png
layout: provider
modified: '2026-05-16'
name: Lenovo
nav: Providers
network: true
overview: 'Lenovo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inventory API and Sessions API. Tagged areas include Data-Center, Hardware, Infrastructure, Personal Computers, and Servers.


  Lenovo''s developer surface includes authentication, product news, engineering blog, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lenovo/refs/heads/main/screenshots/lenovo-2026-06-20T184423.png
security:
- kind: authentication
  name: Lenovo Authentication
  slug: lenovo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lenovo Domain Security
  slug: lenovo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lenovo
tags:
- Data-Center
- Hardware
- Infrastructure
- Personal Computers
- Servers
- Technology
website: https://www.lenovo.com/
---
