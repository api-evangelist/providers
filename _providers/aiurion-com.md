---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public agent API for creating guest sessions, requesting free 3D print quotes, obtaining approval, creating Stripe Checkout URLs, and tracking model review and fulfillment.
  name: Agentic 3D Printing API
  slug: agentic-3d-printing-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/aiurion-com/vocabulary/aiurion-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiurion-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aiurion-com/conformance/aiurion-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiurion-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiurion-com/llms/aiurion-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiurion-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiurion-com/mcp/aiurion-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiurion-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aiurion-com/well-known/aiurion-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiurion-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiurion-com/hosts/aiurion-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiurion-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiurion-com/vendors/aiurion-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiurion-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aiurion-com/security/aiurion-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiurion-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiurion.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aiurion.com/about
- group: docs
  title: ''
  type: APIReference
  url: https://aiurion.com/api/agent/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://aiurion.com/about
- group: operate
  title: ''
  type: Support
  url: https://aiurion.com/contact
- group: company
  title: ''
  type: Blog
  url: https://aiurion.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiurion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiurion.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiurion.com/privacy
created: '2026-11-01'
description: Aiurion provides same-day FDM 3D printing services in San Francisco, offering a range of high-performance materials such as carbon fiber reinforced nylon, PETG, ASA, and flexible TPU. Customers can upload CAD files in formats like STL, OBJ, STEP, and 3MF to receive instant quotes and rapid turnaround, typically within 24‑48 hours. The service includes on‑site support, engineering consultation, and a transparent pricing model with a $100 minimum per job. Aiurion operates from a secure, air‑gapped production facility, ensuring IP confidentiality for hardware startups, robotics teams, and engineers.
image: https://aiurion.com/aiurion-mark-150.png
layout: provider
mcp_servers:
- description: Remote MCP server at aiurion.com.
  name: Aiurion MCP Server
  slug: aiurion-com-mcp-yml
modified: '2026-11-01'
name: Aiurion
nav: Providers
network: true
overview: 'Aiurion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, Manufacturing, Rapid Prototyping, San Francisco, and Hardware.


  Aiurion''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 12 more developer resources.'
random_paper: 19
scopes:
- name: Aiurion Com Scopes
  scope_count: 0
  slug: aiurion-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 10.5
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 21.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aiurion Com Authentication
  slug: aiurion-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aiurion Com Domain Security
  slug: aiurion-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aiurion-com
tags:
- 3D Printing
- Manufacturing
- Rapid Prototyping
- San Francisco
- Hardware
website: https://aiurion.com/
---
