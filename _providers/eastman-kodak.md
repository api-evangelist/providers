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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
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
  schema_version: 0.2
  score: 13.3
  scored_at: '2026-09-07'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eastman-kodak-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eastman-kodak-well-known.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eastman-kodak-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eastman-kodak-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eastman-kodak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eastman-kodak-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/eastman-kodak-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eastman-kodak-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://workflowhelp.kodak.com/display/DOC/Workflow+Documentation
- group: operate
  title: ''
  type: Support
  url: https://www.kodak.com/en/print/page/support/
- group: company
  title: ''
  type: Blog
  url: https://www.kodak.com/en/company/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kodak.com/en/company/page/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kodak.com/en/company/page/site-terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eastman-kodak
- group: company
  title: ''
  type: Website
  url: https://www.kodak.com/en/
- group: company
  title: ''
  type: About
  url: https://www.kodak.com/en/company/home/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.kodak.com/en/company/press-releases/
- group: operate
  title: ''
  type: Contact
  url: https://www.kodak.com/en/company/page/contact-us/
coverage:
  checked: '2026-09-06'
  detail: Kodak ships real software (PRINERGY Workflow, PRINERGY On Demand, ColorFlow, InSite) and even names four of its own cloud APIs in public documentation, but only as firewall allow-list entries on obfuscated Azure hosts that answer 403 to the public, and no developer portal, API reference, SDK or machine-readable contract exists anywhere on kodak.com.
  evidence:
  - status: 0
    url: https://developer.kodak.com/
  - status: 0
    url: https://api.kodak.com/
  - status: 404
    url: https://www.kodak.com/llms.txt
  - status: 403
    url: https://agentncw6dbzhv4klo.azurewebsites.net/
  - status: 200
    url: https://workflowhelp.kodak.com/display/POD/Prinergy+Cloud+Connectivity
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Eastman Kodak Company is a global commercial printing and imaging company that provides hardware, software, consumables, and services to customers in the print, packaging, publishing, manufacturing, and entertainment industries. Kodak does not currently publish a public developer program or API portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eastman-kodak.png
layout: provider
modified: '2026-09-06'
name: Eastman Kodak
nav: Providers
network: true
overview: 'Eastman Kodak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Printing, Imaging, Packaging, Manufacturing, and Print Workflow.


  Eastman Kodak''s developer surface includes changelog, documentation, support, engineering blog, and 14 more developer resources.'
plans:
- name: Eastman Kodak Plans Pricing
  plan_count: 0
  slug: eastman-kodak-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases
  url: https://www.kodak.com/en/company/press-releases/
- date: '2026-05-25'
  title: Kodak posts Q1 2026 revenue of $265 million | KODK 8-K ...
  url: https://www.stocktitan.net/sec-filings/KODK/8-k-eastman-kodak-co-reports-material-event-b02bd4b6ee83.html
- date: '2026-05-25'
  title: Kodak Reports Fourth-Quarter and Full-Year 2025 ...
  url: https://www.businesswire.com/news/home/20260312377142/en/Kodak-Reports-Fourth-Quarter-and-Full-Year-2025-Financial-Results
- date: '2026-05-25'
  title: Kodak Reports Second-Quarter 2025 Financial Results
  url: https://www.kodak.com/en/company/press-release/q2-2025-financial-results/
- date: '2026-05-25'
  title: Kodak press-release
  url: https://www.silverfast.com/show/kodak-press-release/de.html
random_paper: 10
rate_limits:
- limit_count: 0
  name: Eastman Kodak Rate Limits
  slug: eastman-kodak-rate-limits
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 16.8
  provenance:
    conformance: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-07'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/eastman-kodak/refs/heads/main/screenshots/eastman-kodak-2026-06-20T180400.png
security:
- kind: domain-security
  name: Eastman Kodak Domain Security
  slug: eastman-kodak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eastman-kodak
tags:
- Printing
- Imaging
- Packaging
- Manufacturing
- Print Workflow
- Photography
- Advanced Materials
website: https://www.kodak.com/en/
---
