---
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 139
  human_in_the_loop: 2
  name: Identik Me Agentic Access
  operation_count: 208
  slug: identik-me-agentic-access
  summary_line: 208 operations · 139 acting · 2 human-in-the-loop
api_count: 4
apis:
- baseURL: https://electronica.identik.me
  baseurl_source: declared
  description: The Document API from identik-me — 19 operation(s) for document.
  name: identik-me Document API
  slug: identik-me-document-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Document Fields API from identik-me — 6 operation(s) for document fields.
  name: identik-me Document Fields API
  slug: identik-me-document-fields-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Document Recipients API from identik-me — 6 operation(s) for document recipients.
  name: identik-me Document Recipients API
  slug: identik-me-document-recipients-api
- baseURL: https://electronica.identik.me
  baseurl_source: declared
  description: The Documents API from identik-me — 9 operation(s) for documents.
  name: identik-me Documents API
  slug: identik-me-documents-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Embedding API from identik-me — 2 operation(s) for embedding.
  name: identik-me Embedding API
  slug: identik-me-embedding-api
- baseURL: https://electronica.identik.me
  baseurl_source: declared
  description: The Envelope API from identik-me — 12 operation(s) for envelope.
  name: identik-me Envelope API
  slug: identik-me-envelope-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Envelope Attachments API from identik-me — 4 operation(s) for envelope attachments.
  name: identik-me Envelope Attachments API
  slug: identik-me-envelope-attachments-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Envelope Fields API from identik-me — 4 operation(s) for envelope fields.
  name: identik-me Envelope Fields API
  slug: identik-me-envelope-fields-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Envelope Items API from identik-me — 4 operation(s) for envelope items.
  name: identik-me Envelope Items API
  slug: identik-me-envelope-items-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Envelope Recipients API from identik-me — 4 operation(s) for envelope recipients.
  name: identik-me Envelope Recipients API
  slug: identik-me-envelope-recipients-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Firma masiva API from identik-me — 6 operation(s) for firma masiva.
  name: identik-me Firma masiva API
  slug: identik-me-firma-masiva-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Folder API from identik-me — 4 operation(s) for folder.
  name: identik-me Folder API
  slug: identik-me-folder-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Representation API from identik-me — 22 operation(s) for representation.
  name: identik-me Representation API
  slug: identik-me-representation-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Template API from identik-me — 12 operation(s) for template.
  name: identik-me Template API
  slug: identik-me-template-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Template Fields API from identik-me — 6 operation(s) for template fields.
  name: identik-me Template Fields API
  slug: identik-me-template-fields-api
- baseURL: https://firma.identik.me/api/v2
  baseurl_source: declared
  description: The Template Recipients API from identik-me — 6 operation(s) for template recipients.
  name: identik-me Template Recipients API
  slug: identik-me-template-recipients-api
- baseURL: https://electronica.identik.me
  baseurl_source: declared
  description: The Templates API from identik-me — 4 operation(s) for templates.
  name: identik-me Templates API
  slug: identik-me-templates-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/identik-me/agentic-access/identik-me-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/identik-me-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/identik-me/rate-limits/identik-me-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/identik-me-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/identik-me/plans/identik-me-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/identik-me-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/identik-me/rules/identik-me-rules.yml
  title: ''
  type: Spectral
  url: rules/identik-me-rules.yml
- group: design
  href: https://artifacts.apis.io/identik-me/vocabulary/identik-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/identik-me-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/identik-me/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/identik-me/authentication/identik-me-authentication.yml
  title: ''
  type: Authentication
  url: authentication/identik-me-authentication.yml
- group: design
  href: https://artifacts.apis.io/identik-me/errors/identik-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/identik-me-problem-types.yml
- group: design
  href: https://artifacts.apis.io/identik-me/conformance/identik-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/identik-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/identik-me/llms/identik-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/identik-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/identik-me/mcp/identik-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/identik-me-mcp.yml
- group: auth
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/identik-me-www-security.txt
- group: auth
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-sandbox-firma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/identik-me-sandbox-firma-security.txt
- group: auth
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-sandbox-electronica-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/identik-me-sandbox-electronica-security.txt
- group: auth
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-firma-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/identik-me-firma-security.txt
- group: auth
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-electronica-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/identik-me-electronica-security.txt
- group: agent
  href: https://artifacts.apis.io/identik-me/well-known/identik-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/identik-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/identik-me/hosts/identik-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/identik-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/identik-me/vendors/identik-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/identik-me-vendors.yml
- group: build
  href: https://artifacts.apis.io/identik-me/packages/identik-me-packages.yml
  title: ''
  type: SDKs
  url: packages/identik-me-packages.yml
- group: build
  href: https://artifacts.apis.io/identik-me/packages/identik-me-packages.yml
  title: ''
  type: Packages
  url: packages/identik-me-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.identik.me/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://identik.me/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://firma.identik.me/api/docs
- group: auth
  href: https://artifacts.apis.io/identik-me/security/identik-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/identik-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://identik.me/
- group: company
  title: ''
  type: Blog
  url: https://identik.me/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/identik-me
- group: commercial
  title: ''
  type: Pricing
  url: https://identik.me/precios/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://identik.me/privacidad/
created: '2026-10-30'
description: identik-me provides digital signature and electronic document services, enabling individuals and businesses in Argentina to sign contracts, invoices, and official forms online. The platform offers online, electronic, remote, and electronic signature solutions, integrating with government and private systems. It aims to simplify legal compliance and streamline document workflows through a secure, cloud‑based interface.
image: https://identik.me/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at firma.identik.me.
  name: identik-me MCP Server
  slug: identik-me-mcp-yml
modified: '2026-10-30'
name: identik-me
nav: Providers
network: true
overview: 'identik-me publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Document API, Document Fields API, Document Recipients API, and 14 more. Tagged areas include Company, DigitalSignature, DocumentAutomation, Argentina, and API.


  The identik-me catalog on APIs.io includes 1 Spectral governance ruleset.


  identik-me''s developer surface includes authentication, API reference, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Identik Me Plans Pricing
  plan_count: 2
  slug: identik-me-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Identik Me Rate Limits
  slug: identik-me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: identik-me API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: identik-me-rules
scopes:
- name: Identik Me Scopes
  scope_count: 0
  slug: identik-me-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.8
    catalog_earned_first_party: 16.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 44.5
    discoverability: 70.0
    operational_transparency: 52.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Identik Me Authentication
  slug: identik-me-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Identik Me Domain Security
  slug: identik-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: envelope-attachment
  slug: identik-me-envelope-attachment
slug: identik-me
tags:
- Company
- DigitalSignature
- DocumentAutomation
- Argentina
- API
website: https://identik.me/
---
