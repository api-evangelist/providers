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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for managing features, components, products, notes (customer feedback), users, companies, objectives, releases, and webhooks within Productboard. Supports both v1 and v2 endpoints. Authentica
  name: Productboard Public API
  slug: public-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Entities API from Productboard — 5 operation(s) for entities.
  name: Productboard Entities API
  slug: productboard-entities-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Entity Field Values API from Productboard — 2 operation(s) for entity field values.
  name: Productboard Entity Field Values API
  slug: productboard-entity-field-values-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Entity Relationships API from Productboard — 2 operation(s) for entity relationships.
  name: Productboard Entity Relationships API
  slug: productboard-entity-relationships-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Jira Integrations API from Productboard — 4 operation(s) for jira integrations.
  name: Productboard Jira Integrations API
  slug: productboard-jira-integrations-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Members API from Productboard — 4 operation(s) for members.
  name: Productboard Members API
  slug: productboard-members-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Note Relationships API from Productboard — 3 operation(s) for note relationships.
  name: Productboard Note Relationships API
  slug: productboard-note-relationships-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Notes API from Productboard — 5 operation(s) for notes.
  name: Productboard Notes API
  slug: productboard-notes-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Plugin Integrations API from Productboard — 5 operation(s) for plugin integrations.
  name: Productboard Plugin Integrations API
  slug: productboard-plugin-integrations-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Teams API from Productboard — 4 operation(s) for teams.
  name: Productboard Teams API
  slug: productboard-teams-api
- baseURL: https://api.productboard.com
  baseurl_source: declared
  description: The Webhooks API from Productboard — 2 operation(s) for webhooks.
  name: Productboard Webhooks API
  slug: productboard-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: Productboard Public Entities API
  slug: open-productboard-entities-api
- collection_type: open
  name: Productboard Public Entity Field Values API
  slug: open-productboard-entity-field-values-api
- collection_type: open
  name: Productboard Public Entity Relationships API
  slug: open-productboard-entity-relationships-api
- collection_type: open
  name: Productboard Public Jira Integrations API
  slug: open-productboard-jira-integrations-api
- collection_type: open
  name: Productboard Public Members API
  slug: open-productboard-members-api
- collection_type: open
  name: Productboard Public Note Relationships API
  slug: open-productboard-note-relationships-api
- collection_type: open
  name: Productboard Public Notes API
  slug: open-productboard-notes-api
- collection_type: open
  name: Productboard Public Plugin Integrations API
  slug: open-productboard-plugin-integrations-api
- collection_type: open
  name: Productboard Public Teams API
  slug: open-productboard-teams-api
- collection_type: open
  name: Productboard Public Webhooks API
  slug: open-productboard-webhooks-api
common:
- group: other
  href: https://artifacts.apis.io/productboard/capabilities/productboard-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/productboard-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/productboard/security/productboard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/productboard-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/productboard/security/productboard-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/productboard-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/productboard/security/productboard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/productboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/productboard
- group: company
  title: ''
  type: Website
  url: https://www.productboard.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.productboard.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.productboard.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.productboard.com/trial/
- group: operate
  title: ''
  type: Support
  url: https://support.productboard.com
- group: company
  title: ''
  type: Blog
  url: https://www.productboard.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.productboard.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/productboard/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.productboard.com/llms.txt
created: '2026-05-11'
description: Productboard is a product management platform that helps product teams capture user feedback, prioritize features, build product roadmaps, and align engineering, design, and go-to-market stakeholders around what to build next. The Productboard Public REST API (v1 and v2) provides programmatic access to features, components, products, notes, users, companies, objectives, releases, and webhooks at https://api.productboard.com, with authentication via a Public API Access token (Bearer) or OAuth2.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/productboard.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.productboard.com over HTTP.
  name: Productboard MCP Server
  slug: productboard
modified: '2026-05-11'
name: Productboard
nav: Providers
network: true
overview: 'Productboard publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API, Entities API, Entity Field Values API, and 8 more. Tagged areas include Product Management, Roadmapping, Customer Feedback, Prioritization, and Product Operations.


  The Productboard catalog on APIs.io includes 1 Spectral governance ruleset.


  Productboard''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 9 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Productboard API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: productboard-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.2
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 46.3
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 28.9
  previous_composite: 37.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/productboard/productboard-2026-06-20T192139.png
security:
- kind: domain-security
  name: Productboard Domain Security
  slug: productboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Productboard Vulnerability Disclosure
  slug: productboard-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Productboard Trust Center
  slug: productboard-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: productboard
tags:
- Product Management
- Roadmapping
- Customer Feedback
- Prioritization
- Product Operations
website: https://www.productboard.com
---
