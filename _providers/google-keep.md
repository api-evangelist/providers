---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Keep Agentic Access
  operation_count: 5
  slug: google-keep-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 4
apis:
- description: The Google Keep API API from Google Keep — 1 operation(s) for google keep api.
  name: Google Keep Google Keep API API
  slug: google-keep-google-keep-api-api
- description: The Notes API from Google Keep — 1 operation(s) for notes.
  name: Google Keep Notes API
  slug: google-keep-notes-api
- description: The Permissions:batchCreate API from Google Keep — 1 operation(s) for permissions:batchcreate.
  name: Google Keep Permissions:batchCreate API
  slug: google-keep-permissions-batchcreate-api
- description: The Permissions:batchDelete API from Google Keep — 1 operation(s) for permissions:batchdelete.
  name: Google Keep Permissions:batchDelete API
  slug: google-keep-permissions-batchdelete-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Keep Google Keep API API
  slug: open-google-keep-google-keep-api-api
- collection_type: open
  name: Google Keep Google Keep API Notes API
  slug: open-google-keep-notes-api
- collection_type: open
  name: Google Keep Google Keep API Permissions:batchCreate API
  slug: open-google-keep-permissions-batchcreate-api
- collection_type: open
  name: Google Keep Google Keep API Permissions:batchDelete API
  slug: open-google-keep-permissions-batchdelete-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-keep-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-keep-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-keep-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/keep/api/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/feeds/posts/default/-/Google%20Keep
created: '2026-03-13'
description: The Google Keep API provides programmatic access to Google Keep notes for enterprise administrators. It enables creating, listing, retrieving, and deleting notes, downloading note attachments, and managing note permissions. The API is designed for enterprise use cases where administrators need to manage Keep notes across their organization.
finops:
- name: Google Keep Finops
  service_category: API
  slug: google-keep-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-keep.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 3
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Keep
nav: Providers
network: true
overview: 'Google Keep publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Google Keep API API, Notes API, Permissions:batchCreate API, and 1 more. Tagged areas include Google, Google Workspace, Notes, Organization, and Productivity.


  The Google Keep catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Keep''s developer surface includes getting-started guide, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Google Keep Plans Pricing
  plan_count: 3
  slug: google-keep-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Google Keep Rate Limits
  slug: google-keep-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Keep API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-keep-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Google Keep API Rules
  rule_count: 17
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 4
  slug: google-keep-spectral-rules
score:
  band: thin
  composite: 32.6
  delta: -6.4
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 14.3
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-keep/refs/heads/main/screenshots/google-keep-2026-06-20T182208.png
security:
- kind: domain-security
  name: Google Keep Domain Security
  slug: google-keep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Keep Vulnerability Disclosure
  slug: google-keep-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-keep
tags:
- Google
- Google Workspace
- Notes
- Organization
- Productivity
---
