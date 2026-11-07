---
access_model:
  confidence: high
  label: Discontinued — no plans, signup or API
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probe
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: company
  title: ''
  type: Blog
  url: https://www.leanix.net/en/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.leanix.net/en/blog/rss.xml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/leanix/
- group: company
  title: ''
  type: Website
  url: https://www.leanix.net/en/
- group: other
  title: ''
  type: Acquirer
  url: https://www.leanix.net/en/
- group: other
  title: ''
  type: Acquisition Announcement
  url: https://www.leanix.net/en/company/press/leanix-acquire-saas-management-provider-cleanshelf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleanshelf
- group: agent
  href: https://artifacts.apis.io/cleanshelf/well-known/cleanshelf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cleanshelf-well-known.yml
- group: auth
  href: https://artifacts.apis.io/cleanshelf/well-known/cleanshelf-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cleanshelf-security.txt
- group: auth
  href: https://artifacts.apis.io/cleanshelf/security/cleanshelf-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/cleanshelf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cleanshelf/security/cleanshelf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cleanshelf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cleanshelf/security/cleanshelf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanshelf-domain-security.yml
- group: design
  href: https://artifacts.apis.io/cleanshelf/lifecycle/cleanshelf-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cleanshelf-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/cleanshelf/lifecycle/cleanshelf-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/cleanshelf-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cleanshelf/conformance/cleanshelf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleanshelf-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cleanshelf/llms/cleanshelf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleanshelf-llms.txt
- group: commercial
  href: https://artifacts.apis.io/cleanshelf/plans/cleanshelf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cleanshelf-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cleanshelf/rate-limits/cleanshelf-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cleanshelf-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cleanshelf/json-ld/cleanshelf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cleanshelf-context.jsonld
- group: design
  href: https://artifacts.apis.io/cleanshelf/rules/cleanshelf-rules.yml
  title: ''
  type: Spectral
  url: rules/cleanshelf-rules.yml
coverage:
  checked: '2026-09-05'
  detail: 'Cleanshelf was acquired by LeanIX on 24 March 2021 and relaunched as LeanIX SaaS Intelligence, and the brand is now fully absorbed — cleanshelf.com and www.cleanshelf.com 301 to www.leanix.net behind a certificate issued to O=SAP SE, CN=leanix.info with sap.de nameservers, api/app/docs.cleanshelf.com return NXDOMAIN, and the only document either host still serves is an expired RFC 9116 security.txt whose contact is SAP''s vulnerability reporting page. A first-party source and package sweep found nothing either: there is no cleanshelf GitHub organization (404) and no package named cleanshelf on npm, PyPI, RubyGems, crates.io, Packagist, NuGet or Maven Central, so no SDK, CLI or client library survives the shutdown to profile.'
  evidence:
  - status: 301
    url: https://cleanshelf.com/
  - status: 301
    url: https://www.cleanshelf.com/
  - status: 200
    url: https://cleanshelf.com/.well-known/security.txt
  - status: 301
    url: https://cleanshelf.com/openapi.json
  - status: 301
    url: https://cleanshelf.com/.well-known/api-catalog
  - status: 301
    url: https://cleanshelf.com/.well-known/agent-card.json
  - status: 200
    url: https://www.leanix.net/en/company/press/leanix-acquire-saas-management-provider-cleanshelf
  - status: 404
    url: https://api.github.com/orgs/cleanshelf
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=cleanshelf
  - status: 404
    url: https://pypi.org/pypi/cleanshelf/json
  - status: 301
    url: https://cleanshelf.com/llms.txt
  reason: defunct
  state: none
created: '2026-03-27'
deprecated: true
deprecated_note: Cleanshelf was acquired by LeanIX on 24 March 2021 and its technology was relaunched on 1 May 2021 as LeanIX SaaS Intelligence. LeanIX was subsequently acquired by SAP. cleanshelf.com now 301-redirects to www.leanix.net and is served from SAP infrastructure; the Cleanshelf product, brand and API no longer exist independently.
description: Cleanshelf was a San Francisco enterprise SaaS management platform that discovered and inventoried an organization's SaaS applications, optimized software licenses, tracked subscription spend, and surfaced shadow IT. At acquisition it claimed more than 3,000 integrations and managed roughly $700 million in SaaS spend for its customers. LeanIX acquired Cleanshelf on 24 March 2021 and relaunched the technology on 1 May 2021 as LeanIX SaaS Intelligence, with SaaS discovery and cataloging folded into the LeanIX Application Portfolio Management module; LeanIX itself was later acquired by SAP. Cleanshelf publishes no API, developer portal or documentation of its own today — cleanshelf.com 301-redirects to www.leanix.net and its former api, app and docs hostnames no longer resolve. The successor API surface is profiled separately under the LeanIX record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cleanshelf.png
jsonld:
- class_count: 13
  name: Cleanshelf Context
  property_count: 0
  slug: cleanshelf-context
layout: provider
modified: '2026-10-06'
name: Cleanshelf
nav: Providers
network: true
overview: 'Cleanshelf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, License Management, SaaS Management, Shadow IT, and SMP.


  The Cleanshelf catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cleanshelf''s developer surface includes engineering blog and 19 more developer resources.'
plans:
- name: Cleanshelf Plans Pricing
  plan_count: 0
  slug: cleanshelf-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Cleanshelf Rate Limits
  slug: cleanshelf-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Cleanshelf API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: cleanshelf-rules
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 38.8
    catalog_earned_first_party: 0.0
    catalog_gap: 76.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 11.4
    contract_quality: 10.7
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 18.4
  previous_composite: 12.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cleanshelf/cleanshelf-2026-06-20T174453.png
security:
- kind: domain-security
  name: Cleanshelf Domain Security
  slug: cleanshelf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cleanshelf Vulnerability Disclosure
  slug: cleanshelf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cleanshelf
tags:
- Acquired
- License Management
- SaaS Management
- Shadow IT
- SMP
- Software Asset Management
- Spend Optimization
website: https://www.leanix.net/en/
---
