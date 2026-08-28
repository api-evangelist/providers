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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 41
  human_in_the_loop: 0
  name: Wikimedia Agentic Access
  operation_count: 99
  slug: wikimedia-agentic-access
  summary_line: 99 operations · 41 acting
api_count: 20
apis:
- description: The MediaWiki REST API provides a modern RESTful interface for reading and writing wiki content including pages, revisions, file metadata, search, and content transformation between wikitext and HTML.
  name: MediaWiki REST API
  slug: mediawiki-rest-api
- description: On-demand API
  name: Wikimedia articles API
  slug: wikimedia-articles-api
- description: Realtime Batch API
  name: Wikimedia batches API
  slug: wikimedia-batches-api
- description: generation of citation data
  name: Wikimedia Citation API
  slug: wikimedia-citation-api
- description: Metadata
  name: Wikimedia codes API
  slug: wikimedia-codes-api
- description: Metadata
  name: Wikimedia languages API
  slug: wikimedia-languages-api
- description: formula rendering
  name: Wikimedia Math API
  slug: wikimedia-math-api
- description: The Mobile API from Wikimedia — 3 operation(s) for mobile.
  name: Wikimedia Mobile API
  slug: wikimedia-mobile-api
- description: Metadata
  name: Wikimedia namespaces API
  slug: wikimedia-namespaces-api
- description: The offline API from Wikimedia — 2 operation(s) for offline.
  name: Wikimedia offline API
  slug: wikimedia-offline-api
- description: page content in different formats
  name: Wikimedia Page content API
  slug: wikimedia-page-content-api
- description: Metadata
  name: Wikimedia projects API
  slug: wikimedia-projects-api
- description: Private lists of selected pages
  name: Wikimedia Reading lists API
  slug: wikimedia-reading-lists-api
- description: contribution recommendations
  name: Wikimedia Recommendation API
  slug: wikimedia-recommendation-api
- description: Snapshot API
  name: Wikimedia snapshots API
  slug: wikimedia-snapshots-api
- description: (Beta) Structured Contents On-demand API
  name: Wikimedia structured-contents API
  slug: wikimedia-structured-contents-api
- description: (BETA) Structured Contents Snapshot API
  name: Wikimedia structured-snapshots API
  slug: wikimedia-structured-snapshots-api
- description: The Talk pages API from Wikimedia — 2 operation(s) for talk pages.
  name: Wikimedia Talk pages API
  slug: wikimedia-talk-pages-api
- description: convert content between HTML and Wikitext
  name: Wikimedia Transforms API
  slug: wikimedia-transforms-api
- description: The wikidata API from Wikimedia — 3 operation(s) for wikidata.
  name: Wikimedia wikidata API
  slug: wikimedia-wikidata-api
artifact_total: 123
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wikimedia Enterprise API spec articles API
  slug: open-wikimedia-articles-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles batches API
  slug: open-wikimedia-batches-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Citation API
  slug: open-wikimedia-citation-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles codes API
  slug: open-wikimedia-codes-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles languages API
  slug: open-wikimedia-languages-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Math API
  slug: open-wikimedia-math-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Mobile API
  slug: open-wikimedia-mobile-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles namespaces API
  slug: open-wikimedia-namespaces-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles offline API
  slug: open-wikimedia-offline-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Page content API
  slug: open-wikimedia-page-content-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles projects API
  slug: open-wikimedia-projects-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Reading lists API
  slug: open-wikimedia-reading-lists-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Recommendation API
  slug: open-wikimedia-recommendation-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles snapshots API
  slug: open-wikimedia-snapshots-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles structured-contents API
  slug: open-wikimedia-structured-contents-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles structured-snapshots API
  slug: open-wikimedia-structured-snapshots-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Talk pages API
  slug: open-wikimedia-talk-pages-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles Transforms API
  slug: open-wikimedia-transforms-api
