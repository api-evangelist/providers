---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Randomuser Agentic Access
  operation_count: 2
  slug: randomuser-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Generate one or more synthetic user records.
  name: Random User Generator Users API
  slug: randomuser-users-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Random User Generator Users API
  slug: open-randomuser-users-api
- collection_type: open
  name: Random User Generator API
  slug: open-randomuser
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/RandomAPI/Randomuser.me-Node/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/randomuser-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/randomuser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://randomuser.me
- group: docs
  title: ''
  type: Documentation
  url: https://randomuser.me/documentation
- group: operate
  title: ''
  type: ChangeLog
  url: https://randomuser.me/changelog
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/RandomAPI
- group: build
  title: Randomuser.me-Node (Canonical Source)
  type: GitHubRepository
  url: https://github.com/RandomAPI/Randomuser.me-Node
- group: other
  title: ''
  type: X
  url: https://twitter.com/randomapi
- group: commercial
  title: Free (Donation-Funded)
  type: Pricing
  url: https://randomuser.me/#donate
- group: commercial
  title: ''
  type: Plans
  url: plans/randomuser-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/randomuser-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/randomuser-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://github.com/RandomAPI/Randomuser.me-Node/issues
created: '2026-06-13'
description: Free random user data API for generating realistic fake user profiles with names, addresses, photos, and contact data for UI mockups and testing. Open-source REST API with no authentication required, seedable for reproducibility, and multi-format output (JSON, CSV, YAML, XML).
examples:
- key_count: 3
  name: Randomuser Csv Export Example
  slug: randomuser-csv-export-example
- key_count: 2
  name: Randomuser Generate Users Example
  slug: randomuser-generate-users-example
- key_count: 3
  name: Randomuser Paginated Seed Example
  slug: randomuser-paginated-seed-example
features:
- description: No API key, no signup, no per-key quotas; just hit the endpoint.
  name: Free and unauthenticated
- description: The same (seed, page, results, version) tuple always returns the same users.
  name: Seedable reproducibility
- description: Mix 21 nationalities (v1.4) so addresses, IDs, and phone formats stay locale-appropriate.
  name: Multi-nationality cohort
- description: Use `inc` / `exc` to keep payloads small and skip CPU-heavy fields like `login`.
  name: Field projection
- description: JSON, PrettyJSON, CSV, YAML, XML; plus JSONP via `callback`.
  name: Multi-format output
- description: Lock requests to /1.0/ through /1.4/ so upstream releases never break your fixtures.
  name: Path-pinned versioning
- description: Three resolutions (large, medium, thumbnail) hosted on randomuser.me.
  name: Pre-generated portrait images
- description: MIT-licensed Node.js codebase; self-hostable if you need air-gapped operation.
  name: Open source
finops:
- name: Randomuser Finops
  service_category: ''
  slug: randomuser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/randomuser.png
integrations:
- description: Documented usage with $.ajax for browser-side fetches.
  name: jQuery / AJAX
- description: Use directly from server-side JavaScript; offline module available.
  name: Node.js
- description: Pull synthetic users straight into design comps (legacy extension).
  name: Photoshop Extension
- description: Sketch plugin for filling layers with random users (legacy).
  name: Sketch Extension
- description: Multiple community MCP servers expose the API to LLM agents (pipeworx-io, hugo-85, rycid).
  name: Model Context Protocol
json_schemas:
- name: UserResponse
  property_count: 2
  slug: randomuser-user-response
- name: User
  property_count: 12
  slug: randomuser-user
json_structures:
- name: Randomuser User Structure
  property_count: 0
  slug: randomuser-user-structure
jsonld:
- class_count: 39
  name: Randomuser Context
  property_count: 1
  slug: randomuser-context
layout: provider
modified: '2026-06-13'
name: Random User Generator
nav: Providers
network: true
overview: 'Random User Generator publishes 1 API on the [APIs.io](https://apis.io/) network: Users API. Tagged areas include Test Data, Synthetic Data, Mock Data, Open Source, and Public API.


  The Random User Generator catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Random User Generator''s developer surface includes documentation, changelog, pricing, support, and 10 more developer resources.'
plans:
- name: Randomuser Plans Pricing
  plan_count: 1
  slug: randomuser-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Randomuser Rate Limits
  slug: randomuser-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Random User Generator API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: randomuser-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Random User Generator API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: randomuser-rules
score:
  band: thin
  composite: 28.1
  delta: -5.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 26.2
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/randomuser/refs/heads/main/screenshots/randomuser-2026-06-20T192554.png
security:
- kind: domain-security
  name: Randomuser Domain Security
  slug: randomuser-domain-security
  summary_line: TLSv1.3
slug: randomuser
solutions:
- description: Free, public, donation-funded endpoint at randomuser.me/api.
  name: Hosted API
- description: Generate the same shape of users without network calls using the offline RandomAPI module.
  name: Offline npm module
- description: Clone Randomuser.me-Node and run the generator inside your own infrastructure.
  name: Self-hosted
tags:
- Test Data
- Synthetic Data
- Mock Data
- Open Source
- Public API
- Free API
use_cases:
- description: Populate UI mockups, design comps, and Storybook fixtures with realistic users.
  name: Frontend prototyping
- description: Generate seeded fixtures for unit, integration, and snapshot tests.
  name: Test data for QA / CI
- description: Bulk-generate up to 5000 users per request to seed performance test runs.
  name: Load testing
- description: Request specific nationalities to validate address parsing, phone formats, and Unicode rendering.
  name: i18n / localization
- description: Populate sales demos, sandbox environments, and tutorials with realistic-looking accounts.
  name: Demo content
- description: Use the picture URLs as throwaway avatars for prototyping.
  name: Avatar placeholders
website: https://randomuser.me
---
