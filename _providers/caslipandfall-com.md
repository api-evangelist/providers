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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Caslipandfall Com Agentic Access
  operation_count: 1
  slug: caslipandfall-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://caslipandfall.com
  baseurl_source: declared
  description: The Check Slip Fall Evidence API from JSM Injury Firm — 1 operation(s) for check slip fall evidence.
  name: JSM Injury Firm Check Slip Fall Evidence API
  slug: caslipandfall-com-check-slip-fall-evidence-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/caslipandfall-com/agentic-access/caslipandfall-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/caslipandfall-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/caslipandfall-com/rules/caslipandfall-com-rules.yml
  title: ''
  type: Spectral
  url: rules/caslipandfall-com-rules.yml
- group: design
  href: https://artifacts.apis.io/caslipandfall-com/conformance/caslipandfall-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caslipandfall-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caslipandfall-com/mcp/caslipandfall-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caslipandfall-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/caslipandfall-com/hosts/caslipandfall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caslipandfall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/caslipandfall-com/vendors/caslipandfall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caslipandfall-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://caslipandfall.com/docs
- group: auth
  href: https://artifacts.apis.io/caslipandfall-com/security/caslipandfall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caslipandfall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caslipandfall.com/
created: '2026-11-04'
description: JSM Injury Firm provides a free California Slip & Fall Evidence Checker, helping individuals understand what evidence to preserve after a slip and fall incident. The tool offers quick questions, legal guidance, and resources to assess potential claims, emphasizing privacy and on-screen results without email collection.
image: https://caslipandfall.com/og-share-v1.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at caslipandfall.com.
  name: JSM Injury Firm MCP Server
  slug: caslipandfall-com-mcp-yml
modified: '2026-11-04'
name: JSM Injury Firm
nav: Providers
network: true
overview: 'JSM Injury Firm publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Check Slip Fall Evidence API. Tagged areas include Law, Personal Injury, EvidenceChecker, California, and SlipAndFall.


  The JSM Injury Firm catalog on APIs.io includes 1 Spectral governance ruleset.


  JSM Injury Firm''s developer surface includes API reference and 8 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: JSM Injury Firm API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: caslipandfall-com-rules
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 44.7
    developer_ergonomics: 3.6
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caslipandfall Com Domain Security
  slug: caslipandfall-com-domain-security
  summary_line: TLSv1.3
slug: caslipandfall-com
tags:
- Law
- Personal Injury
- EvidenceChecker
- California
- SlipAndFall
website: https://caslipandfall.com/
---
