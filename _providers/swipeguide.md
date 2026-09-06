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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for the L2L Dispatch Smart Manufacturing Platform. HTTPS GET/POST/PUT/DELETE over per-tenant hosts, API-key authenticated, JSON by default (XML optional). Covers 60+ shop-floor resources incl
  name: L2L Dispatch API
  slug: l2l-dispatch-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/swipeguide-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.l2l.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.leading2lean.com/hc/en-us/articles/360051148492-API-Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://support.leading2lean.com/hc/en-us/sections/360010979571-APIs-Integration
- group: start
  title: ''
  type: GettingStarted
  url: https://support.leading2lean.com/hc/en-us/articles/360051600711-API-Code-Examples
- group: operate
  title: ''
  type: Support
  url: https://support.leading2lean.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.l2l.com/customer-support
- group: company
  title: ''
  type: Blog
  url: https://www.l2l.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leading2lean
- group: start
  title: ''
  type: SignUp
  url: https://www.l2l.com/get-started
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.l2l.com/trust-center
- group: auth
  title: ''
  type: Compliance
  url: https://www.l2l.com/security-compliance
- group: operate
  title: ''
  type: ChangeLog
  url: https://leading2lean.atlassian.net/wiki/spaces/LCL/overview
- group: build
  title: ''
  type: Packages
  url: packages/swipeguide-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/swipeguide-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/swipeguide-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swipeguide-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swipeguide-llms.txt
created: '2026-07-17'
description: SwipeGuide was a frontline digital work-instruction platform for manufacturing that has since been acquired by L2L (formerly Leading2Lean); the swipeguide.com domain now 301-redirects to l2l.com. L2L operates a Connected Workforce / Connected Manufacturing Operations platform (the L2L Dispatch Smart Manufacturing Platform) spanning maintenance, production monitoring, quality, skills, and digital work instructions on the shop floor. It exposes the L2L Dispatch REST API (v1.0) for reading and writing shop-floor data — sites, areas, lines, machines, dispatches, pitches, work orders, kaizen and more — authenticated with an API key (query auth, L2LAUTH header, or POST body) plus optional HMAC-SHA512 request signing, returning JSON (default) or XML.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/swipeguide.png
layout: provider
modified: '2026-07-21'
name: Swipeguide
nav: Providers
network: true
overview: 'Swipeguide publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Work Instructions, Frontline, and Shop Floor.


  Swipeguide''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 11 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/swipeguide/refs/heads/main/screenshots/swipeguide-2026-09-02T161410.png
security:
- kind: authentication
  name: Swipeguide Authentication
  slug: swipeguide-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Swipeguide Domain Security
  slug: swipeguide-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Swipeguide Trust Center
  slug: swipeguide-trust-center
  summary_line: SOC 2 Type 2, NIST 800-171, 21 CFR Part 11, ISO 13485, ISO 55000, ITAR, DFARS, GDPR, CCPA
slug: swipeguide
tags:
- Company
- Manufacturing
- Work Instructions
- Frontline
- Shop Floor
- Maintenance
- Connected Worker
- Smart Manufacturing
- Industrial
website: https://www.l2l.com/
---
