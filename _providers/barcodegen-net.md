---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Barcode generation API referenced at /api (no public spec found).
  name: Barcode Generator API
  slug: barcode-generator-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/barcodegen-net/plans/barcodegen-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barcodegen-net-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.barcodegen.net/privacy-policy
- group: agent
  href: https://artifacts.apis.io/barcodegen-net/llms/barcodegen-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barcodegen-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/barcodegen-net/mcp/barcodegen-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/barcodegen-net-mcp.yml
- group: auth
  href: https://artifacts.apis.io/barcodegen-net/well-known/barcodegen-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barcodegen-net-security.txt
- group: auth
  href: https://artifacts.apis.io/barcodegen-net/well-known/barcodegen-net-barcodegen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/barcodegen-net-barcodegen-security.txt
- group: agent
  href: https://artifacts.apis.io/barcodegen-net/well-known/barcodegen-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/barcodegen-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/barcodegen-net/hosts/barcodegen-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barcodegen-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/barcodegen-net/vendors/barcodegen-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/barcodegen-net-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.barcodegen.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.barcodegen.net/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.barcodegen.net/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/barcodegenerator
- group: company
  title: ''
  type: Blog
  url: https://www.barcodegen.net/blog
- group: auth
  href: https://artifacts.apis.io/barcodegen-net/security/barcodegen-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/barcodegen-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/barcodegen-net/security/barcodegen-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barcodegen-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barcodegen.net/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec is publicly available despite an API reference page.
  evidence:
  - status: 404
    url: https://www.barcodegen.net/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Generate EAN-13, UPC-A, Code 128, QR Code and 20+ barcode formats online for free. Create single or bulk barcodes with no signup required. The service offers a simple web interface and API for developers to integrate barcode generation into applications without registration.
image: https://www.barcodegen.net/og-image.webp
layout: provider
mcp_servers:
- description: Remote MCP server at www.barcodegen.net.
  name: Free Barcode Generator Online MCP Server
  slug: barcodegen-net-mcp-yml
modified: '2026-11-02'
name: Free Barcode Generator Online
nav: Providers
network: true
overview: 'Free Barcode Generator Online is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Barcodes, Generator, Free, and Online.


  Free Barcode Generator Online''s developer surface includes pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Barcodegen Net Plans Pricing
  plan_count: 3
  slug: barcodegen-net-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.3
    operational_transparency: 7.9
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barcodegen Net Domain Security
  slug: barcodegen-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Barcodegen Net Vulnerability Disclosure
  slug: barcodegen-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: barcodegen-net
tags:
- Barcodes
- Generator
- Free
- Online
website: https://barcodegen.net/
---
