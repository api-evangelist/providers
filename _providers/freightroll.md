---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/freightroll-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freightroll-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freightroll-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.freightroll.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.freightroll.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freightroll.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freightroll.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://freightroll.com
created: '2026-07-17'
description: FreightRoll is a logistics technology company whose flagship product, YardOS, is a customizable Yard Operating / Management System (YMS) that turns shipping and receiving yards into driver-friendly, self-service hubs. YardOS reduces truck-driver wait times, improves yard throughput, and streamlines gate and dock operations, with the company citing up to a 50% reduction in truck turnaround time, 95%+ fewer human-to-driver interactions, and $100K+ annual savings per facility across a network of 150,000+ registered drivers. FreightRoll integrates with existing systems across API, EDI, and SFTP mechanisms and deploys remotely in under an hour. The company is backed by 500 Global. FreightRoll does not currently publish a public developer portal, API reference, or OpenAPI definition; its public website is Wix-hosted and exposes a Wix Site MCP endpoint for agentic AI access to public site content.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freightroll.png
layout: provider
mcp_servers:
- description: ''
  name: FreightRoll MCP Server
  slug: freightroll-mcp-server
modified: '2026-07-19'
name: FreightRoll
nav: Providers
network: true
overview: 'FreightRoll is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Yard Management, Supply Chain, and Freight.


  FreightRoll''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freightroll/refs/heads/main/screenshots/freightroll-2026-07-25T215156.png
security:
- kind: domain-security
  name: Freightroll Domain Security
  slug: freightroll-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freightroll
tags:
- Company
- Logistics
- Yard Management
- Supply Chain
- Freight
- Transportation
- Trucking
website: https://freightroll.com
---
