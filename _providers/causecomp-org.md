---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/causecomp-org/plans/causecomp-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/causecomp-org-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://www.causecomp.org/terms
- group: agent
  href: https://artifacts.apis.io/causecomp-org/llms/causecomp-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/causecomp-org-llms.txt
- group: auth
  href: https://artifacts.apis.io/causecomp-org/well-known/causecomp-org-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/causecomp-org-security.txt
- group: auth
  href: https://artifacts.apis.io/causecomp-org/well-known/causecomp-org-causecomp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/causecomp-org-causecomp-security.txt
- group: agent
  href: https://artifacts.apis.io/causecomp-org/well-known/causecomp-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/causecomp-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/causecomp-org/hosts/causecomp-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/causecomp-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/causecomp-org/vendors/causecomp-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/causecomp-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.causecomp.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.causecomp.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.causecomp.org/pricing
- group: start
  title: ''
  type: Login
  url: https://www.causecomp.org/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.causecomp.org/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://www.causecomp.org/guides/getting-started
- group: auth
  href: https://artifacts.apis.io/causecomp-org/security/causecomp-org-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/causecomp-org-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/causecomp-org/security/causecomp-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/causecomp-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.causecomp.org/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no machine-readable API contract was found.
  evidence:
  - status: 200
    url: https://www.causecomp.org/guides
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CauseComp provides nonprofit compensation benchmarks derived from IRS Form 990 filings and BLS wage data, offering percentile pay ranges and §4958 comparables for executive and workforce roles. The platform helps nonprofits understand market compensation standards and supports transparent salary planning.
image: https://www.causecomp.org/static/causecomp-og-card.png
layout: provider
modified: '2026-11-04'
name: CauseComp
nav: Providers
network: true
overview: 'CauseComp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Non-Profit, Compensation, Benchmarks, Data, and Transparency.


  CauseComp''s developer surface includes pricing, documentation, getting-started guide, and 14 more developer resources.'
plans:
- name: Causecomp Org Plans Pricing
  plan_count: 3
  slug: causecomp-org-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Causecomp Org Domain Security
  slug: causecomp-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Causecomp Org Vulnerability Disclosure
  slug: causecomp-org-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: causecomp-org
tags:
- Non-Profit
- Compensation
- Benchmarks
- Data
- Transparency
website: https://www.causecomp.org/
---
