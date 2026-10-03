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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Streamable HTTP MCP server providing search_gaps, get_top_gaps, and validate_idea operations.
  name: DDMarketer MCP
  slug: ddmarketer-mcp
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/plans/ddmarketer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ddmarketer-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/llms/ddmarketer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ddmarketer-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/mcp/ddmarketer-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ddmarketer-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/mcp/ddmarketer-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ddmarketer-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/hosts/ddmarketer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ddmarketer-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/vendors/ddmarketer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ddmarketer-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ddmarketer/refs/heads/main/security/ddmarketer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ddmarketer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ddmarketer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ddmarketer.com/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://www.ddmarketer.com/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ddmarketer.com/validate
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ddmarketer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ddmarketer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ddmarketer.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.ddmarketer.com/auth/signup?redirect=%2F
- group: start
  title: ''
  type: Login
  url: https://www.ddmarketer.com/auth/login
created: '2026-09-28'
description: DDMarketer provides a data-driven platform that surfaces validated SaaS opportunities derived from real customer complaints and market gaps. Users can explore weekly updated opportunity lists, access detailed gap analyses, and leverage the MCP server to query validated ideas programmatically. The service offers free tools for idea validation, a paid plan for deeper insights, and integrates with AI coding assistants to streamline product development based on proven demand.
image: https://www.ddmarketer.com/opengraph-image?f9406f769821b2fc
layout: provider
mcp_servers:
- description: ''
  name: DDMarketer MCP Server
  slug: ddmarketer-mcp-server
modified: '2026-09-28'
name: DDMarketer
nav: Providers
network: true
overview: 'DDMarketer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Market Research, OpportunityValidation, and AI Integration.


  DDMarketer''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, and 11 more developer resources.'
plans:
- name: Ddmarketer Plans Pricing
  plan_count: 2
  slug: ddmarketer-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ddmarketer Domain Security
  slug: ddmarketer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ddmarketer
tags:
- Company
- Software-as-a-Service
- Market Research
- OpportunityValidation
- AI Integration
website: https://www.ddmarketer.com/
---
