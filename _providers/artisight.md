---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: The public WordPress REST API served from artisight.com. It is the marketing/content API for the corporate website — posts, pages, media, taxonomies, case studies and the site route index — not a clin
  name: Artisight Website Content API
  slug: website-content-api
- description: A Model Context Protocol server published from artisight.com by the WordPress MCP Adapter, backed by the WordPress Abilities API. Discovery is anonymous — RFC 8414 authorization-server metadata and RF
  name: Artisight MCP Server
  slug: mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://artisight.com/
- group: company
  title: ''
  type: About
  url: https://artisight.com/about/
- group: company
  title: ''
  type: Blog
  url: https://artisight.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://artisight.com/feed/
- group: company
  title: ''
  type: Press
  url: https://artisight.com/press-releases/
- group: other
  title: ''
  type: CaseStudies
  url: https://artisight.com/case-studies/
- group: company
  title: ''
  type: Partners
  url: https://artisight.com/partners/
- group: company
  title: ''
  type: Careers
  url: https://artisight.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://artisight.com/contact/
- group: start
  title: ''
  type: SignUp
  url: https://artisight.com/demo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artisight.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artisight
- group: auth
  title: ''
  type: Compliance
  url: https://artisight.com/smart-hospital-technology/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artisight-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/artisight-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/artisight-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artisight-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/artisight-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artisight-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artisight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artisight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artisight-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artisight-domain-security.yml
created: '2026-08-02'
description: Artisight is a smart hospital platform company founded in 2015 out of Northwestern Medicine that pairs NVIDIA GPU-powered edge sensors — dual 4K cameras, multi-microphone arrays and RTLS radios — with computer vision, speech recognition and deep learning to deliver virtual nursing, ambient clinical documentation, operating-room coordination, patient-safety monitoring, asset and staff tracking, environmental monitoring and predictive analytics across 400+ hospitals in 30+ US health systems. The platform integrates natively and bi-directionally with Epic and Oracle Cerner EHRs, processes video on-premise rather than in the public cloud, and holds HIPAA Expert Determination Certification. Artisight publishes no public developer program, product API or SDK; its only public machine-readable surfaces are the WordPress content REST API, an OAuth 2.0-protected MCP server and an llms.txt on artisight.com.
image: https://artisight.com/wp-content/uploads/2026/01/Artisight-Fallback-Homepage-Image-Video.jpg
layout: provider
mcp_servers:
- description: ''
  name: Artisight MCP Server
  slug: artisight-mcp-server
modified: '2026-08-02'
name: Artisight
nav: Providers
network: true
overview: 'Artisight publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Computer-Vision, and Hospitals.


  Artisight''s developer surface includes engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 9
scopes:
- name: Artisight Scopes
  scope_count: 1
  slug: artisight-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 61.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artisight/refs/heads/main/screenshots/artisight-2026-08-07T161741.png
security:
- kind: authentication
  name: Artisight Authentication
  slug: artisight-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Artisight Domain Security
  slug: artisight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: artisight
tags:
- Company
- Healthcare
- Artificial Intelligence
- Computer-Vision
- Hospitals
- Ambient Intelligence
- Electronic Health Records
- Machine-Learning
- Patient Monitoring
- Internet of Things
website: https://artisight.com/
---
