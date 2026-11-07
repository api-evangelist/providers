---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Snapwonders Com Agentic Access
  operation_count: 33
  slug: snapwonders-com-agentic-access
  summary_line: 33 operations · 13 acting
api_count: 1
apis:
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: '**Analyse images and videos for forensic integrity.** Detects faces, text regions, watermarks, and manipulation artefacts. Returns a per-file forensic grade (A–F) with detailed counts. All endpoints r'
  name: snapwonders-com Analyse API
  slug: snapwonders-com-analyse-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: '**Convert images, videos, and PDFs to different formats.** Supports format conversion, quality control, image resize, video resolution cap, metadata stripping, and PDF-to-image rendering. All endpoint'
  name: snapwonders-com Convert API
  slug: snapwonders-com-convert-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: '**Conceal content inside a cover image.** The output is a stego image visually identical to the original cover that carries an encrypted hidden payload. All endpoints require `X-Api-Key`. **Workflow —'
  name: snapwonders-com Hide API
  slug: snapwonders-com-hide-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: Model Context Protocol endpoint for AI agent integration. 19 tools across steganography (`vaultify_*`), forensic analysis (`snapwonders_analyse_*`), and media conversion (`snapwonders_convert_*`). `X-
  name: snapwonders-com MCP API
  slug: snapwonders-com-mcp-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: '**Start here.** One request per file: `POST /api/upload` with the file as the request body and four plain headers (`X-Api-Key`, `X-Upload-Uid`, `X-Filename`, `Content-Type`). No protocol to implement,'
  name: snapwonders-com Media Upload - Direct API
  slug: snapwonders-com-media-upload-direct-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: 'The [TUS](https://tus.io) resumable protocol at `/api/tus` — several requests per file: `POST` to create the upload, `PATCH` to send chunks, `HEAD` to query the offset and resume. More work to impleme'
  name: snapwonders-com Media Upload - TUS Resumable API
  slug: snapwonders-com-media-upload-tus-resumable-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: '**Extract hidden content from a stego image.** Requires the same password used when the content was originally hidden. All endpoints require `X-Api-Key`. **Workflow — 6 steps:** **Step 1 — Create a se'
  name: snapwonders-com Reveal API
  slug: snapwonders-com-reveal-api
- baseURL: https://snapwonders.com
  baseurl_source: declared
  description: Service health endpoint. No authentication required.
  name: snapwonders-com Status API
  slug: snapwonders-com-status-api
artifact_total: 19
common:
- group: build
  href: https://artifacts.apis.io/snapwonders-com/integrations/snapwonders-com-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/snapwonders-com-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/snapwonders-com/agentic-access/snapwonders-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snapwonders-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/snapwonders-com/rules/snapwonders-com-rules.yml
  title: ''
  type: Spectral
  url: rules/snapwonders-com-rules.yml
- group: design
  href: https://artifacts.apis.io/snapwonders-com/vocabulary/snapwonders-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snapwonders-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/snapwonders-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://snapwonders.com/vulnerability-disclosure-policy
- group: auth
  href: https://artifacts.apis.io/snapwonders-com/authentication/snapwonders-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snapwonders-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/snapwonders-com/errors/snapwonders-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snapwonders-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snapwonders-com/conformance/snapwonders-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snapwonders-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/snapwonders-com/llms/snapwonders-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snapwonders-com-llms.txt
- group: build
  href: https://artifacts.apis.io/snapwonders-com/mcp/snapwonders-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snapwonders-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/snapwonders-com/mcp/snapwonders-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snapwonders-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/snapwonders-com/well-known/snapwonders-com-vaultify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snapwonders-com-vaultify-security.txt
- group: auth
  href: https://artifacts.apis.io/snapwonders-com/well-known/snapwonders-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snapwonders-com-security.txt
- group: agent
  href: https://artifacts.apis.io/snapwonders-com/well-known/snapwonders-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snapwonders-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/snapwonders-com/hosts/snapwonders-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snapwonders-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/snapwonders-com/vendors/snapwonders-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snapwonders-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/snapwonders-com/packages/snapwonders-com-packages.yml
  title: ''
  type: SDKs
  url: packages/snapwonders-com-packages.yml
- group: build
  href: https://artifacts.apis.io/snapwonders-com/packages/snapwonders-com-packages.yml
  title: ''
  type: Packages
  url: packages/snapwonders-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snapwonders.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://snapwonders.com/news
- group: auth
  href: https://artifacts.apis.io/snapwonders-com/security/snapwonders-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snapwonders-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snapwonders-com/security/snapwonders-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snapwonders-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://snapwonders.com/
- group: docs
  title: ''
  type: Documentation
  url: https://snapwonders.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://snapwonders.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://snapwonders.com/developers#getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://snapwonders.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://snapwonders.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snapwonders.com/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://snapwonders.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snapWONDERS
created: '2026-10-30'
description: snapWONDERS provides free photo and video forensics tools that expose GPS data, device fingerprints, and metadata. It also offers Vaultify, a steganography service that hides any file inside a photo or video using military‑grade encryption. The platform operates over clearnet, Tor, and I2P, offering REST and MCP APIs for forensic analysis, steganography, and media conversion, with open‑source SDKs for Python, JavaScript, PHP, and Go.
image: https://snapwonders.com/images/og/og-snapwonders.png
layout: provider
mcp_servers:
- description: Remote MCP server at snapwonders.com.
  name: snapwonders-com MCP Server
  slug: snapwonders-com-mcp-yml
modified: '2026-10-30'
name: snapwonders-com
nav: Providers
network: true
overview: 'snapwonders-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analyse API, Convert API, Hide API, and 5 more. Tagged areas include Forensics, Steganography, MediaConversion, Privacy, and Open Source.


  The snapwonders-com catalog on APIs.io includes 1 Spectral governance ruleset.


  snapwonders-com''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Snapwonders Com Plans Pricing
  plan_count: 0
  slug: snapwonders-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: snapwonders-com API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: snapwonders-com-rules
scopes:
- name: Snapwonders Com Scopes
  scope_count: 0
  slug: snapwonders-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 48.2
    developer_ergonomics: 44.5
    discoverability: 75.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/snapwonders-com/snapwonders-com-2026-11-03T143410.png
security:
- kind: authentication
  name: Snapwonders Com Authentication
  slug: snapwonders-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Snapwonders Com Domain Security
  slug: snapwonders-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Snapwonders Com Vulnerability Disclosure
  slug: snapwonders-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: analyse
  slug: snapwonders-com-analyse
- name: convert
  slug: snapwonders-com-convert
- name: vaultify
  slug: snapwonders-com-vaultify
slug: snapwonders-com
tags:
- Forensics
- Steganography
- MediaConversion
- Privacy
- Open Source
website: https://snapwonders.com/
---
