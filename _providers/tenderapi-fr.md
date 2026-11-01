---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Tenderapi Fr Agentic Access
  operation_count: 23
  slug: tenderapi-fr-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 1
apis:
- description: The auth API from tenderapi-fr — 3 operation(s) for auth.
  name: tenderapi-fr Auth API
  slug: tenderapi-fr-auth-api
- description: Search award outcomes. **Requires the pro tier** (free keys get the exact count, rows locked).
  name: tenderapi-fr Awards API
  slug: tenderapi-fr-awards-api
- description: Subscription and billing. **Available on all tiers**.
  name: tenderapi-fr Billing API
  slug: tenderapi-fr-billing-api
- description: Service health check.
  name: tenderapi-fr Health API
  slug: tenderapi-fr-health-api
- description: API key management. **Available on all tiers**.
  name: tenderapi-fr Keys API
  slug: tenderapi-fr-keys-api
- description: 'Alert profiles. Free: 1 profile, weekly email digest. Pro: up to 10, daily, email/Teams/webhook.'
  name: tenderapi-fr Profiles API
  slug: tenderapi-fr-profiles-api
- description: The renewals API from tenderapi-fr — 1 operation(s) for renewals.
  name: tenderapi-fr Renewals API
  slug: tenderapi-fr-renewals-api
- description: Search tender notices. **Available on all tiers** (free, pro).
  name: tenderapi-fr Tenders API
  slug: tenderapi-fr-tenders-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/tenderapi-fr/agentic-access/tenderapi-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenderapi-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/rules/tenderapi-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/tenderapi-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/json-ld/tenderapi-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tenderapi-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/vocabulary/tenderapi-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tenderapi-fr-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tenderapi-fr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/data-model/tenderapi-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenderapi-fr-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tenderapi-fr/authentication/tenderapi-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenderapi-fr-authentication.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/errors/tenderapi-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenderapi-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-fr/conformance/tenderapi-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenderapi-fr-conformance.yml
- group: other
  href: https://artifacts.apis.io/tenderapi-fr/overlays/tenderapi-fr-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tenderapi-fr-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tenderapi-fr/llms/tenderapi-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tenderapi-fr-llms.txt
- group: build
  href: https://artifacts.apis.io/tenderapi-fr/mcp/tenderapi-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tenderapi-fr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tenderapi-fr/mcp/tenderapi-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tenderapi-fr-mcp.yml
- group: other
  href: https://artifacts.apis.io/tenderapi-fr/hosts/tenderapi-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tenderapi-fr-hosts.yml
- group: auth
  href: https://artifacts.apis.io/tenderapi-fr/security/tenderapi-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenderapi-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenderapi.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://tenderapi.fr/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tenderapi.fr/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://tenderapi.fr/guide
- group: commercial
  title: ''
  type: Pricing
  url: https://tenderapi.fr/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenderapi.fr/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IDNSIDNS/tenderapi-mcp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tenderapi.fr/docs
created: '2026-10-31'
description: TenderAPI provides a unified API for French public procurement data from BOAMP and European TED data. It enables developers to search tenders, retrieve award outcomes, and analyze winner patterns across France and the EU. The service offers endpoints for tenders, awards, profiles, keys, billing, health checks, and more, with API key authentication. Documentation and OpenAPI spec are publicly available.
image: https://tenderapi.fr/
json_schemas:
- name: AwardOut
  property_count: 26
  slug: tenderapi-fr-award-out
- name: MeOut
  property_count: 15
  slug: tenderapi-fr-me-out
- name: ProfileCreate
  property_count: 16
  slug: tenderapi-fr-profile-create
- name: ProfileOut
  property_count: 18
  slug: tenderapi-fr-profile-out
- name: ProfilePreviewIn
  property_count: 16
  slug: tenderapi-fr-profile-preview-in
- name: TenderOut
  property_count: 28
  slug: tenderapi-fr-tender-out
jsonld:
- class_count: 24
  name: Tenderapi Fr Context
  property_count: 114
  slug: tenderapi-fr-context
layout: provider
mcp_servers:
- description: Remote MCP server at tenderapi.fr.
  name: tenderapi-fr MCP Server
  slug: tenderapi-fr-mcp-yml
modified: '2026-10-31'
name: tenderapi-fr
nav: Providers
network: true
overview: 'tenderapi-fr publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Awards API, Billing API, and 5 more. Tagged areas include Company, Procurement, PublicData, API, and France.


  The tenderapi-fr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tenderapi-fr''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Tenderapi Fr Plans Pricing
  plan_count: 0
  slug: tenderapi-fr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Tenderapi Fr Rate Limits
  slug: tenderapi-fr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: tenderapi-fr API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: tenderapi-fr-rules
scopes:
- name: Tenderapi Fr Scopes
  scope_count: 0
  slug: tenderapi-fr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 72.7
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 79.1
    contract_quality: 54.9
    developer_ergonomics: 56.4
    discoverability: 56.7
    operational_transparency: 5.3
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
  name: Tenderapi Fr Authentication
  slug: tenderapi-fr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tenderapi Fr Domain Security
  slug: tenderapi-fr-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: search-tenders
  slug: tenderapi-fr-search-tenders
slug: tenderapi-fr
tags:
- Company
- Procurement
- PublicData
- API
- France
- Europe
website: https://tenderapi.fr/
---
