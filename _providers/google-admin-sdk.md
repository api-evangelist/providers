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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Google Admin Sdk Agentic Access
  operation_count: 20
  slug: google-admin-sdk-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- baseURL: https://admin.googleapis.com
  baseurl_source: declared
  description: The Admin API from Google Admin SDK — 11 operation(s) for admin.
  name: Google Admin SDK Admin API
  slug: google-admin-sdk-admin-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google SDK Directory Admin API
  slug: open-google-admin-sdk-admin-api
- collection_type: open
  name: Google Admin SDK Directory API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-admin-sdk-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-admin-sdk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-admin-sdk-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/admin/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Admin SDK provides a collection of RESTful APIs for managing Google Workspace organizations at scale. It includes the Directory API for managing users, groups, devices, and organizational units; the Reports API for auditing activity and usage; and the Data Transfer API for migrating data between users. These APIs enable programmatic integration with enterprise IT infrastructure.
finops:
- name: Google Admin Sdk Finops
  service_category: API
  slug: google-admin-sdk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-admin-sdk.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 5
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Admin SDK
nav: Providers
network: true
overview: 'Google Admin SDK publishes 1 API on the [APIs.io](https://apis.io/) network: Admin API. Tagged areas include Administration, Devices, Directory, Enterprise, and Google.


  The Google Admin SDK catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Admin SDK''s developer surface includes getting-started guide, pricing, and 5 more developer resources.'
plans:
- name: Google Admin Sdk Plans Pricing
  plan_count: 3
  slug: google-admin-sdk-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Google Admin Sdk Rate Limits
  slug: google-admin-sdk-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Admin SDK API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-admin-sdk-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 60.3
    catalog_earned_first_party: 0.0
    catalog_gap: 54.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-admin-sdk/refs/heads/main/screenshots/google-admin-sdk-2026-06-20T182002.png
security:
- kind: domain-security
  name: Google Admin Sdk Domain Security
  slug: google-admin-sdk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Admin Sdk Vulnerability Disclosure
  slug: google-admin-sdk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-admin-sdk
tags:
- Administration
- Devices
- Directory
- Enterprise
- Google
- Google Workspace
- Group
- User
---
