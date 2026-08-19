---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Offendersearch Api Agentic Access
  operation_count: 36
  slug: offendersearch-api-agentic-access
  summary_line: 36 operations · 18 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: The Account API from Offendersearch API — 1 operation(s) for account.
  name: Offendersearch API Account API
  slug: offendersearch-api-account-api
- description: The Admin API from Offendersearch API — 11 operation(s) for admin.
  name: Offendersearch API Admin API
  slug: offendersearch-api-admin-api
- description: The Auth API from Offendersearch API — 2 operation(s) for auth.
  name: Offendersearch API Auth API
  slug: offendersearch-api-auth-api
- description: The Batch API from Offendersearch API — 1 operation(s) for batch.
  name: Offendersearch API Batch API
  slug: offendersearch-api-batch-api
- description: The Billing API from Offendersearch API — 1 operation(s) for billing.
  name: Offendersearch API Billing API
  slug: offendersearch-api-billing-api
- description: The Compat API from Offendersearch API — 1 operation(s) for compat.
  name: Offendersearch API Compat API
  slug: offendersearch-api-compat-api
- description: The Keys API from Offendersearch API — 3 operation(s) for keys.
  name: Offendersearch API Keys API
  slug: offendersearch-api-keys-api
- description: The Proof Docs API from Offendersearch API — 1 operation(s) for proof docs.
  name: Offendersearch API Proof Docs API
  slug: offendersearch-api-proof-docs-api
- description: The Records API from Offendersearch API — 1 operation(s) for records.
  name: Offendersearch API Records API
  slug: offendersearch-api-records-api
- description: The Report API from Offendersearch API — 1 operation(s) for report.
  name: Offendersearch API Report API
  slug: offendersearch-api-report-api
- description: The Search API from Offendersearch API — 1 operation(s) for search.
  name: Offendersearch API Search API
  slug: offendersearch-api-search-api
- description: The Searches API from Offendersearch API — 3 operation(s) for searches.
  name: Offendersearch API Searches API
  slug: offendersearch-api-searches-api
- description: The Sources API from Offendersearch API — 1 operation(s) for sources.
  name: Offendersearch API Sources API
  slug: offendersearch-api-sources-api
- description: The Support API from Offendersearch API — 1 operation(s) for support.
  name: Offendersearch API Support API
  slug: offendersearch-api-support-api
- description: The Team API from Offendersearch API — 2 operation(s) for team.
  name: Offendersearch API Team API
  slug: offendersearch-api-team-api
- description: The Usage API from Offendersearch API — 1 operation(s) for usage.
  name: Offendersearch API Usage API
  slug: offendersearch-api-usage-api
artifact_total: 23
asyncapis:
- description: ''
  name: Offendersearch Api Webhooks
  slug: offendersearch-api-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/offendersearch-api-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/offendersearch-api-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/offendersearch-api-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offendersearch-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offendersearch-api-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/offendersearch-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/offendersearch-api-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offendersearch-api-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/offendersearch-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/offendersearch-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/offendersearch-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/offendersearch-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/offendersearch-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/offendersearch-api-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/offendersearch-api-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/offendersearch-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/offendersearch-api-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://offendersearch.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://offendersearch.app/sign-up
- group: start
  title: ''
  type: Login
  url: https://offendersearch.app/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offendersearch.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offendersearch.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://offendersearch.app/contact
created: '2026-08-18'
description: 'Offendersearch, Inc. operates a REST API that unifies US sex-offender registry data — all 50 states, the District of Columbia, the US territories and NSOPW, 58 registries in all — behind a single authenticated endpoint. One call searches every jurisdiction and returns scored, de-duplicated records in one normalized 76-field schema, each carrying per-source provenance, a deep link back to the originating registry, and its own lastCheckedAt timestamp. Its defining contract is completeness labelling: an incomplete search is reported as partial with per-source status and a closed incompleteReason enum rather than returned as a silently empty result, so a zero from a registry that did not finish reads as UNKNOWN rather than NO MATCH. The API offers synchronous, asynchronous (with signed webhooks and Idempotency-Key retries) and 1,000-row batch/CSV modes, per-request freshness tiers, consolidated timestamped verification-report PDFs with a citation on every record, and a drop-in
  offenders.io compatibility endpoint. It publishes an OpenAPI 3.1 contract in JSON and YAML, an RFC 9727 api-catalog, an llms.txt, a markdown twin of every documentation page, and a documented (private-beta) MCP server. Pricing is purely metered at $0.15 per call, $0.11 above 2,000 a month. Offendersearch is expressly not a consumer reporting agency and its results are not a consumer report.'
image: https://offendersearch.app/opengraph-image.png
layout: provider
modified: '2026-08-18'
name: Offendersearch API
nav: Providers
network: true
overview: 'Offendersearch API publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Auth API, and 13 more. Tagged areas include background-checks, identity-verification, public-records, criminal-records, and compliance.


  The Offendersearch API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Offendersearch API''s developer surface includes authentication, pricing, signup flow, support, and 20 more developer resources.'
plans:
- name: Offendersearch Api Plans Pricing
  plan_count: 2
  slug: offendersearch-api-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 0
  name: Offendersearch Api Rate Limits
  slug: offendersearch-api-rate-limits
score:
  band: developing
  composite: 47.8
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 16.7
    contract_quality: 61.3
    developer_ergonomics: 18.5
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Offendersearch Api Authentication
  slug: offendersearch-api-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Offendersearch Api Domain Security
  slug: offendersearch-api-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Offendersearch Api Trust Center
  slug: offendersearch-api-trust-center
  summary_line: trust center published
slug: offendersearch-api
tags:
- background-checks
- identity-verification
- public-records
- criminal-records
- compliance
- trust-and-safety
- hr-tech
- recruiting
- proptech
- tenant-screening
- healthcare-screening
- data-api
- mcp-server
- agent-native
---
