---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    error_semantics: derived
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
  score: 4.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Aggregated WHOIS, DNS, SSL, subdomains, and email security intelligence for any domain.
  name: Domain Intelligence API
  slug: domain-intelligence-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/oti-labs-com/rules/oti-labs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/oti-labs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/oti-labs-com/json-ld/oti-labs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/oti-labs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/oti-labs-com/vocabulary/oti-labs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/oti-labs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/oti-labs-com/conformance/oti-labs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oti-labs-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/oti-labs-com/data-model/oti-labs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/oti-labs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/oti-labs-com/errors/oti-labs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oti-labs-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/oti-labs-com/mcp/oti-labs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oti-labs-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/oti-labs-com/hosts/oti-labs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oti-labs-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/oti-labs-com/security/oti-labs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oti-labs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oti-labs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://oti-labs.com/domain-intelligence-api
- group: docs
  title: ''
  type: APIReference
  url: https://oti-labs.com/domain-intelligence-api
- group: commercial
  title: ''
  type: Pricing
  url: https://oti-labs.com/domain-intelligence-api#pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://oti-labs.com/lookup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oti-labs.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/osiris-technical-institute
created: '2026-10-30'
description: OTI Labs provides a Domain Intelligence API that aggregates WHOIS, DNS, SSL, subdomain enumeration, and email security data into a single REST endpoint. The service enables developers and security professionals to retrieve comprehensive domain signals in one call, supporting use cases such as threat intelligence, brand monitoring, and automated security workflows. Powered by the Osiris Technical Institute, OTI Labs offers a free tier with 1,000 requests per month and MIT-licensed source code, positioning itself as a versatile tool for AI agents and security tooling.
image: https://oti-labs.com/assets/og/spot-lookup-v1.png
jsonld:
- class_count: 2
  name: Oti Labs Com Context
  property_count: 4
  slug: oti-labs-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at oti-labs.com.
  name: oti-labs-com MCP Server
  slug: oti-labs-com-mcp-yml
modified: '2026-10-30'
name: oti-labs-com
nav: Providers
network: true
overview: 'oti-labs-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Domain Intelligence, Security, WHOIS, and DNS.


  The oti-labs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  oti-labs-com''s developer surface includes documentation, API reference, pricing, getting-started guide, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: oti-labs-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: oti-labs-com-rules
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 14.3
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 21.4
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/oti-labs-com/oti-labs-com-2026-11-03T140749.png
security:
- kind: domain-security
  name: Oti Labs Com Domain Security
  slug: oti-labs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oti-labs-com
tags:
- Company
- Domain Intelligence
- Security
- WHOIS
- DNS
- SSL
website: https://oti-labs.com/
---
