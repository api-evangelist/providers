---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  trial: false
  try_now: true
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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote MCP server (Streamable HTTP, OAuth) that gives AI agents cited Korean AEC knowledge -- KDS/KCS construction standards, KS standards, building laws and annexed tables, and structural, constructi
  name: Den MCP Server
  slug: den-mcp-server
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/den-archi/plans/den-archi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/den-archi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/den-archi/conventions/den-archi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/den-archi-conventions.yml
- group: auth
  href: https://artifacts.apis.io/den-archi/authentication/den-archi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/den-archi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/den-archi/scopes/den-archi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/den-archi-scopes.yml
- group: design
  href: https://artifacts.apis.io/den-archi/lifecycle/den-archi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/den-archi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/den-archi/conformance/den-archi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/den-archi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/den-archi/mcp/den-archi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/den-archi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/den-archi/well-known/den-archi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/den-archi-well-known.yml
- group: other
  href: https://artifacts.apis.io/den-archi/hosts/den-archi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/den-archi-hosts.yml
- group: build
  href: https://artifacts.apis.io/den-archi/integrations/den-archi-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/den-archi-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/den-archi/vendors/den-archi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/den-archi-vendors.yml
- group: build
  href: https://artifacts.apis.io/den-archi/packages/den-archi-packages.yml
  title: ''
  type: SDKs
  url: packages/den-archi-packages.yml
- group: build
  href: https://artifacts.apis.io/den-archi/packages/den-archi-packages.yml
  title: ''
  type: Packages
  url: packages/den-archi-packages.yml
- group: auth
  href: https://artifacts.apis.io/den-archi/security/den-archi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/den-archi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://den.archi/
- group: start
  title: ''
  type: GettingStarted
  url: https://den.archi/beta.html
- group: start
  title: ''
  type: SignUp
  url: https://mcp.den.archi/signup?via=landing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://den.archi/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://den.archi/privacy.html
created: '2026-11-05'
description: 'Den (den.archi) is a Korean AEC (architecture, engineering and construction) knowledge-curation system delivered as a remote MCP server. It gives AI agents normative and practical AEC knowledge with citations: Korean national construction standards (KDS and KCS), KS standards, building-related laws and their annexed tables, plus structural, construction, MEP, materials and planning know-how. Each clause and number carries its source and applicability conditions, facts are separated from interpretations, and content Den does not hold is explicitly marked as not held. Its tools cover standard/clause lookup, term definitions, causal explanations, construction sequences, method comparisons, site conditions, floor-plan code review and concept linking. It connects to Claude and ChatGPT as a custom connector and is offered as a free beta by application (support@den.archi).'
image: https://den.archi/assets/logo/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.den.archi over streamable HTTP requiring OAuth; 13 tools listed.
  name: Den MCP Server
  slug: den-mcp
modified: '2026-11-05'
name: Den
nav: Providers
network: true
overview: 'Den is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Architecture, Construction, AEC, and Building Codes.


  Den''s developer surface includes authentication, getting-started guide, signup flow, and 16 more developer resources.'
plans:
- name: Den Archi Plans Pricing
  plan_count: 1
  slug: den-archi-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Den Archi Rate Limits
  slug: den-archi-rate-limits
scopes:
- name: Den Archi Scopes
  scope_count: 1
  slug: den-archi-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Den Archi Authentication
  slug: den-archi-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Den Archi Domain Security
  slug: den-archi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: den-archi
tags:
- Company
- Architecture
- Construction
- AEC
- Building Codes
- Standards
- Knowledge Base
- MCP
- AI Agents
- South Korea
website: https://den.archi/
---
