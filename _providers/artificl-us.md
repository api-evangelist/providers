---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides compliance tracking services via MCP endpoints such as CredCycle, DEAWatch, DriverFile, etc.
  name: Artificl API
  slug: artificl-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/artificl-us/plans/artificl-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/artificl-us-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://artificl.us/security
- group: agent
  href: https://artifacts.apis.io/artificl-us/llms/artificl-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artificl-us-llms.txt
- group: agent
  href: https://artifacts.apis.io/artificl-us/mcp/artificl-us-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/artificl-us-mcp.yml
- group: other
  href: https://artifacts.apis.io/artificl-us/hosts/artificl-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artificl-us-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://artificl.us/security
- group: auth
  href: https://artifacts.apis.io/artificl-us/security/artificl-us-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/artificl-us-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/artificl-us/security/artificl-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artificl-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://artificl.us/
- group: commercial
  title: ''
  type: Pricing
  url: https://artificl.us/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://artificl.us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://artificl.us/privacy
- group: operate
  title: ''
  type: Support
  url: https://artificl.us/contact
coverage:
  checked: '2026-10-29'
  detail: Public documentation exists but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract is published.
  evidence:
  - status: 200
    url: https://artificl.us/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Artificl is a one-person Michigan company building focused compliance trackers that your own AI assistant can operate. It offers a suite of specialized apps such as VendorPing, SubProof, LiftLog, HoodDue, DriverFile, DEAWatch, and CredCycle, each tracking expiring documents, permits, certifications, and regulatory compliance for various trades. The platform provides single-job expiry and document trackers, read‑only by default, with every action logged, enabling AI‑driven automation of compliance workflows.
image: https://artificl.us/media/hero-mesh-backdrop.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at credcycle.artificl.us.
  name: artificl-us MCP Server
  slug: artificl-us-mcp-yml
modified: '2026-10-29'
name: artificl-us
nav: Providers
network: true
overview: 'artificl-us is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Compliance, AI, Document Tracking, and Small Business.


  artificl-us'' developer surface includes pricing, support, and 11 more developer resources.'
plans:
- name: Artificl Us Plans Pricing
  plan_count: 4
  slug: artificl-us-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Artificl Us Rate Limits
  slug: artificl-us-rate-limits
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 10.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Artificl Us Authentication
  slug: artificl-us-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Artificl Us Domain Security
  slug: artificl-us-domain-security
  summary_line: TLSv1.3
- kind: trust-center
  name: Artificl Us Trust Center
  slug: artificl-us-trust-center
  summary_line: SOC 2, HIPAA
slug: artificl-us
tags:
- Company
- Compliance
- AI
- Document Tracking
- Small Business
website: https://artificl.us/
---
