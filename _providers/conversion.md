---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Conversion Agentic Access
  operation_count: 29
  slug: conversion-agentic-access
  summary_line: 29 operations · 23 acting
api_count: 1
apis:
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Audiences API from Conversion — 1 operation(s) for audiences.
  name: Conversion Audiences API
  slug: conversion-audiences-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Campaigns API from Conversion — 4 operation(s) for campaigns.
  name: Conversion Campaigns API
  slug: conversion-campaigns-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Contacts API from Conversion — 2 operation(s) for contacts.
  name: Conversion Contacts API
  slug: conversion-contacts-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Custom Objects API from Conversion — 1 operation(s) for custom objects.
  name: Conversion Custom Objects API
  slug: conversion-custom-objects-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Events API from Conversion — 2 operation(s) for events.
  name: Conversion Events API
  slug: conversion-events-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Exports API from Conversion — 10 operation(s) for exports.
  name: Conversion Exports API
  slug: conversion-exports-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Fields API from Conversion — 2 operation(s) for fields.
  name: Conversion Fields API
  slug: conversion-fields-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Forms API from Conversion — 2 operation(s) for forms.
  name: Conversion Forms API
  slug: conversion-forms-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Full Delete API from Conversion — 1 operation(s) for full delete.
  name: Conversion Full Delete API
  slug: conversion-full-delete-api
- baseURL: https://pub-api.conversion.ai/api
  baseurl_source: declared
  description: The Workflows API from Conversion — 1 operation(s) for workflows.
  name: Conversion Workflows API
  slug: conversion-workflows-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/conversion/agentic-access/conversion-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/conversion-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/conversion/rules/conversion-rules.yml
  title: ''
  type: Spectral
  url: rules/conversion-rules.yml
- group: design
  href: https://artifacts.apis.io/conversion/json-ld/conversion-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/conversion-context.jsonld
- group: design
  href: https://artifacts.apis.io/conversion/vocabulary/conversion-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/conversion-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/conversion/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/conversion/data-model/conversion-data-model.yml
  title: ''
  type: DataModel
  url: data-model/conversion-data-model.yml
- group: operate
  href: https://artifacts.apis.io/conversion/changelog/conversion-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/conversion-changelog.yml
- group: start
  href: https://artifacts.apis.io/conversion/sandbox/conversion-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/conversion-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://conversion.ai/security/
- group: auth
  href: https://artifacts.apis.io/conversion/authentication/conversion-authentication.yml
  title: ''
  type: Authentication
  url: authentication/conversion-authentication.yml
- group: design
  href: https://artifacts.apis.io/conversion/errors/conversion-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/conversion-problem-types.yml
- group: design
  href: https://artifacts.apis.io/conversion/conformance/conversion-conformance.yml
  title: ''
  type: Conformance
  url: conformance/conversion-conformance.yml
- group: agent
  href: https://artifacts.apis.io/conversion/llms/conversion-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/conversion-llms.txt
- group: other
  href: https://artifacts.apis.io/conversion/a2a/conversion-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/conversion-a2a.yml
- group: build
  href: https://artifacts.apis.io/conversion/mcp/conversion-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/conversion-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/conversion/mcp/conversion-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/conversion-mcp.yml
- group: auth
  href: https://artifacts.apis.io/conversion/well-known/conversion-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/conversion-support-security.txt
- group: agent
  href: https://artifacts.apis.io/conversion/well-known/conversion-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/conversion-well-known.yml
- group: other
  href: https://artifacts.apis.io/conversion/hosts/conversion-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conversion-hosts.yml
- group: other
  href: https://artifacts.apis.io/conversion/vendors/conversion-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conversion-vendors.yml
- group: build
  href: https://artifacts.apis.io/conversion/packages/conversion-packages.yml
  title: ''
  type: SDKs
  url: packages/conversion-packages.yml
- group: build
  href: https://artifacts.apis.io/conversion/packages/conversion-packages.yml
  title: ''
  type: Packages
  url: packages/conversion-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://conversion.ai/integrations/webhook/
- group: operate
  title: ''
  type: Support
  url: https://support.conversion.ai/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conversion.ai/
- group: auth
  title: ''
  type: Security
  url: https://conversion.ai/security/
- group: operate
  title: ''
  type: ChangeLog
  url: https://conversion.ai/changelog/
- group: auth
  href: https://artifacts.apis.io/conversion/security/conversion-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/conversion-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/conversion/security/conversion-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conversion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://conversion.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.conversion.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.conversion.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.conversion.ai/product-docs/introduction
- group: company
  title: ''
  type: Blog
  url: https://conversion.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://conversion.ai/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conversion.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conversion.ai/privacy/
created: '2026-10-29'
description: Conversion is an AI‑native B2B marketing automation platform that replaces Marketo, Pardot, or HubSpot with AI agents and a complete platform for data, campaigns, and reporting. It offers features such as campaigns, automations, segmentation, email studio, landing pages, forms, lead scoring, Salesforce sync, and more, all built on a modern AI‑driven architecture.
image: https://conversion.ai/favicon.svg
json_schemas:
- name: ContactFields
  property_count: 0
  slug: conversion-contact-fields
- name: Contact
  property_count: 7
  slug: conversion-contact
- name: FieldSchema
  property_count: 7
  slug: conversion-field-schema
- name: RelationshipFieldReference
  property_count: 3
  slug: conversion-relationship-field-reference
- name: RelationshipFieldSide
  property_count: 4
  slug: conversion-relationship-field-side
- name: SubscriptionStatus
  property_count: 0
  slug: conversion-subscription-status
jsonld:
- class_count: 6
  name: Conversion Context
  property_count: 15
  slug: conversion-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.conversion.ai.
  name: Conversion MCP Server
  slug: conversion-mcp-yml
modified: '2026-10-29'
name: Conversion
nav: Providers
network: true
overview: 'Conversion publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audiences API, Campaigns API, Contacts API, and 7 more. Tagged areas include Marketing, Automation, Artificial Intelligence, B2B, and Software-as-a-Service.


  The Conversion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Conversion''s developer surface includes changelog, sandbox, authentication, support, documentation, API reference, getting-started guide, and 30 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Conversion API Rules
  rule_count: 59
  severity_counts:
    error: 51
    hint: 0
    info: 3
    warn: 5
  slug: conversion-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.7
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 62.5
    developer_ergonomics: 45.8
    discoverability: 75.0
    operational_transparency: 25.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 59.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/conversion/conversion-2026-11-03T125233.png
security:
- kind: authentication
  name: Conversion Authentication
  slug: conversion-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Conversion Domain Security
  slug: conversion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Conversion Trust Center
  slug: conversion-trust-center
  summary_line: SOC 2, GDPR
skill_count: 1
skills:
- name: track-event
  slug: conversion-track-event
slug: conversion
tags:
- Marketing
- Automation
- Artificial Intelligence
- B2B
- Software-as-a-Service
- Platform
website: https://conversion.ai
---
