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
api_count: 2
apis:
- description: The core jQuery API for DOM manipulation, event handling, AJAX, effects, animation, and other JavaScript utilities. Documents selectors, methods, and events for working with the DOM in a cross-browser
  name: jQuery Core API
  slug: jquery-core-api
- description: Content Delivery Network endpoints for serving jQuery and related plugin library files (jQuery, jQuery UI, jQuery Mobile, QUnit, Color, PEP) over HTTPS for direct inclusion in web pages.
  name: jQuery CDN
  slug: jquery-cdn
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jquery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jquery.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.jquery.com
- group: company
  title: ''
  type: Blog
  url: https://blog.jquery.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jquery
- group: build
  title: ''
  type: Source Code
  url: https://github.com/jquery/jquery
- group: commercial
  title: ''
  type: License
  url: https://github.com/jquery/jquery/blob/main/LICENSE.txt
- group: operate
  title: ''
  type: Issues
  url: https://github.com/jquery/jquery/issues
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/jquery
- group: other
  title: ''
  type: Contributing
  url: https://contribute.jquery.org
- group: operate
  title: ''
  type: Community
  url: https://forum.jquery.com
created: '2024-01-01'
description: jQuery is a fast, small, and feature-rich JavaScript library that makes HTML document traversal and manipulation, event handling, animation, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers. Only about 30kB minified and gzipped, available as an AMD module, and CSS3 compliant. jQuery 4.0 is the current release; jQuery 3.x receives critical updates only.
finops:
- name: Jquery Finops
  service_category: API
  slug: jquery-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jquery.png
layout: provider
modified: '2026-04-28'
name: jQuery
nav: Providers
network: true
overview: 'jQuery publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AJAX, DOM Manipulation, Front-End, JavaScript, and Library.


  jQuery''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Jquery Plans Pricing
  plan_count: 3
  slug: jquery-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Jquery Rate Limits
  slug: jquery-rate-limits
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jquery/refs/heads/main/screenshots/jquery-2026-06-20T183810.png
security:
- kind: domain-security
  name: Jquery Domain Security
  slug: jquery-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jquery
tags:
- AJAX
- DOM Manipulation
- Front-End
- JavaScript
- Library
website: https://jquery.com
---
