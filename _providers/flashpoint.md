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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Flashpoint's REST API exposes threat intelligence, compromised credentials, vulnerability, and fraud data programmatically. Access is documented on the Flashpoint developer portal (docs.flashpoint.io)
  name: Flashpoint API
  slug: flashpoint-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/flashpoint/plans/flashpoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flashpoint-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/flashpoint/mcp/flashpoint-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/flashpoint-mcp.yml
- group: agent
  href: https://artifacts.apis.io/flashpoint/well-known/flashpoint-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/flashpoint-well-known.yml
- group: other
  href: https://artifacts.apis.io/flashpoint/hosts/flashpoint-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flashpoint-hosts.yml
- group: other
  href: https://artifacts.apis.io/flashpoint/vendors/flashpoint-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flashpoint-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flashpoint.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flashpoint.io/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://flashpoint.io/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://flashpoint.io/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://flashpoint.io/blog/feed/
- group: auth
  href: https://artifacts.apis.io/flashpoint/security/flashpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashpoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashpoint.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flashpoint.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flashpoint.io/
- group: company
  title: ''
  type: Blog
  url: https://flashpoint.io/blog/
- group: start
  title: ''
  type: Login
  url: https://flashpoint.io/login/
- group: operate
  title: ''
  type: Support
  url: https://flashpoint.io/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flashpoint-intel
- group: agent
  href: https://artifacts.apis.io/flashpoint/llms/flashpoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flashpoint-llms.txt
coverage:
  checked: '2026-10-20'
  detail: docs.flashpoint.io (ReadMe) redirects every visitor to a login.flashpoint.io SAML sign-in, and the MCP endpoint api.flashpoint.io/mcp answers 401, so no API reference or contract is publicly readable.
  evidence:
  - status: 302
    url: https://docs.flashpoint.io/
  - status: 401
    url: https://api.flashpoint.io/mcp
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Flashpoint is a threat intelligence company delivering decisive intelligence for cybersecurity, fraud prevention, corporate and physical security, vulnerability management, insider threat, and national security teams. Its Ignite platform and Flashpoint API surface data collected from illicit online communities, the deep and dark web, chat services, and open sources — exposing threat actors, compromised credentials, vulnerabilities, and fraud indicators. Flashpoint makes this finished intelligence and raw data available programmatically through a REST API at api.flashpoint.io, documented at docs.flashpoint.io, so security teams can integrate alerting, data feeds, and finished intelligence into SOC, SIEM, and security automation workflows.
image: https://flashpoint.io/wp-content/themes/flashpoint/favicons/favicon-192.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.flashpoint.io over HTTP.
  name: Flashpoint MCP Server
  slug: flashpoint
modified: '2026-10-06'
name: Flashpoint
nav: Providers
network: true
overview: 'Flashpoint is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Threat Intelligence, Cybersecurity, Security, and Fraud Prevention.


  Flashpoint''s developer surface includes pricing, documentation, engineering blog, support, and 15 more developer resources.'
plans:
- name: Flashpoint Plans Pricing
  plan_count: 3
  slug: flashpoint-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Flashpoint Rate Limits
  slug: flashpoint-rate-limits
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.7
    operational_transparency: 5.3
  previous_composite: 30.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/flashpoint/flashpoint-2026-07-25T214719.png
security:
- kind: domain-security
  name: Flashpoint Domain Security
  slug: flashpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flashpoint
tags:
- Company
- Threat Intelligence
- Cybersecurity
- Security
- Fraud Prevention
- Vulnerability Management
- Dark Web
- Data
website: https://flashpoint.io/
---
