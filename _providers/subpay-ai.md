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
api_count: 1
apis:
- description: Document Reading API for Developers – reads construction pay applications and change orders from PDF to JSON.
  name: Subpay Document Reading API
  slug: subpay-document-reading-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/subpay-ai/conformance/subpay-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/subpay-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/subpay-ai/llms/subpay-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/subpay-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/subpay-ai/mcp/subpay-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/subpay-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/subpay-ai/hosts/subpay-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/subpay-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/subpay-ai/vendors/subpay-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/subpay-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://subpay.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://subpay.ai/privacy
- group: start
  title: ''
  type: Login
  url: https://subpay.ai/login
- group: docs
  title: ''
  type: APIReference
  url: https://subpay.ai/developers
- group: auth
  href: https://artifacts.apis.io/subpay-ai/security/subpay-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/subpay-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://subpay.ai/
created: '2026-10-29'
description: Subpay AI is a fintech company focused on providing AI-driven payment solutions for businesses and consumers. Leveraging advanced machine learning algorithms, Subpay AI streamlines transaction processing, fraud detection, and financial analytics. The platform offers APIs for payment initiation, settlement, and reporting, enabling seamless integration with e‑commerce, SaaS, and mobile applications. Subpay AI emphasizes security, compliance, and scalability, aiming to reduce operational costs and improve user experience across the payment ecosystem.
image: https://subpay.ai/opengraph-image.png?opengraph-image.026dwc32f98zk.png
layout: provider
mcp_servers:
- description: Remote MCP server at subpay.ai.
  name: subpay-ai MCP Server
  slug: subpay-ai-mcp-yml
modified: '2026-10-29'
name: subpay-ai
nav: Providers
network: true
overview: 'subpay-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, AI, Machine-Learning, and API.


  subpay-ai''s developer surface includes API reference and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Subpay Ai Domain Security
  slug: subpay-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: subpay-ai
tags:
- Fintech
- Payments
- AI
- Machine-Learning
- API
website: https://subpay.ai/
---
