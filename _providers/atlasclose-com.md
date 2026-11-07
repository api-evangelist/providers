---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/atlasclose-com/hosts/atlasclose-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlasclose-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/atlasclose-com/vendors/atlasclose-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlasclose-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/atlasclose-com/security/atlasclose-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlasclose-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atlasclose.com/
- group: company
  title: ''
  type: Blog
  url: https://atlasclose.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://atlasclose.com/onboarding.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlasclose.com/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlasclose.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: mailto:brown_clinton@msn.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlaslaw2026/Atlas-Public-Docket
coverage:
  checked: '2026-11-02'
  detail: AtlasClose does not provide a public API; no OpenAPI, AsyncAPI, GraphQL, or other contract was found on its website or API subdomains.
  evidence:
  - status: 404
    url: https://atlasclose.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-11-01'
description: AtlasClose MCP is an experimental governance layer for AI agents, providing authorization, enforcement, and audit recording of agent actions. It offers a controlled environment where AI agents begin with no authority and must request permissions, with decisions logged in a hash‑chained record for tamper detection. The platform is experimental, not production‑certified, and uses synthetic data for demonstrations.
image: https://atlasclose.com/compass-logo.svg
layout: provider
modified: '2026-11-01'
name: AtlasClose
nav: Providers
network: true
overview: 'AtlasClose is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Governance, Experimental, MCP, and Control.


  AtlasClose''s developer surface includes engineering blog, getting-started guide, support, and 7 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Atlasclose Com Rate Limits
  slug: atlasclose-com-rate-limits
scopes:
- name: Atlasclose Com Scopes
  scope_count: 0
  slug: atlasclose-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 14.5
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atlasclose Com Authentication
  slug: atlasclose-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atlasclose Com Domain Security
  slug: atlasclose-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlasclose-com
tags:
- Artificial Intelligence
- Governance
- Experimental
- MCP
- Control
website: https://atlasclose.com/
---
