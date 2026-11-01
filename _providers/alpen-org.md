---
agent_readiness:
  band: agent-aware
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API providing access to Alpen Labs data ingestion, analytics, and reporting services.
  name: Alpen API
  slug: alpen-api
- baseURL: https://alpen.testnet.alpen.org
  baseurl_source: declared
  description: 'Alpen Labs API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Alpen Labs API
  slug: alpen-org-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/alpen-org/rules/alpen-org-rules.yml
  title: ''
  type: Spectral
  url: rules/alpen-org-rules.yml
- group: design
  href: https://artifacts.apis.io/alpen-org/json-ld/alpen-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alpen-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/alpen-org/vocabulary/alpen-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alpen-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/alpen-org/data-model/alpen-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alpen-org-data-model.yml
- group: build
  href: https://artifacts.apis.io/alpen-org/cli/alpen-org-cli.yml
  title: ''
  type: CLI
  url: cli/alpen-org-cli.yml
- group: auth
  href: https://artifacts.apis.io/alpen-org/security/alpen-org-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/alpen-org-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/alpen-org/conformance/alpen-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alpen-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alpen-org/llms/alpen-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpen-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/alpen-org/mcp/alpen-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpen-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/alpen-org/well-known/alpen-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alpen-org-security.txt
- group: auth
  href: https://artifacts.apis.io/alpen-org/well-known/alpen-org-alpen-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alpen-org-alpen-security.txt
- group: agent
  href: https://artifacts.apis.io/alpen-org/well-known/alpen-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpen-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/alpen-org/hosts/alpen-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpen-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/alpen-org/vendors/alpen-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpen-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alpen-org/security/alpen-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alpen-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alpen-org/security/alpen-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpen-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alpen.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpen.org
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alpen.org/welcome/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.alpen.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alpenlabs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alpen.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alpen.org/privacy-policy
created: '2026-10-29'
description: Alpen Labs is a technology-driven company focused on providing advanced data analytics and AI-powered solutions for the financial services industry. Founded with the backing of Ribbit Capital, Alpen Labs leverages cutting‑edge machine learning models to help banks and fintech firms unlock insights from large datasets, improve risk assessment, and automate decision‑making processes. The company offers a suite of APIs that enable secure data ingestion, real‑time analytics, and customizable reporting, all hosted on a scalable cloud infrastructure. Alpen Labs is committed to innovation, security, and compliance, delivering enterprise‑grade solutions that empower clients to stay ahead in a rapidly evolving market.
image: https://www.alpen.org/social-card.png
json_schemas:
- name: GetBuildAlpenAppsRpcEndpointsMdResponse
  property_count: 1
  slug: alpen-org-get-build-alpen-apps-rpc-endpoints-md-response
- name: PostRequest
  property_count: 4
  slug: alpen-org-post-request
jsonld:
- class_count: 2
  name: Alpen Org Context
  property_count: 4
  slug: alpen-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.alpen.org.
  name: Alpen Labs MCP Server
  slug: alpen-org-mcp-yml
modified: '2026-10-29'
name: Alpen Labs
nav: Providers
network: true
overview: 'Alpen Labs is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The Alpen Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Alpen Labs'' developer surface includes CLI, documentation, getting-started guide, engineering blog, and 19 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Alpen Labs API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: alpen-org-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 35.6
    contract_quality: 20.2
    developer_ergonomics: 31.0
    discoverability: 48.3
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alpen Org Domain Security
  slug: alpen-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Alpen Org Vulnerability Disclosure
  slug: alpen-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alpen-org
tags:
- Company
website: https://www.alpen.org/
---
