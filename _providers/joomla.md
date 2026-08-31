---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The built-in Joomla Web Services API provides RESTful JSON endpoints for managing articles, categories, contacts, banners, menus, modules, tags, custom fields, and user accounts in a Joomla installati
  name: Joomla Web Services API
  slug: joomla-web-services-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/joomla-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joomla-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joomla.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joomla.org/J4.x:Joomla_Core_APIs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/joomla
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/joomla
- group: company
  title: ''
  type: Blog
  url: https://community.joomla.org/blogs.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joomla.org/download.html
- group: other
  title: ''
  type: X
  url: https://twitter.com/joomla
- group: commercial
  title: ''
  type: Plans
  url: plans/joomla-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/joomla-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/joomla-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/joomla.json
created: 2026-06-13
description: Joomla is a free and open-source content management system (CMS) built in PHP that includes a built-in REST API for managing core content types. The Web Services API provides JSON endpoints for articles, categories, contacts, banners, menus, modules, tags, fields, and user accounts. Authentication is handled via Bearer tokens with optional HMAC security, and every endpoint requires authentication unless explicitly marked public. Joomla is maintained entirely by volunteers and released under the GNU General Public License.
finops:
- name: Joomla Finops
  service_category: ''
  slug: joomla-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/joomla.png
layout: provider
modified: 2026-06-13
name: Joomla
nav: Providers
network: true
overview: 'Joomla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, Open-Source, PHP, and REST API.


  Joomla''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Joomla Plans Pricing
  plan_count: 1
  slug: joomla-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Joomla Rate Limits
  slug: joomla-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/joomla/refs/heads/main/screenshots/joomla-2026-06-20T183801.png
security:
- kind: domain-security
  name: Joomla Domain Security
  slug: joomla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Joomla Vulnerability Disclosure
  slug: joomla-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: joomla
tags:
- CMS
- Content Management
- Open-Source
- PHP
- REST API
- Articles
- Categories
- Contacts
- Menus
- Modules
- User
website: https://www.joomla.org
---