- collection_type: open
  name: Wikimedia Enterprise API spec articles wikidata API
  slug: open-wikimedia-wikidata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wikimedia-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wikimedia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikimedia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wikimedia-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.mediawiki.org/wiki/API:Main_page
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mediawiki.org/wiki/Wikimedia_Terms_of_Use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://foundation.wikimedia.org/wiki/Privacy_policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.wikimediastatus.net/
- group: company
  title: ''
  type: Blog
  url: https://wikimediafoundation.org/news/
- group: operate
  title: ''
  type: Community
  url: https://www.mediawiki.org/wiki/Communication
- group: other
  title: ''
  type: Licensing
  url: https://creativecommons.org/licenses/by-sa/4.0/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mediawiki.org/wiki/API:Tutorial
- group: other
  title: ''
  type: BugTracker
  url: https://phabricator.wikimedia.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wikimedia
created: '2026-06-13'
description: Wikimedia provides REST APIs for accessing Wikipedia, Wikidata, Commons, and other Wikimedia project content including page summaries, search, media files, page revision history, and usage metrics. The suite includes the MediaWiki Action API for bot and edit operations, the MediaWiki REST API for modern content access, and the Wikimedia Enterprise API for commercial-scale high-volume data reuse across 920+ datasets and 360+ languages.
examples:
- key_count: 10
  name: Enterprise Article
  slug: enterprise-article
- key_count: 7
  name: Enterprise Snapshot
  slug: enterprise-snapshot
- key_count: 3
  name: Media List
  slug: media-list
- key_count: 4
  name: Page Revision
  slug: page-revision
- key_count: 18
  name: Page Summary
  slug: page-summary
finops:
- name: Wikimedia Enterprise
  service_category: ''
  slug: wikimedia-enterprise
image: https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Wikimedia-logo.svg/240px-Wikimedia-logo.svg.png
json_schemas:
- name: article
  property_count: 20
  slug: article
- name: article_body
  property_count: 2
  slug: article_body
- name: article_namespace
  property_count: 1
  slug: article_namespace
- name: batch
  property_count: 7
  slug: batch
- name: category
  property_count: 2
  slug: category
- name: citation
  property_count: 3
  slug: citation
- name: code
  property_count: 3
  slug: code
- name: cx_dict
  property_count: 2
  slug: cx_dict
- name: cx_mt
  property_count: 1
  slug: cx_mt
- name: editor
  property_count: 7
  slug: editor
- name: entity
  property_count: 2
  slug: entity
- name: error
  property_count: 2
  slug: error
- name: event
  property_count: 3
  slug: event
- name: filter
  property_count: 2
  slug: filter
- name: image
  property_count: 10
  slug: image
- name: language
  property_count: 4
  slug: language
- name: license
  property_count: 3
  slug: license
- name: link
  property_count: 3
  slug: link
- name: list_entry
  property_count: 5
  slug: list_entry_read
- name: list_entry_write
  property_count: 2
  slug: list_entry_write
- name: list
  property_count: 5
  slug: list_read
- name: list
  property_count: 2
  slug: list_write
- name: listing
  property_count: 2
  slug: listing
- name: maintenance_tags
  property_count: 4
  slug: maintenance_tags
- name: media_item
  property_count: 6
  slug: media_item
- name: media_list
  property_count: 3
  slug: media_list
- name: morelike_result
  property_count: 0
  slug: morelike_result
- name: namespace
  property_count: 3
  slug: namespace
- name: originalimage
  property_count: 3
  slug: originalimage
- name: part
  property_count: 8
  slug: part
- name: problem
  property_count: 4
  slug: problem
- name: project
  property_count: 5
  slug: project
- name: protection
  property_count: 3
  slug: protection
- name: recommendation_result
  property_count: 2
  slug: recommendation_result
- name: redirect
  property_count: 2
  slug: redirect
- name: reference
  property_count: 7
  slug: reference
- name: referenceneed
  property_count: 1
  slug: referenceneed
