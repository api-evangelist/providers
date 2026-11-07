---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Concord Com Agentic Access
  operation_count: 9
  slug: concord-com-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Concord sends outbound HTTP POST webhooks to a URL you configure in the Automations > Integrations UI, firing on agreement lifecycle events - document fully approved, document fully signed, document e
  name: Concord Webhooks (Outbound Events)
  slug: concord-com-webhooks-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: An Agreement is a contract, disregarding its status. A draft, a contract in progress, a negotiation, an executed document, a template are Agreements. You can create, edit and share Agreements.
  name: Concord Agreement API
  slug: concord-com-agreement-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: The Agreement Versions API from Concord — 1 operation(s) for agreement versions.
  name: Concord Agreement Versions API
  slug: concord-com-agreement-versions-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Once you have created an automated template in Concord, you can then create and customize contracts to send out for collaboration and signature. You can designate which content will be variable. Varia
  name: Concord Automated Template API
  slug: concord-com-automated-template-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Clause library related API
  name: Concord Clause Library API
  slug: concord-com-clause-library-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Custom branding related API
  name: Concord Custom Branding API
  slug: concord-com-custom-branding-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Events related API
  name: Concord Events API
  slug: concord-com-events-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Folders related API
  name: Concord Folders API
  slug: concord-com-folders-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Organization related API
  name: Concord Organization API
  slug: concord-com-organization-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Organization groups related API
  name: Concord Organization Groups API
  slug: concord-com-organization-groups-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Organization invitation related API
  name: Concord Organization invitation API
  slug: concord-com-organization-invitation-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Organization members related API
  name: Concord Organization Members API
  slug: concord-com-organization-members-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Report related API
  name: Concord Report API
  slug: concord-com-report-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Signature configuration related endpoints like auto-request and signature slots configuration. You can, for instance, add/remove slots, update their assignation, change orders.
  name: Concord Signature API
  slug: concord-com-signature-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Tags related API
  name: Concord Tags API
  slug: concord-com-tags-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: User related API
  name: Concord User API
  slug: concord-com-user-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: The User integrations API from Concord — 1 operation(s) for user integrations.
  name: Concord User integrations API
  slug: concord-com-user-integrations-api
- baseURL: https://api.concordnow.com/api/rest/1
  baseurl_source: declared
  description: Events sent by Concord to your custom URL.
  name: Concord Webhooks API
  slug: concord-com-webhooks-api
artifact_total: 31
collections:
- collection_type: open
  name: Concord Agreements API
  slug: open-concord-com-agreements-api
- collection_type: open
  name: Concord Agreements Organizations API
  slug: open-concord-com-organizations-api
- collection_type: open
  name: Concord Agreements Templates API
  slug: open-concord-com-templates-api
- collection_type: open
  name: Concord Agreements Users API
  slug: open-concord-com-users-api
- collection_type: open
  name: Concord API
  slug: open-concord-com
common:
- group: company
  title: ''
  type: Blog
  url: https://www.concord.app/blog
- group: other
  href: https://artifacts.apis.io/concord-com/capabilities/concord-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/concord-com-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/concord-com/agentic-access/concord-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/concord-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/concord-com/security/concord-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concord-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/concord-com/authentication/concord-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/concord-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.concord.app
- group: docs
  title: ''
  type: Documentation
  url: https://help.concord.app/concord-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/concordnow
- group: commercial
  href: https://artifacts.apis.io/concord-com/plans/concord-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/concord-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/concord-com/rate-limits/concord-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/concord-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/concord-com/finops/concord-com-finops.yml
  title: ''
  type: FinOps
  url: finops/concord-com-finops.yml
created: '2026-07-12'
description: Concord is a contract lifecycle management (CLM) platform for creating, negotiating, redlining, e-signing, storing, and tracking agreements in one place, with unlimited electronic signatures, automated templates, approval workflows, and reporting. Concord exposes a documented REST API (base https://api.concordnow.com/api/rest/1) that lets integrators read a user's organizations, list and retrieve agreements and their attachments and members, and pull organization reports, groups, and tags. Outbound webhooks notify external systems of agreement lifecycle events (fully approved, fully signed, expired, signature provided). API key generation is offered on paid plans only.
finops:
- has_sources: true
  method: generated
  name: Concord Com Finops
  primary_unit: ''
  service_category: Contract Lifecycle Management
  slug: concord-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/concord-com.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.concord.app over HTTP.
  name: Concord MCP Server
  slug: concord-com
modified: '2026-10-06'
name: Concord
nav: Providers
network: true
overview: 'Concord publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks (Outbound Events), Agreement API, Agreement Versions API, and 15 more. Tagged areas include Contract Management, Contract Lifecycle Management, Contracts, Agreements, and E-Signature.


  The Concord catalog on APIs.io includes 1 Spectral governance ruleset.


  Concord''s developer surface includes engineering blog, authentication, documentation, and 8 more developer resources.'
plans:
- name: Concord Com Plans Pricing
  plan_count: 3
  slug: concord-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Concord Com Rate Limits
  slug: concord-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Concord API Rules
  rule_count: 65
  severity_counts:
    error: 47
    hint: 0
    info: 4
    warn: 14
  slug: concord-com-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 41.0
    developer_ergonomics: 32.1
    discoverability: 68.3
    operational_transparency: 7.9
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 72.7
      total: 22
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/concord-com/concord-com-2026-07-25T210223.png
security:
- kind: authentication
  name: Concord Com Authentication
  slug: concord-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Concord Com Domain Security
  slug: concord-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: concord-com
tags:
- Contract Management
- Contract Lifecycle Management
- Contracts
- Agreements
- E-Signature
- Document Management
- Legal
- Workflows
website: https://www.concord.app
---
