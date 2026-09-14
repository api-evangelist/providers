---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 2
apis:
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The categories API from Elixir Medical — 2 operation(s) for categories.
  name: Elixir Medical Categories API
  slug: elixir-medical-categories-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The comments API from Elixir Medical — 2 operation(s) for comments.
  name: Elixir Medical Comments API
  slug: elixir-medical-comments-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The media API from Elixir Medical — 4 operation(s) for media.
  name: Elixir Medical Media API
  slug: elixir-medical-media-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The pages API from Elixir Medical — 6 operation(s) for pages.
  name: Elixir Medical Pages API
  slug: elixir-medical-pages-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The posts API from Elixir Medical — 6 operation(s) for posts.
  name: Elixir Medical Posts API
  slug: elixir-medical-posts-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The search API from Elixir Medical — 1 operation(s) for search.
  name: Elixir Medical Search API
  slug: elixir-medical-search-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The statuses API from Elixir Medical — 2 operation(s) for statuses.
  name: Elixir Medical Statuses API
  slug: elixir-medical-statuses-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The tags API from Elixir Medical — 2 operation(s) for tags.
  name: Elixir Medical Tags API
  slug: elixir-medical-tags-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The taxonomies API from Elixir Medical — 2 operation(s) for taxonomies.
  name: Elixir Medical Taxonomies API
  slug: elixir-medical-taxonomies-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The types API from Elixir Medical — 2 operation(s) for types.
  name: Elixir Medical Types API
  slug: elixir-medical-types-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The users API from Elixir Medical — 6 operation(s) for users.
  name: Elixir Medical Users API
  slug: elixir-medical-users-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The wpfm_designations API from Elixir Medical — 2 operation(s) for wpfm_designations.
  name: Elixir Medical Wpfm Designations API
  slug: elixir-medical-wpfm-designations-api
- baseURL: https://elixirmedical.com/wp-json
  baseurl_source: declared
  description: The wpfm_locations API from Elixir Medical — 2 operation(s) for wpfm_locations.
  name: Elixir Medical Wpfm Locations API
  slug: elixir-medical-wpfm-locations-api
artifact_total: 18
collections:
- collection_type: open
  name: Elixir Medical Website Content API (WordPress REST wp/v2)
  slug: open-elixir-medical-wordpress-content
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/elixir-medical-wordpress-content-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elixir-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elixirmedical.com/
- group: company
  title: ''
  type: About
  url: https://elixirmedical.com/us/about-us/
- group: operate
  title: ''
  type: Support
  url: https://elixirmedical.com/us/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://elixirmedical.com/ous/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elixirmedical.com/us/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elixirmedical.com/us/terms-of-use/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/elixir-medical_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elixir-medical-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elixir-medical-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elixir-medical-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elixir-medical-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elixir-medical-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elixir-medical-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elixir-medical-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elixir-medical-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elixir-medical-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: Elixir Medical Corporation is a privately held medical device company headquartered in Milpitas, California, developing implant and interventional platforms for coronary and peripheral artery disease. Its DynamX sirolimus-eluting coronary bioadaptor is designed to restore vessel pulsatility and compliance rather than permanently cage the artery, and holds a European CE mark, Japanese PMDA approval and a U.S. FDA Breakthrough Device designation; the LithiX Hertz Contact intravascular lithotripsy system and the DESyne family of drug-eluting stents round out the portfolio. Elixir Medical operates no developer program and publishes no product, device or clinical API. The only machine-readable surface it serves is the default WordPress REST API of its corporate marketing site, alongside an SEO-plugin-generated llms.txt.
image: https://elixirmedical.com/wp-content/uploads/2023/09/New-Elixir-Logo.png
layout: provider
modified: '2026-08-12'
name: Elixir Medical
nav: Providers
network: true
overview: 'Elixir Medical publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Categories API, Comments API, Media API, and 10 more. Tagged areas include Company, Medical Devices, Health, Cardiovascular, and Coronary Intervention.


  Elixir Medical''s developer surface includes support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Elixir Medical Plans Pricing
  plan_count: 0
  slug: elixir-medical-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Elixir Medical Rate Limits
  slug: elixir-medical-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/elixir-medical/refs/heads/main/screenshots/elixir-medical-2026-09-02T145342.png
security:
- kind: authentication
  name: Elixir Medical Authentication
  slug: elixir-medical-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Elixir Medical Domain Security
  slug: elixir-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: elixir-medical
tags:
- Company
- Medical Devices
- Health
- Cardiovascular
- Coronary Intervention
- Implants
- Life Sciences
- Content
- WordPress
website: https://elixirmedical.com/
---
