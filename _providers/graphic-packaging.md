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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 8.8
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: Read-only HTTP JSON API serving Graphic Packaging International's open job requisitions from careers.graphicpkg.com. Four tools — search_jobs, get_job, list_departments and list_locations — are select
  name: Graphic Packaging Career Site Job Query API
  slug: graphic-packaging-career-site-job-query-api
artifact_total: 6
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/security/graphic-packaging-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graphic-packaging-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/graphic-packaging-international
- group: company
  title: ''
  type: Website
  url: https://www.graphicpkg.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.graphicpkg.com/sustainability/
- group: company
  title: ''
  type: Investors
  url: https://investors.graphicpkg.com/
- group: company
  title: ''
  type: Careers
  url: https://www.graphicpkg.com/careers/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/graphic-packaging-rules.yml
  title: ''
  type: Rules
  url: graphic-packaging-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.graphicpkg.com/feed/
- group: auth
  title: ''
  type: Security
  url: https://www.graphicpkg.com/disclosures-and-company-policies/vulnerability-disclosure-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/security/graphic-packaging-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/graphic-packaging-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.graphicpkg.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.graphicpkg.com/privacy-rights-policies/global-privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.graphicpkg.com/contact-us/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/conformance/graphic-packaging-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graphic-packaging-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/conformance/graphic-packaging-conformance.yml
  title: ''
  type: Compliance
  url: conformance/graphic-packaging-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/plans/graphic-packaging-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/graphic-packaging-plans-pricing.yml
created: '2026-03-21'
description: Graphic Packaging International is a Fortune 500 global manufacturer of sustainable, paperboard-based consumer packaging. Products include folding cartons, multipack cartons, foodservice packaging (cups, lids, to-go containers), microwave and ovenable packaging, paperboard canisters, and packaging machinery. Markets served include food, beverage, foodservice, household, personal care, healthcare, pharmaceuticals, pet care, beauty, and e-commerce. Graphic Packaging publishes no developer program, no API reference and no machine-readable contract; its digital surfaces for customers and suppliers (ODS order data, ACES, GPI Fiber Furnish Tracker and the Esko WebCenter artwork portal) all sit behind logins. The one unauthenticated JSON surface on a graphicpkg.com host is the careers site job query API, which is a tenant of the AppVault career-site platform rather than a Graphic Packaging product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphic-packaging.png
layout: provider
modified: '2026-09-12'
name: Graphic Packaging
nav: Providers
network: true
overview: 'Graphic Packaging publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Packaging, Paperboard, Sustainability, and Manufacturing.


  Graphic Packaging''s developer surface includes engineering blog, support, and 14 more developer resources.'
plans:
- name: Graphic Packaging Plans Pricing
  plan_count: 0
  slug: graphic-packaging-plans-pricing
press:
- date: '2026-05-25'
  title: Pomerantz LLP Brings Class Action Lawsuit Against ...
  url: https://natlawreview.com/press-releases/pomerantz-llp-brings-class-action-lawsuit-against-graphic-packaging-holding
- date: '2026-05-25'
  title: Graphic Packaging Holding Company (GPK) Q1 2026 ...
  url: https://seekingalpha.com/article/4898608-graphic-packaging-holding-company-gpk-q1-2026-earnings-call-transcript
- date: '2026-05-25'
  title: Graphic Packaging Holding Company (GPK) reports earnings
  url: https://qz.com/graphic-packaging-holding-company-gpk-reports-earning-1851761994
- date: '2026-05-25'
  title: Graphic Packaging Holding Company Appoints New ...
  url: https://www.prnewswire.com/news-releases/graphic-packaging-holding-company-appoints-new-investor-relations-and-treasury-leadership-302728165.html
- date: '2026-05-25'
  title: '10-K: Annual report [Section 13 and 15(d), not S-K Item 405]'
  url: https://investors.graphicpkg.com/sec-filings/all-sec-filings/content/0001408075-26-000009/gpk-20251231.htm
random_paper: 11
rate_limits:
- limit_count: 0
  name: Graphic Packaging Rate Limits
  slug: graphic-packaging-rate-limits
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 10.5
  previous_composite: 20.8
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/graphic-packaging/refs/heads/main/screenshots/graphic-packaging-2026-06-20T182327.png
security:
- kind: authentication
  name: Graphic Packaging Authentication
  slug: graphic-packaging-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Graphic Packaging Domain Security
  slug: graphic-packaging-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Graphic Packaging Vulnerability Disclosure
  slug: graphic-packaging-vulnerability-disclosure
  summary_line: disclosure policy published
slug: graphic-packaging
tags:
- Fortune 500
- Packaging
- Paperboard
- Sustainability
- Manufacturing
- Consumer Packaging
- Food Service
website: https://www.graphicpkg.com/
---
