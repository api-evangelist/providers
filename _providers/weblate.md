---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 102
  human_in_the_loop: 0
  name: Weblate Agentic Access
  operation_count: 177
  slug: weblate-agentic-access
  summary_line: 177 operations · 102 acting
api_count: 21
apis:
- description: Added in version 4.4.1.
  name: Weblate addons API
  slug: weblate-addons-api
- description: The categories API from Weblate — 5 operation(s) for categories.
  name: Weblate categories API
  slug: weblate-categories-api
- description: The changes API from Weblate — 2 operation(s) for changes.
  name: Weblate changes API
  slug: weblate-changes-api
- description: Added in version 4.0.
  name: Weblate component-lists API
  slug: weblate-component-lists-api
- description: The components API from Weblate — 17 operation(s) for components.
  name: Weblate components API
  slug: weblate-components-api
- description: The contributions API from Weblate — 1 operation(s) for contributions.
  name: Weblate contributions API
  slug: weblate-contributions-api
- description: Added in version 4.0.
  name: Weblate groups API
  slug: weblate-groups-api
- description: Notification hooks allow external applications to notify Weblate that the VCS repository has been updated. You can use repository endpoints for projects, components and translations to update individu
  name: Weblate hooks API
  slug: weblate-hooks-api
- description: The languages API from Weblate — 3 operation(s) for languages.
  name: Weblate languages API
  slug: weblate-languages-api
- description: Added in version 4.14.
  name: Weblate memory API
  slug: weblate-memory-api
- description: The metrics API from Weblate — 1 operation(s) for metrics.
  name: Weblate metrics API
  slug: weblate-metrics-api
- description: The projects API from Weblate — 20 operation(s) for projects.
  name: Weblate projects API
  slug: weblate-projects-api
- description: The roles API from Weblate — 2 operation(s) for roles.
  name: Weblate roles API
  slug: weblate-roles-api
- description: The schema API from Weblate — 1 operation(s) for schema.
  name: Weblate schema API
  slug: weblate-schema-api
- description: The screenshots API from Weblate — 5 operation(s) for screenshots.
  name: Weblate screenshots API
  slug: weblate-screenshots-api
- description: Added in version 4.18.
  name: Weblate search API
  slug: weblate-search-api
- description: Many endpoints support displaying statistics for their objects.
  name: Weblate statistics API
  slug: weblate-statistics-api
- description: Added in version 4.4. Listing of the tasks is currently not available.
  name: Weblate tasks API
  slug: weblate-tasks-api
- description: The translations API from Weblate — 10 operation(s) for translations.
  name: Weblate translations API
  slug: weblate-translations-api
- description: A unit is a single piece of a translation which pairs a source string with a corresponding translated string and also contains some related metadata. The term is derived from the Translate Toolkit and
  name: Weblate units API
  slug: weblate-units-api
- description: Added in version 4.0.
  name: Weblate users API
  slug: weblate-users-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weblate-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weblate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weblate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weblate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://weblate.org/en/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.weblate.org/en/latest/api.html
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/WeblateOrg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weblate/
- group: company
  title: ''
  type: Blog
  url: https://weblate.org/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://weblate.org/en/hosting/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.weblate.org/
- group: other
  title: ''
  type: X
  url: https://x.com/WeblateOrg
- group: commercial
  title: ''
  type: Plans
  url: plans/weblate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weblate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weblate-finops.yml
created: '2026-06-13'
description: Weblate is an open-source web-based localization platform that provides a comprehensive REST API for managing translation projects, components, strings, and contributors. The platform enables continuous localization workflows with tight version control integration, supporting Git, GitHub, GitLab, and other VCS systems. Developers can use the API to automate translation management, trigger repository synchronization, retrieve translation statistics, and orchestrate automated translation workflows. Weblate is available as a hosted SaaS service or as a self-hosted open-source deployment.
examples:
- key_count: 2
  name: Weblate Create Unit Example
  slug: weblate-create-unit-example
- key_count: 4
  name: Weblate List Projects Example
  slug: weblate-list-projects-example
- key_count: 2
  name: Weblate Memory Lookup Example
  slug: weblate-memory-lookup-example
- key_count: 2
  name: Weblate Repository Push Example
  slug: weblate-repository-push-example
- key_count: 24
  name: Weblate Translation Statistics Example
  slug: weblate-translation-statistics-example
finops:
- name: Weblate Finops
  service_category: ''
  slug: weblate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weblate.png
json_schemas:
- name: Weblate backup
  property_count: 5
  slug: weblate-backup.schema
- name: Weblate component backup
  property_count: 5
  slug: weblate-component.schema
- name: Weblate Translation Memory Schema
  property_count: 0
  slug: weblate-memory.schema
- name: Weblate Messaging
  property_count: 14
  slug: weblate-messaging.schema
- name: Weblate user data export
  property_count: 3
  slug: weblate-userdata.schema
jsonld:
- class_count: 2
  name: Weblate Context
  property_count: 69
  slug: weblate-context
layout: provider
modified: '2026-06-13'
name: Weblate
nav: Providers
network: true
overview: 'Weblate publishes 21 APIs on the [APIs.io](https://apis.io/) network, including addons API, categories API, changes API, and 18 more. Tagged areas include Localization, Translation, Internationalization, Open Source, and Continuous Localization.


  The Weblate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Weblate''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Weblate Plans Pricing
  plan_count: 10
  slug: weblate-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Weblate Rate Limits
  slug: weblate-rate-limits
rules:
- name: Weblate API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: weblate-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weblate/refs/heads/main/screenshots/weblate-2026-06-20T201333.png
security:
- kind: authentication
  name: Weblate Authentication
  slug: weblate-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Weblate Domain Security
  slug: weblate-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Weblate Vulnerability Disclosure
  slug: weblate-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: weblate
tags:
- Localization
- Translation
- Internationalization
- Open Source
- Continuous Localization
- Version Control
website: https://weblate.org/en/
---
