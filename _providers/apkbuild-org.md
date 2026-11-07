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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/apkbuild-org/llms/apkbuild-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apkbuild-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/apkbuild-org/mcp/apkbuild-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apkbuild-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/apkbuild-org/hosts/apkbuild-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apkbuild-org-hosts.yml
- group: auth
  href: https://artifacts.apis.io/apkbuild-org/security/apkbuild-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apkbuild-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apkbuild.org/
- group: company
  title: ''
  type: Blog
  url: https://apkbuild.org/blog
- group: operate
  title: ''
  type: Support
  url: https://apkbuild.org/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://apkbuild.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://apkbuild.org/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apkbuild.org/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://apkbuild.org/signup
coverage:
  checked: '2026-11-01'
  detail: APKBuild.org provides a web service but does not publish a developer program or API documentation.
  evidence:
  - status: 200
    url: https://apkbuild.org/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: APKBuild.org provides an online service to build signed Android APK and AAB packages from website URLs or HTML ZIPs without requiring Android Studio, local toolchains, or SDK installation. Users can upload their web app or zip, select signing options, and receive a ready-to-publish APK/AAB. The platform offers pay‑per‑build pricing, Google sign‑in, AI voice generation, and supports various payment methods. It targets developers seeking quick builds and testing without local environment setup.
image: https://apkbuild.org/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at apkbuild.org.
  name: APKBuild.org MCP Server
  slug: apkbuild-org-mcp-yml
modified: '2026-11-01'
name: APKBuild.org
nav: Providers
network: true
overview: 'APKBuild.org is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Android, Builds, APK, AAB, and Online.


  APKBuild.org''s developer surface includes engineering blog, support, pricing, signup flow, getting-started guide, and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 14.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apkbuild Org Domain Security
  slug: apkbuild-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apkbuild-org
tags:
- Android
- Builds
- APK
- AAB
- Online
- Tool
website: https://apkbuild.org/
---
