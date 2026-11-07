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
    agent_skills: unknown
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
  score: 4.1
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Privacy‑first events from Luxonis OAK cameras for AI agents, as JSON lines and MCP tools. Self‑hosted; MCP Registry name io.github.cloudlabworks/oak-events.
  name: oak-events MCP server
  slug: oak-events-mcp-server
- description: A deliberately faulty MCP server and bounded reference-client harness for testing agent clients against tool errors, delays, malformed results and disconnects. Self‑hosted.
  name: MCP Failure Lab
  slug: mcp-failure-lab
- description: Re‑runnable receipts that check an AI agent's completion claims against the real system. Also packaged as a Gemini CLI extension.
  name: prove-it-done agent skill
  slug: prove-it-done-agent-skill
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/cloudlabworks/security/cloudlabworks-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cloudlabworks-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/cloudlabworks/llms/cloudlabworks-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudlabworks-llms.txt
- group: auth
  href: https://artifacts.apis.io/cloudlabworks/well-known/cloudlabworks-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cloudlabworks-security.txt
- group: agent
  href: https://artifacts.apis.io/cloudlabworks/well-known/cloudlabworks-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudlabworks-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloudlabworks/hosts/cloudlabworks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudlabworks-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudlabworks/vendors/cloudlabworks-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudlabworks-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://cloudlabworks.dev/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudlabworks.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudlabworks.dev/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://cloudlabworks.dev/media/duvall-map.svg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/issaquahd
- group: company
  title: ''
  type: Blog
  url: https://cloudlabworks.dev/blog/feed.xml
- group: auth
  href: https://artifacts.apis.io/cloudlabworks/security/cloudlabworks-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudlabworks-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudlabworks/security/cloudlabworks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudlabworks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cloudlabworks.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudlabworks.dev/llms.txt
coverage:
  checked: '2026-11-02'
  detail: CloudLab Works provides only self‑hosted open‑source tools with no public API or developer program.
  evidence:
  - status: 200
    url: https://cloudlabworks.dev/apis.json
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: CloudLab Works provides open-source, MIT‑licensed reliability tools for hybrid multicloud and AI infrastructure. The platform offers a suite of MCP utilities, event processing libraries, and detailed write‑ups to help developers build robust AI agents. It emphasizes privacy‑first data handling, extensive documentation, and community‑driven support, aiming to simplify complex cloud‑lab environments for both research and production workloads.
image: https://cloudlabworks.dev/media/waku-orca-og.png
layout: provider
mcp_servers:
- description: ''
  name: CloudLab Works MCP Server
  slug: server-json
- description: ''
  name: CloudLab Works MCP Server
  slug: mcp-failure-lab
modified: '2026-11-02'
name: CloudLab Works
nav: Providers
network: true
overview: 'CloudLab Works is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Open Source, MCP, and Cloud.


  CloudLab Works'' developer surface includes engineering blog, documentation, and 14 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 14.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.2
    discoverability: 70.8
    operational_transparency: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cloudlabworks Domain Security
  slug: cloudlabworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cloudlabworks Vulnerability Disclosure
  slug: cloudlabworks-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cloudlabworks
tags:
- Company
- Artificial Intelligence
- Open Source
- MCP
- Cloud
- Tools
website: https://cloudlabworks.dev/
---
