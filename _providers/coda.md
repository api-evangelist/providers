---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 58
  human_in_the_loop: 1
  name: Coda Agentic Access
  operation_count: 124
  slug: coda-agentic-access
  summary_line: 124 operations · 58 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: At this time, the API exposes some limited information about your account. However, `/whoami` is a good endpoint to hit to verify that you're hitting the API correctly and that your token is working a
  name: Coda Account API
  slug: coda-account-api
- description: This API offers analytics data for your docs and Packs over time.
  name: Coda Analytics API
  slug: coda-analytics-api
- description: This API allows you to trigger automations.
  name: Coda Automations API
  slug: coda-automations-api
- description: While columns in Coda have user-friendly names, they also have immutable IDs that are used when reading and writing rows. These endpoints let you query the columns in a table and get basic information
  name: Coda Columns API
  slug: coda-columns-api
- description: Controls provide a user-friendly way to input a value that can affect other parts of the doc. This API lets you list controls and get their current values.
  name: Coda Controls API
  slug: coda-controls-api
- description: The CustomDocDomains API from Coda — 3 operation(s) for customdocdomains.
  name: Coda CustomDocDomains API
  slug: coda-customdocdomains-api
- description: Coda docs are foundational, top-level collaborative projects that contain pages. The API lets you list and search your docs to obtain basic metadata like titles and ownership information.
  name: Coda Docs API
  slug: coda-docs-api
- description: Folders help you organize your docs within workspaces. This API lets you list, create, update, and delete folders.
  name: Coda Folders API
  slug: coda-folders-api
- description: Formulas can be great for performing one-off computations, or used with tables and other formulas to compute a single value. With this API, you can discover formulas in a doc and obtain computed resul
  name: Coda Formulas API
  slug: coda-formulas-api
- description: The Go Links API from Coda — 1 operation(s) for go links.
  name: Coda Go Links API
  slug: coda-go-links-api
- description: These endpoints wouldn't fit anywhere else, but you may find them useful when working with Coda.
  name: Coda Miscellaneous API
  slug: coda-miscellaneous-api
- description: This API allows you to manage Packs that you have developed as well as list publicly available Coda packs.
  name: Coda Packs API
  slug: coda-packs-api
- description: Pages in Coda offer canvases containing rich text, tables, controls, and other objects. At this time, this API lets you list and access pages in a doc.
  name: Coda Pages API
  slug: coda-pages-api
- description: This API lets you manage sharing and permissions for your docs.
  name: Coda Permissions API
  slug: coda-permissions-api
- description: Coda docs can be published publicly and associated with categories to help the world discover them. This API lets you manage the publishing settings of your docs.
  name: Coda Publishing API
  slug: coda-publishing-api
- description: You'll likely use this part of the API the most. These endpoints let you retrieve row data from tables in Coda as well as create, upsert, update, and delete them. Most of these endpoints work for both
  name: Coda Rows API
  slug: coda-rows-api
- description: The Tables API from Coda — 2 operation(s) for tables.
  name: Coda Tables API
  slug: coda-tables-api
- description: This API allows you to manage your workspace's membership and get analytics on membership over time.
  name: Coda Workspaces API
  slug: coda-workspaces-api
artifact_total: 48
asyncapis:
- description: AsyncAPI description of Coda's documented automation/webhook surface. Coda does NOT publish an outbound webhook subscription API in the public REST reference. The documented eventing surface is inboun
  name: Coda Automations Push API
  slug: coda-automations-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coda Account API
  slug: open-coda-account-api
- collection_type: open
  name: Coda Account Analytics API
  slug: open-coda-analytics-api
- collection_type: open
  name: Coda Account Automations API
  slug: open-coda-automations-api
- collection_type: open
  name: Coda Account Columns API
  slug: open-coda-columns-api
- collection_type: open
  name: Coda Account Controls API
  slug: open-coda-controls-api
- collection_type: open
  name: Coda Account CustomDocDomains API
  slug: open-coda-customdocdomains-api
- collection_type: open
  name: Coda Account Docs API
  slug: open-coda-docs-api
- collection_type: open
  name: Coda Account Folders API
  slug: open-coda-folders-api
- collection_type: open
  name: Coda Account Formulas API
  slug: open-coda-formulas-api
- collection_type: open
  name: Coda Account Go Links API
  slug: open-coda-go-links-api
- collection_type: open
  name: Coda Account Miscellaneous API
  slug: open-coda-miscellaneous-api
- collection_type: open
  name: Coda Account Packs API
  slug: open-coda-packs-api
- collection_type: open
  name: Coda Account Pages API
  slug: open-coda-pages-api
- collection_type: open
  name: Coda Account Permissions API
  slug: open-coda-permissions-api
- collection_type: open
  name: Coda Account Publishing API
  slug: open-coda-publishing-api
- collection_type: open
  name: Coda Account Rows API
  slug: open-coda-rows-api
- collection_type: open
  name: Coda Account Tables API
  slug: open-coda-tables-api
- collection_type: open
  name: Coda Account Workspaces API
  slug: open-coda-workspaces-api
- collection_type: open
  name: Coda API
  slug: open-coda
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/coda-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coda-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coda-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codainc
- group: company
  title: ''
  type: Website
  url: https://coda.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coda.io/developers/apis/v1
- group: commercial
  title: ''
  type: Pricing
  url: https://coda.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coda
- group: commercial
  title: ''
  type: Plans
  url: plans/coda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coda-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://coda.io/blog
created: '2026-05-08'
description: Coda is an all-in-one doc platform combining documents, spreadsheets, and apps. The Coda API exposes docs, pages, tables, rows, columns, controls, formulas, automations, packs, permissions, and analytics for programmatic integration.
finops:
- name: Coda Finops
  service_category: Productivity
  slug: coda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coda.png
layout: provider
modified: '2026-05-30'
name: Coda
nav: Providers
network: true
overview: 'Coda publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Automations API, and 15 more. Tagged areas include Productivity, Docs, No-Code, Collaboration, and Database.


  The Coda catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Coda''s developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Coda Plans Pricing
  plan_count: 4
  slug: coda-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Coda Rate Limits
  slug: coda-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Coda API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: coda-asyncapi-spectral-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 65.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 11.4
    contract_quality: 69.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 13.2
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coda/refs/heads/main/screenshots/coda-2026-06-20T174651.png
security:
- kind: authentication
  name: Coda Authentication
  slug: coda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coda Domain Security
  slug: coda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coda Vulnerability Disclosure
  slug: coda-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Coda Trust Center
  slug: coda-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: coda
tags:
- Productivity
- Docs
- No-Code
- Collaboration
- Database
website: https://coda.io/
---
