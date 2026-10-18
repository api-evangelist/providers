---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Provides access to the company's data via a GraphQL endpoint, though ownership could not be verified.
  name: Laws of Motion API
  slug: laws-of-motion-api
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/llms/laws-of-motion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/laws-of-motion-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/mcp/laws-of-motion-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/laws-of-motion-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/well-known/laws-of-motion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/laws-of-motion-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/hosts/laws-of-motion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/laws-of-motion-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/vendors/laws-of-motion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/laws-of-motion-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/laws-of-motion/refs/heads/main/security/laws-of-motion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/laws-of-motion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lawsofmotion.com/
- group: company
  title: ''
  type: AboutUs
  url: https://lawsofmotion.com/pages/about-us
- group: operate
  title: ''
  type: FAQ
  url: https://lawsofmotion.com/pages/faq
- group: operate
  title: ''
  type: Contact
  url: https://lawsofmotion.com/pages/contact
- group: commercial
  title: ''
  type: Legal
  url: https://lawsofmotion.com/pages/legal
- group: company
  title: ''
  type: Press
  url: https://lawsofmotion.com/pages/press
created: '2026-10-12'
description: Laws of Motion is a fashion technology company offering AI‑sized clothing. Their online store provides a range of apparel including pants, shorts, dresses, jumpsuits, blazers, blouses, matching sets, bridal gowns, and robes. The brand emphasizes perfect‑fit solutions through a quiz and AI algorithms, aiming to reduce returns and improve customer satisfaction. Founded with backing from leadout‑capital, the company integrates modern e‑commerce features such as gift cards, a press page, and a comprehensive FAQ.
image: http://lawsofmotion.com/cdn/shop/files/helmet3homepage.jpg?v=13450595073797374221
layout: provider
mcp_servers:
- description: Remote MCP server at lawsofmotion.com.
  name: Laws of Motion MCP Server
  slug: laws-of-motion-mcp-yml
modified: '2026-10-12'
name: Laws of Motion
nav: Providers
network: true
overview: 'Laws of Motion is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Artificial Intelligence, E-Commerce, and Clothing.


  Laws of Motion''s developer surface includes FAQ, legal docs, and 10 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Laws Of Motion Domain Security
  slug: laws-of-motion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laws-of-motion
tags:
- Company
- Fashion
- Artificial Intelligence
- E-Commerce
- Clothing
website: https://lawsofmotion.com/
---
