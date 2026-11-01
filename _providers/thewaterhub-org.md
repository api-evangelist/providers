---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'The Water Hub: the median advertised water softener system price, read from verified brand product pages (August 2026), served as an agent-callable dataset with its source and licence on every answer.'
  name: The Water Hub API
  slug: thewaterhub-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/thewaterhub-org/vocabulary/thewaterhub-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thewaterhub-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thewaterhub-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://thewaterhub.org/terms
- group: auth
  href: https://artifacts.apis.io/thewaterhub-org/authentication/thewaterhub-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thewaterhub-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/thewaterhub-org/conformance/thewaterhub-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thewaterhub-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thewaterhub-org/llms/thewaterhub-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thewaterhub-org-llms.txt
- group: build
  href: https://artifacts.apis.io/thewaterhub-org/mcp/thewaterhub-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thewaterhub-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/thewaterhub-org/mcp/thewaterhub-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thewaterhub-org-mcp.yml
- group: auth
  href: https://artifacts.apis.io/thewaterhub-org/well-known/thewaterhub-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thewaterhub-org-security.txt
- group: agent
  href: https://artifacts.apis.io/thewaterhub-org/well-known/thewaterhub-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thewaterhub-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/thewaterhub-org/hosts/thewaterhub-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thewaterhub-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/thewaterhub-org/vendors/thewaterhub-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thewaterhub-org-vendors.yml
- group: auth
  href: https://artifacts.apis.io/thewaterhub-org/security/thewaterhub-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/thewaterhub-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/thewaterhub-org/security/thewaterhub-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thewaterhub-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thewaterhub.org/
- group: docs
  title: ''
  type: APIReference
  url: https://thewaterhub.org/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thewaterhub.org/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thewaterhub.org/privacy/
created: '2026-10-30'
description: The Water Hub provides a dataset of median advertised residential water softener system prices, sourced from verified brand product pages as of August 2026. The site offers an MCP server exposing tools to query dataset columns, search, retrieve rows, compare, and compute statistics. All figures are cited with source URLs and licensed under the site's terms.
image: https://thewaterhub.org/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at thewaterhub.org.
  name: thewaterhub-org MCP Server
  slug: thewaterhub-org-mcp-yml
modified: '2026-10-30'
name: thewaterhub-org
nav: Providers
network: true
overview: 'thewaterhub-org publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: The Water Hub API. Tagged areas include Company, Water, Pricing, Dataset, and API.


  thewaterhub-org''s developer surface includes authentication, API reference, and 16 more developer resources.'
plans:
- name: Thewaterhub Org Plans Pricing
  plan_count: 0
  slug: thewaterhub-org-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Thewaterhub Org Rate Limits
  slug: thewaterhub-org-rate-limits
scopes:
- name: Thewaterhub Org Scopes
  scope_count: 0
  slug: thewaterhub-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 38.3
    catalog_earned_first_party: 0.0
    catalog_gap: 76.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 8.3
    contract_quality: 24.0
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Thewaterhub Org Authentication
  slug: thewaterhub-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thewaterhub Org Domain Security
  slug: thewaterhub-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Thewaterhub Org Vulnerability Disclosure
  slug: thewaterhub-org-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: dataset
  slug: thewaterhub-org-dataset
- name: enquiry
  slug: thewaterhub-org-enquiry
slug: thewaterhub-org
tags:
- Company
- Water
- Pricing
- Dataset
- API
website: https://thewaterhub.org/
---
