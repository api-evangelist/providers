---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 21.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/dokutrak-com/plans/dokutrak-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dokutrak-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dokutrak.com/security
- group: agent
  href: https://artifacts.apis.io/dokutrak-com/llms/dokutrak-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokutrak-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dokutrak-com/mcp/dokutrak-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dokutrak-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dokutrak-com/well-known/dokutrak-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokutrak-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dokutrak-com/hosts/dokutrak-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dokutrak-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dokutrak-com/vendors/dokutrak-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dokutrak-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/dokutrak-com/packages/dokutrak-com-packages.yml
  title: ''
  type: SDKs
  url: packages/dokutrak-com-packages.yml
- group: build
  href: https://artifacts.apis.io/dokutrak-com/packages/dokutrak-com-packages.yml
  title: ''
  type: Packages
  url: packages/dokutrak-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dokutrak.com/terms
- group: auth
  title: ''
  type: Security
  url: https://dokutrak.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dokutrak.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dokutrak.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dokutrak
- group: company
  title: ''
  type: Blog
  url: https://dokutrak.com/blog
- group: auth
  href: https://artifacts.apis.io/dokutrak-com/security/dokutrak-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dokutrak-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dokutrak-com/security/dokutrak-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dokutrak-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dokutrak-com/security/dokutrak-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokutrak-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokutrak.com/
coverage:
  checked: '2026-11-05'
  detail: No public developer documentation or API specifications were found on dokutrak.com or its API host.
  evidence:
  - status: 200
    url: https://dokutrak.com/
  reason: no-developer-program
  state: none
created: '2026-11-05'
description: DokuTrak provides client document collection software that enables secure, no‑login upload links, automated follow‑ups, missing‑file tracking, and first‑pass AI document checks. Built for accountants, law firms, mortgage brokers, real‑estate agents, recruiters, HR teams, consultants and agencies, it streamlines the document chase so businesses can collect client files efficiently and securely.
image: https://dokutrak.com/og-default.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at app.dokutrak.com.
  name: DokuTrak MCP Server
  slug: dokutrak-com-mcp-yml
modified: '2026-11-05'
name: DokuTrak
nav: Providers
network: true
overview: 'DokuTrak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include DocumentCollection, NoLoginUpload, AI Review, SecureDocs, and Software-as-a-Service.


  DokuTrak''s developer surface includes pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Dokutrak Com Plans Pricing
  plan_count: 3
  slug: dokutrak-com-plans-pricing
random_paper: 9
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.3
    operational_transparency: 15.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dokutrak Com Domain Security
  slug: dokutrak-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dokutrak Com Vulnerability Disclosure
  slug: dokutrak-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Dokutrak Com Trust Center
  slug: dokutrak-com-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: dokutrak-com
tags:
- DocumentCollection
- NoLoginUpload
- AI Review
- SecureDocs
- Software-as-a-Service
website: https://dokutrak.com/
---
