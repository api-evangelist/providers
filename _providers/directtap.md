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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/directtap/refs/heads/main/llms/directtap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/directtap-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/directtap/refs/heads/main/mcp/directtap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/directtap-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/directtap/refs/heads/main/hosts/directtap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directtap-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/directtap/refs/heads/main/vendors/directtap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/directtap-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/directtap/refs/heads/main/security/directtap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directtap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://directtap.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://directtap.ai/for-restaurants
- group: commercial
  title: ''
  type: Pricing
  url: https://directtap.ai/for-restaurants#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://directtap.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://directtap.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://directtap.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://directtap.ai/register
coverage:
  checked: '2026-10-16'
  detail: The DirectTap website serves only a JavaScript shell and no machine‑readable API specification was found.
  evidence:
  - status: 200
    url: https://directtap.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: DirectTap is a zero‑commission restaurant ordering platform that enables independent restaurants to accept online orders directly from customers, keeping 100% of the sale. Founded in 2024 by Tahir Hussain and Tushar Kale under Unoecom Inc, DirectTap provides each restaurant with its own branded ordering page, customer relationship tools, and a marketplace‑free experience. The service aims to eliminate the 20‑30% fees charged by third‑party delivery apps, helping local eateries retain revenue and build direct customer connections. The platform is SaaS‑based, offering registration, menu management, and order processing without hidden fees.
image: https://directtap.ai/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at directtap.ai.
  name: DirectTap MCP Server
  slug: directtap-mcp-yml
modified: '2026-10-16'
name: DirectTap
nav: Providers
network: true
overview: 'DirectTap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Software-as-a-Service, Marketplace, Zero-Commission, and Ordering.


  DirectTap''s developer surface includes documentation, pricing, support, signup flow, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Directtap Domain Security
  slug: directtap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: directtap
tags:
- Restaurant
- Software-as-a-Service
- Marketplace
- Zero-Commission
- Ordering
website: https://directtap.ai/
---