- name: referencerisk
  property_count: 1
  slug: referencerisk
- name: result
  property_count: 3
  slug: result
- name: revertrisk
  property_count: 2
  slug: revertrisk
- name: revision
  property_count: 2
  slug: revision
- name: revisionIdentifier
  property_count: 2
  slug: revisionIdentifier
- name: revisionInfo
  property_count: 12
  slug: revisionInfo
- name: revisions
  property_count: 1
  slug: revisions
- name: scores
  property_count: 3
  slug: scores
- name: size
  property_count: 2
  slug: size
- name: snapshot
  property_count: 8
  slug: snapshot
- name: structured-content
  property_count: 18
  slug: structured-content
- name: summary
  property_count: 13
  slug: summary
- name: table
  property_count: 4
  slug: table
- name: template
  property_count: 2
  slug: template
- name: thumbnail
  property_count: 3
  slug: thumbnail
- name: titles_set
  property_count: 3
  slug: titles_set
- name: version
  property_count: 9
  slug: version
- name: visibility
  property_count: 3
  slug: visibility
- name: wikidata_article
  property_count: 13
  slug: wikidata_article
- name: wikidata_entity
  property_count: 7
  slug: wikidata_entity
- name: wikidata_entity_property
  property_count: 3
  slug: wikidata_entity_property
- name: wikidata_entity_qualifier
  property_count: 2
  slug: wikidata_entity_qualifier
- name: wikidata_entity_reference_part
  property_count: 2
  slug: wikidata_entity_reference_part
- name: wikidata_entity_statement_reference
  property_count: 2
  slug: wikidata_entity_statement_reference
- name: wikidata_entity_value
  property_count: 4
  slug: wikidata_entity_value
- name: wikidata_labels
  property_count: 0
  slug: wikidata_labels
- name: wikidata_sitelinks
  property_count: 3
  slug: wikidata_sitelinks
- name: wikidata_statement
  property_count: 6
  slug: wikidata_statement
- name: wikidata_statements
  property_count: 0
  slug: wikidata_statements
jsonld:
- class_count: 40
  name: Wikimedia Context
  property_count: 3
  slug: wikimedia-context
layout: provider
modified: '2026-06-13'
name: Wikimedia
nav: Providers
network: true
overview: 'Wikimedia publishes 19 APIs on the [APIs.io](https://apis.io/) network, including articles API, batches API, Citation API, and 16 more. Tagged areas include Wikipedia, Wikimedia, Encyclopedia, Open Knowledge, and Content.


  The Wikimedia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Wikimedia''s developer surface includes authentication, developer portal, engineering blog, getting-started guide, GitHub presence, and 9 more developer resources.'
plans:
- name: Wikimedia Enterprise
  plan_count: 2
  slug: wikimedia-enterprise
random_paper: 3
rate_limits:
- limit_count: 2
  name: Mediawiki Action Api
  slug: mediawiki-action-api
- limit_count: 0
  name: Mediawiki Rest Api
  slug: mediawiki-rest-api
- limit_count: 3
  name: Wikimedia Enterprise Api
  slug: wikimedia-enterprise-api
- limit_count: 0
  name: Wikimedia Rest Api
  slug: wikimedia-rest-api
rules:
- effective_rule_count: 5
  extends: []
  name: Wikimedia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wikimedia-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: 4.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 57.6
    developer_ergonomics: 47.6
    discoverability: 81.5
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wikimedia/refs/heads/main/screenshots/wikimedia-2026-06-20T201454.png
security:
- kind: authentication
  name: Wikimedia Authentication
  slug: wikimedia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wikimedia Domain Security
  slug: wikimedia-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wikimedia Vulnerability Disclosure
  slug: wikimedia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wikimedia
tags:
- Wikipedia
- Wikimedia
- Encyclopedia
- Open Knowledge
- Content
- Search
- Reference
website: https://www.mediawiki.org/wiki/API:Main_page
---
