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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eclipse Agentic Access
  operation_count: 8
  slug: eclipse-agentic-access
  summary_line: 8 operations
api_count: 13
apis:
- description: REST API for accessing Eclipse Marketplace data including listings, categories, favorites, and installation statistics for plugins, IDEs, and other extensions.
  name: Eclipse Marketplace API
  slug: marketplace-api
- description: Foundation-wide REST APIs for accessing project data, releases, committer paperwork, GeoIP, downloads, mailing lists, profiles, working groups, and other Eclipse Foundation services. Index of availabl
  name: Eclipse Foundation Web API
  slug: foundation-web-api
- description: REST API exposing Eclipse Foundation project metadata, releases, committers, and project lifecycle data.
  name: Eclipse Projects API
  slug: projects-api
- description: REST API for the Eclipse Open VSX Registry, an open-source alternative to the Visual Studio Marketplace for distributing VS Code-compatible extensions.
  name: Open VSX Registry API
  slug: open-vsx-api
- description: REST API providing access to news, events, and announcements from the Eclipse Foundation newsroom.
  name: Eclipse Newsroom REST API
  slug: newsroom-api
- description: The Eclipse Marketplace REST API API from Eclipse Foundation — 1 operation(s) for eclipse marketplace rest api.
  name: Eclipse Foundation Eclipse Marketplace REST API API
  slug: eclipse-eclipse-marketplace-rest-api-api
- description: The Favorites API from Eclipse Foundation — 1 operation(s) for favorites.
  name: Eclipse Foundation Favorites API
  slug: eclipse-favorites-api
- description: The Featured API from Eclipse Foundation — 1 operation(s) for featured.
  name: Eclipse Foundation Featured API
  slug: eclipse-featured-api
- description: The Node API from Eclipse Foundation — 1 operation(s) for node.
  name: Eclipse Foundation Node API
  slug: eclipse-node-api
- description: The Popular API from Eclipse Foundation — 1 operation(s) for popular.
  name: Eclipse Foundation Popular API
  slug: eclipse-popular-api
- description: The Recent API from Eclipse Foundation — 1 operation(s) for recent.
  name: Eclipse Foundation Recent API
  slug: eclipse-recent-api
- description: The Search API from Eclipse Foundation — 1 operation(s) for search.
  name: Eclipse Foundation Search API
  slug: eclipse-search-api
- description: The Taxonomy API from Eclipse Foundation — 1 operation(s) for taxonomy.
  name: Eclipse Foundation Taxonomy API
  slug: eclipse-taxonomy-api
artifact_total: 20
collections:
- collection_type: open
  name: Eclipse Marketplace REST API
  slug: open-eclipse
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eclipse-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eclipse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eclipse-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eclipse-foundation
- group: start
  title: ''
  type: Portal
  url: https://www.eclipse.org/
- group: docs
  title: ''
  type: API Documentation Index
  url: https://webdev.eclipse.org/docs/api/
- group: company
  title: ''
  type: Blog
  url: https://blogs.eclipse.org/
- group: company
  title: ''
  type: News
  url: https://newsroom.eclipse.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/eclipse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eclipse.org/legal/termsofuse.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eclipse.org/legal/privacy.php
- group: commercial
  title: ''
  type: License
  url: https://www.eclipse.org/legal/epl-2.0/
created: '2024-01-01'
description: The Eclipse Foundation provides a global community of individuals and organizations with a mature, scalable, and business-friendly environment for open source software collaboration and innovation. This index aggregates the developer-facing APIs and services published by the Eclipse Foundation and its working groups.
finops:
- name: Eclipse Finops
  service_category: API
  slug: eclipse-finops
image: https://www.eclipse.org/eclipse.org-common/themes/solstice/public/images/logo/eclipse-foundation-grey-orange.svg
layout: provider
modified: '2026-04-28'
name: Eclipse Foundation
nav: Providers
network: true
overview: 'Eclipse Foundation publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Eclipse Marketplace REST API API, Favorites API, Featured API, and 5 more. Tagged areas include Eclipse Foundation, Foundation, Open Source, and Standards.


  Eclipse Foundation''s developer surface includes developer portal, engineering blog, product news, and 9 more developer resources.'
plans:
- name: Eclipse Plans Pricing
  plan_count: 3
  slug: eclipse-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Eclipse Rate Limits
  slug: eclipse-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 45.1
    developer_ergonomics: 10.9
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eclipse/refs/heads/main/screenshots/eclipse-2026-06-20T180424.png
security:
- kind: domain-security
  name: Eclipse Domain Security
  slug: eclipse-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eclipse Vulnerability Disclosure
  slug: eclipse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eclipse
tags:
- Eclipse Foundation
- Foundation
- Open Source
- Standards
website: https://www.eclipse.org/
---
