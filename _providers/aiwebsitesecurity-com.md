---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
api_count: 1
apis:
- description: Provides security analysis tools via MCP endpoint.
  name: AI Website Security API
  slug: ai-website-security-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/aiwebsitesecurity-com/plans/aiwebsitesecurity-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiwebsitesecurity-com-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://aiwebsitesecurity.com/confidentialite
- group: agent
  href: https://artifacts.apis.io/aiwebsitesecurity-com/llms/aiwebsitesecurity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiwebsitesecurity-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aiwebsitesecurity-com/mcp/aiwebsitesecurity-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiwebsitesecurity-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aiwebsitesecurity-com/well-known/aiwebsitesecurity-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aiwebsitesecurity-com-security.txt
- group: agent
  href: https://artifacts.apis.io/aiwebsitesecurity-com/well-known/aiwebsitesecurity-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiwebsitesecurity-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiwebsitesecurity-com/hosts/aiwebsitesecurity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiwebsitesecurity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aiwebsitesecurity-com/vendors/aiwebsitesecurity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aiwebsitesecurity-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aiwebsitesecurity-com/security/aiwebsitesecurity-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aiwebsitesecurity-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aiwebsitesecurity-com/security/aiwebsitesecurity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiwebsitesecurity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiwebsitesecurity.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://aiwebsitesecurity.com/tarifs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiwebsitesecurity.com/cgv
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiwebsitesecurity.com/mentions-legales
created: '2026-11-01'
description: AI Website Security provides AI‑driven analysis and protection for websites, automatically verifying the provenance of every file on a site. It monitors changes, detects unauthorized modifications, offers real‑time alerts, and can restore sites to a verified state without installing software. Services include file‑justification, continuous monitoring, breach detection, and automated remediation, available in French, English and German.
image: https://aiwebsitesecurity.com/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at scan.aiwebsitesecurity.com.
  name: AI Website Security MCP Server
  slug: aiwebsitesecurity-com-mcp-yml
modified: '2026-11-01'
name: AI Website Security
nav: Providers
network: true
overview: 'AI Website Security is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Artificial Intelligence, Websites, Monitoring, and Compliance.


  AI Website Security''s developer surface includes pricing and 13 more developer resources.'
plans:
- name: Aiwebsitesecurity Com Plans Pricing
  plan_count: 5
  slug: aiwebsitesecurity-com-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 21.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aiwebsitesecurity Com Domain Security
  slug: aiwebsitesecurity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aiwebsitesecurity Com Vulnerability Disclosure
  slug: aiwebsitesecurity-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: aiwebsitesecurity-com
tags:
- Security
- Artificial Intelligence
- Websites
- Monitoring
- Compliance
website: https://aiwebsitesecurity.com/
---
