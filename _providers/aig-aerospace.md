---
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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-18'
api_count: 0
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.aig.com/home/risk-solutions/business/specialty-risks/aviation
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.com/home/risk-solutions/business/specialty-risks/aerospace-and-aviation/airline
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.com/home/risk-solutions/business/specialty-risks/aerospace-and-aviation/unmanned-aircraft-systems
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.co.uk/home/risk-solutions/business/aviation
- group: operate
  title: ''
  type: Support
  url: https://www.aig.com/home/claims/report-a-claim/specialty-aerospace
- group: start
  title: ''
  type: Portal
  url: https://www-249.aig.com/
- group: start
  title: ''
  type: Portal
  url: https://www.myaig.com
- group: operate
  title: ''
  type: Support
  url: https://www.aig.com/home/contact
- group: docs
  title: ''
  type: Documentation
  url: https://www.aig.com/content/dam/aig/america-canada/us/documents/business/highlight-sheet/aig-aerospace-highlight-sheet.pdf
- group: company
  title: ''
  type: Blog
  url: https://www.aig.com/home/newsroom/stories
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aig
- group: auth
  title: ''
  type: Security
  url: https://www.aig.com/home/about/cyber-and-information-security/vulnerability-disclosure
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aig.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aig.com/terms-of-use
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/security/aig-aerospace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aig-aerospace-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/security/aig-aerospace-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aig-aerospace-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/llms/aig-aerospace-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aig-aerospace-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/plans/aig-aerospace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aig-aerospace-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/rate-limits/aig-aerospace-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aig-aerospace-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aig-aerospace/refs/heads/main/packages/aig-aerospace-packages.yml
  title: ''
  type: Packages
  url: packages/aig-aerospace-packages.yml
coverage:
  checked: '2026-09-14'
  detail: AIG Aerospace is a specialty-insurance line inside American International Group, not a software business — its whole public surface is the aviation pages on aig.com plus ten PDF application forms, quoting and binding happen through appointed brokers, and no AIG host served an OpenAPI, a /.well-known/ document or any developer portal when probed (AIG's own former portal host www.developers.aig.com refuses TCP connections on 443).
  evidence:
  - status: 200
    url: https://www.aig.com/home/risk-solutions/business/specialty-risks/aviation
  - status: 404
    url: https://www.aig.com/openapi.json
  - status: 0
    url: https://www.developers.aig.com/apis
  - status: 403
    url: https://www.aig.com/.well-known/api-catalog
  - status: 404
    url: https://developer.aig.com/
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: 'AIG Aerospace is the aviation and aerospace specialty insurance business of American International Group, Inc. (AIG), underwriting hull and liability cover for airlines, general aviation owners and operators, aircraft and component manufacturers, MRO and distribution businesses, airports, ground handlers and service providers, and unmanned aircraft systems, backed by dedicated aerospace claims adjusters and aviation attorneys on a 24/7 hotline. It is a line of business rather than a software company: it publishes no developer portal, no OpenAPI or other machine-readable contract, no SDK, no webhooks and no self-service signup. Its public surface is marketing pages on aig.com plus PDF application forms; quoting and binding run through appointed brokers and claims through authenticated AIG portals. AIG''s one API gateway, commercial.api.aig.com, is contract-only, serves the parent''s broker applications rather than aerospace, and is profiled at api-evangelist/aig.'
features:
- description: Up to 15% of a $2.5B limit of liability on airline risks in a leading or following position, for operators from small scheduled charter to international wide-body.
  name: Airline Hull & Liability
- description: Hull and liability for owners, operators and aircraft management companies, up to $100M agreed hull value and $650M liability limits.
  name: General Aviation
- description: Aerospace product liability for manufacturers, distributors, and maintenance, repair and overhaul operations.
  name: Aviation Product Liability
- description: Liability cover for airport operators, fixed-base operators, ground handlers and aviation service providers.
  name: Airports, Ground Handlers & Service Providers
- description: Physical damage and third-party liability written for drone and UAS exposures, with a dedicated application form.
  name: Unmanned Aircraft Systems
- description: Dedicated aerospace adjusters and aviation attorneys on a 24/7 hotline, with the AIG Claims Promise advancing 50% of AIG's share within 7 days of confirmed coverage and ownership.
  name: Aerospace Claims
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aig.png
layout: provider
modified: '2026-09-14'
name: AIG Aerospace
nav: Providers
network: true
overview: 'AIG Aerospace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Aviation, Aerospace, Specialty Insurance, and Property Casualty.


  AIG Aerospace''s developer surface includes documentation, support, developer portal, engineering blog, and 16 more developer resources.'
plans:
- name: Aig Aerospace Plans Pricing
  plan_count: 0
  slug: aig-aerospace-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Aig Aerospace Rate Limits
  slug: aig-aerospace-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 10.5
  previous_composite: 16.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 30.3
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aig Aerospace Domain Security
  slug: aig-aerospace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aig Aerospace Vulnerability Disclosure
  slug: aig-aerospace-vulnerability-disclosure
  summary_line: Hackerone
slug: aig-aerospace
tags:
- Insurance
- Aviation
- Aerospace
- Specialty Insurance
- Property Casualty
- Claims
- Unmanned Aircraft
- Enterprise
website: https://www.aig.com/home/risk-solutions/business/specialty-risks/aviation
---
