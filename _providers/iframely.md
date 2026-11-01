---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/iframely/plans/iframely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iframely-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.iframely.com/
- group: design
  href: https://artifacts.apis.io/iframely/errors/iframely-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/iframely-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/iframely/llms/iframely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iframely-llms.txt
- group: other
  href: https://artifacts.apis.io/iframely/hosts/iframely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iframely-hosts.yml
- group: build
  href: https://artifacts.apis.io/iframely/packages/iframely-packages.yml
  title: ''
  type: SDKs
  url: packages/iframely-packages.yml
- group: build
  href: https://artifacts.apis.io/iframely/packages/iframely-packages.yml
  title: ''
  type: Packages
  url: packages/iframely-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://iframely.com/signup
- group: auth
  title: ''
  type: Security
  url: https://iframely.com/legal/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://iframely.com/domains/changelog
- group: auth
  href: https://artifacts.apis.io/iframely/security/iframely-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/iframely-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/iframely/security/iframely-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/iframely-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/iframely/security/iframely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iframely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iframely.com/
- group: docs
  title: ''
  type: Documentation
  url: https://iframely.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://iframely.com/docs/data-api
- group: start
  title: ''
  type: GettingStarted
  url: https://iframely.com/docs/iframely-api
- group: operate
  title: ''
  type: Support
  url: https://iframely.com/help
- group: company
  title: ''
  type: Blog
  url: https://iframely.com/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://iframely.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iframely.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iframely.com/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://iframely.com/docs/data-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Iframely provides a service that transforms URLs into rich media embeds, previews, and structured data. Since 2012 it offers a single API that extracts information from a wide range of web content, enabling publishers and developers to embed videos, podcasts, images, social posts, and other media types into their applications. The platform supports thousands of domains and includes features such as customizable embed layouts, analytics, and compliance with privacy regulations. Iframely is used by products that need to display rich previews of shared URLs, helping to improve user engagement and content presentation.
image: https://iframely.com/_app/immutable/assets/thumbnail.CpT0ve9n.png
layout: provider
modified: '2026-10-27'
name: Iframely
nav: Providers
network: true
overview: 'Iframely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Embeds, Media, API, URL, and Content.


  Iframely''s developer surface includes signup flow, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Iframely Plans Pricing
  plan_count: 5
  slug: iframely-plans-pricing
random_paper: 17
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Iframely Domain Security
  slug: iframely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Iframely Vulnerability Disclosure
  slug: iframely-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Iframely Trust Center
  slug: iframely-trust-center
  summary_line: SOC 2
slug: iframely
tags:
- Embeds
- Media
- API
- URL
- Content
website: https://iframely.com/
---
