---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Uncle Nearest Agentic Access
  operation_count: 47
  slug: uncle-nearest-agentic-access
  summary_line: 47 operations · 25 acting
api_count: 3
apis:
- description: Read-only-by-default REST API for the events, venues, organizers, event categories and event tags published on unclenearest.com, served by The Events Calendar plugin from the brand's own WordPress hos
  name: Uncle Nearest Events Calendar REST API (tribe/events/v1)
  slug: uncle-nearest-events-calendar-rest-api-tribeeventsv1
- description: Second-generation Events Calendar REST API on the same host, covering events, organizers, venues and series with named operationIds. Self-publishes an OpenAPI 3.0.4 document at its /docs endpoint. Rea
  name: Uncle Nearest Events Calendar REST API (tec/v1)
  slug: uncle-nearest-events-calendar-rest-api-tecv1
- description: The standard WordPress core REST API exposed at unclenearest.com/wp-json/, publishing the brand's posts, pages, media, categories, tags, taxonomies and custom event post types as JSON. The route index
  name: Uncle Nearest WordPress REST API
  slug: uncle-nearest-wordpress-rest-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uncle-nearest-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://unclenearest.com/
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/uncle-nearest_stock/
- group: company
  title: ''
  type: About
  url: https://unclenearest.com/history
- group: company
  title: ''
  type: Press
  url: https://unclenearest.com/press/
- group: operate
  title: ''
  type: Contact
  url: https://unclenearest.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://unclenearest.com/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://unclenearest.com/nearest-green-distillery-faqs/
- group: other
  title: ''
  type: Events
  url: https://unclenearest.com/live/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unclenearest.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unclenearest.com/privacy/
- group: other
  title: ''
  type: Accessibility
  url: https://unclenearest.com/accessibility/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/unclenearest
- group: company
  title: ''
  type: Facebook
  url: https://facebook.com/unclenearest
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/unclenearest
- group: learn
  title: ''
  type: Youtube
  url: https://www.youtube.com/channel/UCcfM0XBsHSQRB18ssOImb_g
- group: auth
  title: ''
  type: Authentication
  url: authentication/uncle-nearest-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uncle-nearest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uncle-nearest-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uncle-nearest-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uncle-nearest-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uncle-nearest-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uncle-nearest-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uncle-nearest-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: Uncle Nearest, Inc. is an American whiskey company headquartered in Shelbyville, Tennessee, founded in 2017 by Fawn Weaver and Keith Weaver and named for Nathan "Nearest" Green, the formerly enslaved master distiller who taught Jack Daniel the craft. The company produces the Uncle Nearest 1856 Premium Aged, 1884 Small Batch, Master Blend, Single Barrel, Straight Rye and Uncut/Unfiltered Rye expressions, and operates the Nearest Green Distillery visitor destination in Shelbyville with tours, tastings, private events and a retail shop. Uncle Nearest is a privately held, consumer-facing brand with no developer program and no product API; its only public machine-readable surfaces are the WordPress REST API and the two OpenAPI-documented Events Calendar REST APIs served from its own web host at unclenearest.com, which expose the brand's published events, venues and organizers as read-only JSON.
image: https://unclenearest.com/wp-content/themes/unclenearest/lib/img/un-logo-2022.svg
layout: provider
modified: '2026-08-02'
name: Uncle Nearest
nav: Providers
network: true
overview: 'Uncle Nearest publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events Calendar REST API (tribe/events/v1) and Events Calendar REST API (tec/v1). Tagged areas include Company, whiskey, spirits, beverage-alcohol, and consumer-packaged-goods.


  Uncle Nearest''s developer surface includes support, FAQ, YouTube channel, authentication, and 21 more developer resources.'
random_paper: 91
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 49.1
    developer_ergonomics: 16.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Uncle Nearest Authentication
  slug: uncle-nearest-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Uncle Nearest Domain Security
  slug: uncle-nearest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: uncle-nearest
tags:
- Company
- whiskey
- spirits
- beverage-alcohol
- consumer-packaged-goods
- distillery
- hospitality
- events
- tennessee
- wordpress
website: https://unclenearest.com/
---
