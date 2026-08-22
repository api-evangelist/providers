---
agent_readiness:
  band: agent-aware
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Uncle Nearest Agentic Access
  operation_count: 47
  slug: uncle-nearest-agentic-access
  summary_line: 47 operations · 25 acting
api_count: 9
apis:
- description: The standard WordPress core REST API exposed at unclenearest.com/wp-json/, publishing the brand's posts, pages, media, categories, tags, taxonomies and custom event post types as JSON. The route index
  name: Uncle Nearest WordPress REST API
  slug: uncle-nearest-wordpress-rest-api
- description: The Categories API from Uncle Nearest — 2 operation(s) for categories.
  name: Uncle Nearest Categories API
  slug: uncle-nearest-categories-api
- description: These operations are introduced by the Common library.
  name: Uncle Nearest Common API
  slug: uncle-nearest-common-api
- description: The Doc API from Uncle Nearest — 1 operation(s) for doc.
  name: Uncle Nearest Doc API
  slug: uncle-nearest-doc-api
- description: The Events API from Uncle Nearest — 7 operation(s) for events.
  name: Uncle Nearest Events API
  slug: uncle-nearest-events-api
- description: These operations are introduced by Events Pro.
  name: Uncle Nearest Events Pro API
  slug: uncle-nearest-events-pro-api
- description: The Organizers API from Uncle Nearest — 3 operation(s) for organizers.
  name: Uncle Nearest Organizers API
  slug: uncle-nearest-organizers-api
- description: The Tags API from Uncle Nearest — 2 operation(s) for tags.
  name: Uncle Nearest Tags API
  slug: uncle-nearest-tags-api
- description: The Venues API from Uncle Nearest — 3 operation(s) for venues.
  name: Uncle Nearest Venues API
  slug: uncle-nearest-venues-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Events Calendar REST Categories API
  slug: open-uncle-nearest-categories-api
- collection_type: open
  name: Events Calendar REST Common API
  slug: open-uncle-nearest-common-api
- collection_type: open
  name: Events Calendar REST Doc API
  slug: open-uncle-nearest-doc-api
- collection_type: open
  name: Uncle Nearest Events API
  slug: open-uncle-nearest-events-api
- collection_type: open
  name: Events Calendar REST Events Pro API
  slug: open-uncle-nearest-events-pro-api
- collection_type: open
  name: Events Calendar REST Organizers API
  slug: open-uncle-nearest-organizers-api
- collection_type: open
  name: Events Calendar REST Tags API
  slug: open-uncle-nearest-tags-api
- collection_type: open
  name: Events Calendar REST Venues API
  slug: open-uncle-nearest-venues-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uncle-nearest-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/uncle-nearest-events-calendar-v1-overlay.yaml
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
mcp_servers:
- description: ''
  name: uncle-nearest-mcp.yml
  slug: uncle-nearest-mcpyml
modified: '2026-08-02'
name: Uncle Nearest
nav: Providers
network: true
overview: 'Uncle Nearest publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Common API, Doc API, and 5 more. Tagged areas include Company, whiskey, spirits, beverage-alcohol, and consumer-packaged-goods.


  Uncle Nearest''s developer surface includes support, FAQ, YouTube channel, authentication, and 23 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 29.8
  delta: 0.7
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 46.9
    developer_ergonomics: 18.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
