---
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'A remote Model Context Protocol (streamable HTTP) server operated by WayUp, a Yello company, at https://www.wayup.com/mcp. Discovered by probe: the host publishes RFC 9728 protected-resource metadata '
  name: WayUp MCP Server
  slug: wayup-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/yello-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://yello.co/
- group: company
  title: ''
  type: Blog
  url: https://yello.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://yello.co/contact/
- group: start
  title: ''
  type: SignUp
  url: https://yello.co/request-a-demo/
- group: commercial
  title: ''
  type: Pricing
  url: https://yello.co/government-recruiting/how-to-buy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yello.co/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yello.co/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://yello.statuspage.io/
- group: auth
  title: ''
  type: Compliance
  url: https://yello.co/trust-and-security/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yello-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/yello-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yello-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yello-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yello-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/yello-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yello-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/yello-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yello-wayup-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yello-llms.txt
created: '2026-09-04'
description: Yello is a Chicago-based talent acquisition software company, founded in 2008 (originally Recsolu), whose enterprise platform runs campus and early-career recruiting for roughly 100 Fortune 500 employers across 70+ countries and 15+ languages. The product line covers campus planning, recruitment events, candidate sourcing, interview scheduling, a recruitment CRM, recruitment analytics and an AI campus recruiting agent, plus Yello Government Recruiting Solutions (YGRS) for public-sector hiring and the WayUp candidate marketplace and Symba new-hire readiness products acquired by the company. Yello Enterprise is delivered as per-customer tenant sites on yello.co and recsolu.com in US (us-east-1) and EU (eu-west-1) environments. Its integration surface with ATS and HRIS systems (Workday, Taleo, Oracle Recruiting Cloud, iCIMS, SAP SuccessFactors, Greenhouse, ADP) is real but is sold and provisioned through a partner/sales conversation rather than a public developer portal. The one
  openly reachable machine surface found is a remote Model Context Protocol server on the WayUp property, published with RFC 8414 / RFC 9728 OAuth discovery.
image: https://yello.co/wp-content/uploads/2021/04/yello-logo@4x.png
layout: provider
mcp_servers:
- description: ''
  name: Yello MCP Server
  slug: yello-mcp-server
modified: '2026-09-04'
name: Yello
nav: Providers
network: true
overview: 'Yello publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Talent Acquisition, Recruiting, Human Resources, Campus Recruiting, and Applicant Tracking.


  Yello''s developer surface includes engineering blog, support, signup flow, pricing, and 16 more developer resources.'
plans:
- name: Yello Plans Pricing
  plan_count: 0
  slug: yello-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Yello Rate Limits
  slug: yello-rate-limits
scopes:
- name: Yello Scopes
  scope_count: 1
  slug: yello-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa-cpra
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 88.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Yello Authentication
  slug: yello-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Yello Domain Security
  slug: yello-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Yello Trust Center
  slug: yello-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
slug: yello
tags:
- Talent Acquisition
- Recruiting
- Human Resources
- Campus Recruiting
- Applicant Tracking
- Recruitment CRM
- Interview Scheduling
- Jobs
- Model Context Protocol
- Government
website: https://yello.co/
---
