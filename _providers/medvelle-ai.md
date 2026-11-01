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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/medvelle-ai/mcp/medvelle-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/medvelle-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/medvelle-ai/hosts/medvelle-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/medvelle-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/medvelle-ai/security/medvelle-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/medvelle-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.medvelle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.medvelle.com/insights
- group: start
  title: ''
  type: GettingStarted
  url: https://www.medvelle.com/why-medvelle
- group: operate
  title: ''
  type: Support
  url: https://www.medvelle.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.medvelle.com/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.medvelle.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.medvelle.com/privacy-policy
created: '2026-10-21'
description: Medvelle AI provides AI‑powered inventory management and procurement solutions for aesthetic and spa clinics. Their platform automates ordering, compares suppliers, forecasts demand, and offers finance, analytics, and supplier management tools, helping clinics save time and reduce costs while focusing on patient care. The company emphasizes a proprietary procurement process and AI-driven insights to maximize profit for healthcare providers.
image: https://framerusercontent.com/images/9L6S49J3x7kS2C4LK0tHrPFxIGU.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at www.medvelle.com.
  name: Medvelle AI MCP Server
  slug: medvelle-ai-mcp-yml
modified: '2026-10-21'
name: Medvelle AI
nav: Providers
network: true
overview: 'Medvelle AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Inventory Management, Aesthetic Clinics, and Healthcare.


  Medvelle AI''s developer surface includes documentation, getting-started guide, support, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Medvelle Ai Domain Security
  slug: medvelle-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medvelle-ai
tags:
- Company
- AI
- Inventory Management
- Aesthetic Clinics
- Healthcare
website: https://www.medvelle.com/
---
