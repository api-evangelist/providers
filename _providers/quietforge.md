---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: Converts Word, Excel, PowerPoint and OpenDocument files with LibreOffice (PDF is an output format, not an input; files capped at 15 MB), extracts per-page text and metadata from digital PDFs (no OCR),
  name: Quietforge Document Conversion API
  slug: document-conversion-api
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: 'A searchable, health-probed index of live x402 pay-per-call endpoints re-crawled from the Coinbase CDP and PayAI bazaars, with per-endpoint probe history and settlement-verified demand read from USDC '
  name: Quietforge x402 Service Index API
  slug: x402-service-index-api
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: Generates sudoku puzzles with a proven-unique solution and a technique grade, and connected freeform crosswords from 8-30 caller-supplied clue/answer pairs with a verifier. Deterministic per seed; ret
  name: Quietforge Puzzle Generation API
  slug: puzzle-generation-api
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: Typesets a prose manuscript into a print-ready book interior (chapter detection, mirrored margins, running heads, front matter and contents at 5x8, 5.25x8, 5.5x8.5, 6x9 or A5) delivered as a PDF, an e
  name: Quietforge Book Typesetting API
  slug: book-typesetting-api
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: 'Lays out a descendant, ancestor or hourglass family tree chart from people+families JSON or a GEDCOM file (up to 400 people, 10 generations), returned as verified layout JSON or as print-ready poster '
  name: Quietforge Family Tree Chart API
  slug: family-chart-api
- baseURL: https://qf-api.quietforge-studio.workers.dev
  baseurl_source: declared
  description: Audits a CSV or JSON-array dataset (up to 5 MB, 50,000 rows, 200 columns) for duplicate rows, missing values, inferred types, class imbalance, IQR outliers and PII-pattern counts, combined into a heur
  name: Quietforge Dataset Audit API
  slug: dataset-audit-api
artifact_total: 10
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/hosts/quietforge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quietforge-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/vendors/quietforge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quietforge-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/security/quietforge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quietforge-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/mcp/quietforge-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/quietforge-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/authentication/quietforge-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quietforge-authentication.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/plans/quietforge-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quietforge-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/llms/quietforge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quietforge-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quietforge/refs/heads/main/well-known/quietforge-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quietforge-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://qf-api.quietforge-studio.workers.dev/.well-known/api-catalog
- group: other
  title: ''
  type: APIsJSON
  url: https://qf-api.quietforge-studio.workers.dev/apis.json
- group: agent
  title: ''
  type: AgenticAccess
  url: https://qf-api.quietforge-studio.workers.dev/.well-known/x402
- group: company
  title: ''
  type: Website
  url: https://quietforge-studio.pages.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://quietforge-studio.pages.dev/docs-api/
- group: docs
  title: ''
  type: Documentation
  url: https://qf-api.quietforge-studio.workers.dev/docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://qf-api.quietforge-studio.workers.dev/openapi.json
- group: build
  title: ''
  type: Examples
  url: https://qf-api.quietforge-studio.workers.dev/v1/samples
- group: operate
  title: ''
  type: Contact
  url: mailto:quietforgestudio@agentmail.to
created: '2026-09-27'
description: 'Quietforge Studio is a self-described AI-run studio (disclosed by the provider in its apis.json, OpenAPI, x402 manifest and MCP server) that operates pay-per-call HTTP APIs on a Cloudflare Worker: office-document conversion, PDF text extraction, URL/HTML rendering, a health-probed index of x402 endpoints, sudoku and crossword generation, book-interior typesetting, family tree chart layout and dataset quality audits. Authorization is a per-call x402 USDC payment on Base with no signup, account or API key; every paid route has a free static sample response, and a free read-only MCP server exposes seven tools.'
layout: provider
mcp_servers:
- description: 'One first-party remote MCP server (streamable HTTP) on the API host. initialize and tools/list answered anonymously on 2026-10-03: 7 tools, which the server instructions describe as free and read-only'
  name: Quietforge Studio MCP Server
  slug: quietforge-x402-tools
modified: '2026-10-03'
name: Quietforge Studio
nav: Providers
network: true
overview: 'Quietforge Studio publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Quietforge Document Conversion API, Quietforge x402 Service Index API, Quietforge Puzzle Generation API, and 3 more. Tagged areas include Artificial Intelligence, Document Processing, x402, Micropayments, and MCP.


  Quietforge Studio''s developer surface includes authentication, documentation, code examples, and 14 more developer resources.'
plans:
- name: Quietforge Plans Pricing
  plan_count: 16
  slug: quietforge-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 49.4
    developer_ergonomics: 31.0
    discoverability: 81.7
    operational_transparency: 0.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Quietforge Authentication
  slug: quietforge-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Quietforge Domain Security
  slug: quietforge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quietforge
tags:
- Artificial Intelligence
- Document Processing
- x402
- Micropayments
- MCP
- pay-per-call
- Cloudflare Workers
- Software-as-a-Service
- Business Automation
website: https://quietforge-studio.pages.dev/
---
