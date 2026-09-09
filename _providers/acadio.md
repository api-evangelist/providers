---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-08'
api_count: 2
apis:
- description: The Acadio LMS platform surface. Acadio operates an API gateway at api.acadio.com (its own status page lists an "API — Acadio API Services" component) and documents integration entry points in its kno
  name: Acadio LMS Platform
  slug: acadio-lms-platform
- description: Acadio's direct-to-learner course storefront implements the Universal Commerce Protocol over MCP. A live, unauthenticated MCP endpoint at https://acadio.com/api/ucp/mcp answers tools/list with thirtee
  name: Acadio Storefront Agentic Commerce (UCP)
  slug: acadio-storefront-ucp
artifact_total: 9
asyncapis:
- description: ''
  name: Acadio Lms Webhooks
  slug: acadio-lms-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acadio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://acadio.instantdocsbase.com/
- group: operate
  title: ''
  type: Support
  url: https://acadio.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://acadio.com/blogs/lms-articles
- group: start
  title: ''
  type: Login
  url: https://courses.acadio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acadio.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acadio.com/policies/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://acadio.statuspage.io/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/acadio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acadio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/acadio-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acadio-lms-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acadio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acadio-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acadio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acadio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acadio-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acadio-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acadio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acadio-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-06'
description: 'Acadio is a professional-education technology company that builds and operates Acadio LMS, a white-label, cloud-hosted learning management system purpose-built for continuing education, exam prep and certification training. The platform runs branded student and admin portals on acadio.com subdomains, handles course authoring, SCORM 1.2/2004 import, assessments, credits, certificates and regulator reporting, and is sold as a flat per-learner, per-month subscription. Acadio also sells its own FINRA securities licensing exam prep courses (SIE, Series 6, Series 7, Series 63) direct to learners through a Shopify storefront at acadio.com. Its public integration surface is documented in a knowledge base rather than an API reference: JWT single sign-on, Google OAuth 2.0, and an HMAC-signed webhook bus with nineteen topics, plus native connectors for Shopify, WooCommerce, BigCommerce, Zoom, ProctorFree and ChatGPT. The storefront additionally exposes a live, unauthenticated Universal
  Commerce Protocol MCP endpoint for agent-driven purchasing.'
image: https://acadio.com/cdn/shop/files/acadio_dark_social_banner.jpg?v=1762978383
layout: provider
mcp_servers:
- description: 'A live, unauthenticated remote MCP server on Acadio''s own domain that exposes the company''s direct-to-learner securities exam prep storefront to agents: catalog search and lookup, cart construction, c'
  name: Acadio Storefront (Universal Commerce Protocol)
  slug: acadio-storefront-universal-commerce-protocol
modified: '2026-09-06'
name: Acadio
nav: Providers
network: true
overview: 'Acadio publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Learning Management System, Professional Education, and Continuing Education.


  The Acadio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acadio''s developer surface includes documentation, support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Acadio Plans Pricing
  plan_count: 0
  slug: acadio-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Acadio Rate Limits
  slug: acadio-rate-limits
scopes:
- name: Acadio Scopes
  scope_count: 0
  slug: acadio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 40.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Acadio Authentication
  slug: acadio-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Acadio Domain Security
  slug: acadio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acadio
tags:
- Company
- Education
- Learning Management System
- Professional Education
- Continuing Education
- Certification
- Exam Preparation
- SCORM
- Webhooks
- Agentic Commerce
website: https://acadio.com/
---
