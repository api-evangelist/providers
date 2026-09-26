---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/security/sound-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sound-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/security/sound-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sound-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/well-known/sound-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sound-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/well-known/sound-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sound-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/security/sound-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sound-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/packages/sound-packages.yml
  title: ''
  type: Packages
  url: packages/sound-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/plans/sound-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sound-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/rate-limits/sound-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sound-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sound/refs/heads/main/llms/sound-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sound-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.sound.ag/
- group: company
  title: ''
  type: About
  url: https://www.sound.ag/about
- group: other
  title: ''
  type: Products
  url: https://www.sound.ag/sound-solutions
- group: other
  title: ''
  type: Science
  url: https://www.sound.ag/our-science
- group: company
  title: ''
  type: Blog
  url: https://www.sound.ag/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.sound.ag/news
- group: other
  title: ''
  type: Whitepapers
  url: https://www.sound.ag/whitepapers
- group: operate
  title: ''
  type: FAQ
  url: https://www.sound.ag/faq
- group: operate
  title: ''
  type: Support
  url: https://www.sound.ag/contact
- group: company
  title: ''
  type: Careers
  url: https://www.sound.ag/careers
- group: other
  title: ''
  type: Sustainability
  url: https://www.sound.ag/sustainability
- group: start
  title: ''
  type: DealerPortal
  url: https://dealerportal.sound.ag/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soundag
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sound-agriculture/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sound.ag/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sound.ag/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sound_stock/
coverage:
  checked: '2026-09-18'
  detail: Sound Agriculture sells physical crop-nutrition biologicals (SOURCE, BLUEPRINT, INFLECT) through dealers and runs a plant-breeding lab; its whole public surface is a Craft CMS marketing site whose API-shaped paths 404, its api./developer./docs. subdomains are a wildcard CNAME to Pardot with no TLS certificate, its only authenticated host is a Salesforce Experience Cloud dealer portal that 302s to /login, and its GitHub org holds lab-automation code and a Postman collection for Leaf Agriculture's API rather than any Sound API.
  evidence:
  - status: 404
    url: https://www.sound.ag/openapi.json
  - status: 404
    url: https://www.sound.ag/api
  - status: 404
    url: https://www.sound.ag/graphql
  - status: 404
    url: https://www.sound.ag/llms.txt
  - status: 404
    url: https://www.sound.ag/.well-known/agent-card.json
  - status: 404
    url: https://www.sound.ag/.well-known/agent.json
  - status: 302
    url: https://dealerportal.sound.ag/api
  - status: 200
    url: https://dealerportal.sound.ag/.well-known/openid-configuration
  - status: 200
    url: https://www.sound.ag/.well-known/security.txt
  - status: 200
    url: https://github.com/soundag
  - status: 200
    url: https://www.sound.ag/
  - status: 403
    url: https://forgeglobal.com/sound_stock/
  reason: not-a-software-company
  state: none
created: '2026-09-18'
description: 'Sound Agriculture is an Emeryville, California agriculture company founded in 2013 by Eric Davidson and Travis Bayer that sells nature-based crop nutrition products to row-crop growers through an independent dealer network: SOURCE, a foliar-applied soil activator that stimulates soil microbes to supply nitrogen and phosphorus; BLUEPRINT, an arbuscular mycorrhizal fungi inoculant; and INFLECT. It also runs an on-demand breeding program that tunes plant gene expression epigenetically without editing DNA. Sound Agriculture is not a software company and publishes no developer program, API, SDK or machine-readable contract; its only authenticated surface is a Salesforce Experience Cloud dealer portal at dealerportal.sound.ag.'
image: https://soundag-usa-production.imgix.net/assets/general/sound-agriculture-seo-image.jpg?w=1200
layout: provider
modified: '2026-09-18'
name: Sound Agriculture
nav: Providers
network: true
overview: 'Sound Agriculture is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Biologicals, and Crop Nutrition.


  Sound Agriculture''s developer surface includes engineering blog, FAQ, support, and 23 more developer resources.'
plans:
- name: Sound Plans Pricing
  plan_count: 0
  slug: sound-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Sound Rate Limits
  slug: sound-rate-limits
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 49.1
    operational_transparency: 13.2
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sound Domain Security
  slug: sound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sound Vulnerability Disclosure
  slug: sound-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sound
tags:
- Company
- Agriculture
- AgTech
- Biologicals
- Crop Nutrition
- Soil Health
- Fertilizer
- Plant Breeding
- Sustainability
website: https://www.sound.ag/
---
