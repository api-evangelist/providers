---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/docugrip-com/plans/docugrip-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docugrip-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/docugrip-com/changelog/docugrip-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docugrip-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/docugrip-com/conformance/docugrip-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docugrip-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/docugrip-com/llms/docugrip-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docugrip-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/docugrip-com/mcp/docugrip-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docugrip-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/docugrip-com/well-known/docugrip-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docugrip-com-security.txt
- group: agent
  href: https://artifacts.apis.io/docugrip-com/well-known/docugrip-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docugrip-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docugrip-com/hosts/docugrip-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docugrip-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docugrip-com/vendors/docugrip-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docugrip-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docugrip.com/terms
- group: operate
  title: ''
  type: Support
  url: https://docugrip.com/help
- group: operate
  title: ''
  type: StatusPage
  url: https://docugrip.com/status
- group: auth
  title: ''
  type: Security
  url: https://docugrip.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docugrip.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://docugrip.com/pricing
- group: start
  title: ''
  type: Login
  url: https://docugrip.com/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://docugrip.com/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docugrip.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://docugrip.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocuGrip
- group: auth
  href: https://artifacts.apis.io/docugrip-com/security/docugrip-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docugrip-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/docugrip-com/security/docugrip-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docugrip-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docugrip.com/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://docugrip.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DocuGrip provides an online PDF editor, converter, and e‑signature tool that lets users merge, split, compress, convert, edit and sign PDFs instantly. The service is free to start, guarantees files are never uploaded to a server, and offers a suite of PDF utilities in a single web‑based platform. It targets both casual users and professionals needing quick, secure PDF manipulation without installing software.
image: https://docugrip.com/icons/opengraph-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at docugrip.com.
  name: DocuGrip MCP Server
  slug: docugrip-com-mcp-yml
modified: '2026-11-05'
name: DocuGrip
nav: Providers
network: true
overview: 'DocuGrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include PDF editor, PDF converter, E-Signature, Document Security, and OCR.


  DocuGrip''s developer surface includes changelog, support, pricing, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Docugrip Com Plans Pricing
  plan_count: 8
  slug: docugrip-com-plans-pricing
random_paper: 1
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 48.3
    operational_transparency: 47.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docugrip Com Domain Security
  slug: docugrip-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Docugrip Com Vulnerability Disclosure
  slug: docugrip-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: docugrip-com
tags:
- PDF editor
- PDF converter
- E-Signature
- Document Security
- OCR
- PDF compression
- PDF redaction
website: https://docugrip.com/
---
