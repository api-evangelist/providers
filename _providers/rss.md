---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: 'RSS 2.0 is the dominant XML-based syndication format, stewarded by the RSS Advisory Board. A feed consists of a root <rss version="2.0"> element wrapping a single <channel> with required title, link, '
  name: RSS 2.0
  slug: rss-2-0
- description: 'Atom 1.0, defined by IETF RFC 4287, is an XML-based syndication format developed as a more rigorously specified alternative to RSS 2.0. An Atom feed (atom:feed) contains required atom:id, atom:title, '
  name: Atom 1.0
  slug: atom-1-0
- description: JSON Feed 1.1 is a JSON-based syndication format created by Brent Simmons and Manton Reece as a developer-friendly alternative to RSS and Atom. A JSON Feed has top-level version, title, and items, wit
  name: JSON Feed 1.1
  slug: json-feed-1-1
- description: 'The RSS Best Practices Profile is the RSS Advisory Board''s normative guidance on producing RSS feeds that interoperate cleanly across the diverse population of feed readers. It covers character data, '
  name: RSS Best Practices Profile
  slug: rss-best-practices-profile
- description: 'OPML (Outline Processor Markup Language) 2.0 is an XML format for outlines, most commonly used to exchange lists of RSS/Atom feed subscriptions between feed readers. A subscription list OPML file has '
  name: OPML 2.0
  slug: opml-2-0
- description: Feed autodiscovery is the HTML convention by which a web page advertises the location of its RSS, Atom, or JSON Feed using a <link rel="alternate" type="application/rss+xml" href="..."> element in the
  name: Feed Autodiscovery
  slug: feed-autodiscovery
artifact_total: 23
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rssboard.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rssboard.org/rss-specification
- group: other
  title: ''
  type: BestPractices
  url: https://www.rssboard.org/rss-profile
- group: other
  title: ''
  type: Validator
  url: https://www.rssboard.org/rss-validator/
- group: company
  title: ''
  type: Blog
  url: https://www.rssboard.org/news
- group: docs
  title: ''
  type: AtomSpecification
  url: https://datatracker.ietf.org/doc/html/rfc4287
- group: docs
  title: ''
  type: JSONFeedSpecification
  url: https://www.jsonfeed.org/version/1.1/
- group: docs
  title: ''
  type: OPMLSpecification
  url: http://opml.org/spec2.opml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/rss-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rss-vocabulary.yml
created: '2025-01-01'
description: RSS (Really Simple Syndication) is the canonical XML feed format family for publishing and subscribing to streams of frequently updated content — blogs, news, podcasts, and other periodic resources. The RSS family in this index covers RSS 2.0 (stewarded by the RSS Advisory Board), Atom 1.0 (RFC 4287), JSON Feed 1.1, the RSS Best Practices Profile, OPML 2.0 for feed subscription lists, and HTML autodiscovery conventions used by feed readers to locate feeds from a site's homepage.
examples:
- key_count: 2
  name: Atom Feed Example
  slug: atom-feed-example
- key_count: 6
  name: Feed Autodiscovery Example
  slug: feed-autodiscovery-example
- key_count: 12
  name: Json Feed Example
  slug: json-feed-example
- key_count: 4
  name: Opml Subscription List Example
  slug: opml-subscription-list-example
- key_count: 2
  name: Rss Channel Example
  slug: rss-channel-example
- key_count: 11
  name: Rss Item Example
  slug: rss-item-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rss.png
json_schemas:
- name: Atom 1.0 Entry
  property_count: 12
  slug: atom-entry
- name: Atom 1.0 Feed
  property_count: 13
  slug: atom-feed
- name: JSON Feed 1.1 Item
  property_count: 15
  slug: json-feed-item
- name: JSON Feed 1.1
  property_count: 14
  slug: json-feed
- name: OPML 2.0 Subscription List
  property_count: 3
  slug: opml-subscription-list
- name: RSS 2.0 Channel
  property_count: 20
  slug: rss-channel
- name: RSS 2.0 Item
  property_count: 10
  slug: rss-item
json_structures:
- name: Rss Channel Structure
  property_count: 0
  slug: rss-channel-structure
jsonld:
- class_count: 0
  name: Rss Context
  property_count: 65
  slug: rss-context
layout: provider
modified: '2026-05-23'
name: RSS
nav: Providers
network: true
overview: 'RSS publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Syndication, RSS, Atom, JSON Feed, and OPML.


  The RSS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  RSS''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 38
rules:
- name: RSS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rss-jsonschema-spectral-rules
score:
  band: emerging
  composite: 29.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 34.0
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 0.0
  previous_composite: 29.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rss/refs/heads/main/screenshots/rss-2026-06-20T193237.png
security:
- kind: domain-security
  name: Rss Domain Security
  slug: rss-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: rss
tags:
- Syndication
- RSS
- Atom
- JSON Feed
- OPML
- Content
- XML
- Specification
- Standard
website: https://www.rssboard.org/
---
